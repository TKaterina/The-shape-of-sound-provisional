# PAIRED SAMPLES T-TESTS SEPARATED BY CARRIER

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy import stats

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


ratings440 = []
ratings700 = []
ratings1000 = []
am = []
response_time = []
# df_collection variables to be used for outlier exclusion
df_collection_440 = {}
df_collection_700 = {}
df_collection_1000 = {}

# prep data frames
for ii in range(len(names)):

    csv_files = csv_file = 'C://Users/ktamp/OneDrive/Desktop/The-shape-of-sound-provisional-master/data/' + names[ii]
    df = pd.read_csv(csv_files)

    drops = np.isnan(df['slider_3.response'].values) == False
    df = df[drops]
    df = df[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    drops440 = df['carrier'].values == 440
    drops700 = df['carrier'].values == 700
    drops1000 = df['carrier'].values == 1000

    df440 = df[drops440]
    df700 = df[drops700]
    df1000 = df[drops1000]

    df_collection_440[ii] = df440
    df_collection_700[ii] = df700
    df_collection_1000[ii] = df1000

    response_time.append(df['slider_3.rt'].to_frame())

    am.append(np.unique(df['am'].values))


rts = response_time[0]
for i in range(len(names)-1):
    rts = np.concatenate((rts, response_time[i+1]))


M = np.mean(rts)
SD = np.std(rts)
lower_bound = M - 2*SD
upper_bound = M + 2*SD

# remove outliers based on upper and lower bound
for ii in range(len(df_collection_440)):
    drops440 = ((df_collection_440[ii]['slider_3.rt'].values > upper_bound) | (df_collection_440[ii]['slider_3.rt'].values < lower_bound))
    df_collection_440[ii][drops440 == True] = np.nan

    drops700 = ((df_collection_700[ii]['slider_3.rt'].values > upper_bound) | (df_collection_700[ii]['slider_3.rt'].values < lower_bound))
    df_collection_700[ii][drops700 == True] = np.nan

    drops1000 = ((df_collection_1000[ii]['slider_3.rt'].values > upper_bound) | (df_collection_1000[ii]['slider_3.rt'].values < lower_bound))
    df_collection_1000[ii][drops1000 == True] = np.nan

    xtab440 = df_collection_440[ii].pivot_table(index=['question', 'am'])
    xtab700 = df_collection_700[ii].pivot_table(index=['question', 'am'])
    xtab1000 = df_collection_1000[ii].pivot_table(index=['question', 'am'])

    # condition removes participant 2 from final ratings variables
    if ii != 1:
        ratings440.append(xtab440['slider_3.response'].values.reshape(3, 7).T)
        ratings700.append(xtab700['slider_3.response'].values.reshape(3, 7).T)
        ratings1000.append(xtab1000['slider_3.response'].values.reshape(3, 7).T)


# # Paired-sample t-test
ratings_coll = [ratings440, ratings700, ratings1000]

# ppts x am x question
for ii in np.arange(0,1):

    ratings = np.concatenate([rt[None, :, :] for rt in ratings_coll[ii]], axis=0)

    A = ratings[:, :, 0] # pitch
    B = ratings[:, :, 1] # roughness
    C = ratings[:, :, 2] # tremolo

    nperms = 1500
    nulls1 = np.zeros((nperms,))
    nulls2 = np.zeros((nperms,))
    nulls3 = np.zeros((nperms,))

    ratings_t1, ratings_p1 = stats.ttest_rel(A, B, axis=0) # pitch-roughness
    ratings_t2, ratings_p2 = stats.ttest_rel(A, C, axis=0)
    ratings_t3, ratings_p3 = stats.ttest_rel(B, C, axis=0)
    nulls1[0] = ratings_t1.max()  # First null is the same as the observed data
    nulls2[0] = ratings_t2.max()
    nulls3[0] = ratings_t3.max()

    # Pitch - Roughness
    for kk in range(1, nperms):
        swaps = np.random.choice([0, 1], 20)
        perm_A = A.copy()
        perm_B = B.copy()
        for jj in range(len(swaps)):
            if swaps[jj] == 1:
                perm_A[jj, :] = B[jj, :]
                perm_B[jj, :] = A[jj, :]
        t, p = stats.ttest_ind(perm_A, perm_B, axis=0)
        nulls1[kk] = t.max()

    thresh1 = np.percentile(nulls1, [95, 99, 99.9])

    # Pitch - Tremolo
    for kk in range(1, nperms):
        swaps = np.random.choice([0, 1], 20)
        perm_A = A.copy()
        perm_C = C.copy()
        for jj in range(len(swaps)):
            if swaps[jj] == 1:
                perm_A[jj, :] = C[jj, :]
                perm_C[jj, :] = A[jj, :]
        t, p = stats.ttest_ind(perm_A, perm_C, axis=0)
        nulls2[kk] = t.max()

    thresh2 = np.percentile(nulls2, [95, 99, 99.9])

    # Tremolo - Roughness
    for kk in range(1, nperms):
        swaps = np.random.choice([0, 1], 20)
        perm_B = B.copy()
        perm_C = C.copy()
        for jj in range(len(swaps)):
            if swaps[jj] == 1:
                perm_B[jj, :] = C[jj, :]
                perm_C[jj, :] = B[jj, :]
        t, p = stats.ttest_ind(perm_B, perm_C, axis=0)
        nulls3[kk] = t.max()

    thresh3 = np.percentile(nulls3, [95, 99, 99.9])

    plt.figure()
    plt.subplot(121)
    plt.plot((thresh1[0], thresh1[0]), (0, 250), 'k')
    plt.plot((thresh1[1], thresh1[1]), (0, 250), 'k--')
    plt.plot((thresh1[2], thresh1[2]), (0, 250), 'k:')
    plt.legend(['p=0.05', 'p=0.01', 'p=0.001'])
    plt.hist(nulls1, 64, color='b')
    plt.xlabel('t-value')
    plt.ylabel('number of occurences')
    plt.title('Pitch-Roughness')


    plt.subplot(122)
    plt.plot(ratings_t1, color='b')
    plt.plot((0, 6), (thresh1[0], thresh1[0]), 'k')
    plt.plot((0, 6), (thresh1[1], thresh1[1]), 'k--')
    plt.plot((0, 6), (thresh1[2], thresh1[2]), 'k:')
    plt.legend(['Pitch-Roughness','p=0.05', 'p=0.01', 'p=0.001'])
    plt.plot((0, 6), (-thresh1[0], -thresh1[0]), 'k')
    plt.plot((0, 6), (-thresh1[1], -thresh1[1]), 'k--')
    plt.plot((0, 6), (-thresh1[2], -thresh1[2]), 'k:')
    plt.xticks(np.arange(7), am[0])
    plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
    plt.ylabel('t-value')

    plt.figure()
    plt.subplot(121)
    plt.plot((thresh2[0], thresh2[0]), (0, 250), 'k')
    plt.plot((thresh2[1], thresh2[1]), (0, 250), 'k--')
    plt.plot((thresh2[2], thresh2[2]), (0, 250), 'k:')
    plt.legend(['p=0.05', 'p=0.01', 'p=0.001'])
    plt.hist(nulls2, 64, color='r')
    plt.xlabel('t-value')
    plt.ylabel('number of occurences')
    plt.title('Tremolo-Pitch')

    plt.subplot(122)
    plt.plot(ratings_t2, color='r')
    plt.plot((0, 6), (thresh2[0], thresh2[0]), 'k')
    plt.plot((0, 6), (thresh2[1], thresh2[1]), 'k--')
    plt.plot((0, 6), (thresh2[2], thresh2[2]), 'k:')
    plt.legend(['Pitch-Tremolo', 'p=0.05', 'p=0.01', 'p=0.001'])
    plt.plot((0, 6), (-thresh2[0], -thresh2[0]), 'k')
    plt.plot((0, 6), (-thresh2[1], -thresh2[1]), 'k--')
    plt.plot((0, 6), (-thresh2[2], -thresh2[2]), 'k:')
    plt.xticks(np.arange(7), am[0])
    plt.xlabel('Amplitude Modulation Frequency (Hz)')
    plt.ylabel('t-value')

    plt.figure()
    plt.subplot(121)
    plt.plot((thresh3[0], thresh3[0]), (0, 250), 'k')
    plt.plot((thresh3[1], thresh3[1]), (0, 250), 'k--')
    plt.plot((thresh3[2], thresh3[2]), (0, 250), 'k:')
    plt.legend(['p=0.05', 'p=0.01', 'p=0.001'])
    plt.hist(nulls3, 64, color='g')
    plt.xlabel('t-value')
    plt.ylabel('number of occurences')
    plt.title('440 Hz Carrier')

    plt.subplot(122)
    plt.plot(ratings_t3, color='g')
    plt.plot((0, 6), (thresh3[0], thresh3[0]), 'k')
    plt.plot((0, 6), (thresh3[1], thresh3[1]), 'k--')
    plt.plot((0, 6), (thresh3[2], thresh3[2]), 'k:')
    plt.legend(['Roughness-Tremolo', 'p=0.05', 'p=0.01', 'p=0.001'])
    plt.plot((0, 6), (-thresh3[0], -thresh3[0]), 'k')
    plt.plot((0, 6), (-thresh3[1], -thresh3[1]), 'k--')
    plt.plot((0, 6), (-thresh3[2], -thresh3[2]), 'k:')
    plt.xticks(np.arange(7), am[0])
    plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
    plt.ylabel('t-value')
    plt.suptitle('permutation paired t-tests for difference between percepts')





