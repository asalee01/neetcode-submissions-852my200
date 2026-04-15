class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for num in range(1, numRows):
            temp = [1]
            for i in range(1, num):
                val = arr[num-1][i-1] + arr[num-1][i]
                temp.append(val)
            temp.append(1)
            arr.append(temp)
            del temp
        return arr


        