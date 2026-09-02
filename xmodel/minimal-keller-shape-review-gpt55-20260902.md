# Hostile Review: MINIMAL-KELLER-SHAPE

Lane: `MINIMAL-KELLER-SHAPE-REVIEW`. Date: 2026-09-02.
Reviewer: GPT-5.5. Scope: frozen read-only inputs in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.9FRnN1/inputs`;
local primary refs only; no `jc2-lean`; no canonical ledger edits.

## 0. Custody

Input hashes verified before review:

```text
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  minimal-keller-shape-opus5-20260902.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  keller-pencil-genus-opus5-20260902.md
d57d17f8eb6e776013d283e6796bef0db256088011dae2b73d1383c1e40cc56a  keller-pencil-genus-review-grok46-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  sat-mass-opus5-20260902.md
6af7ec8f74fa434c2c88fcbf25a1939ae367605e8feaab1aa8229fe677e04dcc  sat-mass-review-gpt55-20260902.md
0b55a2c8bf7a8ab64fadf458e8a51bc5390bcb4808bd3c97d58a8769a97cc4a7  integration13-coordinator-fable51-20260902.md
```

Primary ref hashes used:

```text
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
449d8028da79c7f2ae9eff9161553fcc35f75a48989f169c5d9ef54edf88773f  box/mks-drivers-20260902/gv.txt
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  box/mks-drivers-20260902/moh.txt
```

Desk replay:

```text
python3 box/mks-drivers-20260902/run4.py
python3 box/mks-drivers-20260902/final.py
```

`final.py` reported 56 attempted distinct maps, 46 resolved, 5 skipped for
non-rational clusters, 46 all-checks-pass, no failures, 14 `nu=1`, 30
`nu=2`, 2 `nu=0`, and 32 rows with `T=T_class`.

Line tags: `MKS` = `minimal-keller-shape-opus5-20260902.md`; `KPG` =
`keller-pencil-genus-opus5-20260902.md`; `KPG-R` =
`keller-pencil-genus-review-grok46-20260902.md`; `SM` =
`sat-mass-opus5-20260902.md`; `SM-R` =
`sat-mass-review-gpt55-20260902.md`; `I13` =
`integration13-coordinator-fable51-20260902.md`; `gv.txt` and `moh.txt` are
the hashed local extractions above.

## 1. Executive Verdict

The report has real content, but two advertised load-bearing claims are too
broad.

`FIRST-FORK` is confirmed after making explicit that tangency to `L_infty`
changes the length of the chain over one base point, not the number of
neighbours of `E_0`. The six required controls reproduce the claimed
`val(E_0)=nu` and `deg_T(E_0)=nu` when `nu>=2`.

`SUBRECTANGULAR` is confirmed only in the exact GGV scope: a GGV minimal pair,
where `B=min gcd(deg P,deg Q)` over all counterexamples, can be moved to a
standard subrectangular `(m,n)`-pair while preserving both total degrees. The
charged statement says "for every counterexample" and then applies it to every
Aut x Aut degree-minimal representative (`MKS:169-180`, `MKS:352-361`). GGV
does not say that. Repair: promote the two-root/free-`E_0` conclusion for a
GGV-global minimal counterexample, and leave the bridge from orbit-minimality
to GGV minimality as `OPEN[SUBRECT-ORBIT-BRIDGE]`.

`LF`, `MIN`, `E0-LEAF-CAP`, the conditional `CH2+Moh => N>=100`, `CH1` as a
control-class refutation, and the sharpened Moh divisor floor are confirmed
with typing repairs below. The `T <= tau <=> D_min <= 2(tau+N)` biconditional
is refuted: the proved statement is one-way, `T<=tau => D_min<=2(tau+N)`.
The one-unit gap `T>=51-N` versus target `T<=50-N` is confirmed.

No new exit price is asserted; no `charge_basis` line is present.

## 2. FIRST-FORK

Verdict: **CONFIRMED with wording repair**.

Charged lines: `MKS:226-255` define `nu` as the number of distinct base points
of the net on `L_infty`, state `deg_{L~}(E_0)=nu`, and assert
`deg_{T_+}(E_0)=nu` when `nu>=2`.

Reproof. Homogenise to the net

```text
< z^{D-deg P} P^h, z^{D-deg Q} Q^h, z^D > .
```

On `L_infty={z=0}` the base scheme is cut by the nonzero top-degree forms among
the two coordinates. Thus its reduced support is exactly the set of distinct
roots of the top form of the max-degree coordinate, or of the gcd of the two
top forms when the degrees are equal. For a Keller counterexample, `MIN` gives
unequal degrees and `LF` gives `l(R)=const*H^r`, so the reduced support is
`# distinct roots of H`. This is the number of distinct points at infinity of a
generic pencil member, counted without multiplicity.

