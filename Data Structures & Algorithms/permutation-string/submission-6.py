class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first thought can sort both arrays and then go through the indexes until 
        #you end the longer one, if at the end the index of shorter is less than its
        #length return false
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        sortA = "".join(sorted(s1))

        for i in range(0, n2-n1+1, 1):
            substr = s2[i:i+n1]
            substrA = "".join(sorted(substr))
            if sortA == substrA:
                return True
        return False
    

        
        