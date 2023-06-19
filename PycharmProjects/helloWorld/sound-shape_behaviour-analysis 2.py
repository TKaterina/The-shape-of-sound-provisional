import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('_Roughness._2023-04-19_18h09.12.811.csv')
df01 = pd.read_csv('PO01_Roughness._2023_Jun_19_1103.csv')
df02 = pd.read_csv('PO02_Roughness._2023_Jun_19_1156.csv')
df3= pd.read_csv('_Roughness_2023_May_30.csv')

def prep(data_frame):
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_3.response'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    xtab = data_frame.pivot_table(index=['question', 'am'])

    ratings = xtab['slider_3.response'].values.reshape(3, 7).T
    am = np.unique(data_frame['am'].values)

    return ratings,am

am = prep(df01)[1]
ratings = [prep(df01)[0], prep(df02)[0], prep(df3)[0]]

output = np.zeros((len(ratings), 1))
result = np.zeros((len(ratings[0]), 3))
for k in np.arange(0,3):
    for j in range(len(ratings[0])):
        for i in range(len(ratings)):
            output[i] = ratings[i][j][k]

        result[j][k] = np.mean(output)

plt.figure()
plt.plot(np.arange(7), result, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
plt.ylabel('Percived Difference Rating')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')


