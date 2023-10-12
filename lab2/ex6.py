from io import StringIO

from Bio import SeqIO


def get_all_substrings(input_string):
    result = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            result.append(input_string[i:j])
    return result


def longest_common_substring(fasta_string):
    fasta_io = StringIO(fasta_string)

    records = SeqIO.parse(fasta_io, "fasta")

    dna_strings = [str(record.seq) for record in records]

    first_string = dna_strings[0]
    substrings = get_all_substrings(first_string)

    longest = substrings[0]

    for substring in substrings:
        substring_len = len(substring)
        is_in_all = True
        for string in dna_strings:
            if substring not in string:
                is_in_all = False
                break

        if is_in_all and substring_len > len(longest):
            longest = substring

    return longest
