file = open("input.txt", 'r').read().split()
index_length = len(file)
word_length = len(file[0])


def checkSum():
    sum_threes = 0
    sum_twos = 0
    for id in file:
        for character in range(0, len(id) - 1):
            # print(id.count(id[character]))
            if id.count(id[character]) == 2:
                sum_twos = sum_twos + 1
                break
    for id in file:
        for character in range(0, len(id) - 1):
            # print(id.count(id[character]))
            if id.count(id[character]) == 3:
                sum_threes = sum_threes + 1
                character = len(id)
                break

    print(sum_twos * sum_threes)

def findSimilar():
    diffs = 0
    temp=""
    result=""
    for index in range(0, index_length):
        for jindex in range(index+1, index_length):
            for letter in range(0, word_length):
                #print(file[index][letter], file[jindex][letter])
                if diffs > 1:
                    break
                if file[index][letter] == file[jindex][letter]:
                    temp = temp + file[index][letter]

                else:
                    diffs = diffs + 1

            if diffs <= 1:
                result = result + temp
            temp = ""
            diffs = 0

    print(result)



checkSum()
findSimilar()




