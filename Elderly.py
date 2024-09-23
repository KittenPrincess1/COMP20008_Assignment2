import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import helper

# 1. Preprocessing
def task2_preprocessing():
    with open('Data/communities.csv', 'r') as in_file:
        communities = pd.read_csv(in_file)

    columns = ["Elderly Population Percentage", "Disability Support Services", 
               "Public Hospitals", "Private Hospitals", "Community Health Centres", 
               "Aged Care Facilities", "Unemployment Rate", 
               "Equivalent household income <$600/week"]

    for col in columns:
        communities[col] = communities[col].apply(helper.standardise)
        communities[col] = communities[col].astype(int)

    return communities

# 2.EDA + Correlation + Trend Analysis
def task2_analysis(communities):
    # EDA
    print("Data Description:")
    print(communities.describe())

    # Correlation Analysis
    print("\nCorrelation Matrix:")
    correlation = communities[["Elderly Population Percentage", "Disability Support Services", 
                               "Unemployment Rate", "Public Hospitals", "Aged Care Facilities"]].corr()
    sns.heatmap(correlation, annot=True)
    plt.title('Correlation Matrix for Elderly and Disabled Services')
    plt.show()

    # Trend Analysis
    plt.scatter(communities["Elderly Population Percentage"], communities["Unemployment Rate"])
    plt.xlabel('Elderly Population Percentage')
    plt.ylabel('Unemployment Rate')
    plt.title('Elderly Population vs Unemployment Rate')
    plt.show()

# 3. Machine Learning Model

def task2_ml(communities):

    # Supervised Model - Linear Relation Model to prediction the Unemployment Rate 
    X = communities[["Elderly Population Percentage", "Disability Support Services", "Public Hospitals", "Aged Care Facilities"]]
    y = communities["Unemployment Rate"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    print("Linear Regression Model Score:", model.score(X, y))

    # Unsuoervised Model - KMeans Cluster
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)
    communities['Cluster'] = kmeans.labels_

    sns.scatterplot(x="Elderly Population Percentage", y="Disability Support Services", hue='Cluster', data=communities)
    plt.title('Clustering of Elderly Population and Disability Services')
    plt.show()

def task2(LGA):
    
    communities = task2_preprocessing()

    task2_analysis(communities)

    task2_ml(communities)

    print(f"Elderly and Disabled analysis completed for {LGA}")