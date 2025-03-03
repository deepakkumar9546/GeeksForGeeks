#User function Template for python3
class Solution:
	def removeVowels(self, s):
	    ans=""
	    for i in s:
	        if i not in "aeiouAEIOU":
	            ans+=i
	       
	    return ans
	        
		# code here
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeVowels(s)

        print(answer)

# } Driver Code Ends