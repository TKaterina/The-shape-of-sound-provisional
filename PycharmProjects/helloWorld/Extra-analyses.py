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
df07 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s007_Roughness._2023_Jul_03_1305.csv")
df08 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s008_Roughness._2023_Jul_03_1505.csv")
df09 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s009_Roughness._2023_Jul_04_1313.csv")
df10 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S010_Roughness._2023_Jul_04_1433.csv")
df11 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s011_Roughness._2023_Jul_05_1215.csv")
df12 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s012_Roughness._2023_Jul_05_1304.csv")
df13 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s013_Roughness._2023_Jul_05_1408.csv")
df14 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s014_Roughness._2023_Jul_05_1515.csv")
df15 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S015_Roughness._2023_Jul_07_1210.csv")
df16 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s016_Roughness._2023_Jul_07_1513.csv")
df17 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s017_Roughness._2023_Jul_11_1207.csv")
df18 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s018_Roughness._2023_Jul_11_1308.csv")
df19 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S019_Roughness._2023_Jul_11_1622.csv")
df20 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S020_Roughness._2023_Jul_12_1208.csv")
df21 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s021_Roughness._2023_Jul_12_1607.csv")

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
xtab7, rt7, _, _ , df07 = prep(df07)
xtab8, rt8, _, _, df08 = prep(df08)
xtab9, rt9, _, _, df09 = prep(df09)
xtab10, rt10, _, _, df10 = prep(df10)
xtab11, rt11, _, _, df11 = prep(df11)
xtab12, rt12, _, _, df12 = prep(df12)
xtab13, rt13, _, _, df13 = prep(df13)
xtab14, rt14, _, _, df14 = prep(df14)
xtab15, rt15, _, _, df15 = prep(df15)
xtab16, rt16, _, _, df16 = prep(df16)
xtab17, rt17, _, _, df17 = prep(df17)
xtab18, rt18, _, _, df18 = prep(df18)
xtab19, rt19, _, _, df19 = prep(df19)
xtab20, rt20, _, _, df20 = prep(df20)
xtab21, rt21, _, _, df21 = prep(df21)

rt = pd.concat([rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10, rt11, rt12, rt13, rt14, rt15, rt16, rt17, rt18, rt19, rt20, rt21])

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
           remove_outliers(xtab6, upper_bound, lower_bound)[0],
           remove_outliers(xtab7, upper_bound, lower_bound)[0],
           remove_outliers(xtab8, upper_bound, lower_bound)[0],
           remove_outliers(xtab9, upper_bound, lower_bound)[0],
           remove_outliers(xtab10, upper_bound, lower_bound)[0],
           remove_outliers(xtab11, upper_bound, lower_bound)[0],
           remove_outliers(xtab12, upper_bound, lower_bound)[0],
           remove_outliers(xtab13, upper_bound, lower_bound)[0],
           remove_outliers(xtab14, upper_bound, lower_bound)[0],
           remove_outliers(xtab15, upper_bound, lower_bound)[0],
           remove_outliers(xtab16, upper_bound, lower_bound)[0],
           remove_outliers(xtab17, upper_bound, lower_bound)[0],
           remove_outliers(xtab18, upper_bound, lower_bound)[0],
           remove_outliers(xtab19, upper_bound, lower_bound)[0],
           remove_outliers(xtab20, upper_bound, lower_bound)[0],
           remove_outliers(xtab21, upper_bound, lower_bound)[0]]

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

    xtab_means = data_frame.pivot_table(index=['question', 'am'], values='slider_3.response', aggfunc=np.mean)
    xtab_std = data_frame.pivot_table(index=['question', 'am'], values='slider_3.response', aggfunc=np.std)
    xtab_range = data_frame.pivot_table(index=['question', 'am', 'carrier'], values='slider_3.response', aggfunc={np.min,np.max})

    wcv = xtab_std['slider_3.response']/xtab_means['slider_3.response']

    return wcv, xtab_means, xtab_range


wbcv = within_block_variance(df01)[0]
wbcv = pd.concat([wbcv,within_block_variance(df02)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df03)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df04)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df05)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df06)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df07)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df08)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df09)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df10)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df11)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df12)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df13)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df14)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df15)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df16)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df17)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df18)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df19)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df20)[0]], axis = 1)
wbcv = pd.concat([wbcv,within_block_variance(df21)[0]], axis = 1)

mean_wbcv = wbcv.mean(axis=1)
mean_wbcv_pitch = np.mean(mean_wbcv[0:7])
mean_wbcv_rough = np.mean(mean_wbcv[7:14])
mean_wbcv_trem = np.mean(mean_wbcv[14:])

plt.figure()
for i in np.arange(0,3):
    plt.plot(mean_wbcv.values[i*7:i*7+7])