Tangency repair. If the generic member is tangent to `L_infty` at one of those
points, the local intersection multiplicity is larger than one, but the
support point is still single. In the resolution over that point the successive
points lie on the strict transform of `L_infty`, forming a chain. Each later
blow-up at `E_{q_j} cap E_0` removes the old adjacency to `E_0` and creates the
new one. Hence one reduced base point over `L_infty` contributes exactly one
final neighbour of `E_0`, no matter how high the tangency is. Distinct reduced
base points give disjoint chains and hence distinct neighbours. This proves
`deg_{L~}(E_0)=nu`.

For the polar subtree, the charged multiplicity argument at `MKS:247-251` is
valid. Along a chain over a base point `p`, the terminal exceptional has
`m = jD - sum_{k<=j} a_{q_k}`. Proximity monotonicity gives the displayed lower
bound, and Bezout gives `sum_p I_p(C_gen,L_infty)=D`. If `nu>=2`, every reduced
point has intersection multiplicity at least one, so the first multiplicity
over any fixed point is at most `D-1`, and the terminal neighbour has `m>0`.
Thus all `nu` neighbours survive in `T_+`.

Repair text:

```text
FIRST-FORK counts reduced points at infinity. Tangency only lengthens the
chain above one reduced point; it does not split that point into multiple
neighbours of E_0.
```

Focused replay, six resolved maps:

```text
map                                D   N  nu  valE0  degT(E0)  T  T_class  Psi
(x, y+x^2)                         2   1   1    1       1       1     0      2
(x, y+x^4)                         4   1   1    1       1       3     2      4
(x, xy)                            2   1   2    2       2       0     0      0
(x, x^2 y^2)                       4   2   2    2       2       1     1      0
(x, x(x-1)(x-2)y^2)                5   2   2    2       2       0     0      4
mock l(P)=(x^2 y^3)^2,l(Q)=...^3  15   8   2    2       2      12    12     12
```

Promotion: promote `FIRST-FORK` as a theorem for dominant maps, with the
reduced-support/tangency wording above. Promote `E_0` fork implication
`nu>=3 => Psi >= D(nu-2)`, since `m_{E_0}=D`.

## 3. SUBRECTANGULAR Gauge and CH2

Verdict: **GAP in the advertised scope; CONFIRMED in GGV-global-minimal scope**.

Charged lines: `MKS:163-180` state a Makar-Limanov / van den Essen
subrectangular gauge for every counterexample and say it preserves both
degrees. `MKS:259-270` then derives monomial top form and `nu=2`.
`MKS:352-361` uses this to say `E_0` is free and CH2 is false for
counterexamples.

Primary text. GGV defines
`B=min gcd(v11(P),v11(Q))` over all counterexamples and calls a pair minimal
when it realizes `B` (`gv.txt:693-700`). GGV then says the subrectangular input
is a known fact for counterexamples, credited to Makar-Limanov/vdE
(`gv.txt:702-705`). But the degree-preserving proposition is narrower:
Proposition 4.7 begins "Let `(P,Q)` be a minimal pair" and produces an
automorphism with `(phi(P),phi(Q))` an `(m,n)`-pair while preserving
`v11(phi(P))=v11(P)` and `v11(phi(Q))=v11(Q)` (`gv.txt:796-799`). The proof
uses vdE Cor. 10.2.21 to get the rectangle (`gv.txt:816-820`) and then uses
minimality to rule out degree-raising inverse cases and prove degree
preservation (`gv.txt:845-879`).

So the exact theorem available from refs is:

