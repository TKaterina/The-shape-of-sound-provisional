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



# instrument_names = {'C:\\Users\\axt275\\Downloads\\banjo_C4_very-long_forte_normal.wav':'banjo',
 #                   'C:\\Users\\axt275\\Downloads\\bass-clarinet_C4_1_fortissimo_normal.wav':'bass-clarinet',
  #                  'C:\\Users\\axt275\\Downloads\\cello_C4_1_fortissimo_arco-normal.wav':'cello',
   #                 'C:\\Users\\axt275\\Downloads\\clarinet_C4_1_fortissimo_normal.wav':'clarinet',
    #                'C:\\Users\\axt275\\Downloads\\flute_C4_1_forte_normal.wav':'flute',
     #               'C:\\Users\\axt275\\Downloads\\french-horn_C4_very-long_forte_normal.wav':'french-horn',
      #              'C:\\Users\\axt275\\Downloads\\guitar_C4_very-long_forte_normal.wav':'guitar',
       #             'C:\\Users\\axt275\\Downloads\\oboe_C4_1_fortissimo_normal.wav':'oboe',
        #            'C:\\Users\\axt275\\Downloads\\trumpet_C4_1_fortissimo_normal.wav':'trumpet',
         #           'C:\\Users\\axt275\\Downloads\\tuba_C4_1_fortissimo_normal.wav':'tuba',
          #          'C:\\Users\\axt275\\Downloads\\viola_C4_1_fortissimo_arco-normal.wav':'viola',
           #         'C:\\Users\\axt275\\Downloads\\violin_C4_1_fortissimo_arco-normal.wav':'violin'}

def prep(data_frame):
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_2.response'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['instrument1', 'instrument2','slider_2.response', 'slider_2.rt']]

    response_time = data_frame['slider_2.rt'].to_frame()

    # data_frame = data_frame.rename(index=instrument_names)

    return data_frame, response_time


xtab1, rt1 = prep(df01)
xtab2, rt2 = prep(df02)
xtab3, rt3 = prep(df03)
xtab4, rt4 = prep(df04)
xtab5, rt5 = prep(df05)
xtab6, rt6 = prep(df06)
xtab7, rt7 = prep(df07)
xtab8, rt8 = prep(df08)
xtab9, rt9 = prep(df09)
xtab10, rt10 = prep(df10)
xtab11, rt11 = prep(df11)
xtab12, rt12 = prep(df12)
xtab13, rt13 = prep(df13)
xtab14, rt14 = prep(df14)
xtab15, rt15 = prep(df15)


rt = pd.concat([rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10, rt11, rt12, rt13, rt14, rt15])

M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD


def remove_outliers(xtab,upper,lower):

    # xtab = xtab.drop(xtab['slider_3.rt'].values < lower_bound | xtab['slider_3.rt'].values > upper_bound)
    drops = ((xtab['slider_2.rt'].values > upper) | (xtab['slider_2.rt'].values < lower))
    xtab.loc[drops==True, 'slider_2.rt'] = 'Outlier'

    xtab = xtab.pivot_table(index='instrument1', columns='instrument2', values='slider_2.response')
    # ratings = xtab['slider_2.response'].values.reshape(11, 6).T
    #  ratings = xtab['slider_3.response'].values.reshape(12, 12).T

    return xtab


ratings = [remove_outliers(xtab1, upper_bound, lower_bound),
           remove_outliers(xtab2, upper_bound, lower_bound),
           remove_outliers(xtab3, upper_bound, lower_bound),
           remove_outliers(xtab4, upper_bound, lower_bound),
           remove_outliers(xtab5, upper_bound, lower_bound),
           remove_outliers(xtab6, upper_bound, lower_bound),
           remove_outliers(xtab7, upper_bound, lower_bound),
           remove_outliers(xtab8, upper_bound, lower_bound),
           remove_outliers(xtab9, upper_bound, lower_bound),
           remove_outliers(xtab10, upper_bound, lower_bound),
           remove_outliers(xtab11, upper_bound, lower_bound),
           remove_outliers(xtab12, upper_bound, lower_bound),
           remove_outliers(xtab13, upper_bound, lower_bound),
           remove_outliers(xtab14, upper_bound, lower_bound),
           remove_outliers(xtab15, upper_bound, lower_bound)]

output = np.zeros((len(ratings), 1))
result = np.zeros((len(ratings[0]), len(ratings[0])))
# standard_deviation = np.zeros((len(ratings[0]), 3))
for k in range(len(ratings[0].values[0])):
    for j in range(len(ratings[0])):
        for i in range(len(ratings)):
            if (ratings[i].values[j][k] != 'Outlier') | (np.isnan(ratings[i].values[j][k])):
                output[i] = ratings[i].values[j][k]
            else:
                output[i] = 'NaN'

        result[j][k] = np.nanmean(output)
        # standard_deviation[j][k] = np.nanstd(output)

x_labels = ['bass-clarinet', 'cello', 'clarinet', 'flute', 'french-horn', 'guitar', 'oboe', 'trumpet', 'tuba', 'viola', 'violin']
y_labels = ['banjo','bass-clarinet', 'cello', 'clarinet', 'flute', 'french-horn', 'guitar', 'oboe', 'trumpet', 'tuba', 'viola']

cax = plt.matshow(result)
plt.title('Similarity matrix for instrument pairs')
plt.xticks(range(11), x_labels, rotation=90)
plt.yticks(range(11), y_labels)
plt.colorbar(cax)
plt.show()
