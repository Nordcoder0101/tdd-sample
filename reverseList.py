def reverseList(list):
    for i in range(0, (round(len(list)/2))):
        temp = list[i]
        list[i] = list[len(list)-1 -i]
        list[len(list)-1 - i] = temp
    return list
       

