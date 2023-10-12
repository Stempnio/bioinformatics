from utils.fasta_utils import get_dna_from_fasta


def transition_transvertion_ration(fasta_string):
    dna_strings = get_dna_from_fasta(fasta_string)

    transitions = 0
    transversions = 0

    strings_zip = zip(list(dna_strings[0]), list(dna_strings[1]))

    for x, y in strings_zip:
        if x != y:
            if x + y in ['AG', 'GA', 'CT', 'TC']:
                transitions += 1
            else:
                transversions += 1

    if transversions == 0:
        return 0

    return transitions / transversions
