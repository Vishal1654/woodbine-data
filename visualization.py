import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

file = 'C:\\Users\\vchopra\\Documents\\woodbine_horses.csv'

dataframe = pd.read_csv(file)

jockeys_name = set(dataframe['win_payoff'].tolist())


dataframe = dataframe.set_index('win_payoff', drop=False)

jockey_placements = OrderedDict()

for jockey in jockeys_name:
    if type(jockey) == str or not np.isnan(jockey):
        data = dataframe.loc[jockey, 'finish_position']
        if type(data) != np.float64:
            jockey_placements[jockey] = data[jockey].values.tolist().count(1)
        else:
            if data == 1:
                jockey_placements[jockey] = 1
            else:
                jockey_placements[jockey] = 0

items = []
for item in list(jockey_placements.items()):
    items.append(item[1])
plt.bar(list(jockey_placements.keys()), items)
plt.show()
