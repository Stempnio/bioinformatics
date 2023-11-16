from Bio import pairwise2
from Bio.Align.substitution_matrices import load


def align_sequences(seq1, seq2, gap_penalty):
    pam250 = load("PAM250")
    alignments = pairwise2.align.localds(seq1, seq2, pam250, gap_penalty, gap_penalty)
    start = alignments[0].start
    end = alignments[0].end

    score = alignments[0].score
    r = alignments[0].seqA[start:end].replace('-', '')
    u = alignments[0].seqB[start:end].replace('-', '')
    return score, r, u
