import requests
import bs4
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def crawling(start_num: int, bundle_num=100) -> list:
    batch_data = []
    for division_number in range(start_num, start_num + bundle_num):
        print(".", sep="")
        url = f"https://www.pa.go.kr/research/contents/speech/index.jsp?spMode=view&catid=c_pa02062&artid={division_number}"
        try:
            # print(url)
            response = requests.get(url, verify=False)
            html = response.text
            soup = bs4.BeautifulSoup(html, "html.parser")

            table = soup.find("tbody")
            tr = table.find_all("tr")
            tds = tr[1].find_all('td')

            title = soup.select("td.subject")[0].text
            speech_text = soup.select("td.content")[0].text

            table = soup.find("tbody")
            tr = table.find_all("tr")

            date = tds[0].text
            president = tds[1].text
            location = tds[2].text
            kind = tr[2].find_all('td')[0].text

            batch_data.append((division_number, president, title, date, location, kind, speech_text))
        except Exception as e:
            president = e.__class__.__name__
            title = e.__str__()
            date = '-'
            location = '-'
            kind = '-'
            speech_text = url

            batch_data.append((division_number, president, title, date, location, kind, speech_text))
    return batch_data


def save_parquet(data: list, start_num: int) -> str:
    to_parquet_df = pd.DataFrame(data,
                                 columns=['division_number', 'president', 'title', 'date', 'location', 'kind', 'speech_text'])
    parquet_file_name = f"parquet/crawling_president_speeches_{start_num}.parquet"
    to_parquet_df.to_parquet(parquet_file_name)
    return parquet_file_name

start_num = 1400001
start_num = start_num + 400

for i in range(start_num, 1401692, 100):
    print(f"crawling:{i}".center(50, ">"))
    data = crawling(i)
    print(f"crawling:{i}".center(50, "<"))
    parquet_file_name = save_parquet(data, i)
    print(parquet_file_name.center(50, "<"))

