class Solution {
public:
    int search(vector<int>& nums, int target) {

        int hi = nums.size() -1;
        int lo = 0;
        int mid = 0;

        while(hi>=lo)
        {
            mid = lo + (hi - lo)/2;
            
            if(nums[mid] == target) return mid;

            if(nums[mid] < target)
            {
                lo = mid +1;
            }
            else
            {
                hi = mid -1;
            }
        }
        return nums[mid] == target ? mid : -1;
        
    }
};
