#include <stack>
class Solution {
public:
    bool isValid(string s) { 
        stack<char> stack;
        for(int i=0;i<s.length();i++){
        if(s[i]=='('||s[i]=='{'||s[i]=='['){
            stack.push(s[i]);
        }else{
            if(stack.empty()){
                return false;
            }
            char x = stack.top();
            if (x=='(' && s[i]==')'){
                stack.pop();
            }
            else if (x=='{'&& s[i]=='}'){
                stack.pop();
            }
            else if(x=='['&& s[i]==']'){
                stack.pop();
            }
            else{
                return false;
            }
        }
        }
        if(stack.empty()){
            return true;
        }
        else{
            return false;
        }
    }};
