# Hostile review: `C74-PLACE`, `EXIT-RPMC(C)`, and the anti-standard same-pair claim

**Reviewer lane:** Opus 5 (model ID `claude-opus-5`), different-model hostile
mathematical referee.  Producer lane of both targets: Sol Ultra.  Independent
predecessor reviewer lane: Fable 5.
**Date:** 2026-08-27
**Targets (fail-closed gate, rehashed at session start):**

```text
xmodel/g2-antistandard-same-pair-source-audit-sol-ultra-20260827.md
    41e3748437f90c0214c424be650ba0c78825117e7e1ffe7575195b3cf2e83ed0   MATCHES (required)
xmodel/g2-pure-sigray-bypass-after-transpose-sol-ultra-20260827.md
    9147ada2c1704a2df10139d79f4863adee53006a6195b9a893f5bd9c343a8e83   MATCHES (required)
xmodel/g2-transpose-equivariance-hostile-review-fable5-20260827.md
    097db69b89bcd25e6ac3181680f6a3da4f804714062865bdc8fd8b765af6c1dc   MATCHES (required)
```

Gate passed; the Fable5 review was read only after hashing.  Below, "AUDIT"
= the anti-standard source audit (`41e37484...`), "BYPASS" = the pure-Sigray
report (`9147ada2...`), "FABLE5" = `097db69b...`.

---

## Headline

**The load-bearing negative half of AUDIT is CONFIRMED and STRENGTHENED.  Its
positive half — that VGG Corollary 7.4 supplies same-fixed-pair information on
"the physical other side" — is REFUTED by a subsumption theorem proved below:
for live `8_28` the anti-chart Corollary-7.4 packet is the signed-transpose
image of a *native-chart* Corollary-7.2 packet on the *same physical Newton
edge* (global `(-3,1)` = the frozen `upper_dir`), a packet VGG itself deploys
inside the proof of Theorem 7.6(5).  It is strictly weaker than the native one
and carries no `y=infinity` chart content.**

Four further results:

1. **Custody REFUTED (targeted).**  AUDIT §8's two arXiv TeX SHA-256 values are
   **wrong**, and wrong in the signature pattern of reconstruction rather than
   of a different file: each agrees with the true value on a 7--8 hex-character
   prefix and then diverges.  All four repository pins in the same section are
   correct.  Exactly the two hashes requiring an external fetch are false.
2. **`EXIT-RPMC(C)` is not a cheaper successor to `RPMC(C)`** — given its own
   first clause the two are *equivalent*, not merely one-way.  Its advertised
   value is localization, not proof cost.  GAP.
3. **The new Riemann--Hurwitz finite-end balance (BYPASS §4) is CONFIRMED**, in
   full, with its hypotheses made explicit.  It is the only completely proved
   new mathematics in either target.
4. **`(m,n) = (alpha,beta)` in BYPASS §3.2 is component-swapped**: the frozen
   record's native orientation is `P=g`, `Q=f`, so `(m,n) = (beta,alpha) =
   (3,2)` while `(alpha,beta) = (2,3)`.  The zero-mismatch conclusion survives
   only because the component-sort bit is tracked.

Nothing here promotes `G2-PSC`, landing, coverage, a degree ceiling, a family
exclusion, `C74-PLACE`, `EXIT-RPMC(C)`, or JC2.  No canonical ledger or
producer artifact was edited.

---

## 0. Evidence base and custody

### 0.1 Primary sources, re-fetched and hashed this session

```text
arxiv.org/e-print/1401.1784  (gz)  e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0
  -> gunzip "Jacobiano14diciembre2015.tex"  (6815 lines)
     vgg.tex   b4908fd596d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5
arxiv.org/e-print/1708.07936 (gz)  2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e
  -> gunzip "Some_algorithms_related_to_the_Jacobian_Conjecture_26_de_agosto_de_2017.tex"
     ggv5.tex  8f5571e527c4e579b185f7e75dcf48cd6c92fa88c82c46c33019d38ab89d78f5
```

All four reproduce FABLE5 §0 byte-for-byte.  My review and FABLE5 therefore
read identical primary text.

### 0.2 AUDIT §8 hash slate — **REFUTED** (two of six)

| item | AUDIT §8 claim | true value (this session) | verdict |
|---|---|---|---|
| VGG TeX | `b4908fd5`**`351210562958ad81ab13dddaee2c257a55362930f68790d0e234724d`** | `b4908fd5`**`96d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5`** | **REFUTED** |
| GGV5 TeX | `8f5571e`**`b5fb5c594a9be47972e6331a3d0b6492edb6b44718ec102ae92dc1453`** | `8f5571e`**`527c4e579b185f7e75dcf48cd6c92fa88c82c46c33019d38ab89d78f5`** | **REFUTED** |
| prototype `verify_r1.py` | `7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5` | identical | CONFIRMED |
| prototype frozen result | `deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd` | identical | CONFIRMED |
| `lib/families.py` (via FABLE5) | `729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e` | identical | CONFIRMED |

Two independent SHA-256 values cannot share an 8-hex and a 7-hex prefix with
the truth by chance (`~2^-32` and `~2^-28`).  The pattern is a hash
*reconstructed from context* rather than *computed from a fetched file*.  The
predecessor audit `g2-transpose-equivariance-hostile-audit-sol-ultra-20260827.md`
(`e31ed8b6...`) records the **correct** values at its lines 485/487; AUDIT
almost certainly inherited the source text through that lane and re-emitted
the digests from memory.

**Consequence for this review:** AUDIT's statement "Primary VGG source read
from arXiv:1401.1784v3; downloaded source `vgg.tex` SHA-256 ..." is not
supported.  I therefore re-verified **every** technical source claim in both
targets against my own fetch; results are reported per item below.  Ironically,
the *content* of AUDIT's source claims is almost entirely accurate (labels,
hypotheses, numbering), which is further evidence of inheritance rather than
invention.  **Repair:** replace the two digests with the values in §0.1 and
mark the fetch as inherited from `e31ed8b6...`, not performed.

### 0.3 A cited regression no longer runs

AUDIT §7.2 asserts that
`cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py`
"passed in about 0.06 seconds with `mathematical_result_unchanged=true`".

In the tree as I found it, that script **fails closed**:

```text
AssertionError at verify_r1.py:30
  digest(ROOT/"ladder/TRANSPORT.md") == TRANSPORT_R1_SHA256
```

`ladder/TRANSPORT.md` has now drifted to a **third** state:

```text
39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624   pinned by frozen verify.py (= git HEAD)
9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c   pinned by verify_r1.py (= what FABLE5 saw)
9e23c5e79a5af2dc207e49481bbaf151173391c558ec86ddb4fae44603a0d297   live working tree, this session
```

This is concurrent-lane drift, not necessarily a false claim by AUDIT; but the
cited evidence is **not currently reproducible as cited**.  I reproduced the
mathematics independently by an in-memory replay that pins the frozen
`verify.py` (`4dfe7c6d...`, matches) and substitutes only the live
`TRANSPORT.md` digest, writing nothing to disk:

```text
replay 0.03 s   math-equal(excluding source_pins) = True
y_infinity: places 16, ramification_per_place 1,
            baseline_tau_1_pole_orders {12:16},
            mutation_tau_2_pole_orders {11:1, 12:15},
            fibre_equation X^2*(X-t)^14-1-a*t^8-X*t^11  (t=0: X^16-1)
x_infinity: pi [1/4, 9/28], presentations 56, deck_orbits 2,
            ramification_per_place 28, pole_order_per_place 42, pole_mass 84
