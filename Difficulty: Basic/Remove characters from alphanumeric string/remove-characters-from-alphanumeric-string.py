#User function Template for python3
class Solution:
	def removeCharacters(self, s):
	    d=""
	    for i in s:
	        if(i.isdigit()):
	            d+=i
	            
	    return d
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeCharacters(s)

        print(answer)

# } Driver Code Ends