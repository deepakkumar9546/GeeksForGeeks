#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        cnt=0
        for i in s:
            if(i.isupper()):
                cnt+=1
            
        return cnt
        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends