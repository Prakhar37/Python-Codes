alist = list(range(1,101))
d = []
for a in alist:
    n = alist.count(a)
if n>1:
        if d.count(a) == 0:
            d.append(a)
#print(d)   

#AND
#to show that numbers are repeating

list = [1,2,2,3,3,6,7]
d = []
for a in list:
    n = list.count(a)
    if n>1:
        if d.count(a) == 0:
            d.append(a)
print(d) 