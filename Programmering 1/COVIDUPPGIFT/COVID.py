#imports
import pandas as pd
import matplotlib.pyplot as plt 


#LÄSER IN DATAFRAMES
dfDeaths = pd.read_csv("National_Daily_Deaths.csv")
dfDeathsendastdeaths = dfDeaths["National_Daily_Deaths"].sum
dfCases = pd.read_csv("Regional_Daliy_Cases.csv")

print(dfDeaths)


