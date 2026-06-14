#solved by ma

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lef=0
        righ=len(nums)-1
        while lef<=righ:
            mid=(lef+righ)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                lef=mid+1
            else:
                righ= mid-1
        return lef





        link for question 🙋 

        
