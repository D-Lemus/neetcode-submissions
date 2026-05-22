class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        counts = [0]*26
        base = ord("a")

        for i in range (len(s)):
            counts[ord(s[i]) - base ] += 1
            counts[ord(t[i]) - base ] -= 1

        return all(x == 0 for x in counts)
