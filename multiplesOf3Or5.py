def solution(number):
    answerList = []
    finalValue = 0
    if number <= 0:
        return 0

    for number in range(0,number):
        if number%3==0:
            if number not in answerList:
                answerList.append(number)
        elif number%5==0:
            if number not in answerList:
                answerList.append(number)
    for item in answerList:
        finalValue += item
    return finalValue