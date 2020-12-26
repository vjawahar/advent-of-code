def challenge1(input):
    for i in range(25, len(input)):
        val = helper1(input, input[i], i)
        if(val != None): return val

    return None

def helper1(input, num, i):
    for j in range(i - 25, i):
        if(int(input[j]) <= int(num)):
            for k in range(j + 1, i):
                if(int(input[k]) + int(input[j]) == int(num)): return None
    return num

def challenge2(input):
    num = challenge1(input)
    ind = input.index(num)
    for i in range(0, ind):
        val = helper2(input, int(num), 0, i, int(input[i]), int(input[i]))
        if(val != None): return val[0] + val[1]
            
    return None

def helper2(input, num, acc, index, min, max):
    if(index >= len(input)):
        return None
    current = int(input[index])
    acc += current
    if(current < min): min = current
    if(current > max): max = current
    if(acc == num):
        val = []
        val.append(min)
        val.append(max)
        return val
    if(acc > num):
        return None
    else: 
        return helper2(input, num, acc, index+1, min, max)



if __name__ == '__main__':
    # with open('inputs/day9_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day9_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day9_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day9_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))