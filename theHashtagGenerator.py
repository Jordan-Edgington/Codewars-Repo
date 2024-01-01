def generate_hashtag(s):
  finalResult = ""
  workingList = s.split()
  finalList = []
  workingList.insert(0,"#")
  for word in workingList:
    word = word.capitalize()
    finalList.append(word)
  finalResult = "".join(finalList)
  if len(finalResult)>140:
      return False
  elif len(s) == 0 or len(finalResult) == 0:
      return False
  else:
    return finalResult