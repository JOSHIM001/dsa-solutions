class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=None
        cand2=None
        count1=0
        count2=0
        res=[]
        for num in nums:
            if num==cand1:
                count1+=1
            elif num==cand2:
                count2+=1
            elif count1==0:
                cand1=num
                count1=1
            elif count2==0:
                cand2=num
                count2=1
            
            else:
                count1-=1
                count2-=1
        if nums.count(cand1)>len(nums)//3:
            res.append(cand1)
        if cand1!=cand2 and nums.count(cand2)>len(nums)//3:
            res.append(cand2)
        return res
