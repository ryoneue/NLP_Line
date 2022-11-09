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

df_out = pd.DataFrame(Count4xlsx).T
df_out[df_out.keys()[:-1]].to_csv("test.csv") #keyにNanが混じるため暫定処置

sorted_dict = sorted(countDict_meishi.items(), key = lambda item: item[1]["num"])

print("Complete Data prosesing.")