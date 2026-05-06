class Solution:
    def isPrefixAndSuffix(self, prefix: str, word: str) -> bool:
        return word.startswith(prefix) and word.endswith(prefix) 
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if (i<j and self.isPrefixAndSuffix(words[i], words[j])):
                    count += 1
        return count
        