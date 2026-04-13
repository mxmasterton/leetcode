class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2
            
            if nums[middle] < target:
                left_pointer = middle + 1
            elif nums[middle] > target:
                right_pointer = middle - 1
            else:
                return middle

        return -1
        