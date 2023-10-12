from io import StringIO

from Bio import SeqIO


def parse_fasta_string(fasta_string):
    fasta_io = StringIO(fasta_string)

    records = SeqIO.parse(fasta_io, "fasta")

    return records


def get_dna_from_fasta(fasta_string):
    records = parse_fasta_string(fasta_string)

    dna_strings = [str(record.seq) for record in records]

    return dna_strings
