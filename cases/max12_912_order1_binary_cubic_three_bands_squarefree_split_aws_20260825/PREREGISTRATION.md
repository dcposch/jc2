# Preregistration — squarefree split-basis overlap shard

Status: frozen before CAS execution.  AWS-only.

Consume the exact emitted squarefree three-band input at SHA-256
`80261b2d528a6c1e85631795be11ff99bbb54c5313a6b5980077c9cdf48aea11`.
It contains seven degree-17 obstruction generators followed by eight degree-16
generators in the same `Q[s1..s9,t1..t8]` ring as the monolithic runs.

Compute

```text
G17 = std(I17),
R16 = reduce(I16,G17),
G   = slimgb(G17+R16).
```

This does not change the ideal: `<G17>=<I17>` and every generator of `R16`
differs from the corresponding generator of `I16` by an element of `<G17>`.
Verify every original generator reduces to zero modulo `G`.  Compare exact
dimension and, if the monolithic lanes finish, reduced-basis bytes.

This is an algorithmic overlap control, not an independent mathematical
implementation or a new theorem.  The runner must refuse non-AWS, non-Linux,
wrong-host, and wrong-tag execution before invoking Python or Singular.

