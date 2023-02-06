n = int(input("Enter the number of students: "))
present = input()
present_lst = list(set(present.split()))
absent_lst = []
for i in range(1, n + 1):
    if str(i) not in present_lst:
        absent_lst.append(i)
absent_lst.sort()
for i in absent_lst:
    print(i, end=" ")