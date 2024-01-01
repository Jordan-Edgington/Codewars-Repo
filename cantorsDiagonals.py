def cantor(nested_list):
    newList = []
    currentIndex = 0
    for list in nested_list:
        if list[currentIndex] == 1:
            newList.append(0)
        else:
            newList.append(1)
        currentIndex+=1
    return newList