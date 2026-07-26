class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #find smallest value
        #find max value after smallest value 

        #work backwards, store max value and 
        #find diffrence between all subsequent values 
        #store in set and grab max 

        max_val = 0
        diff = set()

        if len(prices) == 1:
            return 0

        for i in range(len(prices)-1, -1, -1):

            if prices[i] > max_val:
                max_val = prices[i]
            
            profit = max_val - prices[i]
            
            diff.add(profit)
        
        return max(diff)
        

            






        