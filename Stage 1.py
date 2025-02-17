#Write a function for translating DNA to protein
#Write a function that simulates and generates a logistic population growth curve. Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase [See population curve here] . Most living populations follow a logistic population growth. Therefore, your growth curve can be: Population Size vs Time, Cell density vs Time, OD vs Time, CFU vs Time, etc
#Using your function, generate a dataframe with 100 different growth curves
#Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
#Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

def dna_to_protein(dna):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein=''
    for i in range(0,len(dna),3):
        Codon=dna[i:i+3]
        protein += codon_table[Codon]
    return protein
sequence='AGCTAGCTAGCT'
protein=dna_to_protein(sequence)
print(protein)


import math

def logistic_growth(time, P0, K, r, lag_phase, exp_phase):
    population = []
    for t in time:
        if t < lag_phase:
            population.append(P0)
        else:
            P_t = K / (1 + ((K - P0) / P0) * math.exp(-r * (t - lag_phase)))
            population.append(P_t)
    return population

test_time = list(range(0, 100, 1))
test_population = logistic_growth(test_time, 1, 100, 0.2, 5, 15)
print(f"the first 10 values of the population are {test_population[:10]} ")  

# Generate 100 different growth curves
data = []
time = list(range(0, 100, 1))
for i in range(100):
    P0_values = [1, 2, 3, 4, 5] # Different initial population sizes
    K_values = [60, 70, 80, 90, 100]
    r_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    lag_phase_values = [5, 7, 9, 11, 13]
    exp_phase_values = [20, 25, 30, 35, 40]

    index = i % len(P0_values)  # Cycle through values
    P0 = P0_values[index]
    K = K_values[index]
    r = r_values[index]
    lag_phase = lag_phase_values[index]
    exp_phase = exp_phase_values[index]
    growth = logistic_growth(time, P0, K, r, lag_phase, exp_phase)
    for t, population in zip(time, growth):
        data.append((i, t, population))

import pandas as pd
df = pd.DataFrame(data, columns=["Curve_ID", "Time", "Population"])
print("First few rows of the data frame:")
print(df.head(20))






def time_to_80_percent_max(time, population, K):
    threshold = 0.8 * K
    for i, pop in enumerate(population):
        if pop >= threshold:
            return time[i]
    return None
test_time_to_80 = time_to_80_percent_max(test_time, test_population, 100)
print("time_to_80_percent_max function:")
print(f"{test_time_to_80}s to reach 80% of max population")




def hamming_distance(name1, name2):
    if len(name1) != len(name2):
        raise ValueError("Sequences must be of equal length")
    return sum(1 for a, b in zip(name1, name2) if a != b)

hd= hamming_distance('nora','iyeh') # type: ignore
print (hd)
    
 
