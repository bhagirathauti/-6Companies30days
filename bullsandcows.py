class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls,cows = 0,0
        myHashmap = Counter(secret)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                myHashmap[secret[i]]-=1
        for i in range(len(guess)):
            if guess[i] in myHashmap and secret[i]!=guess[i] and myHashmap[guess[i]]>0:
                cows+=1
                myHashmap[guess[i]]-=1
        return "{}A{}B".format(bulls,cows)
