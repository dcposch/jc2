# Hostile review: N-VS-MAPDEG

Reviewer: gpt-5.5
Date: 2026-09-02
Report: `xmodel/n-vs-mapdeg-review-gpt55-20260902.md`

No exit-price assertion is made here; no `charge_basis` line is emitted. I did
not edit canonical ledgers and did not inspect `jc2-lean`. The only repo write is
this bounded review report.

## Custody

The six frozen inputs in `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.202ftE/inputs`
were hashed before review. All matched the charge:

```text
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  deg-af-vs-n-opus5-20260902.md
50f62fae3d6265f93781185e62979925471063676cbeb0d1fe67c8dfc170e056  deg-af-vs-n-review-gpt55-20260902.md
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  meridian-floor-sharpen-opus5-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  b3-boundary-instrument-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  chau-delta-budget-gpt55-20260902.md
```

Abbreviations: **NVM** = charged `n-vs-mapdeg`; **DG** = charged `deg-af-vs-n`;
**DR** = its review; **MFS** = charged meridian-floor sharpen; **I11** =
integration #11; **CD** = Chau delta budget; **BI** = charged B3 boundary
instrument; **BR** = its review.

## Verdict Matrix

```text
ITEM 1  D_min and NEG-GEN
        VERDICT: CONFIRMED for invariant definition, right-action custody, and
        the general-dominant refutation; GAP if read as an exact D_min
        computation for (x, x^c y^N).
        SOURCE: NVM:89-121, 162-190; Chau 2004 OCR:85-88.
        REPAIR: promote NEG-GEN as
          ceil((c+N+1)/2) <= D_min(F_{N,c}) <= c+N,
        with A_F={u=0}, N_geo=N, n_min=1, Jac=N x^c y^(N-1). The lower bound
        alone refutes any general-dominant bound at fixed N. Exact
        D_min=c+N needs an extra coordinate-pair remainder lemma not supplied.

ITEM 2  Polar ledger, DEG-SPLIT, NOETHER-K, determinant
        VERDICT: CONFIRMED with scope repairs.
        SOURCE: NVM:235-267, 287-331, 343-376, 378-405, 407-444.
        REPAIR: state the compactification and definitions: common-degree
        rational map P^2 -->> P^2, blow up boundary base points on L_infty,
        X\L~=A^2, Z=Phi^*L_infty=D H-sum a_i E_i, kappa=sum_{C->L_inf} k_C,
        T=sum satellite a_i. NOETHER-K is Keller/H2; for general dominant maps
        it has the extra affine ramification term Z.R_aff.

ITEM 3  MERIDIAN-FLOOR+
        VERDICT: CONFIRMED, but it has a stronger consequence than NVM states.
        SOURCE: NVM:483-523; MFS:100-134; I11:62-68, 104-108.
        REPAIR: the p-generator proof gives p(W-S)>=N-1 with p<=n-1, hence
        n>=ceil((N-1)/(W-S))+1. Combined with MF-EXACT it proves
        2 g_L + theta_inf >= W-S+1; in particular it closes the recorded
        OPEN[MF-DEFECT]. It is not merely consistent with the equality case
        g_L=0, theta_inf=1: it excludes that case.

ITEM 4  NO-CEILING and satellite mass
        VERDICT: GAP as a universal theorem; CONFIRMED as a theorem about the
        relaxed lattice/polar ledger plus dominant-map witnesses.
        SOURCE: NVM:446-466, 542-610; BI:63-72, 637-699.
        REPAIR: rename to NO-CEILING[LATTICE-LEDGER]. It covers constraints
        of the form Z nef, Z^2=N, proximity/effectivity, I1-I6, DEG-SPLIT,
        and determinant identities. It does not rule out a Keller-specific
        canonical inequality; NVM itself identifies NOETHER-K/Z.K_X as the
        surviving intersection-theoretic route.

ITEM 5  One-integer reduction
        VERDICT: CONFIRMED.
        SOURCE: NVM:612-653, 655-661, 879-890.
        REPAIR: spell out the implication:
          Z.K_X <= f(N) => n <= (3N+f(N))/(W-S),
        since kappa<=N and W-S>=1. Then delta_aff is bounded by p_a(n).
        Known Keller data beyond automorphisms: none; automorphisms/birational
        N=1 force Z.K_X=-3 and do not evidence N>=2.

ITEM 6  Crossing and Moh
        VERDICT: CONFIRMED with Moh normalization repaired.
        SOURCE: NVM:665-733; Moh OCR:3231-3262, 3596-3598, 3838-3839.
        REPAIR: Moh proves no Jacobian counterexample with both coordinate
        degrees <=100, after standard degree/monic reductions; this is exactly
        max(deg f,deg g)<=100. Therefore a Keller counterexample with
        D_min<=100 would contradict Moh, so D_min>=101 for noninvertible Keller
        maps. No gap between Moh's degree notion and D_min.
```

