class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        if len(nums1)>len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        
        size1 = len(nums1)
        size2 = len(nums2)

        left_total = int((size1+size2+1)/2)#不加1会陷入死循环
        left = 0
        right = size1

        while left<right:
            i = int(left+(right-left+1)/2)
            j = left_total-i
            print("i={}, left={}, right={}, j={}, left_total={}".format(i, left, right, j, left_total))
            print(nums1)
            if nums1[i-1]<nums2[j]:
                #[i, right]
                left = i
            else:
                #[left, i-1]
                right = i-1
        i = left
        j = left_total - i
        #print("i={},j={}".format(i, j))
        nums1_left_max = float('-inf') if i==0 else nums1[i-1]
        nums1_right_min = float('inf') if i == size1 else nums1[i]
        nums2_left_max = float('-inf') if j==0 else nums2[j-1]
        nums_right_min = float('inf') if j == size2 else nums2[j]

        if (size1+size2)%2==0 :
            return (max(nums1_left_max, nums2_left_max)+ min(nums1_right_min, nums_right_min))/2
        else:
            return float(max(nums1_left_max, nums2_left_max))
