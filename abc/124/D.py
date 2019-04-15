def main():
    N, K = map(int, input().split())
    S = input()
    nums = []
    now = 1
    cnt = 0
    for s in S:
        if int(s) == now:
            cnt += 1
        else:
            nums.append(cnt)
            now ^= 1
            cnt = 1
    if cnt > 0:
        nums.append(cnt)
    if len(nums) % 2 == 0:
        nums.append(0)
    add = 2 * K + 1
    ans = 0
    for cnt in range(0, len(nums), 2):
        tmp = 0
        left = cnt
        right = min(cnt + add, len(nums))
        for j in range(left, right):
            tmp += nums[j]
        ans = max(tmp, ans)
    print(ans)


main()
