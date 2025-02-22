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

def main():

     
     """
      from this we see the lowest siftscore is 0 so any
      amino acid with sift score 0 has the most functional impact 
      And the highest foldx score is 67 so any amino acid with foldx score 67 has
      the most structural impact

     """

     #amino acid with the most functional and structural impact
     

     #extract the first amino acid from the amino_acid column
    

     #find the most impactful aa

     
    #create frequency table
    

     #plotting the frequency table
     

     #amino acids with more than 100 occurances
     


     
     
     

# merge sift and foldx dataset into one final dataframe
def merge_df(df1,df2):
     
#mutations that have a SIFT score below 0.05 and  FoldX Score above 2
def mutations(df):
     
#plotting the frequency table
def plot_freq_table(freq_table):
     

def pie_chart(freq_table):
     

main()
    