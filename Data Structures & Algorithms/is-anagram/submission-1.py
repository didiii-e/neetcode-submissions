class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        #question: does string s and string t contain same combination of characters
        #method, iterate through string
        #check if character is in dictionary
        #if yes, add to the value
        #if no

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] = s_dict[s[i]] + 1 
            else:
                s_dict[s[i]] = 0

            if t[i] in t_dict:
                t_dict[t[i]] = t_dict[t[i]] + 1 
            else:
                t_dict[t[i]] = 0

        if s_dict == t_dict:
            return True
        else:
            return False 
                
                


        