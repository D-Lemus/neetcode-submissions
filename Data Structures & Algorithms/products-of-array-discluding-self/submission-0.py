class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        output = [1] * len(nums)

        prefix = 1
        for n in range(len(nums)):
            output[n] = prefix
            prefix *= nums[n]
        
        postfix=1
        for n in range(len(nums) -1,-1,-1):
            output[n] *= postfix
            postfix *= nums[n]
        
        return output


            
