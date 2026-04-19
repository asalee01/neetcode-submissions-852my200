class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../" and len(stack) > 0:
                stack.pop()
                continue
            elif log == "../" and len(stack) == 0:
                continue
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)
        