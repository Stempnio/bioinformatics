def get_substring_indices(string, substring):
    indices = []

    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            indices.append(i + 1)
    return indices