plt.legend(['Pitch', 'Roughness', 'Tremolo'])

           within_block_variance(df02)[0],
           within_block_variance(df03)[0],
           within_block_variance(df04)[0],
           within_block_variance(df05)[0],
           within_block_variance(df06)[0],
           within_block_variance(df07)[0],
           within_block_variance(df08)[0],
           within_block_variance(df09)[0],
           within_block_variance(df10)[0],
           within_block_variance(df11)[0],
           within_block_variance(df12)[0],
           within_block_variance(df13)[0],
           within_block_variance(df14)[0],
           within_block_variance(df15)[0],
           within_block_variance(df16)[0],
           within_block_variance(df17)[0],
           within_block_variance(df18)[0],
           within_block_variance(df19)[0]]

agg_rating = [within_block_variance(df01)[1],
           within_block_variance(df02)[1],
           within_block_variance(df03)[1],
           within_block_variance(df04)[1],
           within_block_variance(df05)[1],
           within_block_variance(df06)[1],
           within_block_variance(df07)[1],
           within_block_variance(df08)[1],
           within_block_variance(df09)[1],
           within_block_variance(df10)[1],
           within_block_variance(df11)[1],
           within_block_variance(df12)[1],
           within_block_variance(df13)[1],
           within_block_variance(df14)[1],
           within_block_variance(df15)[1],
           within_block_variance(df16)[1],
           within_block_variance(df17)[1],
           within_block_variance(df18)[1],
           within_block_variance(df19)[1]]

range_rating = [within_block_variance(df01)[2],
           within_block_variance(df02)[2],
           within_block_variance(df03)[2],
           within_block_variance(df04)[2],
           within_block_variance(df05)[2],
           within_block_variance(df06)[2],
           within_block_variance(df07)[2],
           within_block_variance(df08)[2],
           within_block_variance(df09)[2],
           within_block_variance(df10)[2],
           within_block_variance(df11)[2],
           within_block_variance(df12)[2],
           within_block_variance(df13)[2],
           within_block_variance(df14)[2],
           within_block_variance(df15)[2],
           within_block_variance(df16)[2],
           within_block_variance(df17)[2],
           within_block_variance(df18)[2],
           within_block_variance(df19)[2]]

mean_pitch_low = []
mean_pitch_high = []
mean_rough_low = []
mean_rough_high = []
mean_trem_low = []
mean_trem_high = []
variance_pitch_low = []
variance_pitch_high = []
variance_rough_low = []
variance_rough_high = []
variance_trem_low = []
variance_trem_high = []
for i in range(len(agg_rating)):
    mean_pitch_low = np.concatenate((mean_pitch_low, agg_rating[i]['slider_3.response'].values[0:12]))
    mean_rough_low = np.concatenate((mean_rough_low, agg_rating[i]['slider_3.response'].values[21:33]))
    mean_trem_low = np.concatenate((mean_trem_low, agg_rating[i]['slider_3.response'].values[42:54]))

    mean_pitch_high = np.concatenate((mean_pitch_high,agg_rating[i]['slider_3.response'].values[12:21]))
    mean_rough_high = np.concatenate((mean_rough_high,agg_rating[i]['slider_3.response'].values[33:42]))
    mean_trem_high = np.concatenate((mean_trem_high, agg_rating[i]['slider_3.response'].values[54:]))

    variance_pitch_low = np.concatenate((variance_pitch_low, wbcv[i][0:12]))
    variance_rough_low = np.concatenate((variance_rough_low, wbcv[i][21:33]))
    variance_trem_low = np.concatenate((variance_trem_low, wbcv[i][42:54]))

    variance_pitch_high = np.concatenate((variance_pitch_high, wbcv[i][12:21]))
    variance_rough_high = np.concatenate((variance_rough_high, wbcv[i][33:42]))
    variance_trem_high = np.concatenate((variance_trem_high, wbcv[i][54:]))


plt.subplot(3,2,1)
plt.scatter(variance_pitch_low, mean_pitch_low)
plt.xlabel('Variance of pitch ratings (low freq modulators)')
plt.ylabel('Magnitude of pitch ratings')
plt.subplot(3,2,2)
plt.scatter(variance_pitch_high, mean_pitch_high)
plt.xlabel('Variance of pitch ratings (high freq modulators)')
plt.ylabel('Magnitude of pitch ratings')
plt.subplot(3,2,3)
plt.scatter(variance_rough_low, mean_rough_low)
plt.xlabel('Variance of roughness ratings (low freq modulators)')
plt.ylabel('Magnitude of roughness ratings')
plt.subplot(3,2,4)
plt.scatter(variance_rough_high, mean_rough_high)
plt.xlabel('Variance of roughness ratings (high freq modulators)')
plt.ylabel('Magnitude of roughness ratings')
plt.subplot(3,2,5)
plt.scatter(variance_trem_low, mean_trem_low)
plt.xlabel('Variance of tremolo ratings (low freq modulators)')
plt.ylabel('Magnitude of tremolo ratings')
plt.subplot(3,2,6)
plt.scatter(variance_trem_high, mean_trem_high)
plt.xlabel('Variance of tremolo ratings (high freq modulators)')
plt.ylabel('Magnitude of tremolo ratings')

