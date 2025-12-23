import matplotlib.pyplot as plt
import pandas as pd
from pyprasing import alphas

df=pd.read_csv("avgIQpercountry.csv")

plt.figure(figsize=(10,6))

plt.scatter(df['Mean years of schooling-2021'],df['AverageIq'],color="purple",alpha=0.7)

plt.title('scatter plot of mean years of schooling vs average iq')

plt.xlabel('mean years of schooling-2021')

plt.ylabel('average iq')

plt.grid(True,linestyle="--",alpha=0.7)

plt.show()