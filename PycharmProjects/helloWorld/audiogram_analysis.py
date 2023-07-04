import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# use the whole path file name with a double slash before 'User'
df07 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s007_Roughness._2023_Jul_03_1305.csv")
df08 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s008_Roughness._2023_Jul_03_1505.csv")
df09 = pd.read_csv("C:\\Users\ktamp\OneDrive\Desktop\The-shape-of-sound-provisional-master\data\s009_Roughness._2023_Jul_04_1313.csv")


def prep(data_frame):
    # Keep only rows with slider responses
    drops = np.isnan(data_frame['text_23.started'].values) == False
    data_frame = data_frame[drops]

    data_frame = data_frame[['carrier2', 'volume2', 'key_resp_12.keys']]

    xtab = data_frame.pivot(index='volume2', columns='carrier2', values='key_resp_12.keys')

    xtab = xtab.iloc[::-1]

    xtab = xtab.replace({'space': 1, 'None': 0})

    return xtab


xtab7 = prep(df07)
xtab8 = prep(df08)
xtab9 = prep(df09)


x_labels = ['440.0', '700.0', '1000.0']
y_labels = ['0.00195312', '0.00390625', '0.0078125', '0.015625', '0.03125', '0.0625', '0.125', '0.25', '0.5', '1']

fig = plt.figure()
cax = plt.matshow(xtab7, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax)
plt.grid(True)
plt.show()

fig = plt.figure()
cax2 = plt.matshow(xtab8, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax2)
plt.grid(True)
plt.show()

fig = plt.figure()
cax3 = plt.matshow(xtab9, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax3)
plt.grid(True)
plt.show()