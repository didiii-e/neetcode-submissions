class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create list to store dictionaries in
        dict_list = []
        str_list = []

        #create list of strings to iterate through
        str_list.append(s)
        str_list.append(t)

        #quick case to check 
        if len(s) != len(t):
            return False 

        #iterate through strings
        for str_type in str_list :

            test = dict()

            #for each string, iterate through its characters
            for val in range(len(str_type)):
                char = str_type[val]

                if char in test:
                    test[char] = test[char] + 1 
                else:
                    test[char] = 0 

            
            dict_list.append(test)


        if dict_list[0] == dict_list[1]:
            return True
        else:
            return False



#method one, for each item in list one, check against list 2
#O(n^2)

#method two, compare string lenths, if non equal immediate false
#if equal, go through str1 and create a dictionary, for each letter how many times it appears

#create dic
        