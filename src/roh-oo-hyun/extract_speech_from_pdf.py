import pandas as pd
import sqlite3
from pypdf import PdfReader
import requests
import io


def insert_db(batch_data: list):
    # 리스트에 저장된 데이터를 한번에 데이터베이스에 저장
    connection = sqlite3.connect("president_speeches.db")
    cursor = connection.cursor()
    # 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS president_speeches (
    division_number INT,
    president       TEXT,
    title           TEXT,
    date            TEXT,
    pdf_url         TEXT,
    location        TEXT,
    speech_text     TEXT);
    """)
    connection.commit()

    cursor.executemany("""INSERT INTO president_speeches (
    division_number, 
    president, 
    title, 
    date, 
    pdf_url, 
    location, 
    speech_text) VALUES (?, ?, ?, ?, ?, ?, ?);""", batch_data)
    connection.commit()
    # 데이터베이스 연결 종료
    connection.close()


def save_parquet(batch_data: list, idx: int):
    """batch_data 를 DataFrame 으로 변환 및 저장"""
    to_parquet_df = pd.DataFrame(batch_data,
                                 columns=['division_number', 'president', 'title', 'date', 'pdf_url', 'location',
                                          'speech_text'])
    parquet_file_name = f"president_speeches_batch_data_{int(idx/1000)}.parquet"
    to_parquet_df.to_parquet(parquet_file_name)
    print(f"save parquet:{parquet_file_name}")


# csv 파일 열기
df = pd.read_csv("note/president_archive_ministry_of_public_safety_president_speech_record_speech_20220817.csv")

# DataFrame의 행(연설문)을 순회하며 데이터베이스에 저장할 데이터를 리스트에 저장
batch_data = []
for idx, row in df.iterrows():

    # 구분번호, 대통령, 글제목, 연설일자, 원문보기, 연설장소 를 변수에 저장
    division_number = row['구분번호']
    president = row['대통령']
    title = row['글제목']
    date = row['연설일자']
    pdf_url = row['원문보기']
    location = row['연설장소']
    
    r = requests.get(pdf_url)
    f = io.BytesIO(r.content)

    try:
        reader = PdfReader(f)
        page = reader.pages[0]
        # 연설원문을 변수에 저장
        speech_text = page.extract_text().replace("\n", "")
    except:
        speech_text = "ERR"

    # 데이터베이스에 저장할 데이터를 리스트에 저장
    batch_data.append((division_number, president, title, date, pdf_url, location, speech_text))

    print(idx)
    if idx != 0:
        if idx % 1000 == 0:
            save_parquet(batch_data, idx)
            insert_db(batch_data)
            print(f"insert db:{idx}")
            batch_data = []
