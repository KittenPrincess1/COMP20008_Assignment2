import pandas as pd
import matplotlib.pyplot as plt

def task1(communities):
    services = ["Homelessness", "Centrelink Offices", "Medicare Offices", "Child Protection and Family"]
    demographics = ["Lone parent families, %", "Equivalent household income <$600/week, %", "Personal income <$400/week, %"]
    metric = "IRSD (avg)"
    
    #Find any correlation between the demographics there are and the average IRSD
    for i in range(len(demographics)):
        plt.scatter(x=communities[demographics[i]], y=communities[metric], label=demographics[i], alpha = 0.3)

    plt.legend()
    plt.title('Demographics vs socio-economic disadvantage')
    plt.xlabel('Percentage of population')
    plt.ylabel('Average Index of Relative Socio-Economic Disadvantage')

    plt.savefig("demographics_IRSD_plot.png")
    plt.close('all')
    return