class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if target == nums[middle_pointer]:
                return middle_pointer
            elif nums[left_pointer] <= nums[middle_pointer]:
                # left sorted portion
                if target > nums[middle_pointer] or target < nums[left_pointer]:
                    left_pointer = middle_pointer + 1
                else:
                    right_pointer = middle_pointer - 1
            else:
                # right sorted portion
                if target < nums[middle_pointer] or target > nums[right_pointer]:
                    right_pointer = middle_pointer - 1
                else:
                    left_pointer = middle_pointer + 1

        return -1
