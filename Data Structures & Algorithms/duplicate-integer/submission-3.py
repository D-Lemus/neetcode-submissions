class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        if len(nums) >1:
            for num in nums:
                if num in seen:
                    return True
                    del seen

                seen.append(num)

        del seen
        return False
        