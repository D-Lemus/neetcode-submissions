class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t):
            return False

        for char in s:         
            if char in freq:
                freq[char] += 1
            elif char not in freq:
                freq[char] = 1
            
        for char in t:
            
            if char not in freq:
                return False     
            elif char in freq:
                freq[char]-=1
                if freq[char] == 0:
                    del freq[char]
        
        if not freq:
            return True
        else:
            return False



        
