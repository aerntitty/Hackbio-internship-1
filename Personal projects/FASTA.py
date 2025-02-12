#  FASTA File Parser
# Read a FASTA file (e.g., sequences.fasta) and store headers/sequences in a dictionary.

# For each sequence, calculate: 
# Length
# GC content
# Molecular weight (assume each base has a weight: A=313.2, T=304.2, C=289.2, G=329.2).

# Use lists to store multiple sequences and tuples to return results


def parse_fasta(file_path):
    with open(file_path, "r") as file:
        sequences = {}
        header = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                header = line[1:]
                sequences[header] = ""
            else:
                if header:
                    sequences[header] += line
    return sequences

def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if sequence else 0

def calculate_molecular_weight(sequence):
    base_weights = {"A": 313.2, "T": 304.2, "C": 289.2, "G": 329.2}
    total_weight = 0
    for base in sequence:
        if base not in base_weights:
            raise ValueError(f"Invalid base found in sequence: {base}")
        total_weight += base_weights[base]
    return total_weight

def seq_counter(s):
    A_count =s.count("A")
    T_count=s.count("T")
    C_count= s.count("C")
    G_count=s.count("G")
    
    return A_count,T_count,C_count,G_count 


def analyze_sequences(file_path):
    sequences = parse_fasta(file_path)
    results = []
    for header, sequence in sequences.items():
        length = len(sequence)
        gc_content = calculate_gc_content(sequence)
        molecular_weight = calculate_molecular_weight(sequence)
        A_count, T_count, C_count, G_count = seq_counter(sequence)
        results.append((header, length, gc_content,A_count,C_count,G_count,T_count,molecular_weight))
    return results


file_path = "Personal projects\sequence.fasta"  
analysis_results = analyze_sequences(file_path)

for result in analysis_results:
    print(f"Header: {result[0]}")
    print(f"Length: {result[1]}")
    print(f"GC Content: {result[2]:.2f}%")
    print:(f"A base count : {result[3]}")
    print:(f"C base count : {result[4]}")
    print:(f"G base count : {result[5]}")
    print:(f"T base count : {result[6]}")
    print(f"Molecular Weight: {result[7]:.2f}")
    print("you did it bioinformatician")