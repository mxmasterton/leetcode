class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy_pointer = 0
        sell_pointer = 0

        while sell_pointer < len(prices):
            if prices[sell_pointer] - prices[buy_pointer] > 0:
                profit = max(profit, prices[sell_pointer] - prices[buy_pointer])
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1

        return profit