Promotion recommendation: promote Items 2, 3, 5, and 6 with the repairs above.
Promote Item 1 only as a general-dominant refutation by Jacobian-degree lower
bound, not as exact `D_min`. Promote Item 4 only under the explicit
`NO-CEILING[LATTICE-LEDGER]` scope.

## 1. NEG-GEN

For `F_{N,c}(x,y)=(x,x^c y^N)`, `c>=1`, the generic fibre over `(u,v)` with
`u != 0` is

```text
x=u,        y^N = v/u^c,
```

so the geometric degree is exactly `N`. The escaping values are exactly the
target line `{u=0}`: for `v0 != 0`, take `x=t` and `y=(v0/t^c)^(1/N)`, while
for `u != 0` the fibre stays bounded. Hence `A_F={u=0}`, the closure has degree
`n=1`, and target automorphisms cannot lower below a line, so `n_min=1`.

The Jacobian is

```text
Jac(F_{N,c}) = N x^c y^(N-1).
```

It is not Keller unless `c=0,N=1`, which is outside the charged family. The
degree is spent entirely in affine ramification: multiplicity `c` on `{x=0}`
and multiplicity `N-1` on `{y=0}`. The first divisor is contracted to `(0,0)`;
the second maps onto `{v=0}` when `N>1`. This is exactly the term `Z.R_aff`
which disappears in the Keller derivation.

For any equivalent `G=psi o F o chi`, the chain rule gives

```text
Jac G = const * N * chi_1^c * chi_2^(N-1),
deg Jac G >= c+N-1.
```

Since `deg Jac G <= deg G_1 + deg G_2 - 2 <= 2D(G)-2`,

```text
D_min(F_{N,c}) >= ceil((c+N+1)/2).
```

The identity gauge gives `D(F_{N,c})=c+N`, so the certified computation is the
interval

```text
ceil((c+N+1)/2) <= D_min(F_{N,c}) <= c+N.
```

That interval is enough: for every fixed `N`, the lower bound tends to infinity
with `c`, while `n_min=1`. Thus the general-dominant version of
`OPEN[N-VS-MAPDEG]` is refuted. The source does not prove exact
`D_min=c+N`; add the missing coordinate-pair lemma or do not state an exact
minimum.

The invariant definition itself is sound. `D_min` must minimize over both
source and target automorphism factors (NVM:106). Chau's right-action statement
is real: when `A_f` is nonempty, `d,e,B^d/A^e,R_0` are invariant under source
automorphisms (Chau 2004 OCR:85-88). The formula at NVM:114-121 should be read
as an outer target search with an inner source minimization of `K`, not as an
available numerical ceiling.

## 2. Polar Ledger

Compactification: homogenize `P,Q` to common degree `D=max(deg P,deg Q)` and
resolve the rational map

```text
bar F : P^2 -->> P^2,       [X:Y:Z] |-> [P_D^h:Q_D^h:Z^D]
```

