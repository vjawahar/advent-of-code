visited = []

def challenge1(input):
    visited = []
    return helper(input, 0, 0)

def helper(input, index, acc):
    if(index >= len(input) or index in visited):
        return acc
    else: 
        visited.append(index)
        spl = input[index].split(" ")
        if(spl[0] == "acc"): 
            acc += int(spl[1])
            return helper(input, index+1, acc)
        if(spl[0] == "jmp"):
            return helper(input, index + int(spl[1]), acc)
        else: return helper(input, index+1, acc)

def challenge2(input): #iterate through input copy, if I get a jmp/nop switch it in the copy. Each time I change, run the copy through and see if I get a valid number
    temp = input
    for i in range(0, len(input)):
        spl = input[i].split(" ")
        if(spl[0] == "jmp"):
            # print("switich jmp to nop")
            temp[i] = "nop " + spl[1]
            val = helper2(temp, 0, 0, [])
            if(val != None): return val
            # print("temp: ", temp)
            temp[i] = "jmp " + spl[1]
        if(spl[0] == "nop"):
            # print("switich nop to jmp")
            temp[i] = "jmp " + spl[1]
            val = helper2(temp, 0, 0, [])
            if(val != None): return val
            temp[i] = "nop " + spl[1]
    # print(problem)
    # spl = input[problem[0]].split(" ")
    # if(spl[0] == "jmp"): 
    #     input[problem[0]] = ""
    # if(spl[0] == "nop"):
    #     input[problem[0]] = ""
    return None

def helper2(input, index, acc, visited2):
    # print("index: ", index)
    if(index in visited2):
        # print("visited: ", visited2)
        return None
    if(index >= len(input)):
        return acc
    else: 
        visited2.append(index)
        spl = input[index].split(" ")
        if(spl[0] == "acc"): 
            acc += int(spl[1])
            return helper2(input, index+1, acc, visited2)
        if(spl[0] == "jmp"):
            return helper2(input, index + int(spl[1]), acc, visited2)
        else: return helper2(input, index+1, acc, visited2)


if __name__ == '__main__':
    # with open('inputs/day8_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day8_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day8_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day8_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))