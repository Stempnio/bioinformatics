from Bio import Entrez, SeqIO

Entrez.email = "jakub.stepien@student.uj.edu.pl"


def search_brca1_gene():
    handle = Entrez.esearch(db="gene",
                            term="Homo sapiens[orgn] AND BRCA1[Gene Name]",
                            retmax=10)
    result = Entrez.read(handle)
    handle.close()
    return result["IdList"]


def print_gene_summary_info(gene_info):
    print(
        f'Name: {gene_info["Name"]}, Chromosome: {gene_info["Chromosome"]}, MapLocation: {gene_info["MapLocation"]}, '
        f'Description: {gene_info["Description"]}')


def get_gene_summary(gene_id, db):
    handle = Entrez.esummary(db=db, id=gene_id)
    result = Entrez.read(handle)
    handle.close()
    return result


def get_related_protein_ids(gene_id, db):
    handle = Entrez.elink(dbfrom="gene", db=db, id=gene_id)
    result = Entrez.read(handle)
    handle.close()
    protein_ids = [link["Id"] for link in result[0]["LinkSetDb"][0]["Link"]]
    return protein_ids


def print_omim_record_titles(gene_id):
    db = "omim"
    omim_ids = get_related_protein_ids(gene_id, db)
    for omim_id in omim_ids:
        summary = get_gene_summary(omim_id, db)
        print(f'Title: {summary[0]["Title"]}')


def find_brca1_mutations(brca1_id):
    handle = Entrez.elink(dbfrom="gene", db="snp", id=brca1_id, term="Homo sapiens")
    result = Entrez.read(handle)
    mutations = result[0]["LinkSetDb"][0]["Link"]
    print(f"Mutations count: {len(mutations)}")

    mut_range = min(50, len(mutations))

    for i in range(mut_range):
        mut_id = mutations[i]['Id']
        summary = get_gene_summary(mut_id, "snp")["DocumentSummarySet"]["DocumentSummary"][0]
        print(
            f"SNP_ID: {summary['SNP_ID']}, SNP_CLASS: {summary['SNP_CLASS']}, GENE: {summary['GENES']}, CONTIGPOS: {summary['CHRPOS']}")


def fetch_record(protein_id, db, format="genbank", rettype="gb"):
    handle = Entrez.efetch(db=db, id=protein_id, rettype=rettype, retmode="text")
    record = SeqIO.read(handle, format)
    handle.close()
    return record


def main():
    # Exercise 1,2
    gene_ids = search_brca1_gene()

    brca1_id = ""

    for gene_id in gene_ids:
        summary = get_gene_summary(gene_id, "gene")["DocumentSummarySet"]["DocumentSummary"][0]
        if summary["Name"] == "BRCA1":
            brca1_id = gene_id
        print_gene_summary_info(summary)

    # Exercise 3
    print_omim_record_titles(brca1_id)

    # Exercise 4
    related_ids = get_related_protein_ids(brca1_id, "protein")
    print(f"Related protein ids: {related_ids}")

    # Exercise 5
    protein_id = "121949022"
    protein_record = fetch_record(protein_id=protein_id, db="protein")

    print(f"name: {protein_record.name}, seq: {protein_record.seq}")

    # Exercise 6
    find_brca1_mutations(brca1_id)


if __name__ == "__main__":
    main()
