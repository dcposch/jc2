# Hostile review: G2 transpose equivariance and fixed-pair chart scope

**Reviewer lane:** Fable 5 (model ID `claude-fable-5`), different-model hostile
mathematical referee.  Producer lane of the target: Sol Ultra.  Predecessor
reviewer lane: Opus 5.  Three distinct model lanes.
**Date:** 2026-08-27
**Target:** `xmodel/g2-transpose-equivariance-hostile-audit-sol-ultra-20260827.md`
**Target SHA-256:** `e31ed8b66a3187578d6dfadc5c276573289a0c73dec4afdc81617b86c7f3d088`
(rehashed at session start; **MATCHES** the required value; fail-closed gate
passed)
**Predecessor:** `xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md`
**Predecessor SHA-256:** `f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1`
(rehashed; **MATCHES**)

## Headline verdict

**CONFIRMED WITH REPAIR, and the load-bearing negative half is STRENGTHENED.**

1. **Part 1 of the audit's headline — `TRANSPORT.md` Conjecture A is a
   clausewise PASS — is CONFIRMED** against the primary sources themselves,
   not the producer's prose.  I re-fetched both papers, reproduced the
   producer's four source hashes byte-for-byte, re-derived the compiled
   numbering of every cited item from the TeX (including a comment-aware
   recount that the naive count gets wrong), read GGV5 Theorem 2.20's
   fourteen clauses and VGG Definitions 4.3/5.5, the five type cases, the
   order/`st`/`en`/`Succ`/`Pred` definitions and Propositions 5.17/5.18
   verbatim, and checked each transported clause by hand.  The conjugation
   dictionary (1.5)--(1.8) is forced by the printed counterclockwise
   conventions, and — a corroboration the audit itself missed — **the primary
   source already uses the identical signed flip with the identical
   `Succ`/`Pred` conjugation** inside its own proof of Proposition 4.7.

2. **Part 2 — the conjugated run does not supply the other chart of the same
   fixed pair — is CONFIRMED AND STRENGTHENED.**  The audit's sign
   computation (5.3) assumes the rectangle/NE-corner normal form.  I prove
   below a hypothesis-free version: *no pair in any `L^(l)` is
   simultaneously an x-`(m,n)`-pair and a y-`(m,n)`-pair* — the two printed
   orientation signs are mutually exclusive for every pair, standard or not,
   at every chain stage.  So there is no exotic non-rectangular loophole,
   and the fixed-pair y-run fails Definition 4.3's first sign condition
   unconditionally.

3. **Repairs (none touches the headline):** (i) Theorem 2.20 clause (13)
   consumes "last lower corner" from a **third paper** — GGV2,
   arXiv:1605.09430, Definition 3.21 — which the audit neither fetched nor
   declared; the transport of that clause is sound only because the y-native
   notion is *defined* by conjugation, and the disclosure gap repeats
   exactly the defect class of the Opus5 review's REPAIR 1.  (ii) The
   Section 1.1 claim that a naive convention "would first break Theorem 2.20
   at clause (5)" over-states the ordering: the break **at** clause (5) is
   proven, the claim that it is the **first** break is not.  (iii) Display
   (5.2)'s "equivalently" silently crosses the antipode `tau^2`; true, but
   it needs one line.

Nothing here promotes `G2-PSC`, pole-path reachability, landing, coverage,
`G2-BD`, any family exclusion, a degree ceiling, or any JC2 result.

---

## 0. Primary sources, custody of the evidence base

Fetched read-only this session and hashed:

```text
arxiv.org/e-print/1708.07936 (gz)   2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e
  -> decompressed GGV5 TeX          8f5571e527c4e579b185f7e75dcf48cd6c92fa88c82c46c33019d38ab89d78f5   [MATCHES audit §8]
arxiv.org/pdf/1708.07936v1          e04e3bfd88c62346c467ec7c32f5bb236cdcb2ee4796525408c0c8d68632fcdb   [MATCHES audit §8]
arxiv.org/e-print/1401.1784 (gz)    e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0
  -> decompressed VGG TeX           b4908fd596d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5   [MATCHES audit §8]
arxiv.org/pdf/1401.1784v3           8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60   [MATCHES audit §8]
```