```text
If JC is false, there exists a GGV-minimal counterexample pair, and after a
source automorphism it is a standard (m,n)-pair in L with m,n>1, still
GGV-minimal, satisfying st_11(P)=en_10(P) and the successor inequalities.
```

This is Corollary 5.21 (`gv.txt:1454-1462`), built from Proposition 4.7.
It is not the statement "every Aut x Aut degree-minimal representative has a
degree-preserving subrectangular gauge."

Within that repaired scope, the monomial conclusion is correct. From the
rectangle `Supp(P) subset [0,a]x[0,b]` with `(a,b)` in support
(`gv.txt:816-823`), `(a,b)` is the unique total-degree top exponent of `P`.
Thus `l(P)=c x^a y^b`. The proof also gives
`st_11(Q)=n(abar,bbar)` and `Supp(Q) subset [0,n abar]x[0,n bbar]`
(`gv.txt:865-870`), so `Q` is subrectangular in the same direction. Since
`a,b` are positive (`Definition 4.3`, `gv.txt:721-726`; Proposition 4.6(3),
`gv.txt:786-791`) and `m,n>1` (`gv.txt:879`), the primitive top form is
`H=c x^u y^v` with `u,v>=1`. Hence `nu=2`.

The CH2 consequence is therefore typed as follows:

```text
For a GGV-global minimal counterexample in the GGV/ML/vdE gauge, E_0 is a
valency-2 free vertex of T_+. CH2 ("E_0 leaf") is false in that gauge.
```

It is not yet gauge-free for every orbit-minimal representative. The report
itself notices this as `OPEN[NU2-RIGIDITY]` at `MKS:596-600`, but its headline
and theorem block overstate the scope (`MKS:59-63`, `MKS:668-670`).

Repair text:

```text
Replace "for every counterexample" by "for a GGV-minimal counterexample
realizing B, in the GGV subrectangular gauge." Add
OPEN[SUBRECT-ORBIT-BRIDGE]: prove that every Aut x Aut degree-minimal
counterexample can be moved degree-preservingly into this GGV standard
subrectangular form, or restrict all downstream promotions to the global-B
minimal pair.
```

Bounded quantity: `OPEN[SUBRECT-ORBIT-BRIDGE]` asks for the pair of total
degrees `(deg P,deg Q)` under source automorphisms inside one Aut x Aut orbit,
with target `nu in Z_{>=1}` after degree-preserving gauges. This is at least
as narrow as the report's `OPEN[NU2-RIGIDITY]`.

Promotion: promote `E0-FREE` only in the repaired GGV-global-minimal scope.
Do not promote the advertised "every degree-minimal counterexample" form.

## 4. LF and MIN

Verdict: **CONFIRMED**.

Charged lines: `MKS:105-128`.

`LF`. Since `[P,Q]` is constant, the top homogeneous part of the bracket
vanishes whenever `deg P + deg Q - 2 > 0`: `[l(P),l(Q)]=0`. Write binary forms

```text
A=l(P)=alpha prod L_i^{a_i},   B=l(Q)=beta prod M_j^{b_j}.
```

If a linear factor of `A` is not a factor of `B`, evaluate at a general point
of that line; the wedge `dA wedge dB` has a nonzero leading term, contradiction.
Thus the factor sets agree. For two distinct factors `L_i,L_j`, the bracket
coefficient contains `(a_i b_j-a_j b_i) det(dL_i,dL_j)`, so all ratios
`a_i/b_i` are equal. Let `deg P:deg Q=d:e` in lowest terms; then
`a_i=d h_i`, `b_i=e h_i` and

```text
l(P)=alpha H^d,  l(Q)=beta H^e,  gcd(d,e)=1,  deg H=K=gcd(deg P,deg Q).
```

`MIN`. If `d=1`, then `l(Q)=beta(alpha^{-1}l(P))^e`; the target elementary
automorphism `(U,V)->(U,V-cU^e)` cancels the top degree of `Q` and lowers
`max(deg P,deg Q)`. The case `e=1` is symmetric. If `d=e`, coprimality gives
`d=e=1`, again nonminimal. Therefore at an orbit-degree-minimal representative
`d,e>=2`, `d!=e`, `max(d,e)>=3`, and `D=K max(d,e)>=3K`.

