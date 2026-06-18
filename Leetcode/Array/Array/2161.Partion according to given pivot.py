#Solved by Musa A bdusamed

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n=len(nums)
        great=[]
        less=[]
        equal=[]
        for i in range(n):
            if nums[i]>pivot:
                great.append(nums[i])
            elif nums[i]<pivot:
                less.append(nums[i])
            else:
                equal.append(nums[i])
        return less +equal+great
