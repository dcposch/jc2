# One-P0 child of the nested-U2 theorem: integral reset and a neutral-ray obstruction

Date: 2026-08-29  
Role: **SPECULATIVE CHILD** of a provisional producer result  
Parent: `m2-u2-nested-nu1-boundary-r1-sol56-20260829.md`, treated here
only as PROVISIONAL  
Scope: exactly one standard `nu>=2` P0 chain vertex between a first
`nu=1` U2 merge and the next `nu=1` U2 merge  
Claim level: reduced/local arithmetic and T1 only; no realization, landing,
full hierarchy, panel, degree ceiling, `G2`, or JC2 conclusion

## 0. Narrow result

The direct-boundary finiteness theorem does not extend unchanged through one
P0 vertex.

There is nevertheless a new cap-free fact.  Because the intervening P0
vertex has integral frame and its incoming case-II edge starts at an inner
U2 vertex with `nu=1`, the inner U2 frame itself must be integral.  For fixed
inner base data `a=A/B>0` and `r>=2`, this forces

```text
L_inner | A r.
```

Thus the inner extra degree is effectively finite before any analysis of the
outer merge.

This does **not** make `L_outer` finite.  A neutral P0 step retains the same
reduced `(w,M)` state and zero modeled price while its last characteristic
index and integral frame grow without bound.  Those forgotten quantities
can co-scale with `L_outer`.  Section 5 gives an exact infinite formal family
with

```text
L_inner=1,                    L_outer=K == 1 (mod 6),
nu_P0=2K,
```

which passes both edge-index equations, both U2 T1 tests, the P0 ODE, all
three displayed gcd/MP2 tests, and the arrival-divisibility/coprimality
tests.  It is not a polynomial-pair realization.  Its purpose is to prove
that reduced `(w,M)` plus the lambda budget cannot close the one-P0 case:
one needs an invariant controlling the last P0 `nu`/`kbar`, or a global
index/product synchronization law that excludes the displayed co-scaling.

## 1. Exact dependencies and fixed/variable data

Full-file SHA-256 dependencies:

- `ladder/BOOK-OFFAXIS.md`,
  `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77`;
- provisional parent
  `xmodel/m2-u2-nested-nu1-boundary-r1-sol56-20260829.md`,
  `99bbe233f8f6f7273b2e5f89705aa5f2189681ce649a8723a66a0f99fa92912b`
  (body `11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf`);
- `xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`,
  `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613`;
- its hostile Fable review,
  `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740`;
- `xmodel/m2-finite-reduced-chain-skeleton-r2-repair-sol56-20260829.md`,
  `3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398`;
- the R1 hostile Fable review retained by that repair,
  `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f`;
- the R1 hostile Grok review retained by that repair,
  `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912`.

Fix the pre-inner-U2 data

```text
a=A/B>0 in lowest terms,      r>=2,      mu>=1,
```

and vary `L=L_inner>=1`.  The intervening P0 vertex may carry its own
source-legal discrete data

```text
nu>=2, l>=1, eps>=0, k>=0, lex>=0, and non-chain multiplicities m_j,
```

with `l | M_0`.  Fix the outer arrival count `R>=2`, while allowing the
outer extra degree `K=L_outer>=1` and the selected outer arrival
multiplicity `h | M_1` to vary over their licensed domains.  The finite-inner
statement is uniform in every one of these P0/outer variables.

## 2. Rebuilt inner and P0 frames

The inner U2 formulas are

```text
kappa_0 = a(r+L)/L,
rho_0   = a/L,                         (frame rho, not ODE slope)
W_0     = a(L+r-1)/L,
M_0     = gcd(r mu,r+L).
```

For the P0 child set

```text
s  = 1+k+lex,
Sm = sum_j m_j,
dp_1 = eps + nu(l+Sm),
dq_1 = 1 + nu s,
C  = l(k+lex)-Sm,
E  = l dq_1-dp_1 = (l-eps)+nu C > 0.
```

The printed P0 transport gives

```text
kappa_1 = l W_0 dq_1/E in Z,
rho_1   = kappa_1/dq_1 = l W_0/E,
W_1     = l W_0 s/E,
M_1     = gcd(dp_1,dq_1).
```

All NE, root-multiplicity, pattern, and price conditions remain additional
filters.  They are not needed for the integral-reset lemma.

## 3. Integral-reset lemma: `L_inner` is finite

Let `j` be the positive integral index on the case-II edge from the inner
U2 vertex to the P0 vertex.  The printed edge equation is

```text
kappa_1 = (kappa_0+j)/nu_0.
```

The inner U2 vertex has `nu_0=1`, whereas the P0 target has `nu>=2`, so
N1/P0 requires `kappa_1 in Z`.  Hence

```text
kappa_0 = kappa_1-j in Z.                           (IR)
```

Writing `kappa_0=z_0`, its U2 formula becomes

```text
z_0 = A(r+L)/(B L),
L(B z_0-A)=A r.                                     (IL)
```

In particular `L | A r`, and the exact candidate list is

```text
L = A r/(B z_0-A),
z_0 in N*,                  B z_0>A,
B z_0-A | A r.
```

