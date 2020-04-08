import os
os.getcwd

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('countries.csv')

set(data.continent)
data_2007 = data[data.year == 2007]
asia_2007 = data_2007[data_2007.continent == 'Asia']
europe_2007 = data_2007[data_2007.continent == 'Europe']

print(len(set(asia_2007.country)))
print(len(set(europe_2007.country)))

#mean
print('Mean GDP per Capita in Asia:')
print(asia_2007.gdpPerCapita.mean())

print('Mean GDP per Capita in Europe:')
print(europe_2007.gdpPerCapita.mean())


#median
print('Median GDP per Capita in Asia:')
print(asia_2007.gdpPerCapita.median())

print('Median GDP per Capita in Europe:')
print(europe_2007.gdpPerCapita.median())

#ploting using pyplot
plt.subplot(211)
plt.hist(asia_2007.gdpPerCapita, 20, range=(0,50000), edgecolor='black')
plt.ylabel('Asia')
plt.subplot(212)
plt.hist(europe_2007.gdpPerCapita, 20, range=(0,50000), edgecolor = 'black')
plt.ylabel('Europe')
plt.show()

#comparing life expectancy of america and europe using histogram
data_1997 = data[data.year == 1997]
europe_1997 = data_1997[data_1997.continent == 'Europe']
america_1997 = data_1997[data_1997.continent == 'Americas']

#mean
print('Mean LifeExpectancy in Europe:')
print(europe_1997.lifeExpectancy.mean())

print('Mean LifeExpectancy in Americas:')
print(america_1997.lifeExpectancy.mean())


#median
print('Median Life Expectancy in Europe:')
print(europe_1997.lifeExpectancy.median())

print('Median Life Expectancy in Americas:')
print(america_1997.lifeExpectancy.median())

#plot
plt.subplot(211)
plt.title('Distribution of Age in Europe and Americas')
plt.hist(europe_1997.lifeExpectancy, range=(55,85), edgecolor = 'black')
plt.ylabel('Europe')
plt.subplot(212)
plt.hist(america_1997.lifeExpectancy,  range=(55,85), edgecolor = 'black')
plt.ylabel('Americas')
plt.show()
