def longest_consec(strarr, k):
    joinedList = []
    joinedLenList = []
    currentindex = 0
    maxLen = 0
    if k <= 0 or len(strarr) <= 0 or k > len(strarr):
        return ""
    for string in strarr:
        currentstring = "".join(strarr[currentindex:currentindex+k])
        joinedList.append(currentstring)
        currentindex+=1
    for item in joinedList:
        joinedLenList.append(len(item))
    if len(joinedLenList) > 0:
        maxLen = max(joinedLenList)
    for item in joinedList:
        if maxLen == 0:
            return ""
        elif len(item) == maxLen:
            return item