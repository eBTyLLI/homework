import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
file = 'C:/Users/...'
df = pd.read_csv(file, sep = ',')

#1
female_income = df[df['genre'] == 'Female']['Annual Income'].mean()
print('female_income:', female_income)

#2
mid_income = df['Annual Income (k$)'].median()
high_MI_men = df[(df['genre'] == 'Male') and (df['Annual Income (k$)'] > mid_income)]
high_MI_wemen = high_MI_men = df[(df['genre'] == 'Female') and (df['Annual Income (k$)'] > mid_income)]

print('Мужчин с бОльшими расходами:', high_MI_men)
print('Женщин с бОльшими расходами:', high_MI_wemen)

#3
df_men = df[df['genre'] == 'Male']
plt.figure(figuresize = (8, 6))
plt.scatter(df_men['Age'], df_men['Annual Income'], color = 'darkblue', alpha = 1.3) 
plt.title('Доход от возраста')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.grid()
plt.show()

#4
grouped = df.groupby(['Genre', 'Annual Income'])['Spending Score'].mean().unstack()
grouped.plot(kind='bar', figsize=(10, 6), color=['blue', 'red'])
plt.figure(figuresize = (13, 10))
plt.title('Расход от дохода')
plt.xlabel('Доходы')
plt.ylabel('Расходы')
plt.legend(title = 'Ламинат')
plt.grid()
plt.show()