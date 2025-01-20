class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        n = len(arr)
        result = []
        current_max = max(arr[:k])  
        result.append(current_max)
        for i in range(1, n - k + 1):
            if arr[i - 1] == current_max:
                current_max = max(arr[i:i + k])
            else:
                current_max = max(current_max, arr[i + k - 1])
        
            result.append(current_max)
    
        return result
