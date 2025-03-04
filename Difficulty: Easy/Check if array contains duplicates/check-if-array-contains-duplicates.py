
class Solution:

    def checkDuplicates(self, arr):
        seen=set()
        for num in arr:
            if num in seen:
                return True
                
            seen.add(num)
        return False
       
        #code here



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        if (Solution().checkDuplicates(prices)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends