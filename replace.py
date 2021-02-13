def calc_dist(string1, string2):
    val = 0
    if string1 == "":
        return len(string2)
    elif string2 == "":
        return len(string1)
    elif string1[0] == string2[0]:
        val += calc_dist(string1[1:], string2[1:])
    else:
        val = 1 + min([calc_dist(string1, string2[1:]),calc_dist(string1[1:], string2),calc_dist(string1[1:], string2[1:])])
    return val

def rep_words(inputString,keyword_list,threshold):
    final = ""
    words = inputString.split()
    keywords = keyword_list.split(",")
    for word in words:
        for keyword in keywords:
            if calc_dist(word,keyword) < threshold:
                final += " "+keyword
            else:
                final += " " + word
    return final
