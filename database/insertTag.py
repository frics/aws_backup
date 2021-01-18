import csv
import pymysql

conn = pymysql.connect(host='localhost',
                       user='admin',passwd='recipe123',db='RECIPE_DB',charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
conn.commit()
print ("connect")

f = open('cate_tag_name.csv','r',encoding='UTF8')
csvReader = csv.reader(f)

for row in csvReader:
    cate = (row[0])
    tag = (row[1])
    name = (row[2])

    print (cate + " " + tag + " " + name)
    query = 'INSERT INTO tag VALUES(%s,%s,%s)'
    curs.execute(query,(cate,tag,name))

conn.commit()

f.close()
conn.close()