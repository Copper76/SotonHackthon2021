import math


def calc_dist(string1, string2):
    val = 0
    if string1 == "":
        return len(string2)
    elif string2 == "":
        return len(string1)
    elif string1[0] == string2[0]:
        val += calc_dist(string1[1:], string2[1:])
    else:
        val = 1 + min(
            [calc_dist(string1, string2[1:]), calc_dist(string1[1:], string2), calc_dist(string1[1:], string2[1:])])
    return val


def calc_dist_bool(string1, string2, threshhold):
    if string1 == "":
        return len(string2) < threshold
    elif string2 == "":
        return len(string1) < threshold
    elif string1[0] == string2[0]:
        return calc_dist(string1[1:], string2[1:]) < threshold
    else:
        return 1 + min(
            [calc_dist(string1, string2[1:]), calc_dist(string1[1:], string2),
             calc_dist(string1[1:], string2[1:])]) < threshhold


def rep_words(inputString, keywords, threshold):
    final = ""
    words = inputString.split()
    for word in words:
        insert = word
        for keyword in keywords:
            if calc_dist(word.lower(), keyword.lower()) < threshold:
                insert = keyword
                break
        final += " " + insert
    return final


def rep_words_flex(inputString, keywords):
    final = ""
    words = inputString.split()
    for word in words:
        insert = word
        for keyword in keywords:
            threshold = math.floor(len(keyword) / 4)
            if calc_dist(word.lower(), keyword.lower()) < threshold:
                insert = keyword
                break
        final += " " + insert
    return final

with open("keywords.txt") as myfile:
    keywords = myfile.readlines()

print(rep_words_flex("Cyberman cybermain cybermonkey cybercat cyberdalek monkeydalek is Doctor wholiak", keywords))
