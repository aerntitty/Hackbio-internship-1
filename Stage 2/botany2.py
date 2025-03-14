"""

Task Code 2.3:
Botany and Plant Science
Have a look at this dataset
Some scientists are trying to engineer mutants for a crop to become resistant to a pesticide
They compared the metabolic response of the engineered mutants to the metabolic response of the wild type plants
The took readings after 8 and 24 hours
Your task
Calculate the difference in metabolic response (ΔM) between the DMSO treatment from the 24 hours treatment for the wild type and mutants
Generate a scatter plot showing the difference for ΔM for WT and Mutants
Fit a line that satifies a y-intercept of 0 and a slope of 1.
Using a residual cut off of your choice (calculated a the difference between the fitted line and each point) calculate the residual of each point on the scatter plot
Color metabolites that fall within +/- n of your residual grey. For example, if you have a cut-off of 0.3, color residual values that are within -0.3 and +0.3 grey
Color metabolites that fall outside this range salmon.
What are these metabolites. How do you explain the trends you see on either direction of the plot?
Pick any 6 metabolites that fall outside this range and generate a line plot that spans from their 0h treatment to their 8h and 24hr.
What can you say about the plots you see?

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
url="https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"

df=pd.read_csv(url, sep=r'\s+', engine='python' ,index_col=0)
print(df.head(9))

# difference in metabolic response (ΔM) between the DMSO treatment from the 24 hours treatment for the wild type and mutants
# Select relevant rows for wild_type

WT_dmso=df.loc['WT_DMSO_1']
WT_24h =df.loc["WT_pesticide_24h_1"]

# select relevan roles for the mutant

mutant_DMSO =df.loc["mutant_DMSO_1"]
mutant_24hrs= df.loc["mutant_pesticide_24h_1"]


# Compute ΔM for each condition
deltaM_wt=WT_24h - WT_dmso
deltaM_mut=mutant_24hrs-mutant_DMSO


#create a dataframe
change_df=pd.DataFrame({'wt_change':deltaM_wt, 'mut_change':deltaM_mut})
print(change_df.head())


#create residual 


# Define cutoff for residuals
cutoff = 0.3




# Compute residuals
change_df["residual"]=change_df['mut_change']- change_df['wt_change']

# Create the 'Outliers' column using np.where thank you Oluwafisayo ^y^
change_df['Outliers'] = np.where((-cutoff <= change_df['residual']) & (change_df['residual'] <= cutoff), 'not_outlier', 'outlier')

print(change_df.head())

# Assign colors based on outliers ^{}^

colurs={'outlier':'pink','not_outlier':'grey'}





# Identify outlier metabolites ^<>^
outliers= change_df.loc[change_df['Outliers']=='outlier'].index.to_list()
print('the outliers are:')
print(outliers)
print("*"*50)
# Identify non-outlier metabolites  ^>^

non_outliers= change_df.loc[change_df['Outliers']=='not_outlier'].index.to_list()
print('the non_outliers are:')
print(non_outliers)


# Generate a scatter plot showing the difference for ΔM for WT and Mutants using the colors as hues ^*^
plt.figure(figsize=(10,6))
sns.scatterplot(x='wt_change',y='mut_change',data=change_df,hue='Outliers',palette=colurs,edgecolor=None,alpha=0.7)


# Fit a y = x reference line (slope=1, intercept=0) ^_^
x_vals=change_df['wt_change']
plt.plot(x_vals,x_vals, color='cyan',linestyle="--",label='y=x=(slope=1)')

plt.xlabel('wt_change')
plt.ylabel('mut_change')
plt.title("scatter_plot of wt/mt")
plt.legend()
plt.show()


# Plot line plots for outlier metabolites ^%^
import random
outliers = random.sample(outliers, 6)

# Create a figure with subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 18)) 

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Plot each metabolite in a subplot
for i, metabolite in enumerate(outliers):
    axes[i].plot(df.index, df[metabolite], color='pink', marker='o', linestyle='--')
    axes[i].set_xlabel("Metabolic Conditions")
    axes[i].set_xticklabels(df.index,rotation=70,fontsize=5)
   
    axes[i].set_ylabel("Mutation")
    axes[i].set_title(f'Line plot for {metabolite}')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.subplots_adjust(top=0.95, bottom=0.10, left=0.05, right=0.95, hspace=0.4, wspace=0.4)  # Add padding for more space
plt.suptitle("Line Plots for Outlier Metabolites", fontsize=16)

plt.show()

print(f"The outliers are {outliers}")

"""
githhub rep :https://github.com/aerntitty/Hackbio-internship-1/blob/main/Stage%202/biochemistry.py
linkdein: 
https://www.linkedin.com/posts/nora-iyeh-bb94a32a3_hackbiointernship-datascience-bioinformatics-activity-7300354925174128640-C0ws?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEk4pP0ByfDyuSk1LhIThOUvbjX6eb_Nkrc
"""
