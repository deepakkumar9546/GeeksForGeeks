#User function Template for python3

class Solution:
    def count (self,s):
        u=0
        l=0
        n=0
        p=0
        
        for i in s:
            if(i.isupper()):
                u+=1
            elif(i.islower()):
                l+=1
            elif(i.isdigit()):
                n+=1
            else:
                p+=1
            
        return [u,l,n,p]
        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends