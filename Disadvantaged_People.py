import pandas as pd

def task1(LGA):
    # open the files containing the data concerning Economically disadvantaged people
    with open('Data/communities.csv', 'r') as in_file:
        communities = pd.read_csv(in_file)

    # find the average number of each service, given the number of economically disadvantaged people in a local government area

    # Construct a machine learning model to predict the crime rates of a given area, given its level of economic disadvantage


