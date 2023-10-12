from utils.fasta_utils import parse_fasta_string


def get_highest_gc_content(fasta_string):
    records = parse_fasta_string(fasta_string)

    highest_gc_content = 0
    highest_gc_content_id = ''

    for record in records:
        gc_content = calculate_gc_content(record.seq)
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_gc_content_id = record.id

    return highest_gc_content_id, highest_gc_content


def calculate_gc_content(dna_string):
    gc_count = len([x for x in dna_string if x in ['G', 'C']])

    return gc_count / len(dna_string) * 100


if __name__ == '__main__':
    with open('../inputs/lab2/input_ex8.txt', 'r') as file:
        fasta_input = file.read()
    output = get_highest_gc_content(fasta_input)
    print(output)
