class Tree:
    def __init__(self, name, data):
        self.children = data
        self.name = name

def challenge1(input):
    nodes = []
    for i in range(0, len(input)):
        contains = []
        main_bag = input[i].split("bags contain ")
        sub_bags = main_bag[1].split(", ")

        if(len(sub_bags) != 0 and sub_bags[0] != "no other bags."):
            for i in range(0, len(sub_bags)):
                spl2 = sub_bags[i].split(" ")
                res = spl2[1] + " " + spl2[2]
                
                i = 0
                while(i < len(nodes)):
                    if(nodes[i].name == res):
                        break
                    else:
                        if(i == len(nodes) - 1):
                            i = -1
                            break 
                        i+=1
                if(i >= 0 and i < len(nodes)):
                    contains.append(nodes[i])
                else:
                    child = Tree(res, [])
                    nodes.append(child)
                    contains.append(child)

        root = Tree(main_bag[0], contains)
        nodes.append(root)
        # print("adding: ", root.children[0].name)
        # root.children = contains
    
    for i in range(0, len(input)):
        in_order(nodes[i])
        # print(nodes[i].name)
    return None

def in_order(input):
    if(input == None): return
    length = len(input.children)
    if(length > 0): in_order(input.children[0])
    
    print(input.name)
    
    if(length > 1): in_order(input.children[1])


if __name__ == '__main__':
    with open('inputs/day7_sample.txt') as fh:
        sample = [line.strip() for line in fh.readlines()]
    print(challenge1(sample))

    # with open('inputs/day7_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge1(input))

    # with open('inputs/day7_sample.txt') as fh:
    #     sample = [line.strip() for line in fh.readlines()]
    # print(challenge2(sample))

    # with open('inputs/day7_input.txt') as fh:
    #     input = [line.strip() for line in fh.readlines()]
    # print(challenge2(input))