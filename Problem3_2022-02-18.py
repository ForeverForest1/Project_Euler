"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

#iterate numbers below limit
limit = 600851475143
f = 2
while f<=limit:
    rem = limit%f  #divide limit by smallest factor
    if rem == 0: #if divisible, keep dividing by same factor. until reminder is not 0
        reduce = limit/f
        limit = reduce
    else:        #start dividing by next bigger factor
        f = f+1
#print(reduce)
print(f)
