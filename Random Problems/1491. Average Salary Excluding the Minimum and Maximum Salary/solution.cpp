class Solution {
public:
    double average(vector<int>& salary) {
        int mini = 0;
        int maxi = 0;
        for(int i=0;i<salary.size();i++){
            if(salary[i]>salary[maxi]){
                maxi = i;
            }
            if(salary[i]<salary[mini]){
                mini = i;
            }
        }
        if(mini>maxi){
        salary.erase(salary.begin()+mini);
        salary.erase(salary.begin()+maxi);
        }
        else{
         salary.erase(salary.begin()+maxi);
        salary.erase(salary.begin()+mini);   
        }
        double ans = double(accumulate(salary.begin(),salary.end(),0))/double(salary.size());
        return ans;
    }
};
