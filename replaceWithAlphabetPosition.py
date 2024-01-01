def alphabet_position(text):
    textList = []
    numberList = []
    alphabetList = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    finalString = ""
    for letter in text:
        if letter.isalpha() == True:
            textList.append(letter.lower())
    for letter in textList:
        numberList.append(str(alphabetList.index(letter)+1))
    finalString = " ".join(numberList)
    return finalString