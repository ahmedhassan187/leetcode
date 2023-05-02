class Solution {
public:
    int arraySign(vector<int>& nums) {
        int sum = 1;
        for(int i=0;i<nums.size();i++){
            if (nums[i]==0){
                return 0;
            }
            else{
                sum =sum*nums[i];
            }
// to avoid overflow for int so take sign only from number
            if(sum<0){
                sum=-1;
            }
            else{
                sum=1;
            }
        }
        if(sum >0){
            return 1;
        }
        else{
            return -1;
        }
    }
};
