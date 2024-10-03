import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessing


def task3(communi):
    # Preprocessing the required data, check the columns are exist
    students = ['Primary school students', 'Secondary school students', 'TAFE students', 'University students',
                'Holds degree or higher, persons', 'Did not complete year 12, persons']
    young = ['2007 ERP age 0-4, persons', '2007 ERP age 5-9, persons', '2007 ERP age 10-14, persons', 
             '2007 ERP age 15-19, persons', '2007 ERP age 20-24, persons', '2012 ERP age 0-4, persons', 
             '2012 ERP age 5-9, persons', '2012 ERP age 10-14, persons', '2012 ERP age 15-19, persons', '2012 ERP age 20-24, persons']
    other = ['Unemployed, persons']
    columns = students + young + other  
    for col in columns:
        if col in communi.columns:
            communi[col] = communi[col].apply(preprocessing.standardise)
            communi[col] = communi[col].fillna(0)
            communi[col] = communi[col].astype(int)
        else:
            print("Can't find the specific column.")
    
    # find out the Pearson correlation coefficent
    students_corr = communi[['Unemployed, persons', 'Primary school students', 'Secondary school students', 'TAFE students',
                             'University students', 'Holds degree or higher, persons', 'Did not complete year 12, persons']].corr(method='pearson')
    young_corr = communi[['Unemployed, persons','2007 ERP age 0-4, persons', '2007 ERP age 5-9, persons',  '2007 ERP age 10-14, persons', 
                          '2007 ERP age 15-19, persons', '2007 ERP age 20-24, persons', '2012 ERP age 0-4, persons', '2012 ERP age 5-9, persons', 
                          '2012 ERP age 10-14, persons', '2012 ERP age 15-19, persons', '2012 ERP age 20-24, persons']].corr(method='pearson') 
    
    # Get the correlation base on the Pearson Correlation Heatmap
    plt.figure(figsize=(20, 20))
    sns.heatmap(students_corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation between unemployed persons and student types')
    plt.savefig("unemployed_student_heatmap.png")
    plt.close()

    plt.figure(figsize=(20, 20))
    sns.heatmap(young_corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation between unemployed persons and young groups')
    plt.savefig("unemployed_young_heatmap.png")
    plt.close()

    return
    
    
    
