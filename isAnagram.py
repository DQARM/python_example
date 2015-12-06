class Solution(object):
    def isAnagram(self, s, t): # 44ms
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t) and set(s)==set(t):
            for i in set(s):
                if s.count(i)!=t.count(i):
                    return False
        else:
            return False

        return True
        
    def isAnagram2(self, s, t): # 108ms, from copy from forum        
        from collections import Counter
        return Counter(s) == Counter(t)


print Solution().isAnagram("a","b")