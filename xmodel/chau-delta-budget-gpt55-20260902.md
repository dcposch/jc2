# CHAU-DELTA-BUDGET: Chau cap, infinity delta, and CLAIM [D]

Lane: `CHAU-DELTA` (gpt55).  Date: 2026-09-02.
Output: `xmodel/chau-delta-budget-gpt55-20260902.md`.
Basis commit: `809f2d0175f202d63fe4b33c5b8e68f66791d126`.

No exit-price assertion is made in this report.  No canonical ledger was
edited, no `jc2-lean` content was inspected, and no CAS was used beyond small
sympy series/arithmetic checks.

## Input integrity

The frozen read-only inputs were hashed before review and all matched the
charge:

```text
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.JlCLiT/inputs/ideation-20260902T0741Z-opus5.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.JlCLiT/inputs/companion-curve-alln-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.JlCLiT/inputs/horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.JlCLiT/inputs/mprime-alln-h2-opus5-20260902.md
```

Primary source used: `refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf`,
read with `pdftotext -layout` directly from the local PDF.  The relevant
campaign references are COMPANION C6-C8 and SS3.3/SS7
(`companion...md:314-316,337-368,682-685`), HF Prop. 3.2 and B3-N4
(`horn...md:286-304,317-347`), and the H2 profile/B2 thresholds
(`mprime...md:413-436,672-683`).

## Verdict matrix

1. **CONFIRMED, with notation repair.** Chau applies under the stated Keller
   and monic-in-`y` hypotheses.  Under H2, if `m` is the component
   parametrisation multiplicity, then
   `n = deg A_F = m max(d,e)` and `m <= K`; the resultant exponent is
   `M_R = alpha m` and must not be silently identified with `m` unless the
   `R_0` component is reduced.
2. **GAP / OPEN.** `delta_infty` is not a function of `(m,d,e)` alone once
   `m > 1`.  The needed extra datum is the Puiseux characteristic, equivalently
   the value semigroup, of the unique branch at infinity.  Type:
   `OPEN[DELTA-INFTY-NOT-NUMERICAL]`.
3. **GAP.** With an augmented infinity semigroup the B2 beta bound is immediate
   per tuple, but Chau does not by itself close B2 for `5 <= N <= 16`.  Also,
   fixed geometric degree `N` has no finite `(m,d,e)` list unless some separate
   theorem bounds `max(deg P, deg Q)` in terms of `N`.
4. **CONFIRMED.** CLAIM [D] stands after the same notation repair.  The
   `(9,6)` cap is saturated by the degree-9 realised component, so an actual
   reducible non-properness set of a Keller map of coordinate degrees `(9,6)`
   cannot contain any companion.
5. **CONFIRMED at budget-only scope; exact realisability inherits item 2.**
   `n = 3` has only the cuspidal cubic budget with `k = 0`, hence is case (A).
   B3 needs `n >= 4`.  The finite `n <= 8` necessary list is given below.

## 1. Chau transfer under H2

Notation used here:

```text
D_P = deg P,  D_Q = deg Q,  K = gcd(D_P,D_Q),
D_P = Kd,     D_Q = Ke,     gcd(d,e)=1,     L = max(d,e).
```

Chau Theorem 1 assumes a dominant polynomial map
`f=(P,Q): C^2 -> C^2` with `J(P,Q) = const != 0`, `deg P = Kd`,
`deg Q = Ke`, `gcd(d,e)=1`, and `P,Q` monic in `y`:

```text
P(x,y) = A y^(Kd) + ... ,    Q(x,y) = B y^(Ke) + ... .
```

The monic hypothesis is harmless in the intended use: Chau states just after
Corollary 2 that a right action on the source coordinates does not change
`A_f`, and the numbers `d,e,B^d/A^e,R_0` are invariant under those right
actions.  Thus a generic linear source change can make the top `y` coefficients
nonzero without changing `deg P`, `deg Q`, the geometric degree, or `A_F`.

Chau defines

```text
Res_y(P-u,Q-v) = R_0(u,v) x^N + ... + R_N(u,v),
```

and explicitly says that this `N` is the geometric degree of `f`.  This is the
campaign's geometric degree `N`, not `deg P`, `deg Q`, `d`, `e`, or a Puiseux
denominator.

