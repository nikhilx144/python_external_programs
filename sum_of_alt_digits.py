num = input("Enter a positive number with even number of digits: ")
start = 0
end = 0
if len(num) % 2 == 0 and "-" not in num:
    for i in num[::2]:
        start += int(i)
    for i in num[-1::2]:
        end += int(i)
    print(f"Difference between sum of digits occurring in alternate positions is {abs(start - end)}")
else:
    print("Enter a valid number")