Repair: remove the phrase "`deg P + deg Q - 2 > 0` for a counterexample" as a
separate premise if desired; it is automatic because a noninvertible Keller
pair is not a pair of affine-linear coordinates. The proof otherwise stands.

Promotion: promote `LF` and `MIN`.

## 5. E0-LEAF-CAP, CH1, CH2 Pricing

Verdict: **CONFIRMED as conditionals; advertised vacuity depends on repaired
SUBRECT scope**.

Charged lines: `MKS:379-386` state `E0-LEAF-CAP`. KPG states CH1/CH2 pricing
at `KPG:554-564`; the KPG review confirms CH2 only as a conditional at
`KPG-R:13-18`; Integration #13 promotes the old conditional nine kills at
`I13:38-45` and says the hypotheses are not proved.

Reproof. Use the already reviewed identities

```text
Z.K_X = 2g_L - 2 - N
Z.K_X = Psi - Lambda - kappa
```

from Integration #13 (`I13:22-28`). If `Psi=0` and `E_0` is a leaf of `T_+`,
then `Lambda` includes `m_{E_0}=D`; if `E_0` is isolated it includes `2D`.
Since `kappa>=1`,

```text
2g_L - 2 - N = -Lambda - kappa <= -D - 1
```

and hence

```text
D <= N + 1 - 2g_L <= N+1.
```

For a noninvertible Keller counterexample, Moh gives `D_min>=101`. If CH2
means `Psi=0` plus `E_0` leaf in some gauge, the cap gives
`D_min <= D <= N+1`, so `N>=100`. Thus the new pricing "CH2 + Moh kills every
`N<=99`" is a legitimate conditional and is stronger than the old nine-cell
pricing.

Typing repair. This is vacuous for the repaired GGV-global-minimal
subrectangular counterexample because `nu=2` and `E_0` is not a leaf. It is not
yet proved vacuous for every Aut x Aut degree-minimal representative until
`OPEN[SUBRECT-ORBIT-BRIDGE]` or `OPEN[NU2-RIGIDITY]` is closed.

`CH1`. The report correctly refutes any ambient statement `Psi=0` for all
Jacobian pairs: `(x,y+x^k)` has `Psi=k=D`, reproduced in the replay for
`k=2,...,6` (`MKS:328-343`, `run4.py`). This does not refute the restricted
noninvertible Keller/H2 hypothesis; the repair is to call it a control-class
failure, not a theorem about counterexamples. Under Keller+H2,
`POLAR-DEGREE` gives `Psi=Lambda-2N+n(W-S)`, so adding `MERIDIAN-FLOOR+` gives
the reported `Lambda<=N` consequence (`MKS:393-410`).

Promotion: promote `E0-LEAF-CAP` and the `N<=99` CH2 pricing as a conditional.
Withdraw Integration #13's nine actual kills after fixing the subrectangular
scope. Promote the automorphism family as a scope warning for CH1, not as a
counterexample theorem.

## 6. SAT-MASS, T, and the Moh Cross

Verdict: **REFUTED for the biconditional; CONFIRMED for the one-way price and
the one-unit floor gap**.

Charged lines: `MKS:416-438`. SAT-MASS itself only proved the implication:
`T<=tau` on a degree-minimal `W<=3` H2 representative gives
`D_min<=2(tau+N)` (`SM-R:360-372`, `SM-R:470-472`). It explicitly says this is
conditional and that HALF-CAP is a floor, not evidence that such a `tau`
exists (`SM-R:389-390`).

The valid derivation is:

```text
W<=3 + H2 + nonproper => ell=1.
If D>N, HALF-CAP gives D <= 2(T+kappa).
If D<=N, D <= 2(tau+N) is trivial for tau>=0.
So T<=tau => D_min=D <= 2(tau+kappa) <= 2(tau+N).
```

The reverse implication does not follow. From `D<=2(tau+N)` and
`D=Sn+kappa+T`, one only gets `T<=2tau+2N-Sn-kappa`; no promoted lower bound
forces `Sn+kappa>=tau+N`. HALF-CAP gives `T>=D/2-kappa`, a lower bound, not an
upper bound. Dominant controls already show the algebraic reverse is false:
for the replay row `mock u=4,v=12,m=2,n=3`, `D=48`, `N=25`, `T=35`; with
`tau=0`, `D<=2(tau+N)` holds but `T<=tau` fails. This row is not Keller, but it
pinpoints the missing implication: it cannot be obtained from
HALF-CAP+DEG-SPLIT alone.

