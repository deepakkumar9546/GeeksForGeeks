#User function Template for python3

class Solution:
    def multiply(self, arr):
        sum1=0
        sum2=0
        for i in range(len(arr)//2):
            sum1+=arr[i]
            
        for i in range(len(arr)//2,len(arr)):
            sum2+=arr[i]
            
        return sum1*sum2
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.multiply(arr))
        print("~")

# } Driver Code Ends