class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = list(range(1,n+1))
        curr = 0
        while n>1:
            curr = (curr+(k-1))%n
            friends.pop(curr)
            n-=1
        return friends[0]


        
