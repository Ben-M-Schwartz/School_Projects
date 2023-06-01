def biggestSubSequence(list1, list2):
    common = [[0 for i in range(len(list1))] for j in range(len(list2))]
    if list1[0] == list2[0]:
        common[0][0] = 1
    for i in range(1,len(list1)):
        for j in range(1,len(list2)):
            if list1[i] == list2[j]:
                common[i][j] = common[i-1][j-1] + 1

    Max = 0
    index1 = 0
    index2 = 0
    
    for i in range(len(list1)):
        for j in range(len(list2)):
            if common[i][j] > Max:
                Max = common[i][j]
                index1 = i
                index2 = j

    subSequence = []

    while index1 >0 or index2 > 0:
        if common[index1-1][index2-1] == common[index1][index2]-1:
            subSequence.append(list1[index1])
            index1 = index1-1
            index2 = index2-1
        else:
            index2 = index2 - 1

    for i in range(len(subSequence)):
        temp = subSequence[i]
        subSequence[i] = subSequence[len(subSequence)-i-1]
        subSequence[len(subSequence)-i-1] = temp

    print(subSequence)


biggestSubSequence([1,2,3,4,5,6], [1,4,2,3,6,5])

            


