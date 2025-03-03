#User function Template for python3

class Solution:
    def countWords(self,s):
        #code here
        cnt=0
        for i in s:
            if(i==" "):
                cnt+=1
                
        return cnt+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        s=input()
        obj = Solution()
        print(obj.countWords(s))
        print("~")
# } Driver Code Ends