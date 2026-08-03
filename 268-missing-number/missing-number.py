class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        n_sum=(n*(n+1))//2
        s=0
        for num in nums:
            s+=num
        return n_sum-s
