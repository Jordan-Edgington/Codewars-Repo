def find_outlier(integers):
    oddCount = 0
    for item in integers:
        if item%2 == 0:
            pass
        else:
            oddCount+=1
    if oddCount != 1:
        for item in integers:
            if item%2==0:
                return item
    else:
        for item in integers:
            if item%2!=0:
                return item