by blowing up the base cluster on `L_infty`. Let `sigma:X->P^2`, let
`Phi:X->P^2`, and let the boundary `L~` be the total transform of `L_infty`.
Then `X\L~=A^2`. In `Pic X=<H,E_1,...,E_r>`,

```text
Z := Phi^*(L_infty) = D H - sum_i a_i E_i.
```

Because `Z^2=deg(Phi)*L_infty^2=N`,

```text
sum_i a_i^2 = D^2 - N.
```

For a boundary component `C`, set `m_C=ord_C Z` and `c_C=Z.C`. The projection
formula gives `c_C=0` if `C` is contracted, `c_C=k_C` if `C` maps onto
`L_infty`, and `c_C=s_l n_{c(l)}` for a dicritical over the component
`A_{F,c(l)}`. Define

```text
kappa = sum_{C->L_infty} k_C,
T     = sum_{i satellite} a_i,
Lambda= sum_l s_l n_{c(l)}.
```

The reduced boundary has class `L~_red = H - sum_{satellite i} E_i`, hence
`Z.L~_red=D-T`. On the other hand
`Z.L~_red=sum_C c_C=kappa+Lambda`. Therefore

```text
DEG-SPLIT:       D = Lambda + kappa + T.
```

For a noninvertible Keller map every component of `A_F` is hit by a dicritical,
so

```text
deg(A_F-bar) <= Lambda = D-kappa-T <= D-1.
```

This sharpens Chau's cap exactly as NVM claims. The determinant statement is
also correct with scope: for a smooth SNC compactification of `A^2`, the
boundary components form a Z-basis of `Pic X`, so the intersection matrix has
determinant `(-1)^r`. Do not state it for arbitrary singular/non-SNC
compactifications without resolution.

Noether derivation: `K_X=-3H+sum E_i`, so

```text
Z.K_X = -3D + sum_i a_i.
```

Ramification gives `K_X=Phi^*K_{P^2}+R=-3Z+R`, hence
`Z.K_X=-3N+Z.R` and

```text
sum_i a_i = 3D - 3N + Z.R.                         (general dominant)
```

For Keller maps, `R_aff=0`. Along components mapping to `L_infty`, the
contribution is `(m_C-1)k_C`, whose sum is `N-kappa`. Along dicriticals, the
contribution is `(mu_l-1)s_l n`; under H2 this is `n(W-S)`. Therefore

```text
NOETHER-K:       sum_i a_i = 3D - 2N - kappa + n(W-S),
                 sum_i a_i^2 = D^2 - N.             (Keller, H2)
```

For automorphisms `A_F` is empty, `S=0`, `N=kappa=1`, and this reduces to the
classical Cremona equation `sum a_i=3D-3`.

Desk CAS check, using the same explicit blow-up resolver and synthetic Picard
checker referenced by NVM:

```text
name                 D N | kap Lam T | sum_a sum_a2 D2-N | ZK | Jac
auto y+x^2           2 1 |  1   0  1 |   3     3     3   | -3 | 1
auto y+x^3           3 1 |  1   0  2 |   6     8     8   | -3 | 1
monomial x,xy        2 1 |  1   1  0 |   3     3     3   | -3 | x
monomial x,xy^2      3 2 |  2   1  0 |   5     7     7   | -4 | 2*x*y
NEG x,x^3 y^2        5 2 |  2   1  2 |  11    23    23   | -4 | 2*x^3*y
control x,xy^2+y     3 2 |  2   1  0 |   5     7     7   | -4 | 2*x*y+1
power x^2,y^4        4 8 |  2   0  2 |   4     8     8   | -8 | 8*x*y^3
```

All rows satisfy `D=kap+Lam+T` and `sum_a2=D^2-N`. The two automorphisms satisfy
`NOETHER-K` as `sum_a=3D-3`. The non-Keller rows are controls for the general
polar identities, not for the Keller formula; their missing term is precisely
affine ramification.

I also reran the positive `Z.K_X` witnesses:

```text
psi_k o (x,xy^2), k=2..6:  Z.K_X = -2,-2,0,0,+2
psi_k o (x,xy^3), k=2..6:  Z.K_X = -1,+1,+1,+5,+7
```

So `Z.K_X` is unbounded above in the general dominant class at fixed `N`. These
maps are not Keller.

## 3. Meridian Floor+

The proof uses the pencil through the infinity point of `A_F`, not a generic
target line. Let `(a(t),b(t))` parametrize the one-place curve `A_F`, and set

```text
p = min deg_t l(a(t),b(t)),       l affine-linear.
```

If `n=deg(A_F-bar)>=2`, the leading degree `n` can be killed by a linear form,
so `1<=p<=n-1`. Choose target coordinates with this form as `x`. Then the
defining equation of `A_F` is monic of `y`-degree `p`: a generic vertical line
meets `A_F` in `p` smooth points. Zariski-van Kampen gives generation of
`pi_1(A^2\A_F)` by those `p` meridians.

Each such meridian has the generic cycle type

```text
1^a * product_l mu_l^(s_l),
```

with support `W` and `S=sum s_l` nontrivial cycles. One generator can merge at
most `W-S` blocks in the monodromy action. Transitivity of the degree-`N` etale
cover over the complement therefore gives

```text
p(W-S) >= N-1,
n >= p+1 >= ceil((N-1)/(W-S))+1.
```

This confirms NVM:489-509, including `W=2`: since `mu_l>=2`, `S=1` and
`p>=N-1`, hence `n>=N`.

But the repair is important. I11 promoted MF-EXACT:

```text
n(W-S) = N - 2 + 2g_L + theta_inf.
```

Combining with `n>=p+1` and `p(W-S)>=N-1`,

```text
n(W-S) >= N-1 + (W-S),
2g_L + theta_inf >= W-S+1.
```

Thus MERIDIAN-FLOOR+ proves the recorded `OPEN[MF-DEFECT]` in stronger form:
`2g_L+theta_inf>=2` follows because `W-S>=1`. It is not consistent with
attainment `g_L=0, theta_inf=1`; it rules that attainment out. Promotion should
therefore update I11: the equality case remains a formal case of MF-EXACT, but
is impossible under the H2/Keller hypotheses plus the `p`-projection argument.

## 4. No Ceiling

NVM's lattice argument is correct in its declared algebraic model. Fix a Picard
lattice with intersection form `H^2=1`, `E_i^2=-1`. The conditions

```text
Z = D H - sum a_i E_i,
Z^2=N,
Z nef on boundary classes,
proximity inequalities,
I1-I6 and DEG-SPLIT,
det(boundary matrix)=+-1
```

do not bound `D=Z.H` at fixed `N`. Hodge gives only `D^2>=N`, and four-square
representations realize `D^2-N=sum y_i^2` with `D` arbitrary in the relaxed
lattice. The two dominant families in NVM:547-557 show that this is not only a
formal-lattice pathology: fixed `N` with unbounded `D`, and fixed `N` with
unbounded `n`, are both realized by honest dominant maps satisfying the polar
identities.

The overstatement is NVM:563-565 and the label "no intersection-theoretic
boundary instrument" if read literally. `NOETHER-K` is itself an
intersection/canonical identity, and NVM correctly identifies it as the only
surviving route. The safe theorem is:

```text
NO-CEILING[LATTICE-LEDGER]:
  the polar/effectivity/proximity/determinant package, without the Keller
  ramification condition R_aff=0 or an added canonical upper bound, cannot
  bound D at fixed N.
```

Anything stronger is a heuristic supported by the two families, not a theorem.

## 5. One Integer

Under Keller/H2, `NOETHER-K` is equivalent to

```text
Z.K_X = sum_i a_i - 3D = -2N - kappa + n(W-S).
```

Since `kappa<=N` and `W-S>=1`,

```text
Z.K_X <= f(N)  =>  n <= (2N+kappa+f(N))/(W-S) <= 3N+f(N).
```

Then the promoted degree-delta inequality gives

