# U2 first nested `nu=1` boundary: exact two-parameter finiteness

Date: 2026-08-29  
Role: producer result; independent exact desk algebra, requiring hostile review  
Scope: the first **direct** U2-to-U2 boundary with fixed inner base data  
Claim level: reduced local arithmetic/transport statement only; no realization,
panel, degree-ceiling, `G2`, or JC2 conclusion

## 0. Result

Fix the base data before a first inner U2 merge and fix the arity of the next
outer U2 merge.  Let `L=L_inner>=1` and `K=L_outer>=1` be the two apparently
unbounded extra degrees.  If the inner `nu=1` state is connected **directly**
to the outer `nu=1` merge, then the positive integral edge index gives

```text
n = a [ R(L+r-1)-K ]/(L K) in N* .                  (E)
```

Here `a>0` and `r>=2` are fixed inner base data and `R>=2` is the fixed outer
arrival count.  Equation (E) makes `K` effectively bounded independently of
`L`.  For each `(K,n)` it determines `L`, except at one apparent vertical
resonance

```text
K=R(r-1),                 n=a/(r-1).
```

That resonance cannot be T1-alive: it has `R|K`, and the outer transport ODE
has no polynomial solution with nonzero constant when `R>=2` and `R|K`.
Consequently the set of T1-alive pairs `(L_inner,L_outer)` is finite and is
given by an explicit uncapped divisibility enumeration below.  In particular,
there is no two-unbounded-parameter formal counterfamily at this first direct
nested boundary.

This also strengthens the presently absorbed U2 transport record: **every**
positive multiple `K` of `R` is universally dead, not merely `K=R`.

## 1. Exact dependencies and quantifiers

Source/review dependencies (full-file SHA-256):

- `ladder/BOOK-OFFAXIS.md`,
  `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77`;
- `xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`,
  `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613`;
- its hostile Fable review,
  `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740`;
- `xmodel/m2-u2-terminal-finiteness-r1-repair-sol56-20260829.md`,
  `3989703ae243705166843dfe5183bbc83cba44d9284071e49deca19cd935933e`;
- its hostile Opus review,
  `9a1775f6c9de92e8204098be3a422222f159d0a4f74baf13a75b1d43598c4a58`;
- `xmodel/m2-u2-first-p2-boundary-finiteness-r1-sol56-20260829.md`,
  `8c46e6bf6e31faa191c67ba1bac6d489e0fe27741b35223ff30992f7d27a4db8`;
- its PASS hostile Fable review,
  `111735765957ef971b720a8dcb373fbe32664047e4028a5a1634b020be405939`.

The argument fixes, before varying either extra degree:

```text
a=A/B > 0 in lowest terms,     r>=2,     mu>=1,
R>=2,                          ell>=1,
```

where `(a,r,mu)` is the absorbed arrival data of the inner U2 merge, `R` is
the outer arrival count, and `ell` is the multiplicity with which this inner
state arrives at the outer merge.  The proof varies only

```text
L=L_inner in N*,               K=L_outer in N*.
```

One may instead allow `ell` to vary over its source-licensed divisor set;
that is a finite union and changes none of the bounds.  The theorem does not
fix a numerical degree cap.

Required hypotheses are: both merges are of the reviewed U2 shape, the outer
arrival weights are equal as required by U2, the displayed inner state is
joined to the outer merge by a single case-I edge, and both local transport
equations are T1-alive.  In particular, no claim is made here about a P0
chain inserted between the two U2 vertices.

## 2. The two U2 frames

For the inner U2 merge, the reviewed normal form gives

```text
dp_in = r mu,                  dq_in = r+L,
E_in  = mu L,
kbar_in = a(r+L)/L,
W = w_child = a(L+r-1)/L,
M_in = gcd(r mu,r+L).
```

The frame value `rho_in=a/L` is not the ODE slope `dp_in/dq_in`; this proof
never identifies them.

At the outer U2 merge all `R` nonzero arrivals have multiplicity `ell` and
common weight `W`.  Hence

```text
dp_out = R ell,                dq_out = R+K,
E_out  = ell K,
kbar_out = W(R+K)/K,
M_out = gcd(R ell,R+K),
w_out = W(K+R-1)/K.
```

The typing/divisibility conditions contributed by this selected arrival are

```text
ell | M_in,
ell | r mu,                   L == -r (mod ell),
M_out = gcd(R ell,R+K) >= 2                         (interior MP2).
```

They only thin the candidate set obtained below.

## 3. Exact equal-weight equations

If another outer arrival is a fixed state of weight `b`, equal weight says

```text
a(L+r-1)/L = b.                                    (EW0)
```

Thus it has no solution when `b<=a`, and otherwise has at most the single
candidate `L=a(r-1)/(b-a)`, subject to positive integrality.

More generally, suppose another first-level U2 state has fixed base data
`(b,s)` and extra degree `J`.  Exact equal weight is

```text
a(L+r-1)/L = b(J+s-1)/J,
(a-b)LJ + a(r-1)J - b(s-1)L = 0.                  (EW1)
```

If `a!=b`, then

```text
((a-b)L+a(r-1)) ((a-b)J-b(s-1))
    = -ab(r-1)(s-1).                              (EW2)
```

After clearing the fixed rational denominators, (EW2) is a fixed nonzero
integer product and therefore has only finitely many positive integral
solutions.

If `a=b`, (EW1) instead becomes

```text
(r-1)J=(s-1)L.
```

Writing `g=gcd(r-1,s-1)`, all positive solutions are the single synchronized
ray

```text
L=(r-1)h/g,                   J=(s-1)h/g,
h in N*.
```

Therefore equal-weight matching among finitely many first-level siblings
leaves at most one common unbounded parameter: any unequal limiting base
weight makes the set finite, while equal bases synchronize all parameters.
The edge calculation next kills the remaining two-parameter possibility
without needing to assume that any sibling is fixed.

## 4. The missing integer anchor

For the direct edge from the inner `nu=1` state to the outer `nu=1` merge,
the source case-I rule is

```text
kbar_out = kbar_in + n/nu_in,
n in N*.
```

Since `nu_in=1`, substitution from Section 2 gives

```text
n = kbar_out-kbar_in
  = a [ R(L+r-1)-K ]/(L K).                       (E)
```

This is the integer anchor that is absent if one inspects either rational
U2 frame in isolation.  With `a=A/B` in lowest terms, clearing denominators
gives the exact divisibility equation

```text
L (B n K-A R) = A (R(r-1)-K).                     (D)
```

No integrality of either individual `kbar` has been assumed.

## 5. Effective finiteness and the unique resonance

Positivity in (E) yields

```text
K(L+a) <= a R(L+r-1).
```

In particular, because `L+r-1 <= rL`,

```text
1 <= K < a R r.                                   (B1)
```

For each such `K`, (E) also gives

```text
1 <= n < a R r/K.                                 (B2)
```

Thus `(K,n)` lies in an explicit finite set depending only on the fixed
data, not on a panel cap.  For every enumerated pair define

```text
D = B n K-A R,                 N = A(R(r-1)-K).
```

If `D!=0`, equation (D) supplies the sole candidate

```text
L=N/D,
```

which is retained exactly when it is a positive integer and all U2 typing,
divisibility, equal-weight, and T1 conditions hold.  If `D=0` but `N!=0`,
there is no solution.  The only way `D=N=0` is

```text
K=R(r-1),                    n=A/[B(r-1)] in N*.   (RES)
```

At the level of edge arithmetic alone, (RES) would leave every inner `L`
free.  The following source-ODE lemma excludes it.

### Lemma (universal death for `R|K`)

Let `P` be any degree-`R` polynomial over characteristic zero with `R>=2`.
If `K=mR` with `m>=1`, there do not exist a degree-`K` polynomial `S` and a
nonzero constant `c` satisfying the U2 transport equation

```text
R P S' - K P' S = c.
```

Indeed, division by `R` gives

```text
P S' - m P' S = c/R != 0.                         (T)
```

Let `C=lc(S)/lc(P)^m` and set `T0=S-C P^m`.  The differential operator on
the left of (T) annihilates `P^m`, so `T0` satisfies the same equation, while
`deg(T0)<mR`.  It cannot be zero because the right side is nonzero.  If
`d=deg(T0)`, the leading term of

```text
P T0' - m P' T0
```

has nonzero coefficient

```text
lc(P) lc(T0) (d-mR)
```

and degree `R+d-1>=R-1>=1`.  It therefore cannot equal a nonzero constant.
This contradiction proves the lemma.

The resonant outer degree in (RES) is the multiple `K=(r-1)R`; hence the
lemma makes it T1-dead.  All live candidates consequently arise from the
finite enumeration (B1)--(B2) with `D!=0`.

## 6. What this closes and what it does not

This closes the smallest two-parameter leak explicitly left by the reviewed
first-P2 finiteness note: with fixed pre-inner data and a direct first
U2-to-U2 edge, one cannot vary both `(L_inner,L_outer)` indefinitely.  It
also provides an exact algorithm, rather than a numerical cutoff, for the
surviving pairs.

The proof does **not** establish:

- recursive finiteness when the nominal base weight `a`, inner arity `r`, or
  outer arity `R` already varies with still earlier nested U2 data;
- the same formula across an intervening P0 chain (its terminal frame must
  first be substituted into the case-I edge rule);
- existence or realization of any retained arithmetic candidate;
- full-cell finiteness, neutral-index control, landing, gluing, Statement
  3.9, a panel theorem, a degree ceiling, `G2-PSC`, `G2-BD`, or JC2.

Review should check especially that the campaign's intended “first nested
boundary” is the direct edge quantified in Section 1, and that its arrival
vertex is indeed the inner U2 child state whose frame is `kbar_in`.  If an
unrecorded mandatory chain edge lies between those states, equation (E) must
be replaced by that chain's exact terminal-frame formula.

No web, AWS, heavy computation, canonical edit, or external formalization
repository was used.

---

Report-body SHA-256 (all bytes before the separator line above):
`11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf`.
