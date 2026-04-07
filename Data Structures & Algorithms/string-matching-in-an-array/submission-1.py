class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        #words.sort(key=len)
        for i in words:
            for j in words:
                if(len(i) <= len(j) and i != j):
                    if i in j:
                        res.add(i)
        return list(res)
        