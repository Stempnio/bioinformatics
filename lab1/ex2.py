def reverse_complement(dna_string):
    reversed_string = dna_string[::-1]
    complement = reversed_string.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()
    return complement
