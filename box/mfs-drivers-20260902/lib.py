from math import ceil

def n_from_delta(D):
    """smallest n with (n-1)(n-2)/2 >= D"""
    n = 1
    while (n-1)*(n-2)//2 < D:
        n += 1
    return n

def dicritical_sets(W):
    """multisets of (s,mu), mu>=2, s>=1, sum s*mu = W  (7.B' : every mu_l>=2)"""
    res = set()
    def rec(rem, cur):
        if rem == 0:
            res.add(tuple(sorted(cur)))
            return
        for mu in range(2, rem+1):
            for s in range(1, rem//mu + 1):
                rec(rem - s*mu, cur+[(s,mu)])
    rec(W, [])
    return sorted(res)

def partitions_into(n, m, maxpart):
    """partitions of n into exactly m positive parts each <= maxpart, non-increasing"""
    if m == 0:
        if n == 0: yield ()
        return
    lo = max(1, -(-n//m) if False else 1)
    for p in range(min(n - (m-1), maxpart), 0, -1):
        for rest in partitions_into(n-p, m-1, p):
            yield (p,)+rest
