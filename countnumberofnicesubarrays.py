class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        odd_count = 0
        sub_array_count = 0
        temp = 0
        while right<len(nums):
            if nums[right]%2==1:
                odd_count+=1
                temp = 0
            while odd_count == k:
                temp+=1
                if nums[left]%2==1:
                    odd_count-=1
                left+=1
            sub_array_count += temp
            right+=1
        return sub_array_count
