"""
final answer should be 233168 (based on Excel)
"""
def totalmult(x):
    sum = 0
    n = 1
    final = 0
    multiple = 1
    while multiple < 1000:
        multiple = x*n
        sum = sum + multiple
        #print(n,multiple,sum)
        n = n+1
    if multiple>=1000:
        final = sum - multiple
    else:
        final = sum
    return final
    #print("sum of multiple of",x,":",final)

totaltrio = totalmult(3)
print("sum of multiple of 3:",totaltrio)
totalpenta = totalmult(5)
print("sum of multiple of 3:",totalpenta)
totaldup = totalmult(15)
print("sum of multiple of 15:",totalpenta)
answer = totalmult(3) + totalmult(5) - totalmult(15)
print("answer:",answer)
