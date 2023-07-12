import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# use the whole path file name with a double slash before 'User'
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
xtab10 = prep(df10)
xtab11 = prep(df11)
xtab12 = prep(df12)
xtab13 = prep(df13)
xtab14 = prep(df14)
xtab15 = prep(df15)
xtab16 = prep(df16)
xtab17 = prep(df17)
xtab18 = prep(df18)
xtab19 = prep(df19)

x_labels = ['440.0', '700.0', '1000.0']
y_labels = ['1', '0.5', '0.25', '0.125', '0.0625', '0.03125', '0.015625', '0.0078125', '0.00390625', '0.00195312']

# good audiogram
cax = plt.matshow(xtab7, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax)
plt.grid(True)

# good audiogram
cax2 = plt.matshow(xtab8, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax2)
plt.grid(True)

# good audiogram
cax3 = plt.matshow(xtab9, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax3)
plt.grid(True)

#good audiogram
cax4 = plt.matshow(xtab10, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax4)
plt.grid(True)

cax5 = plt.matshow(xtab11, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax5)
plt.grid(True)

cax6 = plt.matshow(xtab12, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax6)
plt.grid(True)

cax7 = plt.matshow(xtab13, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax7)
plt.grid(True)

# good audiogram
cax8 = plt.matshow(xtab14, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax8)
plt.grid(True)

cax9 = plt.matshow(xtab15, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax9)
plt.grid(True)

# good audiogram
cax10 = plt.matshow(xtab16, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax10)
plt.grid(True)

# good audiogram
cax11 = plt.matshow(xtab17, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax11)
plt.grid(True)

#good audiogram
cax12 = plt.matshow(xtab18, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax12)
plt.grid(True)

# PERFECT audiogram
cax13 = plt.matshow(xtab19, cmap=plt.cm.gray_r)
plt.title('Audiogram')
plt.xticks(range(3), x_labels, rotation=90)
plt.yticks(range(10), y_labels)
plt.colorbar(cax13)
plt.grid(True)