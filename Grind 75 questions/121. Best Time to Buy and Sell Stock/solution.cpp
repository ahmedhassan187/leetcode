class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxi =INT_MAX;
        int temp = 0;
        int res=0;
        for(int i=0;i<prices.size();i++){
                if(prices[i]<maxi){
                    maxi=prices[i];
                }
                temp = prices[i] - maxi;
                if(res<temp){
                    res = temp;
                // }
            }
        }
        return res;
}};
