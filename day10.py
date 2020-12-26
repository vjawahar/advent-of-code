
def challenge1(input):
    val = helper1(input, 0, 0, 0)
    return val
def helper1(input, index, one_count, three_count):
    if(index >= len(input)):
        return (one_count + 1) * (three_count + 1)
    
    if(str(int(input[index]) + 1) in input):
        return helper1(input, index + 1, one_count+1, three_count)
    
    elif(str(int(input[index]) + 3) in input):
        return helper1(input, index + 1, one_count, three_count+1)
    else:
        return helper1(input, index + 1, one_count, three_count)
counter=[0]
def challenge2(input):
    index = input.index('1')
    helper2(input, index)
    if('2' in input):
        index = input.index('2')
        helper2(input, index)
    if('3' in input):
        index = input.index('3')
        helper2(input, index)
    return counter[0]

def helper2(input, index):
    if(not str(int(input[index]) + 1) in input and not str(int(input[index]) + 2) in input and not str(int(input[index]) + 3) in input):
        counter[0]+=1

    if(str(int(input[index]) + 1) in input):
        new_index = input.index(str(int(input[index]) + 1))
        helper2(input, new_index)

    if(str(int(input[index]) + 2) in input):
        new_index = input.index(str(int(input[index]) + 2))
        helper2(input, new_index)

    if(str(int(input[index]) + 3) in input):
        new_index = input.index(str(int(input[index]) + 3))
        helper2(input, new_index)    
    
def jolt_arrange(input):
    sorted = list(map(lambda x : int(x), input))
    sorted += [0, max(sorted)+3]
    sorted.sort()
    # print(sorted)
    total_paths = 1
    # Possible ways to arrange numbers when >1 combo exists
    # 0, 1, 2, 3, 5, (8)    i = 2, i + 1 = 3
    vals_to_combos = {1:1, 2:1, 3:2, 4:4, 5:7}
    start = 0
    for i in range(len(sorted)-1):
        # print(i+1, sorted[i], start)
        # for sequences with >1 possible permutation
        if sorted[i] + 1 != sorted[i+1]:
            num = vals_to_combos[(i+1)-start]
            # print("num: ", num)
            total_paths *= num
            # print(total_paths)
            start = i+1
    
    return total_paths

def challenge3(input):
    val = helper3(input, 0, 1, 1, 1)
    return val

def helper3(input, index, one_count, two_count, three_count):
    if(index >= len(input)):
        print(three_count)
        return (one_count) * (two_count) * (three_count)
    
    if(str(int(input[index]) + 1) in input):
        return helper3(input, index + 1, one_count+1, two_count, three_count)
    elif(str(int(input[index]) + 2) in input):
        return helper3(input, index + 1, one_count, two_count + 1, three_count)
    elif(str(int(input[index]) + 3) in input):
        return helper3(input, index + 1, one_count, two_count, three_count+1)
    else:
        return helper3(input, index + 1, one_count, two_count, three_count)

if __name__ == '__main__':
    # with open('inputs/day10_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day10_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day10_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # # print(challenge2(sample))
    # print(jolt_arrange(sample))
    # print(challenge3(sample))

    with open('inputs/day10_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    # print(challenge2(input))
    print(jolt_arrange(input))
