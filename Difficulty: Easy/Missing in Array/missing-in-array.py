#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        n=len(arr)+1
        totalsum=(n*(n+1))/2
        sum=0
        for i in arr:
            sum+=i
            
        return int(totalsum-sum)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends