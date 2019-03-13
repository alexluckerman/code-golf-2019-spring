lastNum = 3
for prime in range(5, 100000):
  isPrime = True
  for num in range(2, prime):
    if prime % num == 0:
        isPrime = False
        break
  if isPrime:
        print(str(lastNum) + ' ' + str(prime))
        lastNum = prime