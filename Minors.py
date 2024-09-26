import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessing


def task3()
    # Read the CSV file
    communi = pd.read_csv("Data/communities.csv")

     # List of student-related columns
    students = ['Primary school students', 'Secondary school students', 'TAFE students', 'University students', 'Holds degree or higher, persons', 'Did not complete year 12, persons']
    other = ['Unemployed, persons']
    columns = students + other

    # Preprocess the required data 
    for col in columns:
        if col in communi.columns:
            communi[col] = communi[col].apply(preprocessing.standardise)
            communi[col] = communi[col].astype(int)
        else:
            print("Can't find the specific column.")
  
    # Get the LGA types
    communi['LGA Type'] = communi['LGA'].str.extract(r'\((.*?)\)')
   
    # Bar chart to show the number of students in each LGA
    grouped_schools = communi.groupby('LGA Type')[students].sum()
    grouped_schools.plot(kind='bar', figsize=(15, 8), color=['lightblue', 'yellow', 'orange', 'lightgreen', 'pink', 'coral'])
    plt.title('Number of different student levels in LGA types')
    plt.xlabel('LGA Type')
    plt.ylabel('Number of students')
    plt.show()
  
    # Histogram to show the frequency of unemployed persons
    plt.figure(figsize=(10, 6))
    sns.histplot(communi['Unemployed, persons'], bins=30, kde=True)
    plt.title('Unemployed persons frequency')
    plt.xlabel('Number of unemployed persons')
    plt.ylabel('Frequency')
    plt.show()

    # Box plot to show the distribution of unemployed persons in each LGA
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=communi, x='LGA Type', y='Unemployed, persons')
    plt.title('Unemployed Persons by different Local Government Area')
    plt.xlabel('LGA types')
    plt.ylabel('Number of unemployed persons')
    plt.show()

    # check the columns are exist and no missing data 
    exist = False
    for col in columns:
      if col in df.columns:
        exist = True
        break 
    if exist:
      communi[columns] = communi[columns].apply(pd.to_numeric, errors='coerce')
      communi.fillna(0, inplace=True)
    else:
      print("Some data are missing.")
      
    # find out the Pearson correlation coefficent
    pearson_corr = communi[['Unemployed, persons', 'Primary school students', 'Secondary school students', 'TAFE students', 'University students', 'Holds degree or higher, persons',
                            'Did not complete year 12, persons']].corr(method='pearson')
    print("Pearson Correlation Matrix:")
    print(pearson_corr)
  
    # Get the correlatin base on the Pearson Correlation Heatmap
    plt.figure(figsize=(15, 10))
    sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation between unemployed persons and student types')
    plt.show()
    
    
