#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3



class Solution:
    def arranged(self,arr):
        neg=[]
        pos=[]
        res=[]
        for i in range(len(arr)):
            if(arr[i]<0):
                neg.append(arr[i])
            else:
                pos.append(arr[i])
                
        for i in range(len(neg)):
            res.append(pos[i])
            res.append(neg[i])
            
        return res
            
        #Code here


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.arranged(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends