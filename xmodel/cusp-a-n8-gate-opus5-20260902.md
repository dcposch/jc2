# CUSP-A-N8-GATE — case (A) is void at every degree

Lane: `CUSP-A-N8-GATE`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation (two independent proofs) plus exact integer permutation
and homology computation. No Groebner, no CAS decision procedure, no AWS.
Instrument `box/cover_h1.py` consumed by byte-identical copy, unmodified;
drivers in `/tmp/cuspa`, not installed in `box/`.

## 0. Custody, instrument, method

The three charged frozen copies were hashed with `shasum -a 256` **before
any was read**; 3/3 match the charge:

```text
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  homcover-transfer-opus5-20260902.md
fadc17c809e72d64a493fc1fb16a739d441474b401f191081303de3b003d7d62  homcover-transfer-review-gpt55-20260902.md
```

Below: **SW** = the case-A sweep, **HT** = the transfer report, **HV** =
its hostile review. Instrument, as run:

```text
dfb90ce32f589aae00ce7f2d3188114bbf27396120a8da3d8e67c0145b5177b2  box/cover_h1.py
dfb90ce32f589aae00ce7f2d3188114bbf27396120a8da3d8e67c0145b5177b2  /tmp/cuspa/cover_h1.py   (copy, as charged)
```

`python3 box/cover_h1.py` — 4/4 built-in controls PASS on this host,
including the sharp `Z (+) Z/3` trefoil control and the fail-closed
convention discriminator. Every homology number below was produced
through `to_transport_convention`; no `ValueError` was suppressed. A
second, independent implementation (Reidemeister–Schreier + integer SNF,
`/tmp/cuspa/rs_fox.py` + `/tmp/cuspa/snf.py`) recomputes `H^ab` for every
record and agrees with `cover_h1` on rank and torsion in 32/32 cases
(§9, control C3). No charged file was edited; no repository file was
modified.

No `charge_basis` line: this report asserts no new exit price.

## 1. Verdict

```text
OPEN[HOMCOVER-CUSP-A-N8]      CLOSED NEGATIVE, and not only at N = 8.
```

Two independent gates were found. Each of them, alone, kills all 26
charged survivors; each of them, alone, closes MPRIME case (A) at
**every** degree `N >= 2`.

```text
THEOREM NO-CUSP-PREIMAGE  In case (A) the cusp point c of A_F has NO preimage
                          under F.  Hence E = F^{-1}(A_F) is a SMOOTH affine
                          curve and F|_E : E -> A_F \ {c} = C^* is etale.
                          PROVED HERE.  (This corrects the charge's premise.)

THEOREM CUSP-A-VOID       chi(E) = 1 forces a component E_i = A^1, and there is
  (Chain I, Euler)        no non-constant morphism A^1 -> C^*.  Case (A) is
                          EMPTY for every N >= 2.  PROVED HERE.  H2-free.

THEOREM PERIPHERAL-RANK   #orbits<rho(m),rho(z)> = j ; equivalently the base
  (Chain II, part 1)      orbifold of the Seifert fibration of the cover has
                          GENUS 0.  PROVED HERE.  New; sharpens ORBIFOLD-CAGE.

THEOREM MERIDIAN-SPAN     kappa * j <= a.  PROVED HERE.  New; the meridian
  (Chain II, part 2)      lifts over one <rho(z)>-block are all conjugate in H.

THEOREM CUSP-A-VOID-II    PERIPHERAL-RANK gives a <= kappa*j, MERIDIAN-SPAN
  (Chain II)              gives a >= kappa*j; equality forces rho(m) = 1, i.e.
                          a = N, against W = N - a >= 2.  Case (A) EMPTY for
                          every N >= 2.  PROVED HERE.  Purely representation-
                          level, fully machine-checkable.

COROLLARY CUSP-A-KAPPA    SW's conjecture is PROVED, by a stronger route: every
                          kappa = 1 cell is empty at every N, from PERIPHERAL-
                          RANK alone.  (So is every kappa >= 2 cell.)

COROLLARY kappa | a       free by-product; cuts the numerical cage.
```

Measured on the charged residual:

```text
                                  j  a  kappa  t  c  kappa|a  PERIPH  MER-SPAN
trefoil cell (2,3) 16 reps        2  2    2    2  2   pass     pass     FAIL
trefoil cell (3,2)  6 reps        2  2    2    2  2   pass     pass     FAIL
family (3,4D)       6 reps        3  4    2    3  3   pass     pass     FAIL
family (4D,3)       4 reps        3  4    2    3  3   pass     pass     FAIL
N=9 spot (F9.1)     6 reps        2  3    3    2  2   pass     pass     FAIL
```

All 26 charged survivors (32 records in my normalisation, §5) fail
MERIDIAN-SPAN; all pass every previously banked gate and both new *free*
ones (`kappa | a`, PERIPHERAL-RANK). The family collapse is re-measured at
`D = 1, 5, 7, 11, 13` with identical verdicts. Not claimed: anything about
case (B3), `(9,6,2)`, `(9,6,4)`, `Z(G)`, JC2 at any degree, or the
existence of `F` outside case (A).

## 2. The datum the charge gets wrong

The charge states, as pinned background:

> `F` is étale, so `E` has exactly `a` singular points, each ANALYTICALLY
> a `(p,q)` cusp.

The count `a` is right for a **generic** point of `A_F` and wrong for the
**cusp** point. The two are separated by exactly one fact: at a generic
`y in A_F` the local group is cyclic, at the cusp `c` it is the whole
global group.

> **THEOREM NO-CUSP-PREIMAGE.** Let `F : C^2 -> C^2` be Keller of degree
> `N >= 2` with non-properness set `A_F`, let `c in A_F` be a point such
> that `pi_1(B_c \ A_F) -> pi_1(C^2 \ A_F)` is **surjective** for a small
> ball `B_c`. Then `F^{-1}(c) = empty`.
>
> *Proof.* `F` is proper over `X := C^2 \ A_F` and étale, so
> `F : Y := C^2 \ E -> X` is a covering of degree `N`, `E := F^{-1}(A_F)`;
> `Y` is connected (complement of a curve in `C^2`), so the classifying
> `rho : pi_1(X) -> S_N` is transitive. Suppose `x in F^{-1}(c)`. Étale
> means local biholomorphism: choose `U ni x` with `F|_U : U -> F(U)`
> biholomorphic, then shrink `B := B_c` inside `F(U)` (`F` is étale hence
> quasi-finite, so `F^{-1}(c)` is finite and one `B` serves all of it). Put
> `U' := (F|_U)^{-1}(B)`. Then `F : U' \ E -> B \ A_F` is a homeomorphism,
> i.e. a **section** of the covering `Y -> X` restricted over `B \ A_F`.
> The image of a section over a connected base is a connected component of
> the restricted covering. But the restriction of `Y -> X` over `B \ A_F`
> is classified by `rho` composed with the surjection
> `pi_1(B \ A_F) ->> pi_1(X)`, hence has the same orbits as `rho`, hence
> is connected of degree `N`. So `N = 1`. Contradiction. ∎

> **COROLLARY.** In case (A), `A_F = {x^p = y^q}` (Lin–Zaidenberg via
> MPRIME Prop. 7.1) is a cone: with the weighted `C^*`-action
> `lambda.(x,y) = (lambda^q x, lambda^p y)` both `C^2 \ A_F` and
> `B_eps \ A_F` deformation-retract onto the same weighted-sphere
> complement `S^3 \ T(p,q)`, compatibly with inclusion, so
> `pi_1(B_c \ A_F) -> pi_1(C^2 \ A_F)` is an **isomorphism**. Hence
> `F^{-1}(c) = empty`, `E` is a **smooth** affine curve (its only possible
> singularities were the analytic cusps over `c`), its `j` components are
> pairwise **disjoint**, and
> `F|_E : E -> A_F \ {c} = C^*` is étale.

The corresponding true statement about `a` is the one HT already has:
`a = #Fix(rho(m))` is the number of preimages of a **generic** point of
`A_F` (HT (3.1), HV §5, both confirmed). Nothing in HT, HV or SW is
retracted by this: none of CENTRAL-RANK, ORBIFOLD-CAGE, CUSP-PARITY,
CUSP-A-EMPTY uses a preimage of `c`. **Flagged, not claimed:** MPRIME
Prop. 6.1 is quoted by SW §7 as "unique unibranch cusp, `K_p = a-1`,
`a_p = 1`"; MPRIME is not charged to me and I cannot check whether its
`K_p` ledger is a statement about `E` (in which case the premise
`F^{-1}(c) != empty` there needs re-reading) or about the dicritical map
to `A_F` (in which case it is untouched). That is a cross-check request
for the coordinator, not a correction.

## 3. Chain I — the Euler gate closes case (A) at every degree

This is the charge's item (G-C), run to the end. Every number in it is
either pinned by the record or eliminated.

> **THEOREM CUSP-A-VOID.** There is no Keller map `F : C^2 -> C^2` of
> degree `N >= 2` whose non-properness set `A_F` is homeomorphic to `C`
> and singular. Equivalently: MPRIME case (A) is EMPTY at every degree.
>
> *Proof.* By Lin–Zaidenberg, `A_F ~ {x^p = y^q}` under `Aut(C^2)`, with
> `p, q >= 2` coprime; assume this normalisation.
>
> **(i) Euler.** `chi(A_F) = chi(C) = 1`, so `chi(X) = chi(C^2) - chi(A_F)
> = 1 - 1 = 0`. `Y -> X` is an `N`-fold covering, so `chi(Y) = N chi(X)
> = 0`. Additivity of `chi = chi_c` for complex algebraic varieties gives
> ```text
>     chi(E) = chi(C^2) - chi(Y) = 1 - 0 = 1 .
> ```
> **(ii) Structure of `E`.** By THEOREM NO-CUSP-PREIMAGE, `E` is smooth,
> so its `j` irreducible components `E_1,...,E_j` are pairwise disjoint
> and `chi(E) = sum_i chi(E_i)`. Each `E_i` is a smooth irreducible affine
> curve: `E_i = bar E_i \ S_i` with `bar E_i` smooth projective of genus
> `g_i` and `theta_i := |S_i| >= 1` places at infinity, so
> ```text
>     chi(E_i) = 2 - 2 g_i - theta_i  <=  1 ,
>     with equality iff  g_i = 0 and theta_i = 1, i.e. iff  E_i =~ A^1 .
> ```
> **(iii) The forced `A^1`.** The `chi(E_i)` are integers `<= 1` summing to
> `1`, so at least one of them equals `1`: some component is `=~ A^1`.
>
> **(iv) The contradiction.** `F` is étale, so `dF` is invertible and no
> component of `E` is contracted; hence `F|_{E_i} : E_i -> A_F` is
> non-constant. By NO-CUSP-PREIMAGE its image avoids `c`, and
> `A_F \ {c} =~ C^*` (the normalisation `t |-> (t^q, t^p)` is an
> isomorphism off the singular point). So `F|_{E_i}` is a non-constant
> morphism `A^1 -> C^*`, i.e. a non-constant unit of `C[t]`. There is
> none. ∎

**The same computation, in the form the charge asks for.** Writing
`nu := #F^{-1}(c)` (the number of cusps of `E`, `= 0` by §2) and
`Sigma^* := sum_i sum_{P in S_i^*} e_P >= 0`, where `S_i^*` is the set of
places of `E_i` at infinity lying over `C^* = A_F \ {c}` and `e_P` the
ramification index of `bar E_i -> P^1` there, Riemann–Hurwitz for
`bar E_i -> P^1` (unramified at every point of `E_i`, because `F` is a
local isomorphism and the normalisation of a `(p,q)` cusp maps
isomorphically to the normalisation of `A_F`) gives the **exact identity**

