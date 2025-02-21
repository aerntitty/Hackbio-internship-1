from Bio import SeqIO

# Read a FASTA file
for record in SeqIO.parse("Hackbio-internship-1-1\Personal projects\sequence.fasta", "fasta"):
    print(f"ID: {record.id}")
    print(f"Sequence: {record.seq}")
    print(f"Length: {len(record)}")