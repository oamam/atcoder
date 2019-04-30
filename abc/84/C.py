def main():
    N = int(input())
    csf = []
    for _ in range(N - 1):
        C, S, F = map(int, input().split())
        csf.append((C, S, F))
    
    ans = []
    for i in range(N - 1):
        c, s, _  = csf[i]
        t = c + s
        for ii in range(i + 1, N - 1):
            nc, ns, nf = csf[ii]
            if t > ns:
                ns += ((t - ns) // nf) * nf
                if (t - ns) % nf != 0:
                    ns += nf
            t += nc + ns - t
        ans.append(t)
    ans.append(0)
    
    for t in ans:
        print(t)
    

main()
