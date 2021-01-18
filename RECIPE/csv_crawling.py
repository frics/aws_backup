import requests
from bs4 import BeautifulSoup
import pandas as pd

start_index = 1
end_index = 600
tag = []
for i in range(2):

    print('——————INDEX %3d TO %d———————' % (start_index, end_index))
    print("————————PROCESSING————————")
    url = "http://openapi.foodsafetykorea.go.kr/api/31d9c343371a43e1911b/COOKRCP01/xml/" + str(start_index) + "/" + str(
    end_index)


    # url 접속 요청 객체 생성
    request = requests.get(url)

    # open API 소스코드 추출
    html = request.text

    # html code를 python 객체로 변환
    soup = BeautifulSoup(html, 'html.parser')

    # open API에서 요소 추출
    # ex) links = soup.select('DESC_KOR')
   
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
    
    '''
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


    data = [serial_num, name, method, _type, calorie, carbon, protein, fat, salt, url_img, ingredient, seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, seq9, seq10, seq11, seq12, seq13, seq14, seq15, seq16, seq17, seq18, seq19, seq20, seq1_img, seq2_img, seq3_img, seq4_img, seq5_img, seq6_img, seq7_img, seq8_img, seq9_img, seq10_img, seq11_img, seq12_img, seq13_img, seq14_img, seq15_img, seq16_img, seq17_img, seq18_img, seq19_img, seq20_img]
    '''
    data = [serial_num, name, method, _type, calorie, carbon, protein, fat, salt, url_img, ingredient]
    
    
    for i in range(11):
        for j in range(600):
            if not data[i][j].text:
                print("******"+str(j+start_index))
                print(data[i][j])
                data[i][j] = ""
            else:
                data[i][j] = data[i][j].text
                
    output = pd.DataFrame(data)
    name = "result_"+str(end_index)+".csv"

    output.to_csv(name, index=False, encoding="utf-8-sig")
    start_index += 600
    end_index += 600


