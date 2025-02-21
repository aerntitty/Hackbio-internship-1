from Bio.Blast import NCBIWWW
# Run a BLAST search for a given sequence
result_handle = NCBIWWW.qblast("blastn", "nt", "ATGCGTACCTGAC")

# Save the result
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

print("BLAST search completed and saved to my_blast.xml")