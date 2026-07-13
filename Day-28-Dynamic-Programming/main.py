# -----------------------------
# Day 28 - Dynamic Programming
# -----------------------------

# Fibonacci using Memoization

memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


# Fibonacci using Tabulation

def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Climbing Stairs

def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Longest Common Subsequence

def lcs(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# -----------------------------
# Main Program
# -----------------------------

print("=== Dynamic Programming Demo ===\n")

print("Fibonacci (Memoization) of 10:", fib_memo(10))

print("Fibonacci (Tabulation) of 10:", fib_tab(10))

print()

print("Ways to climb 5 stairs:", climb_stairs(5))

print()

print("LCS Length:", lcs("ABCDEF", "AEDF"))
