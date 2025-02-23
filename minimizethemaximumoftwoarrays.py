class Solution: 
	def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int: 
		lo, hi = 0, 1<<32-1
		mult = lcm(divisor1, divisor2)
		while lo < hi: 
			mid = lo + hi >> 1
			if uniqueCnt1 <= mid - mid//divisor1 and uniqueCnt2 <= mid - mid//divisor2 and uniqueCnt1+uniqueCnt2 <= mid - mid//mult: hi = mid
			else: lo = mid+1
		return lo 
