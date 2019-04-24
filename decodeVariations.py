def decodeVariations(S):
    """
    @param S: str
    @return: int
    """


'GHYF' --> '78256'
    N = len(S)
    dp = []
dp[N] = 1
for i from N-1 to 0:
    if S[i] == '0':
        dp[i] = 0
    else if S[i] == '1':
        dp[i] = dp[i + 1] + dp[i + 2]
    else if S[i] == '2':
        dp[i] = dp[i + 1]
        if i + 1 < S.length & & S[i + 1] <= '6':
            dp[i] += dp[i + 2]
        else:
            dp[i] = dp[i + 1]
return dp[0]

print(decodeVariations("78256"))