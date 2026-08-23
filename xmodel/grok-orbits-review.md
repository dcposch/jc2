# Hostile review: equivariance theorem + PCC / WTC-1

Reviewer: Grok 4.6 (hostile referee, verdict tier). Date: 2026-08-20.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Target: `xmodel/sol-pcc-orbits.md`. Two objects.

- **(A)** THE EQUIVARIANCE THEOREM (load-bearing). Claim: the 36 radical
  fibers form one **free** orbit under \(G=(C_3)^2\times(C_2)^2\) via
  diagonal scalings, with
  \[
  F_{\ell,g\lambda}(T_gx)=\chi_\ell(g)\,F_{\ell,\lambda}(x)
  \]
  claimed **PROVED** at source and realized exactly at D25.
- **(B)** The boxed PCC statement, its sufficiency for
  `td <= alpha*beta`, and the isolation of WTC-1 as the earliest
  missing arrow in the Corollary-7.4 packet-to-PCC lane.

Method: independent `python3` arithmetic on
`cases/d23_atlas_p{105337,105673}.json` and the 72 parked
`cases/d25fam_p{P}_{label}.ms` plus both 38-row unions. Own parser
(integer `*`/`^` monomial dictionaries; no copy of the document's
reproduction script). Own cube-root scan, Tonelli square roots of 3,
selector-law reconstruction from `a00pp`, and the **written** §4.2
weights plus the **written** checksum characters — not characters
re-derived from the union and then treated as an oracle. Focused
exact comparison `a00pp` against `a10pp`, `a01pp`, `a00mp`, `a00pm`
before the full Cayley graph. No Singular, no msolve rerun, no
`directionb_tails_D21.pkl` term expansion (pkl load requires the
engine module; out of the commissioned attack surface). Cited books
(`xmodel/grok-k-g5-review.md`, `xmodel/sol-g5-emission.md`,
`xmodel/sol-tdbound-review.md`, `SECTION4-AUTOMATION.md`,
`cases/r1_experiment.py` 357–407 and 501–590,
`cases/directionb_strike.py` 36–58) were read, not trusted.

---

## Verdicts

### Object A — Equivariance theorem

**CONFIRMED as a scoped algebraic theorem plus an exact D25
realization over both banked `F_p`. GAPS only on un-rerun source-pkl
weights, on the 216 witness checks, and on FUTURE-EMISSION FIDELITY
(already isolated by the document). Not REFUTED.**

The 36 selector points are a free \(G\)-torsor at both primes: 36
distinct `F_p`-points, trivial geometric stabilizer, `|G|=36`, one
orbit. Every diagonal entry of every \(T_g\) lies in `F_p` (in the
six-element set \(\{1,-1,\omega,\omega^2,-\omega,-\omega^2\}\)). The
transport is an `F_p`-scheme isomorphism, not merely an isomorphism
after passing to the algebraic closure.

The character identity holds as an exact monomial-dictionary identity
on all `2·36·4·34 = 9792` generator-edge row pairs of the parked D25
systems, including the five residual rows R1–R5 (character 0).
Focused `a00pp → {a10pp, a01pp, a00mp, a00pm}` is 34/34 exact on
each edge at both primes, including the three numerical coefficient
edges the document quotes. Atlas `g_rows` independently satisfy the
same identity on all 432 generator-edge triples per prime.

The all-depth source argument (branch reindexing of the 42/21
products, Jacobian-depth construction commuting with \(C_c\)) is a
proof of equivariance of the **pristine** residue-A / fixed-`r` /
`B`-frozen / no-log / `PIN42` / `W`-chart depth ideal, not a
computation. D25 is a realization, not the proof.

### Object B — PCC sufficiency + WTC-1 isolation

**CONFIRMED. PCC as boxed is a genuine sufficient lemma for
`td <= alpha*beta`. WTC-1 is correctly identified as the earliest
missing arrow in the Corollary-7.4 packet-to-PCC lane. PCC itself
remains CONJECTURE. Not REFUTED.**

The floor-and-sum arithmetic from (1.5)–(1.6) to (1.7) is correct.
KME-2 is the bound rewritten; PCC is strictly stronger and is not a
renaming. After a certified packet, the bank still cannot name an
ordinary center or write \(R_p,S_p\); that is WTC-1. FC5, the `w`
depth invariant, NF-M Bezout, and the 21-of-22 census do not supply
that arrow. A second theorem (PCC-COVER) is still required after
WTC-1; the document does not pretend otherwise.

**Tier deserved.** Object A: INTERNAL theorem of this chart and these
two split primes, with a characteristic-zero source proof in the
stated splitting field. Not DEPTH-STAB, not a germ, not a Keller pair.
Object B: sufficiency PROVED; truth of PCC and of WTC-1 unproved, and
correctly left unproved.

---

## Exact scope of “one fiber decides all 36”

This is the consequence the rest of the campaign will try to spend.
State it as a theorem with its actual hypotheses, not as a slogan.

**What one `a00pp` verdict plus equivariance does decide.**
Fix one banked split prime, one square root of 3, the residue-A
`B`-frozen no-log `PIN42` \(W\)-chart, and a presentation \(I(\lambda)\)
of the depth-\(D\) ideal on fiber \(\lambda\) that is related to the
pristine source by a character-semi-invariant exact localization
(the parked D25 systems are in this class; a reduced monic GB of an
equivariant ideal is in this class). Let \(T_g\in\mathrm{GL}_{28}(\mathbf F_p)\)
be the diagonal scaling of §4.2. Then

\[
T_g^*I(g\lambda)=I(\lambda),
\]

so \(\mathbf F_p[x]/I(\lambda)\cong\mathbf F_p[x]/I(g\lambda)\) as
\(\mathbf F_p\)-algebras. Every isomorphism invariant is therefore
constant on the 36 fibers, **including dimension**:

- emptiness / `NONEMPTY` over \(\mathbf F_p\) and over
  \(\overline{\mathbf F}_p\);
- Krull dimension of the affine scheme (arithmetic and geometric);
- degree, Hilbert function, leading-term ideal of a reduced GB
  (diagonal scaling preserves monomials and any monomial order;
  only leading-coefficient normalization is needed);
- Jacobian / conormal ranks, determinantal rank defects;
- existence of a point over \(\mathbf F_p\) or over an extension
  (an \(\mathbf F_p\)-point transports to an \(\mathbf F_p\)-point
  by \(T_g\), because \(T_g\) is \(\mathbf F_p\)-rational);
- component count after the corresponding base change.

Empirically this already matches the atlas: at both primes, all 36
fibers have `d21 dim = 13`, `det23 dim = 11`, `n_basis = 397/509`,
`cond_dim = 3`, `nf_rank = 5`, verdict `NONEMPTY`. Those numbers are
not an extra miracle; they are the theorem plus GB uniqueness.

**The scalings are \(\mathbf F_p\)-rational.** They do **not** live
in an extension. Verified:

- \(p\in\{105337,105673\}\), both \(\equiv 1\pmod{12}\), both
  \(42\mid(p-1)\).
- \(\bigl(\frac{3}{p}\bigr)=1\). Square roots of 3 exist in
  \(\mathbf F_p\) (Tonelli: 795 and 14686 for the atlas's choice of
  \(r\)). This puts the **selector points** on \(\mathbf F_p\), and
  is why the 36 fibers are \(\mathbf F_p\)-rational points of
  \(B_{36}\). It is **not** what makes \(T_g\) rational.
- Primitive cube roots exist in \(\mathbf F_p\) (full scan, two
  each): \(\omega=15094,\;\omega^2=90242\) at 105337;
  \(\omega=13168,\;\omega^2=92504\) at 105673. These are exactly the
  document's values. \(\omega^2+\omega+1=0\), \(\omega^3=1\),
  \(\omega\neq 1\).
- Every diagonal entry of every \(T_g\) is in
  \(\{1,-1,\omega,\omega^2,-\omega,-\omega^2\}\subset\mathbf F_p^\times\).
  \(\sqrt{3}\) never appears in \(T_g\). Sign characters are
  \(\pm 1\in\mathbf F_p\).

Consequently the transport is an isomorphism of affine
\(\mathbf F_p\)-schemes. It is **not** “only over the closure.”
(If these primes had failed to contain \(\omega\), geometric
dimension would still match after \(\mathbf F_p(\omega)/\mathbf F_p\),
but \(\mathbf F_p\)-points and arithmetic invariants would not
automatically transport. That is not this bank: \(\omega\in\mathbf F_p\).
Separately, \(\zeta_{42}\) also lies in both fields, so the source
proof's cyclotomic device does not leave \(\mathbf F_p\) either at
these two primes.)

**What one fiber does not decide.**

1. A future optimized D27+ presentation obtained by pivoting, Schur
   reduction, saturation, or fiber-dependent gauges, unless it
   passes FUTURE-EMISSION FIDELITY. Copying printed coefficients
   onto another fiber is false (saturation identity (5.6); the
   annihilator must be transported). This gap is operational and
   finite, and is already the document's gate, not a hidden hole
   in the theorem.
2. The other \(\sqrt{3}\) embedding. The two \(r\)'s are not in
   the same \(G\)-orbit.
3. The other prime. \(|G|=36\) does not mix 105337 with 105673.
   The honest reduction is \(36\to 1\) per prime and \(72\to 2\)
   across the bank, as written in (6.2).
4. Unfrozen `B`, log chart, other infinity charts, pole-chart
   swap. No action is claimed.
5. DEPTH-STAB, Hensel, an inverse-limit point, algebraization, or
   a polynomial Keller pair. Equivariance of a finite-depth
   obstruction is not a germ.
6. Numerical coefficient arrays themselves. Invariants match;
   coordinates of a witness map by \(T_g\) and are not equal as
   tuples.

**Bottom line for the campaign.** For every faithful emitted system
at one of these two primes, one representative solve plus 35
explicit diagonal transports replaces 36 solves, **and that includes
dimension**. The parked D25 systems are faithful in this sense
(character identity checked). A compiler that silently breaks
homogeneity does not get the 36× for free.

---

## A. Attack on the equivariance theorem

### A.1 Selector torsor and freeness. CONFIRMED.

Selector algebra (3.1) at \(p=105337\), \(r=795\):

\[
A_1^3=3+r=798,\quad A_2^3=3-r,\quad 2h_i^2=3,
\]

and the atlas `a00pp` point is exactly (3.4):
`(50630, 10114, 50267, 50267)`. Same at \(p=105673\), \(r=14686\),
point (3.5). Union selector rows are the same equations in msolve
syntax (`A1r^3+104539` is \(A_1^3-(3+r)\), etc.).

Independent reconstruction: every labeled fiber is
\((\omega^i A_1,\;\omega^j A_2,\;s_1 h,\;s_2 h)\) with 0 mismatches
at both primes. 36 distinct 4-tuples. No nontrivial \(g\) fixes the
`a00pp` point (because \(A_1\neq 0\), \(A_2\neq 0\), \(h\neq 0\),
and \(A_1^3\neq A_2^3\)). Action on labels is free by construction
and the geometric action on the 36 points is free because those
points are distinct. One orbit of size 36. Atlas
`fiber_ms_md5` pairwise distinct: these are 36 different
specializations, not a copied GB.

The \(B_{36}\simeq\mathbf F_p^{36}\) claim is the Chinese remainder
decomposition of an étale complete intersection with 36
\(\mathbf F_p\)-points. Confirmed by exhibiting the 36 points and
the four equations; no extra geometric points over \(\mathbf F_p\)
exist because a cubic has at most three roots and a quadratic at
most two.

### A.2 Diagonal-scaling isomorphisms, exact coefficients. CONFIRMED.

