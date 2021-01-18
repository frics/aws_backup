import csv
import pymysql

conn = pymysql.connect(host='localhost',
                       user='admin',passwd='recipe123',db='RECIPE_DB',charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
conn.commit()

f = open('cate_tag_icnum.csv','r',encoding='UTF8')
csvReader = csv.reader(f)

for row in csvReader:
    cate = (row[0])
    tag = (row[1])
    tagNumber = (row[2])

    print (cate + " " + tag + " " + tagNumber)
    query = 'INSERT INTO numbering VALUES(%s,%s,%s)'
    curs.execute(query,(cate,tag,tagNumber))

conn.commit()

f.close()
conn.close()