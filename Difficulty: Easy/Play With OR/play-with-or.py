#User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) :
        list=[]
        for i in range(n-1):
            list.append(arr[i] | arr[i+1])
        list.append(arr[n-1])
        
        return list
        #Complete the function


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




    print("~")
# } Driver Code Ends