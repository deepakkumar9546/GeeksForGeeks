#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

#User function Template for python3
def distinct(arr):
    d=set()
    for i in arr:
        if i not in d:
            d.add(i)
            
    return len(d)
    # Your Code here
    


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        print(distinct(arr))
        print("~")
# } Driver Code Ends