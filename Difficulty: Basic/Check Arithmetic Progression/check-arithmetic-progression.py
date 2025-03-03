class Solution:
    def checkIsAP(self, arr):
        #Your code goes here
        
        arr.sort()
        if(len(arr)<2):
            return True
        
        for i in range(len(arr)-1):
            if((arr[1]-arr[0]) != (arr[i+1]-arr[i])):
                return False
            
        return True
      



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.checkIsAP(arr)
        if ans:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends