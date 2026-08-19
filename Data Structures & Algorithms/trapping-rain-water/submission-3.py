class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        maxl , maxr = height[0] , height[-1]
        if len(height)<=1:
            return 0
        ans = 0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl = max(maxl,height[l])
                ans += maxl - height[l]
            else:
                r-=1
                maxr = max(maxr,height[r])
                ans += maxr - height[r]
        return ans 
        # leftmax , rightmax = [0]*len(height) , [0]*len(height)
        # if len(height)<=0:
        #     return 0
        # if len(height)==1:
        #     return 0
        # leftmax[0]=height[0]
        # rightmax[-1]=height[-1]
        # for i in range(1,len(height)):
        #     leftmax[i]=max(leftmax[i-1],height[i-1])
        # for i in range(len(height)-2,-1,-1):
        #     rightmax[i]=max(rightmax[i+1],height[i+1])
        # # print(leftmax,rightmax)
        # trap = [0]*len(height)
        # for i in range(len(trap)):
        #     trap[i]=max(min(leftmax[i],rightmax[i]) - height[i] , 0 )
        # # ans = 0 
        # # print(trap)
        # return sum(trap)