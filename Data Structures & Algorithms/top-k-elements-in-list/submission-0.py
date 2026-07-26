class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        answer = {}
        final = []
        max_value = 0 

        #create dictionary with number : frequency 
        for n in nums:
            if n in answer:
                answer[n] += 1          
            else:
                answer[n] = 1

        #create list of lists of length length nums 
        #iterate through each freqency count starting at len(nums) -1 
        
        buckets = [[] for _ in range(len(nums) + 1 )]

        print(len(buckets))

        #dictionary
        #key: the number of repeats
        #values: the original number

        print(answer)

        for keys, values in answer.items():
            print("key, value")
            print((keys ,values))
            buckets[values].append(keys)


        #grab k, work backwards, see which 

        for frequency in range(len(buckets) - 1, 0, -1):
            for number in buckets[frequency]:
                final.append(number)

            if len(final) == k:
                return final
        
        return final 

        

        