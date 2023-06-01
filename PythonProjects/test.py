def quickSortHelper(myList, start, end):
    if start < end:

        pivot = myList[start]

        stop = False

        i = start+1
        j = end
        
        while stop == False:
            

            while myList[i] <= pivot and i<=j:
                i +=1

            while myList[j] >= pivot and j>=i:
                j -=1

            if j<i:
                stop = True
                
            else:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
                    
                
                
        temp = myList[start]
        myList[start] = myList[j]
        myList[j] = temp

        quickSortHelper(myList, start, j-1)
        quickSortHelper(myList, j+1, end)

    return myList

def quickSort(myList):
    return quickSortHelper(myList, 0, len(myList)-1)

print(quickSort([5, 4, 3, 2, 5, 3, 4, 6, 7, 8, 6, 7, 5, 6, 4, 4, 3]))
