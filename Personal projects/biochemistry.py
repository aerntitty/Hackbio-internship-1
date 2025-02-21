"""
Import both sift and foldx datasets; in both datasets, create a column specific_Protein_aa which will be
 a cantenation of the Protein and Amino_acid columns such that If you have 
 Protein A5A607 and Amino_acid E63D, you have specific_Protein_aa A5A607_E63D
Using the specific_Protein_aa column, merge sift and foldx dataset into one final dataframe.
According to the authors;
A SIFT Score below 0.05 is deleterious
A FoldX score greater than 2 kCal/mol is deleterious
Using the criteria above, Find all mutations that have a SIFT score below 0.05 and 
    FoldX Score above 2 (i.e: Mutations that affect both structure and function)
Study the amino acid substitution nomenclature
Investigate for the amino acid that has the most functional and structural impact
Hint: Using the amino acid column, find a way to select the first amino acid. Solution here
Generate a frequency table for all the amino acids
Using the amino frequency table above, generate a barplot and
     pie chart to represent the frequency of the amino acids.
Briefly describe the amino acid with the highest impact on protein structure and function
What can you say about the structural property and functional property
     of amino acids with more than 100 occurences.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

df1=pd.read_csv(r"Hackbio-internship-1-1\shift.csv")
df2=pd.read_csv(r"Hackbio-internship-1-1\foldX.csv")
df1["specific_Protein_aa"]=df1["Protein"]+"_"+df1["Amino_acid"]
df2["specific_Protein_aa"]=df2["Protein"]+"_"+df2["Amino_acid"]

print(df1.head(5))
print(df2.head(5))