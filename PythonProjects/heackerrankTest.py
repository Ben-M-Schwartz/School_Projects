def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    k = 0
    ranks = []
    
    for i in range(len(player)):
        for j in range(k, len(ranked)):
            if(ranked[j] > player[i]):
                ranks.append(len(ranked) - j + 1)
                k = j
                break
            if(j == len(ranked)-1):
                ranks.append(1)
        
            
    return ranks


"""def pylons(k, arr):
    count = 0
    position = 0
    inRange = 0

    while position < len(arr):
        if position >= inRange:
            test = False
            back = position + k
            front = position - k + 1
            
            if(front<0):
                front = 0

            
            while position < back:
                if(arr[position] == 1):
                    test = True
                    position = j
            if (test == False):
                return -1
            count = count + 1
            front = position

        
        position = position+1
    return count




print(pylons(2, [0,1,1,1,1,0]))
print(pylons(2, [0,1,0,0,0,1,0]))
print(pylons(3, [0,1,0,0,0,1,1,1,1,1]))"""




"""class Solution(object):
   def search(self, nums, target):
      low = 0
      high = len(nums)
      while low<high:
         mid = low + (high-low)//2
         if nums[mid] == target:
            return mid
         if nums[low]<=nums[mid]:
            if target >=nums[low] and target <nums[mid]:
               high = mid
            else:
               low = mid+1
         else:
            if target<=nums[high-1] and target>nums[mid]:
               low = mid+1
            else:
               high = mid
      return -1"""


def search(nums, target):
        if(len(nums) == 0):
            return -1
        
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            return -1
        
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i = i + 1
        
        left = nums[:i]
        right = nums[i:]
        print(i)
        print(left)
        print(right)
        
        def binarySearch(arr,x):
            l = 0
            r = len(arr)-1
  
            while l <= r: 
  
                mid = l + (r - l) // 2; 

                if arr[mid] == x: 
                    return mid 
  
                elif arr[mid] < x: 
                    l = mid + 1

                else: 
                    r = mid - 1
      
            return -1
            
        searchLeft = binarySearch(left,target)
        searchRight = binarySearch(right,target)
            
        if(searchRight > -1):
            searchRight = searchRight + i
            
        return max(searchLeft, searchRight)

print(search([3,1], 1))
arr = [3,1]
print(arr[:1])
print(arr[1:])

def binarySearch(arr,x):
    l = 0
    r = len(arr)-1
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 

        if arr[mid] == x: 
            return mid 
  
        elif arr[mid] < x: 
            l = mid + 1

        else: 
            r = mid - 1
      
    return -1

        
        
