class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mincandidate = prices[0];
        int profit = 0;
        for(int i =0; i<prices.size(); i++)
        {
            if(mincandidate>=prices[i])
            {   
            mincandidate = prices[i];   
            }else if (profit<prices[i]-mincandidate){
                profit=prices[i]-mincandidate;//4 // 5 // 6
            }
        }
        return profit;
    }
};
