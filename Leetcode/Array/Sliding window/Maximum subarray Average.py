#Solved by ma

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr_s=sum(nums[:k])
        max_s=sum(nums[:k])
        l,r=0,k
        while r<n:
            curr_s=curr_s-nums[l]+nums[r]
            max_s=max(max_s,curr_s)
            r+=1
            l+=1
        return max_s/k
