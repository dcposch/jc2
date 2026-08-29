# Mixed-multiplicity root window — coordinator integration — 2026-08-28

## Disposition

**GREEN, with the scope repair below.**  This integrates an independent
Sol/xhigh derivation, a hostile GPT-5.5/xhigh audit, and the coordinator's
direct rereading of Sigray, Proposition 8.1, Statement 8.2, Statement 8.4,
Statements 9.2--9.4, and Proposition 9.3 in `refs/sigray_full.pdf`.

This theorem extends the promoted all-`mu=1` root window edgewise to mixed
multiplicities.  It does **not** extend MP6's `k=0` conclusion to an
all-`mu>=2` root merge.

## The theorem

Let `R=(0,y)` be a genuine contact-zero root merge.  Let

```text
R,H_e in V_a cap T_a^searrow,   H_e=R+c_e,   D_R>0.
```

Use the lower/rootward-to-upper orientation in Sigray Proposition 9.3:
`F=R`, `G=H_e`.  A genuine contact-zero merge has

```text
R in V_{2,a} \ V_{1,a},
```

so every incoming root edge is Proposition 9.3 case I.

For the Proposition 8.1 reduced root data `p,q`, put

```text
A = deg p,                 B = deg q,
mu_e = mult(p,c_e),        i = the Proposition 8.1 exponent at R,
X_R = D_R/i,
w_e = (kappa_bar(H_e) - D_H_e/deg(p_H_e))/nu_H_e.
```

Then every actual searrow parent edge satisfies

```text
X_R = mu_e(1-w_e),
X_R = A/B,
w_e = 1 - A/(mu_e B),
0 < w_e < 1.
```

## Proof trace

1. Proposition 9.3(c),(d), Statement 9.2, and
   `deg(p_H_e)=i*mu_e` give the case-I handshake
   `X_R=mu_e(1-w_e)`.
2. At a genuine root merge, `p` has at least two distinct roots.  The proof
   of Proposition 8.1 makes `q` have multiplicity one at every `p`-root, so
   `B>=2`.  In Proposition 8.1(iv), the left side has potential degree
   `A+B-1`, strictly above the right side.  Its leading term therefore
   cancels, giving `X_R=A/B`.
3. The raw `T_a^searrow` sign computation on the edge gives
   `mu_e B>A`.  Hence `A/(mu_e B)` lies strictly between zero and one.

The third step is the safe root reading.  Do not cite Statement 8.2 as a
blanket root theorem: its printed proof invokes the nonroot formulation and
the pure-power `deg q=1` endpoint is an edge case.  For a *genuine merge*,
the preceding `q`-root and `B>=2` argument supplies exactly the needed
scope.

## When one arrival has `mu=1`

If at least one arriving edge has `mu_e=1`, the repaired root-scope form of
MP6 applies.  Write `r` for the number of arriving roots and
`S=sum_e mu_e`.  Then

```text
A=S,                  B=r+l,
X_R=S/(r+l),          w_e=1-S/(mu_e(r+l)),
M_R=gcd(S,r+l),       psi=r+l-1,
l >= S-r+1.
```

The last inequality is the `mu=1` edge's searrow condition `r+l>S`.
For all `mu_e=1`, this specializes to

```text
S=r,   l>=1,   w_e=l/(r+l),   M_R=gcd(r,l).
```

## Scope firewall

Do **not** infer any of the following for an all-`mu_e>=2` root merge:

```text
A=S;  B=r+l;  k=0;  absence of northeast/non-chain p-roots;  B>A.
```

Only the edgewise identities and `0<w_e<1` are promoted there.  This is not
a root extension of Statement 8.4 and not a root-global invocation of
Statement 8.2.

## Immediate campaign consequences

- Any independently certified parent-depth alphabet contained in
  `[1,infinity)` excludes that parent from a genuine root merge, regardless
  of `mu_e`.
- The certified row-1 alphabet `W={2}` therefore excludes any root meet that
  receives that row-1 branch.  In particular, within the filed
  `BOOK-OFFAXIS` perimeter it kills the root-meet subcase of the unique
  two-pole `td=7` entry.  It does not close that entry's interior-merge
  sector or the full `td=7` panel.
- The stronger claim that the whole two-pole `td=6` root sector is now empty
  is a high-confidence promotion candidate.  It still requires a narrow
  dependency audit of `L1a(b)`/the claim that a row-1 `M=1` branch reaches
  every such root meet; do not use it as a whole-sector theorem until that
  audit is recorded.

## Provenance

- Producer: `/root/mixed_root_extension`, Sol xhigh, read-only response.
- Hostile audit: `/root/mixed_root_hostile`, GPT-5.5 xhigh,
  `REPAIR`; the repair is the Statement 8.2/root-scope wording above.
- Coordinator: direct page-level check against `refs/sigray_full.pdf`.
- No CAS, AWS, or `jc2-lean` was used or touched.
