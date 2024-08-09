//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    void bitManipulation(int num, int i) {
        int ith_bit=(num>>(i-1))&1;
        int set_bit=num | (1<<(i-1));
        int clear_bit=num & (~(1<<i-1));
        
        cout<<ith_bit<<" "<<set_bit<<" "<<clear_bit;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n >> i;
        Solution ob;
        ob.bitManipulation(n, i);
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends