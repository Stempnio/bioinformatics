from Bio import SeqIO, Entrez
from Bio.Blast import NCBIWWW, NCBIXML


def print_alignments(blast_record):
    for alignment in blast_record.alignments:
        print('Alignment----------------------------------')
        print('title:', alignment.title)
        print('length:', alignment.length)
        for hsp in alignment.hsps:
            print('HSP : ')
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')


def read_blast(sequence, program, database):
    result_handle = NCBIWWW.qblast(program=program,
                                   database=database,
                                   sequence=sequence,
                                   hitlist_size=1)
    blast_records = NCBIXML.parse(result_handle)
    blast_record = next(blast_records)

    print_alignments(blast_record)


def fetch_id(term):
    Entrez.email = 'jakub.stepien@student.uj.edu.pl'
    handle = Entrez.esearch(db="gene", term=term)
    result = Entrez.read(handle)
    id = str(result["IdList"][0])
    return id


def fetch_seq_by_id(id):
    Entrez.email = 'jakub.stepien@student.uj.edu.pl'
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    return record.seq


def fetch_rhodopsin_seq():
    term = "NM_000539.3"
    id = fetch_id(term)
    return fetch_seq_by_id(id)


def read_seq_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().replace('\n', '')


if __name__ == '__main__':
    print('*Zadanie 3*')
    ex3_seq = read_seq_from_file('ex3_seq.txt')
    read_blast(ex3_seq, "blastn", "nt")
    print('Pochodzi z genu BRCA1')

    print('*Zadanie 4*')
    ex4_seq = read_seq_from_file('ex4_seq.txt')
    read_blast(ex4_seq, "blastp", "nr")
    print('CNR1 - Cannabinoid receptor 1')
    print('Rola białka:')
    print('odpowiada za kontrolę apetytu oraz pamięć i przetwarzanie emocji')
    print('Występuje na chromosomie 6')
    print('Mandrillus leucophaeus - Mandryl równikowy')
    print('Theropithecus gelada - Dżelada brunatna')
    print('Rhinopithecus roxellana - Rokselana złocista')
    print('Symphalangus syndactylus - Siamang wielki')
    print('Pan troglodytes - Szympans zwyczajny')

    print('*Zadanie 5*')
    rhodopsin_seq = fetch_rhodopsin_seq()
    print('Rhodopsin sequence: ', rhodopsin_seq)
    read_blast(rhodopsin_seq, "tblastx", 'nt')
