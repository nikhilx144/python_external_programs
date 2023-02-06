n = int(input("Enter a positive integer: "))
for i in range(1, n//2 + 1):
    if n == 4*i + 6:
        print(f"{n} is a consecutive four sum number")
        break
else:
    print(f"{n} is not a consecutive four sum number")
