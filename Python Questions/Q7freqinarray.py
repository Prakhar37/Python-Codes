from multiprocessing.dummy import Array


a = [1,2,2,3,3,3,3,3,4,4,4,4]
max =0
b = a[0]
for i in a:
    freq = a.count(i)
    if freq>max:
        max = freq
        b = i
print("The given set of numbers are ",a , "and the most frequent number is ", b)        

