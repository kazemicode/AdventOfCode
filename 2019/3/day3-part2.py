def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])

def storePos(path):
    positions = {}
    x = 0
    y = 0
    steps = 0
    for item in path:
        direction = item[0]
        amount = int(item[1:])
        for i in range(amount):
            if direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'R': x += 1
            elif direction == 'L': x -= 1
            steps += 1
            pos = (x,y)
            if pos not in positions:       # only store first time reached
                positions[pos] = steps
    return positions


with open("input.txt", 'r') as f:
    w1 = f.readline().strip().split(',')
    w2 = f.readline().strip().split(',')


wire1 = storePos(w1)
wire2 = storePos(w2)
cross = set(wire1.keys()).intersection(set(wire2.keys()))


leastSteps = float('inf')

for position in cross:
    if wire1[position] + wire2[position] < leastSteps:
        leastSteps = wire1[position] + wire2[position]
        intersection = position
print("Least amount of steps to intersection %s is %d steps" %(intersection, leastSteps))
