# Runtime is going to be O(N) for both solutions. However, this one has spacetime of O(N), where we can do it in O(1)
# Runtime: O(N)
# Spacetime: O(N)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        max_flowers = 0
        for mid in range(1, len(flowerbed) - 1):
            left, right = mid - 1, mid + 1
            if flowerbed[left] == 0 and flowerbed[right] == 0 and flowerbed[mid] == 0:
                flowerbed[mid] = 1
                max_flowers += 1

        return max_flowers >= n