So my review and the audit read **byte-identical** primary text.  GGV5 is
"Some algorithms related to the Jacobian Conjecture" (source filename dated
2017-08-26); its bibliography confirms `GGV1` = Valqui--Guccione--Guccione,
*On the shape of possible counterexamples to the Jacobian Conjecture*,
J. Algebra **471** (2017) 13--74 = arXiv:1401.1784 (the campaign's VGG), and
`GGV2` = *The Two-Dimensional Jacobian Conjecture and the Lower Side of the
Newton Polygon*, arXiv:1605.09430 — see Repair R1.

Repository pins rehashed (all match the audit's Section 8 and the live tree):

```text
ladder/TRANSPORT.md        9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c   [MATCHES]
opus5 predecessor          f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1   [MATCHES]
lib/families.py            729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e   [MATCHES]
prototype RESULT.json      deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd   [MATCHES]
```

**Numbering re-derivation (not taken on trust).**  Both papers put all
theorem-like environments on one per-section counter.  A naive count of
`\begin` lines in VGG section 5 is wrong: line 2158 is a commented-out
remark.  The comment-aware recount gives 5.5 = `def regular corner`,
5.7 = `some properties of corners`, 5.10 = `estamos en Case IIa`,
5.12 = `first component`, 5.14 = Case II, 5.16 = Case II.b),
**5.17 = Case III**, **5.18 = Case II ("encima de la diagonal")**,
5.20 = `todos son Smp`, 5.21 = `B finito`, 5.22 = `esquina regular unica` —
and this recount is *independently confirmed* by GGV5's own cross-citations
of Definition 5.5, Corollary 5.7(1), Remarks 5.10/5.12, Propositions 5.14,
5.16, 5.18(4), Corollary 5.21 and Proposition 5.22, every one of which lands
on the right labelled object.  Definition `Smp` is item 4.3 of section 4.
The display `\label{mlambda}` inside Proposition 5.18 is the ninth numbered
equation of section 5, i.e. **(5.9)**.  GGV5's theorem
`standard pair generates complete chain` is the twentieth countered item of
its section 2, i.e. **Theorem 2.20**, with clauses printed (1)--(14).  All
of the audit's citations resolve correctly.

---

## 1. Item 1 — conjugation, bracket sign, support/weight, `st/en`, order, `Pred/Succ`

### R-A1. Signed conjugation and bracket (1.1)--(1.2) — **CONFIRMED**

`(tau F)(x,y) = F(y,-x)` gives `(tau F)_x = -F_Y(y,-x)`,
`(tau F)_y = F_X(y,-x)`, hence

```text
[tau F, tau G]_{x,y} = F_X G_Y - F_Y G_X |_{(y,-x)} = tau([F,G]_{X,Y}),
```

with the constant preserved exactly; the unsigned swap `F(y,x)` gives
`-sigma([F,G])`.  Both re-derived by hand.  Since VGG's Jacobian-pair and
`(m,n)`-pair definitions require only `[P,Q] in K^x` (arbitrary nonzero
constant — verified verbatim), the audit's claim that the unsigned swap
changes no admissibility condition is correct, and the signed choice's extra
value (preserving the constant) is real but optional.

**Corroboration the audit missed:** VGG's own proof of Proposition 4.7
introduces "the flip `psi_1(x) := y`, `psi_1(y) := -x`" — literally (1.1) on
`L^(1)` — and conjugates a `Succ`-at-`(1,0)` condition into a
`Pred`-at-`(0,1)` condition and back via `psi_1 o phi_1' o psi_1`.  The
audit's dictionary is not merely consistent with the primary source; its
germ is *in* the primary source.  This strengthens correctness and slightly
trims novelty (see §7).

### R-A2. Termwise support/weight map (1.3)--(1.4) — **CONFIRMED**

`X^{i/l}Y^j -> (-1)^j x^j y^{i/l}`, so `Supp(tau F) = T Supp(F)` and, against
VGG's printed `v_{rho,sigma}(i/l, j) = rho i/l + sigma j` with the **max**
convention (Definition at VGG line 324, read verbatim),
`v_{Tw}(tau F) = v_w(F)` and `ell_{Tw}(tau F) = tau(ell_w(F))`.  Identical to
`TRANSPORT.md` (4.1)--(4.2), whose pinned hash matches.

### R-A3. Endpoint dictionary (1.5)--(1.6) — **CONFIRMED**

VGG defines `st/en` as "the first and the last point ... when we run
**counterclockwise** along the boundary of `H(P)`", uniquely characterized
(printed endnote) by `(rho,sigma) x (en - st) > 0`.  `T` negates cross
products, so with global names `st_{Tw}(tau F) = T en_w(F)` and conversely —
(1.5) is forced, and matches `TRANSPORT.md` (4.2).  The y-native names (1.6)
are then exactly the printed definitions read in the local coordinates
`(y,-x)`: local records of `tau F` coincide with native records of `F`, and
converting local records to global exponents is `T`.  Checked directly.

### R-A4. Order and `Pred`/`Succ` (1.7)--(1.8) — **CONFIRMED**

VGG's order on half-circle-free intervals is printed as
`(rho,sigma) < (rho',sigma') <=> (rho,sigma) x (rho',sigma') > 0`
(equation `\label{order}`), and `Succ_P`/`Pred_P` are the first elements of
`Dir(P)` counterclockwise/clockwise (Definition `Sucesor y predecesor`,
verbatim).  `T` negates cross products, so the transported order is the
reversed global order and a y-native predecessor is a global successor:
(1.7)--(1.8) are forced, not chosen.  `Dir(P)` itself is pure support
cardinality (`#Supp(ell) > 1`) and `A(P)` is built from `Dir`, `I`, `v`,
`st` only — everything in the dictionary's closure.

### R-A5. "A naive convention ... would first break Theorem 2.20 at clause (5)" — **CONFIRMED WITH REPAIR**

The definitive half is right: at a stage corner with `h < i`, clause (5)
demands `m^{-1} st_{rho_h,sigma_h}(P_i) = A_{h+1}`; the leading form there is
not a monomial (else `A_{h+1} = A_h`, contradicting clause (11)'s strict
`v_{01}` descent), so replacing y-native `st` by global `st` reads
`T en/m = T A_h != T A_{h+1}` and the clause **provably fails**.  But
"first" is over-stated: clause (3)'s pair predicate itself contains an
endpoint token (`v_{1,-1}(en_{1,0}(P)) < 0`, Definition 4.3).  Under the
same naive convention that token becomes `v_{1,-1}(st_{1,0}(P_i)) < 0`, a
strictly *stronger* condition (on the `(1,0)` edge `st` maximizes
`v_{1,-1}`), which the fourteen clauses guarantee only at `i = 0` (there it
is literally the printed standard condition).  For `i >= 1` nothing pins it,
so the naive convention may already break at clause (3); and the fully naive
reading that also keeps the defining directions global breaks clause (3)
outright.  **Repair:** weaken to "provably breaks no later than clause (5);
(1.6)--(1.8) are mandatory".  The mandatory-convention conclusion — the only
load-bearing part — stands.

### R-A6. Corners, pair transport, (1.9)--(1.11) — **CONFIRMED**

Definition 4.3 verbatim:

```text
(m,n)-pair:  [P,Q] in K^x,  v11(P)/v11(Q) = v10(P)/v10(Q) = m/n,
             v_{1,-1}(en_{1,0}(P)) < 0.
standard:    P,Q in L^(1)  and  v_{1,-1}(st_{1,0}(P)) < 0.
```

The audit's global rendering of the conjugated pair definition — ratios at
`v_11` and `v_01`, base direction `(0,1)`, printed local `v_{1,-1}` becoming
global `v_{(-1,1)}` — is exactly right, and (1.11) holds because the local
records of `(tau P, tau Q)` equal the native records of `(P,Q)`.  The five
type cases (I.a, I.b, II.a, II.b, III — read verbatim at VGG lines
2331--2360) use only bracket vanishing, `#factors` of the face polynomial,
alignment, and local `v_{1,-1}(st)` signs; all transport verbatim.  Regular
corners (Definition 5.5, verbatim: `b >= 1`, `b > a/l`, `(rho,sigma) in
Dir(P)`, `A = en_{rho,sigma}(P)/m`) carry the orientation `v_{1,-1}(A) < 0`
in the printed definition itself.

## 2. Item 2 — GGV5 Theorem 2.20, all fourteen clauses

I transcribed the fourteen clauses from the TeX and checked the audit's
table row by row.  The exact statement quantifies: for each **standard**
`(m,n)`-pair, there exist stage data with (1) `l_0 = 1 <= ... <= l_{j+1}`;
(2) `(rho_0,sigma_0) > ... > (rho_{j+1},sigma_{j+1})` in
`I = ](1,-1),(1,0)]`; (3) `(P_i,Q_i)` an `(m,n)`-pair in `L^(l_i)` for
`1 <= i <= j+1` and `(P_0,Q_0) = (P,Q)`; (4) earlier leading forms
preserved; (5) earlier corners type II.a with `st/m = A_{h+1}`; (6)
`A_0 = en_{10}(P)/m` and stage corners type II; (7) II.a identity step;
(8) II.b: `l_{i+1} = lcm(rho_i, l_i)`, root `lambda in K^x` of `p_i` with
`m | m_lambda`, generated corner `(k_i/(m l_i), 0) +
(m_lambda/m)(-sigma_i/rho_i, 1)`, and `ell(P_{i+1}) = phi(ell(P_i))` with
`phi(y) = y + lambda x^{sigma_i/rho_i}`; (9) terminal type I; (10) child;
(11) `v_{01}` strict descent; (12) completeness; (13) the `l_t = 1` prefix:
regular-corner set of `(P,Q)`, IIa/IIb split, `A'_t` the **last lower
corner** "(see GGV2 Definition 3.21)", identity pairs; (14) the regular
corner set of `(P_{j+1},Q_{j+1})`.

All fourteen conjugated rows of the audit's table check out against this
text under the dictionary (1.5)--(1.8): **fourteen PASS verdicts CONFIRMED**.
The child/generated/final-corner/complete-chain machinery (GGV5 Definitions
`valid edges`, `generated`, `child`, `final corner`, `complete chain`, the
`Gamma` multiplicity sets and `gamma_max = min(gcd(a-a',b-b'), b-1)`) is
pure local-record arithmetic, unchanged under transport, as claimed.  The
audit's meta-proof — apply the printed x-theorem to
`(tau^{-1} Phat, tau^{-1} Qhat)` and conjugate the entire witness — is a
sound transport-of-structure argument and does not depend on the campaign
port.

**Repair R1 (dependency disclosure, clause 13).**  Clause (13)'s "last lower
corner" is defined in **GGV2 = arXiv:1605.09430, Definition 3.21** — a third
paper.  GGV5 §1 also leans on GGV2 (Definition 3.17, Remarks 3.8/3.9,
Proposition 3.25) for the `PLLC` machinery that valid-edge condition (4)
consumes.  The audit's Section 8 declares only GGV5 and VGG as primary
sources and its Section 0 says every clause was checked "against the primary
GGV5/VGG definitions" — for clause (13) that is not literally possible from
the declared sources.  The clause-(13) PASS *survives* because the y-native
"last lower corner" is defined by conjugation (transport-of-structure needs
no knowledge of the definition's internals), and because the `PLLC` layer is
corner arithmetic.  But the dependency must be declared, exactly as the
Opus5 review forced the `theta_i`/VGG declaration on the earlier producer.
Verdict: clause (13) **CONFIRMED WITH REPAIR** (disclosure only).

## 3. Item 3 — VGG Propositions 5.17 and 5.18, and (5.9)

**Proposition 5.17 (Case III) — CONFIRMED.**  Verbatim hypotheses: regular
corner, `[ell P, ell Q] = 0`, `p(z) = mu (z-lambda)^r` — which *implies*
`rho | l` (printed conclusion, so the audit's "`rho|l` is unchanged" is the
correct invariance of an integer conclusion); `phi in Aut(L^(l))` with
`phi(y) = y + lambda x^{sigma/rho}`.  Conclusions (1)--(4) exactly as the
audit lists: preserved `en` plus intermediate leading forms on
`](rho,sigma),(-rho,-sigma)[`; the `(m,n)`-pair in the *same* `L^(l)`; the
regular corner at the *new direction* `(rho',sigma') = Pred_{phi(P)}(rho,sigma)`;
and `(a/l,b) = st_{rho,sigma}(phi(P))/m`.  Under the dictionary each maps to
its y-native image; `Pred^y = T Pred = global Succ` is exactly (1.8).

**Proposition 5.18 (Case II) — CONFIRMED, including (5.9).**  Verbatim: the
hypothesis display `\label{mlambda}` is

```text
(5.9)   m_lambda >= (m/l) * (a*rho + b*l*sigma)/(rho + sigma),
```

the successor is `phi(x^{1/l'}) = x^{1/l'}`, `phi(y) = y + lambda x^{sigma/rho}`
with `l' = lcm(rho,l)`, `A^(1) = st_{rho,sigma}(phi(P))/m`, and the four
conclusions are: preserved `en` + intermediate forms; `(phi(P),phi(Q))` an
`(m,n)`-pair in `L^(l')`; `st_{rho,sigma}(phi(P)) = (k/l,0) +
m_lambda(-sigma/rho,1)` with **`m | m_lambda` as a conclusion** (from
integrality of `st/m`, printed proof read); both regular corners with the
old one type II.a.  The audit's invariant rewriting
`(m/l)(a rho + b l sigma)/(rho+sigma) = m v_w(A)/(rho+sigma)` is an identity
(`v_w(A) = (a rho + b l sigma)/l` for `A = (a/l,b)`), and since
`v_{Tw}(TA) = v_w(A)` and `(Tw)_1 + (Tw)_2 = rho + sigma`, **(5.9) is
literally invariant** — confirmed.  The proof's two sign inequalities
(`v_{1,-1}(st(phi P)) < 0`, `v_{0,-1}(st(phi P)) < -1`, display `\label{e3}`)
become global `v_{(-1,1)}` and `v_{(-1,0)}` exactly as stated.  The
conjugated successor `psi(x) = x - lambda y^{sigma/rho}` and the local
reading `V -> V + lambda y^{sigma/rho}` at `V = -x` were re-derived by hand;
same face polynomial, same roots, same multiplicities, same Kummer index.

## 4. Item 4 — same-pair versus conjugated-pair object identity

**CONFIRMED.**  `C_y(tau P, tau Q) = tau C_X(P,Q)` (display 5.1) is the same
occurrence in new coordinates: in the y-fraction category every occurrence
has `y -> infinity` with `x ~ lambda y^{-u}` bounded (`I_y = T(I)` forces
`u in [0,1)`), and for the conjugated pair those are precisely the images of
the native `X -> infinity` occurrences.  The genuinely missing object is
`C_y(P,Q)` — the fixed pair's native `Y = infinity` chart (on the `8_28`
prototype: the sixteen-place, mutation-sensitive side, per the predecessor's
O1).  One nit: (5.2)'s "equivalently `C_X(tau P, tau Q)`" crosses
`tau^2 = ((x,y) |-> (-x,-y))`; since the antipode preserves supports, all
valuations, and the bracket (determinant one), pair-ness and chain
admissibility are blind to it, so the equivalence is true — but the audit
should say this one line rather than imply `tau^{-1} = tau`.  **CONFIRMED
WITH REPAIR** (one-line justification).

## 5. Item 5 — Definition 4.3 rejection, clause (3) first, clause (6) downstream, the `8_28` sign

### R-E1. Does Definition 4.3 really reject the same-pair y-local input? — **CONFIRMED AND STRENGTHENED**

The audit's (5.3) computes the sign at the base corner under the
rectangle/NE-corner normal form.  I remove every hypothesis:

> **Lemma (orientation disjointness).**  Let `P in L^(l) \ {0}` have finite
> support.  Write `M_i = max{i-exponents}`, `j* = max{j : (M_i,j) in Supp}`,
> `M_j = max{j-exponents}`, `i_0 = max{i : (i,M_j) in Supp}`.  By the printed
> cross-product convention, `en_{1,0}(P) = (M_i, j*)` and
> `st_{0,1}(P) = (i_0, M_j)`.  The x-pair sign condition is
> `v_{1,-1}(en_{1,0}(P)) < 0`, i.e. `M_i < j*`; the y-native pair sign
> condition on the *same* `P` is `v^y_{1,-1}(en^y-local) = M_j - i_0 < 0`,
> i.e. `M_j < i_0`.  If both held, then
> `M_j < i_0 <= M_i < j* <= M_j`, a contradiction.  Hence **no pair, in any
> `L^(l)`, is simultaneously an x-`(m,n)`-pair and a y-`(m,n)`-pair.**  QED

This needs no rectangle, no NE corner, no standardness, and applies at every
chain stage `i`, so even a hypothetical "restart the y-theory at a later
stage pair" is dead.  The audit's rectangle computation ((5.3):
corner `(b,a)`, sign `b-a > 0`) is the special case `i_0 = ma`, `M_j = mb`
and is **CONFIRMED**; the concrete `8_28` instance `28 - 8 = 20 > 0` is
arithmetic on the pinned record `A_0 = (8,28)` and is **CONFIRMED**.  The
standard-pair endpoint condition fails in the same orientation
(`st^y`-local record `(mb, i_0')` with `i_0' <= ma < mb`), as claimed.

