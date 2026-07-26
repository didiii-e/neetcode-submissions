class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        if len(s) < 2:
            return True

        for i in range(len(s)//2 + 1):
            first = s[i]
            last = s[len(s) - 1 - i]

            if first != last:
                return False
            
        return True


        #length of string
        #compare 0 with length of string - 1
        #compare 0 + 1 with lenth of string - 2 
        #if any of these are unequal, return false 
        