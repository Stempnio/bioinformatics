from lab1.ex1 import count_symbols
from lab1.ex2 import reverse_complement
from lab1.ex3 import get_transcribed_rna
from lab1.ex4 import get_protein_string


def test_count_symbols():
    dna_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    expected = '20 12 17 21'
    assert count_symbols(dna_string) == expected


def test_reverse_complement():
    dna_string = 'AAAACCCGGT'
    expected = 'ACCGGGTTTT'
    assert reverse_complement(dna_string) == expected


def test_get_transcribed_rna():
    dna_string = 'GATGGAACTTGACTACGTAAATT'
    expected = 'GAUGGAACUUGACUACGUAAAUU'
    assert get_transcribed_rna(dna_string) == expected


def test_get_protein_string():
    rna_string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    expected = 'MAMAPRTEINSTRING'
    assert get_protein_string(rna_string) == expected
