data = open("input.txt", 'r').read().split()
result = 0

def main():
    for mass in data:
        calcFuel(mass)

def calcFuel(mass):
    global result
    fuel = int(mass)/3-2
    result += fuel
    if fuel/3 > 2:      # don't calculate negative fuel -- that's weird
        calcFuel(fuel)  # figure out how much fuel you need to carry the fuel

main()
print(result)
