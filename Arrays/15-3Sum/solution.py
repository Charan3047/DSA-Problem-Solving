class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []

        a = sorted(nums)
        for i in range(n-2):
            if i > 0 and a[i] == a[i-1]:
                continue

            if a[i] > 0:
                break
            left = i + 1
            right = n - 1
            sum = -1 * a[i]

            while left < right:
                s = a[left] + a[right]
                if s == sum:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < n and a[left] == a[left - 1]:
                        left += 1

                    while right > 0 and a[right] == a[right + 1]:
                        right -= 1

                elif s < sum:
                    left += 1

                else:
                    right -= 1

        return res

                