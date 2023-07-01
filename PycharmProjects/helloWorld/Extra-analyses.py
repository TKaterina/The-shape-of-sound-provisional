import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# use the whole path file name with a double slash before 'User'
df01 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S001_Roughness._2023_Jun_29_1205.csv")
df02 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s002_Roughness._2023_Jun_29_1409.csv")
df03 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S003_Roughness._2023_Jun_29_1603.csv")
df04 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s004_Roughness._2023_Jun_30_1239.csv")
df05 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s005_Roughness._2023_Jun_30_1400.csv")
df06 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S006_Roughness._2023_Jun_30_1504.csv")


def prep(data_frame):
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_3.response'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    xtab = data_frame.pivot_table(index=['question', 'am', 'carrier'])

    ratings = xtab['slider_3.response'].values.reshape(3, 7, 3).T

    amp = np.unique(data_frame['am'].values)
    carr = np.unique(data_frame['carrier'].values)

    return xtab, ratings, amp, carr


xtab1 = prep(df01)[0]
xtab2 = prep(df02)[0]
xtab3 = prep(df03)[0]
xtab4 = prep(df04)[0]
xtab5 = prep(df05)[0]
xtab6 = prep(df06)[0]

ratings = [prep(df01)[1], prep(df02)[1], prep(df03)[1], prep(df04)[1], prep(df05)[1], prep(df06)[1]]

am = prep(df01)[2]
carrier = prep(df01)[3]

output = np.zeros((len(ratings), 1))
result = np.zeros([len(carrier), len(am), 3])
standard_deviation = np.zeros([len(carrier), len(am), 3])

for m in np.arange(0,3):
    for k in range(len(carrier)):
        for j in range(len(am)):
            for i in range(len(ratings)):
                if ratings[i][k][j][m] != 'Outlier':
                    output[i] = ratings[i][k][j][m]
                else:
                    output[i] = 'NaN'

            result[k][j][m] = np.nanmean(output)
            standard_deviation[k][j] = np.nanstd(output)


carrier_title = ['440 Hz carrier', '700 Hz carrier', '1000 Hz carrier']
plt.figure()
for i in np.arange(0,3):
    plt.subplot(1,3,i+1)
    plt.plot(np.arange(7), result[i], lw=2)
    plt.xticks(np.arange(7), am)
    plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
    plt.ylabel('Perceived Difference Rating')
    plt.legend(['Pitch', 'Roughness', 'Tremolo'])
    plt.grid(True)
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title(carrier_title[i])



plt.plot(ratings[0], linestyle='solid')
plt.plot(ratings[1], linestyle='dashed')
plt.plot(ratings[2], linestyle='dotted')
plt.plot(ratings[3], linestyle='solid')
plt.plot(ratings[4], linestyle='dashed')
plt.plot(ratings[5], linestyle='dotted')

