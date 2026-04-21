class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs

    def helper(self, i, current_comb, combs, n, k):
        if len(current_comb) == k:
            combs.append(current_comb.copy())
            return
        if i > n:
            return

        current_comb.append(i)
        self.helper(i + 1, current_comb, combs, n, k)
        current_comb.pop()

        self.helper(i + 1, current_comb, combs, n, k)