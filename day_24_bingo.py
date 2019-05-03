while True:
    """
    1到n之间的n个自然数,除0和1之外的其他值都没有成功写入内存
    """
    n = int(input())
    dp = 0
    for i in range(1, n+1):
        d = set(str(i))
        if d == {"0","1"} or d == {"0"} or d == {"1"}:
            dp += 1
    print(dp)

