class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_length = 1
        current_streak = 1
        nums_hash_set = set(nums)

        if not nums:
            return 0

        for n in nums:
            if n-1 in nums_hash_set:
                continue
            elif n+1 in nums_hash_set:
                for i in range (1, len(nums)):
                    if n+i in nums_hash_set:
                        current_streak += 1
                    else:
                        break

                if current_streak > max_length:
                    max_length = current_streak

                current_streak = 1

        return max_length
        