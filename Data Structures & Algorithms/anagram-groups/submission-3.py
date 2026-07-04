class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        seen_words = {}

        for word in strs:

            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word in seen_words:
                seen_words[sorted_word].append(word)

            else:
                seen_words[sorted_word] = [word]

        return list(seen_words.values())             



