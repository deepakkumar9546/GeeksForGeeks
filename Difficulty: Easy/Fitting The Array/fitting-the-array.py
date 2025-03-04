#User function Template for python3

class Solution:
    def isFit (self,arr, brr, n) : 
        
        arr.sort()
        brr.sort()
        
        for i in range(len(arr)):
            if(arr[i]>brr[i]):
                return False
                
        return True
            
        #Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    a=Solution()
    ans = a.isFit(arr, brr, n)
    if(ans == True):
        print("YES")
    else:
        print("NO")
    print("~")
# } Driver Code Ends