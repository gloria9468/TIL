import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns # 상자그림 그래프 그릴때 사용함.

df = pd.read_csv('/Users/hyun/MYTIL/TIL/ksuStudy/probability_and_statistics/gapminder.tsv', sep = '\t')
# df

# 히스토그램
plt.hist(df['lifeExp'])
plt.show()

plt.hist(df['lifeExp'], alpha = 0.3, bins = 7)
plt.show()

plt.hist(df['lifeExp'], alpha = 0.3, bins = 7, rwidth=2, color='red')
plt.show()

# 원그래프
df2 = df.groupby('continent')
df2.describe()

# year 컬럼의 count만 뽑기
year_count_series = df2['year'].count()

# 리스트로 변환
year_count_list = year_count_series.tolist()

# (대륙 이름, count) 형태로 리스트 만들기
#year_count_with_labels = list(zip(year_count_series.index, year_count_series.values))

print(year_count_list) # sizes = [624, 300, 396, 360, 24]
#print(year_count_with_labels)

labels = [1,2,3,4,5]
colors = ['red', 'green', 'blue', 'yellow', 'purple']
plt.pie(year_count_list, labels = labels, colors = colors, autopct = '%.1f%%', shadow= True, startangle= 90)
plt.axis('equal')
plt.show()


# 상자그림
sns.boxenplot(x='continent', y='lifeExp', data=df)
sns.boxplot(x='continent', y='lifeExp', data=df)
plt.show()