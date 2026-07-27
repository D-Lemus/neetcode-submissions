class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s) != len(t): return False

        for i in s:
            if i in freq:
                freq[i] += 1
                
            else:
                freq[i] = 1

        for i in t:
            if i not in freq:
                return False

            if i in freq:
                freq[i] -= 1
                if freq[i]==0:
                    del freq[i]

        if not freq:
            return True
        else:
            return False
        