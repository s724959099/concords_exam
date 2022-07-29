"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
import typing


class Solution(object):
    def maxProfit(self, prices: typing.List[int]) -> int:
        min_price = prices[0] if prices else 0
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


if __name__ == '__main__':
    s = Solution()
    d = []
    assert s.maxProfit(d) == 0
    d = [1, 2, 3, 0, 2]
    assert s.maxProfit(d) == 2
    d = [7, 1, 5, 3, 6, 4]
    assert s.maxProfit(d) == 5
    d = [7, 6, 4, 3, 1]
    assert s.maxProfit(d) == 0
