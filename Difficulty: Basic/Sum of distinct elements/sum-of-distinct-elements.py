#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
	
	def findSum(self,arr):
	    sum=0
	    s=set(arr)
	    for i in s:
	        sum+=i
	        
	    return sum
	        
		# code here


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findSum(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends