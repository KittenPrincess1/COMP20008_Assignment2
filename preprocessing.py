import pandas as pd

def get_data(file_name):
    with open(file_name, 'r') as in_file:
        communities = pd.read_csv(in_file)

def standardise(s):
    try:
        return int(s)
    except:
        return 0