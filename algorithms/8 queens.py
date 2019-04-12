'''
In 8 * 8 chess board, place 8 queens so that each of them can not attack each other.
Return how many posible soulutions are there in total?
'''

def eight_queens():
	row = 8
	col = 8
	used = [[0 for i in range(row)] for j in range(col)]

	def set_used(p, used, u):
		dirs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
		for d in dirs:
			tmp = p[:]
			while tmp[0] + d[0] >= 0 and tmp[0] + d[0] < 8 and tmp[1] + d[1] >= 0 and tmp[1] + d[1] < 8:
				tmp[0] += d[0]
				tmp[1] += d[1]
				used[tmp[0]][tmp[1]] += u

	count = [0]
	def find_solution(level):
		if level == row:
			count[0] += 1
			return

		for i in range(col):
			if not used[level][i]:
				set_used([level, i], used, 1)
				find_solution(level + 1)
				set_used([level, i], used, -1)

	find_solution(0)

	return count

print(eight_queens())

