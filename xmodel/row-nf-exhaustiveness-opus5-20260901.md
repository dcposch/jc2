# THEOREM EXHAUST — the explicit ROW-NF families exhaust the campaign rows (6,4) and (8,4)

Lane: EXHAUSTIVENESS (last mathematical dependency of the promoted S4 row-kill theorem, integration #5 §1)
Model: Opus 5 | Date: 2026-09-01 | Budget: 5h desk-scale, no CAS

## 0. Input verification and scope

## 1. The claim to be proved, stated with all quantifiers

## 2. Inventory: what each link actually asserts, and at what quantifier

### 2.1 ROW-SWEEP (a): the delta-sequence census and its gauge

### 2.2 ROW-NF (b): the normal form and the parametrization it consumes

### 2.3 The D1-DEGREE cage (c): invariants up to Aut(A^2)

### 2.4 ROW-84 (d): deg(P - Q^2) = 6 <=> Delta = (8,4,6,3)

## 3. The composition argument: transport of the S4 representation through T in Aut(A^2)

## 4. Proof of THEOREM EXHAUST at (6,4)

## 5. Proof of THEOREM EXHAUST at (8,4)

## 6. Verdict, and the exact typed status of each residual obligation

## 7. What remains of the N=4 reducible residual if EXHAUST lands

## 8. Sources consulted

---

## 0. Input verification and scope

Six frozen copies were hashed with `shasum -a 256` **before any was read**; 6/6 reproduce the
boxed manifest byte-for-byte. The stop condition did not fire.

```text
46e08515…  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md   [CI5]
a88890bd…  row-64-84-closure-review-grok46-20260901.md                           [CLOS]
aa873151…  row-sweep-sol56-20260831.md                                           [SWEEP]
64878fe8…  row-sweep-hostile-review-grok46-20260831.md                           [SWREV]
d0dc4f79…  pi1s4-64-zvk-u6-opus5-20260831.md                                     [ZVK]
9344d6b3…  pi1s4-64-zvk-u6-hostile-review-grok46-20260831.md                     [ZVKREV]
```

One primary source was re-fetched on this host and re-hashed; it reproduces the custody value
already recorded in `SWREV` §0 and `SWEEP` §0:

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9
  241372 bytes,  https://arxiv.org/pdf/0910.2613v2
  C. Galindo, F. Monserrat, "The Abhyankar-Moh theorem for plane valuations at infinity".
  Consumed: Definition 2.2 (p. 2) and Theorem 2.1 (p. 3).   [GM]
```

**Execution disclosure.** No CAS was run; no job of uncertain duration was run. Every algebraic
step below is a hand expansion displayed in full. Two of them (the minus-branch quartic `N`, and
the plus-branch reduction to `h`) were re-derived here from the power-sum identities and are
displayed, not quoted. No canonical ledger, charged file, or `jc2-lean` was touched. One output
file only.

**FALLACY-v2 posture.** This report asserts no new exit price, so it carries no `charge_basis`
line. The negative rules that bite here are *floor/attainment* (a numerical census is not an
existence theorem, and an exhaustiveness statement is not a kill) and *variable/ring map* (every
automorphism below is displayed with its coordinate images, generator order and Jacobian; a
matching degree pair is never used as evidence of an identification).

## 1. The claim to be proved, stated with all quantifiers

Throughout, a **row-`(d,n)` member** is a pair `(D, ν)` where `ν : A^1 → A^2`, `t ↦ (P(t),Q(t))`,
is a polynomial map that is **birational onto its image** `D`, with `deg_t P = d`, `deg_t Q = n`,
`d > n`. Such a `D` automatically has exactly one place at infinity. Write

* `A_D := C[P,Q] ⊂ C[t]` — the affine coordinate ring of `D` (`ν` birational ⇒ `A_D` has fraction
  field `C(t)` and `C[t]` is its integral closure);
* `v := deg_t`, and `S_D := v(A_D \ {0}) ⊆ N` — the **semigroup at infinity** of `D` in the sense
  of `GM` Definition 2.2 (`S_{C,∞} = {−ν_{C,p}(h) : h ∈ O_C(C∖{p})}`; for a polynomial
  parametrisation `−ν_{C,p}(h) = deg_t h(P,Q)`);
* `δ_aff(D) := Σ_{p ∈ D} δ_p = dim_C C[t]/A_D`, the affine double-point number;
* `Δ = (δ_0, …, δ_g)` — the Abhyankar–Moh δ-sequence of `D`, which by `GM` Theorem 2.1
  **generates** `S_D` and satisfies axioms (1)–(3) there.

The explicit families of the promoted theorem (`CI5` §1) are, for `b ∈ C`, `c ∈ C^*`,

```text
  r = t^3 + b t + c ,      q = t^4 + (2b/3) t^2 + (4c/3) t ,
  D_{b,c}  = image of  t ↦ ( r(t)^2 , q(t) ) ,
  D'_{b,c} = image of  t ↦ ( r(t)^2 + q(t)^2 , q(t) )  =  Φ^{-1}(D_{b,c}),   Φ(x,y) = (x−y^2, y).
```

> **THEOREM EXHAUST.** *Let `(D,ν)` be a member of the campaign's N=4 residual curve rows, i.e.*
>
> * *(i) a row-`(6,4)` member with `Δ = (6,4,3)`, or*
> * *(ii) a row-`(8,4)` member with `Δ = (8,4,6,3)`.*
>
> *Then there exist `T ∈ Aut(A^2)` and an affine reparametrisation `t ↦ λt+μ` (`λ ≠ 0`) of the
> source, and parameters `b ∈ C`, `c ∈ C^*`, such that*
>
> ```text
>      T(D) = D_{b,c}   in case (i),        T(D) = D_{b,c}   in case (ii) as well,
> ```
>
> *and in case (ii) `T` may be taken of the form `T = T_1 ∘ Φ` with `Φ(x,y) = (x−y^2,y)`, so that
> equivalently `Φ^{-1}T(D) = D'_{b,c}` exhibits `D` as an `Aut(A^2)`-image of the octic family
> member. No hypothesis on the affine singularity types is used: nodality is **not** consumed.*

Two quantifier warnings are built into that statement and are discharged in §2.

1. The hypothesis is `Δ`, **not** "`D` is nodal with three nodes". The row-kill target family
   `{D_{b,c} : c ≠ 0}` is strictly larger than the nodal locus (it contains the `D_4` fibre
   `j = 0`, `CLOS` §7), so proving `row ⊆ family` is the useful direction and the extra fibres
   cost nothing: `CI5` §1 kills the family for **every** `c ≠ 0`.
2. `Δ` and the pair `(d,n)` are **gauge-dependent** data of the embedded curve, not invariants of
   `D` up to `Aut(A^2)`; that is precisely why rows `(6,4)` and `(8,4)` are two gauges of one
   geometric class. THEOREM EXHAUST is therefore a statement about a row member *in the gauge in
   which the cage placed it*, and its conclusion is an identification *after* a gauge change. §3
   writes out why that suffices.

## 2. Inventory: what each link actually asserts, and at what quantifier

### 2.1 ROW-SWEEP (a): the delta-sequence census and its gauge

`SWEEP` §2 and `SWREV` §3 assert: among row-`(6,4)` members, the admissible δ-sequences are
exactly `Δ = (6,4,c)`, `c ∈ {3,5,7,9,11}`, and nodal (M-INF) kills `c ∈ {5,7,9,11}`.

I re-ran the census from `GM` Theorem 2.1 directly. With `δ_0=6, δ_1=4`: `d_1=6`, `d_2=4`… in
`GM`'s indexing `d_i = gcd(δ_0,…,δ_{i−1})`, so `d_1=6`, `d_2=gcd(6,4)=2`, `n_1=3`; axiom (2) at
`i=1` is `n_1δ_1 = 12 ∈ ⟨6⟩` ✓. For `δ_2=c`: `d_3 = gcd(2,c)` must be `1` (axiom (1) forbids
`n_2=1`), so `c` is **odd** and the sequence stops at `g=2`; axiom (2) is `2c ∈ ⟨6,4⟩ =
{0,4,6,8,10,…}`, which fails only at `c=1`; axiom (3) is `c < n_1δ_1 = 12`. Hence
`c ∈ {3,5,7,9,11}` — **CONFIRMED**, complete, and with no four-term sequence.

**Gauge.** The census is run at fixed `(δ_0,δ_1) = (deg_t P, deg_t Q) = (6,4)`, i.e. in the
coordinate system the D1-DEGREE cage supplies; it is *not* a census over `Aut(A^2)`-classes.
Two consequences are worth typing because they look like tensions and are not:

* The `(6,4)` gauge is *shear-reduced*: `4 ∤ 6`, so no `P ↦ P − φ(Q)` lowers `deg P`. The `(8,4)`
  gauge is *not*: `4 | 8`, and `P ↦ P − Q^2` drops the degree to `6`. So the `(8,4)` row is the
  same geometry seen in an unreduced gauge — exactly the `Φ`-duplication of `SWEEP` §6.
* Birationality is a hypothesis of the row, not a consequence of `(deg P, deg Q)=(6,4)`. If `ν`
  were `2:1` its image carries a `(3,2)` parametrisation and belongs to a different row. This is
  not idle: it is precisely the `c=0` degeneration of the normal form (§4, step 9).

**Correction (this lane).** `SWREV` §7 lists among its classical facts "the numerical semigroup
`⟨3,4⟩` … is the **unique** oversemigroup of `⟨4,6⟩` of that genus". That is **false**: the
numerical semigroups of genus `3` containing `⟨4,6⟩` are exactly `⟨3,4⟩` (gaps `{1,2,5}`),
`⟨4,5,6,7⟩` (gaps `{1,2,3}`) and `⟨2,7⟩` (gaps `{1,3,5}`) — three, not one. Nothing promoted
rides on it: `SWEEP` §2 uses the safe phrasing ("contains `⟨3,4⟩`, hence is exactly `⟨3,4⟩`" —
valid because `3 ∈ S_D` is known there), and the proof below never uses uniqueness. But the
false sentence must not be reused: "`δ_aff = 3` at `(6,4)` forces `S_D = ⟨3,4⟩`" is **not** a
semigroup-theoretic fact. It is true for row members only through `GM` Theorem 2.1
(`S_D = ⟨Δ⟩`, and among the five admissible `Δ` only `(6,4,3)` has genus `3`).

### 2.2 ROW-NF (b): the normal form and the parametrization it consumes

`ZVK` Theorem ROW-NF reads "*every member of the residual row `Δ=(6,4,3)` is, after a target
automorphism of `A^2` and a reparametrisation of the normalisation,* `x=r^2, y=q, …, c ≠ 0`".
Its §1.1 opens: "*By Theorem FOLD (charged §1.2, **PROVISIONAL as consumed**, but its statement is
all that is used) every member of `Δ=(6,4,3)` is, after a triangular target automorphism,
`D = {(r(t)^2, q(t))}`*". `ZVKREV` §0 accepts this typing explicitly: "*Theorem FOLD's statement
is used as a hypothesis of ROW-NF, and is not re-proved here beyond a spot-check of the semigroup
reduction `p = r^2 +` (linear in `r,q`)*".

