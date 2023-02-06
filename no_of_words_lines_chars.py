chars = 0
words = 0
lines = 0
with open("text.txt", "r") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line.strip('\n'))
print(f"Lines: {lines}\nWords: {words}\nCharacters: {chars}")
