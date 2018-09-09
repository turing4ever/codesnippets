class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        non_score = ['+', 'D', 'C']
        scores = []
        for op in ops:
            if op not in non_score:
                scores.append(int(op))
            elif op == '+' and len(scores)>=2:
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(2*scores[-1])
            elif op == 'C':
                scores.pop()
        return sum(scores)
