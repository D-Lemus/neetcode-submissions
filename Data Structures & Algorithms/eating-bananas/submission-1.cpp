class Solution {

private:
    long long maxHours(vector<int> &piles, int mid){
        int hours = 0;
        for(int p: piles)
        {
            hours += (p+mid-1) /mid;
        }

        return hours;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int lo = 1;
        int hi = *max_element(piles.begin(), piles.end());
        while(hi > lo)
        {
            int mid = lo + (hi -lo) / 2;

            if(maxHours(piles, mid) > h)
            {
                lo = mid+1;
            }else{
                hi = mid;

            }

        }
        return lo;
        
        
    }
};
