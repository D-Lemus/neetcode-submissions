class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for num in s:
            if num in freq:
                freq[num] += 1
            elif num not in freq:
                freq[num] = 1


        for num in t:

            if num not in freq:
                return False

            freq[num] -= 1
            if freq[num] == 0:
                del freq[num]
            
        
        if not freq:
             return True
        else: 
            return False