So the quantifier of the reviewed ROW-NF is: **every member that is already known to be a fold**
`(r^2,q)` is, after the displayed elementary normalisations, a `D_{b,c}` with `c ≠ 0`. The
`Δ=(6,4,3) ⇒ fold` implication is imported from FOLD, which is not promoted. *That single
implication is the whole exhaustiveness gap at `(6,4)`*, and §4 proves it outright — the
"spot-check" `ZVKREV` alludes to is in fact a complete argument once the semigroup is nailed.

Two further quantifier facts about ROW-NF, both needed downstream:

* `ZVKREV` §1.2 gives a Puiseux-free derivation of the coefficient conditions `(1.2)` from *"the
  minus-branch system has no solution with `t ≠ s`"*. That hypothesis is **not** the row
  hypothesis. The row hypothesis is `δ_aff(D)=3`; the bridge `δ_aff(D)=3 ⇒ m=0` is used but not
  proved in either report (`ZVK` routes through Lemma 1.2's resultant count; `ZVKREV` §1.4 proves
  only the converse, `(1.2) ⇒ δ_aff=3`). §4, step 8 supplies the forward bridge, and shows the
  minus-branch condition must be strengthened by two degenerate cases (`r(t)=r(s)=0`, and
  `t=s` with `q'(τ)=0` at a root of `r`) that the quartic `N` in fact already sees.