One-unit gap. Combining Moh `D_min>=101` with HALF-CAP gives

```text
T >= D_min/2 - kappa >= 101/2 - N.
```

Since `T` is integral, `T>=51-N`. The SAT-CROSS target for an outright Moh
closure is `tau<=50-N` (`SM:584-590`, `SM-R:377-386`). So the target cap is
exactly one integer below the known floor. That statement is correct.

Repair text:

```text
Replace "T<=tau <=> D_min<=2(tau+N)" by
"T<=tau => D_min<=2(tau+N); conversely, D_min<=2(tau+N) is only the
Moh-cross consequence and supplies no T cap."
```

Promotion: promote the one-way SAT-CROSS price and the floor gap. Do not
promote `T-IS-THE-CEILING` as a biconditional.

## 7. T Free / Newton Polygon Typing

Verdict: **CONFIRMED as non-attainment / no-bound typing; not a Keller theorem**.

Charged lines: `MKS:440-449` say `T=sum_C(nu_C-1)c_C`, with `nu_C` a
continuant of satellite-chain data, and that GGV constrains only the first
corner. SAT-MASS states the same definition at `SM:261-278` and retypes
`OPEN[SAT-MASS]` as `OPEN[NU-BOUND]` at `SM:742-746`.

The local replay supports the freedom claim in the ambient dominant category:
`psi_k o (x,xy^3)` keeps the coarse profile `(N,S,W)=(3,1,3)` while producing
`T=0,5,8` for `k=1,2,3`. This is not a Keller counterexample family, so it
does not prove freedom inside the Keller locus. It does prove that the ledger
identities alone do not bound `T`.

GGV primary text supports the claimed first-corner restrictions:
`A_0=(u,v)` has `u+v>=16` by Proposition 6.5 and Corollary 6.6
(`gv.txt:1719-1769`), `u>=4` and `v<=u(u-1)` by Proposition 6.7
(`gv.txt:1772-1786`), and the small case is `A_0=(4,12)`,
`(rho,sigma)=(4,-1)`, `gamma=3`, otherwise `v11(A_0)>20`
(`gv.txt:2307-2310`, `gv.txt:2400-2413`). GGV does not give a promoted bound
on the number of later characteristic pairs or on `T`.

Promotion: promote the typing "`T` is the continuant/satellite-chain integer
and remains `OPEN[NU-BOUND]` for Keller minimal pairs." Do not promote an
unconditional upper bound or any attainment claim.

## 8. Moh-Sharp

Verdict: **CONFIRMED**.

Charged lines: `MKS:451-464`. Primary refs:

* GGV defines `B` as the minimum gcd of total degrees over counterexamples
  (`gv.txt:693-700`) and proves `B>=16` (`gv.txt:1761-1769`).
* Moh searches `deg f=m < deg g=n <= 100` with constant Jacobian and
  simultaneous degree-minimality (`moh.txt:3255-3262`), lists the only possible
  degree pairs below 100 as `(64,68)`, `(84,56)`, `(75,50)`, `(99,66)`
  (`moh.txt:3594-3603`), and concludes no counterexample of degrees `<=100`
  (`moh.txt:3838-3839`).

Together with `MIN`, a degree-minimal counterexample has

```text
deg P = Kd, deg Q = Ke, gcd(d,e)=1, d,e>=2, d!=e, max(d,e)>=3,
K=gcd(deg P,deg Q)>=16.
```

Moh gives `D_min>=101`. Since `D_min=K max(d,e)` with `K>=16` and
`K<=D_min/3`, the first admissible value above Moh's floor is not just any
integer `>=101`; it must have a divisor in `[16,D_min/3]`. Desk arithmetic for
`101<=D<=120` gives exactly

```text
excluded: 101, 103, 106, 107, 109, 113, 118
allowed:  102(17,34), 104(26), 105(21,35), 108(18,27,36),
          110(22), 111(37), 112(16,28), 114(19,38), 115(23),
          116(29), 117(39), 119(17), 120(20,24,30,40)
```

