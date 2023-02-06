l = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele = int(input("Enter number: "))
    l.append((ele, ele**3))
print(l)