Parser: 36 parked files per prime, 28 variables in identical order,
34 rows, 6096 monomial terms each, 0 rejected terms, term-count
census `{6096: 36}`. Claimed 6096 is exact, not an estimate.

Convention used: geometric source-to-target \(y=T_g x\) of (4.1),
with the written §4.2 weights (cube exponents 2 on the first
blocks, 1 on the second; signs on `{x16,x53,x55}` and
`{x24,x58,x60}`). Inverse-pullback would swap cube exponents 1 and
2 and would **fail** these files. The written convention is the
one the emissions satisfy.

**Focused edges from `a00pp` (the attack the user named).** At
both primes, 34/34 rows exact on each of

```text
a00pp -rho1-> a10pp
a00pp -rho2-> a01pp
a00pp -sigma1-> a00mp
a00pp -sigma2-> a00pm
```

Paper's quoted coefficients at \(p=105337\), read from atlas
`g_rows` and matching the identity:

```text
g1, x53*uW1:  50008 -> 81147 = omega*50008      (a00pp -> a10pp)
g1, x72:      103704 -> 1277 = omega^2*103704
g1, x53*uW1:  50008 -> 55329 = -50008           (a00pp -> a00mp)
```

All three equalities hold in \(\mathbf F_{105337}\).

**Residuals R1–R5 (rows 29–33), character 0.** Supports identical
fiber-to-fiber (`148,148,148,148,144` terms). Scaled target equals
source on `a00pp → a10pp` and on `a00pp → a00mp`. Sign characters
are identically 1, as claimed: coefficient sign changes are
cancelled by the displayed variable sign changes, and the residual
block does not pick up a leftover minus.

**Full Cayley graph.** All 4896 generator-edge identities at
105337, all 4896 at 105673, zero failures. Because the four
diagonal matrices commute (they are diagonal) and generate \(G\),
the identity extends from generators to every \(g\in G\). Row
characters are units, so this is an ideal-level scheme isomorphism
(4.4), not a support bijection.

Atlas `g_rows` (the three displayed polynomials, not the D25
parked g-block) satisfy the same identity on 432 edges per prime,
and reproduce the (3.6)/(K.10) census: 18/6/3 classes with
multiplicities 2/6/12, 36 joint triples. Those rows are **not**
homogeneous in the 28 D25 variables after selector specialization
(g1 under rho1 has monomial weights \(\{0,1,2\}\) on a single
fiber). That is expected: baked-in \(A_1,A_2,h_i\) coefficients
carry the complementary weights, and the cross-fiber identity is
what restores a uniform row character. The union 38-row files,
which keep `A1r,A2r,h1r,h2r` as variables, **are** row-homogeneous
under the written weights; derived checksums equal the boxed
strings

```text
rho1: 10011112222200000011111100 | 202 | 00000
rho2: 10011112222220000011111100 | 210 | 00000
s1,s2: 0^34
```

at both primes. (Two union terms `A1r^3`, `A2r^3` have no leading
`1*` in the file; they are still weight 0 under every generator,
since \(3\equiv 0\pmod{3}\). Parked files have no such terms.)

No variable permutation and no row permutation occurs. Same 28
names, same order, same monomial supports on every checked edge.

### A.3 Source-level proof. CONFIRMED as a scoped proof; not machine-checked termwise.

`cases/r1_experiment.py:519-538` builds each orbit product from
factors at phases \(c=k+7j\). \(C_{-14}\) sends \(c\mapsto c-14=
k+7(j-2)\), which permutes the inner index of each complete 42-
or 21-suborbit and preserves the outer direction \(k\). Through-d0
factors (\(k=0\), \(c=7j\)) stay through-d0. \(C_{21}\) sends
\(c\mapsto k+7(j+3)\). On the even 21-orbit support every level is
even, so \(C_{21}\) is the identity there; \(\sigma_i\) acts only
on `Gp_i`, as written.

Descent on invariant coefficient objects matches (5.2),
recomputed:

