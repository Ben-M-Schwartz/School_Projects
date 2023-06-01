def mergeSort(mylist):
    print("Splitting", mylist)
    
    if len(mylist)>1:
        if len(mylist) == 2:
            list1 = [mylist[0]]
            list2 = [mylist[1]]
            list3 = []

        else:
            length = len(mylist)
            split1 = (length)//3
            split2 = 2*((length)//3)

            list1 = mylist[:split1]
            list2 = mylist[split1:split2]
            list3 = mylist[split2:]

        mergeSort(list1)
        mergeSort(list2)
        mergeSort(list3)

        i = 0
        j = 0
        k = 0
        l = 0

        while i<len(list1) and j<len(list2) and k<len(list3):
            if list1[i] <= list2[j]:
                if list1[i] <= list3[k]:
                    mylist[l] = list1[i]
                    i += 1
                    l += 1
                else:
                    mylist[l] = list3[k]
                    k += 1
                    l+=1
            else:
                if list2[j] <= list3[k]:
                    mylist[l] = list2[j]
                    j += 1
                    l+=1
                else:
                    mylist[l] = list3[k]
                    k += 1
                    l+=1
        while i<len(list1) and j<len(list2):
            if list1[i] <= list2[j]:
                mylist[l] = list1[i]
                i += 1
                l+=1
            else:
                mylist[l] = list2[j]
                j += 1
                k+=1
                
        while j<len(list2) and k<len(list3):
            if list2[j] <= list3[k]:
                mylist[l] = list2[j]
                j += 1
                l+=1
            else:
                mylist[l] = list3[k]
                k += 1
                l+=1

        while i<len(list1) and k<len(list3):
            if list1[i] <= list3[k]:
                mylist[l] = list1[i]
                i += 1
                l+=1
            else:
                mylist[l] = list3[k]
                k += 1
                l+=1

        while i < len(list1):
            mylist[l] = list1[i]
            i += 1
            l+=1

        while j < len(list2):
            mylist[l] = list2[j]
            j += 1
            l+=1

        while k < len(list3):
            mylist[l] = list3[k]
            k += 1
            l+=1
    print("Merging", mylist)


mylist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(mylist))
print(mylist)

