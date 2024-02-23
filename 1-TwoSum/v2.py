class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums = nums.copy()
        sort_nums.sort()
        first_i = 0
        end_i = len(nums)-1
        while True:
            sum = sort_nums[first_i]+sort_nums[end_i]
            if sum > target:
                end_i = end_i-1
            elif sum < target:
                first_i=first_i+1
            else:
                break
        res=[]
        i = 0
        while len(res)<2:
            if nums[i]==sort_nums[first_i] or nums[i]==sort_nums[end_i]:
                res.append(i)
            i=i+1
        
        return res
