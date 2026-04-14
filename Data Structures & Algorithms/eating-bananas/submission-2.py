class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_pointer = 1
        right_pointer = max(piles)

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2

            time = sum(math.ceil(pile / middle) for pile in piles)
        
            if time <= h:
                result = middle
                right_pointer = middle - 1
            else:
                left_pointer = middle + 1

        return result