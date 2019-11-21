#Zara Antal
#CSCI 102 - Section C
#Week 12 - Part A

def PrintOutput(word):
    print(word)

def LoadFile(file):
    contents = []
    my_file = open(file)
    for line in my_file:
        contents.append(line.strip())
    my_file.close()
    return contents

def UpdateString(string1, string2, plc):
    if plc < len(string1):
        string1 = string1[:plc] + string2 + string1[plc+1:]
    return string1

def FindWordCount(list1, string):
    count = 0
    for i in list1:
        if string in i:
            count = count + 1
    return count

def ScoreFinder(players, scores, find):
    score = -1
    for i in range(len(players)):
        if(players[i].lower == find.lower()):
            score = scores[i]
            break
    if scores == -1:
        print("player not found")
    else:
        print(find, "got a score of", score)

def Union(A, B):
    world_list = []
    for i in A:
        if i not in world_list:
            world_list.append(i)
    for i in B:
        if i not in world_list:
            world_list.append(i)
    return world_list

def Intersection(A, B):
    world_list = []
    for x in A:
        if (not x in world_list) and (x in B):
            for i in range(min(A.count(x), B.count(x))):
                world_list.append(x)
    return world_list

def NotIn(list1, list2):
    world_list = []
    for i in list1:
        if i not in list2:
            world_list.append(x)
    return world_list


