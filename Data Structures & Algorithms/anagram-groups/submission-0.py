class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = {}
        
        for s in strs:

            s_dict = {}

            key = "".join(sorted(s))

            if key in answer:
                answer[key].append(s)
            else:
                #need to store this as a list not a string 
                answer[key] = [s]
        
        return list(answer.values())









            


        
        

