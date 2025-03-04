from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        d=[]
        for i in range(N):
            d.append(abs((cur-pos[i])*time[i]))
            
        return min(d)
            
            
            
        
            
            
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        cur = int(input())
        
        
        pos=IntArray().Input(N)
        
        
        time=IntArray().Input(N)
        
        obj = Solution()
        res = obj.minimumTime(N, cur, pos, time)
        
        print(res)
        

        print("~")
# } Driver Code Ends