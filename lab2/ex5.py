def calculate_hamming_distance(dna_string_s, dna_string_t):
    strings = zip(list(dna_string_s), list(dna_string_t))
    count = [(x, y) for x, y in strings if x != y]
    return len(count)
