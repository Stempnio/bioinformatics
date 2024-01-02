import random
from typing import Tuple
import pylcs
from utils.fasta_utils import parse_fasta_string


def generate_reads_with_coverage(dna_sequence, output_file_path, read_length=200, coverage=5):
    num_reads = len(dna_sequence) * coverage // read_length

    reads = []
    for _ in range(num_reads):
        start_index = random.randint(0, len(dna_sequence) - read_length)
        read = dna_sequence[start_index:start_index + read_length]
        reads.append(read)

    save_reads_to_fasta(reads, output_file_path)


def save_reads_to_fasta(reads, file_path):
    with open(file_path, 'w') as fasta_file:
        for index, read in enumerate(reads, start=1):
            fasta_file.write(f">Read_{index}\n{read}\n")


def get_reads_from_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        fasta_string = fasta_file.read()

    records = parse_fasta_string(fasta_string)

    reads = [str(record.seq) for record in records]

    return reads


def greedy_sequence_assembly(reads_file_path):
    reads = get_reads_from_fasta(reads_file_path)

    while True:
        overlapped_reads, assembled_sequence, max_overlap = get_most_overlapped_reads(reads)

        if max_overlap == 0:
            return reads

        reads.append(assembled_sequence)
        reads.remove(overlapped_reads[0])
        reads.remove(overlapped_reads[1])

        if len(reads) == 1:
            return reads


def get_most_overlapped_reads(reads):
    max_overlap = 0
    overlapped_reads: Tuple[str, str] | None = None
    assembled_sequence = None

    for x in reads:
        for y in reads:
            if x != y:
                suffix_score = suffix_overlap_score(x, y)

                if suffix_score > max_overlap:
                    max_overlap = suffix_score
                    overlapped_reads = (x, y)
                    assembled_sequence = x + y[suffix_score:]

                prefix_score = prefix_overlap_score(x, y)
                if prefix_score > max_overlap:
                    max_overlap = prefix_score
                    overlapped_reads = (y, x)
                    assembled_sequence = y + x[prefix_score:]

    return overlapped_reads, assembled_sequence, max_overlap


def suffix_overlap_score(x, y):
    for i in range(len(x)):
        if x[i:] == y[:len(x) - i]:
            return len(x) - i
    return 0


def prefix_overlap_score(x, y):
    for i in range(len(x)):
        if x[:i] == y[-len(x) + i:]:
            return len(x) - i
    return 0


def read_chromosome_y(max_length=10000):
    chromosome_y_file_path = './chromosome_y.fa'
    with open(chromosome_y_file_path, 'r') as fasta_file:
        fasta_string = fasta_file.read()

    records = parse_fasta_string(fasta_string)

    record = next(records)

    sequence = str(record.seq).replace('N', '')

    return str(sequence)[:max_length]


def compare_sequences(original, assembled):
    lcs_length = pylcs.lcs(original, assembled)
    similarity_score = lcs_length / len(original)
    return lcs_length, similarity_score


if __name__ == '__main__':
    chromosome_y_fragment = read_chromosome_y(max_length=8000)

    reads_file_path = './reads.fa'

    generate_reads_with_coverage(chromosome_y_fragment, reads_file_path)

    contigs = greedy_sequence_assembly(reads_file_path)

    print(f'Number of contigs: {len(contigs)}')

    if len(contigs) == 1:
        print('Sequence assembled successfully')
        assembled_sequence = contigs[0]

        lcs_length, similarity_score = compare_sequences(chromosome_y_fragment, assembled_sequence)

        print(f'Longest common subsequence length: {lcs_length}')
        print(f'Similarity score: {similarity_score}')

    # c)
    # Wynik nie zgadza się z sekwencją wyjściową jednak jest do niej bardzo podobny.
    # Podobieństwo wyniosło około 96 %
