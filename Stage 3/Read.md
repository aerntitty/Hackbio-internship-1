# Molecular Clustering and Drug Discovery Insights

## Project Overview
This project explores the clustering of molecular descriptors to analyze their implications for drug discovery, bioavailability, and molecular complexity. By using clustering techniques, we can identify distinct molecular properties and how they influence factors such as solubility, membrane permeability, and potential drug-likeness.

## Methodology
- **Data Preprocessing:** Molecular descriptors were extracted and cleaned for clustering.
- **Clustering Approach:** K-Means (or other clustering techniques) was applied to categorize molecules into two distinct clusters.
- **Descriptor Analysis:** Molecular properties such as BondCount, AtomCount, Rotatable Bonds, Simple Ring Count, Molecular Weight, Lipophilicity (XLogP), Hydrogen Bonding Capacity (HBA & HBD), Aromaticity, and Polar Surface Area (TPSA) were analyzed.
- **Box Plot Insights:** Visualizations were used to interpret key molecular differences across clusters.

## Key Findings
### **Cluster 0: Smaller, More Soluble Molecules**
- **Lower BondCount (20-25) and AtomCount (~20)**
- **Likely to be more bioavailable due to smaller size and higher solubility**
- **Better candidates for oral drug formulations**

### **Cluster 1: Larger, More Complex Molecules**
- **Higher BondCount (30-40) and AtomCount (~30+)**
- **Higher Molecular Weight and Lipophilicity, suggesting better membrane permeability**
- **Greater Aromaticity and Hydrogen Bonding, influencing receptor interactions**
- **Potential challenges in solubility and bioavailability due to increased size**

## Implications for Drug Discovery
- **Cluster 0 molecules** could be prioritized for drugs requiring high solubility and rapid absorption.
- **Cluster 1 molecules** may need specialized drug delivery mechanisms due to their complexity and lipophilicity.
- **Understanding molecular clustering** can help in lead optimization and drug formulation strategies.

## Requirements
- Python 3.x
- Pandas, Scikit-learn, Matplotlib, Seaborn

## How to Use
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the clustering script to generate insights.

## Future Enhancements
- Application of advanced clustering methods (e.g., DBSCAN, Hierarchical Clustering)
- Inclusion of additional molecular descriptors
- Integration with cheminformatics databases for deeper analysis

## Contributors
- @aerntitty
- @teodorades

#

