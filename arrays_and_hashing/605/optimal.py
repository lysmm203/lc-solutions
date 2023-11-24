# Optimal solution doesn't initialize a new array. Still changes the flowerbed array though
# Runtime: O(N)
# Spacetime: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flowers = 0

        for mid in range(len(flowerbed)):
            left, right = mid - 1, mid + 1
            if (flowerbed[mid] == 0 and
            (left == -1 or flowerbed[left] == 0) and
            (right >= len(flowerbed) or flowerbed[right] == 0)):
                flowerbed[mid] = 1
                max_flowers += 1

        return max_flowers >= n