class Solution {
public:
    int addDigits(int num) {
    if((num%10)==num){
        return num;
    }
    else{
        return addDigits(int(num/10)+(num%10));
    }
    }
};
