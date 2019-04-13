'''
Given an array of integers, a target number, if there is a way
to get the target number using the integers in the array(each interger once),
return the solution, if not, return -1. If multiple solutions exist, return
any of them.

The integers in the array are between [0, 100]
The length of the array is between [0, 100]
The target number is between [0, 10000]
'''

def find_sum(arr, target):
	dp = [None] * 10001
	dp[0] = 0

	for num in arr:
		for i in range(10000, -1, -1):
			print(i)
			if dp[i] is not None and dp[i + num] is None:
				dp[i + num] = num # save num to print solution

	if dp[target] is None:
		return -1

	trace = target
	solution = []
	while trace != 0:
		solution.append(dp[trace])
		trace -= dp[trace]

	return solution

nums = [
		79, 37, 79, 16, 72, 45, 24, 64, 89, 38, 75, 19, 6, 69, 26, 26, 5, 88, 53, 9,
		58, 28, 36, 57, 37, 52, 72, 77, 19, 36, 32, 83, 61, 15, 90, 34, 75, 81, 68, 67,
		81, 47, 65, 43, 17, 52, 17, 55, 2, 77, 40, 53, 98, 82, 42, 35, 9, 79, 22, 20, 50,
		85, 66, 48, 70, 100, 98, 34, 21, 41, 42, 94, 13, 81, 32, 82, 68, 69, 85, 64, 89, 
		4, 82, 36, 68, 100, 11, 16, 51, 68, 19, 55, 85, 58, 7, 38, 63, 11, 37, 61, 69, 
]
tar = 1113

result = find_sum(nums, tar)
print(result) # [37, 57, 36, 28, 58, 9, 53, 88, 5, 26, 26, 69, 19, 75, 38, 89, 64, 24, 45, 72, 79, 37, 79]
print(sum(result)) # 1113

