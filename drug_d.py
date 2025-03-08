import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Step 1: Load the Dataset
url = "https://github.com/HackBio-Internship/2025_project_collection/raw/refs/heads/main/Python/Dataset/drug_class_struct.txt"
df = pd.read_csv(url, sep="\t")  

# Step 2: Explore the Data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())  # Check for missing values

# Drop 'ID' column
df = df.drop(columns=['ID'])

# Convert object columns to numeric
obj_columns = ['SMILES', 'target']
df[obj_columns] = df[obj_columns].apply(pd.to_numeric, errors='coerce')

# Fill missing values with 0
df = df.fillna(0)


# Step 3: Identify Chemical Features
features = df.drop(columns=["score"])  # "score" is the docking score
score = df["score"]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 4: Perform PCA
pca = PCA(n_components=2)  
pca_features = pca.fit_transform(features_scaled)
df_pca = pd.DataFrame(pca_features, columns=["PC1", "PC2"])
df_pca["score"] = score

# Step 5: Apply K-Means Clustering

# Applying K-Means Clustering and Silhouette Analysis to get best k value
silhouette_scores = []
K_range = range(2, 10)  # Trying k from 2 to 9
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(features_scaled)
    score = silhouette_score(features_scaled, labels)
    silhouette_scores.append(score)

# Choose the best k (highest silhouette score)
best_k = K_range[np.argmax(silhouette_scores)]
print(f"Optimal number of clusters: {best_k}")


num_clusters = best_k 
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df_pca["cluster"] = kmeans.fit_predict(pca_features)
df["cluster"] = kmeans.fit_predict(features_scaled)

# Step 6: Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="cluster", palette="viridis", alpha=0.7, edgecolor="k")
plt.legend(title="Cluster")
plt.title("Chemical Space Representation with K-Means Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df_pca["PC1"], df_pca["PC2"], c=df_pca["score"], cmap="viridis", alpha=0.7, edgecolor="k")
plt.colorbar(label="Docking Score")
plt.title("Chemical Space Representation Colored by Docking Score")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# Step 7: Cluster Analysis
cluster_analysis = df_pca.groupby("cluster")["score"].agg(["mean", "min", "max", "count"])
cluster_analysis = cluster_analysis.sort_values(by="mean")  # Sort by lowest mean score
print('this is the cluster analysis')
print(cluster_analysis)

# Step 8: Feature Analysis per Cluster showing mean of all the columns
feature_means = df.groupby("cluster").mean()
print(feature_means)

# Step 9: Identify Most Distinctive Features of Cluster 1
cluster_1_means = feature_means.loc[1]
overall_means = df.mean()
diff = cluster_1_means - overall_means
print("Most Distinctive Features of Cluster 1:")
print(diff.sort_values())  # See which features stand out most

# Step 10: Visualize Feature Distributions Across Clusters
important_features = ["MW", "XLogP", "HBA", "HBD", "AromaticRingCount", "TPSA_NO", "TPSA_NOPS"]
for feature in important_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df_pca["cluster"], y=df[feature])
    plt.title(f"{feature} Across Clusters")
    plt.show()

# Step 11: Correlation Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

"""
MW interpretation from box plot 
MW is the molecular weight of the compound. The box plot shows the distribution of molecular weights across 
the clusters.
Cluster 0 (Leftmost Box)

Median MW is lower than the other clusters.
The interquartile range (IQR) is smaller, meaning MW values are more tightly packed.
There are multiple outliers (dots below the whiskers), indicating some significantly smaller MW compounds.

Cluster 1 (Middle Box)

Higher median MW than Cluster 0.
Wider IQR, suggesting more variability in MW.
A few outliers below the whiskers.

Cluster 2 (Rightmost Box)

Very similar to Cluster 1 in median and IQR.
The highest MW values are found here, as indicated by the top whisker reaching the maximum.



"""








