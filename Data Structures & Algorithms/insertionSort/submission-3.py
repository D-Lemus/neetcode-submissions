# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if not pairs:
            return []
            
        iterations = []
        pairs_copy = [Pair(p.key,p.value) for p in pairs]
        iterations.append(pairs_copy)


        for i in range(1, len(pairs)):
            prev = i - 1

            while prev >= 0 and pairs[prev+1].key<pairs[prev].key:
                
                tmp = pairs[prev+1]
                pairs[prev+1] = pairs[prev]
                pairs[prev] = tmp
                prev -= 1

            pairs_copy = [Pair(p.key,p.value) for p in pairs]
            iterations.append(pairs_copy)


        return iterations
