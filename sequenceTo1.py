def seq_to_one(n):
    sequenceList = []
    if n < 1:
        for number in range(n,2):
            sequenceList.append(number)
    elif n > 1:
        for number in range(1,n + 1):
            sequenceList.append(number)
        sequenceList = sequenceList[::-1]
    else:
        return [1]
    return sequenceList