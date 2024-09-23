import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import helper

# 1. Preprocessing
def task2_preprocessing():

    communities = pd.read_csv('Data/communities.csv')

    if 'Estimated Resident Population' in communities.columns:

        communities['Elderly Population Percentage'] = (communities['Population aged 65+'] / communities['Estimated Resident Population']) * 100
    else:
        print("Missing column for Elderly Population calculation")

    columns = ["Elderly Population Percentage", "Disability Support Services", 
               "Public Hospitals", "Private Hospitals", "Community Health Centres", 
               "Aged Care Facilities", "Unemployment Rate", 
               "Equivalent household income <$600/week", 
               "Travel time to GPO", "Distance to GPO"]

    for col in columns:
        if col in communities.columns:
            communities[col] = communities[col].apply(helper.standardise)
            communities[col] = communities[col].astype(int)
        else:
            print(f"Column {col} not found in the dataset")

    return communities

# 2.EDA + Correlation + Trend Analysis
def task2_analysis(communities):
    # EDA
    print("Data Description:")
    print(communities.describe())

    plt.figure(figsize=(10, 6))
    sns.histplot(communities['Elderly Population Percentage'], bins=20)
    plt.title('Distribution of Elderly Population Percentage')
    plt.show()


    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Unemployment Rate', y='Equivalent household income <$600/week', data=communities)
    plt.title('Unemployment Rate vs Low Income Households')
    plt.show()

def task2_correlation(communities):
    # Correlation Analysis
    correlation = communities[["Elderly Population Percentage", "Disability Support Services", 
                               "Unemployment Rate", "Public Hospitals", "Aged Care Facilities"]].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Elderly and Disabled Services')
    plt.show()


# 3. Machine Learning Model

def task2_supervised_ml(communities):

    # Supervised Model - Linear Relation Model to prediction the Unemployment Rate 
    X = communities[["Elderly Population Percentage", "Disability Support Services", "Public Hospitals", "Aged Care Facilities"]]
    y = communities["Unemployment Rate"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    print("Linear Regression Model Score:", model.score(X, y))


def task2_unsupervised_ml(communities):

    # Unsuoervised Model - KMeans Cluster
    X = communities[["Elderly Population Percentage", "Disability Support Services", "Public Hospitals", "Aged Care Facilities"]]
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)
    
    communities['Cluster'] = kmeans.labels_
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Elderly Population Percentage", y="Disability Support Services", hue='Cluster', data=communities)
    plt.title('Clustering of Elderly and Disability Services')
    plt.show()



def task2(LGA):

    communities = task2_preprocessing()

    task2_analysis(communities)

    task2_correlation(communities)

    task2_supervised_ml(communities)
    
    task2_unsupervised_ml(communities)

    print(f"Elderly and Disabled analysis completed for {LGA}")


if __name__ == "__main__":
    localGovernmentArea = 'Melbourne (C)' 
    task2(localGovernmentArea)