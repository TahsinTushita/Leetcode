class Solution:
    def maxProfit(self, prices) -> int:
        price = prices[0]
        profit = 0
        start = 1
        end = len(prices)

        while start < end:
            if prices[start] < price:
                price = prices[start]
            elif prices[start] - price > profit:
                profit = prices[start] - price
            start += 1
        return profit

if __name__ == '__main__':
    s1 = Solution()
    print(s1.maxProfit([7,1,5,3,6,4,7,0]))