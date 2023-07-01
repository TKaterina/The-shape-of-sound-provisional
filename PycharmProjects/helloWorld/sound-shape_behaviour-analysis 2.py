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

    xtab = data_frame.pivot_table(index=['question', 'am'])

    response_time = data_frame['slider_3.rt'].to_frame()

    amp = np.unique(data_frame['am'].values)

    return xtab, response_time, amp


xtab1, rt1, am = prep(df01)
xtab2, rt2, _ = prep(df02)
xtab3, rt3, _ = prep(df03)
xtab4, rt4, _ = prep(df04)
xtab5, rt5, _ = prep(df05)
xtab6, rt6, _ = prep(df06)


rt = pd.concat([rt1, rt2, rt3, rt4, rt5, rt6])

M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD


def remove_outliers(xtab,upper,lower):

    # xtab = xtab.drop(xtab['slider_3.rt'].values < lower_bound | xtab['slider_3.rt'].values > upper_bound)
    drops = ((xtab['slider_3.rt'].values > upper) | (xtab['slider_3.rt'].values < lower))
    xtab[drops==True] = 'Outlier'
    ratings = xtab['slider_3.response'].values.reshape(3, 7).T

    return ratings,xtab,


ratings = [remove_outliers(xtab1, upper_bound, lower_bound)[0],
           remove_outliers(xtab2, upper_bound, lower_bound)[0],
           remove_outliers(xtab3, upper_bound, lower_bound)[0],
           remove_outliers(xtab4, upper_bound, lower_bound)[0],
           remove_outliers(xtab5, upper_bound, lower_bound)[0],
           remove_outliers(xtab6, upper_bound, lower_bound)[0]]

output = np.zeros((len(ratings), 1))
result = np.zeros((len(ratings[0]), 3))
standard_deviation = np.zeros((len(ratings[0]), 3))

for k in np.arange(0,3):
    for j in range(len(ratings[0])):
        for i in range(len(ratings)):
            if ratings[i][j][k] != 'Outlier':
                output[i] = ratings[i][j][k]
            else:
                output[i] = 'NaN'

        result[j][k] = np.nanmean(output)
        standard_deviation[j][k] = np.nanstd(output)



plt.figure()
plt.plot(np.arange(7), result, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
plt.ylabel('Perceived Difference Rating')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')

# temporary calculation of covariance for each modulator frequency and percept.
covariance = standard_deviation/result
plt.figure()
plt.plot(np.arange(7), covariance, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
plt.ylabel('Covariance of ratings')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')

