'''
chose k numbers from an array of numbers, print all the combinations
eg: nums = [1, 2, 3, 4], k = 3
[1, 2, 3]
[1, 2, 4]
[1, 3, 4]
[2, 3, 4]
'''

def combination(nums, k):
	used = [False] * len(nums)
	chose = [0] * k

	def c_helper(level, start):
		if level == k:
			print(chose)
			return 

		for i in range(start, len(nums)):
			if not used[i]:
				chose[level] = nums[i]
				used[i] = True
				c_helper(level + 1, i + 1)
				used[i] = False

	c_helper(0, 0)

nums = [1, 2, 3, 4]
combination(nums, 3)
