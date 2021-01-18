import pymysql
import json

conn = pymysql.connect(host='localhost',
                       user='admin',passwd='recipe123',db='RECIPE_DB',charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
conn.commit()

jsonPath = "../OCR/resource/jsonPath/jsonResult.json"


with open(jsonPath,"r",encoding='utf8') as jsonFile:
    jsonData = json.load(jsonFile)
    length = len(jsonData)

    for i in range(0,length):
        index = "classification" + str(i)
        name = jsonData[index]['name']
        query = "SELECT * FROM tag WHERE name=%s"
        curs.execute(query,(name))
        result = curs.fetchone()
        #print(result['cate'])
        if(result == None):
            cate = jsonData[index]['cate']
            tag = jsonData[index]['tag']
            name = jsonData[index]['name']
            query = "SELECT * FROM tempTable WHERE name=%s"
            curs.execute(query,(name))
            result = curs.fetchall()
            print(result)

            if(len(result) == 0):
                insertQuery = "INSERT INTO tempTable (cate,tag,name,count) VALUES (%s,%s,%s,%s)"
                curs.execute(insertQuery,(cate,tag,name,1))
                conn.commit()
                result1 = curs.fetchone()
                #print(result1)
            else:
                selectQuery = "SELECT count from tempTable WHERE name=%s"
                curs.execute(selectQuery,(name))
                result2 = curs.fetchone()
                insertCount = result2['count'] + 1
                print(insertCount)
                if(insertCount >= 3):
                    insertQuery = "INSERT INTO tag (cate,tag,name) VALUES (%s,%s,%s)"
                    curs.execute(insertQuery,(cate,tag,name))
                    conn.commit()
                    deleteQuery = "DELETE FROM tempTable WHERE name=%s"
                    curs.execute(deleteQuery,(name))
                    conn.commit()
                else:
                    updateQuery = "UPDATE tempTable SET count=%s WHERE name=%s"
                    curs.execute(updateQuery,(insertCount,name))
                    conn.commit()

