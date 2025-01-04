class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights = [h for _,h in envelopes]
        lis = []
        for h in heights:
            idx = bisect_left(lis,h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx]=h
        return len(lis)
        
