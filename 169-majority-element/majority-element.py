class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candt=0
        for num in nums:
            if count==0:
                candt=num
                count=1
            elif candt==num:
                count+=1
            else:
                count-=1
        return candt