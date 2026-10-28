class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
<<<<<<< HEAD

=======
        
>>>>>>> f392afc9619f052e7161716ff5a698e7bb78b3e3
for num in nums:
            if num not in frequency:
                frequency[num] = 1

            else:
                frequency[num] += 1

        sorted_freq = sorted(frequency, key=lambda num: frequency[num], reverse=True)
        
<<<<<<< HEAD
        return sorted_freq[:k]
=======
        return sorted_freq[:k]
>>>>>>> f392afc9619f052e7161716ff5a698e7bb78b3e3