"""
XLogP interpretation from box plot 

XLogP is a measure of a molecule's lipophilicity, which refers to how well a compound dissolves in fats,
oils, and non-polar solvents versus water.

A higher XLogP value means the molecule is more hydrophobic (lipophilic), meaning
it prefers non-polar environments and is less soluble in water.
A lower or negative XLogP value means the molecule is more hydrophilic,
meaning it dissolves well in water but not in lipids.
Lipophilicity is important in drug discovery because:
Too high XLogP (above 5) may lead to poor solubility and bioavailability.
Too low XLogP (negative values) means the drug may not easily pass through cell membranes.


Interpreting the Box Plot
This box plot shows the distribution of XLogP values across three clusters.

Key Observations:
Cluster 0 (Leftmost Box)

Median XLogP is around 2.
The interquartile range (IQR) spans from slightly negative values to around 4.
Many outliers exist in the negative range (below -5), indicating some very hydrophilic compounds.
Cluster 1 (Middle Box)

Median XLogP is similar to Cluster 0.
The IQR shows a slightly broader range.
There are also many outliers in the negative direction, but not as extreme as Cluster 0.
Cluster 2 (Rightmost Box)

Median XLogP is higher than the other two clusters (around 3-4).
The overall range is shifted towards more lipophilic values.
Outliers exist but are more concentrated in the positive range.

Conclusion
Cluster 2 contains the most lipophilic molecules, which could indicate better membrane permeability but might have lower solubility.
Cluster 0 and Cluster 1 contain more hydrophilic molecules, with some extreme outliers having very low XLogP values.
This plot helps determine which clusters are more suited for drug-like properties based on lipophilicity.
"""


"""
HBA interpretation from box plot
What is HBA?
HBA (Hydrogen Bond Acceptors) refers to the number of atoms in a molecule that can accept hydrogen bonds, typically oxygen and nitrogen atoms with lone pairs.

A higher HBA value means the molecule has more polar functional groups, making it more water-soluble but possibly harder to pass through lipid membranes.
A lower HBA value means the molecule is less polar, potentially improving membrane permeability but reducing solubility.
In drug discovery, Lipinski’s Rule of Five suggests that an ideal drug should have HBA ≤ 10 for good bioavailability.
Interpreting the Box Plot
This plot shows the distribution of HBA values across three clusters.

Key Observations:
Cluster 0 (Leftmost Box)

Median HBA is around 4.
IQR spans from about 2 to 6, with a few outliers reaching 8+.
The lower whisker suggests some molecules have very few HBA groups (1 or 2), meaning they might be less polar.
Cluster 1 (Middle Box)

Highest median HBA value (around 6-7).
The IQR shows values ranging from 4 to 8, with outliers reaching 14+.
This cluster has the most polar molecules, making them more soluble but possibly less membrane-permeable.
Cluster 2 (Rightmost Box)

Median HBA is around 5.
IQR spans from about 3 to 6, with a few outliers reaching 10.
This cluster has moderate polarity, meaning a mix of lipophilic and hydrophilic compounds.

Conclusion
Cluster 1 contains the most hydrogen bond acceptors, indicating the most hydrophilic molecules, which may have higher solubility but lower permeability.
Cluster 0 and Cluster 2 have a lower HBA range, meaning they likely contain more membrane-permeable compounds.
Comparing this with XLogP, we can determine which clusters balance solubility vs. permeability best.
"""



"""
HBD interpretation from box plot
What is HBD?
HBD (Hydrogen Bond Donors) refers to the number of atoms in a molecule that can donate hydrogen bonds, typically hydroxyl (-OH) and amine (-NH) groups.

Higher HBD values indicate more hydrophilic molecules, which improve water solubility but can reduce membrane permeability.
Lower HBD values suggest more lipophilic molecules, which might pass through membranes more easily but have lower solubility.
Lipinski’s Rule of Five states that an ideal drug should have HBD ≤ 5 for good oral bioavailability.
Interpreting the Box Plot
This plot shows HBD distribution across clusters.

Key Observations:
Cluster 0 (Leftmost Box)

Median HBD is about 1.
IQR ranges from 0 to 2, with some outliers reaching 4-5.
This cluster contains mostly low-HBD molecules, which may be more membrane-permeable.
Cluster 1 (Middle Box)

Median HBD is around 2.
IQR spans 1 to 3, but with several outliers reaching 6+.
This cluster contains more hydrogen bond donors, making it the most hydrophilic.
Cluster 2 (Rightmost Box)

Median HBD is below 1.
IQR is tight (0 to 1), with a few outliers reaching 3-4.
This cluster has the lowest HBD values, suggesting it contains the most lipophilic molecules.


Conclusion
Cluster 1 has the highest HBD values, making these molecules the most water-soluble but possibly less permeable.
Cluster 0 has moderate HBD values, balancing solubility and permeability.
Cluster 2 has the lowest HBD values, meaning these molecules may be the most membrane-permeable but less soluble.
"""


