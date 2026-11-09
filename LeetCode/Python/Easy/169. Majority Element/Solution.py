class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #boyer moores algo
        cand=None
        count=0
        for num in nums:
            if count ==0:
                count+=1
                cand=num
            elif num==cand:
                count+=1
            else:
                count-=1
        return cand