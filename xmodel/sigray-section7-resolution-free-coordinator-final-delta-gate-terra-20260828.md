# Final delta gate: Section 7 resolution-free repair

Date: 2026-08-28  
Reviewed coordinator hash: `cbc7d6d2724599492712bcaaaa40f305f59697d6fc209cb3c072c62787a240d7`  
Verdict: **FAIL.**

The quotient-coordinate failures are repaired, but the new direct
Q/jump/max argument does not transport `kappa_F` across fibres. A strict
prefix and a scalar cover identification preserve the zero/nonzero status of
one *given* coefficient; they do not give a bijection between the roots of
`P(z)-a_0` and those of `P(z)-a`. Those root sets are precisely the
realizations whose zero/nonzero status the argument uses.

| delta clause | verdict | check |
|---|---|---|
| `tau_(F,a)` is well-defined and formula domains are typed | **PASS** | With a fixed reference presentation, two target presentations aligned to it differ by a prefix stabilizer; `[eta_a] -> [omega eta_a]` is therefore independent on the quotient. The now-explicit nontrivial scaling `z_ref=omega^m z_a` makes (4.2) well-typed. |
| Formal deck quotient equals the EW2 root-orbit quotient | **PASS** | A prefix-preserving deck reparametrization gives the same next truncated direction; distinct effective orbits have distinct coefficients at height `u` and therefore distinct `F*c` directions. This supplies the previously missing bridge for arbitrary rational `u`, including the fixed zero orbit. |
| Centered first value and common `g` value | **PASS** | Defining `A_F=p_(f-a0,F)`, `P_F=a0+A_F`, and using the transported parameter gives exactly `p_(f-a,F(a))=P_F(z)-a`; the same aligned fixed-polynomial expansion gives `p_(g,F(a))=Q_F(z)`. |
| Every-`z` realization and no duplication | **PASS, apart from the weight issue** | `tau^(-1)` sends a reference point to a centred root orbit, EW2 realizes it, and EW1 plus injective flag transport removes cross-flag duplication. The map correctly counts clusters, not punctures. |
| Direct Q/jump/max transport of `kappa_F` | **FAIL** | The paragraph after (4.2) incorrectly concludes that the complete multiset of rooted jumps is preserved. It compares `omega c` with `c`, but the reference roots satisfy `P(z)=a0` and the target roots satisfy `P(z)=a`; there is no rootwise correspondence when `a` changes. Thus zero versus nonzero coefficient directions can appear or disappear. |

Smallest formal witness: take `K=e=2`, `n=3`, so the effective coefficient
action is `eta -> -eta`, with `z=eta^2`, and take a zero-order first residual

```text
P(z)=z.
```

On the reference fibre `a0=0`, the only covered root is `eta=0`; on the
fibre `a=1`, the covered roots are `eta=+1,-1`. The strict prefix, `K,n,e`,
and the quotient transport can all be identical, yet the former realization
has no post-height gcd jump while the latter has the nonzero-coefficient jump
`e -> gcd(e,n)=1`. This is exactly the zero/nonzero/doubly-realized case the
amendment claims to cover. It is a local formal counterexample to the
transport inference, not a claim of a global Keller counterexample.

Consequently (4.3) is unproved and the fixed weights `b_i` in (6.1) need not
be the weights of the target clusters. The cluster bijection and centered
value map may survive, but the pointwise baseline identity and global
`(22-cl)` do not follow from this report.

Smallest repair: replace the direct prefix argument with an independently
proved theorem that the **repaired jump/max value itself** is invariant under
the cross-fibre `M_(a0,a)` transport, including collision of a zero root with
nonzero root orbits; or redefine the baseline using the transported
cluster's actual weight and rework the Euler integral. Neither conclusion
is supplied by Statement 3.14, the deck quotient, or the cited H5a
convention alone.