This is cap-free and depends only on the fixed inner base data.  Notice why
the direct-U2 proof could not use it: a direct outer U2 vertex also has
`nu=1`, so its frame is allowed to be rational and performs no integral
reset.

## 4. Outer coupling after the P0 step

Let the next U2 merge have `R` equal arrivals of multiplicity `h`, common
weight `W_1`, and extra degree `K`.  Its frame is

```text
kappa_2 = W_1(R+K)/K.
```

For the selected case-I edge from the P0 vertex, whose characteristic index
is `nu`, the positive integral edge index `n` satisfies

```text
n = nu kappa_2-kappa_1
  = (l W_0/E) [nu s R/K-1]
  = kappa_1 (nu s R-K)/(dq_1 K) in N*.              (OE)
```

Equivalently, with `z=kappa_1 in N*`,

```text
K(n dq_1+z)=z nu s R.                               (OC)
```

For fixed full P0 data, (OC) is a finite divisor equation.  It does not give
a uniform outer bound when `nu` varies: on the zero-cost neutral ray both
`nu` and `z=W_0(nu+1)` are unbounded.  Positivity only gives

```text
K < nu s R,                    K < z R/n,
```

whose right sides contain precisely the coordinates erased by the reduced
P0 state.

## 5. Exact neutral-ray formal counterfamily

This family shows that the loss in Section 4 is real at the full displayed
local-equation tier, not merely a weak inequality.

Fix the inner U2 data

```text
a=1,                r=2,                mu=3,
L=1.
```

Then

```text
kappa_0=3,          rho_0=1,            W_0=2,
M_0=gcd(6,3)=3.
```

For every `K=6q+1`, `q>=0`, take one neutral P0 step with

```text
l=3, eps=k=lex=Sm=0, s=1, E=3, nu=2K.
```

Its exact data are

```text
dp_1=6K,                         dq_1=2K+1,
kappa_1=4K+2,                    rho_1=2,
W_1=2,                           M_1=gcd(6K,2K+1)=3,
j=kappa_1-kappa_0=4K-1 in N*.
```

The clean neutral P0 ODE is alive directly.  Put
`Z=eta^nu-c^nu`, `p=Z^3`, `q=eta Z`, and
`delta=dp_1/dq_1=3nu/(nu+1)`.  Then

```text
delta p q' - p' q = -delta c^nu p != 0.
```

Now take an outer U2 merge with

```text
R=2,                 h=3,                 L_outer=K.
```

Use two symmetric copies of the displayed P0 arrival so equal weight is
exact.  The outer data are

```text
dp_2=6,              dq_2=K+2,
M_2=gcd(6,K+2)=3,
kappa_2=2(K+2)/K,
n=nu kappa_2-kappa_1=6 in N*.
```

All additional local arithmetic checks advertised above hold:

```text
l=3 | M_0,
h=3 | M_1,
gcd(nu,h)=gcd(2K,3)=1,
M_0=M_1=M_2=3>=2.
```

Both U2 transport equations are T1-alive: their radical degree is `2`, and
their extra degrees `1` and `K` are odd.  For the inner cell this is visible
already from `Rad=t^2-A`, `S=t`, which gives constant `-2A != 0`; the
reviewed quadratic classification supplies the outer odd-`K` solution.
The root-multiplicity inequalities are strict, and the intervening P0 step
is clean/neutral, hence has modeled price zero.

Therefore the formal local data survive for every `K==1 (mod 6)`.  The
reduced state presented to the outer merge is always

```text
(W_1,M_1,lambda_P0)=(2,3,0),
```

while `(nu,kappa_1,K)=(2K,4K+2,K)` escapes to infinity.

## 6. Precise obstruction and maximum consequence

The maximum unconditional consequence at this scope is:

> For fixed pre-inner-U2 data `(a=A/B,r,mu)`, any path consisting of that
> `nu=1` U2 vertex, exactly one standard `nu>=2` P0 vertex, and then a
> `nu=1` U2 merge has `L_inner | A r`.  No theorem bounding `L_outer`
> follows from the reviewed reduced P0 state `(w,M)`, modeled lambda budget,
> the two local edge equations, MP2, St 8.4, the arrival coprimality law, or
> local T1.

The counterfamily identifies the missing datum exactly.  A successful
extension must add at least one constraint that is sensitive to the last
P0 index `nu` or frame `kappa_1` and that forbids their linear co-scaling
with `K`.  Candidate sources are a full hierarchy `i`/degree-product
synchronization equation, a partner-dependent special-`nu` law, or a
realization/gluing condition.  Any invariant factoring only through
`(W_1,M_1,lambda)` cannot distinguish the family and therefore cannot prove
outer finiteness.

This note does not assert that the formal family is realizable by one global
Sigray configuration or by a Keller pair.  It does not settle sibling
index-product compatibility, full degrees, neutral-stack identification,
landing, Statement 3.9, panel completeness, a degree ceiling, `G2`, or JC2.

No web, AWS, heavy computation, canonical edit, commit, or push was used for
the mathematics in this report.

---

Report-body SHA-256 (all bytes before the separator line above):
`16dcbfcf26259f76cefa42eaced12fff4a334514f113d672f173818ce6a3c31b`.
