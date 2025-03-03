#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        maxi=arr1[0]
        for i in range(0,len(arr1)):
            if(arr1[i]>maxi):
                maxi=arr1[i]
        mini=arr2[0]
        for i in range(0,len(arr2)):
            if(arr2[i]<mini):
                mini=arr2[i]
        return maxi*mini
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.find_multiplication(arr1, arr2)
        print(ans)
        print("~")

# } Driver Code Ends