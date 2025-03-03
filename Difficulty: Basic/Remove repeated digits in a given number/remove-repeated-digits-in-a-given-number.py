#User function Template for python3

class Solution:
    def modify(self, N):
        p=str(N)
        d=""
        for i in range(len(p)-1):
            if(p[i]!=p[i+1]):
                d+=p[i]
                
        d+=p[len(p)-1]
                
        return d
                
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())

        solObj = Solution()

        print(solObj.modify(num))
# } Driver Code Ends