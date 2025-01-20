class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        Dict = defaultdict(list)
        for e,t in access_times:
            Dict[e].append(int(t))
        res = []
        for e,t in Dict.items():
            t.sort()
            n = len(t)
            for i in range(n-2):
                if t[i+2] - t[i] <100:
                    res.append(e)
                    break
        return res
        
