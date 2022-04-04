"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#prime numbers between 1-20 are 1, 2, 3, 5, 7, 11, 13, 17 and 19.
#Common multiples in range 1-20 have to be multiples of the product of these prime numbers
n= 9699690 #product of all prime numbers between 1-20
while True:
    sum = 0
    for f in range(1,21):
        rem = n%f
        sum = sum + rem
    if sum != 0: #if sum of remainder is 0, tested number can be evenly divided by all numbers in the range
        print(f"There is remainder. Test num is {n}, Last factor is {f}, Sum of Rem is {sum}")
        n = n+9699690 #increment of test number by value of this prime product, since answer is a multiple of this number
        True #restart while loop
    elif sum == 0:
        print(f'Answer is {n}')
        break #stop while loop if answer is found
