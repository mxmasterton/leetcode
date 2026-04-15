class Solution:
    def merge(self, nums_a: List[int], m: int, nums_b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointer_a = m - 1
        pointer_b = n - 1
        pointer_out = m + n - 1

        while pointer_a >= 0 and pointer_b >= 0:
            if nums_a[pointer_a] >= nums_b[pointer_b]:
                nums_a[pointer_out] = nums_a[pointer_a]
                pointer_a -= 1
            else:
                nums_a[pointer_out] = nums_b[pointer_b]
                pointer_b -= 1
            pointer_out -= 1

        while pointer_b >= 0:
            nums_a[pointer_out] = nums_b[pointer_b]
            pointer_b -= 1
            pointer_out -= 1