```text
   (G-C)      chi(E)  =  nu  -  Sigma^*        and     chi(E) = 1 .
```

So the charged identity is `nu = 1 + Sigma^* >= 1`: a Keller counterexample
in case (A) would need at least one cusp on `E`. §2 says `nu = 0`. That
is the mismatch, and a mismatch is a kill.

**What the record pins, and what it does not.** Pinned by the charged
record: `N`, `j = rank H^ab`, `a = #Fix(rho(m))`, `kappa`, `M`, `W = N-a`,
the dicritical partition `(s_l, mu_l)` of `W`, the meridian cycle type.
Derived here and *not* previously pinned: `chi(E) = 1`; `nu = 0`; `E`
smooth; components disjoint; `chi(E_i) = -sum_{S_i^*} e_P <= 0` for every
`i`. Still **not** pinned by anything (and not needed): the individual
`g_i`, `theta_i`, the component degrees `d_i` over `A_F`, the ramification
profile at infinity, and hence the link at infinity `K_infty` of `E` and
its `Delta_infty`. The Euler gate closes without any of them, which is
exactly why it beats (G-A) (§6).

**Scope.** Chain I uses only: `A_F` homeomorphic to `C` and singular; `F`
étale; `N >= 2`. It does **not** use `H2`, CUSP-KILL, 7.B, CUSP-PARITY,
ORBIFOLD-CAGE, CENTRAL-RANK, or any homology of the cover. It is not a
strengthening of the cage; it is a different argument. Under `H2`, case
(A) is exactly the branch it kills. Composed with the banked SMOOTH-KILL
**at SMOOTH-KILL's own typing** (not re-derived here, its hypotheses not
checked here) it would read: *the non-properness set of a noninvertible
Keller map is never homeomorphic to `C`* — recorded as a consequence,
not asserted.

## 4. Chain II — two new representation-level gates

Chain II is independent of Chain I: it never mentions `chi`, `nu`, or the
normalisation of `E`; it uses Lemma F1 and 3-manifold topology, and it is
decidable by a short permutation computation, which is what makes it
usable as an instrument at every `N`.

Throughout: `G = G_{p,q}`, `z = alpha^p` central, `rho : G -> S_N`
transitive, `H = rho^{-1}(Stab_1)`, `Y = C^2 \ E` with `pi_1(Y) = H` and
`H_1(Y) = Z^j` free on the meridians of the `j` components of `E`
(Lemma F1, HT §2.1, HV confirmed). `rho(z)` is central in a transitive
group, hence semiregular of order `kappa` with `M = N/kappa` orbits; those
orbits are blocks of imprimitivity, `rho(z)` acts simply transitively on
each, and the induced action on blocks factors through
`bar G := G/<z> = Z/p * Z/q`, with block stabiliser `Delta` of index `M`.
Write `bar m` for the induced permutation of `m = alpha^e beta^f`
(`eq + fp = 1`) on the `M` blocks.

`X = C^2 \ A_F` deformation-retracts onto the compact core
`M_0 := S^3 \ int nu(T(p,q))` (weighted cone retraction, §2), so the
covering `Y -> X` retracts onto the `N`-fold cover `Sigma_H -> M_0`:
**`Y` is homotopy equivalent to a compact orientable 3-manifold `Sigma_H`
whose boundary is `t` tori**, `t = #` orbits of the peripheral subgroup
`P = <m, lambda>`; and `lambda = z m^{-pq}`, so
`rho(P) = <rho(m), rho(z)>` and

```text
   t  =  # orbits of <rho(m), rho(z)> on N points  =  # cycles of bar m on M blocks .
```

`Sigma_H` is Seifert fibred over the degree-`M` orbifold cover
`O'` of `D^2(p,q)`, and `t` is the number of boundary circles of `O'`,
the `c` of the ORBIFOLD-CAGE derivation, so `2g + c = j` (HT §5.3) with
`g = genus(O')`.

### 4.1 THEOREM PERIPHERAL-RANK (the base orbifold has genus 0)

> **THEOREM.** `t = c = j`, equivalently `g = 0`.
>
> *Proof.* Each meridian of a component `E_i` is a lift of `m` at a sheet
> fixed by `rho(m)`, hence a loop in the preimage of the tube around
> `A_F`, hence freely homotopic into `partial Sigma_H`. By Lemma F1 those
> `j` meridians generate `H_1(Y) = H_1(Sigma_H)`. So
> `H_1(partial Sigma_H; Q) -> H_1(Sigma_H; Q)` is **onto**. Half-lives-
> half-dies for a compact orientable 3-manifold gives
> `rank(image) = (1/2) dim H_1(partial Sigma_H; Q) = t`. Hence
> `j = b_1(Sigma_H) = t`. With `2g + c = j` and `c = t = j`, `g = 0`. ∎

This is strictly stronger than ORBIFOLD-CAGE `(C-1)`, which pins only the
combination `2g + c = j`. As a gate it reads: **in the degree-`M` orbifold
cover, `bar m` must have exactly `j` cycles.** MEASURED: all 32 `N = 8`
records and the `N = 9` spot cell **pass** it (§5) — it is a real, cheap,
all-`N` gate, but it is not what kills the survivors.

### 4.2 THEOREM MERIDIAN-SPAN

