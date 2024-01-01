def spin_words(sentence):
  wordListReversed = []
  wordList = sentence.split()
  for item in wordList:
    if len(item) >= 5:
      wordListReversed.append(item[::-1])
    else:
      wordListReversed.append(item)
  finalString = " ".join(wordListReversed)
  return finalString