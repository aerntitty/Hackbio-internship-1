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

     column_df1=['Protein','Amino_Acid','sift_Score']
     column_df2=['Protein','Amino_Acid','foldX_Score']

     df1=pd.read_csv(r"Hackbio-internship-1-1\shift.csv",sep=',',names=column_df1,header=0)
     df2=pd.read_csv(r"Hackbio-internship-1-1\foldX.csv",sep=',',names=column_df2,header=0)

     #create a column specific_Protein_aa
     df1["specific_Protein_aa"]=df1["Protein"]+"_"+df1["Amino_Acid"]
     df2["specific_Protein_aa"]=df2["Protein"]+"_"+df2["Amino_Acid"]
     final_df=merge_df(df1,df2)
     final_df.drop(["Protein_y","Amino_Acid_y"],axis=1,inplace=True)
     final_df.rename(
          columns={
               "Protein_x":"Protein",
               "Amino_Acid_x":"Amino_Acid"
          },
          inplace=True   
     )
     print (final_df.head())
     # mutated amino acids 
     mutations_df=mutations(final_df)
     print(mutations_df.head())
     print(mutations_df.describe()) 

     
  
     #amino acid with the most functional and structural impact
     amino_acid=mutations_df.iloc[0,1]
     print(f"The amino acid with the most functional and structural impact is {amino_acid}")

     #extract the first amino acid from the amino_acid column
     mutations_df["main_aa"]=mutations_df['Amino_Acid'].str[0]

     #find the most impactful aa

     counts=mutations_df["main_aa"].value_counts()
     most_impactfulaa=counts.idxmax()
     print(f"The most impactful amino acid is {most_impactfulaa}")

     cols=['Aminoacid','Count']
     freq_table=counts.reset_index()
     freq_table.columns=cols
     print(freq_table)

     #plotting the frequency table
     plot_freq_table(freq_table)
     pie_chart(freq_table)


     #amino acids with more than 100 occurances

     aa_100=freq_table[freq_table["Count"]>100]
     amino_acids=aa_100["Aminoacid"].tolist()
     print(f"The amino acids with more than 100 occurences are {amino_acids}")

     
     
     

# merge sift and foldx dataset into one final dataframe
def merge_df(df1,df2):
     final_df=pd.merge(df1,df2, on="specific_Protein_aa")
     return final_df
#mutations that have a SIFT score below 0.05 and  FoldX Score above 2
def mutations(df):
     mutations=df[(df["sift_Score"]<0.05) & (df["foldX_Score"]>2)]
     #sort the mutations to see which one is way lower than 0.05 and way higher than 2
     mutations=mutations.sort_values(by="sift_Score",ascending=True)
     mutations=mutations.sort_values(by="foldX_Score",ascending=False)
     return mutations
#plotting the frequency table
def plot_freq_table(freq_table):
     plt.figure(figsize=(10,5))
     sns.barplot(x=freq_table['Aminoacid'],y=freq_table['Count'])
     plt.title("Frequency of amino acids")
     plt.xlabel("Amino acids")
     plt.ylabel("Frequency")
     plt.xticks(rotation=45)
     plt.show()

def pie_chart(freq_table):
     plt.figure(figsize=(12,12))
     plt.pie(freq_table['Count'],labels=freq_table['Aminoacid'],autopct='%1.1f%%')
     plt.title("Frequency of amino acids")
     plt.show()

main()

"""

github: https://github.com/aerntitty/Hackbio-internship-1/blob/main/Stage%202/biochemistry.py
linkedin:https://www.linkedin.com/posts/nora-iyeh-bb94a32a3_hackbiointernship-bioinformatics-proteinengineering-activity-7300348819769028608-Yv77?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEk4pP0ByfDyuSk1LhIThOUvbjX6eb_Nkrc
"""
    

    
