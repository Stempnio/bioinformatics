from lab2.ex5 import calculate_hamming_distance
from lab2.ex6 import longest_common_substring


def test_hamming_distance():
    first_string = 'GAGCCTACTAACGGGAT'
    second_string = 'CATCGTAATGACGGCCT'
    expected = 7
    output = calculate_hamming_distance(first_string, second_string)
    assert output == expected


def test_common_strings():
    with open('inputs/lab2/test_input_ex5.txt', 'r') as file:
        fasta_input = file.read()
    output = longest_common_substring(fasta_input)
    expected = ['AC', 'AT', 'CA', 'TA']
    assert output in expected
