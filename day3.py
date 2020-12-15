import csv


def challenge1(input):
    col = 0
    trees = 0
    for i in range(0, len(input)):
        # print("i: ", input[i])
        # print(input[i][0][0])
        if(input[i][0][col] == "#"): trees+=1  
        col+=3
        if(col >= len(input[i][0])): col= col -len(input[i][0]) 
    return trees

def challenge2(input):
    col1 = 0
    col2 = 0
    col3 = 0
    col4 = 0
    tree0 = challenge1(input)
    tree1 = 0
    tree2 = 0
    tree3 = 0
    tree4 = 0
    for i in range(0, len(input)):
        # print("i: ", input[i])
        # print(input[i][0][0])
        if(input[i][0][col1] == "#"): tree1+=1  
        if(input[i][0][col2] == "#"): tree2+=1 
        if(input[i][0][col3] == "#"): tree3+=1 
        
        col1+=1
        col2+=5
        col3+=7
        if(col1 >= len(input[i][0])): col1 = col1 -len(input[i][0]) 
        if(col2 >= len(input[i][0])): col2 = col2 -len(input[i][0]) 
        if(col3 >= len(input[i][0])): col3 = col3 -len(input[i][0]) 

    for j in range(0, len(input), 2):
        if(input[j][0][col4] == "#"): tree4+=1  
        col4+=1
        if(col4 >= len(input[j][0])): col4= col4 -len(input[j][0]) 

    return tree0 * tree1 * tree2 * tree3 * tree4

if __name__ == '__main__':
    # CHALLENGE 1: 
    # with open('inputs/day3_sample.csv') as f:
    #     reader = csv.reader(f)
    #     sample = list(reader)
    # print(challenge1(sample))
    # with open('inputs/day3_input.csv') as f:
    #     reader = csv.reader(f)
    #     input = list(reader)
    # print(challenge1(input))

    # CHALLENGE 2:
    with open('inputs/day3_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    print(challenge2(sample))
    with open('inputs/day3_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    print(challenge2(input))
