#User function Template for python3

class Solution:

    def findLength(self, s):
        s = s.rstrip()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                cnt += 1
            else:
                break

        return cnt
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        s = input()

        solObj = Solution()

        ans = solObj.findLength(s)

        print(ans)
# } Driver Code Ends