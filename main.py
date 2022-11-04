from LINE import LINE
           

txt = "data/line_utf-8.txt"
# data = np.loadtxt(txt, encoding="utf-8",dtype="str" ,delimiter='\n')
datapath = "cleanData.npy"

LineData = LINE(datapath)


    

countDict = LineData.wordCount()
countDict_meishi = LineData.wordSelect("名詞")
sorted_dict = sorted(countDict_meishi.items(), key = lambda item: item[1])
