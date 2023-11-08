from Bio.Align import PairwiseAligner


def align_sequences(seq1, seq2, matrix, gap_penalty):
    aligner = PairwiseAligner()
    aligner.open_gap_score = -gap_penalty
    aligner.extend_gap_score = -gap_penalty
    aligner.substitution_matrix = matrix
    score = aligner.score(seq1, seq2)
    return score
