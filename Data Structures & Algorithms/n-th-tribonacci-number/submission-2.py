class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0,1,1]
        # we update curr % 3 to be curr sum
        # at the end return n % 3.
        if (n < 3):
            return t[n]
        for i in range (3, n+1):
            t[i % 3] = sum(t)
        return t[n%3]
        

        