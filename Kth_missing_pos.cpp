class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int i=0;
        int j=1;
        int counter=0;
        while(counter<k){
            if(i<arr.size()){
                if(arr[i]==j){
                    i++;
                    j++;
                }
                else{
                    j++;
                    counter++;
                }
            }
            else{
                j++;
                counter++;
            }
        }
        return j-1;
    }
};
