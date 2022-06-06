a = 1
b = 100
print("Prime numbers between 1 and 100 are:")
for no in range(a,b+1):
    if no > 1:
        for i in range(2,no):
            if(no % i) == 0:
                break
        else:
            print(no)    