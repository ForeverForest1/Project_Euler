"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 +...10^2 = 385

The square of the sum of the first ten natural numbers is, (1+2+...10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


sumsq = 0 #sum of squares
sum = 0 #unsquared sum
for i in range(1,101):
    sq = i**2
    sumsq = sumsq + sq
    sum = sum + i
sqsum = sum**2 #square of unsquared sum
diff = sqsum - sumsq
print("Square of sum:", sqsum)
print("Sum of sq:", sumsq)
print("Difference:", diff)
