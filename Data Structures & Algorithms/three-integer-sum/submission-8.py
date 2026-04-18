class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out = []
        for i, num in enumerate(nums):
            left_pointer = i + 1
            right_pointer = len(nums) - 1

            if i > 0 and num == nums[i - 1]:
                continue

            target = -num
            while left_pointer < right_pointer:
                if nums[left_pointer] + nums[right_pointer] > target:
                    right_pointer -= 1
                elif nums[left_pointer] + nums[right_pointer] < target:
                    left_pointer += 1
                else:
                    out.append([num, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1

                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1

        return out