> **LEMMA (block conjugacy).** `Fix(rho(m))` is a union of `n_0 := a/kappa`
> whole blocks, and for `i, i'` in the same block the meridian lifts
> `h_i := t_i m t_i^{-1}` and `h_{i'}` are **conjugate in `H`**; hence
> `[h_i] = [h_{i'}]` in `H^ab`.
>
> *Proof.* `rho(z)` commutes with `rho(m)`, so `Fix(rho(m))` is
> `rho(z)`-invariant, i.e. a union of blocks; on a block `B`, `rho(m)`
> commutes with the simply transitive `rho(z)|_B`, so `rho(m)|_B =
> rho(z)^{k_B}|_B`, and a single fixed point forces `k_B = 0`, i.e.
> `rho(m)|_B = id`. In particular `kappa | a` and `n_0 = a/kappa`. For
> `i' = rho(z)^r(i)` we have `t_{i'} = h t_i z^r` for some `h in H`, and
> `z` is central, so `h_{i'} = h (t_i m t_i^{-1}) h^{-1} = h h_i h^{-1}`. ∎

> **THEOREM MERIDIAN-SPAN.** `kappa * j <= a`.
>
> *Proof.* The meridians of the `j` components of `E` are exactly the
> classes `[h_i]`, `i in Fix(rho(m))` (a fixed sheet is a punctured
> transverse disc centred at a point of `E`; meridians at different points
> of the same irreducible component are conjugate, hence equal in `H_1`).
> By Lemma F1 they are `j` **distinct** basis elements of `H^ab = Z^j`. By
> the block-conjugacy lemma there are at most `n_0 = a/kappa` distinct
> classes. So `j <= a/kappa`. ∎

MEASURED, and this is the sharp check of the whole computation: the number
of distinct meridian classes returned by the Reidemeister–Schreier driver
equals `a/kappa` **exactly**, in 32/32 records (§9, control C4). The
predicted values are `1` for the trefoil cell (`a = 2`, `kappa = 2`) and
`2` for the family (`a = 4`, `kappa = 2`); the measured values are `1` and
`2`. Against `j = 2` and `j = 3`: **FAIL**, uniformly.

### 4.3 THEOREM CUSP-A-VOID-II

