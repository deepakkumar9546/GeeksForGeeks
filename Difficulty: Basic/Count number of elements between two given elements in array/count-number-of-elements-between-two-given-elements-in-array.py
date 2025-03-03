class Solution:
    def getCount(self, arr, num1, num2):
        #Your code goes here
        s1=arr.index(num1)
        s2=len(arr)-1-arr[::-1].index(num2)
        c=0
        
        if s1>=s2 :
            return 0
        return s2-s1-1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        num1, num2 = map(int, input().strip().split())
        ob = Solution()
        print(ob.getCount(arr, num1, num2))
        print("~")
# } Driver Code Ends