non_keller_witness: Jac(f,g_1)|_{x=0} = -12 y^11 + 8 y^22
```

So AUDIT §7.2's numbers and FABLE5 §6's independent census are both
**CONFIRMED**; only the custody wrapper is stale.  **Repair:** emit an `R2`
wrapper pinning `9e23c5e7...`, or freeze `TRANSPORT.md` before citing this
regression again.

### 0.4 Numbering, independently re-derived

Comment-aware environment count over `vgg.tex` (all theorem-like environments
share one per-section counter; `\newtheorem{theorem}{Theorem}[section]`,
lines 70--82), sections resolved at lines 299/506/1181/1461/1889/3123/3775/5001:

```text
2.1  P y Q alineados            2.3  extremosalineados        2.6  central
6.8  remark (psi_1, psi_2)      6.9  impossibles
7.1  proporcionalidad de direcciones mayores   7.2  fracciones de F
7.3  proporcionalidad de direcciones menores   7.4  fracciones de F1
7.5  direcciones intermedias positivas         7.6  divisibilidad
7.7  multiplicidad de la potencia              7.8  factores
```

This confirms AUDIT's and BYPASS's citations, including BYPASS §3's
"Theorem-2.6 rationality hypothesis" (`central` **is** 2.6).  `L := K[x,y]`
(line 175), `L^(l) := K[x^{+-1/l}, y]` (line 181),
`V_{>=0} = {rho+sigma >= 0}`, `V_{>0} = {rho+sigma > 0}` (lines 310--318).

---

## 1. Question 1 — Conjecture A as abstract conjugation; the anti-standard input sign

### 1.1 "Passes clausewise **only** as abstract conjugation" — **CONFIRMED, STRENGTHENED**

FABLE5 verified all fourteen GGV5 Theorem 2.20 clauses and VGG 5.17/5.18/(5.9)
under the dictionary.  I do not re-litigate that count; I attack the *modality*.

The proof method in AUDIT and FABLE5 is transport of structure: define every
y-native notion as the printed notion read in local coordinates `(y,-x)`, then
apply the printed x-theorem to `(tau^{-1}P, tau^{-1}Q)` and conjugate the
witness.  Such an argument proves, for **every** predicate `Phi` in the
transported vocabulary,

```text
    Phi^y(tau P, tau Q)   <=>   Phi^x(P, Q).
```

This is a biconditional, not a one-way transfer.  Therefore no y-native
statement obtained this way can be logically independent of its x-image, and
in particular **no y-native theorem so obtained can constrain a pair beyond
what the x-theory already constrains**.  That is the exact sense in which the
pass is "only abstract conjugation", and it is airtight.  The whole
mathematical content is the *adequacy of the dictionary*, i.e. that the printed
definitions are expressible in the transported vocabulary.

**New primary-source trim (beyond FABLE5).**  FABLE5 credits VGG's proof of
Proposition 4.7 with the "germ" of the flip and the `Succ`/`Pred` conjugation.
The stronger fact is that **VGG Remark 6.8 prints the entire dictionary**, at
`l = 1`, verbatim (`vgg.tex` lines 3657--3684):

```text
psi_1(x) := y,  psi_1(y) := -x,   psi_1 in Aut(L),  L = K[x,y]
"the action induced by psi_1 on the Newton polygon ... is the orthogonal
 reflection at the main diagonal, and so, it maps edges ... into edges ...,
 interchanging st and en."
(cambio de direccion)              bar psi_1(rho,sigma) := (sigma, rho)
(polinomios por cambio de direccion)
        v_{rho_k,sigma_k}(psi_k(P)) = v_{rho,sigma}(P)
   ell_{rho_k,sigma_k}(psi_k(P)) = psi_k(ell_{rho,sigma}(P))
```

That is `TRANSPORT.md` (4.1)--(4.2), AUDIT (1.3)--(1.5), and the `st`/`en`
interchange, all printed.  FABLE5's §12 check list does **not** include Remark
6.8; AUDIT quotes it (its (4.5)) only for the *definitions* of `psi_1, psi_2`.
Neither notes that the same remark contains the load-bearing equivariance.
**Verdict: CONFIRMED WITH REPAIR (attribution).**  What genuinely remains new
in Conjecture A is (i) the extension from `L = K[x,y]` to `L^(l)` and to the
y-cylinder `K[y^{+-1/l}, x]` for `l > 1`, and (ii) the clausewise verification
of GGV5 Theorem 2.20.  The `l = 1` dictionary is primary source.

### 1.2 Does the fixed pair necessarily fail Definition 4.3 in the anti chart? — **CONFIRMED**

I re-derived FABLE5's orientation-disjointness lemma independently and it is
correct.  With `M_i = max i-exponents`, `j* = max{j : (M_i,j) in Supp}`,
`M_j = max j-exponents`, `i_0 = max{i : (i,M_j) in Supp}`: the printed
counterclockwise convention gives `en_{1,0}(P) = (M_i, j*)`, the x-sign
`v_{1,-1}(en_{1,0}(P)) < 0` is `M_i < j*`, the y-local sign is `M_j < i_0`, and
both together give `M_j < i_0 <= M_i < j* <= M_j`.  **CONFIRMED.**

**One precision FABLE5 did not state.**  The negation of the y-condition is
`M_j >= i_0`, i.e. `v^y_{1,-1} >= 0`, *not* `> 0`.  The boundary case
`M_j = i_0` (support maximum attained at a single coordinatewise-maximal
vertex, e.g. a square support) gives sign exactly zero and fails **both**
Definition 4.3 and the Proposition 7.3 hypothesis `b < a/l`.  The disjointness
lemma is unaffected; but the corollary "necessarily satisfies the anti sign" is
*false in general* and needs the next item.

### 1.3 The anti-standard **positive** sign at a transposed regular corner — **CONFIRMED (new, exact)**

The relevant positive sign is not at direction `(1,0)` but at the source
direction.  Reading the printed definitions:

> **Lemma A (sign equivalence).**  Let `(rho_0,sigma_0) in Dir(P)` and let
> `A = (a/l, b) := en_{rho_0,sigma_0}(P)/m`.  Let `w_0 = T(rho_0,sigma_0)`
> with `T(rho,sigma) = (sigma,rho)` (VGG (cambio de direccion)).  Then
> `st_{w_0}(tau P)/m = T A = (b, a/l)`, and Proposition 7.3 / Corollary 7.4
> hypothesis "`b' < a'/l'`" at `w_0` holds **iff** `b > a/l` at
> `(rho_0,sigma_0)` — which is exactly clause (1) of VGG Definition 5.5's
> *regular corner*.

So for every **regular corner** of an `(m,n)`-pair the anti-standard positive
sign is automatic and *strict* (Definition 5.5 prints `b > a/l`).  Live
`8_28`: `A_0 = (8,28)`, `28 > 8`, so `T A_0 = (28,8)` with `8 < 28`.  AUDIT's
"`28 - 8 = 20 > 0`" is correct and, better, forced.  **CONFIRMED.**

**Undisclosed asymmetry (repair).**  Corollary 7.4 hypothesis (2) requires
`(1/m) st_{w_0}(P_y) in (1/l)Z x N`.  Under `T` this becomes, in global terms,
`A in N x (1/l)Z`, i.e. it demands `l | a` in addition to `b in N`.  Corollary
7.2's hypothesis (2) demands only `b in N`.  **For `l > 1` the anti-chart
hypothesis is strictly stronger than the native one.**  Live `8_28` has `l = 1`
at stage 0, so the live instance is unaffected; but the generalisation to later
chain stages (`l = lcm(rho_i, l_i) > 1`) is not free.  Neither target discloses
this.

---

## 2. Question 2 — can any automorphism supply the missing physical infinity chart?

### 2.1 The cylinder classification (AUDIT (4.1)--(4.4)) — **CONFIRMED**

I proved it rather than accepting it.  Let `A = K[u^{+-1}, v] = R[v]`,
`R = K[u^{+-1}]`.  `A` is a domain and `R[v]^x = R^x = K^x u^Z`, so any
`K`-automorphism `Phi` sends the unit `u` to `c u^e`, `e in {1,-1}` (surjectivity
forces `|e| = 1`).  Then `Phi` restricts to `Aut(R)`, and `A = R[Phi(v)]`
forces `deg_v Phi(v) = 1`, i.e. `Phi(v) = alpha(u) v + b(u)` with
`alpha in R^x = d u^k`.  Hence (4.1).  `J(Phi) = e c d u^{e+k-1}` (4.2), constant
iff `k = 1 - e` (4.3), giving exactly the two classes of (4.4).  **CONFIRMED.**

### 2.2 The live chart-preserving no-go (AUDIT §4.2) — **CONFIRMED**

Independently re-derived.  In the flipped `1/m`-frame the frozen start polygon
is `S_y = conv{(0,0),(4,0),(28,8),(0,1)}`, whose unique first-coordinate maximum
is `(28,8)`.  Take `Phi(Y)=cY`, `Phi(V)=dV+b(Y)`, `s :=` top Laurent exponent of
`b` (`-inf` if `b=0`).  A monomial `Y^i V^j` maps into
`span{Y^{i+ts'} V^{j-t}}`, `0<=t<=j`, `s'` a Laurent exponent of `b`.

* `s <= 0`: every image exponent has first coordinate `<= i`, so the maximum
  stays `28m`; terms at first coordinate `28m` arise only from `(28m, 8m)` with
  `s' = 0`, and the top one is `c^{28m} d^{8m} Y^{28m}V^{8m}` (no cancellation).
  Hence `en^{loc}_{1,0} = (28m, 8m)` and the sign is `20m > 0`.
