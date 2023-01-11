from collections import defaultdict


def printAnagramsTogether(words):
	groupedWords = defaultdict(list)

	for word in words:
		groupedWords["".join(sorted(word))].append(word)

	for group in groupedWords.values():
		print(" ".join(group))


if __name__ == "__main__":
	arr = ["cat", "dog", "tac", "god", "act"]
	printAnagramsTogether(arr)
