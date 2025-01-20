class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start:int,combination:List[int],total:int):
            if len(combination)==k and total == n:
                result.append(combination[:])
            for i in range(start,9):
                if total + (i+1) > n:
                    continue
                combination.append(i+1)
                backtrack(i+1,combination,total+(i+1))
                combination.pop()
        result = []
        backtrack(0,[],0)
        return result
            
        
