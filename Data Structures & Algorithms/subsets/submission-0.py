class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, current_set = [], []
        self.helper(0, nums, current_set, subsets)
        return subsets

    def helper(self, i, nums, current_set, subsets):
        if i >= len(nums):
            subsets.append(current_set.copy())
            return

        # decision to include nums[i]
        current_set.append(nums[i])
        self.helper(i + 1, nums, current_set, subsets)
        current_set.pop()

        # decision NOT to include nums[i]
        self.helper(i + 1, nums, current_set, subsets)