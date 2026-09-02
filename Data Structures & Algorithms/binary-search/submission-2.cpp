class Solution {
public:
    int search(vector<int>& nums, int target) {

        
        int hi = nums.size() -1 ;
        int lo = 0;
        int mid = hi-lo+1/2;

        while(hi>lo){

            if(nums[mid] == target) return mid;

            else if(nums[mid]>target)
            {
                hi = mid-1;
                mid = lo + (hi-lo+1)/2;
            }
            else
            {
                lo = mid+1;
                mid = lo + (hi-lo+1)/2;
            }


        }

        return nums[mid] == target ? mid: -1;

        
    }
};
