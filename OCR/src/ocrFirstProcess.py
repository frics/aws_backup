# -*- coding: utf-8 -*-
from PIL import Image
from pytesseract import *
import configparser
import sys
import os
import csv
import re
import json
import pandas as pd


# field name to convert json
fields = ["ingredient", "price"]

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')


def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'):
    img = Image.open(fullPath)
    txtName = os.path.join(outTxtPath, fileName.split('.')[0])

    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_space=1')

    strToTxt(txtName, outText)

    isNumber(outTxtPath, fileName)


def strToTxt(txtName, outText):
    with open(txtName + '.txt', 'w', encoding='utf-8') as f:
        f.write(outText)


def isNumber(outTxtPath, fileName):
    txtName = os.path.join(outTxtPath, fileName.split('.')[0])
    if os.path.getsize(txtName + '.txt') != 0:
        with open(txtName + '.txt', 'r', encoding='utf-8') as textFile:
            textLines = textFile.readlines()
            list = []
            for line in textLines:
                if (line != '\n'):
                    p = re.compile('^[0-9]+\n?')
                    if (p.search(line) == None):
                        print(line)
                        list.append(line)

        with open(txtName + '.txt', 'w', encoding='utf-8') as writeFile:
            writeFile.writelines(list)






if __name__ == "__main__":
    outTxtPath = "../resource/OcrTxtPath"
    fullName = "../resource/SaveImgPath/result.jpg"
    
    ocrToStr(fullName, outTxtPath, "pic.jpg", 'kor')

