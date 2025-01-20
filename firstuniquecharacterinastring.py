class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        idx = -1
        for i in freq.keys():
            if freq[i] == 1:
                idx = s.index(i)
                break
        if idx != -1:
            return idx
        else:
            return -1
