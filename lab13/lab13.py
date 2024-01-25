import os
import random
import time
import jpredapi
import re
from itertools import groupby


def generate_random_sequences(original_seq, result_length):
    result = []
    for i in range(result_length):
        seq_list = list(original_seq)
        random.shuffle(seq_list)
        result.append(''.join(seq_list))

    return result


def extract_job_id(text):
    pattern = r'jp_[\w\d]+'
    matches = re.findall(pattern, text)
    return matches[0] if matches else None


def submit_sequence_to_jpred(sequence):
    response = jpredapi.submit(mode="single", user_format="raw", seq=sequence)
    return extract_job_id(str(response.content))


def fetch_result_from_jpred(job_id):
    status = jpredapi.get_results(jobid=job_id, results_dir_path="jpred_sspred/results", extract=True)
    return status


def get_jpred_result_path(job_id):
    return f"jpred_sspred/results/{job_id}/{job_id}.jnet"


def await_jpred_result(job_id, max_retries=100, sleep_time=10):
    current_try = 0
    results_path = get_jpred_result_path(job_id)

    while current_try < max_retries:
        if os.path.exists(results_path):
            return
        else:
            fetch_result_from_jpred(job_id)
            current_try += 1
            time.sleep(sleep_time)


def get_jpred_prediction(job_id):
    results_path = get_jpred_result_path(job_id)
    with open(results_path, 'r') as file:
        lines = file.readlines()
        return lines[1].split(':')[1].replace(',', '')


def get_segment_lengths(secondary_structure):
    return [len(list(group)) for char, group in groupby(secondary_structure) if char in 'HE']


def get_avg_segment_length(secondary_structure):
    segment_lengths = get_segment_lengths(secondary_structure)
    return sum(segment_lengths) / len(segment_lengths) if segment_lengths else 0


def count_structure_elements(secondary_structure):
    return secondary_structure.count('H') + secondary_structure.count('E')


def verify_hypothesis(original_sequence, secondary_structure):
    original_count = count_structure_elements(secondary_structure)
    original_avg_length = get_avg_segment_length(secondary_structure)

    random_sequences_count = 6
    random_sequences = generate_random_sequences(original_sequence, random_sequences_count)

    true_count = 0

    for sequence in random_sequences:
        job_id = submit_sequence_to_jpred(sequence)
        await_jpred_result(job_id)
        prediction = get_jpred_prediction(job_id)
        pred_count = count_structure_elements(prediction)

        pred_avg_length = get_avg_segment_length(prediction)

        if pred_count < original_count or pred_avg_length < original_avg_length:
            print('Hypothesis confirmed')
            true_count += 1
        else:
            print('Hypothesis not confirmed')

        print(f'Original Secondary Structure Element Count: {original_count}')
        print(f'Predicted Secondary Structure Element Count: {pred_count}')
        print(f'Original Average Length of Each Secondary Structure Element: {original_avg_length}')
        print(f'Predicted Average Length of Each Secondary Structure Element: {pred_avg_length}')
        print('------------------------------')

    print(f'Hypothesis confirmed in {true_count} out of {random_sequences_count} cases')


if __name__ == '__main__':
    myoglobin_sequence = "MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKHGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISECIIQVLQSKHPGDFGADAQGAMNKALELFRKDMASNYKELGFQG"
    secondary_structure = "----HHHHHHHHHHHHHH---HHHHHHHHHHHHHHH-----------------------HHHHHHHHHHHHHHHHH------HHHHHHHHHHHHHH--------HHHHHHHHHHHHHHH------HHHHHHHHHHHHHHHHHHHHHHHHH----"

    verify_hypothesis(myoglobin_sequence, secondary_structure)
