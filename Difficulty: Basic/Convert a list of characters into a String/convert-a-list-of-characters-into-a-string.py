#User function Template for python3

class Solution:
    def chartostr(self, arr,N):
        p=""
        for i in arr:
            p+=i
        return p
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N= int(input())
        arr =input().split()
        ob = Solution()
        print(ob.chartostr(arr,N))
        print("~")
# } Driver Code Ends