Theorem 1 gives each irreducible component a polynomial parametrisation

```text
xi |-> (A xi^(m_i d) + lower,  B xi^(m_i e) + lower),    m_i in N.
```

COMPANION C6 records the campaign form: with Lemma A/birational
normalisation, `deg D_i = m_i L`.  COMPANION C8 records Chau Corollary 2:
all components meet the same point of `L_infty`, and each has one place at
infinity, with common exponent `d/e` and common `c^e` after the correction in
COMPANION SS3.3.  Under H2, `A_F` is irreducible, so there is one such component:

```text
A_F = image(xi |-> (a(xi),b(xi))),
deg a = m d,  deg b = m e,  deg A_F = n = m L,
one place at infinity.
```

The only repair needed is notation.  Chau Corollary 1's exponent in `R_0` is a
resultant exponent.  If

```text
R_0 = c prod_i f_i^(alpha_i),        alpha_i >= 1,
```

and the weighted leading form of `f_i` is
`(B^d u^e - A^e v^d)^(m_i)`, then the corrected Corollary 1 exponent is

```text
M_R = sum_i alpha_i m_i.
```

The degree bounds from the resultant are

```text
deg_u R_0 <= deg_y Q = Ke,    deg_v R_0 <= deg_y P = Kd.
```

The leading form contributes `deg_u = M_R e` and `deg_v = M_R d`, so
`M_R <= K`.  Hence every component multiplicity satisfies `m_i <= K`, and under
H2, `m <= K`.  If the submission's `M` means this component multiplicity, the
transfer is confirmed.  If it means Chau Corollary 1's resultant exponent, then
`deg A_F = M L` has a missing reducedness hypothesis and should be replaced by
`deg A_F = m L <= M_R L`.

Consequently the degree cap that is actually needed is still valid:

```text
sum_i deg D_i = L sum_i m_i <= L M_R <= L K = max(deg P, deg Q).
```

## 2. The infinity delta

The proposed closed form `delta_infty(m,d,e)` does not exist at the level of
Chau's numerical data.  Chau fixes the first asymptotic exponent and the leading
coefficient class; he does not fix the later Puiseux characteristic exponents.

Assume first `d > e`; the case `e > d` is obtained by swapping `u,v`.  Write
`r = md`, `s = me`, `n = r`.  In the projective chart `U=1` at the infinity point,
with `tau = 1/xi`,

```text
Z = 1/a(tau^-1),        W = b(tau^-1)/a(tau^-1),
ord_tau Z = md,         ord_tau W = m(d-e).
```

These two orders have gcd `m`.  For `m > 1`, they cannot be the whole value
semigroup of a one-branch plane singularity.  The missing data are precisely the
later Puiseux characteristic values that make the gcd drop to `1`.

Closed form after supplying the missing datum: let
`Gamma_infty` be the value semigroup of the branch at infinity, with
characteristic sequence `beta_0,...,beta_g`, `e_i = gcd(beta_0,...,beta_i)`,
`e_g = 1`, and `n_i = e_{i-1}/e_i`.  Then

```text
delta_infty = # (N_{\ge 0} \ Gamma_infty)
             = (1/2) ( sum_{i=1}^g (n_i - 1) beta_i - beta_0 + 1 ).
```

For `m=1` and `d != e`, the first two orders are coprime, so the branch has the
single characteristic pair determined by `(|d-e|, max(d,e))`.  The failure is
exactly at the multiplicity `m > 1` cases that the `(9,6)` row uses.

Control on the realised `(9,6,2)` component.  COMPANION SS3.3 gives

```text
(u,v) = (t^9 + 12 t^5 + 24 t,  t^6 + 8 t^2),
(m,d,e) = (3,3,2),  n = 9.
```

At infinity, in the chart above,

```text
Z = tau^9 - 12 tau^13 + 120 tau^17 - ...
W = tau^3 - 4 tau^7 + 24 tau^11 - ...
W^3 - Z              = -64 tau^21 + ...
W^3 - Z + 64 W^7     = -64 tau^25 + ...
```

The value `21` is still divisible by `3`; the first value dropping the gcd to
`1` is `25`.  Thus `Gamma_infty = <3,25>` at the characteristic level, and

```text
delta_infty = (3-1)(25-1)/2 = 24.
```

The degree-9 genus budget is

```text
p_a = (9-1)(9-2)/2 = 28.
```

The realised affine curve has four nodes, so `delta_aff = 4`; hence
`delta_aff + delta_infty = 4 + 24 = 28`, as required.

Variation with the same Chau numbers.  The polynomial curve

```text
(u,v) = (t^9, t^6 + t)
```

has the same bidegree `(9,6)`, the same `(m,d,e) = (3,3,2)`, and one place at
infinity.  But now

```text
Z = tau^9,       W = tau^3 + tau^8,
W^3 - Z = 3 tau^14 + ...
```

so the characteristic semigroup is `<3,14>` and
`delta_infty = (3-1)(14-1)/2 = 13`.  I do not assert that this curve is a
Keller non-properness set; it is enough to show that Chau's `(m,d,e)` data alone
do not determine the infinity branch.  The honest campaign type is therefore
`OPEN[DELTA-INFTY-NOT-NUMERICAL]`.

## 3. B2 substitution

For any augmented tuple where the infinity semigroup is known, set

```text
n = m max(d,e),
Delta_aff = (n-1)(n-2)/2 - delta_infty.
```

In case (B2), each point counted by `beta` carries at least one singular branch,
hence contributes at least `1` to the affine delta sum.  Therefore

```text
beta <= Delta_aff.
```

MPRIME's H2 profile gives the lower requirements:

```text
5 <= N <= 10:   beta >= 2,
11 <= N <= 16:  beta >= 1.
```

Thus an augmented tuple kills B2 if

```text
Delta_aff <= 1   for 5 <= N <= 10,
Delta_aff = 0    for 11 <= N <= 16.
```

This is a valid per-curve or per-`(m,d,e,Gamma_infty)` beta bound.  It is not a
closed B2 theorem from `(m,d,e)` alone, because item 2 leaves
`delta_infty` unpinned.

The admissible `(m,d,e)` set is also not finite at fixed geometric degree `N`
from Chau alone.  The cap is

```text
m max(d,e) <= max(deg P, deg Q),
```

and no charged input proves `max(deg P,deg Q) <= f(N)`.  In fact the known
degree inequalities go in the wrong direction for finiteness.  A finite list is
available only after fixing an external coordinate-degree cap, fixing `n`, or
adding a theorem of type `OPEN[N-VS-MAPDEG]`.

## 4. CLAIM [D]

CLAIM [D] stands.

Check (a), additivity.  With `R_0 = c prod_i f_i^(alpha_i)`, `alpha_i >= 1`,
and corrected Chau leading forms
`f_i^+ = (B^d u^e - A^e v^d)^(m_i)`, the weighted-leading form of `R_0` is

```text
(B^d u^e - A^e v^d)^(sum_i alpha_i m_i).
```

So `M_R = sum_i alpha_i m_i >= sum_i m_i`.

Check (b), the realised component's `m_1`.  At the row with
`deg P = 9`, `deg Q = 6`,

```text
K = gcd(9,6) = 3,   (d,e) = (3,2),   L = 3.
```

Any component of degree `9` in this numerical row has

```text
deg D_1 = m_1 L = 9,   hence m_1 = 3.
```

The explicit leading form `(u^2-v^3)^3` is a positive control, not the only
reason for `m_1 = 3`.

Check (c), normalisation and resultant degree.  Chau's monic-in-`y`
normalisation is achieved by generic source linear change; it preserves the
coordinate degrees and `A_F`.  In the resultant, Chau's `N` is the geometric
degree, while the degree bounds used for the cap are

```text
deg_u R_0 <= deg_y Q = 6,     deg_v R_0 <= deg_y P = 9.
```

The realised component alone has `m_1 = 3`, so its leading contribution already
has `deg_u = 3e = 6` and `deg_v = 3d = 9`.  Any companion has `m_2 >= 1` and
would force

```text
M_R >= m_1 + m_2 >= 4 > K = 3,
```

equivalently

```text
deg D_1 + deg D_2 >= 9 + 3 > max(deg P,deg Q) = 9.
```

Therefore no Keller map with coordinate degrees `(9,6)` can have a reducible
`A_F` containing the realised degree-9 component.  The companion curve may exist
as an abstract rational one-place curve, as COMPANION's construction shows, but
it cannot be the additional component of the actual `R_0` for this row.

General razor.  Under the exact hypotheses:

```text
F=(P,Q) is Keller, A_F != empty;
after generic source linear change P,Q are monic in y;
deg P = Kd, deg Q = Ke, gcd(d,e)=1;
A_F = union_i D_i is the actual non-properness set cut out by R_0;
each D_i is counted as a reduced irreducible component, with Chau
parametrisation multiplicity m_i and one place at infinity.
```

Then every candidate reducible numerical type must satisfy

```text
sum_i deg D_i <= max(deg P, deg Q).
```

This is a necessary prefilter only.  It does not assert realisation when the
inequality holds.

## 5. B3 at geometric degree N = 4, with n <= 8

Use HF Prop. 3.2:

```text
gcd(p,q)=1, p,q >= 2, and, up to swapping p and q,
one of p,q is divisible by 2 and the other by 3.
```

I also impose the automatic tangent-line bound `max(p,q) <= n`: for a cusp
`x^p=y^q`, the tangent line meets the branch with multiplicity `max(p,q)`, so
Bezout with an irreducible degree-`n` curve forbids `max(p,q)>n`.  Without this
line-contact check, the genus budget alone would falsely admit pairs such as
`(2,9)` on a quintic.

For fixed `n`, the Chau triples are exactly

```text
T_n = { (n/L, L, c), (n/L, c, L) :
        L | n, 2 <= L <= n, 1 <= c < L, gcd(c,L)=1 }.
```

For a cusp pair `(p,q)`, put `delta_c = (p-1)(q-1)/2` and
`p_a(n) = (n-1)(n-2)/2`.  With `k` double points of contacts `t_i >= 1`,
the budget is

```text
delta_c + sum_i t_i + delta_infty = p_a(n).
```

Thus the budget-only necessary range is

```text
1 <= k <= p_a(n) - delta_c
```

for B3.  Exact realisability still requires choosing contacts and an infinity
semigroup with `delta_infty = p_a(n) - delta_c - sum_i t_i`.

The finite list for `n <= 8`, written up to swapping `p,q`, is:

```text
n=3, p_a=1:
  cusp (2,3), delta_c=1 gives k=0 only.  This is case (A), not B3.

n=4, p_a=3, T_4 as above:
  (2,3), delta_c=1, k=1..2.

n=5, p_a=6, T_5 as above:
  (2,3), delta_c=1, k=1..5;
  (3,4), delta_c=3, k=1..3.

n=6, p_a=10, T_6 as above:
  (2,3), delta_c=1, k=1..9;
  (3,4), delta_c=3, k=1..7.

n=7, p_a=15, T_7 as above:
  (2,3), delta_c=1, k=1..14;
  (3,4), delta_c=3, k=1..12.

n=8, p_a=21, T_8 as above:
  (2,3), delta_c=1, k=1..20;
  (3,4), delta_c=3, k=1..18;
  (3,8), delta_c=7, k=1..14.
```

All admissible budget tuples are the Cartesian product of the listed cusp/k
rows for a given `n` with `T_n`.  If ordered cusp pairs are required rather than
the usual up-to-swap convention, include the swapped orientation satisfying the
corresponding half of HF Prop. 3.2.

The Opus claim that `n >= 4` is forced for B3 is confirmed: for `n = 3`,
`p_a=1`, the only cusp budget is `(2,3)` with `delta_c=1`, leaving
`delta_infty = 0` and no double point.  That is the one-cusp case (A), not the
B3 profile "cusp plus multibranch point".

## Final disposition

The Chau degree transfer is valuable, but the Card 1 shortcut overpromotes the
infinity delta.  The cap `sum deg D_i <= max(deg P,deg Q)` is solid and kills
the proposed `(9,6)` companion realisation.  The delta-budget becomes a finite
enumeration only after adding the infinity Puiseux characteristic or an
external degree cap in geometric degree `N`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14374`.
- Body SHA-256:
  `8df5428eeb2cc333b8f432067a6da7e7c1d389f65f1361029f529cdd5a6edc37`.
- Frozen basis: `809f2d0175f202d63fe4b33c5b8e68f66791d126`.
