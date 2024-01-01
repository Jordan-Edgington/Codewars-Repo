def unique_in_order(sequence):
  newList = []
  currentIndex = 0
  for item in sequence:
    print(currentIndex)
    print(item)
    print("the item before this is", sequence[currentIndex-1])
    if sequence.index(item,currentIndex) == 0:
       newList.append(item)
    elif item == sequence[currentIndex-1]:
       pass
    else:
       newList.append(item)
    currentIndex += 1
  return newList