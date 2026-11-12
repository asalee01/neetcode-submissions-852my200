class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp = [0] * len(temperatures)
        #monotonic increasing stack maintained
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                temp[idx]= i - idx 
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            temp[idx]= 0
        
        return temp
        #i = 0; stack = [30]
        #i = 1; stack = [38] temps = [1]
        #i = 2; stack = [38,30] temps = [1]
        #i = 3; stack = [38,36] temps = [1,X,1]
        # i = 4; stack = [38,36,35]
        #i=5; stack= [40] temps =[1,4,1,2,1,0,0]