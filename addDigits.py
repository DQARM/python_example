class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.num=num
        while (num >9):
            num=num/10+num%10
        return num 

A = Solution()
print A.addDigits(12345)
		