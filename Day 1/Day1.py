file = open("input.txt", 'r').read().split()
sum = 0

for line in file:
    sum = sum + int(line)

print(sum)