### R-E2. Clause (3) first substantive failure, clause (6) downstream — **CONFIRMED** (with one precision)

Precision: the printed clause (3) asserts `(m,n)`-pair-ness for
`1 <= i <= j+1` and the identification `(P_0,Q_0) = (P,Q)`; pair-ness of the
*input* is the theorem's **hypothesis** (Definition 4.3), so strictly the
same-pair application fails at the hypothesis, before any clause — which the
audit's own §0 says in so many words ("a FAIL before Theorem 2.20", "an
input/object-identity failure").  Within the clause list, (1)--(2) constrain
only the bookkeeping sequences, and (3) is the first clause that names
pair-ness; the audit's "exposed first inside Theorem 2.20 at clause (3)" is
the right reading.  Clause (6) is then indeed downstream and *separately*
dead: the would-be initial corner `en^y_{(0,1)}(P)/m` has local record
`(b,a)` with `a < b`, violating Definition 5.5(1)'s printed `b_loc > a_loc/l`
— it is not a regular corner, so clause (6)'s assertion has no subject.
Both sub-claims **CONFIRMED**.

### R-E3. Theorem failure versus software guard — **CONFIRMED**

`lib/families.py:156` (`assert a < b`, hash-pinned file) sits in
`get_starting_edges`, whose input contract transcribes GGV5's Algorithm
`GetStartingEdges` input line, printed verbatim in the TeX: "A corner
`A=(a,b) in N x N` **with `a<b`**".  The same orientation is carried by
Definition 4.3's sign, Definition 5.5(1)'s `b > a/l`, and valid-edge
condition (2)'s `v_{1,-1}(A) < 0`.  The guard faithfully mirrors the primary
source; the obstruction is mathematical, not software.  There is also **no
hidden standard-orientation hypothesis**: the orientation is printed, three
times over, and — decisively — VGG's own selection machinery *chooses* it
(Proposition 4.7's proof flips via `psi_1` when needed; Proposition 5.20
standardizes with chart-preserving translations `phi(x) = x`,
`phi(y) = y + lambda` only; Corollary 5.21 inherits the choice).  The
orientation is a normalization decision made once at selection, exactly as
the audit's part 2 requires.

## 6. Item 6 — the prototype `H-TRUNC` series/sign check

**CONFIRMED.**  From the frozen prototype (`RESULT.json`, hash matches): the
`x_infinity` block records the Puiseux exponent ladder `pi = [1/4, 9/28]`,
56 presentations in 2 deck orbits of ramification 28, pole order 42 per
place, pole mass 84 — all consistent with the predecessor's independent
census.  I re-derived (7.1) by hand from the prototype's defining pair
component `f = B^2 - x - y^8`, `B = x(xy^4-1)^7`: on `x -> infinity`
branches, `w := xy^4 - 1` satisfies `x^2 w^14 = x + y^8 + a`, so
`w = xi x^{-1/14}(1 + O(x^{-13/14}))` with `xi^14 = 1`, and
`y = zeta x^{-1/4}(1+w)^{1/4} = zeta x^{-1/4} + (zeta xi/4) x^{-9/28} + ...`
with `zeta^4 = 1` — exactly (7.1), including the coefficient `zeta xi/4`
(`-1/4 - 1/14 = -9/28`).  The first GGV translation `lambda = zeta` is the
strict truncation below `9/28`; the conjugated branch (7.2) and source-map
sign (6.2) `x -> x - lambda y^{-1/4}` follow from `psi` as computed in §3.
The negative half is also right and matters: the prototype is **non-Keller**
(canonical witness on file), live `CornerData` is coefficient-free through
its transitive closure (predecessor O0, 16 fields, no exact pair, no root
coefficient, no series), so this atom certifies the interface and the sign
conventions, **not** live `H-TRUNC` for a hypothetical Keller realization —
that needs a theorem-level truncation-completeness proof or a
coefficient-complete exact-pair witness.  And the check lives entirely in
the already-covered native-x chart; it cannot substitute for the missing
`C_y(P,Q)`.  All three sub-claims **CONFIRMED**.

## 7. Item 7 — novelty, deduplication, and `G2-PSC` implications

- **Conjecture A was genuinely open.**  `TRANSPORT.md` §8 states it as
  unproved; the Grok transport review's closing list confirms "Conjecture A
  (native transposed GGV5 admissibility)" among the correctly-labelled
  unproven statements.  Supplying the convention dictionary and the
  clausewise proof is a real increment.  **CONFIRMED as new**, with one
  trim: the signed flip and the `Succ`/`Pred` conjugation germ are already
  in VGG's proof of Proposition 4.7 (§1 above), which the audit should cite.
- **Part 2 is the execution of the predecessor's DISC-1**, with outcome
  "No": the swap exists as a category isomorphism, but it transports the
  occurrence rather than producing a second run, and Definition 4.3 rejects
  the same-pair input — now hypothesis-free by the disjointness lemma.  The
  other-chart inexpressibility *itself* is the predecessor's O2-strengthened
  and clause (4.0); the audit attributes this correctly and adds the
  decisive primary-source sign check DISC-1 asked for.  **Novelty claims
  honest.**
- **Implications for `G2-PSC`: CONFIRMED as stated.**  Conjecture A closes
  native y-chart re-certification of the transported ledger (retiring
  `TRANSPORT.md` §4's second type caution), so the ledger/admissibility
  layer may be promoted; it does **not** close clause (4.0); the live
  residue at `8_28` remains second-chart source/coverage, pole-path
  reachability and gluing, then Q/jump/max and tower data, all under the
  filed Sigray Proposition 4.2 gap.  Per the predecessor's DISC-1 "No"
  branch, `G2-PSC` cannot be closed by any strengthening of Theorem 2.20
  alone: the options remain a genuine T-transpose theorem, a chart-tracked
  normalization, or the pure-Sigray architecture of `REDUCTION.md` §7.1.
- The `8_28` conjugated-chain instance (6.1), the two-frame (5.9) value 4,
  `m_lambda = 21 >= 4`, `3 | 21`, and the single deck orbit reproduce the
  predecessor's D3(a) and the pinned family record (`(8,28) -> (11/4,7)`,
  `mn = (3,2)`, degree check `deg p_0 = mb = 84 = 4*21`).  **CONFIRMED**,
  correctly credited, not claimed as new.

## 8. Falsification attempts (all failed to break the headline)

1. **Naive global endpoint conventions:** break the theorem (clause (5)
   provably; possibly clause (3) earlier) — so they falsify nothing; they
   confirm (1.6)--(1.8) are mandatory.  Only the audit's "first at (5)"
   ordering needed repair (R-A5).
2. **Unsigned swap:** flips the bracket constant's sign and the local
   coefficient signs; every admissibility predicate (`in K^x`, `= 0`,
   `#factors`, sign tests on records) is blind to it.  No break.
3. **Same-pair versus conjugated-pair identity:** attacked via the
   disjointness question — could some non-rectangular pair be both x- and
   y-admissible?  No: the lemma in §5 excludes it for every pair at every
   stage.  The strongest possible version of the audit's part 2 is true.
4. **Hidden standard-orientation hypothesis:** none; the orientation is
   printed in Definition 4.3, Definition 5.5(1), the valid-edge conditions,
   GGV5's algorithm input, and is *selected* by VGG 4.7/5.20/5.21.
5. **Software guard versus theorem:** the guard transcribes the printed
   input contract; removing it would not create a theorem where Definition
   4.3 refuses the input.
6. **Numbering attack:** the audit's (5.17/5.18/(5.9)/4.3/2.20) citations
   could have been off by the commented-remark shift; the comment-aware
   recount plus GGV5's eight cross-citations eliminate that.

## 9. Verdict table

| # | atom | verdict |
|---|---|---|
| A1 | signed conjugation (1.1), bracket rule (1.2), unsigned-swap analysis | **CONFIRMED** (+ VGG 4.7 `psi_1` corroboration) |
| A2 | termwise/support/weight (1.3)--(1.4) vs printed `v`, max convention | **CONFIRMED** |
| A3 | endpoint dictionary (1.5)--(1.6) vs counterclockwise `st/en`, cross-product endnote | **CONFIRMED** |
| A4 | order/`Pred`/`Succ` (1.7)--(1.8) vs `\eqref{order}` and Definition `Sucesor y predecesor` | **CONFIRMED** |
| A5 | naive convention "would first break at clause (5)" | **CONFIRMED WITH REPAIR** (breaks *no later than* (5); "first" unproven) |
| A6 | corners/pair transport (1.9)--(1.11) vs Definition 4.3 verbatim | **CONFIRMED** |
| B | successor conjugation (2.1)--(2.4) vs Thm 2.20(8), Prop 5.18 | **CONFIRMED** |
| C1--C14 | fourteen clauses, conjugated, per audit table | **CONFIRMED** (all fourteen) |
| C13' | clause (13) "last lower corner" dependency | **CONFIRMED WITH REPAIR** (GGV2 arXiv:1605.09430 Def 3.21 undeclared) |
| D1 | Prop 5.17 (Case III), four clauses, `rho\|l`, `Pred` reading | **CONFIRMED** |
| D2 | Prop 5.18 (Case II), four clauses, successor, `m\|m_lambda` | **CONFIRMED** |
| D3 | (5.9) identification and literal invariance | **CONFIRMED** (equation independently pinned) |
| E1 | object identity (5.1)--(5.2) | **CONFIRMED WITH REPAIR** (`tau^2` antipode line) |
| E2 | Definition 4.3 rejects same-pair y-local input (5.3) | **CONFIRMED AND STRENGTHENED** (hypothesis-free disjointness lemma) |
| E3 | clause (3) first substantive failure; clause (6) downstream | **CONFIRMED** (hypothesis-level precision noted) |
| E4 | `28-8=20>0` concrete `8_28` sign | **CONFIRMED** |
| E5 | not the software guard; guard mirrors printed sources | **CONFIRMED** |
| F | `8_28` conjugated chain (6.1), (5.9)=4 both frames, orbit/root data | **CONFIRMED** (credited to predecessor where due) |
| G | prototype `H-TRUNC` atom (7.1)--(7.2); cannot certify Keller live case | **CONFIRMED** (series re-derived; exponents frozen in `RESULT.json`) |
| H1 | Conjecture A novelty (previously open) | **CONFIRMED** (with VGG 4.7 citation trim) |
| H2 | part 2 = DISC-1 execution; attribution to Opus5 (4.0)/O2 | **CONFIRMED** |
| H3 | `G2-PSC` implications and residue list | **CONFIRMED** |
| I1 | audit §8 hash slate (4 arXiv + 4 repo pins) | **CONFIRMED** (8/8 byte-identical) |
| I2 | audit custody/scope self-report (one file, disclosed `rg` leak) | **PROVISIONAL** (consistent with the tree; concurrent-lane writes not fully auditable read-only) |

