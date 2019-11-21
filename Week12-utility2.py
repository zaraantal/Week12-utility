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
