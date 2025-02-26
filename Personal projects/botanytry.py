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
wt_dmso=df.loc["WT_DMSO_1"]
wt_24hrs=df.loc["WT_pesticide_24h_1"]


# select relevan roles for the mutant
mt_dmso=df.loc["mutant_DMSO_1"]
mt_24hrs=df.loc["mutant_pesticide_24h_1"]



# Compute ΔM for each condition
delta_wt=wt_24hrs-wt_dmso
delta_mt=mt_24hrs-mt_dmso


#create a dataframe
final_df=pd.DataFrame({"delta_wt": delta_wt, "delta_mt" : delta_mt})






# Define cutoff for residuals
cutoff = 0.3




# Compute residuals
final_df["Residuals"]=final_df['delta_wt']-final_df['delta_mt']


# Create the 'Outliers' column using np.where thank you Oluwafisayo ^y^
final_df["Outliers"]=np.where((-cutoff<=final_df["Residuals"])&(final_df["Residuals"]<= cutoff),"non_outlier","outlier")
print(final_df.head(9))








# Identify outlier metabolites ^<>^
outliers=final_df.loc[final_df['Outliers']=="outlier"].index.to_list()
print("the outliers are :")
print(outliers)

# Identify non-outlier metabolites  ^>^

non_outliers=final_df.loc[final_df['Outliers']=="non_outlier"].index.to_list()
print("the non_outliers are :")
print(non_outliers)




# Generate a scatter plot showing the difference for ΔM for WT and Mutants using the colors as hues ^*^

# Assign colors based on outliers ^{}^
colours=({"outlier":"pink","non_outlier":"grey"})
plt.figure(figsize=(16,6))
sns.scatterplot(data=final_df,x="delta_wt",y="delta_mt",hue="Outliers",palette=colours,edgecolor=None,alpha=0.7)





# Fit a y = x reference line (slope=1, intercept=0) ^_^
x_val=final_df["delta_wt"]
plt.plot(x_val,x_val,linestyle="--",color="black",label="y=x=(slope1)")
plt.title("ΔM for WT and Mutants")
plt.xlabel("Wildtype")
plt.ylabel( "Mutated_Type")
plt.legend()
plt.show()


# Plot line plots for outlier metabolites ^%^

# Select 6 random metabolites for fairness ps i couldnt just pick six i am just a girl lmalone ^~^
import random
outliers = random.sample(outliers, 6)

# Create a figure with subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 18))  # Adjust the number of rows and columns as needed

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
plt.subplots_adjust(top=0.95, bottom=0.10, left=0.05, right=0.95, hspace=0.4, wspace=0.4)  # Add padding
plt.suptitle("Line Plots for Outlier Metabolites", fontsize=16)
# Show the figure with all subplots
plt.show()

print(f"The outliers are {outliers}")