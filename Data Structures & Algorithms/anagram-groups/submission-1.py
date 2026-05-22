class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_anagrams = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in grouped_anagrams:
                grouped_anagrams[key] = []

            grouped_anagrams[key].append(word)

            

        return list(grouped_anagrams.values())

                

        

















        