import pandas as pd
import matplotlib.pyplot as plt
import helper

def task1(LGA):
    # open the files containing the data concerning Economically disadvantaged people
    with open('Data/communities.csv', 'r') as in_file:
        communities = pd.read_csv(in_file)
    services = ["Homelessness", "Centrelink Offices", "Medicare Offices"]
    demographics = ["Equivalent household income <$600/week", "Personal income <$400/week, persons", "IRSD (avg)"]
    #preprocess the data so that it can be treated as an integer with no issues
    for service in services:
        communities[service] = communities[service].apply(helper.standardise)
        communities[service] = communities[service].astype(int)
    for demographic in demographics:
        communities[demographic] = communities[demographic].apply(helper.standardise)
        communities[demographic] = communities[demographic].astype(int)
    # find the average number of each service, given the number of economically disadvantaged people in a local government area
    servicesRequired = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            service = services[i]
            demographic = demographics[j]
            servicesPerCapita = communities[service].mean()/communities[demographic].mean()
            servicesRequired[i][j] = servicesPerCapita*communities.loc[communities["LGA"] == LGA][demographic]
    # print out a json file with the required services listed in it and bar graphs
    fig = plt.figure(figsize=(6, 15))
    ax = fig.subplots(len(services))
    for i in range(3):
        service = services[i]
        relevantData = servicesRequired[i]
        chartData = []

        for demographic in demographics:
            chartData.append(communities.loc[communities["LGA"] == LGA][service].sum())
        
        df = pd.DataFrame({'Required Value': relevantData, 'Actual Value': chartData}, index = demographics)
        ax[i] = df.plot.bar(rot=0)
        ax[i].set_title(demographic)

    plt.savefig("Economically_Disadvanted_People.png")
    plt.close()

    # Construct a machine learning model to predict the crime rates of a given area, given its level of economic disadvantage

    #print out to a json file a list of the services required, as well as the types of crime this LGA is most at risk of
    return