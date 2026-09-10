class Solution(object):
    def removeDuplicates(self, nums):

        n = len(nums)

        unique_index = 0
        current_index = 1
        unique_count = 1

        while current_index < n:
            if nums[current_index] == nums[current_index - 1]:
                current_index += 1
                continue

            nums[unique_index + 1] = nums[current_index]
            unique_index += 1
            unique_count += 1
            current_index += 1

        return unique_count