class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        left=0
        right=len(height)-1
        while left<right:
            maxi=max(maxi,(right-left)*min(height[right],height[left]))
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return maxi