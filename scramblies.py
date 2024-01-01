#see if str1 can be scrambled to make up str2
def scramble(str1,str2):
  str1Dic = {}
  
  for item in str1:
    if item in str1Dic:
      str1Dic[item] += 1
    else:
      str1Dic[item] = 1
  
  for item in str2:
    if item in str1Dic:
      str1Dic[item]-=1
    elif item not in str1Dic:
      return False

  for item in str1Dic:
    if str1Dic[item] < 0:
      return False
  
  return True