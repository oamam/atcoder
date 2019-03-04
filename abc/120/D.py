class UF():
    def __init__(self, N: int):
        self.parent = [-1 for _ in range(N)]

    def root(self, A: int) -> int:
        if self.parent[A] < 0:
            return A
        self.parent[A] = self.root(self.parent[A])
        return self.parent[A]

    def size(self, A: int) -> int:
        return -self.parent[self.root(A)]

    def connect(self, A: int, B: int) -> bool:
        A = self.root(A)
        B = self.root(B)
        if A == B:
            return False
        if self.size(A) < self.size(B):
            A, B = B, A
        self.parent[A] += self.parent[B]
        self.parent[B] = A
        return True


def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a - 1)
        B.append(b - 1)
    ans = [0 for _ in range(M)]
    ans[M - 1] = (N * (N - 1)) // 2
    uf = UF(N)
    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if uf.root(A[i]) != uf.root(B[i]):
            ans[i - 1] -= uf.size(A[i]) * uf.size(B[i])
            uf.connect(A[i], B[i])

    for a in ans:
        print(a)


main()
