class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        res = []

        for num in nums:
            if num not in s_:
                frequency[num] = 1

            else:
                frequency[num] += 1

        sorted_freq = sorted(frequency, key=lambda num: frequency[num], reverse=True)
        
        return res[:k]
