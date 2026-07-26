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

        string_tuple = (s, t)
        results_list = []

        for i, string in enumerate(string_tuple):
            string_dict = {}
            for char in string:
                if char in string_dict:
                    string_dict[char] += 1
                else:
                    string_dict[char] = 0
                
            results_list.append(string_dict)
            
        
        if results_list[0] == results_list[1]:
            return True
        else:
            return False
                
                


        