"""
Aromatic Ring Count interpretation from box plot

What is Aromatic Ring Count?
Aromatic rings (e.g., benzene rings) play a significant role in drug design because they:

Improve molecular stability
Enhance membrane permeability
Increase binding affinity to target proteins
However, too many aromatic rings can reduce solubility and increase metabolic instability.

Interpreting the Box Plot
This box plot displays the distribution of aromatic ring counts across clusters.

Key Observations:
Cluster 0 (Leftmost Box)

Median aromatic ring count: ~1
IQR spans 0 to 2, with a few outliers reaching 4.
This suggests less aromaticity, meaning these molecules might be more flexible but less lipophilic.
Cluster 1 (Middle Box)

Median aromatic ring count: ~2
IQR: 1 to 3, with outliers reaching 5-6 rings.
This cluster contains more aromatic compounds, which may enhance binding affinity but could impact solubility.
Cluster 2 (Rightmost Box)

Median aromatic ring count: ~2
IQR: 1 to 3, with outliers reaching 8 rings.
Similar to Cluster 1, but with some extreme outliers, indicating highly aromatic molecules.


Conclusion
Cluster 0 has the lowest aromatic ring count, likely containing more flexible and hydrophilic molecules.
Clusters 1 and 2 have similar median values, but Cluster 2 contains highly aromatic molecules, which may improve binding affinity but reduce solubility.
Cluster 2 has the highest outliers (up to 8 rings), which may indicate polycyclic or rigid drug-like molecules.




"""

"""
TPSA_NO and TPSA_NOP interpretation from box plot

TPSA (Topological Polar Surface Area) is a molecular descriptor used in drug discovery and medicinal 
Chemistry to estimate a molecule's ability to interact with biological environments, particularly in terms of solubility and permeability.

Meaning of TPSA
TPSA measures the total surface area of polar atoms (usually oxygen, nitrogen, and attached hydrogens) in a molecule. 
It is expressed in square angstroms (Å²) and is used to predict drug absorption, bioavailability, and blood-brain barrier permeability.

Explanation of the Box Plots for TPSA_NO and TPSA_NOPS Across Clusters
1. TPSA_NO Across Clusters
Cluster 0: Has a relatively compact distribution with a median TPSA_NO around 50. There are some outliers above 100, but they are not as 
extreme as in other clusters.
Cluster 1: Shows the highest median TPSA_NO, around 90. It also has the widest interquartile range (IQR), indicating higher variability. 
The presence of numerous outliers above 150 suggests that some molecules in this cluster have significantly higher TPSA_NO values.
Cluster 2: Has a median similar to Cluster 0 but with a slightly wider spread. Outliers extend beyond 100 but are fewer compared to Cluster 1.
Interpretation:
Cluster 1 contains molecules with the highest TPSA_NO values, meaning they have more polar surface area, potentially making them more hydrophilic.
Clusters 0 and 2 have lower and more similar distributions, suggesting molecules in these groups share a comparable degree of polar surface area.

2. TPSA_NOPS Across Clusters
Cluster 0: Similar to the TPSA_NO plot, this cluster has a median TPSA_NOPS around 50, with a moderate spread and outliers exceeding 100.
Cluster 1: Again, this cluster has the highest median TPSA_NOPS, around 90, and the largest spread. Many molecules in this cluster have significantly
higher polar surface area values, as indicated by the numerous outliers above 150.
Cluster 2: This cluster has a median TPSA_NOPS slightly lower than Cluster 0, with a similar distribution but slightly fewer extreme outliers.
Interpretation:
The trends in TPSA_NOPS closely mirror those in TPSA_NO, reinforcing the idea that Cluster 1 contains molecules with the highest polar surface area,
while Clusters 0 and 2 have lower values. If TPSA_NOPS accounts for additional elements beyond nitrogen and oxygen (like sulfur or phosphorus), 
this suggests that molecules in Cluster 1 might contain these atoms more frequently, contributing to their higher TPSA.

Overall Conclusion
Cluster 1 consistently shows the highest median values and the widest range for both TPSA_NO and TPSA_NOPS. This suggests that it contains molecules with
significantly larger polar surface areas.
Clusters 0 and 2 have lower and similar TPSA values, indicating that molecules in these groups may be less polar and potentially more hydrophobic.
The presence of numerous outliers in Cluster 1 suggests that some molecules have extreme TPSA values, which could affect their bioavailability and solubility.

"""



