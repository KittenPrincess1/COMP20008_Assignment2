import pandas as pd
import matplotlib.pyplot as plt
import json
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
    # and use it to project the number of a service that our LGA will require, given its demographics
    servicesRequired = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            service = services[i]
            demographic = demographics[j]
            servicesPerCapita = communities[service].mean()/communities[demographic].mean()
            servicesRequired[i][j] = servicesPerCapita*(communities.loc[communities["LGA"] == LGA][demographic].sum())
    # print out a bar graph comparing the number of required services in the Local Government Area
    fig = plt.figure(figsize=(6, 15))
    ax = fig.subplots(len(services))
    for i in range(3):
        demographic = demographics[i]
        relevantData = servicesRequired[i] #this is the number of services that the community requires
        chartData = [] # this is the number of services that the community actually has

        for service in services:
            chartData.append(communities.loc[communities["LGA"] == LGA][service].sum())
        
        df = pd.DataFrame({'Required Value': relevantData, 'Actual Value': chartData}, index = services)
        ax[i] = df.plot.bar(rot=0)
        ax[i].set_title(demographic)

    plt.savefig("Economically_Disadvanted_People.png")
    plt.close()

    # Construct a machine learning model to predict the crime rates of a given area, given its level of economic disadvantage

    #print out to a json file a list of the services required, as well as the types of crime this LGA is most at risk of
    servicesToIncrease = ""
    for i in range(3):
        for j in range(3):
            service = services[i]
            if int(servicesRequired[i][j]) > communities.loc[communities["LGA"] == LGA][service].sum():
                if len(servicesToIncrease) > 0:
                    servicesToIncrease = servicesToIncrease + ", " + service
                else:
                    servicesToIncrease = service
                break

    crimes = ""
    summary = {
        "Services to increase": servicesToIncrease,
        "Crimes that may increase": crimes
    }

    with open("Economically_Disadvantaged_People.json", "w") as outfile:
        json.dump(summary, outfile, indent=4)
    return