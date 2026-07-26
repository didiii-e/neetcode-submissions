class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_vals = set()

        for char in nums:
            if char in unique_vals:
                return True
            else:
                unique_vals.add(char)
        
        return False

 


 #appears more than once
 #sets contain unique values and also have a runtime of O(1)
 #

        