class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [] 
        for i in nums:
            if len(m) == 0:
                m.append(i)
            elif len(m) < 3:
                if i < m[0]:
                    m.insert(0, i)
                elif i > m[-1]:
                    m.append(i)
                elif i > m[0] and i < m[-1]:
                    m.insert(1, i)
            elif len(m) == 3:
                if i > m[0] and i < m[1]:
                    m[0] = i
                elif i > m[1] and i < m[2]:
                    m.insert(2, i)
                    m.pop(0)
                elif i > m[2]:
                    m.insert(3, i)
                    m.pop(0)
        if len(m) == 3:
            return m[0]
        else:
            return m[-1]