**Overall: CONFIRMED WITH REPAIR.**  No atom is REFUTED.  Required repairs
before promotion: declare the GGV2 dependency (C13'), weaken the
naive-convention ordering sentence (A5), add the antipode line (E1), and
cite VGG 4.7's flip as prior art for the dictionary (H1).

## 10. Narrowest promotable statement

> **T-A (transpose equivariance, with fixed-pair scope).**  Define
> `tau_l : K[X^{1/l},X^{-1/l},Y] -> K[y^{1/l},y^{-1/l},x]` by
> `tau_l(X^{1/l}) = y^{1/l}`, `tau_l(Y) = -x`, and define every y-native
> notion (valuation, leading form, `st/en`, direction order, `Succ/Pred`,
> `Dir`, `A(-)`, `(m,n)`-pair, standard pair, regular corner, the five
> types, valid edge, child, generated/final corner, complete chain, last
> lower corner) as the printed VGG/GGV5/GGV2 notion read in the local
> coordinates `(y,-x)` — equivalently, as the `tau`-conjugate.  Then:
> (i) `(P,Q)` is an x-standard `(m,n)`-pair iff `(tau P, tau Q)` is a
> y-standard `(m,n)`-pair; (ii) for every x-standard `(m,n)`-pair, the
> `tau`-image of any Theorem 2.20 witness satisfies all fourteen y-native
> clauses for `(tau P, tau Q)`, and VGG 5.17/5.18 hold y-natively with
> (5.9) literally invariant; (iii) no pair in any `L^(l)` is simultaneously
> an x-`(m,n)`-pair and a y-`(m,n)`-pair; hence (iv) the guaranteed y-run
> is `tau` of the x-run — the same occurrence in new coordinates — and
> neither theorem supplies a source run naming the fixed pair's other
> infinity chart.  This resolves `TRANSPORT.md` Conjecture A affirmatively
> at the ledger/admissibility layer and proves the second-chart clause
> (4.0) is not closed by conjugation.  No `G2-PSC`, coverage, reachability,
> landing, `G2-BD`, ceiling, or JC2 content.

Clause (iii) is this review's addition; (i), (ii), (iv) are the audit's, with
the repairs of §9 applied.

## 11. Cheapest next proof obligation

**Chart tracking through the GGV selection pipeline.**  The selection route
is: counterexample --> van den Essen Corollary 10.2.21 (an *arbitrary*
`Aut(L)` element producing the subrectangular form `1 <= a <= b`) --> VGG
Proposition 4.7 (flip `psi_1` plus controlled fixes) --> Proposition 5.20
(pure translations `phi(x) = x`, `phi(y) = y + lambda`) --> Corollary 5.21.
Propositions 4.7/5.20 are chart-rigid (flip and translations), so the only
step that could conceivably relocate the missing `Y = infinity` chart into a
freshly selected pair's native chart is the van den Essen normalization.
The obligation: read the proof of vdE Theorem 10.2.1/Corollary 10.2.21 and
determine whether its automorphism can be forced into a chart-tracked normal
form (linear/flip times triangular of controlled direction); then run the
pipeline exactly on the coefficient-complete non-Keller `8_28` prototype and
observe which boundary places the re-selected pair's native chart names.
Outcome "rigid": T-transpose is genuinely new mathematics and the campaign
should commit to the pure-Sigray bypass (`REDUCTION.md` §7.1) for coverage.
Outcome "trackable": a second x-run on a re-selected pair reaches the old
y-chart, and `G2-PSC`'s clause (4.0) reduces to a gluing statement.
Desk-scale: one primary-source read plus exact arithmetic on frozen data; no
CAS, no AWS.  (Secondary, pure bookkeeping: file T-A and the disjointness
lemma into `TRANSPORT.md` §8 with the GGV2 citation — a producer action, not
taken here.)

## 12. Checks, identity, custody, scope firewall

**Model identity.**  Fable 5, exact model ID `claude-fable-5`, acting as a
different-model hostile mathematical referee.  No sub-agent, no
`ultrareview`, no delegated review was invoked.  This session had shell and
read-only network access; both were used only as recorded here.

**Checks run.**
- Fail-closed rehash of target and predecessor (both MATCH, §top).
- Read-only arXiv fetches of both e-prints and both PDFs; decompression;
  all four audit-recorded hashes reproduced byte-for-byte (§0).
- Independent comment-aware re-derivation of the compiled numbering of GGV5
  Theorem 2.20 and VGG 4.3/5.5/5.14/5.16/5.17/5.18/5.20/5.21/5.22 and of
  equation (5.9), cross-validated against eight GGV5 citations (§0).
- Verbatim reads: GGV5 §1--§2 (PLLC, valid edges, `Gamma`, children,
  complete chains, Theorem 2.20 with proof head, Algorithm inputs);
  VGG preliminaries (`L^(l)`, `v`, `ell`, `st/en` + cross-product endnote),
  `\eqref{order}`, `Sucesor y predecesor`, Definition 4.3, Proposition 4.7
  with its `psi_1` endnote, Definition 5.5, the five type cases,
  Propositions 5.14/5.16/5.17/5.18 (with (5.9) and `\eqref{e3}`),
  Proposition 5.20's proof, Corollary 5.21.
- Hand algebra: bracket chain rule for `tau` and the unsigned swap;
  termwise (1.3); endpoint/cross-product reversal; `psi = tau phi tau^{-1}`
  and the `V = -x` reading; generated-corner transport (2.4) and the `8_28`
  instance `(0,1) + 7(1,1/4) = (7,11/4)`; (5.9) invariance identity; the
  orientation-disjointness lemma; both (5.9) evaluations equal to 4;
  `28 - 8 = 20 > 0`; the prototype series (7.1)--(7.2) from
  `x^2 w^14 = x + y^8 + a`; `deg p_0 = 84 = 4*21`.
- Repository pins: `ladder/TRANSPORT.md`, `lib/families.py` (line 156 read
  in context), prototype `RESULT.json` (exponent ladder `[1/4, 9/28]`,
  56 presentations, 2 orbits, ramification 28 confirmed in the frozen
  bytes); novelty greps over `xmodel/` and `ladder/` only.

**Custody.**  I wrote exactly one file: this report, at
`xmodel/g2-transpose-equivariance-hostile-review-fable5-20260827.md`.  No
canonical ledger, producer report, frozen artifact, adapter, or any other
repository file was edited.  The final SHA-256 of this file is emitted in
the review transcript (a file cannot contain its own hash).  All arXiv
material was stored under `/tmp`, outside the repository.

**Scope firewall.**
- Every search and read ran from `/Users/dc/code/math/jc2` or absolute
  paths within it, always scoped to named subdirectories (`xmodel/`,
  `ladder/`, `lib/`, `cases/`, `refs/`); `jc2-lean` was never entered,
  listed, read, grepped, built, status-inspected, or edited, and no search
  pattern touched it.
- No heavy local algebra (largest computation: hand-checkable exact
  arithmetic and hashing), no CAS, no AWS access or mutation, no job
  launches.  Network use: exactly four read-only arXiv fetches.
- This review proves no `G2-PSC`, pole-path surjectivity, landing theorem,
  coverage statement, family exclusion, degree ceiling, counterexample, or
  JC2 result.  The `8_28` prototype is non-Keller; nothing here bears on a
  Keller-restricted claim.  The disjointness lemma is a statement about
  Definition 4.3's sign conditions only.  No promoted campaign result is
  weakened; no ledger promotion is performed here — T-A's filing is left to
  the producer with the §9 repairs applied.
