#User function Template for python3

class Solution:
    def removeDuplicate(self, arr):
        a=[]
        s=set()
        for i in arr:
            if i not in s:
                s.add(i)
                a.append(i)
                
        return a
        
        
        # code here
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicate(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends