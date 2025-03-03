#User function Template for python3

class Solution:
    def convert(self, s):
        # code here
        return s.title()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.convert(s))
# } Driver Code Ends