class Solution(object):
    def sortedSquares(self, nums):
        p = len(nums)
        positive = []
        negative = []
        final = []

        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        n = len(positive)
        m = len(negative)
        i = j = 0

        positive = [x*x for x in positive]
        negative = [x*x for x in negative][::-1]

        while i < m and j < n:
            if negative[i] < positive[j]:
                final.append(negative[i])
                i += 1

            else:
                final.append(positive[j])
                j += 1

        while i < m:
            final.append(negative[i])
            i += 1

        while j < n:
            final.append(positive[j])
            j += 1

        return final
