# Python program to implement wildcard
# pattern matching algorithm
def finding(s, p, n, m):
	# return 1 if n and m are negative
	if n < 0 and m < 0:
		return 1

	# return 0 if m is negative
	if m < 0:
		return 0

	# return n if n is negative
	if n < 0:
		# while m is positive
		while m >= 0:
			if p[m] != '*':
				return 0
			m -= 1
		return 1

	# if dp state is not visited
	if dp[n][m] == -1:
		if p[m] == '*':
			dp[n][m] = finding(s, p, n - 1, m) or finding(s, p, n, m - 1)
			return dp[n][m]
		else:
			if p[m] != s[n] and p[m] != '?':
				dp[n][m] = 0
				return dp[n][m]
			else:
				dp[n][m] = finding(s, p, n - 1, m - 1)
				return dp[n][m]

	# return dp[n][m] if dp state is previsited
	return dp[n][m]

def isMatch(s, p):
	global dp
	dp = []

	# resize the dp array
	for i in range(len(s) + 1):
		dp.append([-1] * (len(p) + 1))
	dp[len(s)][len(p)] = finding(s, p, len(s) - 1, len(p) - 1)
	return dp[len(s)][len(p)]

# Driver code


def main():
	s = "baaabab"
	p = "*****ba*****ab"
	# p = "ba*****ab"
	# p = "ba*ab"
	# p = "a*ab"
	# p = "a*****ab"
	# p = "*a*****ab"
	# p = "ba*ab****"
	# p = "****"
	# p = "*"
	# p = "aa?ab"
	# p = "b*b"
	# p = "a*a"
	# p = "baaabab"
	# p = "?baaabab"
	# p = "*baaaba*"

	if isMatch(s, p):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

# This code is contributed by divyansh2212
