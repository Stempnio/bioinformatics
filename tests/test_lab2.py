import pytest

from lab2.ex5 import calculate_hamming_distance
from lab2.ex6 import longest_common_substring
from lab2.ex7 import transition_transvertion_ration
from lab2.ex8 import get_highest_gc_content


def test_hamming_distance():
    first_string = 'GAGCCTACTAACGGGAT'
    second_string = 'CATCGTAATGACGGCCT'
    expected = 7
    output = calculate_hamming_distance(first_string, second_string)
    assert output == expected


def test_common_strings():
    with open('inputs/lab2/test_input_ex6.txt', 'r') as file:
        fasta_input = file.read()
    output = longest_common_substring(fasta_input)
    expected = ['AC', 'AT', 'CA', 'TA']
    assert output in expected


def test_transition_transvertion_ratio():
    with open('inputs/lab2/test_input_ex7.txt', 'r') as file:
        fasta_input = file.read()
    output = transition_transvertion_ration(fasta_input)
    expected = 1.21428571429
    assert expected == pytest.approx(output)


def test_highest_gc_content():
    with open('inputs/lab2/test_input_ex8.txt', 'r') as file:
        fasta_input = file.read()
    output = get_highest_gc_content(fasta_input)
    expected = ('Rosalind_0808', 60.919540)
    assert expected == pytest.approx(output)
