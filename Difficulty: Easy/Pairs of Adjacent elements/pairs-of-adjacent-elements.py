#User function Template for python3

class Solution:
    def adjacentPairs(self,arr):
        cnt=0
        for i in range(1,len(arr)):
            if((arr[i-1]<arr[i]) and (arr[i]-arr[i-1])==1):
                cnt+=1
                
        return cnt
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.adjacentPairs(arr))
        print("~")

# } Driver Code Ends