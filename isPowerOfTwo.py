class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(int(n/2)+2):
            print "123"
            print i
            print n
            if i*i== n:
                print "456"
                return True
            elif i*i>n:
                print "789"
                return False    
            #else:
            #    continue

print Solution().isPowerOfTwo(1)