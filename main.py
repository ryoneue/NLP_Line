from LINE import LINE
           

txt = "data/line_utf-8.txt"
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
datapath = "cleanData.npy"

debug = True
LineData = LINE(datapath,debug=debug)


    

countDict = LineData.wordCount()
countDict_meishi = LineData.wordSelect("名詞")
sorted_dict = sorted(countDict_meishi.items(), key = lambda item: item[1]["num"])
print("Complete Data prosesing.")