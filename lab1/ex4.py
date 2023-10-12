from utils.codon_utils import codon_map


def get_protein_string(rna_string):
    codons = [rna_string[i: i + 3] for i in range(0, len(rna_string), 3)]
    result_list = [codon_map[x] for x in codons if codon_map[x] != 'Stop']
    return ''.join(result_list)
