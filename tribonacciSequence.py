def tribonacci(signature,n):
  tribonacciList = signature
  for x in range(0,n-3):
    newNum = tribonacciList[x] + tribonacciList[x+1] +tribonacciList[x+2]
    tribonacciList.append(newNum)
  return tribonacciList[0:n]