#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def num(self, k, arr):
        d=0
        for i in arr:
            for digit in str(i):
                if digit==str(k):
                    d+=1
                    
        return d
            
            
            
        
       
        # code here


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.num(k,arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends