class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
                freq[i] = freq.get(i,0)+1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, frequency in freq.items():
            buckets[frequency].append(num) 


        result = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
        
                for num in buckets[i]:
                    result.append(num)

                    if len(result) == k:
                        return result
        return result


