class Solution(object):
    def threeSumClosest(self, nums, target):

        n = len(nums)

        s = 0
        max_diff = float('-inf')
        max_sum = 0

        nums = sorted(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                diff = abs(sum - target)
                if(max_diff > diff):
                    max_diff = diff
                    max_sum = sum

                if s < target:
                    j += 1

                else:
                    k -= 1

        return max_sum