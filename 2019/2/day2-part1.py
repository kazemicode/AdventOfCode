

# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
# To run one, start by looking at the first integer (called position 0).
# Here, you will find an opcode - either 1, 2, or 99.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
#  The three integers immediately after the opcode tell you these three positions -
# the first two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
# Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

# Opcode 99 means that the program is finished and should immediately halt.

# Encountering an unknown opcode means something went wrong.


def restore(arr, one, two):
    # restore the gravity assist program (your puzzle input) to the "1202 program alarm" state
    # it had just before the last computer caught fire.
    # To do this, before running the program, replace position 1 with the value 12
    # and replace position 2 with the value 2
    arr[1] = one
    arr[2] = two

def intcode(data):
    i = 0
    while i < len(data):
        if data[i] == 99:
            print("halted")
            break
        elif data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        else:
            print("error")
            break
        i = i + 4


dataArray = []
with open("input.txt", 'r') as f:
    dataArray = [int(n) for n in f.read().split(',')]

restore(dataArray, 12, 2)
result = intcode(dataArray)
print(dataArray[0])

