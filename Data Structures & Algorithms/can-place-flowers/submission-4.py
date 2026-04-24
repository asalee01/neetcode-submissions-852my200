class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = n
        flowers = [0] + flowerbed + [0]
        for i in range(1, len(flowers)-1):
            if flowers[i] == 0 and flowers[i-1] == 0 and flowers[i+1] == 0:
                flowers[i] = 1
                cnt -= 1
        
        return cnt <= 0
        