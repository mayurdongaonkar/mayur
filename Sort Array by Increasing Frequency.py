from collections import Counter
class Solution:
	def frequencySort(self, nums: list):
		d = Counter(nums)
		def check(x):
			return d[x]

		nums.sort(reverse=True)
		nums.sort(key=check)
		return nums

nums = [1,1,2,2,2,3]
S = Solution()
print(S.frequencySort(nums))

d = Counter(nums)
print(d[2])