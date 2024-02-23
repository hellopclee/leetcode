class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            res = target-nums[i]
            j=i+1
            while j< size:
                if nums[j] == res:
                    return [i,j]
                j=j+1
