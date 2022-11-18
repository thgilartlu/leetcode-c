class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1
      
# RUNTIME
# Runtime: 62 ms
# Performance: 46.27%

# MEMORY
# Memory: 13.9 MB
# Performance: 60.8%
