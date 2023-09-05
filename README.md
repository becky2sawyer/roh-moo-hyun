# roh-moo-hyun
- 노무현 대통령의 연설문을 제공합니다.
- South Korean former president Roh Moo-hyun, a politician who dedicated his life to democracy and human rights. I pay my respects to Roh Moo-hyun

![roh](https://img.seoul.co.kr//img/upload/2016/05/23/SSI_20160523162354.jpg)

### USE
```bash
$ python -V
Python 3.11.0

$ pip install roh-moo-hyun

$ $ rmh-search -h
usage: rmh-search [-h] [-t | -s] keyword

positional arguments:
  keyword       Search word

options:
  -h, --help    show this help message and exit
  -t, --title   Search speech title like
  -s, --speech  Search speech title speech

$ rmh-search -s "임시정부"
('2003-03-01', '제84주년 3·1절 기념사')
('2003-04-13', '대한민국 임시정부 수립 84주년 기념식 연설')
('2003-07-10', '[중국 국빈방문]한·중 경제인(상하이) 초청 오찬연설')
('2004-06-06', '제49회 현충일 추념사 ')
('2004-09-15', '대한민국 임시정부 기념사업회 창립총회 축하 메시지')
('2005-03-01', '제86주년 3·1절 기념사 ')
('2006-03-01', '제87주년 3·1절 기념사')
('2006-04-13', '대한민국 임시정부 수립 87주년 기념 메시지 ')
('2006-06-23', '대한민국 임시정부 기념관 건립 추진위원회 발족식 축하 전문 ')
('2006-10-13', '[중국방문]주중 대사관 신청사개관식 축사 ')
```
### Data
```bash
cat president_archive_ministry_of_public_safety_president_speech_record_speech_20220817.csv | cut -d',' -f2 | uniq
대통령
이승만
윤보선
박정희
최규하
전두환
전두환
노태우
김영삼
김대중
노무현
이명박
박근혜
```

## Ref
- [대통령기록관_행정안전부 대통령기록관_대통령연설기록 연설문](https://www.data.go.kr/data/15084167/fileData.do#tab-layer-openapi)
- https://stackoverflow.com/questions/45470964/python-extracting-text-from-webpage-pdf
- https://pypdf.readthedocs.io/en/latest/user/extract-text.html
- https://setuptools.pypa.io/en/latest/userguide/datafiles.html

## Development environment setting
```bash
$ pdm add requests
$ pdm add -dG test pytest pytest-cov
```

```bash
$ docker build -t president_speech:0.2.0 .
$ docker run -d --name roh-moo-hyun020 -v "$PWD":/usr/src/app president_speech:0.2.0
```
