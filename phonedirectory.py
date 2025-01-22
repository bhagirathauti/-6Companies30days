class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact=sorted(set(contact))
        res = []
        for i in range(0,len(s)):
            prefix = s[:i+1]
            matches = [c for c in contact if c.startswith(prefix)]
            if not matches:
                res.append(["0"])
            else:
                res.append(matches)
        return res
