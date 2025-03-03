#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        p=""
        for i in s:
            if i in 'aeiouAEIOU':
                p+=i
            
        if len(p)==0:
            return "No Vowel"
            
        return p
            
        
        
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))
        print("~")
# } Driver Code Ends