- level 32: \(\omega^{-32}=\omega\), so \(A_i\mapsto\omega A_i\);
- level 37: \(\omega^{-37}=\omega^2\), so \(W_i,HW_i\mapsto\omega^2(W_i,HW_i)\),
  hence \(h_i=HW_i/W_i\) is cube-fixed and \(uW_i\mapsto\omega\,uW_i\);
- \(\sigma_i\) fixes \(A_i,W_i\), flips \(HW_i\), flips \(h_i\).

Shared prefix levels 18, 24, 30 are cube-fixed
(\(\omega^{-18}=\omega^{-24}=\omega^{-30}=1\)). Branch-merge
variables `vf1_*` / `vf2_*` are not shared across \(i=1,2\), so
the two cube generators do not compete for a single slot. `B`,
`GB42`, `GB21` are fixed. `PIN42` sits at a cube-fixed even level.
Open conditions \(W_i\neq 0\) are stable. The raw Jacobian-depth
combination in `directionb_strike.py:51-58` is built from
\(\Phi,\Gamma\), \(\eta\)-derivatives, and \(\theta=t\,d/dt\); those
operations commute with \(C_c\). Pristine rows can be taken
invariant; parked D25 rows pick up characters from specialized
selector coefficients. That is consistent, not a contradiction.

Adjoining \(\zeta_{42}\) is a proof device. The induced action on
the registry uses only \(\omega=\zeta^{14}\) and \(\pm 1\).

Scope is exactly the banner: residue-A, fixed \(r\), `B`-frozen,
no-log, `PIN42`, \(W\)-chart, 42 invertible. It is not a theorem
about the other \(\sqrt{3}\), the other pole chart, or unfrozen
`B`.

**GAPS, not refutations.**

- The 43,574 radical-expanded D21.pkl monomial weights were not
  independently re-expanded in this review. The phase arithmetic
  is the proof; the pkl is a regression.
- The 216/prime D23 witness transports were not rerun (witness
  coordinates were not in the commissioned payloads).
- FUTURE-EMISSION FIDELITY remains a real gate for D27+. The
  document already refuses to spend the 36× on an uncertified
  compiler. Keep that refusal.

The \(2^2\) sign-chart lift ambiguity is harmless for the orbit
count: a gauge that flips \(W_i\) and \(HW_i\) together fixes
\(h_i\) and does not move the selector label. The canonical lift
(fix \(W_i\) under \(\sigma_i\), flip \(HW_i\)) is the one the
identities use.

The auxiliary \(u_A(A_1-A_2)=1\) row is not character-homogeneous
under independent cube rotations. Denominator
\(\omega^a A_1-\omega^b A_2\neq 0\) on all 36 fibers because
\(A_1^3\neq A_2^3\). Folded D25 has already eliminated it. Not an
orbit-breaker.

### A.4 What the theorem does not say, and does not need to

Fiber equivariance does not prove DEPTH-STAB, a Hensel condition,
an inverse-limit point, algebraization, or a polynomial Keller
pair. The document's ledger already says **NO**. Correct.

---

## B. Attack on PCC and WTC-1

### B.1 Boxed PCC is sufficient for `td <= alpha*beta`. CONFIRMED.

Setup: dominant nonautomorphic Sigray-normalized Keller pair,
coprime type \(2\le\alpha<\beta\), \(d=B\alpha\), \(e=B\beta\),
pencils \(\mathcal L_f=\langle F,Z^d\rangle\),
\(\mathcal L_g=\langle G,Z^e\rangle\), \(\pi:X\to\mathbb P^2\) the
minimal simultaneous point resolution making both maps morphisms.
\(R_p,S_p\) are orders of mobile strict transforms of generic
members, in the orthogonal total-transform point basis, zero when
\(p\) is not a base center of that pencil.

Generic fiber classes (1.4) have \(C^2=D^2=0\) because they are
fibers of morphisms to \(\mathbb P^1\). The Bézout identities
(1.5) are the expansion of those squares and of \(C\cdot D\) in
the orthogonal basis \((H,E_p^*)\), \((E_p^*)^2=-1\).

The identification \(C\cdot D=\mathrm{td}\) is the one-sentence
step. It is standard and is not a cheat: after both pencils are
resolved, a generic pair of **finite** target values is not
attained on \(Z=0\) (every point of \(F=Z=0\) is a base point of
\(\mathcal L_f\), similarly for \(G\)), and residual intersections
of proper transforms are the affine generic fiber of \((f,g)\), of
degree \(\mathrm{td}\). Characteristic zero makes the extension
separable. A hostile reading can still call the sentence a sketch
rather than a written intersection-theory lemma; it is the same
sketch already accepted at
`xmodel/grok-k-g5-review.md:525-533,579-583`, now with the cluster
and point-basis conventions pinned so that a further blowup after
both pencils are resolved adds zero generic multiplicities and
does not change (1.2). That pinning is a tightening, not a
weakening to a tautology. Not enough to withhold CONFIRMED.

Floors: \(R_p,S_p\) are nonnegative integers, so
\(R_p\ge\alpha h_p\), \(S_p\ge\beta h_p\), and
\(R_p S_p\ge\alpha\beta h_p^2\) termwise, including the cases
\(h_p=0\) and the cases where \(p\) belongs to only one cluster.
Summing and invoking PCC:

\[
B^2\alpha\beta-\mathrm{td}
=\sum R_p S_p
\ge\alpha\beta\sum h_p^2
\ge\alpha\beta(B^2-1),
\]

hence \(\mathrm{td}\le\alpha\beta\). No converse is used or
claimed. Jacobian constancy is used only to place the pair in the
Keller/Sigray setup (so \(\mathrm{td}\) is defined and finite);
the inequality itself is intersection-theoretic.

Equality analysis at \(\mathrm{td}=\alpha\beta\): both summed
inequalities and every product inequality become equalities, so
\(\sum h_p^2=B^2-1\) and \(R_p=\alpha h_p\), \(S_p=\beta h_p\) at
every center with \(h_p>0\), while \(h_p=0\) forces \(R_p S_p=0\).
PCC is correspondingly strong. Sufficiency is proved; truth is
not.

KME-2, \(\Delta^2\ge-2\), is exactly the bound rewritten via
(1.8). It is not an independent sufficient mechanism. PCC is the
only named G5 target that can imply the sharp bound without
renaming it. Confirmed.

### B.2 WTC-1 is the earliest missing arrow in the stated lane. CONFIRMED.

Lane, as actually written:

1. Certified Corollary 7.4 packet
   \(\ell(P)=\lambda\widetilde R^{q\alpha}\),
   \(\ell(Q)=\mu\widetilde R^{q\beta}\)
   (SECTION4-AUTOMATION R1 supplies the edge-power for a certified
   Laurent/weighted frame).
2. **WTC-1**: transport the complete base ideals \((F,Z^d)\),
   \((G,Z^e)\), including both denominator sections, through an
   explicit chart into the minimal simultaneous point resolution;
   name a proper or infinitely-near center; strip recorded
   exceptional factors; conclude the mobile ordinary
   multiplicities obey (2.2); record proximity parents.
3. **PCC-COVER**: identify or separate packet centers by actual
   proximity ancestry so that integers \(c_p\le h_p\) satisfy
   \(\sum c_p^2\ge B^2-1\).
4. PCC \(\Rightarrow\) `td <= alpha*beta`.

WTC-1 is the first absent implication in that sequence. The
conditional local lemma (2.2) is immediate once the hypothesis is
available and is not banked. The counter-form
`u^{qα}+x`, `u^{qβ}+2x` is a valid obstruction: weighted initials
alone do not name an ordinary multiplicity. Proximity accounting
and no-double-counting are correctly postponed to PCC-COVER;
trying to sum squares before a center dictionary exists would
reverse the dependency.

**Not claimed, and not true:** that WTC-1 is the earliest missing
arrow toward TD-BOUND among **all** routes. Log ramification
(ranked route 2) bypasses floors and PCC entirely. The document
says this.

**FC5 / `w` / NF-M / 21-of-22 do not secretly supply WTC-1.**
Reconfirmed against the earlier G5 audit, not re-litigated from
scratch:

- FC5 emits two scalars \((w,M)\) from a local frame. No pole
  mass, no ordinary center, no exceptional divisor, no proximity,
  no cross-chart identifier. \(\Phi_s\) is exact at poles and
  nonmonotone on internal charts.
- The `w` recurrence is depth-closure for a **fixed** \(M=1\)
  entry. It does not bound distinct entries, does not cover
  \(M\ge 2\) suffixes, and has no point-cluster meaning.
- NF-M Bézout counts coefficient decorations of a **fixed**
  discrete schema and emitted frame. It does not produce
  \(I_\infty\) or a point-basis vector. The one-type-for-every-\(A\)
  family with constant \((w,M)=(2/3,3)\) is exact quantifier
  control, not a Keller counterexample.
- 21-of-22 is a construction effect of the pole-count constraints
  \(q>\alpha\) and off-axis \(q=\alpha\). Frequency is not
  coverage.

A precision point, not a reversal: SECTION4-AUTOMATION R1 is
printed for one polynomial \(P\). WTC-1 takes as **input** a
certified pair-packet. The missing arrow is the transport of that
packet, not the existence of Cor 7.4. If a future audit found that
common-power for **both** \(P\) and \(Q\) in the same
\(\widetilde R\) was itself unbanked, that would be an earlier
gap in the lane; it is not the gap the document is isolating, and
`sol-tdbound-review.md:437-445` already treats the pair-form as
the content of Cor 7.4 under its hypotheses.

The one-pole cap \(ab\le\nu\) is exactly TD-BOUND in the one-pole
sector. It is a necessary sector test, not a substitute for PCC.

---

## Recomputation ledger (this review)

Independent of the document's reproduction script.

- Cube-root full scan at both primes; Tonelli square roots of 3;
  \(42\mid(p-1)\); \(\bigl(\frac{3}{p}\bigr)=1\).
- Atlas JSON both primes: 36 labels, selector law 0 mismatches,
  36 distinct 4-tuples, trivial geometric stabilizer, orbit size
  36, uniform `(dim 13, dim 11, n_basis 397/509, cond_dim 3,
  nf_rank 5, NONEMPTY)`, g-class counts 18/6/3, 36 joint triples,
  36 distinct `fiber_ms_md5`.
- Atlas `g_rows` monomial-dictionary identity: 432/432 edges per
  prime; quoted 50008/81147/103704/1277/55329 edges exact.
- Union `d25fam_p{P}.ms`: 32 vars, 38 rows, checksums match (4.3);
  selector constants match \(3\pm r\) and \(2h^2=3\).
- Parked D25, both primes, all 36 labels: 28 vars, 34 rows, 6096
  terms, 0 syntax rejects. Focused four neighbors of `a00pp`:
  34/34. Residuals R1–R5 character 0, supports equal, scaled
  coefficients equal. Full generator Cayley graph: 4896+4896
  identities, 0 failures.

Not rerun: `directionb_tails_D21.pkl` 43,574-term weights; 216
fiber-witness checks; `tdbound_scan.py` / `depth_closure_check.py`
/ `nfm_check.py` (those regressions do not fill WTC-1 or PCC).

---

## What this does not earn

Object A is not a characteristic-zero theorem that 36 schemes over
\(\mathbf Q(\sqrt{3},\omega)\) have been Groebner-solved. It is a
proof that they are isomorphic, plus an exact modular realization
of that isomorphism at D25 at two split primes. Object B does not
move PCC out of CONJECTURE and does not prove TD-BOUND. The 36×
solver saving is real for faithful presentations and is a
compiler-gate away for everything else.
