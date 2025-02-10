#  FASTA File Parser
# Read a FASTA file (e.g., sequences.fasta) and store headers/sequences in a dictionary.

#For each sequence, calculate: 
# Length
#GC content

# Molecular weight (assume each base has a weight: A=313.2, T=304.2, C=289.2, G=329.2).

#Use lists to store multiple sequences and tuples to return results

with open("Personal projects\sequence.fasta","r") as file:
    lines=file.readlines()
    for line in lines:
        print(line.rstrip())
        print(len(line))