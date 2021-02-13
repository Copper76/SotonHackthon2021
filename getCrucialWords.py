from collections import Counter

with open('dwscripts.txt') as fin:
    counter = Counter(fin.read().strip().split())

f = open("crucialcrucialwords.txt","w")
f.write(str(counter.most_common()))
f.close()
