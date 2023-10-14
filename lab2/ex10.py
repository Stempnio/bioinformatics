from lab1.ex2 import reverse_complement
from utils.codon_utils import dna_codon_map, DNA_START_CODON
from utils.fasta_utils import get_dna_from_fasta


def get_translation_candidates(fasta_string):
    dna_strings = get_dna_from_fasta(fasta_string)

    dna_seq = dna_strings[0]

    frames = get_frames(dna_seq)

    candidates = []
    for frame in frames:
        candidates.extend(get_frame_candidates(frame))

    return set(candidates)


def get_frames(dna_seq):
    frames = []
    reverse_complement_seq = reverse_complement(dna_seq)

    for i in range(3):
        frames.append(get_frame(dna_seq, i))
        frames.append(get_frame(reverse_complement_seq, i))

    return frames


def get_frame(dna_seq, starting_index):
    return [dna_seq[i: i + 3] for i in range(starting_index, len(dna_seq), 3) if len(dna_seq[i: i + 3]) == 3]


def get_frame_candidates(frame):
    candidates = []
    for i, codon in enumerate(frame):
        if codon == DNA_START_CODON:
            current = dna_codon_map[codon]
            did_encounter_stop = False
            for _, x in enumerate(frame[i + 1:], i + 1):
                if dna_codon_map[x] != 'Stop':
                    current += dna_codon_map[x]
                else:
                    did_encounter_stop = True
                    break

            if did_encounter_stop:
                candidates.append(current)

    return candidates
