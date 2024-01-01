def find_short(s):
    wordList = s.split()
    lenList = []
    finalList = []
    for word in wordList:
        lenList.append(len(word))
    lenList.sort()
    smallLen = lenList[0]
    return smallLen