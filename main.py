from encodings.utf_8 import encode
import numpy as np
import pandas as pd
import glob
import copy

def cleanLine(line):
    tmp = copy.copy(line)
    tmp = tmp.replace("\n", "")
    return tmp

def parseLine(line, num):
    parse = {}
    parse["num"] = num
    if "保存日時:" in line:
        date = datalist[1].split("保存日時")[-1][1:-1]
        date_f = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M')
        parse["date"] = date_f

    elif "[LINE]" in line:
        print("LINE")
        
    elif  len(line.split("\t")) == 3:        
        time, name, sentence = line.split("\t")
        parse["time"] = time
        parse["name"] = name
        parse["sentence"] = sentence
        
    return parse

txt = "data/line_utf-8.txt"
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
with open(txt,encoding=("utf-8")) as f:
    datalist = f.readlines()
    
cleanData = []
for num, line in enumerate(datalist):
    line = cleanLine(line)
#    print(line)
    parse = parseLine(line, num)
    cleanData.append(parse)