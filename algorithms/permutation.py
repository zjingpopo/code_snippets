'''
chose k numbers from an array of numbers, print all permutations
eg: nums = [1, 2, 3, 4], k = 3
[1, 2, 3]
[1, 2, 4]
[1, 3, 2]
[1, 3, 4]
[1, 4, 2]
[1, 4, 3]
[2, 1, 3]
[2, 1, 4]
[2, 3, 1]
[2, 3, 4]
[2, 4, 1]
[2, 4, 3]
[3, 1, 2]
[3, 1, 4]
[3, 2, 1]
[3, 2, 4]
[3, 4, 1]
[3, 4, 2]
[4, 1, 2]
[4, 1, 3]
[4, 2, 1]
[4, 2, 3]
[4, 3, 1]
[4, 3, 2]
'''

def permutation(nums, k):
	used = [False] * len(nums)
	chose = [0] * k

	def p_helper(level):
		if level == k:
			print(chose)
			return
		for i in range(len(nums)):
			if not used[i]:
				chose[level] = nums[i]
				used[i] = True
				p_helper(level + 1)
				used[i] = False

	p_helper(0)


nums = [1, 2, 3, 4]
permutation(nums, 3)