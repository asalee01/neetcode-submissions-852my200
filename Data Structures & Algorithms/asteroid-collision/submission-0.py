class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                coll = stack[-1] + ast
                if coll > 0:
                    ast = 0
                elif coll < 0:
                    stack.pop()
                else:
                    ast = 0
                    stack.pop()
            if ast != 0:
                stack.append(ast)
        return stack
