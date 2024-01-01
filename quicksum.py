def quicksum(packet):
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetIndex = 0
    packetIndex = 0
    totalValue = 0
    currentIndex = 0
    for item in packet:
        if item.isupper() is True or item == " ":
            alphabetIndex = alphabet.index(item)
            packetIndex = packet.index(item,currentIndex)+1
            print("the alphabetIndex is "+str(alphabetIndex)+" and the packetIndex is "+str(packetIndex))
            totalValue += (alphabetIndex*packetIndex)
            print(totalValue)
        else:
            return 0
        currentIndex +=1
    return totalValue