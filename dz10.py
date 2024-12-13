import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#1
ds = pd.Series(data = [1, 2, 3, 4, 'f', [1, 2, 3]], index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(ds)
ds_1 = pd.Series(data = np.array([0.1, 0.2, 0.3, 0.4]), index = [1, 2, 3, 4])
print(ds_1)
data = {'Russia' : 454351,
        'USA' : 694746,
        'China' : 947635}
df = pd.Series(data)
print(df)

#2
df = pd.DataFrame({
    'first': ['one', 'apple', 'qiwi', 'palm', 'Russia'],
    'second': [ 'banana', 'one', 'kiwi', 'Russia', 'palm']})
print(df)
print(df[df != df.loc[df['first'].isin(df['second']), 'first'].values].dropna())

#3
sr = pd.Series(['Russia', 'Russia', 'Russia', 'USA', 'China', 'USA',  'USA', 'USA', 'China', 'China', 'China', 'China', 'China'])
print(sr)

plt.bar(sr.value_counts().index, sr.value_counts().values)
plt.grid(axis = 'Series', linestyle = '--', alpha = 1.3)
plt.show()

#4
df_1 = pd.DataFrame({
    'fruits': ['kiwi', 'apple', 'orange', 'avocado', 'banana'],
    'vegetables': ['onion', 'poptato' 'beetroot', 'carrot', 'eggplant']
})
df_2 = pd.DataFrame({
    'vegetables': ['onion', 'poptato' 'beetroot', 'carrot', 'eggplant'],
    'fruits': ['kiwi', 'apple', 'orange', 'avocado', 'banana']
})
df_3 = pd.DataFrame({
    'list': ['cherry', 'melon', 'berry', 'strawberry', 'watermelon']
})
print('df_1')
print(df_1)
print('df_2')
print(df_2)
print('df_3')
print(df_3)

df_1_2 = pd.concat([df_1,df_2]).reset_index(drop=True)
df_1_2.index.name = 'Number'
print('df_1_2')
print( df_1_2)
df_1_2_3 = pd.merge(df_1_2, df_3, how = 'one more', on = 'Number')
print('df_1_2_3')
print(df_1_2_3)

#5
df_price = pd.DataFrame({
    'swimming_glasses': [13254, 14516, 1654, 9435, 6452, 21213],
    'swimming_trunks': [67333, 656185, 51344, 65266, 624465, 34411]
})
print(df_price)

plt.plot(list(df_price.index),list(df_price['swimming_glasses']), label = 'swimming_glasses', color='grey')
plt.plot(list(df_price.index),list(df_price['swimming_trunksx`']), label='swimming_trunks', color='lightblue')
plt.xlabel('Год')
plt.ylabel('Цена за штуку, руб')
plt.legend()
plt.grid()
plt.show()