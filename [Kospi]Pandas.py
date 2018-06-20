import pandas as pd

def get_url():
    url = 'http://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI'
    print("요청 URL = {}".format(url))
    return url

url = get_url()
df = pd.DataFrame()
print(url)
for page in range(1, 6):
    pg_url = '{url}&page={page}'.format(url=url, page=page)
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

df = df.rename(columns= {'날짜': 'date', '체결가': 'close', '전일비': 'diff','등락률': 'updown', '거래량(천주)': 'volume', '거래대금(백만)': 'price'})
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by=['date'], ascending=True)
df2 = df[['date', 'close']]
df2 = df2.dropna(how='all')

print(df2)