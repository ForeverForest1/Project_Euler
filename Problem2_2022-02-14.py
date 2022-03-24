"""
find even value terms
Conditions:
1) num%2 = 0
2) num < 4*10**6

fibonacci: 1, 2, 3, 5, 8, 13, 21, 34, 55
sum of fibonacci < 40: 2 + 8 + 34 = 44

"""
#initialising
f1 = 1
f2 = 2
fn = f1
sum = f2
limit = 40

while f2<limit:
    fn = fn + f2
    f2 = fn + f2
    print("int_fn:", fn)
    print("int_f2:", f2)
    if fn < limit:
        if fn%2 == 0: #add to sum if fn is even number
            sum = sum + fn
            print("int_sum:", sum)
    #f2 = fn + f2
    #print("int_f2:", f2)
    if f2 < limit: #add to sum if f2 is even number
        if f2%2 == 0:
            sum = sum + f2
            print("intsum:", sum)
    #fn = fn + f2
    #print("int_2_fn:",fn)
    continue
print("final sum:",sum)

"""
#correct answer obtained
f1 = 1
f2 = 2
fn = f1
sum = f2
limit = 4*10**6

while f2<limit:
    fn = fn + f2
    print("int_fn:", fn)
    if fn < limit:
        if fn%2 == 0:
            sum = sum + fn
            print("int_sum:", sum)
    f2 = fn + f2
    print("int_f2:", f2)
    if f2 < limit:
        if f2%2 == 0:
            sum = sum + f2
            print("intsum:", sum)
    #fn = fn + f2
    #print("int_2_fn:",fn)
    continue
print("final sum:",sum)

"""