* `s > 0`: `max_{Supp}(i + js)` over the vertices `{0, 4m, 28m+8ms, ms}` is
  `28m + 8ms`, attained only at `(28m, 8m)` with `t = j = 8m`, `s' = s`; the
  V-exponent there is `0` and the coefficient is a single nonzero product.
  Hence `en^{loc}_{1,0} = (28m + 8ms, 0)`, sign `> 0`.

Either way Definition 4.3's `v_{1,-1}(en_{1,0}) < 0` fails.  **CONFIRMED.**

### 2.3 `psi_2`, swaps, inversion — **CONFIRMED verbatim**

Against `vgg.tex` Remark 6.8: `psi_2(x) = -x^{-1}`, `psi_2(y) = x^2 y`,
`bar psi_2(rho,sigma) = (-rho, 2 rho + sigma)`, monomial action `(a,b) ->
(-a+2b, b)` (determinant `-1`, hence the printed `st`/`en` interchange).  All
of AUDIT (4.5)--(4.6) and BYPASS (2.1)--(2.3) are literal.  Jacobian of `psi_2`
recomputed: `x^{-2}*x^2 - 0 = 1`.  The three obstructions in AUDIT §4.3 check:
`bar psi_2(-1,4) = (1,2)`; requiring outputs `(1,0)` and `(1,1)` forces inputs
`(-1,2)` and `(-1,3)`, i.e. global `(2,-1)` and `(3,-1)`; and neither lies in
Proposition 7.1's interval `I_0 = [(4,-1),(0,-1)[` (angles `333.4` and `341.6`
degrees, both strictly *below* the source `345.96` in the counterclockwise arc).
VGG Proposition 6.9's proof indeed uses exactly `bar psi_1(2,-1) = (-1,2)` and
`bar psi_2(-1,2) = (1,0)`.  **CONFIRMED.**

### 2.4 **GAP: the classification does not answer the question asked**

Question 2 asks about "any polynomial/Laurent symplectic automorphism".  AUDIT
§4.1 classifies automorphisms of the **Laurent cylinder** `K[u^{+-1}, v]` only.
The Jacobian-one subgroup of `Aut(K[x,y])` is far larger — by Jung--van der
Kulk it is the amalgamated product of the affine and triangular subgroups, and
`x -> x + p(y)` with `deg p >= 2` is Jacobian-one but does **not** act on
`K[x^{+-1}, y]`.  AUDIT §4.4's table enumerates a fixed four-item menu (swap,
signed rotation, component swap, inversion) and does not cover this.

Two honest statements replace the missing one:

* **(2a)** If the pair is required to be *literally unchanged*, the question is
  vacuous: an automorphism that relocates a `y=infinity` place into a native
  `x=infinity` chart necessarily changes the pair to `(P o phi, Q o phi)`.  The
  only content is then which *re-selected* pairs are reachable.
* **(2b)** FABLE5's disjointness lemma does **not** block re-selection.  For
  `phi in Aut(K[x,y])`, `phi` induces an isomorphism `f^{-1}(a) -> (f o
  phi)^{-1}(a)`, hence a *bijection* on boundary places; only the chart label
  (which coordinate is the Laurent one) can change.  So a re-selected pair can
  be x-standard *and* its native chart can contain the images of the old
  `y=infinity` places.  The disjointness lemma forbids one pair from being
  x- and y-admissible simultaneously; it says nothing about two different pairs.

**Verdict: AUDIT §4.1--§4.4 CONFIRMED as stated but INSUFFICIENT for Question
2; the residual obligation is exactly FABLE5 §11's chart tracking through van
den Essen Corollary 10.2.21 / VGG 4.7 / 5.20 / 5.21.**  Neither target should be
read as having closed it.  I did not attempt vdE 10.2.21 here.

---

## 3. Question 3 — VGG 7.3/7.4, paired common powers, and the exponents 12 and 8

### 3.1 What is in the *statement* — read verbatim

Proposition 7.3 (`vgg.tex` 4192--4234) hypotheses: `m,n` coprime `> 1`;
`P,Q in L^(l)`; `[P,Q] in K^x`; **`v_{1,1}(P)/v_{1,1}(Q) = v_{0,1}(P)/v_{0,1}(Q)
= m/n`** (note `(0,1)`, where Proposition 7.1 has `(1,0)`); `T_0 in K[P,Q]`,
`T_j := [T_{j-1},P]`; `(rho_0,sigma_0) in V_{>=0}` with (1) `in Dir(P)` and
`v>0`, (2) `st(T_j) ~ st(P)`, (3) `st(P)/m = st(Q)/n in (1/l)Z x N`, (4)
`b < a/l`.  Interval `I_1 := [(0,-1), (rho_0,sigma_0)]`, `(tilde rho, tilde
sigma) := min{... : v_{rho',sigma'}(P) > 0 throughout}`.  Conclusion for
`(tilde rho,tilde sigma) <= (rho,sigma) < (rho_0,sigma_0)`: bracket vanishing
plus constant valuation ratio.  Proof, in full: *"Mimic the proof of
Proposition 7.1."*

Corollary 7.4: same ratio hypotheses; (1) `Dir`+positivity, (2) `st(P)/m =
st(Q)/n in (1/l)Z x N`, (3) `b < a/l`; `F` the `(rho_0,sigma_0)`-homogeneous
element of **Theorem 2.6**; **if** there are coprime `p,q in N` with
`st_{rho_0,sigma_0}(F) = (p/q)(a/l,b)`, **then** for every `(rho,sigma)` in the
same half-open interval there is a homogeneous `R` with
`ell_{rho,sigma}(P) = R^{qm}`.  Proof, in full: *"Mimic the proof of Corollary
7.2."*

AUDIT (2.1)--(2.5) reproduce this correctly, including the `(0,1)` ratio.
**CONFIRMED.**  Three scope facts AUDIT states correctly and must not be
softened: the conclusion is **strictly below** `rho_0` (the corner face itself
is *not* certified); only `P` appears; no scalar appears.

### 3.2 What follows only from the *proof* — **CONFIRMED WITH REPAIR**

The paired form is genuinely there, in the proof of **Corollary 7.2**
(`vgg.tex` 4110--4190).  Applying Proposition 7.1 with `T_0 = G_0, G_1, Q` and
then VGG Proposition 2.1(2b), the proof writes a common primitive `R_0` with

```text
v(R_0)(u_0,u_1,u_2,u_3) = (v(G_0), v(G_1), v(P), v(Q))
                        = (v(P)/(sqm)) * (rqm, rqm+sqm-ps, sqm, sqn),
d := gcd(rqm, rqm+sqm-ps, sqm, sqn) = gcd(qm, s),   d | s,
so   u_2 = sqm/d   and   u_3 = sqn/d.
```

Hence with `S := R_0^{s/d}`:  `ell(P) = gamma_2 S^{qm}`, `ell(Q) = gamma_3
S^{qn}`, **same `S`**.  AUDIT's `u_P = qm*s/d`, `u_Q = qn*s/d` is exact, and its
insistence on separate scalars `alpha, beta` in (2.5a) is correct: the printed
absorption `gamma^{qm} = gamma_2` cannot simultaneously satisfy
`gamma^{qn} = gamma_3`.

**Repair (attribution).**  AUDIT says the companion is in "its proof", meaning
Corollary 7.4's.  Corollary 7.4's printed proof is one sentence.  The correct
statement is: *the paired form is printed in the proof of Corollary 7.2 and
reaches the anti side only through 7.4's "mimic" instruction*, which is a
proof-obligation transfer, not a printed derivation.  Anyone promoting (2.5a)
on the anti side owes the executed mimic.

### 3.3 Are the live exponents exactly 12 and 8? — **CONFIRMED, and forced**

New exact determination (not in either target).  `F` is
`(rho_0,sigma_0)`-homogeneous with `v_{rho_0,sigma_0}(F) = rho_0 + sigma_0`
(Theorem 2.6, first display of `eq central`).  Combining with the alignment
hypothesis `st(F) = (p/q)(a/l,b)` and `v(a/l,b) = v_{rho_0,sigma_0}(P)/m`:

```text
        p/q  =  m (rho_0 + sigma_0) / v_{rho_0,sigma_0}(P).                (*)
```

Frozen live record (`lib/families.py`, hash `729a5ee7...`, read this session):
`A_0=(8,1,28)`, `A'_0=(1,0)`, `steps=((4,-1,3,4),)`, `(m,n)=(3,2)`,
`degP=108`, `degQ=72`, `S=((0,0),(1,0),(8,28),(0,4))`, `upper_dir=(-3,1)`.
Then `rho_0+sigma_0 = 3` and `v_{4,-1}(P) = m(32-28) = 12`, so
`(*)` gives `p/q = 9/12 = 3/4`, `gcd(3,4)=1`, hence **`q = 4`**, matching the
frozen `steps` value.  The transposed frame gives the same numbers
(`(-1)+4 = 3`, `v_{-1,4}(P_y) = m(-28+32) = 12`).  Therefore

