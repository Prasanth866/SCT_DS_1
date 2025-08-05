import pandas as pd
import matplotlib.pyplot as plt
population=pd.read_csv('india_population_by_states_2022.csv')
population.drop([36],inplace=True)
population['Population(in Millions)']=population['Population[50]']/1000000
population.plot(kind='bar',x='State/UT',y='Population(in Millions)')
plt.show()
