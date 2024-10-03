import pandas as pd

def get_data(file_name):
    with open(file_name, 'r') as in_file:
        communities = pd.read_csv(in_file)

    # add in any rows that you want to analyse as integers
    numerical_rows = [
        "IRSD (avg)", "Aboriginal or Torres Strait Islander, persons", "Born overseas, persons", 
        "Born in non-English speaking country, persons", "Homelessness", "Centrelink Offices", "Medicare Offices",
        "Equivalent household income <$600/week, %", "Personal income <$400/week, %", "Female-headed lone parent families, %",
        "Male-headed lone parent families, %", "Child Protection and Family"
        ]

    for row in numerical_rows:
        communities[row] = communities[row].apply(standardise)
        communities[row] = communities[row].astype(float)

    #create any required rows that are derived from preexisting rows
    communities["Lone parent families, %"] = communities["Male-headed lone parent families, %"] + communities["Female-headed lone parent families, %"]

    return communities

def standardise(s):
    try:
        return float(s)
    except:
        return 0