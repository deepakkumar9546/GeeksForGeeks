
class Solution:
    def maxDays(self, arr):
        # code here
        arr.sort()
        return arr[len(arr)-1]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())

    for i in range(1, t + 1):
        arr = list(map(int, data[i].strip().split()))
        ob = Solution()
        print(ob.maxDays(arr))
        print("~")

# } Driver Code Ends