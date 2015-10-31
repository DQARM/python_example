class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.pop(nums.index(0))
            nums.append(0)

a=[0,0,0,0,1,2,0,3,4,0,5,6,7,8,9,0]
print a
Solution().moveZeroes(a)
print a