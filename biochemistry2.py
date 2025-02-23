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
     
     column1=['Protein','Amino_Acid', 'shift_Score']
     column2=['Protein','Amino_Acid', 'foldX_Score']
     
     df1=pd.read_csv(r"/Users/beckyiyeh/Documents/Hackbio-internship-1/Stage 2/shift.csv",sep=',',names= column1 , header=0)
     df2=pd.read_csv(r"/Users/beckyiyeh/Documents/Hackbio-internship-1/Stage 2/foldX.csv",sep=',',names= column2 , header=0)
     
     
     


     #create a column specific_Protein_aa
     df1["specific_Protein_aa"]=df1["Protein"]+"_"+df1["Amino_Acid"]
     df2["specific_Protein_aa"]=df2["Protein"]+"_"+df2["Amino_Acid"]
     
     
     
     #merge data on 
     merged_df=merged(df1,df2)
    
     merged_df.drop(
          ["Protein_y",
          "Amino_Acid_y"],
          axis= 1,
          inplace=True
     )
     
     merged_df.rename(columns=
                      {
                           "Protein_x":"Protein",
                           "Amino_Acid_x":"Amino_acid"
                      },inplace=True)
     print(merged_df.head())
     
     # mutated amino acids
     mutated_df=mutated(merged_df)
     aa=mutated_df.iloc[0,1]
     print(mutated_df.head())
     print(f"the most mutated amino acid is {aa}")
   
     

     #extract the first amino acid from the amino_acid column
     mutated_df["specific_aa"]=mutated_df["Amino_acid"].str[0]
     print(mutated_df.head())
     
     #find the most impactful aa
     
     counts=mutated_df["specific_aa"].value_counts()
     most_impactful_aa= counts.idxmax()
     print(f"most impactful amino acid is {most_impactful_aa}")
     
    #create frequency table
     cols=["Amino_acid","Frequency"]
     freq_table=counts.reset_index()
     freq_table.columns=cols
     print(freq_table.head())
    
     

     #plotting the frequency table
     bar_plot(freq_table)
     pie_plot(freq_table)
     
     

     #amino acids with more than 100 occurances
     aa_100_occurance=freq_table[freq_table['Frequency']> 100]
     amino_acid=aa_100_occurance["Amino_acid"].to_list
     print("amino acids with more than 100 occurnaces are")
     print(amino_acid)
    

     
     
     

# merge sift and foldx dataset into one final dataframe
def merged(df1,df2):
     merged_df=pd.merge(df1,df2,on="specific_Protein_aa")
     return merged_df

     
#mutations that have a SIFT score below 0.05 and  FoldX Score above 2

def mutated(df):
     muatation=df[(df["shift_Score"] < 0.05)&(df["foldX_Score"]>2)]
     mutation=muatation.sort_values("shift_Score",ascending=True)
     mutation=mutation.sort_values("foldX_Score",ascending=False)
     return mutation


     
#plotting the frequency table
def bar_plot(df):
     plt.figure(figsize=(16,6))
     sns.barplot(x=df["Amino_acid"],y=df["Frequency"])
     plt.title("Frequency plot of amino acid")
     plt.xlabel("Amino acid")
     plt.ylabel("Frequency")
     plt.show()
     
def pie_plot(df):
     plt.figure(figsize=(20,10))
     plt.pie(df["Frequency"],labels=df["Amino_acid"],autopct='%1.1f%%')
     plt.title("Frequency pieplot of amino acid")
     plt.show()
     
     


     


main()
    