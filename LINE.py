from encodings.utf_8 import encode
import numpy as np
import pandas as pd
import glob
import copy
import MeCab
import unidic
import tqdm
import os
import re
import datetime
tagger = MeCab.Tagger()
class LINE:

    def __init__(self, DataPath, debug=False):
        self.cleanData=[]
        # self.parse = {}
        self.datapath = DataPath
        self.debug = debug
        self.loadData()
        
        # self.mecab = MeCab.Tagger()
        # self.countDict = 

    def loadData(self):
        txt = "data/line_utf-8.txt"
        if not os.path.exists(txt): txt = "data/sample.txt"
        
        if not os.path.exists(self.datapath) or self.debug:
            with open(txt,encoding=("utf-8")) as f:
                datalist = f.readlines()
                
            # cleanData = []
            for num, line in tqdm.tqdm(enumerate(datalist), total=len(datalist)):
                line = self.cleanLine(line)

            #    print(line)
                parse = self.parseLine(line, num)
                self.cleanData.append(parse)
            np.save("cleanData.npy", self.cleanData)
                
        else:
            self.cleanData = np.load(self.datapath, allow_pickle=True)        

    def cleanLine(self, line):
        tmp = copy.copy(line)
        if "☎" in tmp:
            tmp = "[通話]"

        tmp = tmp.replace("\n", "")
        return tmp
    
    def parseLine(self, line, num):
        parse = {}
        parse["num"] = num
        
        tags = re.findall('\[.{1,5}\]', line)
        parse["tag"] = tags
        
        for tag in tags:
    #        print(line, tag, tags)
            line = line.replace(tag, " replace")
    #        print(line)
        # if "保存日時:" in line:
            # date = datalist[1].split("保存日時")[-1][1:-1]
            # date_f = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M')
            # self.parse["date"] = date_f
    
        # if "[LINE]" in line:
        #     print("LINE")
            
            
        if  len(line.split("\t")) == 3:        
            time, name, sentence = line.split("\t")
            parse["time"] = time
            parse["name"] = name
            parse["sentence"] = sentence[1:] # 文面の先頭のダブルクオーテーションを削除
            
            parse["Msentence"] = tagger.parse(sentence)
            
        return parse
    
    def wordCount(self):
        countDict = {}
        for parse in self.cleanData:
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

    
        
    def wordSelect(self, morp):
        countDict = {}
        for cdata in self.cleanData:
            if "Msentence" in cdata.keys():
                Msentence = cdata["Msentence"]
                sentence = cdata["sentence"]

                
    #            print(Msentence)
    #            tags = re.finditer('\[.*\]', Msentence)
    #            for tag in tags:
    #                Msentence.replace(tag, " ")
                    
                name = cdata["name"]
                Wakati = Msentence.split("\n")
                for wakati in Wakati:
    #                print(wakati)
    #                if re.search('\[.*\]', wakati):
    #                    print(wakati)
    #                    continue
                        
                    if wakati == "EOS":
                        break                
                    word = wakati.split("\t")[0]
                    morp_info = wakati.split("\t")[1]
                    word_class = morp_info.split(",")[0]

                    if word_class == morp:
                        if word in countDict.keys() :
                            countDict[word]["num"] += 1
                            countDict[word]["morp"].append(morp_info)
                            countDict[word]["name"].append(name)
                        else:                    
                            data_info = {"morp": [], "name": [], "num":1}
                            countDict[word] = data_info
                            countDict[word]["morp"].append(morp_info)
                            countDict[word]["name"].append(name)
        return countDict

    def Select(self, morp, user=False):
        countDict = {}
        for cdata in self.cleanData:
            if "Msentence" in cdata.keys():
                Msentence = cdata["Msentence"]
                sentence = cdata["sentence"]

                
    #            print(Msentence)
    #            tags = re.finditer('\[.*\]', Msentence)
    #            for tag in tags:
    #                Msentence.replace(tag, " ")
                    
                
                Wakati = Msentence.split("\n")
                for wakati in Wakati:
    #                print(wakati)
    #                if re.search('\[.*\]', wakati):
    #                    print(wakati)
    #                    continue
                        
                    if wakati == "EOS":
                        break                
                    word = wakati.split("\t")[0]
                    morp_info = wakati.split("\t")[1]
                    word_class = morp_info.split(",")[0]
                    

                    if word_class == morp:
                        if word in countDict.keys() :
                            countDict[word]["num"] += 1
                            countDict[word]["morp"].append(morp_info)
                        else:                    
                            data_info = {"morp": [], "num":1}
                            countDict[word] = data_info
                            countDict[word]["morp"].append(morp_info)
        return countDict

    def count4dic(self, info, key, users=False):
        info_in = info[key]
        info_out = {}
        if key == "name":
            for user in users:
                info_out[user] = 0

        for n in np.unique(info_in):

            #names[n] = 0
            count = info_in.count(n)
            info_out[n] = count
        return info_out

    def Count(self, countDict):
        out_dic = {}
        users = np.unique([i[1]["name"][0] for i in countDict.items()])[1:]
        for word,info in countDict.items():
            morp = info["morp"]
            name = info["name"]
            
            # names = np.unique(name)
            # for i,n in enumerate(names):
            #     #names[n] = 0
            #     count_name = name.count(n)
            #     names[n] = count_name
            if word == "こんばんは":
                a = 1

            names = self.count4dic(info, "name", users=users)
            morps = self.count4dic(info, "morp")
            # merge = names | morps
            merge = names
            out_dic[word] = pd.Series(merge)
        return out_dic  

            
                