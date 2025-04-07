import pandas as pd

# 가상의 락 밴드 데이터를 생성합니다.
data = {https://www.billboard.com/charts/rock-songs/
    
    'Band': ['Band A', 'Band B', 'Band C', 'Band D'],
    'Albums Sold': [500, 1500, 1000, 2000],
    'Concert Attendance': [30000, 45000, 20000, 60000],
}

# 데이터프레임을 생성합니다.
df = pd.DataFrame(data)

# 순위를 매기기 위해 'Albums Sold'와 'Concert Attendance'의 평균을 계산합니다.
df['Average Score'] = (df['Albums Sold'] + df['Concert Attendance']) / 2

# 'Average Score'를 기준으로 내림차순으로 정렬하고, 순위를 매깁니다.
df['Rank'] = df['Average Score'].rank(ascending=False)

# 결과를 출력합니다.
print(df.sort_values(by='Rank'))
