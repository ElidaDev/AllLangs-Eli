import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

Co2Df = pd.read_csv("Data/co2_data.csv",header=5)
TempDf = pd.read_csv("Data/temperature_data.csv",header=0)

#Replaces -99.99 in averages with NAN
Co2Df["Average"]= Co2Df["Average"].replace(-99.99,math.nan)
#Removes NANS from the data 
Co2Df.dropna(subset=["Average"],inplace=True)

#Plots the graph
plt.plot(Co2Df["decimal_year"],Co2Df["Average"])
# plt.scatter(Co2Df["decimal_year"],Co2Df["Average"])


#Line of best fit
b, a = np.polyfit(Co2Df["decimal_year"], Co2Df["Average"], deg=1)
plt.plot(Co2Df["decimal_year"], a + b * Co2Df["decimal_year"], color="k", lw=2.5)
#Shows the graph

#REQUIRED FOR ASSIGNMENTS
plt.title("Average Co2 Over time")
plt.ylabel("Average Co2")
plt.xlabel("Years")

plt.show()