def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed to make each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # Initialize dp[0] as 0 since we need 0 coins to make a total of 0
    dp[0] = 0

    # Iterate through each coin and update dp values
    for coin in coins:
        for value in range(coin, total + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    # If dp[total] remains unchanged, it means we cannot make the total with the given coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]

