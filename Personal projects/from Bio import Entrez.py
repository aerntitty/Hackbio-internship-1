from Bio import Entrez

# Provide your email for NCBI's database
Entrez.email = "niyeh24@gmail.com"

# Fetch a record from NCBI
handle = Entrez.efetch(db="nucleotide", id="NM_001200", rettype="fasta", retmode="text")
sequence_data = handle.read()
print(sequence_data)
