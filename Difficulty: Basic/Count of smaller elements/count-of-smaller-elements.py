#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        cnt=0
        for i in range(len(arr)):
            if(arr[i]<=x):
                cnt+=1
        return cnt
            
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        x = int(data[index])
        index += 1
        arr = list(map(int, data[index].split()))
        index += 1
        obj = Solution()
        ans = obj.countOfElements(x, arr)
        print(ans)
        print("~")
# } Driver Code Ends