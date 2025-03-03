#User function Template for python3
class Solution:
	def isSame(self, s):
	    ans=""
	    c=0
	    for i in range(len(s)):
	        if s[i].isalpha():
	            ans+=s[i]
	        else:
	            c=int(s[i:])
	            break
	    if len(ans)==c:
	        return 1
	    else:
	        return 0
	    
	        
	        
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)


# } Driver Code Ends