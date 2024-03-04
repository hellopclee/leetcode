class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        for i in range(0, size-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, size-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left = j+1
                right = size-1
                while left<right:
                    if left>j+1 and nums[left]==nums[left-1]:
                        left=left+1
                        continue
                    diff = nums[i]+nums[j]+nums[left]+nums[right]-target
                    if diff>0:
                        right=right-1
                    elif diff<0:
                        left = left+1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        print(i,j,left, right)
                        left = left+1
        return res

        
