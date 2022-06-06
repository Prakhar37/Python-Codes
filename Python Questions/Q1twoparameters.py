x = input("Give the numbers: ")
y = list(x)
z = input("Select the order: ")
if z == "asc":
    y.sort()
    print("This is in ascending order -", y)
elif z == "dsc":
    y.sort(reverse = True)
    print("This is descending order - ",y)
elif z == "none":
    print(y)