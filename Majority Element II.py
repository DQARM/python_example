#https://leetcode.com/problems/majority-element-ii/
class Solution(object):
    def majorityElement(self, nums):     # 80, 60, 64, 64, 60ms
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        reviewed=set()
        if len(nums)<=3:
            return list(set(nums))

        for i in xrange((len(nums))/3*2):
            print "len_"+str((len(nums)+1)/2)
            print "here_"+str(i)
            if nums[i] not in reviewed:
                print "here2_"+str(i)
                if nums.count(nums[i]) > len(nums)/3:
                    reviewed.add(nums[i])
        return list(reviewed)

print Solution().majorityElement([1,2,3])