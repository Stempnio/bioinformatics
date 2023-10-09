def count_symbols(dna_string):
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    return f'{a_count} {c_count} {g_count} {t_count}'
