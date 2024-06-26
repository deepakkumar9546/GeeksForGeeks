//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    bool ispar(string x)
    {
       stack<char> s;
       for(int i=0;i<x.length();i++){
           char ch=x[i];
           if(ch=='(' || ch=='{' || ch=='['){
               s.push(ch);
           }
           else{
               if(!s.empty()){
                   char top=s.top();
                if((ch==')' && top=='(' || ch=='}' && top=='{' || ch==']' && top=='[')){
                    s.pop();
                }
            else{
                return false;
            }    
               }
               else{
                   return false;
               }
           }
       }
       if(s.empty())
       return true;
       
       else
       return false;
    }

};

//{ Driver Code Starts.

int main()
{
   int t;
   string a;
   cin>>t;
   while(t--)
   {
       cin>>a;
       Solution obj;
       if(obj.ispar(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}
// } Driver Code Ends