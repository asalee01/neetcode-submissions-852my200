class Solution:
    def tribonacci(self, n: int) -> int:
        self.fib0 = 0
        self.fib1 = 1
        self.fib2 = 1
        # we update curr % 3 to be curr sum
        # at the end return n % 3.
        for i in range (3, n+1, 1):
            if (i % 3 == 0):
                self.fib0 = self.fib0 + self.fib1 + self.fib2
            elif (i% 3 == 1) :
                self.fib1 = self.fib0 + self.fib1 + self.fib2
            else:
                self.fib2 = self.fib0 + self.fib1 + self.fib2
        if (n % 3 == 0):
            return self.fib0
        elif (n % 3 == 1):
            return self.fib1
        else:
            return self.fib2
        

        