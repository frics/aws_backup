import requests
from bs4 import BeautifulSoup
#url 접속 요청 객체 생성
request = requests.get("http://openapi.foodsafetykorea.go.kr/api/31d9c343371a43e1911b/I2790/xml/1/5")

#open API 소스코드 추출
html = request.text

#html code를 python 객체로 변환
soup = BeautifulSoup(html, 'html.parser')

import pymysql

connect = pymysql.connect(host='recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com',
                          user='root', 
                          password='recipe123',
                          db ='test',
                          charset ='utf8')

#open API에서 DESC_KOR 요소 추출
#links = soup.select('DESC_KOR')
serial_num = soup.select('RCP_SEQ')
for link in serial_num:
    sql = "INSERT INTO food(name) VALUES(%d)"
    curs.execute(sql, link)
name = soup.select('RCP_NM')
method = soup.select('RCP_WAY2')
_type = soup.select('RCP_PAT2')
calorie = soup.select('INFO_ENG')
carbon = soup.select('INFO_CAR')
protein = soup.select('INFO_PRO')
fat = soup.select('INFO_FAT')
salt = soup.select('INFO_NA')
url_img = soup.select('ATT_FILE_NO_MK')
ingredient = soup.select('RCP_PARTS_DTLS')
seq1 = soup.select('MANUAL01')
seq2 = soup.select('MANUAL02')
seq3 = soup.select('MANUAL03')
seq4 = soup.select('MANUAL04')
seq5 = soup.select('MANUAL05')
seq6 = soup.select('MANUAL06')
seq7 = soup.select('MANUAL07')
seq8 = soup.select('MANUAL08')
seq9 = soup.select('MANUAL09')
seq10 = soup.select('MANUAL10')
seq11 = soup.select('MANUAL11')
seq12 = soup.select('MANUAL12')
seq13 = soup.select('MANUAL13')
seq14 = soup.select('MANUAL14')
seq15 = soup.select('MANUAL15')
seq16 = soup.select('MANUAL16')
seq17 = soup.select('MANUAL17')
seq18 = soup.select('MANUAL18')
seq19 = soup.select('MANUAL19')
seq20 = soup.select('MANUAL20')
seq1_img = soup.select('MANUALIMG01')
seq2_img = soup.select('MANUALIMG02')
seq3_img = soup.select('MANUALIMG03')
seq4_img = soup.select('MANUALIMG04')
seq5_img = soup.select('MANUALIMG05')
seq6_img = soup.select('MANUALIMG06')
seq7_img = soup.select('MANUALIMG07')
seq8_img = soup.select('MANUALIMG08')
seq9_img = soup.select('MANUALIMG09')
seq10_img = soup.select('MANUALIMG10')
seq11_img = soup.select('MANUALIMG11')
seq12_img = soup.select('MANUALIMG12')
seq13_img = soup.select('MANUALIMG13')
seq14_img = soup.select('MANUALIMG14')
seq15_img = soup.select('MANUALIMG15')
seq16_img = soup.select('MANUALIMG16')
seq17_img = soup.select('MANUALIMG17')
seq18_img = soup.select('MANUALIMG18')
seq19_img = soup.select('MANUALIMG19')
seq20_img = soup.select('MANUALIMG20')

#for link in links:
#    print(link.text)
    


curs = connect.cursor(pymysql.cursors.DictCursor)



connect.commit()
connect.close()