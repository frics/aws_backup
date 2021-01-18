import json
import pymysql


txtPath = "../resource/OcrTxtPath/pic.txt"
txtList = []


with open(txtPath, 'r', encoding='utf8') as f:
    for line in f:
        line = line.replace("\n","")
        txtList.append(line)


conn = pymysql.connect(host='recipe-db.cshisawjylld.ap-northeast-2.rds.amazonaws.com',
                       user='root',passwd='recipe123',db='classification',charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
conn.commit()

dict1 = {}
dict2 = {}
def constructJson(result,name,index):
    sno = "classification" + str(index)
    if(result == None) :
        dict2['cate'] = "카테고리 없음"
        dict2['tag'] = "태그없음"
        dict2['name'] = name
        dict1[sno] = dict2
    else:
        dict1[sno] = result


for index in range (0,len(txtList)):
    query = 'SELECT * FROM cate_tag_name WHERE name=(%s)'
    curs.execute(query,(txtList[index]))
    result = curs.fetchone()
    print(result)
    constructJson(result,txtList[index],index)

outFileName = "../resource/jsonPath/jsonResult.json"
out_file = open(outFileName,"w",encoding='utf-8')
json.dump(dict1, out_file, ensure_ascii=False)
out_file.close()

