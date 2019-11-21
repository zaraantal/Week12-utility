#Zara Antal
#CSCI 102 - Section C
#Week 12 - Part A

def PrintOutput(word):
    PrintOutput(word)

def LoadFile(file):
    list1 = []
    my_file = open(filename)
    for line in my_file:
        list1.append(line.strip())
    my_file.close()
    return list1

def UpdateString(string1,string2,index):
    if(index>=0 and index<len(string1)):
        string1 = string1[:index] + string2 + string1[index+1:]
    return string1

def FindWordCount(list1, string):
    count = 0
    for i in list1:
        if string in i:
            count = count + 1
    return count

def ScoreFinder(player_names, player_scores, player_to_find):
    scores = -1
    for i in range(len(player_names)):
        if(player_names[i].lower() == player_to_find.lower()):
            scores = player_scores[i]
            break
    if(player_scores == -1):
        print("player not found")
    else:
        print(player_to_find,"got a score of",score)

def Union(A, B):
    world_list = []
    for i in A:
        if i not in world_list:
            world_list.append(i)
    for i in B:
        if i not in world_list:
            world_list.append(i)
    return world_list

def Intersection(list1, list2):
    world_list = []
    for x in list1:
        if (not x in world_list) and (x in list2):
            for i in range(min(list1.count(x), list2.count(x))):
                world_list.append(x)
    return world_list


