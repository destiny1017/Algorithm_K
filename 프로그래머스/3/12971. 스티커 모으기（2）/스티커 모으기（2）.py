def max_sticker(stickers):
    dp = [0] * len(stickers)
    dp[0] = stickers[0]
    dp[1] = max(stickers[0], stickers[1])

    for i in range(2, len(stickers)):
        dp[i] = max(dp[i-1], dp[i-2] + stickers[i])
    
    return dp[-1]

def solution(sticker):
    if len(sticker) == 1: return sticker[0]
    if len(sticker) == 2: return max(sticker[0], sticker[1])

    # 첫 번째 스티커 포함 마지막 스티커 제외
    case1 = max_sticker(sticker[:-1])

    # 첫 번째 스티커 제외 마지막 스티커 포함
    case2 = max_sticker(sticker[1:])

    return max(case1, case2)
