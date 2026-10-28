class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s_ = {}
        c = 0
        res = []

        for num in nums:
            if num not in s_:
                s_[num] = 1

            else:
                s_[num] += 1

        s_ = sorted(s_, key=lambda num: s_[num], reverse=True)
        for num in s_:
            if len(res) != k:
                res.append(num)

        return res