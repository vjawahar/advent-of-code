counter = [0]
counter[0] = 1
def challenge1(input):
    # print(len(input))
    # print(len(input[0]))
    # print(input[0])
    # input[0] = input[0][0:1] + "n" + input[0][2:10]
    # print(input[0])
    # temp = input
    # keep a count and keep going until there are no new changes
    i = 0
    while(counter[0] != 0): #counter != 0
        # print("temp: ", temp)
        input = run_board(input)
        i+=1
        # print("counter: ", counter[0])

    occ_count = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if(input[i][j] == "#"): occ_count += 1
    return occ_count

def run_board(input):
    counter[0] = 0
    # print("INPUT: ", input)
    temp2 = input[:]
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            char = temp2[i][j]
            if(char == "L"):
                if(none_occupied(temp2, i, j)):
                    # print("here!")
                    counter[0]+=1
                    input[i] = input[i][0:j] + "#" + input[i][j+1:len(input[i])] 
                    # print("new input: ", input[i])
            elif(char == "#"):
                if(num_occupied(temp2, i, j) >= 4):
                    counter[0]+=1
                    input[i] = input[i][0:j] + "L" + input[i][j+1:len(input[i])] 
                    # print("new input: ", input[i])

    # print("ending input: ", input)
    return input    


def none_occupied(input, i, j):
    # print("i: ", i, " and j: ", j)
    # print("input: ", input)
    if(boundaries(i-1, j) and not check_occupied(input, i - 1, j, "#")): 
        # print("false 1")
        return False
    if(boundaries(i-1, j - 1) and not check_occupied(input, i - 1, j-1, "#")): 
        # print("false 2")
        return False
    if(boundaries(i-1, j + 1) and not check_occupied(input, i - 1, j + 1, "#")): 
        # print("false 3")
        return False
    
    if(boundaries(i+1, j) and not check_occupied(input, i + 1, j, "#")): 
        # print("false 4")
        return False
    if(boundaries(i+1, j-1) and not check_occupied(input, i + 1, j-1, "#")): 
        # print("false 5")
        return False
    if(boundaries(i+1, j+1) and not check_occupied(input, i + 1, j + 1, "#")): 
        # print("false 6")
        return False
  
    if(boundaries(i, j-1) and not check_occupied(input, i, j-1, "#")): 
        # print("CHAR IS: ", input[i][j-1])
        # print("false 7")
        return False
    if(boundaries(i, j + 1) and not check_occupied(input, i, j + 1, "#")): 
        # print("false 8")
        return False
    
    else:
        # print("here att true (everything was empty!)") 
        return True

def num_occupied(input, i, j):
    count = 0
    # print("i: ", i, " and: ", j)
    if(boundaries(i-1, j) and check_occupied2(input, i - 1, j)): 
        # print("count 1")
        count += 1
    if(boundaries(i-1, j-1) and check_occupied2(input, i - 1, j-1)): 
        # print("count 2")
        count += 1
    if(boundaries(i-1, j + 1) and check_occupied2(input, i - 1, j + 1)): 
        # print("count 3")
        count += 1
   
    if(boundaries(i+1, j) and check_occupied2(input, i + 1, j)): 
        # print("count 4")
        count += 1
    if(boundaries(i+1, j-1) and check_occupied2(input, i + 1, j-1)): 
        # print("count 5")
        count += 1
    if(boundaries(i+1, j+1) and check_occupied2(input, i + 1, j + 1)): 
        # print("count 6")
        count += 1
    
    if(boundaries(i, j-1) and check_occupied2(input, i, j-1)): 
        # print("count 7")
        count += 1
    if(boundaries(i, j+1) and check_occupied2(input, i, j + 1)): 
        # print("check: ", input[i][j+1])
        # print("count 8")
        count += 1

    return count

def check_occupied(input, i, j, char):
    if(i >= 0 and i < 97 and j >= 0 and j < 91):
        if(not input[i][j] == char): return True
    else: 
        return False

def check_occupied2(input, i, j):
    if(i >= 0 and i < 97 and j >= 0 and j < 91):
        if(input[i][j] == "#"): return True
    else: 
        return False

def boundaries(i, j): 
    if(i >= 0 and i < 97 and j >= 0 and j < 91): return True
    else: return False



def challenge2(input):
    while(counter[0] != 0):
        input = run_board2(input)

    occ_count = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if(input[i][j] == "#"): occ_count += 1
    return occ_count


def run_board2(input):
    counter[0] = 0
    # print("INPUT: ", input)
    temp2 = input[:]
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            char = temp2[i][j]
            if(char == "L"):
                if(check_surrounding(temp2, i, j) == 0):
                    # print("here!")
                    counter[0]+=1
                    input[i] = input[i][0:j] + "#" + input[i][j+1:len(input[i])] 
                    # print("new input: ", input[i])
            elif(char == "#"):
                if(check_surrounding(temp2, i, j) >= 5):
                    counter[0]+=1
                    input[i] = input[i][0:j] + "L" + input[i][j+1:len(input[i])] 
                    # print("new input: ", input[i])

    # print("ending input: ", input)
    return input  

def check_surrounding(input, i, j):
    count_occupied = 0
    # Top Left
    if(get_next_seat(input, i-1, j-1, -1, -1)): count_occupied+=1

    #Top
    if(get_next_seat(input, i-1, j, -1, 0)): count_occupied+=1   

    #Top Right
    if(get_next_seat(input, i-1, j+1, -1, 1)): count_occupied+=1 

    #Left
    if(get_next_seat(input, i, j-1, 0, -1)): count_occupied+=1 

    #Right
    if(get_next_seat(input, i, j+1, 0, 1)): count_occupied+=1 

    #Bottom Left
    if(get_next_seat(input, i+1, j-1, 1, -1)): count_occupied+=1 

    #Bottom
    if(get_next_seat(input, i+1, j, 1, 0)): count_occupied+=1    

    #Bottom Right
    if(get_next_seat(input, i+1, j+1, 1, 1)): count_occupied+=1  

    return count_occupied

def get_next_seat(input, i, j, i_step, j_step):
    if(not boundaries(i, j) or input[i][j] == "L"):
        return False
    if(input[i][j] == "#"):
        return True
    else:
        return get_next_seat(input, i + i_step, j + j_step, i_step, j_step)

if __name__ == '__main__':
    # with open('inputs/day11_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day11_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day11_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day11_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))