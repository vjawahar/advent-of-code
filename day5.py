


def challenge1(input):
    max_id = 0
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            # print(input[i][j])
            if(input[i][j] == "B"): 
                row_min = (row_max + row_min)/2 + 1
                # print("here at B: row min: ", row_min, " row max: ", row_max)
            if(input[i][j] == "F"):
                row_max = (row_max + row_min)/2
                # print("here at F: row min: ", row_min, " row max: ", row_max)
            if(input[i][j] == "L"):
                col_max = (col_max + col_min)/2
                # print("here at L")
            if(input[i][j] == "R"):
                col_min = (col_max + col_min)/2 + 1
                # print("here at R")
        # print("row min: " , row_min)
        # print("row max: ", row_min)
        # print("col min: ", col_min)
        # print("col max: ", col_max)
        #when out of loop, calaculate id
        id = row_max*8 + col_max
        # print("id: ", id)
        if(id > max_id): max_id = id
        col_max = 7 
        col_min = 0
        row_min = 0
        row_max = 127
    return max_id


def challenge2(input): #find all seat IDs, add them to the list, then iterate through 1-max and if an id is not in my list, check if the +1 and -1 are also not in list
    max_id = 0
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7
    id_list = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            # print(input[i][j])
            if(input[i][j] == "B"): 
                row_min = (row_max + row_min)/2 + 1
            if(input[i][j] == "F"):
                row_max = (row_max + row_min)/2
            if(input[i][j] == "L"):
                col_max = (col_max + col_min)/2
            if(input[i][j] == "R"):
                col_min = (col_max + col_min)/2 + 1
        id = row_max*8 + col_max
        if(id > max_id): max_id = id
        id_list.append(id)
        col_max = 7 
        col_min = 0
        row_min = 0
        row_max = 127


    for k in range(1, max_id):
        if(not k in id_list and k+1 in id_list and k-1 in id_list):
            return k
    return None


if __name__ == '__main__':
    # with open('inputs/day5_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day5_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day5_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day5_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))