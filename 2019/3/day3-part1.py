def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])

def storePos(path):
    positions = set()
    x = 0
    y = 0
    for item in path:
        direction = item[0]
        amount = int(item[1:])
        for i in range(amount):
            if direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'R': x += 1
            elif direction == 'L': x -= 1
            else: print("an error occurred")

            positions.add((x,y))
    return positions


with open("input.txt", 'r') as f:
    w1 = f.readline().strip().split(',')
    w2 = f.readline().strip().split(',')


wire1 = storePos(w1)
wire2 = storePos(w2)
cross = wire1.intersection(wire2)

closestIntersection = min(cross, key=manhattan)

print(closestIntersection, manhattan(closestIntersection))
