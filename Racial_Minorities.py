import pandas as pd
import matplotlib.pyplot as plt

def task4():
    communities = pd.read_csv('Data/communities.csv')

    # Preprocessing to remove string values 
    aboriginals = communities['Aboriginal or Torres Strait Islander, persons'].replace('<5', 0)
    aboriginals = aboriginals.astype(int)

    IRSD_avg = communities['IRSD (avg)'].replace('<5', 0)
    IRSD_avg = IRSD_avg.astype(float)
    
    BOS = communities['Born overseas, persons'].replace('<5', 0)
    BOS = BOS.astype(int)

    NESB = communities['Born in non-English speaking country, persons'].replace('<5', 0)
    NESB = NESB.astype(int)

    df1 = pd.merge(aboriginals, IRSD_avg, right_index =True, left_index = True)
    df2 = pd.DataFrame(BOS).join(NESB).join(IRSD_avg)

    # Data Analysis  
    # Number of Indigenous Australians Vs average IRSD for each community scatter plot
    plot1 = df1.plot(kind='scatter', 
                     x='Aboriginal or Torres Strait Islander, persons', 
                     y='IRSD (avg)',
                     ylabel='Average Index of Relative Socio-Economic Disadvantage',
                     title='Indigigenous Australians Vs Socio-Economic Disadvatage',
                     logx=True)
    
    plt.savefig('Indigienous_People.png')
    plt.close()

    # Number of people born oversears and born in non-English Speaking countries Vs avergage IRSD for each community scatter plot
    plt.scatter(x=df2['Born overseas, persons'], y=df2['IRSD (avg)'], label='Born Overseas', alpha=0.3)
    plt.scatter(x=df2['Born in non-English speaking country, persons'], y=df2['IRSD (avg)'], label='Born in non-English Speaking Country', alpha=0.3)

    plt.legend()
    plt.title('Born Overseas Vs Socio-Economic Disadvantage')
    plt.xlabel('Number of People')
    plt.xscale('log')
    plt.ylabel('Average Index of Relative Socio-Economic Disadvantage')

    plt.savefig('Born_Overseas.png')
    plt.close()

    return
task4()    