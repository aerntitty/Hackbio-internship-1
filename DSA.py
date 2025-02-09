# DNA SEQUENCE ANALYZER
# TO GET THE GC PERCENTAGE AND COUNT OF ALL NUCLEOTIDE BASES PRESENT IN A DNA SEQ
# AND TO GET THE REVERSE COMPLEMENT STRAND

def main():
    seq="ATGCGATAGCTAGCTAGCT"
    A_count, T_count, C_count, G_count = seq_counter(seq)
    gc_percentage=((G_count+C_count)/len(seq))*100
    print(f"Nucleotide Count : ['A' : {A_count},'T':{T_count},'C':{C_count},'G':{G_count}]")
    print(f"GC Content : {gc_percentage :.2f}%")
    

    print("Reverse Complement:", reverse_complement(seq))

def seq_counter(s):
    A_count =s.count("A")
    T_count=s.count("T")
    C_count= s.count("C")
    G_count=s.count("G")
    
    return A_count,T_count,C_count,G_count 

def reverse_complement(sequence):
    # Create a dictionary to map nucleotides to their complements
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the sequence and complement each nucleotide
    reversed_seq = sequence[::-1]
    rc = ''.join([complement[base] for base in reversed_seq])
    
    return rc


main()
