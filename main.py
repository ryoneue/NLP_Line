from encodings.utf_8 import encode
import numpy as np
import pandas as pd
import glob
import copy
import MeCab
import unidic
import tqdm

def cleanLine(line):
    tmp = copy.copy(line)
    tmp = tmp.replace("\n", "")
    return tmp

def parseLine(line, num):
    parse = {}
    parse["num"] = num
    tagger = MeCab.Tagger()
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
        parse["Msentence"] = tagger.parse(sentence) 
        
    return parse

def wordCount(cleanData):
    countDict = {}
    for parse in cleanData:
        if "Msentence" in parse.keys():
            Msentence = parse["Msentence"]
            Wakati = Msentence.split("\n")
            for wakati in Wakati:
#                print(wakati)
                if wakati == "EOS":
                    break
                word = wakati.split("\t")[0]
                if word in countDict.keys():
                    countDict[word] += 1
                else:
                    countDict[word] = 1
    return countDict
    

txt = "data/line_utf-8.txt"
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
with open(txt,encoding=("utf-8")) as f:
    datalist = f.readlines()
    
cleanData = []
for num, line in tqdm.tqdm(enumerate(datalist), total=len(datalist)):
    line = cleanLine(line)
#    print(line)
    parse = parseLine(line, num)
    cleanData.append(parse)
countDict = wordCount(cleanData)
    
