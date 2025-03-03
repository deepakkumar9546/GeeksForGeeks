#User function Template for python3

class Solution:
    def removeSpecialCharacter (self, S):
        d=""
        for i in S:
            if(i.isalpha()):
                d+=i
            
        return d if d else "-1"
        
    
            
		#code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.removeSpecialCharacter(S))


# } Driver Code Ends