class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequence = set()
        repeated= set()
        for i in range(0,len(s)-9):
            curr_seq = s[i:i+10]
            if curr_seq in sequence:
                repeated.add(curr_seq)
            sequence.add(curr_seq)
        return list(repeated)
        
