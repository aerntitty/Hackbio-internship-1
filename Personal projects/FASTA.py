#  FASTA File Parser
# Read a FASTA file (e.g., sequences.fasta) and store headers/sequences in a dictionary.

#For each sequence, calculate: 
# Length
#GC content

# Molecular weight (assume each base has a weight: A=313.2, T=304.2, C=289.2, G=329.2).

#Use lists to store multiple sequences and tuples to return results
From DSA import seq_counter

with open("Personal projects\sequence.fasta","r") as file:
    lines=file.readlines()
    for line in lines:
        print(len(line))
        A_count, T_count, C_count, G_count = seq_counter(line)
         gc_percentage=((G_count+C_count)/len(seq))*100
        print(f"Nucleotide Count : ['A' : {A_count},'T':{T_count},'C':{C_count},'G':{G_count}]")
        print(f"GC Content : {gc_percentage :.2f}%")
        

