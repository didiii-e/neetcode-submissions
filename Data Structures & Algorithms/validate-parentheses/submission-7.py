class Solution:
    def isValid(self, s: str) -> bool:

        s = s.strip()

        valid_pairs = {")" : "(","]" : "[","}" : "{"}
        stack = []

        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char in valid_pairs:
                if stack and stack[-1] == valid_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True

        


                