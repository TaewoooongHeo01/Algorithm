import sys

#stdin = open("input.txt")

n = int(sys.stdin.readline().rstrip())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if (i % 2 == 0) and (dp[i] > dp[i // 2]):
        dp[i] = dp[i//2] + 1
    if (i % 3 == 0) and (dp[i] > dp[i // 3]):
        dp[i] = dp[i//3] + 1

print(dp[n])

