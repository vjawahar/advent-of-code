import csv, re

def challenge1(input):
    passport = 0
    num_cred = 0
    for i in range(0, len(input)):
        if(len(input[i]) != 0):
            spl = input[i][0].split()
            # print(spl)
            for j in range(0, len(spl)):
                temp = spl[j].split(":")
                if(temp[0] != "cid"): num_cred += 1
            # print(num_cred)
        else: 
            if(num_cred == 7): passport += 1
            num_cred = 0

    if(num_cred == 7): passport += 1
    return passport

def challenge2(input):
    num_cred = 0
    passport = 0
    for i in range(0, len(input)):
            # check_valid(input[i][0]) group everyone up into one
        if(len(input[i]) != 0):
            spl = input[i][0].split()
            # print(spl)
            for j in range(0, len(spl)):
                temp = spl[j].split(":")
                # print("temp: ", temp) 
                val = True
                #check validity of each, as long as each one is valid I can add it to the num of creds
                if(temp[0] == "ecl"): val = ecl(temp[1])
                if(temp[0] == "pid"): val = pid(temp[1])
                if(temp[0] == "byr"): val = byr(temp[1])
                if(temp[0] == "iyr"): val = iyr(temp[1])
                if(temp[0] == "eyr"): val = eyr(temp[1])
                if(temp[0] == "hgt"): val = hgt(temp[1])
                if(temp[0] == "hcl"): val = hcl(temp[1])

                if(val and temp[0] != "cid"): 
                    num_cred += 1
            # print(num_cred)
        else: 
            if(num_cred == 7):
                passport += 1
            num_cred = 0
    if(num_cred == 7): passport += 1    
    return passport


def ecl(input):
    if(input == "amb" or input == "blu" or input == "brn" or input == "gry" or input == "grn" or input == "hzl" or input == "oth"): return True
    return False
def pid(input):
    pattern = r'^[0-9]{9}$'
    match = re.search(pattern, input)
    if(match != None and match.group(0) == input): return True
    return False
def byr(input): 
    num = int(input)
    if(num >= 1920 and num <= 2002): return True
    return False
def iyr(input):
    num = int(input)
    if(num >= 2010 and num <= 2020): return True
    return False
def eyr(input):
    num = int(input)
    if(num >= 2020 and num <= 2030): return True
    return False
def hgt(input): 
    pattern1 = r'^(1[5-8][0-9]|19[0-3])cm$'
    pattern2 = r'^(59|6[0-9]|7[0-6])in$'

    match1 = re.search(pattern1, input)
    match2 = re.search(pattern2, input)

    if((match1 != None and match1.group(0) == input) or (match2 != None and match2.group(0) == input)): return True
    return False
def hcl(input):
    pattern = r'^#[0-9a-f]{6}$'
    match = re.search(pattern, input)
    if(match != None and match.group(0) == input): return True
    return False

def check_valid(input):
    num_cred = 0
    spl = input.split()
    for j in range(0, len(spl)):
        temp = spl[j].split(":")
        if(temp[0] != "cid"): num_cred += 1
    if(num_cred == 7): return True
    return False

if __name__ == '__main__':
    # CHALLENGE 1: 
    # with open('inputs/day4_sample.csv') as f:
    #     reader = csv.reader(f)
    #     sample = list(reader)
    # print(challenge1(sample))
    # with open('inputs/day4_input.csv') as f:
    #     reader = csv.reader(f)
    #     input = list(reader)
    # print(challenge1(input))

    # CHALLENGE 2:
    # with open('inputs/day4_sample.csv') as f:
    #     reader = csv.reader(f)
    #     sample = list(reader)
    # print(challenge2(sample))
    with open('inputs/day4_input.csv') as f:
        reader = csv.reader(f)
        input = list(reader)
    print(challenge2(input))





