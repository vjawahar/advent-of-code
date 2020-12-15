import csv

def challenge1(input):
    res = 0
    for i in range(0, len(input)): 
        list = input[i][0].split()
     
        nums = list[0].split("-")
        min = int(nums[0])
        max = int(nums[1])

        letter = (list[1].split(":"))[0]
        count = 0

        for j in list[2]:
            if(j == letter): count+= 1

        if(count >= min and count <= max): res+=1

    return res

def challenge2(input):
    res = 0
    for i in range(0, len(input)): 
        list = input[i][0].split()

        nums = list[0].split("-")
        pos1 = int(nums[0])
        pos2 = int(nums[1])

        letter = (list[1].split(":"))[0]

        if((list[2][pos1 - 1] == letter) ^ (list[2][pos2 - 1] == letter)): res+= 1

    return res

if __name__ == '__main__':
    # CHALLENGE 1: 
    # with open('inputs/day2_sample.csv') as f:
    #     reader = csv.reader(f)
    #     sample = list(reader)
    # print(challenge1(sample))
    # with open('inputs/day2_input.csv') as f:
    #     reader = csv.reader(f)
    #     input = list(reader)
    # print(challenge1(input))

    # CHALLENGE 2:
    with open('inputs/day2_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    print(challenge2(sample))
    with open('inputs/day2_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    print(challenge2(input))
