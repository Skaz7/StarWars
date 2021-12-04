import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('D:\\Users\\sebas\\OneDrive\\Repositories\\StarWars\\Star Wars.xlsx')

print(df.columns)  # prints names of columns

print()

# total number of people asked
people_asked = len(df)

# number of people who have seen the movies
have_seen = len(df.loc[df['Have you seen any of the 6 films in the Star Wars franchise?'] == 'Yes'])

# number of people who have not seen the movies
have_not_seen = len(df.loc[df['Have you seen any of the 6 films in the Star Wars franchise?'] == 'No'])

print()

print(have_not_seen)
print(have_seen)

# prepare the plot
data = [have_seen, have_not_seen]
labels = 'People who have seen any od Star Wars movies', 'People who have not seen any of Star Wars movies'
explode = (0, 0.1)
colors = ['#99ff99', '#66b3ff']

figure1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, colors=colors)

plt.show()