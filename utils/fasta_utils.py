from io import StringIO

from Bio import SeqIO


def parse_fasta_string(fasta_string):
    fasta_io = StringIO(fasta_string)

    records = SeqIO.parse(fasta_io, "fasta")

    dna_strings = [str(record.seq) for record in records]

    return dna_strings
