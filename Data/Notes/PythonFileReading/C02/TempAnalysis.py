import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

TempDf = pd.read_csv("Data/temperature_data.csv",header=0)

#Replaces -99.99 in Anomalys with NAN
TempDf["Anomaly"]= TempDf["Anomaly"].replace(-99.99,math.nan)
#Removes NANS from the data 
TempDf.dropna(subset=["Anomaly"],inplace=True)

#Plots the graph
plt.scatter(TempDf["Year"],TempDf["Anomaly"])


#Line of best fit
b, a = np.polyfit(TempDf["Year"], TempDf["Anomaly"], deg=1)
plt.plot(TempDf["Year"], a + b * TempDf["Year"], color="k", lw=2.5)
#Shows the graph

#REQUIRED FOR ASSIGNMENTS
plt.title(" Temperature Anomaly Over time")
plt.ylabel(" Temperature Anomalies")
plt.xlabel("Years")

plt.show()