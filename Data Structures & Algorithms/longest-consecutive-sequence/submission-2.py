class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = {}
        maxi = 1
        if len(nums) == 0:
            return 0

        for i in nums:
            hs[i] = 1
        for i in hs:
            count = 1
            if i-1 not in hs:
                while i+1 in hs:
                    count += 1
                    maxi = max(count, maxi)
                    i += 1
            else:
                continue
        return maxi


