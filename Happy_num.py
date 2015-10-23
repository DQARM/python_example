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


        self.number=n
        seen_numbers = set()
        while self.number > 1 and (self.number not in seen_numbers):
            seen_numbers.add(self.number)
            self.number = happy(self.number)
        return self.number == 1
		

print Solution().isHappy(123456789012345678901234567890)