from utils.fasta_utils import parse_fasta_string


def get_string_graph(fasta_string, k=None):
    records = parse_fasta_string(fasta_string)

    results = []

    for i, x in enumerate(records):
        inner_records = parse_fasta_string(fasta_string)
        for _, y in enumerate(inner_records, i + 1):
            x_string = str(x.seq)
            y_string = str(y.seq)

            if x_string != y_string and is_overlap(x_string, y_string, k):
                results.append((x.id, y.id))

    return results


def is_overlap(string1, string2, k=None):
    if k is not None:
        return string1[-k:] == string2[:k]

    max_overlap_len = min(len(string1), len(string2))

    for i in range(max_overlap_len, 0, -1):
        if string1[-i:] == string2[:i]:
            return True

    return False


def format_string_graph(edges):
    result = ""
    for start, end in edges:
        result += f'{start} {end}\n'

    return result
