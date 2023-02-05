def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    cc = 0
    for coin in coins:
        if coin > cc+1:
            return cc + 1
        cc += coin
    return cc +1
