import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create array of excel file names
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
         'S019_Roughness._2023_Jul_11_1622.csv',
         'S020_Roughness._2023_Jul_12_1208.csv',
         's021_Roughness._2023_Jul_12_1607.csv']


# define function to pre-process data
def prep(data_frame_names,idx):

    csv_file = 'C://Users/ktamp/OneDrive/Desktop/The-shape-of-sound-provisional-master/data/' + data_frame_names[idx]
    data_frame = pd.read_csv(csv_file)

    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_3.response'].values) == False
    data_frame = data_frame[drops]

    # keep only columns of interest
    data_frame = data_frame[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    # reshape data frame into tables one with a 'carrier' column the other without
    xtab = data_frame.pivot_table(index=['question', 'am', 'carrier'])
    xtab_agg = data_frame.pivot_table(index=['question', 'am'])

    # isolate response times
    response_time = data_frame['slider_3.rt'].to_frame()

    # save unique modulator and carrier values
    amp = np.unique(data_frame['am'].values)
    carr = np.unique(data_frame['carrier'].values)

    return xtab, response_time, amp, carr, data_frame, xtab_agg


# prep all data sets and create rt variable with all response times
df_collection = {}
xtab_collection = {}
xtab_agg_collection = {}
xtab_collection[0], rt, am, carrier, df_collection[0], xtab_agg_collection[0] = prep(names,0)
for i in range(len(names)-1):

    xtab_collection[i+1], response_time, _, _, df_collection[i+1], xtab_agg_collection[i+1] = prep(names, i+1)
    rt = pd.concat([rt, response_time])

# find upper and lower bounds to be used for outlier exclusion
M = np.mean(rt.values)
SD = np.std(rt.values)
lower_bound = M - 2*SD
upper_bound = M + 2*SD

# define function for removing outliers from both versions of the dataset tables
def remove_outliers(xtab_collection, xtab_agg_collection, upper, lower, idx):

    # if response time falls outside bounds, replace its slider response with 'Outlier'
    drops = ((xtab_collection[idx]['slider_3.rt'].values > upper) | (xtab_collection[idx]['slider_3.rt'].values < lower))
    xtab_collection[idx][drops==True] = 'Outlier'

    drops_agg = ((xtab_agg_collection[idx]['slider_3.rt'].values > upper) | (xtab_agg_collection[idx]['slider_3.rt'].values < lower))
    xtab_agg_collection[idx][drops_agg == True] = 'Outlier'

    # reshape the two tables for use in calculating means
    ratings = xtab_collection[idx]['slider_3.response'].values.reshape(3, 7, 3).T
    agg_ratings = xtab_agg_collection[idx]['slider_3.response'].values.reshape(3, 7).T

    return ratings, agg_ratings


# remove the outlier from all data sets
ratings_collection = {}
agg_ratings_collection = {}
for i in range(len(names)):
    ratings_collection[i], agg_ratings_collection[i] = remove_outliers(xtab_collection, xtab_agg_collection, upper_bound, lower_bound, i)


# create arrays of zeros
temp = np.zeros((len(agg_ratings_collection), 1))
result = np.zeros((len(agg_ratings_collection[0]), 3))
standard_deviation = np.zeros((len(agg_ratings_collection[0]), 3))

# go through all ratings per question, modulator, and participant and calculate the mean rating
for k in np.arange(0,3):
    for j in range(len(agg_ratings_collection[0])):
        for i in range(len(agg_ratings_collection)):
            if agg_ratings_collection[i][j][k] != 'Outlier':
                temp[i] = agg_ratings_collection[i][j][k]
            else:
                # if value is an outlier, use nan in its place inside temp
                temp[i] = 'NaN'

        # calculate the standard deviation and mean of each modulator for each question
        standard_deviation[j][k] = np.nanstd(output)
        result[j][k] = np.nanmean(output)


# calculate between subject coefficient of variation for each modulator frequency and percept.
btw_var = standard_deviation/result

# define function to calculate the within block variance --> But aggregate across carriers.
def within_block_variance(data_frame):

    xtab_means = data_frame.pivot_table(index=['question', 'am'], values='slider_3.response', aggfunc=np.mean)
    xtab_std = data_frame.pivot_table(index=['question', 'am'], values='slider_3.response', aggfunc=np.std)

    wcv = xtab_std['slider_3.response']/xtab_means['slider_3.response']

    return wcv


# calculate the within participant variance between blocks for each participant
wbcv_collection = within_block_variance(df_collection[0])
for i in range(len(names)-1):
    wbcv_collection = pd.concat([wbcv_collection,within_block_variance(df_collection[i+1])], axis = 1)

# calculate the mean across participants
mean_wbcv = wbcv_collection.mean(axis=1)

# plot the mean ratings aggregated across carriers
plt.figure()
plt.plot(np.arange(7), result, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequency (Hz)')
plt.ylabel('Perceived Difference Rating')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Mean rating per percept and modulator')

# plot between and within participant variance using the same metric (std/mean)
plt.figure()
plt.subplot(1,2,1)
plt.plot(np.arange(7), btw_var, lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequency (Hz)')
plt.ylabel('Coefficient of variance')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Between participant variance')

plt.subplot(1,2,2)
for i in np.arange(0,3):
    plt.plot(np.arange(7), mean_wbcv.values[i*7:i*7+7], lw=2)
plt.xticks(np.arange(7), am)
plt.xlabel('Amplitude Modulation Frequency (Hz)')
plt.ylabel('Coefficient of variance')
plt.legend(['Pitch', 'Roughness', 'Tremolo'])
plt.grid(True)
for tag in ['top', 'right']:
    plt.gca().spines[tag].set_visible(False)
plt.title('Within participant variance')