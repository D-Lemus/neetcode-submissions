class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        remove_char = [" ",".",",","?","!",";",":","'","\""]
        s = s.lower()

        for char in remove_char:
            s = s.replace(char,"")

        if s[::-1] == s:
            return True
        else:
            return False


        