class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        shifted = {target - x for x in nums}
        result = {}

        for i in range(len(nums)):
            if nums[i] in shifted:
                result[i] = nums[i]

        if len(result) ==3:
            result = {
            index: value
            for index, value in result.items()
            if value != target/2
        }
    
    
        return list(result.keys())


#looks through append
#if length 2, return
#if length 3, remove the value where shifted = target/2 

#create a dictionary of each pair of index and value
#if dictionary length 2, return the indexes 
#if dictionary length 3, delete the value where = target/2 


#if target/2 exists in nums, it will break
#if target/2 is the only repeat, then that is the answer 
        


#for i, iterate through and sum up i with i+1, i+2..., then for 
#i+1, iterate through and fum up i+1 + i+2, etc and 
#depending on the location of place where it sums it up, can figure out index

#array and dictionary/sets here 

#target - nums, and then 
#the answer is the two digits that exist in both sets 

#target - nums = 
#[-3, -4, 0, 3, 7]
#target = -7
#[-4, -3, -7, -10, -14] -- nums2, has to be a set 
#O(n)

#for num in nums 
#   does nums[i] exist in nums2, if yes, return i 


        