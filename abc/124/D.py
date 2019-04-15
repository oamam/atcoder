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
    sum = [0 for _ in range(len(nums) + 1)]
    for i in range(len(nums)):
        sum[i + 1] = sum[i] + nums[i]
    ans = 0
    for cnt in range(0, len(nums), 2):
        left = cnt
        right = min(cnt + add, len(nums))
        tmp = sum[right] - sum[left]
        ans = max(tmp, ans)
    print(ans)


main()
