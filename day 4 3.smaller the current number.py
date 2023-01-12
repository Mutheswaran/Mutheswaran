def constructLowerArray(arr, countSmaller, n):

	for i in range(n):
		countSmaller[i] = 0

	for i in range(n):
		for j in range(i + 1, n):
			if (arr[j] < arr[i]):
				countSmaller[i] += 1

def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()

arr = [12, 1, 2, 3, 0, 11, 4]
n = len(arr)
low = [0]*n
constructLowerArray(arr, low, n)
printArray(low, n)

