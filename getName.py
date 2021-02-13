filepath = 'dwscripts.txt';
filewrite = './keywords.txt';
words = [];
with open(filepath) as myfile:
   line = myfile.read()
   strings = line.split(":")[:-1];

   for string in strings:
        try:
            words.append(string.split()[-1]);
        except:
            print(string);
wordlist = str(list(set(words)));
print(wordlist)


f = open(filewrite, 'w');
f.write(wordlist);
f.close();