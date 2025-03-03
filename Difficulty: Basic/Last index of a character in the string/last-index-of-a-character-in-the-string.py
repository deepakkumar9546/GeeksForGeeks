#User function Template for python3

class Solution:
    def LastIndex(self, s, p):
        count=-1
        for i in range(len(s)):
            if(s[i]==p):
                count=i
        return count
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
        print("~")
# } Driver Code Ends