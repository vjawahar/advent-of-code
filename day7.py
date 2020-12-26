def challenge1(input):
    bags = {}
    for i in range(0, len(input)):
        main_bag_list = input[i].split(" bags contain ")
        sub_bags = main_bag_list[1].split(", ")
        main_bag = main_bag_list[0]
        child = {}
        if(len(sub_bags) != 0 and sub_bags[0] != "no other bags."):
            for i in range(0, len(sub_bags)):
                spl2 = sub_bags[i].split(" ")
                num = int(spl2[0])
                res = spl2[1] + " " + spl2[2]
                child[res] = num
        bags[main_bag] = child
            # if(bags.get(main_bag) == None):print("error") #error
        
    # print(bags)
    count = 0
    for key, val in bags.items():
        if(key != "shiny gold"):
            if(helper(bags, key)): 
                count += 1
    return count

# for key,val in bags.items():
#     key = red
#     val = {muted yellow: 2, brighht white: 1}

def helper(input, name):
    # print("helper called")
    if(name == "shiny gold"):
        # print("HERE AT SHINY GOLD with count: ", count)
        # return count
        return True
    if(input.get(name) == None):
        return False
    else: 
        for key, val in input[name].items():
            val = helper(input, key)
            if(val):
                return True
        return False


def challenge2(input):
    count = 0
    bags = {}
    for i in range(0, len(input)):
        main_bag_list = input[i].split(" bags contain ")
        sub_bags = main_bag_list[1].split(", ")
        main_bag = main_bag_list[0]
        child = {}
        if(len(sub_bags) != 0 and sub_bags[0] != "no other bags."):
            for i in range(0, len(sub_bags)):
                spl2 = sub_bags[i].split(" ")
                num = int(spl2[0])
                res = spl2[1] + " " + spl2[2]
                child[res] = num
        bags[main_bag] = child
    # print(bags["dotted black"].values())
    # if(not bags["dotted black"].values()): print("heyo")
    return helper2(bags, "shiny gold")

def helper2(input, name):
    # if(not input[name].values()): 
    #     return 1
    # else: 
    val = 0
    for color, count in input[name].items():
        val += count*(1 + helper2(input, color)) 
    return val

if __name__ == '__main__':
    # with open('inputs/day7_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge1(sample))

    # with open('inputs/day7_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day7_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    with open('inputs/day7_input.txt') as fh:
        input = [line.strip() for line in fh.readlines()]
    print(challenge2(input))