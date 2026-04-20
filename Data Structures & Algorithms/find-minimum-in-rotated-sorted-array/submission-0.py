class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            if nums[left_pointer] <= nums[right_pointer]:
                result = min(result, nums[left_pointer])
                break

            middle = (left_pointer + right_pointer) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left_pointer]:
                left_pointer = middle + 1
            else:
                right_pointer = middle - 1

        return result