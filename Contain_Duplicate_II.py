import time
class Solution(object):
 
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            print "here"
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
a=[1,2,3,4,5,4,3,2,1,3,4,4,5]
print Solution().containsNearbyDuplicate(a,1)
