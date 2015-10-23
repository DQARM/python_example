class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square(x):
            return int(x) * int(x)
    
        def happy(number):
            return sum(map(square, list(str(number))))

        if n == 1:
            return True
        elif n == 4:
            return False
        else:
            return self.isHappy(happy(n))		

print Solution().isHappy(123456789012345678901234567890)