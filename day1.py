import csv

def challenge1(input):
    # Loop through input 
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            if int(input[i][0]) + int(input[j][0]) == 2020:
                return int(input[i][0]) * int(input[j][0])
    # No matches found
    return None

def challenge2(input):
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            remaining = 2020 - (int(input[i][0]) + int(input[j][0]))
            num_list = [0]
            num_list[0] = str(remaining)
            if num_list in input:
                return int(input[i][0]) * int(input[j][0]) * remaining
    return None

if __name__ == '__main__':
    # CHALLENGE 1: 
    # with open('inputs/day1_sample.csv') as f:
    #     reader = csv.reader(f)
    #     sample = list(reader)
    # print(challenge1(sample))
    # with open('inputs/day1_input.csv') as f:
    #     reader = csv.reader(f)
    #     input = list(reader)
    # print(challenge1(input))

    # CHALLENGE 2:
    with open('inputs/day1_sample.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    print(challenge2(sample))
    with open('inputs/day1_input.csv') as f:
        reader = csv.reader(f)
        sample = list(reader)
    print(challenge2(sample))
  