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
    left = 0
    right = 0
    tmp = 0
    for cnt in range(0, len(nums), 2):
        nleft = cnt
        nright = min(cnt + add, len(nums))
        while nleft > left:
            tmp -= nums[left]
            left += 1
        while nright > right:
            tmp += nums[right]
            right += 1
        ans = max(tmp, ans)
    print(ans)


main()
