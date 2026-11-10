class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [0] * len(isConnected)
        rank = [1] * len(isConnected)

        #start by setting each city to be its own province
        for i in range(len(isConnected)):
            parents[i] = i
        
        #finds the parent of the node "x"
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x,y):
            pX = find(x)
            pY = find(y)

            if pX == pY:
                return False

            if rank[pX] > rank[pY]:
                #merge y onto x 
                parents[pY] = pX
            elif rank[pY] > rank[pX]:
                #merge x onto y
                parents[pX] = pY
            else:
                parents[pY] = pX
                rank[pX] += 1
            return True
        count = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        count -= 1
        
        return count
                
        


            
        
        



            
    
        
        