class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])
            postfix.append(postfix[-1] * nums[len(nums) - i - 1])

        return [prefix[j] * postfix[len(nums) - j - 1] for j in range(len(nums))]