```text
        qm = 12   (on P),        qn = 8   (on Q).
```

**Moreover the alignment is a theorem, not a hypothesis, here.**  VGG **Theorem
7.6(3)** prints: *for all `j > 0` the element `F_j` constructed via Theorem 2.6
satisfies `en_{rho_j,sigma_j}(F_j) = (p_j/q_j)(1/m) en_{rho_j,sigma_j}(P)` with
`p_j, q_j` coprime; if `A_0` is of type II, this holds also for `j = 0`.*  Live
`8_28` has a type-II.b corner at `(4,-1)`, so `(p_0,q_0) = (3,4)` is
theorem-backed and Theorem 2.6(2)'s alternative branch `st(F) = (1,1)` is
excluded.  **CONFIRMED.**  (Consistency cross-check: on the certified face
`v(P)/m = v(Q)/n = 4`, `v(R) = 1`, `12*1 = 12 = v(P)`, `8*1 = 8 = v(Q)`; and
`en(R) = (7,2)` has `v_{1,-3}(7,2) = 1`.  All four agree.)

Two scope guards AUDIT does not state:
* **VGG Proposition 7.8(3)** applies live (`A_0 = (1,0) + 7(1,4)`, `sigma_0=-1`,
  `A'_0=(1,0)`, `gcd(7,4)=1`) and concludes `ell_{4,-1}(P)` is **at most an
  `m`-th power** — a *cube*, not a 12th power.  The `R^{12}` lives only on the
  faces strictly past the corner.  The reducer log's phrase "on the Pred faces"
  is the correct scope; "on every face in the certified positive interval" must
  never be read as including `w_0`.
* Theorem 7.6(4) prints `q_i` does not divide `d_i`; the 12th power is not
  claimed maximal at the corner.

### 3.4 **REFUTED: this is not the other infinity chart.  Subsumption theorem.**

> **Theorem S (transpose subsumption).**  Let `(P,Q)` with `[P,Q] in K^x`, let
> `tau` be the signed transpose and `T(rho,sigma) = (sigma,rho)` (VGG
> (cambio de direccion)).  Then, at `w_0 := T(rho_0,sigma_0)`:
>
> 1. the hypotheses of Proposition 7.3 / Corollary 7.4 for `(tau P, tau Q)`
>    hold **iff** the hypotheses of Proposition 7.1 / Corollary 7.2 for
>    `(P,Q)` at `(rho_0,sigma_0)` hold — with one exception: hypothesis (3)/(2)
>    is *strictly stronger* on the anti side, additionally requiring `l | a`;
> 2. the certified global arc satisfies `tau(I_1) = [(rho_0,sigma_0), (-1,0)]
>    (strictly contained in) I_0 = [(rho_0,sigma_0), (0,-1)[`;
> 3. hence the `tau`-image of every 7.3/7.4 conclusion is already a
>    consequence of 7.1/7.2 applied natively, and 7.1/7.2 certifies a strictly
>    larger arc.

*Proof.*  Termwise, `x^i y^j -> +- V^i Y^j`, so the global exponent `(i,j)` has
local record `(j,i)`; hence `v^{loc}_{1,1} = v^{glob}_{1,1}` and
`v^{loc}_{0,1} = v^{glob}_{1,0}` — this is exactly the `(0,1)`-vs-`(1,0)`
difference between 7.3 and 7.1, so the ratio hypotheses correspond.  `T`
negates cross products, so `st^{loc}_{Tw}(tau F) = T en^{glob}_w(F)` and the
direction order reverses; brackets and `K[P,Q]` are `tau`-equivariant, so
`T_j^{loc} = tau(T_j)`.  Proportionality is `T`-invariant, giving 7.3(2) <->
7.1(2).  `T(a/l,b) = (b,a/l)` turns `b < a/l` into `b > a/l`, giving 7.3(4) <->
7.1(4); membership `in (1/l)Z x N` maps to `in N x (1/l)Z`, whence the extra
`l | a`.  `rho+sigma` is `T`-invariant, so `V_{>=0}` is preserved.  Finally
`T(0,-1) = (-1,0)`, and on the counterclockwise circle `(-1,0)` (180 deg)
precedes `(0,-1)` (270 deg) in the arc starting at `(rho_0,sigma_0) in
V_{>=0}`; hence (2), and (3) follows since `(tilde rho, tilde sigma)` is a max
over a subset.  QED

**Live instantiation.**  Independent Newton-polygon computation (my own hull
and outer-normal code, no campaign library):

```text
global  S   hull CCW (0,0)(1,0)(8,28)(0,4):   Dir(P)   = {(0,-1), (4,-1), (-3,1), (-1,0)}
                                              v>0 only at (4,-1) and (-3,1)   [v = 4, 4]
local   S_y hull CCW (0,0)(4,0)(28,8)(0,1):   Dir(P_y) = {(0,-1), (1,-3), (-1,4), (-1,0)}
                                              v>0 only at (1,-3) and (-1,4)   [v = 4, 4]
```

Native Corollary 7.2 at `(4,-1)`: `(tilde rho, tilde sigma) = (-3,1)` (the next
`Dir` element is `(-1,0)` with `v = 0`), certifying `((4,-1), (-3,1)]`.
Anti Corollary 7.4 at `(-1,4)`: `(tilde rho, tilde sigma) = (1,-3)`, certifying
`[(1,-3), (-1,4))`.  **`T(1,-3) = (-3,1)`: one and the same physical Newton
edge**, namely the edge from `(8,28)` to `(0,4)` whose outer normal is the
frozen `upper_dir = (-3,1)`.  Each certified interval contains exactly one
element of `Dir`, and they correspond.

**And VGG itself already runs the native version.**  The proof of Theorem
7.6(5) reads: *"Thus the hypotheses of Corollary 7.2 are satisfied with
`(rho_0,sigma_0) = (rho_j,sigma_j)` and `(rho,sigma) = (rho_i,sigma_i)`, and
hence `R_i^{m d_i} = ell_{rho_i,sigma_i}(P) = R^{m q_j}`."*  The `R^{m q_0} =
R^{12}` face-power certificate on the native upper side is therefore printed
primary source deployed by VGG, not new anti-side information.

**Verdicts.**
* AUDIT §0.3 "VGG Proposition 7.3 and Corollary 7.4 are already a genuine
  theorem on the opposite side of the *same fixed Keller pair*" — **CONFIRMED
  only under the reading "opposite side of the Newton polygon"; REFUTED under
  the reading "other infinity chart"**, which the report's own title, §0.2,
  §1 heading ("The exact same-pair opposite chart") and §2.2 invite.
* AUDIT §2.2 "Corollary 7.4 gives a theorem-backed root core **on the physical
  other side**; it is not merely a support analogy" — **REFUTED as worded.**
  The face is the native `upper_dir` face, which AUDIT's own (2.9) discloses two
  sentences earlier.  The certificate is real; its location is native.
* AUDIT §5 "Corollary 7.4 has already paid for the hardest face-algebra input
  needed **on the opposite side**" — **REFUTED**: the payment was already made
  natively by Corollary 7.2, and the anti route pays *more* (the `l | a`
  integrality, the smaller arc).
* AUDIT §0.4's scope table ("what 7.3/7.4 supplies") — **CONFIRMED row by row**;
  every "no" is correct, and the row "same fixed pair in the `y` cylinder: yes"
  should be re-labelled *"same fixed pair, native upper directions, transposed
  presentation"*.
* `ladder/REDUCTION.md`'s current "Transpose discriminator" entry is more
  careful than AUDIT (it says "narrower same-pair opposite-**side**
  common-power corridor" and separately that the theorem "produces the other
  chart of a conjugated pair, not the missing chart of the fixed pair").  It
  still needs Theorem S folded in, but its verdict labels are not falsified.
  Filing is a producer action; I did not edit it.

### 3.5 The reducer quote — **CONFIRMED faithful, with one precision**

I re-ran `reduce_family(section4_families()['8_28'])` (desk scale, seconds):
`reduced 2`, and the log contains

```text
R1/R2: Cor 7.4 at flipped chain edge 0, dir (-1, 4), q=4:
       l(P) = lam R^4m on the Pred faces, en(R) = (7, 2) (lattice ok)
