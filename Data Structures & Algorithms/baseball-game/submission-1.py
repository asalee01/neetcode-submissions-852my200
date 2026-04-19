class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res, stack = 0, []
        for oper in operations:
            if (oper == "+"):
                stack.append(stack[-1] + stack[-2])
                res += stack[-1]
            elif (oper == "C"):
                val = stack.pop()
                res -= val
                del val 
            elif(oper == "D"):
                stack.append(stack[-1] * 2)
                res += stack[-1]

            else:
                stack.append(int(oper))
                res += int(oper)
        del stack
        return res
            
        