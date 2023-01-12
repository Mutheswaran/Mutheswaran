


def shouldSwap(string, start, curr):

	for i in range(start, curr):
		if string[i] == string[curr]:
			return 0
	return 1


def findPermutations(string, index, n):

	if index >= n:
		print(''.join(string))
		return

	for i in range(index, n):

		
		check = shouldSwap(string, index, i)
		if check:
			string[index], string[i] = string[i], string[index]
			findPermutations(string, index + 1, n)
			string[index], string[i] = string[i], string[index]

if __name__ == "__main__":

	string = list("ABCA")
	n = len(string)
	findPermutations(string, 0, n)
	
