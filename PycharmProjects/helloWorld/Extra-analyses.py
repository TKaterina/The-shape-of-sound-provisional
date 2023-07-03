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

    response_time = data_frame['slider_3.rt'].to_frame()
    # ratings = xtab['slider_3.response'].values.reshape(3, 7, 3).T

    amp = np.unique(data_frame['am'].values)
    carr = np.unique(data_frame['carrier'].values)

    return xtab, response_time, amp, carr, data_frame


xtab1, rt1, am, carrier, df01 = prep(df01)
xtab2, rt2, _, _ , df02 = prep(df02)
xtab3, rt3, _, _, df03 = prep(df03)
xtab4, rt4, _, _, df04 = prep(df04)
xtab5, rt5, _, _, df05 = prep(df05)
xtab6, rt6, _, _, df06 = prep(df06)

rt = pd.concat([rt1, rt2, rt3, rt4, rt5, rt6])

M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD


def remove_outliers(xtab,upper,lower):

    # xtab = xtab.drop(xtab['slider_3.rt'].values < lower_bound | xtab['slider_3.rt'].values > upper_bound)
    drops = ((xtab['slider_3.rt'].values > upper) | (xtab['slider_3.rt'].values < lower))
    xtab[drops==True] = 'Outlier'
    ratings = xtab['slider_3.response'].values.reshape(3, 7, 3).T

    return ratings, xtab


ratings = [remove_outliers(xtab1, upper_bound, lower_bound)[0],
           remove_outliers(xtab2, upper_bound, lower_bound)[0],
           remove_outliers(xtab3, upper_bound, lower_bound)[0],
           remove_outliers(xtab4, upper_bound, lower_bound)[0],
           remove_outliers(xtab5, upper_bound, lower_bound)[0],
           remove_outliers(xtab6, upper_bound, lower_bound)[0]]

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
    plt.xlabel('Amplitude Modulation Frequency (Hz)')
    plt.ylabel('Perceived Difference Rating')
    plt.legend(['Pitch', 'Roughness', 'Tremolo'])
    plt.grid(True)
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title(carrier_title[i])

# calculate the within subjects variance per percept
def within_block_variance(data_frame):

    # xtab_means = data_frame.pivot_table(index=['question', 'am', 'carrier'],values = 'slider_3.response', aggfunc=np.mean)
    # xtab_std = data_frame.pivot_table(index=['question', 'am', 'carrier'], values='slider_3.response',aggfunc=np.std)
    xtab_range = data_frame.pivot_table(index=['question', 'am', 'carrier'], values='slider_3.response',aggfunc={np.min,np.max})
    # xtab_range = data_frame.pivot_table(index=['question', 'am', 'carrier'], values='slider_3.response',aggfunc=np.range)

    #xtab_diff = data_frame.pivot_table(index=['question', 'am', 'carrier', 'slider_3.rt'])
    #difference = np.zeros((np.int16(len(xtab_diff)/3), 1))
    #wcv = np.zeros((np.int16(len(xtab_diff) / 3), 1))
    #for n in range(0,len(xtab_diff), 3):
        #difference[n] = np.diff(xtab_diff['slider_3.response'].values[n: n+3], 2)

        #temp = difference[n] ** 2 / 2
        # Individual CVs
        #cv = np.sqrt(temp) / xtab_means['slider_3.response'].values[n]
        # Within-subject coefficient of variation
        #wcv[n] = np.sqrt(np.mean(cv ** 2))

    wcv = xtab_range['amax'].values - xtab_range['amin'].values

    return wcv, xtab_range


wbcv = [within_block_variance(df01)[0],
           within_block_variance(df02)[0],
           within_block_variance(df03)[0],
           within_block_variance(df04)[0],
           within_block_variance(df05)[0],
           within_block_variance(df06)[0]]

agg_rating = [within_block_variance(df01)[1],
           within_block_variance(df02)[1],
           within_block_variance(df03)[1],
           within_block_variance(df04)[1],
           within_block_variance(df05)[1],
           within_block_variance(df06)[1]]

plt.figure()
for i in range(len(wbcv)):

    plt.hist(wbcv[i], bins=np.arange(0, 100, 5), alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.xlabel('Modulator x Carrier Frequency Combination')
    plt.ylabel('Covariance of ratings between blocks')
    plt.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6'])
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Covariance of ratings between blocks')


plt.figure()
for i in range(len(wbcv)):
    plt.subplot(1, 3, 1)
    plt.hist(wbcv[i][0:21], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.xlabel('Range of tremolo ratings between blocks')
    plt.ylabel('Frequency')
    plt.legend(
        ['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6'])
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)

    plt.subplot(1, 3, 2)
    plt.hist(wbcv[i][22:42], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.xlabel('Range of roughness ratings between blocks')
    plt.ylabel('Frequency')
    plt.legend(
        ['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6'])
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)

    plt.subplot(1, 3, 3)
    plt.hist(wbcv[i][43:], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.xlabel('Range of pitch ratings between blocks')
    plt.ylabel('Frequency')
    plt.legend(
        ['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6'])
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)


