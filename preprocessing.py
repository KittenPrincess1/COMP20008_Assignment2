import pandas as pd

def get_data(file_name):
    with open(file_name, 'r') as in_file:
        communities = pd.read_csv(in_file)

    # add in any rows that you want to analyse as integers
    integer_rows = [
        "IRSD (avg)", "Aboriginal or Torres Strait Islander, persons", "Born overseas, persons", 
        "Born in non-English speaking country, persons", "Homelessness", "Centrelink Offices", "Medicare Offices",
        "Equivalent household income <$600/week", "Personal income <$400/week, persons"
        ]

    for row in integer_rows:
        communities[row] = communities[row].apply(standardise)
        communities[row] = communities[row].astype(int)

    return communities

def standardise(s):
    try:
        return int(s)
    except:
        return 0