"""
Here’s a detailed write-up summarizing the differences between the three clusters based on the box plots, with a focus on **Cluster 1**.  

---

### **Analysis of Molecular Properties Across Clusters**  

The clustering analysis reveals distinct differences in molecular properties across **Cluster 0, Cluster 1, and Cluster 2**, with **Cluster 1
standing out due to its higher polarity and unique physicochemical characteristics**.  

#### **Cluster 1: Highly Polar Compounds with Reduced Permeability**  
Cluster 1 exhibits the **highest values** for **TPSA_NO and TPSA_NOPS**, indicating that its molecules have a significantly larger **polar 
surface area**. This suggests that compounds in this cluster are likely to be **more hydrophilic**, which can impact their solubility and permeability.  

- **TPSA_NO and TPSA_NOPS**: The high values in Cluster 1 suggest strong hydrogen-bonding potential, which can reduce the ability of these molecules
to pass through **lipophilic membranes** (e.g., the blood-brain barrier).  
- **LogP (Lipophilicity)**: Compared to the other clusters, Cluster 1 shows a **lower LogP value**, meaning these molecules are **less lipophilic** and 
more water-soluble. This aligns with their high TPSA values, reinforcing their **poor membrane permeability** but **better solubility in aqueous environments**.  
- **Molecular Weight (MW)**: Cluster 1 also has relatively higher MW values, which could further contribute to reduced permeability and possibly lower
oral bioavailability, depending on the specific range.  
- **Fraction of Sp3 Hybridized Carbons (Fsp3)**: The Fsp3 values suggest that Cluster 1 molecules have more **rigid, planar structures** rather than
flexible, saturated carbon frameworks.  

**Implications:**  
- **Druggability**: These molecules may struggle with **oral absorption and crossing biological membranes**, making them more suitable for 
**injectable formulations or highly targeted drug delivery** strategies.  
- **Potential Use Cases**: Given their hydrophilicity, these compounds might be candidates for **enzyme inhibitors, nucleoside analogs, 
or drugs requiring carrier-mediated transport**.  

---

#### **Cluster 0 & Cluster 2: More Lipophilic & Permeable Compounds**  
Compared to Cluster 1, Clusters 0 and 2 exhibit properties that suggest they may have **better permeability and oral bioavailability**:  

- **Lower TPSA_NO and TPSA_NOPS**: These clusters have **smaller polar surface areas**, suggesting **higher lipophilicity** and **greater passive 
diffusion potential**.  
- **Higher LogP**: The increased LogP values indicate a **greater affinity for lipid membranes**, which may facilitate absorption and distribution.  
- **Lower Molecular Weight**: Compounds in Clusters 0 and 2 tend to be smaller, which can enhance their ability to **cross biological barriers** and be 
**metabolized efficiently**.  
- **Higher Fsp3 Values**: A higher fraction of sp3-hybridized carbons suggests that these molecules are **less rigid**, which can sometimes improve
**binding to diverse biological targets**.  

**Implications:**  
- **Cluster 0 & 2 compounds may have higher oral bioavailability and better blood-brain barrier permeability**.  
- **Potential Use Cases**: These molecules could be more suitable for **CNS drugs, orally available therapeutics, or lipophilic enzyme inhibitors**.  

---

### **Conclusion**  
This clustering analysis highlights **Cluster 1 as a distinct group of highly polar molecules with limited permeability but strong hydrogen-bonding potential
**, making them ideal for **targeted drug delivery or specific enzymatic interactions**. In contrast, Clusters 0 and 2 contain **more lipophilic and
membrane-permeable compounds**, which may be more favorable for **oral drug formulations and CNS-targeted therapies**.  

"""


