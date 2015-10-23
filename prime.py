class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        primes=range(2,n)
        for i in primes:
            #print " i_0= "+str(i)
            if not i: 
                #print " i= "+str(i)
                continue
            for j in xrange(i*i,n,i):
                primes[j-2]=0
                #print primes
        return len(primes)-primes.count(0)     
		
a=Solution().countPrimes(46349)	
print a