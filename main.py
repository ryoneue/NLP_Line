from LINE import LINE
import pandas as pd
import numpy as np       
import argparse   

parser = argparse.ArgumentParser(description='Parameter for NLP prossess.')
parser.add_argument('--model', default="nlp", type=str,
                    help='mecab or ginza')
parser.add_argument('--txt', default="data/sample.txt", type=str,
                    help='Input text path.')


args = parser.parse_args()
mode = args.model
txt = "data/line_utf-8.txt"
txt = args.txt

print("Prossesing file:" , txt)
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
datapath = "cleanData.npy"

debug = False
LineData = LINE(datapath,debug=debug, mode=mode)


    

# countDict = LineData.wordCount()
select = ["名詞", "URL"]
countDict_meishi = LineData.wordSelect(select,numLimit=5)
Count4xlsx = LineData.Count(countDict_meishi)

df_out = pd.DataFrame(Count4xlsx).T
df_out[df_out.keys()[:-1]].to_csv("test.csv") #keyにNanが混じるため暫定処置
df_out[df_out.keys()[:-1]].to_excel("test.xlsx") #keyにNanが混じるため暫定処置

sorted_dict = sorted(countDict_meishi.items(), key = lambda item: item[1]["num"])

print("Complete Data prosesing.")