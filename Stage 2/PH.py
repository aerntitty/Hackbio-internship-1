"""
Public Health
NHANES is a program run by the CDC to assess the health and nutritional status of
 adults and children in the US. It combines survey questions and physical examinations,
  including medical and physiological measurements and laboratory tests, and examines a representative sample of about 
  5,000 people each year. The data is used to determine the prevalence of diseases and risk factors, establish national standards, 
  and support epidemiology studies and health sciences research. This information helps to develop public health policy, design health
   programs and services, and expand the nation's health knowledge.
Dataset here
Data Dictionary
Tasks:
Process all NA (either by deleting or by converting to zero) {Hard :fire:}
Visualize the distribution of BMI, Weight, Weight in pounds (weight *2.2) and Age with an histogram.
What’s the mean 60-second pulse rate for all participants in the data?
73.63382
What’s the range of values for diastolic blood pressure in all participants? (Hint: see help for min(), max()).
0-116
What’s the variance and standard deviation for income among all participants?
Visualize the relationship between weight and height ?
Color the points by
gender
diabetes
smoking status
Conduct t-test between the following variables and make conclusions on the relationship between them based on P-Value
Age and Gender
BMI and Diabetes
Alcohol Year and Relationship Status

"""
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv(r"Stage 2\nhanes.csv",sep=',',index_col=0)
#check for null values
print("WE WILL BEGIN CHECKING FOR AND CORRECTING NULL VALUES")

print("                                                                                                                                                                                              ")

print(df.head())
print(df.isnull().sum())
#Handling null values i wnated to just drop them before but it will affect final result 
df=df.fillna(method='ffill')


df=df.fillna({'Education':'High School','MaritalStatus' : 'NeverMarried ', 'RelationshipStatus':'Single','Work' :'None'})
df=df.fillna(0)
print(df.isnull().sum()) # FINAL  cross check to see if they are all gone

#now lets print out our dataframe 
print(df.head(2))
print("                                                                                                                                                                                              ")
print("NOW FOR A VERY NOT SO PREETY HISTOGRAMS")

print("                                                                                                                                                                                              ")


#Visualize the distribution of BMI, Weight, Weight in pounds (weight *2.2) and Age with an histogram.
fig, ax = plt.subplots(2,2, figsize=(10,10))
sns.histplot(df['BMI'], ax=ax[0,0])
ax[0,0].set_title('BMI Distribution')
sns.histplot(df['Weight'], ax=ax[0,1])
ax[0,1].set_title('Weight Distribution')    
sns.histplot(df['Weight']*2.2, ax=ax[1,0])
ax[1,0].set_title('Weight in Pounds Distribution')
sns.histplot(df['Age'], ax=ax[1,1])
ax[1,1].set_title('Age Distribution')
plt.show()

print("                                                                                                                                                                                              ")


#What’s the mean 60-second pulse rate for all participants in the data?
print("The mean 60-second pulse rate for all participants in the data is: ")
print(df['Pulse'].mean())
print('*'*50)
print("                                                                                                                                                                                              ")


#what is the diastolic blood pressure range 

max_BPDia= df['BPDia'].max() # we first get the mas because you know range is max - min i definently knew that and did not just googleit
min_BPDia=df['BPDia'].min() # and now the min
print(f'the maximum diastolic blood pressure is {max_BPDia} and the minimum is {min_BPDia}' )
range_BPDia=max_BPDia-min_BPDia
print(f"so the range of diastolic blood pressure is {range_BPDia}")
print('*' *50)
print("                                                                                                                                                                                              ")


# What’s the variance and standard deviation for income among all participants
income_varience=df["Income"].var()
income_std=df['Income'].std()
print(f'the varience and standard deviation of income all our participants was {income_varience:.2f} and {income_std:.2f} respectively ')
print('*'*50)
print("                                                                                         ")


#visualize the relationship between weight and height color using scatter plot

print("WAIT FOR ALL THE PLOTS ^^")
print("                                                                                                                                                                                              ")


#with gender 
gender_palette = {'male': 'blue', 'female': 'red'}
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Weight', y='Height', hue='Gender', palette=gender_palette, alpha=0.7)
plt.title('Relationship between Weight and Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(title='Gender')
plt.show()

# with diabetes

Diabetes_palette = {'No': 'blue', 'Yes': 'red'}
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Weight', y='Height', hue='Diabetes', palette=Diabetes_palette, alpha=0.7)
plt.title('Relationship between Weight and Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(title='Diabetes')
plt.show()


#with smoking statues

Smoking_palette = {'Former': 'blue', 'Current': 'red','Never':'green'}
df= df.replace({'SmokingStatus':{0 : 'Never'}})
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Weight', y='Height', hue='SmokingStatus', palette=Smoking_palette, alpha=0.7)
plt.title('Relationship between Weight and Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(title='SmokingStatus')
plt.show()

print("T-TEST TIME")



# Perform t-test between Age and Gender
t_test_age_gender, p_value_age_gender = stats.ttest_ind(df[df['Gender'] == 'male']['Age'], df[df['Gender'] == 'female']['Age'])
print(f"T-test between Age and Gender: t-value = {t_test_age_gender:.2f}, p-value = {p_value_age_gender:.2f}")

# Perform t-test between BMI and Diabetes
t_test_bmi_diabetes, p_value_bmi_diabetes = stats.ttest_ind(df[df['Diabetes'] == 'Yes']['BMI'], df[df['Diabetes'] == 'No']['BMI'])
print(f"T-test between BMI and Diabetes: t-value = {t_test_bmi_diabetes:.2f}, p-value = {p_value_bmi_diabetes:.2f}")

#Perform t-test between Alcohol Year and Relationship Status

t_test_rs ,p_value_rs= stats.ttest_ind(df[df["RelationshipStatus"]=='Committed']["AlcoholYear"], df[df["RelationshipStatus"]=='Single']["AlcoholYear"])
print(f'T-test between RelationshipStatus and Alcohol year: t-value = {t_test_rs:.2f}, p-value = {p_value_rs:.2f}"')

"""
github linkfor task: https://github.com/aerntitty/Hackbio-internship-1/blob/main/Stage%202/PH.py
linkedein post:https://www.linkedin.com/posts/nora-iyeh-bb94a32a3_hackbiointernship-datascience-publichealth-activity-7300340943931518976-f-9x?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEk4pP0ByfDyuSk1LhIThOUvbjX6eb_Nkrc 



"""