> **THEOREM.** In case (A) no admissible `rho` exists at any `N >= 2`.
>
> *Proof.* `#cyc(bar m) >= #Fix(bar m) >= n_0` (every block on which
> `rho(m)` is the identity is a fixed block). PERIPHERAL-RANK gives
> `#cyc(bar m) = j`, so `j >= n_0 = a/kappa`, i.e. `a <= kappa j`.
> MERIDIAN-SPAN gives `a >= kappa j`. Hence `a = kappa j` and the chain
> `j = #cyc(bar m) = #Fix(bar m) = n_0` is an equality throughout.
> `#cyc(bar m) = #Fix(bar m)` forces `bar m = id`, so `#Fix(bar m) = M`,
> so `n_0 = M`: every block has `rho(m)|_B = id`, i.e. `rho(m) = id` and
> `a = N`. But `W = N - a = sum_l s_l mu_l >= 2` (at least one dicritical,
> `mu_l >= 2` by THEOREM 7.B' under `H2`). Contradiction. ∎

Consumed here, at banked typing: Lemma F1 (HT, HV-confirmed);
`2 <= j <= a <= N-2` (CUSP-KILL + `[P3]` + 7.B'); ORBIFOLD-CAGE's
`2g + c = j`. Proved here: PERIPHERAL-RANK, the block-conjugacy lemma,
MERIDIAN-SPAN. Chain II therefore does need `H2` (through 7.B'), whereas
Chain I does not; that asymmetry is deliberate and is the reason both are
reported.

### 4.4 CUSP-A-KAPPA (charge item 2) — proved, by a stronger route

SW §8 conjectures that every `kappa = 1` cage cell dies at the meridian
cycle-type gate at every `N`. The conjecture is **true**, and PERIPHERAL-
RANK alone proves it without any search:

> **COROLLARY.** `kappa = 1` is impossible in case (A) at every `N >= 2`.
>
> *Proof.* `kappa = 1` iff `rho(z) = 1` (a central semiregular element with
> a fixed point is trivial), so blocks are points, `M = N`, `bar m =
> rho(m)`. PERIPHERAL-RANK: `j = #cyc(rho(m))`. CUSP-KILL: `j <= a =
> #Fix(rho(m))`. Always `#Fix <= #cyc`. So
> `j <= #Fix(rho(m)) <= #cyc(rho(m)) = j`: equality, hence every cycle of
> `rho(m)` is a fixed point, `rho(m) = 1`, `a = N`, `W = 0`, against
> `W >= 2`. ∎

Stronger than conjectured in two ways: the obstruction is named exactly
(the genus-0 identity, not the cycle type as such), and it is a proof
rather than an exhaustion, so it also covers cells whose `alpha`-type
splits into several conjugacy classes — the precise place where SW §8
records that its `N = 9` conjugacy reduction does not run.

### 4.5 Free by-products for the numerical cage

```text
(N1)  kappa | a                          (block-conjugacy lemma)
(N2)  a <= kappa * j                     (PERIPHERAL-RANK)
(N3)  # cycles of bar m on M blocks = j  (PERIPHERAL-RANK, sharp form)
```

These are cheap and independent of the kill; they are the residue worth
carrying to other profiles. On SW's `N = 8` cage they already bite at the
*numerical* level even though the surviving representations pass them: the
trefoil cell's listed meridians `a = 3` and `a = 5` and the family's
`a = 3` are removed by `(N1)` alone (`kappa = 2`).

## 5. Typed ledger of the survivors (charge item 3)

Normalisation: `alpha` fixed to a cycle-type representative, `beta` scanned
over all of `S_8`. Gates in order: relation `alpha^p = beta^q`;
transitivity; `2 <= a <= N-2`; `H^ab` torsion-free; `2 <= j <= a`;
non-regular (`|rho(G)| > N`, COR 7.2). This reproduces HT §5.5 / HV §6 /
SW §7 exactly.

```text
cell      alpha type  rel. beta  transitive  survivors   HT/SW expected
(2,3)       (4,4)        33          32          16          16
(3,2)       (6,2)        12          12           6           6
(3,4)       (6,2)        48          48           6           6
(4,3)       (8)          33          33           4           4
```

The charge's 26 = 16 (trefoil) + 6 + 4 (family). My 32 records are those
plus the 6 trefoil-cell records seen through the mirror normalisation
`(3,2)`; all 32 are decided below, so the 26 are covered with margin.

Per-record gate values (uniform inside each cell; the tally is over all
records of the cell):

```text
cell  n   j  a  kappa M  mer type      s  s'  c  t  ndist  n0=a/kappa  |rho(G)|
(2,3) 16  2  2    2   4  (3,3,1,1)     2  2   2  2    1        1          24
(3,2)  6  2  2    2   4  (3,3,1,1)     2  2   2  2    1        1          24
(3,4)  6  3  4    2   4  (4,1,1,1,1)   2  1   3  3    2        2         192
(4,3)  4  3  4    2   4  (4,1,1,1,1)   1  2   3  3    2        2         192

gate                            (2,3)  (3,2)  (3,4)  (4,3)
kappa | a                        pass   pass   pass   pass
PERIPHERAL-RANK  t = j           pass   pass   pass   pass
genus(O') = 0                    pass   pass   pass   pass
a <= kappa * j                   pass   pass   pass   pass
RS  vs  cover_h1  agreement      pass   pass   pass   pass
MERIDIAN-SPAN  kappa*j <= a      FAIL   FAIL   FAIL   FAIL
    (measured ndist = n_0 < j)    1<2    1<2    2<3    2<3
Chain I  CUSP-A-VOID             KILL   KILL   KILL   KILL
```

Family, MEASURED at `D = 1, 5, 7, 11, 13` (`q = 4D`, `alpha` of type
`(6,2)` fixed): 6 survivors at every `D`, with identical
`(kappa, j, a, t) = (2, 3, 4, 3)` and identical verdicts — SW's collapse
observation, re-measured, and the kill is `D`-independent by proof.

`N = 9` spot cell (SW §8, family F9.1, `p=2, q=3, M=3, kappa=3`): 6
survivors reproduced, `j = 2`, `a = 3`, meridian type `(6,1,1,1)`,
`t = c = 2 = j` (PERIPHERAL-RANK pass), `ndist = n_0 = 1 < j = 2`
(MERIDIAN-SPAN FAIL). The kill is not an `N = 8` accident.

**Verdict for every one of the 26 (32) survivors: KILLED, twice
independently.** No survivor is left; `OPEN[HOMCOVER-CUSP-A-N8]` closes
negative, and so does case (A) at every degree.

## 6. (G-A) Alexander / Libgober, honestly

Computed anyway, as charged, on the Reidemeister–Schreier presentation of
`H` (`N + 1 = 9` generators, `N = 8` relators, deficiency 1 — consistent
with `chi(Sigma_H) = 0`), by exact Fox calculus over
`Z[H^ab] = Z[t_1^{±1},...,t_j^{±1}]`, with `Delta_1 = gcd` of the `9`
maximal minors. MEASURED, up to units and up to the `GL_j(Z)` ambiguity of
the coordinates on `H^ab`:

```text
cell (2,3), 16 records :  Delta_1  =  Phi_3(u) = u^2 + u + 1
cell (3,2),  6 records :  Delta_1  =  Phi_3(u)
cell (3,4),  6 records :  Delta_1  =  (u - 1) * Phi_3(u)^2
cell (4,3),  4 records :  Delta_1  =  (u - 1) * Phi_3(u)^2
        in every case  u = t^v  for a single primitive  v in Z^j .
```

What this can and cannot do:

* The charged divisibility — `Delta` divides the product of the local
  Alexander polynomials at the singular points times `Delta_infty` — has
  an **empty local factor** here, because `E` is smooth (§2). So the
  charged form of (G-A) degenerates to `Delta_1 | Delta_infty`, and the
  record pins nothing about `K_infty` (§3). **(G-A) as charged is not
  decidable on the record.** It is not needed: Chains I and II both close
  without it.
* Worth recording, and *not* used as a kill: on the charge's own (now
  refuted) premise of `a` cusps of type `(p,q)`, the local factor would be
  `((t^{pq}-1)(t-1) / ((t^p-1)(t^q-1)))^a`, which for `(2,3)` is
  `Phi_6(t)^a = (t^2-t+1)^a`. The measured `Delta_1` is `Phi_3`, and no
  power of `Phi_6` is divisible by `Phi_3`. So the charged premise is
  internally inconsistent with the measured Alexander polynomial as well
  as with §2 — two independent symptoms of the same wrong datum. This is
  an observation about the premise, not a gate: with `Delta_infty`
  unpinned, divisibility cannot be tested either way.
* `OPEN[HOMCOVER-MODP-DIVISIBILITY]` (HT §2.3) is **not needed** and is
  left open; see §7.

## 7. (G-B) mod-`p` Betti jumps and characteristic varieties

MEASURED / immediate:

* `H^ab = Z^j` is torsion-free on every record (32/32, two independent
  implementations), so `dim_{F_p} H^1(H; F_p) = j` for **every** prime
  `p` — there is no mod-`p` jump at all, and HT's `t_p` (LEMMA MOD-P) is
  `0` for every `p`. The mod-`p` route is empty here; that is a fact about
  these covers, not a failure of the method.
* The first characteristic variety is `V_1 = V(E_1)`. MEASURED: `E_1` is
  **not** principal — it factors as `Delta_1 . C` with `C` the ideal of the
  nine cofactors, and `V(C) = {1}` (the trivial character) in every cell
  checked. Hence
  ```text
      V_1(H)  =  V(Delta_1)  u  {1}
              =  union of translated subtori  { t^v = zeta },  zeta^3 = 1,
                 together with  { t^v = 1 }  in the (3,4)/(4,3) cells.
  ```
  Every component is a **translated codimension-1 subtorus by a torsion
  character**, which is exactly the shape Arapura's structure theorem
  permits for a smooth quasi-projective `Y`, and exactly the shape a
  pencil `Y -> C^*` produces. **(G-B) is consistent; it does not kill.**
  Reported as a negative result: it is why the charge's first two levers
  were not the ones that closed the lane.

## 8. (G-D) the small case, by hand

`|rho(G)| = 24`, centre of order `2`, element orders
`{1:1, 2:1, 3:8, 4:6, 6:8}` (MEASURED) — that is the binary tetrahedral
group `SL(2,3)`, and the map is the classical
`B_3 = G_{2,3} ->> SL(2,Z) ->> SL(2,3)` with `z = alpha^2 |-> -I`
(`kappa = 2`). The 8 points are the nonzero vectors of `F_3^2`; the point
stabiliser is the order-3 unipotent subgroup, which is the charge's
"point stabiliser of order 3".

`Y` explicitly: the block quotient is `SL(2,3)/{±I} = A_4` on the `M = 4`
blocks (the four lines of `F_3^2`), `Delta` of index 4 in
`Z/2 * Z/3 = PSL(2,Z)`. MEASURED orbifold data: `p`-side local degrees
`(2,2)` (cone orders `1,1`), `q`-side local degrees `(3,1)` (cone orders
`1, 3`), `c = #cyc(bar m) = 2`, hence

```text
   O'  =  ANNULUS with one cone point of order 3 ,  genus 0 ,
   Delta = pi_1^{orb}(O') = Z * Z/3 ,   r = 1 = j - 1  (CENTRAL-RANK, checks) ,
   Sigma_H = Seifert fibration over O' with 2 boundary tori .
```

(For the family cell: `O'` = 3-holed sphere with one cone point of order
`3`, `Delta = F_2 * Z/3`, `r = 2 = j-1`, `c = 3`.)

Now decide directly, as the charge asks. The charge's question is "can
`Y` be a plane-curve complement with two `(2,3)`-cusps and two
components?" Both halves of the premise fail and the answer is no:

1. **The cusps are not there.** `F^{-1}(c) = empty` (§2): `E` is smooth.
2. **Two components are impossible.** `chi(E) = 1` and `E` smooth with
   `j = 2` disjoint components forces `{chi(E_1), chi(E_2)} = {1, 0}`
   (each `<= 1`, integers, sum `1`), so `E_1 =~ A^1` and `E_2` is a smooth
   affine curve with `2g+theta = 2`, i.e. `theta = 2, g = 0`. The `A^1`
   component must map non-constantly to `A_F \ {c} =~ C^*`: impossible.
3. **Independently, at the group level.** `a = 2` and `kappa = 2` put both
   `rho(m)`-fixed sheets in one `<rho(z)>`-block, so the two meridian
   lifts are conjugate in `H` and carry the *same* class in
   `H^ab = Z^2`. A two-component plane curve complement has two
   *independent* meridians (Lemma F1). MEASURED: `ndist = 1`. Kill.

The second rank-1 direction in `H^ab` is therefore *not* a second component
of `E`: it is the annulus / Seifert-fibre direction of `O'`, i.e. the image
of the centre `Z_H` that CENTRAL-RANK injects. Naming it answers the
charge's second option — why the survivors pass every homological gate:
**rank in `H^ab` equals component count only if the rank is carried by
meridians, and HOM-COVER only ever tested the rank.** MERIDIAN-SPAN is
that missing test.

## 9. Controls

**C1 — instrument.** `python3 box/cover_h1.py`: 4/4 built-in controls
PASS, including `Z (+) Z/3` and the fail-closed convention refusal. The
`/tmp/cuspa` copy is byte-identical (hash in §0).

**C2 — replication of the charged census.** HT §5.5 / SW §7 counts
`16 / 6 / 6 / 4` at the four base cells and the relation/transitive
intermediate counts `33/32`, `12/12`, `48/48`, `33/33` are reproduced here
from an independently written enumerator (§5). SW's family collapse is
reproduced at `D = 1, 5, 7, 11, 13`; SW's `N = 9` F9.1 count of 6 is
reproduced.

**C3 — cross-implementation homology.** `H^ab` computed twice, by
`box/cover_h1.py` (Fox matrix + own SNF over the sheets) and by an
independent Reidemeister–Schreier presentation + a second SNF: rank and
torsion agree in 32/32 records. This is what licenses reading the RS
generators as a presentation of the same `H`.

**C4 — the sharp prediction.** The block-conjugacy lemma predicts
`#distinct meridian classes = n_0 = a/kappa`, a nontrivial integer
computed by a completely different route (conjugacy in `H`) from the one
that measures it (Fox/SNF images in `H^ab`). MEASURED: equality in 32/32
records, 0 mismatches.

**C5 — the meridian classes are meridians.** The composite
`H ->> H^ab -> G^ab = Z<m>` is computed independently from the Schreier
transversal (`alpha |-> q`, `beta |-> p`). Every measured meridian class
evaluates to exactly `1` under it, in every cell (MEASURED: the value set
is `{1}`). A misidentified class would generically not.

**C6 — positive control, the gate can pass.** `N = 1` (trivial `rho`,
`H = G`, `E = A_F`): `j = 1`, `a = 1`, `ndist = 1 = j`, basis determinant
`-1`. MERIDIAN-BASIS **passes**. So the gate is not vacuously false. It
also returns `ndist = 2` on the family cells, so it is not pinned to `1`.

**C7 — the two gates are not the same gate.** At `N = 8`, over all
coprime `(p, q) <= 7` with `alpha` normalised to a cycle-type
representative: 32 candidates survive the banked filters; **32/32 pass
PERIPHERAL-RANK, 0/32 pass MERIDIAN-SPAN, 0/32 pass both** — the
distribution a genuinely independent pair of gates should have, and the
`0` in the last column is THEOREM CUSP-A-VOID-II's prediction.

**C8 — negative control on Chain I (it does not prove too much).** The
argument's use of `chi(C^2) = 1` is load-bearing, and the same bookkeeping
is *satisfiable* when the source has `chi <= 0`. Witness: `V = C^* x C`,
`F(u,v) = (u^2, v)`, étale of degree 2, non-proper exactly over
`A_F = {x = 0}` (contractible), `E = F^{-1}(A_F) = empty`. The identity
`chi(E) = chi(V) - N chi(X)` reads `0 = 0 - 2*0`: **consistent**, no
contradiction, and indeed the map exists. Replacing `V` by `C^2` turns the
identity into `chi(E) = 1`, which §3 shows is unattainable. The obstruction
is exactly `chi(C^2) = 1 > 0`.

**C9 — negative control on the surjectivity hypothesis.** THEOREM
NO-CUSP-PREIMAGE needs *both* étaleness and the local-to-global
surjection. `F(u,v) = (u^2, v) : C^2 -> C^2` with `A = {x = 0}` has
`F^{-1}(0,0) != empty` — and `F` is not étale there. `{xy = 0}` is a cone
with `pi_1(B \ A) -> pi_1(C^2 \ A)` an isomorphism, yet nothing is
concluded about maps that ramify over it. Both hypotheses are used.

**C10 — the cage sweep at `N <= 7`.** The full candidate filter at
`N <= 7` over all coprime `(p,q) <= 7` returns **0 candidates**, matching
CUSP-A-EMPTY. The new gates do the `N >= 8` work, not `N <= 7` again.

## 10. Scope, non-claims, successors

**In scope and closed.** MPRIME case (A), every degree `N >= 2`, EMPTY,
by two independent proofs. `OPEN[HOMCOVER-CUSP-A-N8]` closes negative.
SW's CUSP-A-KAPPA conjecture is proved. The `8 <= N <= 16` census of SW §4
and the appendix families are all case-(A) cells and are all killed by the
same two theorems; no enumeration of them is needed and none is asserted.

**Explicitly not claimed.** Nothing about case (B3): the arguments use
`A_F` homeomorphic to `C` at three separate places (`chi(A_F) = 1`; the
cone structure giving the local-to-global surjection; `A_F \ {c} =~ C^*`),
and a multibranch point breaks all three. Nothing about `(9,6,2)`,
`(9,6,4)`, `Z(G)`, or any transfer. No claim that a Keller counterexample
does or does not exist. No realisation claim of any kind: the survivors
were `REPRESENTATIVE` and are now refuted, which is a statement about the
representation data, not about a curve.

**Named successors, typed, not run here.**

```text
SUCC-1  NO-CUSP-PREIMAGE at other profiles.  It needs only that SOME singular
        point c of A_F has  pi_1(B_c \ A_F) ->> pi_1(C^2 \ A_F).  Which points
        those are is not automatic off a cone; each one is missed by F and
        removes a term from  chi(E) = nu - Sigma^*.  Stated with no (B3) input.
SUCC-2  The Euler identity at a general profile:  chi(E) = 1 - N(1 - chi(A_F)),
        with  chi(E) = nu - Sigma^*  when every component of E is unibranch.
        A profile with A_F contractible is dead on arrival; chi(A_F)=0 is void.
SUCC-3  MERIDIAN-SPAN as a standing instrument.  Wherever the covering datum has
        a central (or block-forming) element, meridian lifts over one block
        collapse in H^ab and rank(H^ab) over-counts components.  HOM-COVER should
        report the meridian-class count, not just the rank.  Already coded.
```

## 11. FALLACY-v2 audit

* **Flag/place/series.** The germ `pi_1(B_c \ A_F)`, the link at infinity,
  `G = pi_1(C^2\A_F)` and `G_{p,q}` are kept apart. The one identification
  made — `pi_1(B_c\A_F) = pi_1(C^2\A_F) = G_{p,q}` in case (A) — is
  **proved** from the weighted cone structure, is the same one HT proves
  and HV confirms, is used at exactly one place (§2), and its necessity is
  controlled (C9). `A_F \ {c}` is never identified with `A_F`.
* **Carrier/attainment.** The survivors were `REPRESENTATIVE` group data,
  and a refutation of representative data refutes any carrier over it. No
  `FULL_ACTUAL_EXIT` is asserted or needed; nothing claims a curve exists.
* **Floor/attainment.** `chi(E_i) <= 1` is a bound; the kill uses the
  attained case `chi(E_i) = 1`, which is forced by an integer sum, not
  assumed. `#distinct meridian classes <= n_0` is a bound; the measurement
  attains it (C4) but the theorem only uses the bound.
* **Per-ray / exit-set.** No exit price asserted; no `charge_basis` line.
* **Pole/interior.** No pole identities in play.
* **Variable/ring map.** Two conventions are load-bearing and both are
  declared: `cover_h1`'s transport convention (every call goes through
  `to_transport_convention`), and the right coset action
  `i . x = rho(x)^{-1}(i)` used by the Reidemeister–Schreier driver. They
  are the same convention, and C3 is the check that they are.
* **Raw remainder / `sat()`.** Not in play; no Groebner computation.
* **Prime label/derivative.** `s'` is the `q`-side cone-preimage count,
  never a derivative; the dicritical `s_l` is a different symbol and
  appears only in `W = sum_l s_l mu_l`; `n_0` (blocks with `rho(m)|_B=id`)
  is kept distinct from `s`, `s'`, `t`, `c`.
* **Target/arrival index.** `a` is used only as `#Fix(rho(m))` at a
  *generic* point of `A_F`; the *cusp* count is written `nu` and is a
  different number (`0`). Conflating them is exactly the charge's error
  and the report keeps two symbols for it.
* **No gap filled by cap or analogy.** Where the charged levers do not
  decide — (G-A) without `Delta_infty`, (G-B) at all — the report says so
  and does not substitute. Where a banked report may be affected
  (MPRIME Prop. 6.1) the item is FLAGGED for cross-check, not asserted.

## 12. Typed verdict block

```text
LANE              CUSP-A-N8-GATE
CHARGE            find and apply a NEW gate deciding the N=8 case-(A) survivors.

VERDICT           TWO new gates found; each kills all 26 survivors and closes
                  case (A) at EVERY degree N >= 2.  OPEN[HOMCOVER-CUSP-A-N8]
                  CLOSED NEGATIVE.

PROVED HERE       NO-CUSP-PREIMAGE   F^{-1}(cusp) = empty ; E is SMOOTH.
                  CUSP-A-VOID        (Chain I, Euler)  case (A) empty, all N,
                                     H2-FREE; uses only Lin-Zaidenberg + etale.
                  PERIPHERAL-RANK    t = c = j ; base orbifold has genus 0.
                                     Sharpens ORBIFOLD-CAGE (which pins 2g+c=j).
                  MERIDIAN-SPAN      kappa * j <= a.
                  CUSP-A-VOID-II     (Chain II)  the two force rho(m)=1, against
                                     W >= 2.  Case (A) empty, all N.
                  CUSP-A-KAPPA       SW's conjecture PROVED (from PERIPHERAL-RANK
                                     alone), stronger than conjectured.
                  kappa | a          free cage by-product.
                  chi(E) = nu - Sigma^*   the exact (G-C) identity.

CORRECTS          The charge's premise "E has exactly a singular points, each a
                  (p,q) cusp".  E has NONE.  a is the generic-fibre count, not
                  the cusp-fibre count.  Independently symptomatic in (G-A):
                  measured Delta_1 = Phi_3, incompatible with any power of the
                  (2,3)-cusp local factor Phi_6.

FLAGGED           MPRIME Prop. 6.1 as quoted by SW section 7 ("unique unibranch
                  cusp, K_p = a-1") -- if its ledger is about E, its premise
                  needs re-reading.  MPRIME not charged here; NOT claimed.

MEASURED          census replication 16/6/6/4 with intermediate counts 33/32,
                  12/12, 48/48, 33/33 -- matches HT/HV/SW.
                  32/32 records: kappa|a pass, PERIPHERAL-RANK pass, a<=kappa*j
                  pass, MERIDIAN-SPAN FAIL.
                  32/32: ndist = a/kappa exactly (0 mismatches) -- sharp check.
                  32/32: RS presentation vs cover_h1 agree on rank and torsion.
                  32/32: psi(meridian class) = 1 under H^ab -> G^ab.
                  family q=4D at D=1,5,7,11,13: 6 survivors each, same verdict.
                  N=9 F9.1: 6 survivors, PERIPHERAL pass, MERIDIAN-SPAN FAIL.
                  N<=7 sweep, all coprime (p,q)<=7: 0 candidates (CUSP-A-EMPTY).
                  N=8 sweep, all coprime (p,q)<=7: 32 candidates, 0 pass both.
                  Alexander:  Phi_3(t^v)  and  (t^v-1) Phi_3(t^v)^2 .
                  dim H^1(H;F_p) = j for every p (no mod-p jump anywhere).
                  |rho(G)| = 24 = SL(2,3) with O' = annulus + one order-3 cone
                  point;  |rho(G)| = 192 with O' = 3-holed sphere + order-3 cone.

CONSUMED          MPRIME Prop 7.1 (Lin-Zaidenberg), CUSP-KILL (j>=2, j<=a, M>=2),
                  [P3] + 7.B' (meridian cycle type, mu_l >= 2, hence W >= 2),
                  COR 7.2 (nonregular), SMOOTH-KILL -- at banked typing.
                  HT Lemma F1, CENTRAL-RANK, ORBIFOLD-CAGE, CUSP-PARITY,
                  CUSP-A-EMPTY -- at HV's confirmed typing.
                  SW's N=8 counts and N=9 spot data -- MEASURED, replicated.
                  Classical: half-lives-half-dies; Seifert fibration of a torus
                  knot complement; additivity of chi_c for complex varieties.

NOT CONSUMED      any (B3) transfer; Z(G) = 1; OPEN[HOMCOVER-LINK-INFTY-SURJ];
                  OPEN[HOMCOVER-MODP-DIVISIBILITY] (not needed, left open);
                  OPEN[CABLE-UNIVERSALITY].

NOT CLAIMED       anything about case (B3), (9,6,2), (9,6,4), JC2 at any degree,
                  existence of F, or realisation of any curve.

OPENS RAISED      SUCC-1  which singular points of A_F have surjective local
                          pi_1 at a general profile (each is missed by F).
                  SUCC-2  the Euler identity at a general profile.
                  SUCC-3  MERIDIAN-SPAN as a standing HOM-COVER instrument.

DEVIATIONS        (1) The charge's four levers were run; (G-A) and (G-B) are
                      reported as NOT decisive on the record and the lane was
                      closed by (G-C) plus a new gate the charge did not name.
                  (2) The result is stated at every N, not only N=8, because
                      neither proof is degree-sensitive.  This exceeds the
                      charge and is flagged as such rather than trimmed.
                  (3) Drivers left in /tmp/cuspa, not installed in box/,
                      following HT and SW.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `39583`.
- Body SHA-256:
  `36629822a85006b5d05b7002ec86880b6ec3edfa99250f8210ee71871bb18ab5`.
- Frozen basis: `fb747b0bc358955548f59b112c89e9fa703d2249`.
