def solution(s):
    letterList = []
    answerList = []
    for letter in s:
        letterList.append(letter)
    while len(letterList) > 0:
        x = "".join(letterList[0:2])
        if len(x) == 2:
            answerList.append(x)
        else:
            letterList.append("_")
            x = "".join(letterList[0:2])
            answerList.append(x)
        if len(letterList) >=2:
            letterList.remove(letterList[0])
            letterList.remove(letterList[0])
        else:
            pass
    return answerList