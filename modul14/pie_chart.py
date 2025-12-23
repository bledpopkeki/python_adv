import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("avgIQpercountry.csv")

novel_prices_by_continent=df.groupby('continent')['Nobel Prices']).sun()

no_of_continents=novel_prices_by_continent.count()
print(no_of_continents)

colors=['gold','lightcoral','yellow','thistle','orange','skyblue']
plt.figure(figsize=(10,10))

novel_prices_by_continent.plot(kind="pie",colors=colors,autopct="%1.1f%%")

plt.title('Distrubiton of Nobel prices by continent')
plt.axis('equal')
plt.ylabel('')

plt.tight_layout()
plt.show()