* The normalisations "translate `t`, translate and scale `y`" are target automorphisms plus a
  source affine change; `x` is rescaled once. All are in `Aut(A^2)`. The residual `t ↦ αt` action
  with weights `(2,3)` on `(b,c)` shows the family is one-dimensional with modulus `j = b^3/c^2`,
  but the promoted kill covers every `(b,c)` with `c ≠ 0` anyway, so no orbit bookkeeping is
  needed.

### 2.3 The D1-DEGREE cage (c): invariants up to Aut(A^2)

The cage supplies `(d,n)` and the residual class ("every affine singular point exactly two smooth
branches", `SWEEP` §1). What must be checked is that the campaign is *licensed* to replace `D_1`
by `T(D_1)`. It is, and the licence is already load-bearing in promoted material:

* `SWREV` §1 ("Invariance") re-states D1-DEGREE hostile-review Item 1 and observes that its
  argument "never uses that shape": for any biregular `T` of the target, `det dT` constant
  preserves the Keller property, `A_{T∘F} = T(A_F)`, and the finite cover, branch locus, fibre
  cardinalities, `a_D`, `a_p`, meridian classes and the two-smooth-branch local type all pull
  back. Over `C` **every** `T ∈ Aut(A^2)` has constant nonzero Jacobian (it is a unit in
  `C[x,y]`), so the "Jacobian 1" phrasing is not a restriction: scalings are included.
* The two `(6,3)` kills that `SWEEP`/`SWREV` **promote** are themselves triangular-automorphism
  reductions (`T(u,v) = (u−φ(v),v)`) into the coprime Main Theorem. Refusing the licence here
  would retract those kills.

What the cage does **not** give is a canonical gauge: `Δ`, `(d,n)`, `β_1`, `M_∞`, the projective
degree and the germ at infinity are all gauge-dependent (`CLOS` §4's adjudication table lists
exactly these as "does not transport"). The two data that *do* transport are the pair
`(A^2, D)` up to isomorphism and `π_1` with its meridian conjugacy class (`CLOS` §3,
**CONFIRMED**). §3 shows those two are all the composition needs.

### 2.4 ROW-84 (d): `deg(P−Q^2)=6 ⟺ Δ=(8,4,6,3)`

`CLOS` §1 re-derives this as an identity from the monic `(8,4)` parametrisation, the definition
`δ_2 = min{deg(P−φ(Q)) : deg φ ≤ 2}`, and `δ_aff=3`, in two independent ways (the chart order
`ord_s(w−v^2) = 16 − deg(P−Q^2)`, and the direct minimisation). Verdict **CONFIRMED**,
unconditional, consuming no ROW-NF and no literature. §5 reproves it a third way, in the
semigroup basis, where it appears as the vanishing of one basis coefficient; this is the form in
which it feeds exhaustiveness.

## 3. The composition: transport of the S_4 representation through `T ∈ Aut(A^2)`

This is the argument the charge asks to see written out. It is short, but every clause is a
place where a gauge-dependent invariant could be smuggled in, so each is displayed.

Let `D_1` be a campaign residual curve in row `(6,4)` or `(8,4)`, and let

```text
   Ψ : π_1(C^2 ∖ D_1, *) ↠ S_4 ,     Ψ(meridian of D_1) ∈ {transpositions}
```

be the forbidden object (the campaign's `S_4` datum is a quotient of the complement of the single
curve `D_1`: `SWEEP` §1, §2, and the M-INF gate "`M_∞ ≤ 3d−3 ⇒ π_1(C^2−D)=Z` and hence kills the
prescribed `S_4` quotient"). Let `T ∈ Aut(A^2)` be the automorphism produced by THEOREM EXHAUST,
so `T(D_1) = D_{b,c}` with `c ≠ 0`.

1. **Complement isomorphism.** `T` is biregular on `A^2` and carries `D_1` onto `D_{b,c}` as a
   set, hence restricts to a biregular isomorphism `T : C^2 ∖ D_1 → C^2 ∖ D_{b,c}`, with
   biregular inverse. In particular it is a diffeomorphism of the two complements.
2. **`π_1` isomorphism.** `T_* : π_1(C^2∖D_1, *) → π_1(C^2∖D_{b,c}, T(*))` is an isomorphism of
   groups. The base-point choice is immaterial: both surjectivity onto `S_4` and "every meridian
   is a transposition" are invariant under composing with an inner automorphism, and change of
   base point along a path is exactly that.
3. **Meridians go to meridians.** A meridian of an irreducible affine curve `D` is the class of
   the positively oriented boundary of a small disc transverse to `D` at a smooth point. `T` is
   holomorphic with `dT` invertible and `C`-linear, so it maps smooth points of `D_1` to smooth
   points of `D_{b,c}`, small transverse discs to small transverse discs, and preserves the
   complex (hence the induced) orientation of the disc. So `T_*` sends meridians to meridians —
   not to inverse meridians (`CLOS` §3, **CONFIRMED**, same argument with `Φ`). Both curves are
   irreducible with connected smooth locus, so meridians form a single conjugacy class in each,
   and `T_*` carries that class *onto* the target class.
4. **Composition.** Suppose `Ψ` exists. Then `Ψ ∘ (T_*)^{-1} : π_1(C^2 ∖ D_{b,c}) ↠ S_4` is a
   surjection, and by (3) it sends every meridian of `D_{b,c}` to a transposition (given a
   meridian `m` of `D_{b,c}`, `(T_*)^{-1}(m)` is a meridian of `D_1`, whose `Ψ`-image is a
   transposition by hypothesis). This contradicts the promoted theorem (`CI5` §1), which forbids
   exactly this for **every** `c ≠ 0`. Hence no such `Ψ` exists on `D_1`. ∎

**Why the gauge-dependence of §2.3 is harmless.** The composition consumes only items (1)–(3),
i.e. the pair `(A^2,D)` up to isomorphism and `π_1` with its meridian class. It consumes **no**
projective degree, no germ at infinity, no `β_1`, no `M_∞`, no braid basis, no `γ_∞`, and no
line pencil — precisely the objects `CLOS` §4 certifies as *non*-transporting. The direction of
inference also matters: a *non-existence* statement is pulled back along `T`, so nothing has to
be re-established downstairs about `D_1`'s infinity data. This is the fork `CLOS` §4 records the
gate as having taken ("if 'target-equivalent' means an actual `T ∈ Aut(A^2)`, then
`A^2∖D ≅ A^2∖T(D)` and the transposition-quotient property transfers regardless of degree,
pencil, or braid basis").

**Two scope clauses, typed, not waved.**

* *`T(D_1)` is still a campaign object.* Not needed for step 4, but true and already promoted:
  by the invariance item of §2.3 the Keller property, the cover, the branch locus, `a_p` and the
  two-smooth-branch local type all transport. So the identification does not smuggle `D_1` out of
  the residual class; it re-gauges it.
* *Single-curve scope.* Steps 1–4 are for the complement of the one curve `D_1`. If a residual
  configuration carried further components, the relevant complement would be that of the whole
  divisor and `Ψ` would not descend to `C^2∖D_1`; the rows swept here are single-curve rows, and
  nothing below is claimed for a reducible configuration.

## 4. Proof of THEOREM EXHAUST at `(6,4)`

Let `(D,ν)`, `ν = (P,Q)`, be a row-`(6,4)` member with `Δ = (6,4,3)`. Write `A_D = C[P,Q]`,
`S_D = v(A_D∖0)`.

**Step 0 (the two identities used throughout).** `ν` birational ⇒ `C[t]` is the integral closure
of `A_D` and `A^1` is the normalisation of `D` with `ν` the normalisation map, so

```text
   δ_aff(D) = dim_C ( ν_* O_{A^1} / O_D ) = dim_C C[t]/A_D = # ( N ∖ S_D ) .        (4.1)
```

The middle equality is the definition of the double-point number; the right-hand one holds
because a `C`-basis of `A_D` adapted to the degree filtration has one element in each degree of
`S_D` and no two of the same degree, so `dim_C C[t]_{≤m}/(A_D)_{≤m} = #([0,m] ∖ S_D)`. Second,
by `GM` Definition 2.2 and Theorem 2.1, `S_D` is *generated* by `Δ`.

**Step 1 (`3 ∈ S_D`).** Immediate from Step 0: `δ_2 = 3` is an entry of `Δ` and `Δ ⊆ ⟨Δ⟩ = S_D`.
Only this containment direction is used — the reversed direction (`S_D ⊆ ⟨Δ⟩`) is never invoked.
Fix `R ∈ A_D` with `deg_t R = 3`.

**Step 2 (`S_D = ⟨3,4⟩` and `δ_aff(D)=3`).** The germ of `D̄` at its unique point at infinity has
`(ord v, ord w) = (a,d) = (2,6)`; the AM cluster of `Δ=(6,4,3)` is `(2^7,1,1)`, giving
`δ_∞ = 7` (`SWEEP` §2, `SWREV` §3, both re-derived there from the corrected cluster identity).
With `p_a = (6−1)(6−2)/2 = 10` the genus split gives `δ_aff(D) = 10 − 7 = 3`. By (4.1),
`#(N∖S_D) = 3`. Since `3,4 ∈ S_D` we have `S_D ⊇ ⟨3,4⟩`, whose gap set `{1,2,5}` already has
three elements; a strictly larger semigroup would have fewer gaps. Hence `S_D = ⟨3,4⟩`.
*(Cross-check, not used: `⟨Δ⟩ = ⟨6,4,3⟩ = ⟨3,4⟩` directly. The two routes agree, which is the
non-circular consistency check; the semigroup-uniqueness sentence corrected in §2.1 is not used.)*

**Step 3 (`C[R,Q] = A_D`, with an explicit basis).** `C[R,Q] ⊆ A_D`, and
`v(C[R,Q]) ⊇ ⟨3,4⟩ = S_D ⊇ v(C[R,Q])`, so both rings have the same value semigroup; by the
degree-filtration count of Step 0 they have the same finite codimension in `C[t]`, hence

```text
   C[R,Q] = C[P,Q] = A_D ,   and   v = deg_t  maps  A_D  onto  ⟨3,4⟩ .
```

Every `s ∈ ⟨3,4⟩` is uniquely `s = 3i+4j` with `i ≥ 0`, `0 ≤ j ≤ 2` (`j ≡ s mod 3` fixes `j`,
then `i = (s−4j)/3`). The monomials `{R^iQ^j : i ≥ 0, 0 ≤ j ≤ 2}` therefore have pairwise
distinct degrees, all in `S_D`, so they are `C`-independent; and since every element of `A_D` has
degree in `S_D`, subtracting the unique matching monomial strictly lowers the degree, so the
reduction terminates and they **span**. They are a basis.

**Step 4 (the fold is forced).** `deg P = 6`. The basis monomials of degree `≤ 6` are
`1, R, Q, R^2` (degrees `0,3,4,6`), and only `R^2` has degree `6`. Hence

```text
   P = α R^2 + β Q + γ R + ε ,     α ≠ 0 ,   β,γ,ε ∈ C .                            (4.2)
```

**This is Theorem FOLD, proved rather than assumed**, and it is the link the closure review
retained as PROVISIONAL. No nodality, no Puiseux expansion and no literature beyond `GM`
Theorem 2.1 entered: only `3 ∈ S_D`, `δ_aff = 3` and a dimension count.

**Step 5 (an explicit `T_1 ∈ Aut(A^2)`).** Complete the square: put `R̃ := R + γ/(2α)`, still of
degree `3` and still with `C[R̃,Q] = A_D`; then `P = α R̃^2 + βQ + ε'`, `ε' = ε − γ^2/(4α)`. Set

```text
   T_1(x,y) := ( α^{-1}( x − β y − ε' ) , y ) ,    T_1^{-1}(x,y) = ( αx + βy + ε' , y ) ,
   Jac T_1 = α^{-1} ∈ C^* ,     T_1 ∈ Aut(A^2)  (triangular, affine in x over y).
```

Then `T_1 ∘ ν = ( R̃^2 , Q )`, i.e. `T_1(D)` is the image of `t ↦ (R̃(t)^2, Q(t))`.

**Step 6 (normalisation).** Write `R̃ = a_3t^3 + a_2t^2 + …`, `Q = e_4t^4 + …`. Replace `t` by
`t + β_0` with `β_0 = a_2/(3a_3)` to kill the `t^2` term of `R̃`; rescale `x` by `a_3^{-2}` and
`y` by `e_4^{-1}`, and translate `y` by the constant term. All target moves are linear/affine
automorphisms of `A^2` composed into `T_1`; the source move is an affine reparametrisation. The
result is `T(D) = ` image of `t ↦ (r(t)^2, q(t))` with

```text
   r = t^3 + b t + c ,      q = t^4 + q_3 t^3 + q_2 t^2 + q_1 t .                    (4.3)
```

`T ∈ Aut(A^2)` is an automorphism, so `T(D)` has the same coordinate ring inside `C[t]`
(`C[r^2,q] = C[P,Q] = A_D`), hence the same `S_D = ⟨3,4⟩` and the same `δ_aff = 3`. Also
`C[r,q] = C[R̃,Q] = A_D = C[r^2,q]`, i.e. **`r ∈ C[r^2,q]`** — the fold is semigroup-trivial.

**Step 7 (`δ_aff` of the unfolded curve is 3, always).** Let `D'` = image of `t ↦ (r(t),q(t))`.
Its projective closure is a quartic (`max(3,4)=4`) with a single point at infinity where
`(ord v, ord w) = (1,4)`, i.e. multiplicity one: smooth. So `δ_∞(D') = 0` and
`δ_aff(D') = p_a = 3`, unconditionally in `(b,c,q_3,q_2,q_1)`. With (4.1),
`v(C[r,q]) = ⟨3,4⟩` and, since `C[r^2,q] ⊆ C[r,q]`,

```text
   δ_aff(D) = 3 + dim_C C[r,q]/C[r^2,q] ,     so    δ_aff(D) = 3  ⟺  r ∈ C[r^2,q] .   (4.4)
```

**Step 8 (the coefficient conditions are forced).** Put `e_1 = t+s`, `e_2 = ts`. From the power
sums `t^4−s^4 = (t−s)e_1(e_1^2−2e_2)`, `t^3−s^3 = (t−s)(e_1^2−e_2)`, `t^2−s^2 = (t−s)e_1`,

```text
   Dq := [q(t)−q(s)]/(t−s) = e_1(e_1^2−2e_2) + q_3(e_1^2−e_2) + q_2 e_1 + q_1 .
```

The minus branch is `r(t)+r(s) = e_1^3 − 3e_1e_2 + be_1 + 2c = 0`, i.e. (for `e_1 ≠ 0`)
`e_2 = (e_1^2+b)/3 + 2c/(3e_1)`. Substituting and multiplying by `−3e_1`:

```text
   N(e_1) := −3e_1·Dq
           = −e_1^4 − 2q_3 e_1^3 + (2b−3q_2) e_1^2 + (q_3 b + 4c − 3q_1) e_1 + 2c q_3 .  (4.5)
```

*(Hand-verified here from the displayed power sums; it reproduces `ZVKREV` §1.2 exactly.)*

*Claim: `δ_aff(D)=3` forces `N ≡ −e_1^4`.* Suppose `N(e_1^*) = 0` with `e_1^* ≠ 0`; let
`e_2^*` be as above and `t,s` the roots of `X^2 − e_1^*X + e_2^*`. Then `r(t)+r(s)=0` and
`(t−s)·Dq = q(t)−q(s) = 0`.

* If `t ≠ s` and `r(t) ≠ 0`: every `F ∈ C[r^2,q]` satisfies `F(t)=F(s)` (both `r^2` and `q` do),
  while `r(t) = −r(s) ≠ r(s)`. So `r ∉ C[r^2,q]` and (4.4) gives `δ_aff(D) ≥ 4`.
* If `t ≠ s` and `r(t) = r(s) = 0`: `D'` has two branches at `(0,y_0)`, `u = u_i(y)` with
  `u_i(y_0)=0`; their contact is `ord(u_1−u_2)`, while the corresponding branches of `D` are
  `x = u_i(y)^2` with contact `ord(u_1^2−u_2^2) = ord(u_1−u_2) + ord(u_1+u_2) ≥ ord(u_1−u_2)+1`.
  So `δ` strictly increases at that point, and `θ(u,y)=(u^2,y)` is a local isomorphism at every
  other point of `D'` with `u ≠ 0` (Jacobian `2u`) and at every simple `u=0` point where `y` is a
  local coordinate. Hence `δ_aff(D) ≥ δ_aff(D')+1 = 4`.
* If `t = s`: then `e_1^{*2} = 4e_2^*`, `2r(t)=0` and `Dq|_{t=s} = q'(t) = 0`, i.e. `τ := t` is a
  root of `r` with `q'(τ)=0`. Then `x = r(t)^2` and `y − q(τ)` both vanish to order `≥ 2` at
  `τ`, so `D` has a branch of multiplicity `≥ 2` at `(0,q(τ))`, whereas `D'` is unibranch of
  multiplicity `1` there. Again `δ_aff(D) ≥ 4`.

`N` has leading coefficient `−1`, so "no nonzero root" is equivalent to the vanishing of its four
lower coefficients:

```text
   q_3 = 0 ,     q_2 = 2b/3 ,     q_1 = 4c/3 ,     ( 2c q_3 = 0 automatic ) .          (4.6)
```

That is exactly `ZVK` `(1.2)`, now derived **from the row hypothesis** `δ_aff(D)=3` rather than
from the auxiliary hypothesis "the minus branch is empty".

**Step 9 (`c ≠ 0`).** Suppose `c = 0`. Then `r = t^3+bt` is odd and, by (4.6), `q = t^4+(2b/3)t^2`
is even; so `x = r^2` and `y = q` are both even, `ν` factors through `t ↦ t^2`, and `ν` is `2:1`
— contradicting birationality (the image then carries a `(3,2)` parametrisation and is not a
row-`(6,4)` member at all). Hence `c ≠ 0`, and `T(D) = D_{b,c}`. ∎

Combining: `T(D) = D_{b,c}` with `c ≠ 0`, `T ∈ Aut(A^2)` explicit. Conversely every `D_{b,c}`
with `c ≠ 0` is a row-`(6,4)` member with `Δ=(6,4,3)` (`ZVKREV` §1.4, `SWREV` §3), so the
inclusion is an equality of `Aut(A^2)`-classes, not merely a containment.

## 5. Proof of THEOREM EXHAUST at `(8,4)`

Let `(D,ν)` be a row-`(8,4)` member with `Δ = (8,4,6,3)`.

**Steps 1–2.** `δ_3 = 3 ∈ ⟨Δ⟩ = S_D` (`GM` Theorem 2.1), so pick `R ∈ A_D` of degree `3`. The AM
cluster of `(8,4,6,3)` is `(4^2,2^6,1^2)`, `δ_∞ = 18` (`SWEEP` §6, `SWREV` §4), and
`p_a = (8−1)(8−2)/2 = 21`, so `δ_aff(D) = 3`. By (4.1) and `3,4 ∈ S_D`, exactly as in §4 Step 2,
`S_D = ⟨3,4⟩`, and by §4 Step 3 `A_D = C[R,Q]` with basis `{R^iQ^j : j ≤ 2}`.

**Step 4′ (the octic expansion, and a third proof of ROW-84).** The basis monomials of degree
`≤ 8` are `1, R, Q, R^2, RQ, Q^2` of degrees `0,3,4,6,7,8`, so

```text
   P = c_{02} Q^2 + c_{11} RQ + c_{20} R^2 + c_{01} Q + c_{10} R + c_{00} ,   c_{02} ≠ 0 .  (5.1)
```

Now compute `δ_2 = min{ deg_t (P − φ(Q)) : φ ∈ C[y] }`. For `deg φ ≥ 3`, `deg φ(Q) ≥ 12 > 8`, so
the minimum is attained with `deg φ ≤ 2`, and then `φ(Q) = λ_2Q^2 + λ_1Q + λ_0` is a combination
of basis monomials. Subtracting it changes only `c_{02}, c_{01}, c_{00}`. Since basis monomials
have distinct degrees, the degree of the difference is the largest degree with a surviving
nonzero coefficient. Hence

```text
   δ_2 = 8 if λ_2 ≠ c_{02};  else  7 if c_{11} ≠ 0;  else  6 if c_{20} ≠ 0;  else ≤ 4 .
   So    δ_2 = 6   ⟺   c_{11} = 0  and  c_{20} ≠ 0   ⟺   deg(P − c_{02}Q^2) = 6 .
```

This reproves `CLOS` §1's equivalence `Δ=(8,4,6,3) ⟺ deg(P−Q^2)=6` a third way (the review's two
routes were the chart order `ord_s(w−v^2)=16−m` and the direct minimisation), and it is the form
exhaustiveness needs: **`δ_2 = 6` is exactly the vanishing of the one basis coefficient `c_{11}`
that obstructs the fold.**

**Step 5′.** With `c_{11}=0`, complete the square in `R`: `R̃ := R + c_{10}/(2c_{20})`, so
`P = c_{20}R̃^2 + c_{02}Q^2 + c_{01}Q + ε'`. Set

```text
   T_1(x,y) := ( c_{20}^{-1} ( x − c_{02} y^2 − c_{01} y − ε' ) , y ) ,
   T_1^{-1}(x,y) = ( c_{20}x + c_{02}y^2 + c_{01}y + ε' , y ) ,   Jac T_1 = c_{20}^{-1} ∈ C^* ,
```

a triangular (hence biregular) automorphism of `A^2`, with `T_1∘ν = (R̃^2, Q)`. Note
`T_1 = (scaling) ∘ (x,y)↦(x−c_{01}y−ε', y) ∘ Φ_{c_{02}}`, `Φ_λ(x,y) := (x−λy^2,y)`: the reviewed
shear `Φ` is literally the `Q^2`-clearing factor of `T_1`, and the `c_{11}RQ` term — which would
have left an irreducible degree-`7` residue and no fold — is absent by `Δ`.

**Steps 6–9.** Verbatim as in §4: those steps consume only `deg r = 3`, `deg q = 4`,
`δ_aff = 3` (invariant under `T_1`) and birationality of `ν`. They give the normalisation (4.3),
the forced coefficients (4.6) and `c ≠ 0`. Hence `T(D) = D_{b,c}` with `c ≠ 0`, and equivalently
`Φ^{-1}T(D) = D'_{b,c}`. ∎

The `(8,4)` case therefore needs no separate machinery and, in particular, does **not** consume
the `Φ`-transport of the kill: it lands on `D_{b,c}` directly. The `Φ`-transport (`CLOS` §§2–3)
remains the right statement for identifying the two *families*, and is unaffected.

## 6. Verdict, and the exact typed status of each residual obligation

**Verdict: THEOREM EXHAUST is PROVED, not typed OPEN.** The link the closure review retained as
PROVISIONAL — "`Δ=(6,4,3)` member ⇒ fold `(r^2,q)` after a target automorphism" (Theorem FOLD's
statement, imported by `ZVK` §1.1) — is §4 Step 4, a four-line consequence of `3 ∈ S_D`,
`δ_aff = 3` and a degree-filtration dimension count. Combined with §3, the promoted row-kill
covers the campaign rows outright:

> **COROLLARY.** *No campaign residual curve in row `(6,4)` with `Δ=(6,4,3)`, and none in row
> `(8,4)` with `Δ=(8,4,6,3)`, admits a surjection `π_1(C^2∖D_1) ↠ S_4` carrying every meridian to
> a transposition.*

**Everything the corollary rides.**

1. `GM` Theorem 2.1 (published, re-fetched, hash `637acfd1…`): the δ-sequence *generates* the
   semigroup at infinity. Only `Δ ⊆ S_D` is used; the reverse containment is never invoked, and
   the Remark 2.1 "change of variables" caveat is harmless because `GM` states
   `S_{C',∞} = S_{C,∞}` for it.
2. `δ_∞ = 7` at `(6,4,3)` and `δ_∞ = 18` at `(8,4,6,3)`, from the corrected cluster identity
   (`SWEEP` §1–2, §6; `SWREV` §2–4, CONFIRMED). Doubly sourced: `#gaps⟨Δ⟩ = 3` gives the same
   `δ_aff` and the two routes agree.
3. Birationality of `ν` as part of the row definition (used twice: for (4.1), and for `c ≠ 0`).
4. The `Aut(A^2)` licence of §2.3 — already load-bearing in the promoted `(6,3)` kills.
5. The promoted ROW-KILL theorem (`CI5` §1) at its corrected scope, for every `c ≠ 0`.

**Not consumed:** Theorem FOLD (proved instead); ROW-NF as a black box (re-derived, and its
coefficient conditions re-founded on the row hypothesis); nodality or any affine-singularity
typing; M-INF; A'(1)–(4); any AM converse or realisation statement; the `Φ`-transport of the kill
(the `(8,4)` proof lands on `D_{b,c}` directly); `FIXED-TUPLE`; the semigroup-uniqueness sentence.

**Three repairs this lane records.**

* **(C1)** `SWREV` §7's classical-fact "`⟨3,4⟩` is the unique genus-`3` oversemigroup of `⟨4,6⟩`"
  is **false** (three such: `⟨3,4⟩`, `⟨4,5,6,7⟩`, `⟨2,7⟩`). Not load-bearing anywhere; must not
  be reused as "`δ_aff=3` at `(6,4)` forces `S_D=⟨3,4⟩`", which is true only through `GM`.
* **(C2)** The derivation of `(1.2)` in `ZVK` §1.3 / `ZVKREV` §1.2 starts from *"the minus branch
  has no solution"*; the row hypothesis is `δ_aff(D)=3`. §4 Step 8 supplies the missing forward
  bridge and shows it also disposes of two degenerate configurations the phrase "minus pair"
  does not name (a pair with `r(t)=r(s)=0`, and `t=s` at a root of `r` with `q'(τ)=0`) — both are
  already visible as roots of the same quartic `N`, so `(1.2)` is unchanged.
* **(C3)** `c ≠ 0` is forced by **birationality** (§4 Step 9), an elementary argument that does
  not consume `ZVK` Lemma 1.2's resultant count nor the inequality `2m−5 ≥ −5`.

**Typing of this report.** Single-model, desk-scale, unreviewed. Under campaign practice a
flagship promotion needs a different-model hostile gate; the recommended charge is §4 Steps 1–4
(the semigroup/fold core), §4 Step 8 (the forward bridge with its three cases), and §5 Step 4′
(the basis reproof of ROW-84). Until that gate runs, the correct label is
**PROVED-HERE / REVIEW-PENDING**, not PROMOTED — the same discipline `CI5` §3 applies to
"exhaustiveness lemma … separately promoted".

**What EXHAUST does *not* do.** It does not touch the cage's list of rows `(d,n)`, nor the
census within a row (`Δ=(6,4,3)` sole nodal survivor), nor M-INF. Those remain exactly as
`SWEEP`/`SWREV` promoted them, at the nodal quantifier. EXHAUST is the identification step only.

## 7. What remains of the N=4 residual if EXHAUST lands

`SWEEP` §10 / `SWREV` §7 sweep eight rows. Four were already KILLED (`(6,3)`–`(7,4)` and
`(6,3)`–`(8,3)` by triangular reduction into the promoted coprime Main Theorem; nodal `(8,2)` and
nodal `(9,3)` by M-INF). With EXHAUST plus §3, rows nodal `(6,4)` and nodal `(8,4)` — one
geometric class, not two — are **KILLED** as well. What remains is exactly the six AM-numerical
types of rows `(8,6)` and `(9,6)`:

```text
 (8,6):  Δ=(8,6,11) (β_1;δ_∞,δ_aff;M_∞)=(21;10,11;22)   S_D=⟨6,8,11⟩
         Δ=(8,6,9)                      (23;11,10;24)   S_D=⟨6,8,9⟩
         Δ=(8,6,7)                      (25;12, 9;26)   S_D=⟨6,7,8⟩
         Δ=(8,6,3)                      (29;14, 7;30)   S_D=⟨3,8⟩
 (9,6):  Δ=(9,6,4)                      (23;22, 6;25)   S_D=⟨4,6,9⟩
         Δ=(9,6,2)                      (25;24, 4;27)   S_D=⟨2,9⟩
```

and for each the two open obligations are unchanged: an in-class **nodal realisation or
exclusion** (Galindo's converse produces a one-place curve of the stated δ-sequence, *not* an
`A^1`-normalisation with the required number of reduced off-diagonal double fibres), or a
**noncoprime fixed-tuple theorem** with route-to-node data. `OPEN[ROW-(8,6)-NODAL-REALIZATION
+S4-TUPLE]` and `OPEN[ROW-(9,6)-NODAL-REALIZATION+S4-TUPLE]` stand verbatim. EMPTY or KILLED on
all six ⟹ B0 closes at N=4 unconditionally (`CI5` §2.3), with the ROW-NF exhaustiveness
dependency discharged rather than assumed.

**Successor handle (observation of this lane, unreviewed).** The §4 method is not row-specific:
it applies verbatim whenever `S_D` has a generator strictly below `n`. Exactly two of the six
types qualify. For `Δ=(8,6,3)`, `S_D=⟨3,8⟩`, so `A_D = C[R,P]` with `deg R=3` and
`Q = αR^2+βR+γ` (`α≠0`); completing the square, a linear automorphism in `y` puts the curve in
the form `(P, R̃^2)` — a **`y`-fold of a coprime `(8,3)` pair**, i.e. the exact analogue of
`D_{b,c}` one row up. For `Δ=(9,6,2)`, `S_D=⟨2,9⟩`, `A_D=C[Z,P]` with `deg Z=2` and `Q` a cubic
in `Z`. The other four types have `min(S_D∖0) ≥ 4` and admit no such reduction. A closed normal
form for those two types looks reachable by the same desk-scale route.

## 8. Sources consulted

Charged frozen inputs: hashes in §0, all six verified before reading.

Primary literature, re-fetched and re-hashed on this host:

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9   241372 bytes
  C. Galindo, F. Monserrat, "The Abhyankar-Moh theorem for plane valuations at infinity",
  arXiv:0910.2613v2,  https://arxiv.org/pdf/0910.2613v2
  Consumed: Definition 2.2 (semigroup at infinity, p. 2); Theorem 2.1 (δ-sequence axioms and
  "Δ generates S_{C,∞}", p. 3) with Remark 2.1. Proposition 2.1 not re-derived; the cluster
  conversions are taken from `SWEEP`/`SWREV` at their reviewed scope.
```

Classical facts used without a hashed citation: `δ = dim_C(ν_*O/O)` for a birational
normalisation; `p_a = (d−1)(d−2)/2`; a plane branch of multiplicity one is smooth; automorphisms
of `A^2` over `C` have constant nonzero Jacobian; power-sum divided differences; a nonconstant
complex polynomial has a root.

Promoted campaign statements consumed at their written scopes, not re-proved: Theorem ROW-KILL as
corrected (`CI5` §1); the `Aut(A^2)` invariance of the residual class (D1-DEGREE hostile review
Item 1 as re-stated in `SWREV` §1); the corrected cluster identity and the `(6,4)`/`(8,4)`
δ-censuses (`SWEEP` §§2,6; `SWREV` §§3–4); `Φ_*` meridian transport (`CLOS` §3).

Not consumed: Theorem FOLD; ROW-NF as a black box; M-INF; (M-INF-T); A'(1)–(5); any AM converse;
Shirane Cor. 0.6 and Oka05 (they sit inside promoted ROW-KILL and are not re-opened here).

<!-- BODY-END -->