```text
delta_aff <= p_a(n) = (n-1)(n-2)/2.
```

So any upper bound for `Z.K_X` in terms of `N` closes
`OPEN[DELTA-AFF-VS-N]`. Conversely, a bound on `n` bounds this integer because
`kappa` and `W-S` are already `N`-bounded in the profile range. This confirms
NVM:620-628.

Known Keller evidence beyond automorphisms: none in the reviewed record.
Automorphisms and birational maps have `N=1` and force `Z.K_X=-3`; that value is
Noether's equation, not evidence for noninvertible Keller maps with `N>=2`.
For general dominant maps the statement is false, as the positive witnesses
above show.

## 6. Crossing And Moh

With MERIDIAN-FLOOR+ and DEG-SPLIT,

```text
D_min >= S*n + kappa
      >= S*(ceil((N-1)/(W-S))+1) + kappa.
```

The guaranteed worst case is `S=1`, `kappa=1`, so

```text
D_min >= ceil((N-1)/(W-1)) + 2.
```

Therefore a proved ceiling `D_min<=C` empties the cell whenever

```text
C <= ceil((N-1)/(W-1)) + 1.
```

At `W=2`, this reads `D_min>=N+1`, exactly as charged.

Moh normalization was checked in the local PDF. Moh works with polynomial pairs
`(f,g)` satisfying the Jacobian condition. His theorem setup normalizes
`deg f=deg_y f=m` and `deg g=deg_y g=n` (Moh OCR:3231-3232), then searches
`m<n<=100` under simultaneous-degree minimality (OCR:3255-3262). Appendix II
lists the remaining degree pairs `(64,68),(84,56),(75,50),(99,66)` (OCR
3596-3598) and closes with no counterexample in degrees `<=100` (OCR
3838-3839).

This is a statement about both coordinate degrees, equivalently
`max(deg f,deg g)<=100`. If a noninvertible Keller map had `D_min<=100`, some
`psi o F o chi` would be a Keller counterexample with both coordinate degrees
`<=100`; Moh rules that out. Since automorphisms are preserved under the two
automorphism factors, `F` would be an automorphism. Thus

```text
MOH-FLOOR: noninvertible Keller => D_min >= 101.
```

Consequently any proved `C(N)<=100` for the invariant map degree kills that
geometric degree outright. The whole charged `(B2)` range `5..16` and `(B3)`
range `4..8` are included. There is no gap between Moh's degree and `D_min`.

## Opens

```text
OPEN[N-VS-MAPDEG] upper half
  Question: is D_min bounded above by a function of geometric degree N for
  noninvertible Keller maps?
  Bounded quantity: D_min(F)=min_{psi,chi} max(deg(psi o F o chi)_1,
  deg(psi o F o chi)_2).

OPEN[DELTA-AFF-VS-N]
  Question: is delta_aff(A_F) bounded above by a function of N?
  Bounded quantity: delta_aff, equivalently the number of gaps of the affine
  one-place semigroup in the reviewed H2 setting.

OPEN[ANTICANON-DEFECT]
  Question: is Z.K_X=sum_i a_i-3D bounded above by a function of N for
  noninvertible Keller maps, in particular is it <=0?
  Bounded quantity: the integer Z.K_X, equivalently deg(branch divisor of Phi
  with multiplicity) - 3N.

OPEN[SAT-MASS]
  Question: is T=D-Sn-kappa bounded above by a function of N for a
  degree-minimal Keller representative?
  Bounded quantity: T=sum_{satellite base points} a_i in Z_{\ge 0}.

OPEN[MIN-EMBED-DEGREE]
  Question: is n_min <= 2 delta_aff+1 unconditionally for the one-place curve?
  Bounded quantity: n_min, the minimum degree of the closure of A_F under target
  automorphisms.
```

`OPEN[MF-DEFECT]` should not remain open if MERIDIAN-FLOOR+ is promoted: the
bounded pair `(g_L,theta_inf)` then satisfies the stronger
`2g_L+theta_inf>=W-S+1`.

