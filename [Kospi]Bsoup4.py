from bs4 import BeautifulSoup
import urllib.request as req

def get_url():
    url = 'http://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI'
    return url
url = get_url()

def get_num():
    num_list = soup.find_all("td", class_="number_1")
    num_result = []
    for num in num_list:
        nums = num.string
        num_result.append(nums)
        num_endunum = num_result[0:24:4]
    return num_endunum

def get_day():
    day_list = soup.find_all("td", class_="date")
    day_result = []
    for day in day_list:
        days = day.string
        day_result.append(days)
    return day_result


all_day = []
all_num = []

for page in range(1, 6):
    pg_url = '{url}&page={page}'.format(url=url, page=page)
    res = req.urlopen(pg_url)
    soup = BeautifulSoup(res, "html.parser")
    all_day.extend(get_day())
    all_num.extend(get_num())



print(all_day, all_num)