"""
HEAT MAP EXPLANATION

Explanation of the Feature Correlation Heatmap
This heatmap provides a correlation matrix of various molecular properties, showing how each feature relates to others.
The correlation values range from -1 to 1, where:

1.0 (dark red) → Perfect positive correlation (when one increases, the other also increases).
-1.0 (dark blue) → Perfect negative correlation (when one increases, the other decreases).
0 (white/neutral) → No correlation between the features.
Key Observations from the Heatmap
1. High Correlations (Red Regions) – Features that Increase Together
Molecular Weight (MW) vs. MW_EXACT (1.00) → Expected, as they measure similar properties.
MW vs. HAC (Heavy Atom Count) & BondCount (~0.98 - 0.96) → Larger molecules naturally have more atoms and bonds.
TPSA_NO vs. TPSA_NOPS (~0.89) → Since both represent polar surface area with different atom considerations, they scale together.
HAC vs. AtomCount (~1.00) → Heavy atom count is highly linked to total atom count.
Rotatable Bonds (RotBondCount) vs. HalogenCount (~0.50) → Some flexibility in molecules might be linked to halogen presence.
2. Negative Correlations (Blue Regions) – Features that Move in Opposite Directions
TPSA_NO vs. XLogP (-0.36) → Higher polarity (TPSA) leads to lower lipophilicity (XLogP), making molecules less membrane-permeable.
TPSA_NOPS vs. XLogP (-0.34) → Similar to TPSA_NO, meaning more polar surface area results in less lipophilicity.
Fsp3 vs. HAC (-0.34) → Molecules with a higher fraction of sp3 carbons tend to be less planar, meaning they likely have fewer heavy atoms.
3. Cluster Correlations
Cluster vs. XLogP (~0.17) → Slight positive correlation suggests some clusters might contain more lipophilic compounds.
Cluster vs. TPSA_NO (~-0.14) → Slight negative correlation means some clusters contain more polar molecules.
4. No Significant Correlation (Near 0, White Areas)
Some features, such as PosCount, NegCount, SpiroCount, and AromaticRingCount, have little or no correlation with other molecular 
properties, indicating they vary independently across the dataset.


"""

"""
Cluster Analysis Based on the Feature Correlation Heatmap**  

The heatmap reveals how different molecular properties correlate with one another and how they relate to the assigned **clusters**.

---

Cluster 1: Key Characteristics**  
Cluster 1 is **moderately correlated with lipophilicity (XLogP)** (~0.17) and has a **slightly negative correlation with TPSA_NO (-0.14)**, suggesting that:  
- **Higher lipophilicity**: The molecules in this cluster tend to be more **hydrophobic**, meaning they dissolve better in **fatty environments** rather 
than water.  
- **Lower polar surface area (TPSA_NO)**: They are likely to **cross biological membranes more easily**, as a lower TPSA typically correlates with better 
cell permeability.  
- **Potential drug-like properties**: Since **XLogP is positively correlated with Cluster 1**, compounds in this cluster might favor **membrane permeability**, 
which is useful for drug absorption. However, excessive lipophilicity can also lead to **poor solubility and toxicity risks**.

---

Cluster 2: More Polar Compounds**
- This cluster likely contains compounds with **higher TPSA values** (more polar surface area).  
- A **negative correlation with XLogP** suggests **lower lipophilicity**, meaning these molecules might struggle to pass through 
**lipid membranes** and may require **transporters** or **alternative delivery mechanisms**.  
- High **TPSA and HAC (heavy atom count)** suggest the presence of many **hydrogen bond donors/acceptors**, possibly making these molecules 
**more water-soluble**.

---

Cluster 3: Intermediate or Balanced Properties**
- Cluster 3 appears to **balance between lipophilicity and polarity**, with **XLogP, TPSA, and HAC showing moderate correlations**.
- This cluster could represent molecules **with a mix of hydrophobic and hydrophilic regions**, making them **versatile in different biological environments**.
- **Moderate molecular weight (MW) and atom count** suggest that these molecules may be **structurally diverse**.

---
Summary: Cluster 1 vs. Other Clusters
| Feature | Cluster 1 | Cluster 2 | Cluster 3 |
|---------|-----------|-----------|-----------|
| **XLogP (Lipophilicity)** | **Higher** (Hydrophobic) | **Lower** (Hydrophilic) | Intermediate |
| **TPSA (Polar Surface Area)** | **Lower** (More permeable) | **Higher** (More soluble) | Balanced |
| **Molecular Weight (MW)** | Moderate | Higher | Moderate |
| **Heavy Atom Count (HAC)** | Lower | Higher | Moderate |
| **Membrane Permeability** | **Good** | **Lower** | **Balanced** |
| **Water Solubility** | Lower | **Higher** | Balanced |

---

Implications for Drug Discovery**
- **Cluster 1 molecules are more lipophilic**, meaning they are more likely to cross cell membranes. 
This can be **beneficial for oral bioavailability** but might **increase toxicity risks** if they accumulate in fatty tissues.  
- **Cluster 2 molecules are more hydrophilic**, making them more **soluble in water** but potentially harder to **transport across lipid membranes**.  
- **Cluster 3 molecules strike a balance**, making them **versatile candidates** for further optimization.  


"""