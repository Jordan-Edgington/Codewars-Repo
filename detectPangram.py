def is_pangram(s):
  letterList = []
  for letter in s:
      if letter.isalpha() and letter not in letterList:
          letterList.append(letter.lower())
  if len(letterList) == 26:
      return True
  return False
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))