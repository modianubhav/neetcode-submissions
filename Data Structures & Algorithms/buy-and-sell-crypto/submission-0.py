class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low_price = prices[0]
        profit = 0

        for price in prices:
            low_price = min(low_price, price)
            profit = max(profit, price-low_price)

        return profit
        