class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            print(di.get(target - nums[i]))
            if (target - nums[i]) in di:
                return [di.get(target - nums[i]), i]
            di[nums[i]] = i
        return [0,0]