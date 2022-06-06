def sum(str):
    sum = 0
    for a in str:
        if a.isdigit() == True:
            b = int(a)
            sum = sum + b
    return sum
print(sum ("123gugu4575"))    
print(sum("h20 15 wa73r"))