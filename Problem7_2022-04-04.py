"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
"""
useful link:
https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
"""

lstprime = list()
def primes(n):
  sieve = [True] * (n+1)
  for p in range(2, n+1):
    if (sieve[p]):
      #print (p)
      lstprime.append(p)
      for i in range(p, n+1, p):
        sieve[i] = False

primes(150000)
print(len(lstprime))
print(lstprime[0])
print(lstprime[10000])
