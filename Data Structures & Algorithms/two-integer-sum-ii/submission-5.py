class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(numbers)):
            want = target - numbers[i]
            if want in visited:
                return [visited[want], i+1]
            visited[numbers[i]] = i+1
        return []
        