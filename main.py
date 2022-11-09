from LINE import LINE
import pandas as pd
import numpy as np          

txt = "data/line_utf-8.txt"
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
datapath = "cleanData.npy"

debug = True
LineData = LINE(datapath,debug=debug)


    

countDict = LineData.wordCount()
countDict_meishi = LineData.wordSelect("名詞")
Count4xlsx = LineData.Count(countDict_meishi)

pd.DataFrame(Count4xlsx).to_csv("test.csv")
sorted_dict = sorted(countDict_meishi.items(), key = lambda item: item[1]["num"])

print("Complete Data prosesing.")