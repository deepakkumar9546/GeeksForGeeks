#User function Template for python3
class Solution:
	def penaltyScore(self, S):
	    cnt=0
	    for i in range(len(S)-1):
	        if S[i]=='2':
	            if (S[i+1]=='1'):
	                cnt+=1
	                
	    return cnt
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.penaltyScore(S)
		
		print(answer)


# } Driver Code Ends