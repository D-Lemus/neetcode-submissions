class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(s)!=len(t):
            return False

        for word in s:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        for word in t:
            if word in freq:
                freq[word] -= 1
                if freq[word] ==0:
                    del freq[word]
            else:
                return False


        if not freq:
            return True
        else:
            return False