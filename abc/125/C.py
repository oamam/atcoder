def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    L = [A[0]]
    R = [A[-1]]
    for i in range(1, N - 1):
        L.append(gcd(L[-1], A[i]))
    for j in range(N - 2, 0, -1):
        R.append(gcd(R[-1], A[j]))
    ans = R[-1]
    for k in range(1, N - 1):
        ans = max(ans, gcd(L[k - 1], R[N - 2 - k]))
    print(max(ans, L[-1]))
    
main()
