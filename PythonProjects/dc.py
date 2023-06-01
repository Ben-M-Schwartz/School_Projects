def binOnes(alist):
    if len(alist) == 1:
        return alist[0]

    mid = len(alist)//2
    return binOnes(alist[:mid]) + binOnes(alist[mid:])


def smallestMissing(alist, low, high):
    if(high-low <= 1):
        if alist[low] != low:
            return low
        elif alist[high] != high:
            return high
        else:
            return None
    mid = (high+low)//2
    if alist[mid] == mid:
        return smallestMissing(alist, mid, high)
    else:
        return smallestMissing(alist, low, mid)


def dcMul(a, b):
    if b==1:
        return a

    return dcMul(a, (b+1)//2) + dcMul(a, b//2)


def dcExp(a, b):
    if b==0:
        return 1
    if b==1:
        return a
    return dcExp(a, (b+1)//2) * dcExp(a, b//2)


def dcSumArray(alist):
    if len(alist) == 1:
        return alist[0]
    mid = len(alist)//2
    return dcSumArray(alist[:mid]) + dcSumArray(alist[mid:])


def maxSubArray(alist):
    if len(alist) == 1:
        return alist
    mid = len(alist)//2
    leftList = maxSubArray(alist[:mid])
    rightList = maxSubArray(alist[mid:])
    sm1 = 0
    sum1 = -999999
    position1 = mid
    for i in range(mid, len(alist)):
        sm1 = sm1 + alist[i]
        if(sm1 > sum1):
            sum1 = sm1
            position = i+1
        

    sm2 = 0
    sum2 = -9999999
    position2 = mid-1
    for j in range(mid-1, 0, -1):
        sm2 = sm2 + alist[j]
        if(sm2 > sum2):
            sum2 = sm2
            position2 = j-1

    print(alist)
    print([position2, position1])


    midList = alist[position2:position1]

    leftSum = sum(leftList)
    rightSum = sum(rightList)
    midSum = sum(midList)

    maxSum = max(leftSum, rightSum, midSum)

    if(leftSum == maxSum):
        return leftList
    elif(rightSum == maxSum):
        return rightList
    else:
        return midList
    

def checkMajority(x, alist):
    count = 0
    for i in range(len(alist)):
        if(x == alist[i]):
            count = count+1
    return count

def equivalent(alist):
    if(len(alist) == 1):
        return alist[0]
    mid = len(alist)//2
    x = equivalent(alist[:mid])
    y = equivalent(alist[mid:])
    if (x == y):
        return x
    elif x!= None:
        a = checkMajority(x, alist[:mid])
        b = checkMajority(x, alist[mid:])
        if(a+b > mid):
            return x
    elif y!= None:
        a = checkMajority(y, alist[:mid])
        b = checkMajority(y, alist[mid:])
        if(a+b > mid):
            return y
    return None

def bankTest(alist):
    if (equivalent(alist) != None):
        return True
    else:
        return False


print(bankTest([1,2,3,2,2,2,2,2,2,2]))

    def minDistance(self, dist, sptSet): 
   
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
   
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 
   
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
   
        for cout in range(self.V): 
   
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
   
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
   
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and \ 
                     sptSet[v] == False and \ 
                     dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
   
        self.printSolution(dist)

    def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxint 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
  
        # Key values used to pick minimum weight edge in cut 
        key = [sys.maxint] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
  
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent)

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in 
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't
            #  cause cycle, include it in result 
            #  and increment the indexof result 
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print "Edges in the constructed MST"
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)







    
