import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# use the whole path file name with a double slash before 'User'
df01 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S001_Roughness._2023_Jun_29_1205.csv")
df02 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s002_Roughness._2023_Jun_29_1409.csv")
df03 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\S003_Roughness._2023_Jun_29_1603.csv")


def prep(data_frame):
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['slider_3.response'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['carrier', 'am', 'question', 'slider_3.response', 'slider_3.rt']]

    xtab = data_frame.pivot_table(index=['question', 'am'])

    response_time = data_frame['slider_3.rt'].to_frame()

    ratings = xtab['slider_3.response'].values.reshape(3, 7).T
    amp = np.unique(data_frame['am'].values)

    return xtab, response_time, amp, ratings


xtab1, rt1, am, _ = prep(df01)
xtab2, rt2, _, _ = prep(df02)
xtab3, rt3, _, _ = prep(df03)

ratings = [prep(df01)[3], prep(df02)[3], prep(df03)[3]]

plt.plot(ratings[0], linestyle='solid')
plt.plot(ratings[1], linestyle='dashed')
plt.plot(ratings[2], linestyle='dotted')

