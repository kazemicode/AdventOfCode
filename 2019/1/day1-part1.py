data = open("input.txt", 'r').read().split()
result = 0

def calcFuel():
    global result
    for mass in data:
        result += int(mass)/3-2
    return result


print(calcFuel())
