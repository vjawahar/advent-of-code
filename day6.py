
def challenge1(input):
    count = 0
    current = []
    for i in range(0, len(input)):
        if(len(input[i]) != 0):
            for j in range(0, len(input[i])):
                if(not input[i][j] in current):
                    current.append(input[i][j])
        else:
            count += len(current)
            current = []
    count+= len(current)
    return count


def challenge2(input):
    count = 0
    start_row = 0
    for i in range(0, len(input)):
        if(len(input[i]) == 0):
            for j in range(0, len(input[start_row])):
                letter_count = 1
                for k in range(start_row + 1, i):
                    if(not input[start_row][j] in input[k]):
                        break
                    else:
                        letter_count+=1
                if(letter_count == (i - start_row)): 
                    count+=1
            start_row = i + 1
    
    for j in range(0, len(input[start_row])):
        letter_count = 1
        for k in range(start_row + 1, i + 1):
            if(not input[start_row][j] in input[k]):
                break
            else:
                letter_count+=1
        if(letter_count == (i + 1 - start_row)): 
            count+=1
    return count


if __name__ == '__main__':
    # with open('inputs/day6_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day6_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day6_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day6_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))