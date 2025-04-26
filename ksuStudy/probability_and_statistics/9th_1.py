import pandas as pd

# 기초 통계 실습
'''
인덱스 이름으로 접근 : loc[] --> ex) loc['a']
인덱스 순서/번호/숫자로 접근 : iloc[] --> ex) iloc[1]
열에 접근하는 코드 : 변수명.[]
ex) df.['lifeExp']
평균 : 변수명.mean()
최댓값 : 변수명.max()
최솟값 : 변수명.min()
중앙값 : 변수명.median()
분산 : 데이터 프레임명.var()
표준편차 : 데이터 프레임명.std()
기초통계 : 데이터 프레임명.describe()
'''

df = pd.read_csv('/Users/hyun/MYTIL/TIL/ksuStudy/probability_and_statistics/gapminder.tsv', sep = '\t')
#df


df.loc[0] # 행 선택
df.loc[[0, 10, 100, 1000]] # 여러 행에 접근

df.iloc[0] # 인덱스 번호로 접근

df['lifeExp'] # 열 선택

df['lifeExp'].mean()
df['lifeExp'].max()
df['lifeExp'].min()
df['lifeExp'].median()

df['lifeExp'].var()
df['lifeExp'].std()
df['lifeExp'].describe()