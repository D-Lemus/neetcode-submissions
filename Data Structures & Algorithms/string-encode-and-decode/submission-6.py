class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'pluh'

        coded_words = ''
        coded_word = ''
        for word in strs:
            for char in word:
                coded_word += bin(ord(char))[2:] + '#'
            coded_words += coded_word + ' '
            coded_word = ''
        return coded_words[:-1:]


    def decode(self, s: str) -> List[str]:

        if s == 'pluh':
            return []

        s = s.split(' ')
        uncoded_words = []
        uncoded = []

        for word in s:
            uncoded = word.split('#')
            for char in range(len(uncoded)-1):
                uncoded[char] = chr(int(str(uncoded[char]),2))
            uncoded_words.append(''.join(uncoded))

        return uncoded_words
