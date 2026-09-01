class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = sys.maxsize
        curr_price = 0
        max_price = 0

        for price in prices:
            curr_price = price - min
            if curr_price > max_price:
                max_price = curr_price

            elif price < min:
                min = price
            

        
        return max_price


            



