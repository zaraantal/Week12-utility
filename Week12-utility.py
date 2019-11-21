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

def ScoreFinder(player_names, player_scores, name):
    score = -1
    for i in range(len(player_names)):
        if(player_names[i].lower() == name.lower()):
            score = player_scores[i]
            break
    if(player_scores == -1):
        print("player not found")
    else:
        print(name,"got a score of",score)
