import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = ['S001_Roughness._2023_Jun_29_1205.csv',
                    's002_Roughness._2023_Jun_29_1409.csv',
                    'S003_Roughness._2023_Jun_29_1603.csv',
                    's004_Roughness._2023_Jun_30_1239.csv',
                    's005_Roughness._2023_Jun_30_1400.csv',
                    'S006_Roughness._2023_Jun_30_1504.csv',
                    's007_Roughness._2023_Jul_03_1305.csv',
                    's008_Roughness._2023_Jul_03_1505.csv',
                    's009_Roughness._2023_Jul_04_1313.csv',
                    'S010_Roughness._2023_Jul_04_1433.csv',
                    's011_Roughness._2023_Jul_05_1215.csv',
                    's012_Roughness._2023_Jul_05_1304.csv',
                    's013_Roughness._2023_Jul_05_1408.csv',
                    's014_Roughness._2023_Jul_05_1515.csv',
                    'S015_Roughness._2023_Jul_07_1210.csv',
                    's016_Roughness._2023_Jul_07_1513.csv',
                    's017_Roughness._2023_Jul_11_1207.csv',
                    's018_Roughness._2023_Jul_11_1308.csv',
                    'S019_Roughness._2023_Jul_11_1622.csv']

def prep(data_frame_names,idx):

    csv_file = 'C://Users/ktamp/OneDrive/Desktop/The-shape-of-sound-provisional-master/data/' + data_frame_names[idx]
    data_frame = pd.read_csv(csv_file)
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_3.response'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    xtab = data_frame.pivot_table(index=['question', 'am', 'carrier'])
    xtab_agg = data_frame.pivot_table(index=['question', 'am'])

    response_time = data_frame['slider_3.rt'].to_frame()

    amp = np.unique(data_frame['am'].values)
    carr = np.unique(data_frame['carrier'].values)

    return xtab, response_time, amp, carr, data_frame, xtab_agg


df_collection = {}
xtab_collection = {}
xtab_agg_collection = {}
xtab_collection[0], rt, am, carrier, df_collection[0], xtab_agg_collection[0] = prep(names,0)

for i in range(len(names)-1):

    xtab_collection[i+1], response_time, _, _, df_collection[i+1], xtab_agg_collection[i+1] = prep(names, i+1)
    rt = pd.concat([rt, response_time])

M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD


def remove_outliers(xtab_collection, xtab_agg_collection, upper, lower, idx):

    # xtab = xtab.drop(xtab['slider_3.rt'].values < lower_bound | xtab['slider_3.rt'].values > upper_bound)
    drops = ((xtab_collection[idx]['slider_3.rt'].values > upper) | (xtab_collection[idx]['slider_3.rt'].values < lower))
    xtab_collection[idx][drops==True] = 'Outlier'

    drops_agg = ((xtab_agg_collection[idx]['slider_3.rt'].values > upper) | (xtab_agg_collection[idx]['slider_3.rt'].values < lower))
    xtab_agg_collection[idx][drops_agg == True] = 'Outlier'

    ratings = xtab_collection[idx]['slider_3.response'].values.reshape(3, 7, 3).T
    agg_ratings = xtab_agg_collection[idx]['slider_3.response'].values.reshape(3, 7).T

    return ratings, agg_ratings

#
# ratings_collection = {}
# agg_ratings_collection = {}
# for i in range(len(names)):
#     ratings_collection[i], agg_ratings_collection[i] = remove_outliers(xtab_collection, xtab_agg_collection, upper_bound, lower_bound, i)
#

