class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s_ = {}

        for num in nums:
            if num not in s_:
                s_[num] = 1

            else:
                return True
            
        return False