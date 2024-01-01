def add_binary(a,b):
  c = a+b
  n = 0
  nResult = 0
  twoNList = []
  binaryList = []
  finalString = ""
  #must now convert c to binary
  while nResult < c:
      nResult = 2**n
      n +=1
      twoNList.append(nResult)
      print("The current n value is ", n, ".")
  print(twoNList)
  for item in reversed(twoNList):
    if c - item >= 0:
      c = c - item
      binaryList.append("1")
    elif c - item < 0:
      binaryList.append("0")
  print(binaryList)
  while binaryList[0] == "0":
      binaryList.remove(binaryList[0])
  finalString = "".join(binaryList)
  return finalString