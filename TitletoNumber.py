class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        value=0
        # this program does consider the situation that input includes not-alpahabets
        
        for i in s:
            value=value*26+ord(i)-64 #ord('A') is 65, so we minus 64 here
        return value