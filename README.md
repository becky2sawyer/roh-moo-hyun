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

### Missing value
| division\_number | president | title | date | pdf\_url | location | speech\_text |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1309360 | 노무현 | 제주국제컨벤션센터 개관식 축하 메시지 | 2003-03-22 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264265700042657014624.PDF | 국내 | ERR |
| 1309364 | 노무현 | 제1회 동북아경제포럼 축하 메시지 | 2003-04-08 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264266100042661014628.PDF | 국내 | ERR |
| 1309370 | 노무현 | 부활절 축하 메시지 | 2003-04-20 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264266700042667014634.PDF | 국내 | ERR |
| 1309393 | 노무현 | 2003 서울국제도서전 축하 메시지 | 2003-06-04 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264269000042690014657.PDF | 국내 | ERR |
| 1309660 | 노무현 | 희망 2005 이웃사랑캠페인 메시지 | 2004-12-04 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264295700042957014924.PDF | 국내 | ERR |
| 1309659 | 노무현 | 숭산 큰스님 조의 메시지  | 2004-12-04 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264295600042956014923.PDF | 국내 | ERR |
| 1309675 | 노무현 | 서부 사하라 의료지원단 장병에게 보내는 격려 서신  | 2005-02-09 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264297200042972014939.PDF | 국내 | ERR |
| 1309673 | 노무현 | 자이툰부대 장병에게 보내는 격려 서신  | 2005-02-09 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264297000042970014937.PDF | 국내 | ERR |
| 1309696 | 노무현 | 이데일리 창간 5주년 축하 메시지  | 2005-03-27 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264299300042993014960.PDF | 국내 | ERR |
| 1309726 | 노무현 | 불기2549년 부처님 오신 날 봉축 메시지 | 2005-05-15 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264302300043023014990.PDF | 국내 | ERR |
| 1309745 | 노무현 | 충청투데이 창간 15주년 축하 메시지  | 2005-06-10 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264304200043042015009.PDF | 국제 | ERR |
| 1309761 | 노무현 | 2006 서울 세계도서관정보대회 초청 메시지  | 2005-08-14 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264305800043058015025.PDF | 국내 | ERR |
| 1309775 | 노무현 | \[코스타리카 국빈방문\]한·SICA 정상회의 개회식 연설 | 2005-09-12 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264307200043072015039.PDF | 국내 | ERR |
| 1309787 | 노무현 | 2005 동아시아 경제포럼 축하 전문 | 2005-10-05 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264308400043084015051.PDF | 국내 | ERR |
| 1309812 | 노무현 | 2005 바르게 살기 운동 전국대회 축하 메시지 | 2005-11-16 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264310900043109015076.PDF | 국내 | ERR |
| 1309810 | 노무현 | 톨레도 페루 대통령을 위한 오찬사 | 2005-11-16 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264310700043107015074.PDF | 국내 | ERR |
| 1309821 | 노무현 | 지상파 DMB 공동 개국 축하 메시지  | 2005-12-01 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264311800043118015085.PDF | 국내 | ERR |
| 1309826 | 노무현 | 김대중 전 대통령 노벨 평화상 수상 5주년 축하 메시지  | 2005-12-08 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264312300043123015090.PDF | 국내 | ERR |
| 1309898 | 노무현 | 한국고용정보원 개원식 축하 메시지 | 2006-06-21 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264319500043195015162.PDF | 국내 | ERR |
| 1309904 | 노무현 | 민선 제4기 지방자치단체장 취임 축하 메시지 | 2006-07-01 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264320100043201015168.PDF | 국내 | ERR |
| 1309907 | 노무현 | 제5회 재외동포교육 국제학술대회 축하 메시지  | 2006-07-26 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264320400043204015171.PDF | 국내 | ERR |
| 1309908 | 노무현 | 제67차 국제 와이즈멘 세계대회 축하 메시지  | 2006-08-03 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264320500043205015172.PDF | 국내 | ERR |
| 1309923 | 노무현 | \[핀란드 국빈방문\]헬싱키 시 주최 오찬 답사 | 2006-09-08 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264322000043220015187.PDF | 국내 | ERR |
| 1309960 | 노무현 | 제4회 자율관리어업 전국대회 축하 메시지 | 2006-11-22 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264325700043257015224.PDF | 국내 | ERR |
| 1309961 | 노무현 | 라스무슨 덴마크 총리내외를 위한 오찬사  | 2006-11-23 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264325800043258015225.PDF | 국내 | ERR |
| 1309974 | 노무현 | 유센코 우크라이나 대통령내외를 위한 만찬사  | 2006-12-18 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264327100043271015238.PDF | 국내 | ERR |
| 1310062 | 노무현 | 아프가니스탄 피랍 사태와 관련하여 드리는 말씀 | 2007-07-21 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264335900043359015326.PDF | 국내 | ERR |
| 1310089 | 노무현 | 전북대학교 개교 60주년 축하 메시지 | 2007-10-12 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264338600043386015353.PDF | 국내 | ERR |
| 1310123 | 노무현 | 2007 신기술 실용화 촉진대회 축하 메시지 | 2007-12-13 | http://dams.pa.go.kr:8888/dams/DOCUMENT/2009/11/26/DOC/SRC/0104200911264342000043420015387.PDF | 국내 | ERR |

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
$ docker build -t roh_moo_hyun:0.2.0 .
$ docker run -d --name roh-moo-hyun020 -v "$PWD":/usr/src/app roh_moo_hyun:0.2.0
```
