class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #we have neighbors being defined as one with same color + [[0,1], [1,0], [0,-1], [-1,0]] from current pixel.
        #so from starting pixel do a dfsand the pixel you recurse if it meets
        #the condition, otherwise stop. 
        #we will be modifyin the original image array, so we return that.

        #EDGE CASES: atleast 1 row and col in image always,colors are ints cannot
        # be less than 0. 
        visited = []
        og_color = image[sr][sc]
        def dfs(i, j):
            #BASE CASE:
            if not ((image[i][j] == og_color)):
                return
            neighbors0 = [1,-1,0,0]
            neighbors1 = [0,0,1,-1]

            image[i][j] = color
            visited.append((i,j))
            for x in range(len(neighbors0)):
                if ((0 <= i+neighbors0[x] < len(image)) and 
                (0 <= j+neighbors1[x] < len(image[0])) and not (i+neighbors0[x], j+neighbors1[x]) in visited):
                    dfs(i+neighbors0[x], j+neighbors1[x])

        dfs(sr, sc)    
        return image
        