import preprocessing, Minors, Racial_Minorities, Disadvantaged_People

df = preprocessing.get_data("Data/communities.csv")

Disadvantaged_People.task1(df)

Minors.task3(df)

Racial_Minorities.task4(df)