Moh's surviving list cross-checks the arithmetic: `(64,68)` has `K=4` and is
excluded by GGV; `(84,56)`, `(75,50)`, `(99,66)` have `K=28,25,33` and
maximal coprime factor `3`.

Repair: state `D_min>=102` as "Moh floor plus GGV divisibility", not as a
direct consequence of `K>=16` alone. Also keep Moh's `d_s` separate from
`K`; the report does this at `MKS:142-143`.

Promotion: promote `MOH-SHARP`.

## 9. T = T_class and rho_0

Verdict: **CONFIRMED in the repaired subrectangular scope; GAP if stated for
all degree-minimal representatives**.

SAT-MASS review repaired the global formula:

```text
T_ext - T_class = D - sum_level1 a_i - rho_0
```

with `rho_0=Z.E_0=D-sum_{i->0}a_i` (`SM-R:221-239`, `SM-R:475-477`). It also
refuted the unqualified formula without `-rho_0` using
`(x+y^2,y+x^2)`, where `D=2`, `N=4`, `rho_0=2`, and `T=T_class=0`
(`SM-R:248-258`, `SM-R:488-490`).

In the two-sided subrectangular GGV-global-minimal scope, the gauge does make
`rho_0=0`. If the larger coordinate has top form `(x^u y^v)^e`, the two
level-one base points are `[0:1:0]` and `[1:0:0]`, and the level-one
multiplicities are `eu` and `ev`; their sum is `e(u+v)=D`. Hence
`rho_0=D-sum_level1 a_i=0`. Substituting in the repaired SAT-MASS formula gives
`T_ext=T_class`. The replay is consistent: `final.py` reports `T=T_class` on
32 resolved rows and `T>T_class` on the 14 `nu=1` rows; the focused
subrectangular mock rows all have `T=T_class`.

Repair: bind the equality to the repaired gauge and to `T_ext`.

```text
In the GGV two-sided subrectangular gauge, rho_0=0 and there is no
L_infty-tail, so T_ext=T_class. Outside this gauge use
T_ext-T_class=D-sum_level1 a_i-rho_0.
```

Promotion: promote `T=T_class` only in the repaired GGV-global-minimal
subrectangular gauge. Do not promote a global `T_class` replacement.

## 10. Verdict Block

