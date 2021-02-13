filepath = 'dwscripts.txt'
filewrite = './keywords.txt'
keywords = []
with open(filepath) as myfile:
    lines = myfile.readlines()
    for line in lines:
        words = line.split()
        if words:
            if words[0][-1] == ":":
                keywords.append(line.split()[0][:-1])
    keywords = list(set(keywords))

f = open(filewrite, 'w')
for keyword in keywords:
    f.write(keyword+"\n")
f.close()
