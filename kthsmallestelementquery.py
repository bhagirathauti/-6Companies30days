class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans, trimmed = [], {}
        for k, trimi in queries:
            if trimi not in trimmed:
                trimmed[trimi] = sorted([(num[-trimi:], i) for i, num in enumerate(nums)])
            ans.append(trimmed[trimi][k-1][1])
        return ans

