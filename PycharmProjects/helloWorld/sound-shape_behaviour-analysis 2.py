import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('_Roughness._2023-04-19_18h09.12.811.csv')

# Keep only rows with slider responses
drops = np.isnan(df['slider.response'].values) == False
df = df[drops]

df = df[['carrier', 'am', 'question', 'slider.response', 'slider.rt']]


xtab = df.pivot_table(index=['question', 'am'])


plt.figure()
ratings = xtab['slider.response'].values.reshape(3,7).T
am = np.unique(df['am'].values)


plt.figure()
plt.plot(np.arange(7), ratings, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
plt.ylabel('Percived Difference Rating')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')