```text
ITEM A  FIRST-FORK
STATUS  CONFIRMED, wording repair.
LINES   MKS:226-255.
REPAIR  Count reduced points at infinity; tangency to L_infty lengthens the
        chain over one point and contributes one final E_0-neighbour.
PROMOTE Yes.

ITEM B  SUBRECTANGULAR GAUGE / CH2 REFUTATION
STATUS  GAP in advertised scope; CONFIRMED for GGV-global minimal pairs.
LINES   MKS:163-180, 259-270, 350-361; GGV gv.txt:693-705, 796-879,
        1454-1462.
REPAIR  Replace "every counterexample / every degree-minimal representative"
        by "a GGV-minimal counterexample realizing B, in the GGV standard
        subrectangular gauge" unless OPEN[SUBRECT-ORBIT-BRIDGE] is closed.
PROMOTE Restricted only. CH2 is false in that gauge, not yet gauge-free.

ITEM C  LF and MIN
STATUS  CONFIRMED.
LINES   MKS:105-128.
REPAIR  None load-bearing.
PROMOTE Yes.

ITEM D  E0-LEAF-CAP and CH2+Moh pricing
STATUS  CONFIRMED as conditional; vacuity inherits Item B's scope.
LINES   MKS:379-386; KPG:554-564; KPG-R:13-18; I13:38-45.
REPAIR  CH2+Moh gives N>=100 if Psi=0 and E_0 leaf. Withdraw the nine actual
        kills after E_0-free gauge; call them conditional/vacuous only in the
        repaired subrectangular scope.
PROMOTE Conditional theorem and N<=99 price. No actual cell kill.

ITEM E  CH1 control refutation
STATUS  CONFIRMED as control-class refutation; GAP if read as Keller
        counterexample refutation.
LINES   MKS:328-343, 391-410.
REPAIR  Say "(x,y+x^k) refutes ambient Psi=0 for Jacobian pairs"; do not say it
        refutes the restricted noninvertible Keller/H2 CH1.
PROMOTE Scope warning only.

ITEM F  T <= tau versus D_min
STATUS  REFUTED for biconditional; CONFIRMED for one-way implication and
        one-unit floor gap.
LINES   MKS:428-438; SM-R:360-390, 470-472.
REPAIR  T<=tau => D_min<=2(tau+N). No converse from HALF-CAP+DEG-SPLIT.
        Moh+HALF-CAP gives T>=51-N, one integer above target T<=50-N.
PROMOTE One-way SAT-CROSS and floor gap only.

ITEM G  T free / continuant data
STATUS  CONFIRMED as OPEN typing.
LINES   MKS:440-449; SM:261-278, 742-746; GGV gv.txt:1719-1786,
        2307-2310, 2400-2413.
REPAIR  GGV bounds first-corner data, not the number of later characteristic
        pairs or T. Ambient examples show ledger freedom; Keller case remains
        OPEN[NU-BOUND].
PROMOTE Typing only; no bound.

ITEM H  MOH-SHARP
STATUS  CONFIRMED.
LINES   MKS:451-464; GGV gv.txt:1761-1769; Moh moh.txt:3255-3262,
        3594-3603, 3838-3839.
REPAIR  Say "Moh floor plus GGV divisibility" for D_min>=102. Keep Moh d_s
        distinct from K.
PROMOTE Yes.

ITEM I  T = T_class in gauge / rho_0
STATUS  CONFIRMED in repaired subrectangular scope; GAP globally.
LINES   MKS:282-291; SM-R:221-239, 248-258, 475-490.
REPAIR  In two-sided subrectangular gauge, sum_level1 a_i=D, hence rho_0=0 and
        T_ext=T_class. Outside that scope use the repaired formula with
        -rho_0.
PROMOTE Restricted only.
```

## 11. Open Items

`OPEN[SUBRECT-ORBIT-BRIDGE]`. Does every Aut x Aut degree-minimal
counterexample admit a source automorphism to the GGV standard subrectangular
form while preserving both total degrees? Bounded quantity: the ordered degree
pair `(deg P,deg Q)` inside one Aut x Aut orbit, and the resulting
`nu in Z_{>=1}`.

`OPEN[NU2-RIGIDITY]` remains as in the producer (`MKS:596-600`): is `nu=2`
forced in every degree-minimal gauge, or only in the GGV subrectangular gauge?
Bounded quantity: `nu`, the number of reduced roots of the top form at a
degree-minimal representative.

`OPEN[NU-BOUND] / OPEN[SAT-MASS]` remains as in SAT-MASS (`SM:742-746`):
bound `nu_C=ord_C(sigma^*L_infty)` on non-contracted boundary components by a
function of `N`, equivalently bound `T=sum_C(nu_C-1)c_C`.

`OPEN[FORK-MULT]` remains as in `MKS:589-594`: bound the polar multiplicities
`m_C` at contracted forks with `Z.C=0`, especially the `N=4` B3 boundary
cluster with `E_0` free and `m_{E_0}=D>=102`.

## 12. FALLACY-v2 Audit

Flag/place/series are separated: `nu` is reduced top-form support on
`L_infty`; `nu_C` is source polar multiplicity/continuant data. Tangency is
strict-below chain length, not extra at-level flags.

Carrier/attainment and floor/attainment are separated. Moh and HALF-CAP are
floors; they do not produce a `T` cap. The SAT-CROSS cap is conditional and
has no witness of attainment.

Pole/interior is checked: `rho_0=0` is used only after either `D>N` via
SAT-MASS Lemma L4 or the direct subrectangular computation
`sum_level1 a_i=D`.

No `sat()` wrapping, raw-remainder normal form, prime-label derivative, or
merge-free/M-descent argument is used. Variable/ring map for replay is
`QQ[x,y]`, with the driver resolving the homogenised net
`<z^{D-dP}P^h,z^{D-dQ}Q^h,z^D>` by exact rational blow-ups.

No exit claim is made; no `charge_basis` line is required.

<!-- BODY-END -->