variance_pitch = np.concatenate((variance_pitch_low,variance_pitch_high))
variance_rough = np.concatenate((variance_rough_low,variance_rough_high))
variance_trem = np.concatenate((variance_trem_low,variance_trem_high))
mean_pitch = np.concatenate((mean_pitch_low,mean_pitch_high))
mean_rough = np.concatenate((mean_rough_low,mean_rough_high))
mean_trem = np.concatenate((mean_trem_low,mean_trem_high))

plt.subplot(3, 1, 1)
plt.scatter(variance_pitch, mean_pitch)
plt.xlabel('Within participant pitch response range')
plt.ylabel('Frequency')
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Covariance of ratings between blocks')
plt.subplot(3, 1, 2)
plt.scatter(variance_rough, mean_rough)
plt.xlabel('Within participant roughness response range')
plt.ylabel('Frequency')
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.subplot(3, 1, 3)
plt.scatter(variance_trem, mean_trem)
plt.xlabel('Within participant tremolo response range')
plt.ylabel('Frequency')
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)

plt.hist(wbcv)
plt.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6',
            'Participant 7', 'Participant 8', 'Participant 9', 'Participant 10', 'Participant 11', 'Participant 12',
            'Participant 13', 'Participant 14', 'Participant 15', 'Participant 16', 'Participant 17', 'Participant 18',
            'Participant 19'], loc='best')
bins = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
plt.xticks(bins, labels)
plt.xlabel('Between block response range')
plt.ylabel('Frequency')

fig, ax = plt.subplots(1, 2, figsize=(12, 7))
for i in range(len(wbcv)):
    # plot the between block variance of pitch at modulators = {5, 10, 20 ,40, 80} hz
    plt.subplot(1, 2, 1)
    plt.hist(wbcv[i][0:15], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Pitch at modulators = {5, 10, 20 ,40, 80} hz')

    # plot the between block variance of pitch at modulators = {160, 320} hz
    plt.subplot(1, 2, 2)
    plt.hist(wbcv[i][15:21], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Pitch at modulators = {160, 320} hz')

fig.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6', 'Participant 7', 'Participant 8', 'Participant 9', 'Participant 10', 'Participant 11', 'Participant 12', 'Participant 13', 'Participant 14', 'Participant 15', 'Participant 16', 'Participant 17', 'Participant 18', 'Participant 19'], loc='center right')

fig, ax = plt.subplots(1, 2, figsize=(12, 7))
for i in range(len(wbcv)):
    # plot the between block variance of roughness at modulators = {5, 10, 20} hz
    plt.subplot(1, 2, 1)
    plt.hist(wbcv[i][21:30], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Roughness at modulators = {5, 10, 20} hz')

    # plot the between block variance of roughness at modulators = {40, 80, 160, 320} hz
    plt.subplot(1, 2, 2)
    plt.hist(wbcv[i][30:42], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Roughness at modulators = {40, 80, 160, 320} hz')

fig.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6', 'Participant 7', 'Participant 8', 'Participant 9', 'Participant 10', 'Participant 11', 'Participant 12', 'Participant 13', 'Participant 14', 'Participant 15', 'Participant 16', 'Participant 17', 'Participant 18', 'Participant 19'], loc='center right')

fig, ax = plt.subplots(1, 2, figsize=(12, 7))
for i in range(len(wbcv)):
    # plot the between block variance of tremolo at modulators = {5, 10, 20, 40} hz
    plt.subplot(1, 2, 1)
    plt.hist(wbcv[i][42:54], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Tremolo at modulators = {5, 10, 20, 40} hz')

    # plot the between block variance of tremolo at modulators = {80, 160, 320} hz
    plt.subplot(1, 2, 2)
    plt.hist(wbcv[i][54:], alpha=0.5, edgecolor='black', linewidth=1.2, ls='solid')
    plt.ylabel('Frequency')
    plt.xlabel('Within participant variance between blocks')
    for tag in ['top', 'right']:
        plt.gca().spines[tag].set_visible(False)
    plt.title('Tremolo at modulators = {80, 160, 320} hz')

fig.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5', 'Participant 6', 'Participant 7', 'Participant 8', 'Participant 9', 'Participant 10', 'Participant 11', 'Participant 12', 'Participant 13', 'Participant 14', 'Participant 15', 'Participant 16', 'Participant 17', 'Participant 18', 'Participant 19'], loc='center right')#

