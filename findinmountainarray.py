# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary_search(start, end, target, is_asc):
            while start <= end:
                mid = (start + end) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    return mid
                if is_asc: 
                    if mid_val < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else: 
                    if mid_val < target:
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1
        n = mountainArr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left
        index = binary_search(0, peak, target, True)
        if index != -1:
            return index
        return binary_search(peak + 1, n - 1, target, False)
        
