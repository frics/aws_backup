import requests
from bs4 import BeautifulSoup


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

 
    ingredient = soup.select('RCP_PARTS_DTLS')

    for item in ingredient:
        print()
        print(item.text)
        print()

    start_index+=100
    end_index+=100
print("-----------------DB 연동 완료-----------------")
connect.close()

