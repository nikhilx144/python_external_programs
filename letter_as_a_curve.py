zero = ["C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "S", "T", "U", "V", "W", "X", "Y", "Z"]
one = ["A", "D", "O", "P", "Q", "R"]
two = ["B"]

zero_h = 0
one_h = 0
two_h = 0

string = input("Enter the text in uppercase: ")
for i in string.upper():
    if i in one:
        one_h += 1
    elif i in two:
        two_h += 1
    elif i in zero:
        zero_h += 1
print(f"The total number of holes in the given text is {one_h + (2*two_h)}")