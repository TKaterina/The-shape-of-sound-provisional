# TWO SAMPLE T-TEST FOR COMPARING MUSICALLY INEXPERIENCED AND EXPERIENCED PARTICIPANTS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# create array of excel file names (Remove participant 2 due to mutliple outliers)
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


ratings_experience = []
ratings_inexperience = []
am = []
response_time =[]
# df_collection to be used for outlier exclusion
df_collection = {}


# prep data frames
for ii in range(len(names)):

    csv_files = csv_file = 'C://Users/ktamp/OneDrive/Desktop/The-shape-of-sound-provisional-master/data/' + names[ii]
    df = pd.read_csv(csv_files)

    # Keep only rows with slider responses
    drops = np.isnan(df['slider_3.response'].values) == False
    df = df[drops]

    df = df[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]
    df_collection[ii] = df

    am.append(np.unique(df['am'].values))
    response_time.append(df['slider_3.rt'].to_frame())


rts = response_time[0]
for i in range(len(names)-1):
    rts = np.concatenate((rts, response_time[i+1]))


M = np.mean(rts)
SD = np.std(rts)
lower_bound = M - 2*SD
upper_bound = M + 2*SD

# create boolean variable splitting participants into experienced and inexperienced
exp = ['True','False', 'True', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 'False',
       'True', 'True', 'False', 'True', 'True', 'True']

# remove outliers based on upper and lower bound
for ii in range(len(df_collection)):
    drops = ((df_collection[ii]['slider_3.rt'].values > upper_bound) | (df_collection[ii]['slider_3.rt'].values < lower_bound))
    df_collection[ii][drops == True] = np.nan

    xtab = df_collection[ii].pivot_table(index=['question', 'am'])

    # condition removes participant 2 from final ratings variables and inner loop separated ppt based on experience
    if ii != 1:
        if exp[ii] == 'True':
            ratings_experience.append(xtab['slider_3.response'].values.reshape(3, 7).T)
        else:
            ratings_inexperience.append(xtab['slider_3.response'].values.reshape(3, 7).T)



# ppts x am x question
ratings_experience = np.concatenate([rt[None, :, :] for rt in ratings_experience], axis=0)
ratings_inexperience = np.concatenate([rt[None, :, :] for rt in ratings_inexperience], axis=0)

# comparing experience X no experience for all each sensation
for ii in np.arange(0,3):
    X = np.vstack((ratings_experience[:,:,ii], ratings_inexperience[:,:,ii]))
    groups = np.repeat([1,2], 10)

    nperms = 1500
    nulls = np.zeros((nperms,))

    ratings_t, ratings_p = stats.ttest_ind(X[groups==1, :], X[groups==2, :], axis=0)
    nulls[0] = ratings_t.max()  # First null is the same as the observed data

    # Randomly rearrange group memberships for all data
    for jj in range(1, nperms):
        perm_groups = groups[np.random.permutation(np.arange(20))]
        t, p = stats.ttest_ind(X[perm_groups==1, :], X[perm_groups==2, :], axis=0)
        nulls[jj] = t.max()

    thresh = np.percentile(nulls, [95, 99, 99.9])

    plt.figure()
    plt.subplot(121)
    plt.plot((thresh[0], thresh[0]), (0, 250), 'k')
    plt.plot((thresh[1], thresh[1]), (0, 250), 'k--')
    plt.plot((thresh[2], thresh[2]), (0, 250), 'k:')
    plt.legend(['p=0.05', 'p=0.01', 'p=0.001'])
    plt.hist(nulls, 64)
    plt.xlabel('t-value')
    plt.ylabel('number of occurences')

    plt.subplot(122)
    plt.plot(ratings_t)
    plt.plot((0, 6), (thresh[0], thresh[0]), 'k')
    plt.plot((0, 6), (thresh[1], thresh[1]), 'k--')
    plt.plot((0, 6), (thresh[2], thresh[2]), 'k:')
    plt.legend(['Tremolo - Roughness', 'p=0.05', 'p=0.01', 'p=0.001'])
    plt.plot((0, 6), (-thresh[0], -thresh[0]), 'k')
    plt.plot((0, 6), (-thresh[1], -thresh[1]), 'k--')
    plt.plot((0, 6), (-thresh[2], -thresh[2]), 'k:')

    plt.xticks(np.arange(7), am[0])
    plt.xlabel('Amplitude Modulation Frequenacy (Hz)')
    plt.ylabel('t-value')

    plt.suptitle('permutation t-tests for difference between percepts')
