class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #for each number in the array, 
        #grab target - number
        #see if any of 

        #if its greater than the target we can ignore
        #we only care about the list up to the target
        #numbers before the target
        #(1, 1, 1, 1, 2, 3, 8, 9)

        #for each number, find the difference and then see if the
        #difference is in the string, if no then skip

        for index_1, number in enumerate(numbers): 
            value_2 = target - number 

            if value_2 in numbers:
                for index_2, n in enumerate(numbers):
                    if n == value_2:
                        return [index_1 + 1, index_2 + 1]
        