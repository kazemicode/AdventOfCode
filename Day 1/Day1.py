freqs = open("input.txt", 'r').read().split()
result_freq = 0
count = 0
seen = []

def resulting_frequency():
    result = 0
    for current_freq in freqs:
        result = result + int(current_freq)
        print(result)
    return result



def getFirstRepeat():
    global freqs
    global result_freq
    global count
    print("try number ", count)

    for current_freq in freqs:
        seen.append(result_freq)
        result_freq = result_freq + int(current_freq)
        if result_freq in seen:
            print(result_freq)
            return
    count = count + 1
    getFirstRepeat()



getFirstRepeat()
