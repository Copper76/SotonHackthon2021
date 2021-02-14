from collections import Counter

punctuation = [",",".","!","?",";",":","[","]","(",")"]

with open('dwscripts.txt') as fin:
    
    x = fin.read().strip().lower()
    
    for p in punctuation:
        x = x.replace(p,"")
    
    counter = Counter(x.split())

f = open("crucialcrucialwords.txt","w")

crucialwords = []

for word, count in counter.most_common(1000):
    crucialwords.append(word + "")

f.write(str(crucialwords))
f.close()
