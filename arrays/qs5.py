class Solution:
	def fib(self, n: int) -> int:
		# Defined INSIDE fib, so it doesn't need 'self'
		def func(num):
			if num == 0 or num == 1:
				return num
			return func(num - 1) + func(num - 2)
		
		return func(n)