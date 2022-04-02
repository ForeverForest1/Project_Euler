"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
#brute force. can try to slice string and reverse next time (a[::-1], where a is the list)
lst = list()
def oddtest(x):
    n = 0
    lastdigit = int(repr(x)[n-1])
    seclast = int(repr(x)[n-2])
    firstdigit = int(repr(x)[n])
    secdigit = int(repr(x)[n+1])
    middigit = int(repr(x)[n+2])
    if secdigit - middigit == seclast - middigit:
        if firstdigit == lastdigit:
            lst.append(x)

def eventest(x):
    n = 0
    lastdigit = int(repr(x)[n-1])
    seclast = int(repr(x)[n-2])
    firstdigit = int(repr(x)[n])
    secdigit = int(repr(x)[n+1])
    thirdigit = int(repr(x)[n+2])
    thirlast = int(repr(x)[n-3])
    if secdigit == seclast:
        if firstdigit == lastdigit:
            if thirdigit == thirlast:
                lst.append(x)

for i in range(100,1000):
    for k in range(100,1000):
        prod = i*k
        if len(str(prod)) == 5:
            oddtest(prod)
        elif len(str(prod)) == 6:
            eventest (prod)
        else:
            print("not 5 or 6 digits")
            oddtest(prod)
print(max(lst))