## Fallacy-v2 Check

Flag/place/series: `D`, `D_min`, `n`, `n_min`, `p`, `N`, `kappa`, `T`, and
`Z.K_X` are kept distinct. `m_C` is polar multiplicity; `a_i` is base-point
multiplicity; `mu_l` is dicritical ramification.

Carrier/attainment: NEG-GEN and the two positive `Z.K_X` families are dominant
non-Keller controls. They do not approximate Keller counterexamples. MF-EXACT
is an identity; MERIDIAN-FLOOR+ excludes its old equality case rather than
assuming an attainment.

Pole/interior: `NOETHER-K` is used only after `R_aff=0` is stated. For
non-Keller rows, only the general polar identities are checked.

Floor/attainment: Moh, DEG-SPLIT, and MERIDIAN-FLOOR+ are floors. The crossing
statements are conditional on an external ceiling.

Variable/ring map: all computations are over `Q` with variables `(x,y)`;
`Z=Phi^*L_infty` is in `Pic X=<H,E_i>`. No saturation, quotient normal form, or
raw-remainder substitution is used.

## Typed Verdict Block

```text
LANE     N-VS-MAPDEG hostile review
SCOPE    Keller, noninvertible where stated; H2 where A_F is treated as a
         one-place irreducible curve. General dominant controls are explicitly
         non-Keller.

CONFIRMED
  D_min definition over both Aut factors; right-action invariance of A_F and
  Chau data (d,e,R_0) under Chau's hypotheses.
  NEG-GEN as a general-dominant refutation by D_min >= ceil((c+N+1)/2),
  with A_F={u=0}, N_geo=N, n_min=1, and affine ramification degree c+N-1.
  DEG-SPLIT: D=sum_l s_l deg(Phi(l)-bar)+kappa+T.
  CAP-STRICT: deg(A_F-bar)<=D-kappa-T<=D-1 for noninvertible Keller maps.
  NOETHER-K: sum a_i=3D-2N-kappa+n(W-S), sum a_i^2=D^2-N, under Keller/H2.
  Boundary determinant det=(-1)^r for smooth SNC compactifications of A^2.
  MERIDIAN-FLOOR+: p(W-S)>=N-1, p<=n-1, hence n>=ceil((N-1)/(W-S))+1.
  One-integer reduction: a bound on Z.K_X bounds n and delta_aff.
  Crossing: D_min<=ceil((N-1)/(W-1))+1 empties (N,W); W=2 gives D_min>=N+1.
  MOH-FLOOR: noninvertible Keller maps have D_min>=101.

GAP / SCOPED
  Exact D_min(F_{N,c}) is not computed in the charged report; only the interval
  ceil((c+N+1)/2)<=D_min<=c+N is proved.
  NO-CEILING is not a theorem against every possible intersection-theoretic
  boundary method. Promote only as NO-CEILING[LATTICE-LEDGER].

REFUTED
  General-dominant upper N->D_min bound: refuted by NEG-GEN.
  Z.K_X<=0 for general dominant maps: refuted by psi_k o (x,xy^2) and
  psi_k o (x,xy^3), with positive values up to +7.
  Keeping OPEN[MF-DEFECT] open after promoting MERIDIAN-FLOOR+: refuted;
  MF+ proves the stronger defect inequality.

MEASURED
  41-map summary rerun: all 41 satisfy I1/I2/Z^2/DEG-SPLIT/proximity checks.
  Seven-row spot table above includes automorphisms, (x,xy^N), NEG-GEN, and a
  non-Keller near-control with Jac=2xy+1.
  Positive anticanonical witnesses rerun for k=2..6 at N=2,3.
  Moh PDF checked directly with pdftotext and page image for Appendix II.

PROMOTION
  Promote Items 2,3,5,6 with repairs. Promote Item 1 as lower-bound refutation
  only. Promote Item 4 only under the lattice-ledger scope.
```

<!-- BODY-END -->
