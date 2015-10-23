class Solution(object):
    
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num<=0:
            return False
        while(num%2==0):
            num=num/2
            print "here1"
        while(num%3==0):
            num=num/3
            print "here2"
        while (num%5==0):
            num=num/5
            print "here3"
       
        if num==1:
            return True
        else:
            return False
			

a=Solution().isUgly(1800)
print a