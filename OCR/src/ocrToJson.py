# -*- coding: utf-8 -*-
from PIL import Image
from pytesseract import *
import configparser
import sys
import os
import json



#whitelist to distinguish item
item = ["품명","상품명","상품","item","ITEM","품"]

#whitelist to distinguish price
price = ["단가","가격","상품가","PRICE","price"]

#whitelist to distinguish end line
end = ["면세합","소","알인금액","과세금액"]

#whitelist to price separator
separator = [",","."," "]

#field name to convert json
fields = ["ingredient","price","amount"]

#set property file path
config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')

#convert image to string
def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'):

    img = Image.open(fullPath)
    txtName = os.path.join(outTxtPath,fileName.split('.')[0])

    outText = image_to_string(img,lang=lang,config='--psm 1 -c preserve_interword_spaces=1')

    strToTxt(txtName,outText) #convert string to text file

    #processData(outTxtPath,fileName) #process text file


def strToTxt(txtName,outText):
    with open(txtName + '.txt', 'w', encoding='utf-8') as f:
        f.write(outText)

def processData(outTxtPath,fileName):
    txtName = os.path.join(outTxtPath,fileName.split('.')[0])
    if os.path.getsize(txtName+'.txt') !=0:
        with open(txtName+'.txt', 'r', encoding='utf-8') as textFile:
            list = []
            for row in textFile:
                nextRow = row.split('\n')
                for word in nextRow:
                    if (word !=''):
                        saveWord = ' '.join(word.split())
                        list.append(saveWord+'\n')

        with open(txtName + '.txt', 'w', encoding='utf-8') as writeFile:
            writeFile.writelines(list)

    ingredientsToTxt(list,outTxtPath) #extract ingredients and price

    txtToJson(outTxtPath) #convert to Json file


def ingredientsToTxt(list,outTxtPath):
    txtName = os.path.join(outTxtPath,"result")

    with open(txtName + '.txt', 'w', encoding='utf-8') as writeFile:
        length = len(list)
        for i in range(0, length):
            if list[i - 1].split(' ')[0] in item:
                if list[i - 1].split(' ')[1] in price:
                    startIdx = i

        for j in range(startIdx, length):
            newPrice = convertPrice(list[j].split(' ')[1]) #remove '.' and ',' in price string
            writeFile.write(list[j].split(' ')[0]+' '+newPrice+"\n")
            if list[j + 1].split(' ')[0] in end:
                break

def convertPrice(price):
    length = len(separator)
    for i in range(0,length):
        if separator[i] in price:
            price = price.replace(separator[i],"")
    return price


def txtToJson(outTxtPath):
    filename = os.path.join(outTxtPath,"result.txt")
    #resultant dictionary
    dict1 = {}

    with open(filename,"r",encoding='utf-8') as resultFile:
        l = 1  # count variable for employee id creation
        for line in resultFile:
            # reading line by line from the text file
            description = list(line.strip().split(None, 3))

            # for output see below
            #print(description)

            # for automatic creation of id for each refrigerator
            sno = 'refrigerator' + str(l)
            # loop variable
            i = 0
            # intermediate dictionary
            dict2 = {}
            while i < len(fields):
                # creating dictionary for each employee
                dict2[fields[i]] = description[i]
                i = i + 1

            # appending the record of each employee to
            # the main dictionary
            dict1[sno] = dict2
            l = l + 1
    # creating json file
    print("resultJson")

    outFileName = os.path.dirname(os.path.realpath(__file__)) + os.sep +'resultJson'  # OCR/reslutJson
    out_file = open(outFileName, "w", encoding='utf-8')
    json.dump(dict1, out_file, ensure_ascii=False, indent=3)
    out_file.close()



if __name__ == "__main__":
    print("------main------")
    outTxtPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.sep + 'resource' + os.sep + 'OcrTxtPath'
    print(outTxtPath)
    #outTxtPath = os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath']
    #outJsonPath = os.path.dirname(os.path.realpath(__file__)) + config['Path']['TxtJsonPath']

    
    fullName = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.sep + 'resource' + os.sep + 'OriImgPath' + os.sep + 'gs.jpg'
    ocrToStr(fullName,outTxtPath, 'test1.jpg', 'kor+eng')

