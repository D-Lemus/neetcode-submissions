class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Input: nums = [1,4,1,2]
        # Output: [1,4,1,2,1,4,1,2]
        length = len(nums)
        new_length = 2 * len(nums)
        ans = [0] * new_length

        i=0
        j=0
        while j < new_length:
            if i == length:
                i = 0

            ans[j]=nums[i]

            j+=1
            i+=1

        return ans



  