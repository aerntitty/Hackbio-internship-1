sequences = ["ATG", "TGC", "CGA"]

def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

for seq1 in sequences:
    for seq2 in sequences:
        if seq1 != seq2:
            distance = hamming_distance(seq1, seq2)
            print(f"Hamming distance between {seq1} and {seq2} is {distance}")
