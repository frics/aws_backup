import requests
from bs4 import BeautifulSoup
import pymysql



#mysql db 연결
connect = pymysql.connect(host='recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com',
                          user='root', 
                          password='recipe123',
                          db ='RECIPE',
                          charset ='utf8')
curs = connect.cursor(pymysql.cursors.DictCursor)
start_index = 1
end_index = 100



print("----식품안전나라 조리식품의 레시피 DB 연동----")
print("-----------------PROCESS START----------------", end='\n\n')

for i in range(12):
    
    print('------------INDEX %3d TO %d--------------'%(start_index, end_index))
    print("-----------------PROCESSING-----------------")
    url = "http://openapi.foodsafetykorea.go.kr/api/31d9c343371a43e1911b/COOKRCP01/xml/"+str(start_index)+ "/" + str(end_index)
    #url 접속 요청 객체 생성
    request = requests.get(url)

    #open API 소스코드 추출
    html = request.text

    #html code를 python 객체로 변환
    soup = BeautifulSoup(html, 'html.parser')



    #open API에서 요소 추출
    #ex) links = soup.select('DESC_KOR')
    serial_num = soup.select('RCP_SEQ')
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
    seq1_img = soup.select('MANUAL_IMG01')
    seq2_img = soup.select('MANUAL_IMG02')
    seq3_img = soup.select('MANUAL_IMG03')
    seq4_img = soup.select('MANUAL_IMG04')
    seq5_img = soup.select('MANUAL_IMG05')
    seq6_img = soup.select('MANUAL_IMG06')
    seq7_img = soup.select('MANUAL_IMG07')
    seq8_img = soup.select('MANUAL_IMG08')
    seq9_img = soup.select('MANUAL_IMG09')
    seq10_img = soup.select('MANUAL_IMG10')
    seq11_img = soup.select('MANUAL_IMG11')
    seq12_img = soup.select('MANUAL_IMG12')
    seq13_img = soup.select('MANUAL_IMG13')
    seq14_img = soup.select('MANUAL_IMG14')
    seq15_img = soup.select('MANUAL_IMG15')
    seq16_img = soup.select('MANUAL_IMG16')
    seq17_img = soup.select('MANUAL_IMG17')
    seq18_img = soup.select('MANUAL_IMG18')
    seq19_img = soup.select('MANUAL_IMG19')
    seq20_img = soup.select('MANUAL_IMG20')


    data = []

    data = [serial_num, name, method, _type, calorie, carbon, protein, fat, salt, url_img, ingredient, seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, seq9, seq10, seq11, seq12, seq13, seq14, seq15, seq16, seq17, seq18, seq19, seq20, seq1_img, seq2_img, seq3_img, seq4_img, seq5_img, seq6_img, seq7_img, seq8_img, seq9_img, seq10_img, seq11_img, seq12_img, seq13_img, seq14_img, seq15_img, seq16_img, seq17_img, seq18_img, seq19_img, seq20_img]

    #html태크 형식을 text형식으로 변환하여 저장
    for i in range(51):
        for j in range(100):
            if not data[i][j].text: 
                
                data[i][j] = ""
            else:
                data[i][j] = data[i][j].text



    for i in range(100): 
        #mysql 명령어, 각 필드의 데이터형과 필드 이름 매칭
        sql = "INSERT INTO recipes(serial_num, name, method, type, calorie, carbonhydrate, protein, fat, salt, url_img, ingredient, seq_1, seq_2, seq_3, seq_4, seq_5, seq_6, seq_7, seq_8, seq_9, seq_10, seq_11, seq_12, seq_13, seq_14, seq_15, seq_16, seq_17, seq_18, seq_19, seq_20, seq_1_img, seq_2_img, seq_3_img, seq_4_img, seq_5_img, seq_6_img, seq_7_img, seq_8_img, seq_9_img, seq_10_img, seq_11_img, seq_12_img, seq_13_img, seq_14_img, seq_15_img, seq_16_img, seq_17_img, seq_18_img, seq_19_img, seq_20_img) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        curs.execute(sql, (data[0][i], data[1][i], data[2][i], data[3][i], data[4][i], data[5][i], data[6][i], data[7][i], data[8][i], data[9][i], data[10][i], data[11][i], data[12][i], data[13][i], data[14][i], data[15][i], data[16][i], data[17][i], data[18][i], data[19][i], data[20][i], data[21][i], data[22][i], data[23][i], data[24][i], data[25][i], data[26][i], data[27][i], data[28][i], data[29][i], data[30][i], data[31][i], data[32][i], data[33][i], data[34][i], data[35][i], data[36][i], data[37][i], data[38][i], data[39][i], data[40][i], data[41][i], data[42][i], data[43][i], data[44][i], data[45][i], data[46][i], data[47][i], data[48][i], data[49][i], data[50][i]))
        connect.commit()
    print("------------------PROCESS END-----------------")
    print('------------INDEX %3d TO %d--------------'%(start_index, end_index), end = '\n\n')
    start_index+=100
    end_index+=100
print("-----------------DB 연동 완료-----------------")
connect.close()

