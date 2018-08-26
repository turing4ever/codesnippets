class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        def avail(flowerbed, i):
            if flowerbed[i] == 1:
                return False
            else:
                if i-1>=0 and flowerbed[i-1]==1:
                    return False
                if i+1<=len(flowerbed)-1 and flowerbed[i+1]==1:
                    return False
                flowerbed[i] = 1
                return True
        for i in range(len(flowerbed)):
            if n > 0 and avail(flowerbed, i):
                n -= 1
        if n:
            return False
        else:
            return True

