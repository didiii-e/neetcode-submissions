class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_list = []
        max_length = 1

        if len(s) < 2:
            return len(s)

        for char in s:
            print('char', char)
            if char not in max_list:
                print('entered first if')
                max_list.append(char)
            else:
                #xyx
                print('entered else')
                for i, a in enumerate(max_list):
                    if a == char:
                        if i < (len(max_list) - 1):
                            max_list = max_list[i+1:]
                            max_list.append(char)
                        else:
                            max_list = []
                            max_list.append(char)
                
            print('max_list after update:', max_list)
            
            if len(max_list) > max_length:
                max_length = len(max_list)
        
        return max_length
        

'''
dvdf
once you get to d, remove the first instance

abcc



you have to find where the repetition 
happens and then set list to everything after the repeat

'''