c-derivation: continuations of en(R)=(7, 2) below (-1, 4): [((1,0),(1,-3)), ((3,0),(1,-2))]
c-derivation: (c,0) candidates [4, 12]; GGV5 table value c=4
stageA[0] face (1,0)->(7,2) @(1,-3): shape z^0*[2] admitted ... shape z^0*[1,1] admitted
```

AUDIT §7.1's quote is a faithful paraphrase.  **Precision:** `continuations()`
enumerates *candidate* next faces for the **unknown** reduced polygon, not
faces of the frozen `S`.  Only the first, `st(R)=(1,0)` at `(1,-3)` (`c = 4`),
is realised by the frozen record; `st(R)=(3,0)` at `(1,-2)` (`c = 12`) is a
different hypothetical polygon, and at `(1,-2)` the frozen `P_y` has a
*monomial* leading form.  AUDIT's phrase "the two arithmetically admissible
continuations" is defensible; "The campaign's exact support reduction makes
this concrete" over-reads it.  `en(R) = (7,2)`, `R = Y h(Y^3 V)` with
`deg h = 2`, `h(0) != 0`, residual partitions `[2]`/`[1,1]`, nonzero roots, and
determinant-one cut `V -> V + lambda Y^{-3}` are all **CONFIRMED** by hand
(25 lattice points on the face, spacing `(3,1)`, `h^{12}` of degree 24).

---

## 4. Question 4 — is `C74-PLACE` the narrowest honest obligation?

**Verdict: REFUTED as "narrowest", CONFIRMED as "necessary in substance".**
By Theorem S its declared localization ("deliberately local to the other
chart") is wrong: its Corollary-7.4 input is a native-chart certificate.  Its
*mathematical* content — all-root retention, truncation compatibility,
place bijection, proximity provenance — is chart-agnostic and genuinely owed.
Below I split it into five strictly smaller lemmas with exact hypotheses and
record where each currently fails.

### L1 (face-power custody) — available now, no new mathematics

*Hypotheses:* `(P,Q)` an `(m,n)`-pair in `L^(l)`, a type-II regular corner
`(A_j,(rho_j,sigma_j))`, `v > 0` on the closed run to `(tilde rho, tilde
sigma)`.  *Conclusion:* on every `(rho,sigma) in ((rho_j,sigma_j),(tilde
rho,tilde sigma)]` there is a common primitive `S` with
`ell(P) = alpha S^{q_j m}`, `ell(Q) = beta S^{q_j n}`, `alpha,beta in K^x`.
*Status:* **immediate** from VGG Cor 7.2 proof + Thm 7.6(3) (see §3.2--3.3).
Live: `(rho,sigma) = (-3,1)`, exponents `12` and `8`, `en(S)=(2,7)` globally.
No transpose needed.  This is the honest form of AUDIT's (2.5a).

### L2 (root-set identity and multiplicity conversion) — **repair required**

*Statement:* the roots of the residual of `S` and of `ell(P)` coincide as sets,
and multiplicities satisfy `mult_{ell(P)}(lambda) = q m * mult_S(lambda)`.
*Status:* trivially true, and **necessary**: `C74-PLACE` clause 3 says only
"root multiplicity ... survive every cut" without saying *which*.  Newton
--Puiseux ramification denominators are computed from the multiplicity in the
**defining polynomial's face** (`q m *` the primitive one).  Using `S`'s
multiplicity is an off-by-a-factor-12 error at live `8_28`.  **Repair: name the
convention.**  VGG Remark 7.7 (`multiplicidad de la potencia`) is the printed
tool for the `z -> z^{rho}` substitution and should be cited.

### L3 (`H-TRUNC`, truncation compatibility) — the load-bearing clause; **GAP**

*Exact hypotheses needed, none of which `C74-PLACE` states:*
(i) a coefficient-complete exact Keller realization (live `CornerData` has
none — AUDIT §2.2 discloses this correctly);
(ii) an explicit choice of which component is the fibre carrier `H` (see §6.2:
the frozen native orientation is `P=g`, `Q=f`, so `H = Q`, **not** `P`, and the
face powers certified by L1 are the `q m`-th power of the *other* component);
(iii) the corridor condition `v_{rho,sigma}(H) > 0`, which is exactly what makes
the fibre constant `a` invisible to the face algebra.
*Why it is load-bearing and not free:* the certified interval ends at
`(tilde rho, tilde sigma)`, defined by the failure of `v > 0`, and that failure
is *precisely* the step at which the constant `a` enters and the Puiseux branch
terminates.  So the certificate covers the corridor and stops one step short of
every actual place.  `C74-PLACE` acknowledges this ("Complete each child by the
ordinary all-root Newton--Puiseux algorithm; do not assume that Corollary 7.4
recursively re-applies after the cut") — which is honest, but it means clause 1
is *not* supported by Corollary 7.4 at the only step where a place is
determined.  **GAP, correctly flagged by AUDIT as "the load-bearing clause",
under-specified as to hypotheses.**

### L4 (chart coverage) — **REFUTED for the certified interval alone**

`C74-PLACE` clause 2 asserts every boundary place in the chart "enters one of
the certified first-root children".  For the frozen live polygon this is false
for a countable reason: `Dir(P_y)` intersected with the certified interval
`[(1,-3),(-1,4))` is the **single** direction `(1,-3)`, so there is at most one
first-root family; and `(1,-3)` has `-sigma/rho = 3 > 0`, i.e. `V ~ c Y^3`,
which is *not* a bounded-`V` branch.  Coverage therefore cannot follow from the
certificate; it must come from the exact-pair two-chart constructor (BYPASS
§1.1), which needs no VGG input at all.  **Repair: delete "certified" from
clause 2 and state coverage as an independent exact-pair lemma.**

### L5 (deck / leaf-place bijection / no duplication) — **GAP, needs the Kummer index**

The deck group is the Kummer group of `L^(l') / L^(l)`, `l' = lcm(rho, l)` (VGG
Prop 5.18), acting on `x^{1/l'}`.  `C74-PLACE` clause 2 says leaves modulo "the
full Kummer deck action" biject the places; the exact hypothesis is that the
*reduced branch denominator* equals `l'` at the leaf, which requires the
multiplicity convention of L2 and the tower `l_0 | l_1 | ...` of Theorem
2.20(1).  The prototype gives the only evidence: 56 presentations / 2 deck
orbits / ramification 28 at `x=infinity`, 16 places with ramification 1 at
`y=infinity`.  The `y=infinity` block is where the mutation is visible
(`{12:16}` vs `{12:15, 11:1}`), and its control is explicitly **non-Keller**
(`Jac|_{x=0} = -12y^11 + 8y^22`).  So it certifies the interface, not the
lemma.  **GAP.**

### Consolidated answer to Question 4

`C74-PLACE` is **not** narrowest and is **mislocalized**.  The narrowest honest
decomposition for its stated goal is:

```text
L1  native face-power custody      AVAILABLE (VGG 7.2-proof + 7.6(3))
L2  multiplicity conversion        AVAILABLE, needs a named convention
L3  H-TRUNC in the corridor        OPEN; needs (i)-(iii) above; the terminal
                                   step is outside every VGG certificate
L4  chart coverage                 belongs to the exact-pair constructor,
                                   NOT to any VGG corollary
L5  deck / leaf-place bijection    OPEN; needs the reduced-denominator law
```

and the "other chart" qualifier should be dropped from all five.  The genuinely
missing second-chart object is `C_y(P,Q)` (FABLE5 §4), and Theorem S shows no
part of VGG §7 supplies it.

---

## 5. Question 5 — the generic-fibre finite-end balance

> `sum_{S in N} e_S = td + b_1(f^{-1}(a)) - 1`

**Verdict: CONFIRMED.**  Re-derived independently, line by line.

*Hypotheses (I make each explicit; BYPASS §4 states most but not all):*
`K = C` (or algebraically closed, char 0); `(f,g)` a Keller pair,
`J(f,g) in C^x`; `a` chosen so that `C := f^{-1}(a)` is **irreducible** (a
generic; smoothness is automatic, since `df` never vanishes for a Keller pair
— every fibre is smooth, which BYPASS does not point out and which strengthens
its own statement); `bar C` the smooth projective model, genus `g_C`;
`B = bar C \ C = P (sqcup) N` with `|P| = r_infty`, `|N| = r_0`,
`r = r_infty + r_0 >= 1`; `lambda_S = -ord_S(g) >= 1` on `P`,
`e_S = ord_S(g - g(S)) >= 1` on `N`; `d = deg(g : bar C -> P^1)`.

*Chain:*
1. **Primitivity.** If `f = h(u)`, `deg h > 1`, then `h'` has a root `c`, and
   `{u = c} != (empty)` because `u - c` non-constant cannot be a unit of
   `C[x,y]` (`C[x,y]^x = C^x`); on that set `df = h'(u) du = 0`, contradicting
   `J in C^x`.  **CORRECT** — BYPASS's argument is right, and the surjectivity
   step it leaves implicit is supplied by the unit group.
2. `g` is non-constant on the irreducible `C`, so `d >= 1` and, for generic
   `a`, `d = td(f,g)` (the generic fibre cardinality of `(f,g)`).
3. `g` is regular on `C`, so `g^{-1}(infinity) subset B`, giving
   `sum_{P} lambda_S = d`.
4. `g|_C` is unramified: `dg|_{T_p C} = 0` would force `df ^ dg = 0` at `p`.
   All ramification is in `B`.
5. Riemann--Hurwitz: `2g_C - 2 = -2d + sum_P (lambda_S - 1) + sum_N (e_S - 1)`.
6. Substituting (3): `sum_N e_S = 2g_C - 2 + d + r`.
7. `b_1(C) = 2g_C + r - 1` (needs `r >= 1`), hence
   `sum_N e_S = d + b_1(C) - 1`.  **QED**

*Consequences.*
* "`N` empty `=>` `d = 1` and `b_1 = 0`" — **CONFIRMED** (`d >= 1`, `b_1 >= 0`,
  sum `= 1`); then `r = 1`, `g_C = 0`, `C ~= A^1`, `d = 1` gives an
  isomorphism, and `d = 1` plus Keller gives an automorphism.
* (4.4) `sum_N e_S >= d` — **CONDITIONAL** on `b_1(C) >= 1`, i.e. on the cited
  "dual-pencil endpoint".  I did not verify that; note it is essentially
  Abhyankar--Moh--Suzuki (a generic fibre isomorphic to `A^1` makes `f` a
  coordinate).  Cite it, do not re-derive it inside this lemma.
* (4.5) three-way identity — **CONFIRMED as a consequence** of (1.1) + (1.3) +
  (4.3), inheriting the perimeters of the first two.  I verified the algebra:
  `sum_F a_F b_F / nu_F = d/(alpha beta)` from (1.1); `(1.3)` gives the middle
  term; `(4.3)` gives the right.  I also cross-checked (1.3) against the
  campaign's own promoted statement (`notes.md` 2026-08-23, `E_MR = sum_i E_i`,
  `deg Psi <= C(alpha beta)^2`, `td = deg Psi/(alpha beta)` in
  `ladder/REDUCTION.md` §7.2): consistent.
* `GENERIC-POLE-SATURATION` is correctly self-described as "a clean target, not
  a cheap one".  **CONFIRMED, no promotion.**

*Novelty:* BYPASS says "No literature novelty is claimed."  Correct — this is
the standard pencil Riemann--Hurwitz count.  Its value is that it is **fully
proved**, unlike everything else in either target.

---

## 6. Question 6 — the zero-mismatch corridor and `EXIT-RPMC(C)`

### 6.1 `(3.3)`: `v_{rho,sigma}(P)/m = v_{rho,sigma}(Q)/n` on the corridor — **CONFIRMED**

Take `T_0 = Q` in Proposition 7.3.  Its hypothesis (2) is automatic for this
tower: `T_1 = [Q,P] in K^x` has `st = (0,0)`, proportional to everything with
`mu = 0`, and `T_2 = [T_1, P] = 0`; `st(T_0) = st(Q) ~ st(P)` is hypothesis (3).
The conclusion gives `v(Q)/v(P) = v_{rho_0,sigma_0}(Q)/v_{rho_0,sigma_0}(P) =
n/m` throughout.  **CONFIRMED.**  (Same argument natively for Proposition 7.1;
by Theorem S the corridor is the native one.)

### 6.2 `(3.4)`: proximity transport — **CONFIRMED WITH TWO REPAIRS**

*Repair 1 (closure direction).*  The point-basis inversion is
`m_p = v_p - sum_{q : p -> q} v_q`, the sum running over the points **to which
`p` is proximate** — the parent *and*, for a satellite point, one further
ancestor.  BYPASS §3.2 writes "the string and its parent", which is correct for
free points and **incomplete for satellite points**.  State it as: *the set of
centers on which `(3.3)` is assumed must be closed under the proximity
relation*.  With that, the transform is an invertible integer-linear map, so
`v_p(f)/alpha = v_p(g)/beta` on the closed set gives `R_p/alpha = S_p/beta`,
contributing `0` to `(1.3)`.  **CONFIRMED.**

*Repair 2 (component swap) — the identification `(m,n) = (alpha,beta)` is
wrong as printed.*  The frozen prototype records
`native_orientation: ["P=g=B^3+lower", "Q=f=B^2+lower"]`, and
`degrees = [108, 72]` with `(m,n) = (3,2)`.  Hence `deg f = 72 = B alpha`,
`deg g = 108 = B beta`, `B = 36`, `(alpha,beta) = (2,3)`, and therefore

```text
        (m, n)  =  (3, 2)  =  (beta, alpha),      NOT  (alpha, beta).
```

The zero-mismatch conclusion is unharmed — `v(P)/m = v(Q)/n` with `P = g`,
`Q = f` is exactly `v(g)/beta = v(f)/alpha`, giving `R_p/alpha = S_p/beta` —
but only because the component-sort bit is tracked.  BYPASS §3.2's sentence
"When `(m,n)=(alpha,beta)` are the normalized pair exponents" is
**component-swapped and must be corrected**; the same swap is the reason
`C74-PLACE` clause 3 rightly lists the component-sort bit, and the reason L3(ii)
above matters (`H` is `Q`, the `qn = 8` component, not `P`).

*Residual GAP (not a repair, an obligation).*  `R_p, S_p` are multiplicities of
the two **pencils** at infinitely near points over `L_infinity` in `P^2`,
anchored at the roots of the common leading form `H` (`F_d = xi H^alpha`,
`G_e = eta H^beta`).  The VGG valuations `v_{rho,sigma}` live on a Laurent
cylinder reached by non-polynomial changes of variable, and the live certified
direction `(-3,1)` has `rho + sigma = -2 < 0`, i.e. it is an `x -> 0` valuation
of the cylinder, not obviously a center over `L_infinity` of the original
polynomial pair.  **The identification is exactly `C74-PLACE`'s clause 4 and is
not established.**  Neither target claims otherwise; the corridor result must
not be quoted without it.

### 6.3 Does `EXIT-RPMC(C)` imply a type-relative degree bound? — **CONFIRMED but GAP on the strategy**

*The implication.*  `RPMC(C)` (as filed in `notes.md`): for each proper root
`P_i` of `H` with multiplicity `mu_i`, `sum_i mu_i = B`,
`E_i = (1/2) sum_{p > P_i}(R_p/alpha - S_p/beta)^2 <= C mu_i / B`.  Summing and
using the promoted orthogonal split `E_MR = sum_i E_i` and `(1.3)` gives
`d/(alpha beta) <= C`, i.e. `td <= C alpha beta` — **type-relative only**, as
`ladder/REDUCTION.md` §7.2 already says.  Arithmetic **CONFIRMED**.

*The strategy claim — GAP.*  `EXIT-RPMC(C)` has two clauses: (1) every nonzero
normalized discrepancy lies in a unique subtree rooted at a first exit from a
corridor; (2) for each proper root `P`, the total energy of its exit subtrees is
`<= C mu_P / B`.  Given (1), the energy of `P`'s exit subtrees **is** `E_P`.
Hence

```text
        EXIT-RPMC(C)  <=>  RPMC(C)   (given clause 1),
```

not merely `=>`.  The reformulation therefore removes **no** proof cost from
the hard inequality; its entire value is localization (knowing which centers to
inspect).  BYPASS §5 concedes clause 2 is "the new Keller-specific capacity
inequality", but the framing of `EXIT-RPMC(C)` as a "clean next numerical
theorem" and a "sharper proof organization" over-promises.  AUDIT §6's
"`C74-PLACE + EXIT-RPMC(C)` would give the existing `RPMC(C)` route" is
literally true and, by the equivalence, uninformative about cost.
**Repair: state the equivalence.**  Also note clause (1) is *stronger* than
what corridor-zero gives: corridor-zero says corridor centers have zero energy;
clause (1) additionally asserts that all remaining centers are organized into
disjoint exit subtrees indexed by proper roots — that is the orthogonal-split
statement again, plus a corridor decomposition, and it is unproved.

### 6.4 Cheapest exact discriminator that changes allocation

Ranked by cost, all desk-scale; the first is **already executed in this
review** and is decisive.

* **D1 — the subsumption census (cost: seconds; already run).**  For the frozen
  family record, compute `Dir` and `v_{rho,sigma}` in both frames and compare
  the Corollary-7.2 certified arc `((rho_0,sigma_0), (tilde rho,tilde sigma)]`
  with the `T`-image of the Corollary-7.4 arc.  **Result: identical single face
  (global `(-3,1)`), and `tau(I_1)` strictly inside `I_0`.**  Combined with
  Theorem S this is a *proof*, not a sample: **the anti-standard/Cor-7.4 lane
  emits no center that the native Cor-7.2 lane does not already emit.**
  Allocation consequence: the anti lane's remaining value is exactly zero
  beyond an erratum.  This discriminator is strictly cheaper than AUDIT §7.3's
  proposed generic-quadratic symbolic test, and it fires first.
* **D2 — component-orientation regression (cost: minutes).**  Assert in the
  reducer/prototype that `native_orientation` is carried into every statement
  that names `alpha, beta, R_p, S_p`, and add a red-team case with `P,Q`
  swapped that must change the emitted `(alpha,beta)`.  This is the smallest
  test that would have caught §6.2's swap.
* **D3 — custody R2 wrapper (cost: minutes).**  Re-pin the prototype replay to
  the live `TRANSPORT.md` (`9e23c5e7...`), or freeze `TRANSPORT.md`.  Until
  then AUDIT §7.2's regression cannot be cited.
* **D4 — the only test that could revive the anti lane (cost: 1 primary-source
  read).**  Theorem S is unconditional, so the anti lane can only be revived by
  a *different* pair.  The decisive read is FABLE5 §11's: does van den Essen
  Corollary 10.2.21's normalizing automorphism admit a chart-tracked normal
  form?  "Rigid" kills the whole hybrid route to the second chart; "trackable"
  reduces `G2-PSC` clause (4.0) to gluing.  **This, not `C74-PLACE`, is the
  next allocation.**
* **D5 — `mu_P = 1` one-exit sector of `EXIT-RPMC(C)`.**  Worth doing, but only
  after §6.2's repairs, and with the §6.3 equivalence understood so that no
  cost saving is assumed.

---

## 7. Itemized verdict table

| # | atom | verdict |
|---|---|---|
| C1 | three required target hashes | **CONFIRMED** (3/3 match) |
| C2 | AUDIT §8 VGG TeX SHA-256 | **REFUTED** (true `b4908fd596d5...`) |
| C3 | AUDIT §8 GGV5 TeX SHA-256 | **REFUTED** (true `8f5571e527c4...`) |
| C4 | AUDIT §8 prototype hashes (2) | **CONFIRMED** |
| C5 | AUDIT §7.2 replay "passed" | **GAP** — fails closed now (`TRANSPORT.md` drift); math independently reproduced |
| C6 | AUDIT §7.1 reducer quote | **CONFIRMED** faithful; "continuations" are candidates, not frozen faces |
| C7 | AUDIT/BYPASS numbering (2.1/2.3/2.6/6.8/6.9/7.1--7.8) | **CONFIRMED** by independent comment-aware recount |
| Q1a | Conjecture A passes only as abstract conjugation | **CONFIRMED, STRENGTHENED** (biconditional transport of structure) |
| Q1b | dictionary novelty | **CONFIRMED WITH REPAIR** — VGG Remark 6.8 prints `bar psi_1(rho,sigma)=(sigma,rho)`, `v`/`ell` equivariance and the `st`/`en` interchange at `l=1` |
| Q1c | fixed pair fails Def 4.3 in the anti chart | **CONFIRMED** (disjointness lemma re-derived); boundary case `M_j = i_0` noted |
| Q1d | fixed pair satisfies the Prop-7.3 positive sign | **CONFIRMED (new)** — Lemma A: equivalent to Def 5.5(1) `b > a/l` at the native regular corner |
| Q1e | anti hypothesis is strictly stronger for `l>1` | **NEW FINDING** — requires `l \| a`; undisclosed in both targets |
| Q2a | cylinder automorphism classification (4.1)--(4.4) | **CONFIRMED** (proved via `R[v]^x` and `deg_v`) |
| Q2b | live chart-preserving no-go §4.2 | **CONFIRMED** (both `s<=0` and `s>0` cases re-derived) |
| Q2c | `psi_1`,`psi_2`, direction actions, Prop 6.9 use | **CONFIRMED verbatim** against Remark 6.8 |
| Q2d | scope of §4.1--§4.4 vs the question asked | **GAP** — classifies only cylinder automorphisms; Jung--van der Kulk not covered; residual obligation = vdE chart tracking |
| Q2e | disjointness lemma blocks re-selection? | **REFUTED as a blocker** — it constrains one pair, not `(P o phi, Q o phi)` |
| Q3a | Prop 7.3 / Cor 7.4 statements as reported | **CONFIRMED verbatim**, incl. the `(0,1)` ratio and the strict `< (rho_0,sigma_0)` |
| Q3b | paired `Q` power is proof-only | **CONFIRMED WITH REPAIR** — printed in Cor **7.2**'s proof (`u_2=sqm/d`, `u_3=sqn/d`); Cor 7.4's proof is "mimic" |
| Q3c | exponents exactly 12 and 8 | **CONFIRMED** and forced: `p/q = m(rho_0+sigma_0)/v_{rho_0,sigma_0}(P) = 3/4`; alignment is VGG Thm 7.6(3), not a hypothesis |
| Q3d | separate scalars `alpha, beta` needed | **CONFIRMED** (`gamma^{qm}=gamma_2` cannot also fix `gamma_3`) |
| Q3e | corner face itself is a 12th power | **REFUTED** — VGG Prop 7.8(3) gives at most an `m`-th (cube); the certificate is strictly past the corner |
| Q3f | "genuine theorem on the opposite side of the same fixed pair" | **CONFIRMED only as "opposite side of the Newton polygon"** |
| Q3g | "theorem-backed root core on the physical other side" | **REFUTED** — Theorem S; the face is the native `upper_dir = (-3,1)` |
| Q3h | "Cor 7.4 has already paid the hardest face-algebra input on the opposite side" | **REFUTED** — paid natively by Cor 7.2, which VGG itself invokes in the proof of Thm 7.6(5); anti route pays more |
| Q3i | AUDIT §0.4 supplied/missing table | **CONFIRMED row by row** (one row mislabelled) |
| Q3j | AUDIT §3 "standard sign in the complete chain" table | **CONFIRMED** (not re-derived clause by clause; FABLE5 covers it, and Theorem S makes it moot for this route) |
| Q4a | `C74-PLACE` is narrowest | **REFUTED** — mislocalized; split into L1--L5 |
| Q4b | clause 1 (`H-TRUNC`) load-bearing | **CONFIRMED as load-bearing, GAP as stated** — terminal step lies outside every VGG certificate by construction |
| Q4c | clause 2 (all-place coverage) | **REFUTED for the certified interval** — live certified `Dir` is a single direction with `-sigma/rho = 3 > 0` |
| Q4d | clause 3 (typed custody) | **GAP** — multiplicity convention (`qm x`) and reduced-denominator law unspecified |
| Q4e | proximity/no-duplication output field | **GAP** — the cylinder-to-`L_infinity` identification is unestablished (see 6.2) |
| Q4f | live instance is coefficient-free | **CONFIRMED and correctly disclosed** by AUDIT |
| Q5 | `sum_N e_S = td + b_1 - 1` | **CONFIRMED** (full re-derivation; hypotheses listed; smoothness is automatic for Keller `f`) |
| Q5b | `N` empty `=>` automorphism | **CONFIRMED** |
| Q5c | `(4.4)` `sum_N e_S >= d` | **CONFIRMED conditionally** on the inherited `b_1 >= 1` (AMS-type input) |
| Q5d | `(4.5)` three-way identity | **CONFIRMED** modulo the perimeters of (1.1) and (1.3) |
| Q6a | `(3.3)` on the corridor | **CONFIRMED** (Q-tower alignment automatic) |
| Q6b | `(3.4)` proximity transport | **CONFIRMED WITH REPAIR** — closure must be under "proximate to", not just "parent" |
| Q6c | `(m,n) = (alpha,beta)` | **REFUTED** — frozen orientation gives `(m,n) = (beta,alpha) = (3,2)`, `(alpha,beta) = (2,3)` |
| Q6d | cylinder valuations = pencil point-basis centers | **GAP** — unestablished; `(-3,1)` has `rho+sigma < 0` |
| Q6e | `EXIT-RPMC(C) => RPMC(C)` | **CONFIRMED** |
| Q6f | `EXIT-RPMC(C)` is a cheaper/sharper successor | **GAP** — given its clause 1 the two are *equivalent*; no proof cost removed |
| Q6g | "total degree is supported at the exits" | **CONFIRMED as a conditional**, on `C74-PLACE`; not a theorem |

No atom of FABLE5 is refuted.  Two of its judgements are extended: its
novelty trim (VGG Prop 4.7) should be strengthened to VGG Remark 6.8, and its
disjointness lemma is confirmed but does not block re-selection (Q2e).

---

## 8. Narrowest promotable statements from this review

Only these three are literally proved here.  I promote nothing; filing is a
producer action.

> **T-S (transpose subsumption of VGG §7).**  With `T(rho,sigma)=(sigma,rho)`
> and `tau` the signed transpose: `(tau P, tau Q)` satisfies Proposition 7.3 /
> Corollary 7.4 at `T(rho_0,sigma_0)` iff `(P,Q)` satisfies Proposition 7.1 /
> Corollary 7.2 at `(rho_0,sigma_0)` and, for `l > 1`, additionally `l | a`;
> the `tau`-image of the anti-side certified arc is `[(rho_0,sigma_0),(-1,0)]`,
> strictly inside the native `I_0 = [(rho_0,sigma_0),(0,-1)[`.  Hence VGG §7
> applied to a transposed pair yields nothing beyond VGG §7 applied natively,
> and at live `8_28` both certify the single face with global outer normal
> `(-3,1)` (`= upper_dir`), with `ell(P) = alpha S^12`, `ell(Q) = beta S^8`.
> **No second-chart content.**

> **T-q (forced corridor exponent).**  If `F` is the Theorem-2.6 element at
> `(rho_0,sigma_0)` and `en/st_{rho_0,sigma_0}(F) = (p/q)(1/m)
> en/st_{rho_0,sigma_0}(P)` with `gcd(p,q)=1`, then
> `p/q = m(rho_0+sigma_0)/v_{rho_0,sigma_0}(P)`.  At live `8_28` this gives
> `3/4`, hence `q = 4`, `qm = 12`, `qn = 8`, matching the frozen
> `steps=((4,-1,3,4),)`; the alignment branch is supplied by VGG Theorem
> 7.6(3) for the type-II corner, not assumed.

> **T-RH (finite-end balance).**  For a Keller pair `(f,g)` over an
> algebraically closed field of characteristic zero and a generic `a` making
> `C = f^{-1}(a)` irreducible: `sum_{S in N} e_S = td(f,g) + b_1(C) - 1`, where
> `N` are the boundary places at which `g` has a finite value, `e_S =
> ord_S(g-g(S))`, and `b_1(C) = 2g_C + r - 1`.  In particular `N = (empty)`
> forces `td = 1`, i.e. an automorphism.

Explicitly **not** promoted: `G2-PSC`, `C74-PLACE` (any clause), `EXIT-RPMC(C)`,
`RPMC(C)`, landing, coverage, `G2-BD`, any degree ceiling, any family
exclusion, any counterexample, JC2.

---

## 9. Allocation recommendation (narrow)

1. **Close the anti-standard / Corollary-7.4 lane at zero.**  T-S is
   unconditional; the lane is provably subsumed by the native Corollary 7.2 the
   campaign already holds.  One erratum on AUDIT (§0.3, §2.2, §5 wording,
   §8 hashes) and a one-line fold into the `REDUCTION.md` "Transpose
   discriminator" paragraph are the only remaining work.
2. **Re-file the useful content natively.**  Replace `C74-PLACE` by L1--L5 of
   §4, dropping "other chart" throughout and adding the L2 multiplicity
   convention and the L3(ii) component identification (`H = Q = f`).  L1 is
   available today; L4 belongs to the exact-pair constructor, not to VGG.
3. **Run D1--D3 (§6.4) before anything else.**  D1 is done; D2 and D3 are
   minutes and both guard live defects found here.
4. **Make D4 the next real allocation.**  Only van den Essen chart tracking can
   change the second-chart verdict; VGG §7 provably cannot.
5. **Treat T-RH as the deliverable of the BYPASS lane.**  It is the one fully
   proved new item; file it with the §5 hypothesis list and the AMS dependency
   for `(4.4)` named, and add the finite-valued ends to the intrinsic target as
   BYPASS §6.4 recommends.
6. **Do not expect `EXIT-RPMC(C)` to be cheaper than `RPMC(C)`.**  Budget it as
   `RPMC(C)` with better localization; attack the `mu_P = 1` sector only after
   the §6.2 repairs.

---

## 10. Checks, identity, custody, scope firewall

**Model identity.** Opus 5, exact model ID `claude-opus-5`, acting as a
different-model hostile mathematical referee.  No sub-agent, no `ultrareview`,
no delegated review was invoked.

**Checks run this session.**
* Fail-closed rehash of all three required targets (3/3 MATCH).
* Read-only arXiv fetch of both e-prints; decompression; independent SHA-256 of
  both `.gz` and both `.tex`; comparison against AUDIT §8 (2 REFUTED) and
  FABLE5 §0 (4/4 MATCH).
* Independent comment-aware re-derivation of VGG's per-section theorem
  numbering; verbatim reads of Prop 2.1/2.3, Theorem 2.6, the preliminaries
  (`V`, `V_{>=0}`, `v`, `ell`, `st`/`en` + cross-product remark, interval/order),
  Remark 6.8 with `cambio de direccion` and `polinomios por cambio de
  direccion`, Prop 6.9 head and proof head, Prop 7.1 statement + proof head,
  Cor 7.2 statement + **full proof**, Prop 7.3 + Cor 7.4 statements + proofs,
  Remark 7.5, Theorem 7.6 clauses (2)--(8) + full proof, Remark 7.7, Prop 7.8.
* Hand algebra: the `p/q` identity `(*)`; Lemma A; Theorem S in full; the
  `l | a` asymmetry; the `Aut(K[u^{+-1},v])` classification; the two-case live
  no-go; the `psi_2` monomial/direction action and the `(2,-1)`,`(3,-1)` input
  requirement; the `25`-lattice-point face and `R = Y h(Y^3V)`, `deg h = 2`;
  the `v(P)=12`, `v(Q)=8`, `v(R)=1`, `en(R)=(7,2)` consistency square; the
  Riemann--Hurwitz chain (1)--(7) of §5; the `E_MR` / `(1.3)` / `td` consistency
  against `notes.md` and `ladder/REDUCTION.md` §7.2; the `(alpha,beta)=(2,3)`
  vs `(m,n)=(3,2)` swap.
* Small exact computations (desk scale, seconds, no CAS): my own convex-hull /
  outer-normal census of `S` and `S_y`; the frozen `CornerData` record; one run
  of `reduce_family(section4_families()['8_28'])`; an in-memory replay of the
  frozen prototype `verify.py` with the live `TRANSPORT.md` digest substituted
  (`math-equal = True`, `0.03 s`, nothing written).
* Repository pins rehashed: `lib/families.py`, `lib/reduce4.py`, the six
  prototype artifacts, `ladder/TRANSPORT.md` (live and `git show HEAD:`),
  the predecessor transpose audit.

**Custody.**  I wrote exactly one file: this report, at
`xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md`.  No canonical
ledger (`ladder/REDUCTION.md`, `ladder/TRANSPORT.md`, `PROGRESS.md`,
`APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, `notes.md`), no producer
report, no frozen artifact, no adapter and no other repository file was
created, edited, or deleted.  All arXiv material was stored under
`/tmp/o5src`, outside the repository.  The final SHA-256 of this file is
emitted on stdout (a file cannot contain its own hash).

**Scope firewall.**  Every read, search and command was issued against
`/Users/dc/code/math/jc2` or explicit paths within it, always naming a
subdirectory (`xmodel/`, `ladder/`, `lib/`, `cases/`, `refs/`) or a single
file.  **`jc2-lean` was never entered, listed, read, grepped, built,
status-inspected, or modified**, and no search pattern could reach it: I issued
no repository-root recursive search at any point.  No accidental traversal
occurred and none is disclosed.  No heavy local CAS was used; the largest
computation was a 0.03 s in-memory replay and one seconds-scale family
reduction.  No AWS resource was accessed, launched, or mutated.  Network use:
exactly two read-only arXiv e-print fetches.

**Scope of conclusions.**  This review proves no `G2-PSC`, no pole-path
coverage or surjectivity, no landing theorem, no bounded delay, no degree
ceiling, no family exclusion, no counterexample, and no JC2 result.  The
`8_28` prototype is non-Keller (`Jac(f,g_1)|_{x=0} = -12y^11 + 8y^22`) and
nothing here bears on a Keller-restricted claim.  Live `CornerData` remains
coefficient-free; T-S, T-q and T-RH are the only statements I claim proved, and
T-q is conditional on the frozen record being a faithful GGV5 chain datum.
