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



# filename = ["C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S001_Roughness._2023_Jun_29_1205.csv",
#                "C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s002_Roughness._2023_Jun_29_1409.csv",
 #               "C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S003_Roughness._2023_Jun_29_1603.csv",
  #              "C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s004_Roughness._2023_Jun_30_1239.csv",
   #             "C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s005_Roughness._2023_Jun_30_1400.csv",
    #        "C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S006_Roughness._2023_Jun_30_1504.csv"]

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
xtab7, rt7, _ = prep(df07)
xtab8, rt8, _ = prep(df08)
xtab9, rt9, _ = prep(df09)
xtab10, rt10, _ = prep(df10)
xtab11, rt11, _ = prep(df11)
xtab12, rt12, _ = prep(df12)
xtab13, rt13, _ = prep(df13)
xtab14, rt14, _ = prep(df14)
xtab15, rt15, _ = prep(df15)

rt = pd.concat([rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10, rt11, rt12, rt13, rt14, rt15])


M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD

# plot the response times
bins = np.linspace(0, 15, 15)
plt.hist(rt, bins)
plt.axvline(upper_bound, color='r', ls='dotted')
plt.axvline(M, color='k', ls='dashed')
plt.title('Histogram of response times')
plt.ylabel('Frequency')
plt.xlabel('Time (seconds)')
plt.xticks(bins, rotation=45)
plt.legend(['Upper outlier bound', 'Mean response time', 'Response times'])

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
           remove_outliers(xtab6, upper_bound, lower_bound)[0],
           remove_outliers(xtab7, upper_bound, lower_bound)[0],
           remove_outliers(xtab8, upper_bound, lower_bound)[0],
           remove_outliers(xtab9, upper_bound, lower_bound)[0],
           remove_outliers(xtab10, upper_bound, lower_bound)[0],
           remove_outliers(xtab11, upper_bound, lower_bound)[0],
           remove_outliers(xtab12, upper_bound, lower_bound)[0],
           remove_outliers(xtab13, upper_bound, lower_bound)[0],
           remove_outliers(xtab14, upper_bound, lower_bound)[0],
           remove_outliers(xtab15, upper_bound, lower_bound)[0]]

output = np.zeros((len(ratings), 1))
result = np.zeros((len(ratings[0]), 3))
variance = np.zeros((len(ratings[0]), 3))
standard_deviation = np.zeros((len(ratings[0]), 3))
n_obs = np.zeros((len(ratings[0]), 3))

for k in np.arange(0,3):
    for j in range(len(ratings[0])):
        count = 0
        for i in range(len(ratings)):
            if ratings[i][j][k] != 'Outlier':
                output[i] = ratings[i][j][k]
                count += 1
            else:
                output[i] = 'NaN'

        n_obs[j][k] = count
        variance[j][k] = np.nanvar(output)
        standard_deviation[j][k] = np.nanstd(output)
        result[j][k] = np.nanmean(output)


plt.figure()
plt.plot(np.arange(7), result, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequency (Hz)')
plt.ylabel('Perceived Difference Rating')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')

# calculation of between subject coefficient of variation for each modulator frequency and percept.
btw_var = np.sqrt(n_obs * variance) / result
btw_var2 = standard_deviation/result

plt.figure()
plt.plot(np.arange(7), btw_var2, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequency (Hz)')
plt.ylabel('Covariance of ratings')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Percept x AM freq')
