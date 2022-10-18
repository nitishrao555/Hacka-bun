# Function to print all sublists of the specified list
def printallSublists(nums):
	# consider all sublists starting from i
	for i in range(len(nums)):
		# consider all sublists ending at `j`
		for j in range(i, len(nums)):
			# Function to print a sublist formed by [i, j]
			print(nums[i: j + 1])

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	printallSublists(nums)
