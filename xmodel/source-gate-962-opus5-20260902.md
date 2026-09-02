# SOURCE-GATE-962 — the retyped source question, three stacked razors, Mode 1 on `(9,6,2)`

Lane: `source-gate-962-opus5-20260902`. Basis `f35adc89`. Hostile standard.
Nothing here is promoted, no row is closed, no exit price is asserted, and no
`charge_basis` line is required or given (§12).

## 0. Custody, scope, method

All five charged inputs verified byte-exact against the frozen read-only copies
before any other read:

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  ideation-20260902T0022Z-opus5.md
83319c5e0ddbdb2bfa43b983aae28c57474703205e244cda6e1460942e5809b9  ideation-20260902T0022Z-grok46.md
4b0e4dde91a8bbe06dfde68e0c8c4559d92bcb8355a0b57acf32ba8b36a7d3b4  ideation-20260902T0022Z-sol56.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  round1033-sheet-gate-opus5-20260831.md
```

Short names: `[G]` grok46, `[S]` sol56, `[O]` opus5 (the three ideation
submissions), `[R96]` REP-96-INNER, `[SG]` SHEET-GATE. Also read on disk and
cited by line: `domrina-gap-repair-opus5-20260901.md:141-176` (Lemma DET-LINF),
`tb-g2-finish-opus5-20260901.md:418-480`, `notes.md:17290-17310` (footguns
#10/#11, SIROCCO census receipt), `box/bmfact_962.sage`, `box/cover_h1.py`.

Ran in-lane, no CAS, no AWS, no network: `box/cover_h1.py` (audited §3, two
defects found, repaired, fifth control added); `box/covergeo.py` (written this
lane, §7); four throwaway audit scripts (SNF cross-check, `d_1∘d_2` validity,
convention-witness search, `B_3` torsion census) whose conclusions are
reproduced below. Numbers labelled MEASURED came from those runs; everything
else is desk derivation and marked so. No sibling `20260902T0022Z` report was
opened beyond the three charged submissions.

---

## 1. Task (1) — the retype, as ONE typed object

### 1.1 The three statements, as written

* `[G] §3`: SHEET-GATE `Y = Spec B` "is never `C^2` (Lemma 2.2: `B_Y`
  nonempty)"; the right question is whether the Riemann-existence cover admits a
  Zariski-open `U ≅ A^2` whose complement is a curve mapping onto `D`, with
  four-box numbers matching SHEET-GATE.
* `[S] §1/§4`: the label "`Y` is `C2`" is unsafe; construct `q : Y → A^2` from a
  full monodromy survivor and **seek the divisor `B_Y` for which `U = Y − B_Y`
  is the Keller source** — "do not test whether the whole `Y` is `A2`". Safe
  replacement token `OPEN[REP-96-A2-OPEN-IMMERSION-BOUNDARY]`.
* `[O] §3.1`: `F` is étale everywhere, so nothing is branched; by ZMT the
  normalisation `Ȳ` contains the source as an *open* subset with `Ȳ ∖ C^2` a
  curve, and `Ȳ` is normal and typically singular, so `Ȳ ≅ C^2` is **not
  necessary**. The necessary finite condition is `(SRC)`: the `N`-sheeted
  covering space of `C^2 ∖ A` determined by `rho` is the complement of a plane
  curve in `C^2`.

### 1.2 Lemma SRC-0 — the three `Y`s are one scheme

The three submissions each name a surface; none proves the surfaces agree. They
do, and that is what makes a single typed object possible.

> **Lemma SRC-0.** Let `F : A^2 → A^2` be Keller with non-properness set
> `A = A_F`, `td = N`, and let `rho : pi_1(A^2 ∖ A) → S_N` be the monodromy of
> the covering `F : A^2 ∖ F^{-1}(A) → A^2 ∖ A` (`[O] §3.1`, `ACS-1`). Then
> `Spec B` of `[SG] §2.1` (`B` = integral closure of `C[F_1,F_2]` in `C(x,y)`),
> `Ȳ` of `[O] §3.1`, and the Riemann-existence surface `Y_rho` of `[G] §3` /
> `[R96] §7 R2` are **the same scheme**.
>
> *Proof.* `Spec B = Ȳ` is the definition. For `Y_rho`: `q : Spec B → A^2` is
> finite, `Spec B` is normal, and over `V := A^2 ∖ A` the fibres of `q` lie in
> `U = j(A^2)` (`[SG]` Lemma 2.3), where `q|_U = F` is étale; so
> `q^{-1}(V) = F^{-1}(V)` is exactly the covering space determined by `rho`.
> A normal scheme, finite over `A^2`, restricting to a given connected étale
> cover over `V`, is the normalisation of `A^2` in that cover's function field,
> which is `Y_rho` (Grauert–Remmert / GAGA supply its algebraicity). ∎

So `[G]`'s "SHEET-GATE `Y` is the correct `Y`" and `[O]`'s "the branched cover
is the wrong object" are **not in conflict**: same surface, different property
asserted. `[G]`/`[S]` are right that it is never `A^2`; `[O]` is right that
`Ȳ ≅ C^2` is not necessary. Both follow from `[SG]` Lemma 2.2 alone.

### 1.3 The typed object

> **`(SRC-OPEN)`.** Let `D ⊂ A^2` be a curve and `rho : pi_1(A^2 ∖ D) → S_N`
> transitive, with `Y_rho` its Riemann-existence surface and `q : Y_rho → A^2`
> the finite degree-`N` map. `rho` arises from a Keller counterexample `F` with
> `A_F = D` **only if** there is a Zariski-open `U ⊆ Y_rho` with
>
> 1. `U ≅ A^2`;
> 2. `B_Y := Y_rho ∖ U` nonempty and pure of codimension one;
> 3. `q|_U` étale;
> 4. `q(B_Y) = D`;
> 5. the `[SG] §2.2` four-box numbers hold on every component `D_i`: with
>    `g_i = rho(meridian_i)`, `sigma_i = #Fix(g_i) = a^{(i)} + b^{(i)}`,
>    `N = a^{(i)} + sum_j delta_j e_j`, `1 <= a^{(i)} <= N − 2`, some `e_j >= 2`.
>
> `[O]`'s `(SRC)` is the restriction of `(SRC-OPEN)` to `q^{-1}(A^2 ∖ D)`:
> `V_rho ≅ A^2 ∖ E` with `E = F^{-1}(D)` a plane curve. It is implied by
> `(SRC-OPEN)`, hence a legitimate (strictly weaker) razor.

Every clause is *necessary*, none is claimed sufficient. Clause 1 is not
"`Y ≅ A^2`"; clauses 2–4 are `[SG]` Lemmas 2.2/2.3 turned into demands on a
hypothetical `rho`; clause 5 is `[G]`'s four-box match; `[S]`'s
`SOURCE-OPEN-BOUNDARY-LATTICE` is clause 1 plus a completion of the declared `U`.

### 1.4 Token discipline

`OPEN[REP-96-SOURCE-IS-C2]` (`[R96]:652`) is **retired as mis-typed**: it asks
for `Y ≅ C^2`, which `[SG]` Lemma 2.2 refutes for every Keller `F`, so the token
is unsatisfiable and its "openness" was an artifact. Successor
**`OPEN[SOURCE-OPEN-U]`** = does a `U` satisfying `(SRC-OPEN)` exist for a given
`rho`; `[S]`'s `OPEN[REP-96-A2-OPEN-IMMERSION-BOUNDARY]` is an alias. This is a
*typing* correction, not a closure: the geometric gap `[R96] §7 R2` names is
undiminished and now lives in the successor token.

---

## 2. The three razors, stacked on one input

**Input type `INPUT-rho-D`** (everything conjugacy-invariant, nothing labelled):

```text
   N ;  components D_i with chi_c(D_i-normalisation) ;
   generic cycle type of rho(meridian_i)  (a partition of N) ;
   Sing D : for each p, the branch number r_p and the H_p-orbit multiset ;
   [ optional, must be cited ] the four-box split b^{(i)} ; a_p .
```

The three razors as necessary conditions on `INPUT-rho-D`:

| razor | source | necessary condition | needs beyond `INPUT-rho-D` |
|---|---|---|---|
| (a) HOM-COVER | `[O] §3` | `torsion(H_1(V_rho)) = 0` and `rank = r(E)` | a **presentation** of `pi_1(A^2∖D)` and the labelled `rho` |
| (b) FOUR-BOX EULER | `[G] §3` | `chi_c(Y)_RH = 1 + chi_c(B_Y)` | nothing |
| (c) BOUNDARY LATTICE | `[S] §4` | `det L̃_infty <= 0` on a declared `U`-completion | a resolved completion and its dicritical/non-dicritical split |

Only razor (b) runs on `INPUT-rho-D` alone — hence the Mode-1 verdict is razor
(b)'s, and razors (a) and (c) return typed status rather than numbers. The stack
is a chain, not three independent tests: §3.8 shows razor (a)'s *rank* output
decides razor (b)'s free parameter (the sheet-location bit `b`).

---

## 3. Task 2(a) — HOM-COVER: instrument audit first, then status

### 3.1 The mathematics is correct

`[O] §3.2`'s razor rests on `H_1(C^2 ∖ E) = Z^{r(E)}`, free of rank the
component count; re-derived independently from
`H_2(C^2)=0 → H_0(E) → H_1(C^2∖E) → H_1(C^2)=0`. `H_1` of a covering space is
the abelianisation of the corresponding subgroup. Both steps stand, and `[O]`'s
floor/attainment discipline is kept: passing HOM-COVER is not existence.

The free-rank formula is the one line a reviewer would wave through, so:
`im(d_1) ⊆ Z[S]` is the augmentation submodule, free of rank `k−1` for a
connected cover, so `0 → H_1 → coker(d_2) → im(d_1) → 0` **splits**,
`coker(d_2) = H_1 ⊕ Z^{k-1}`, and one Smith normal form returns torsion and rank
together as `free_rank = n·k − rank(d_2) − (k−1)`. Verified.

### 3.2 The four controls, independently re-derived

Re-derived by hand, not merely re-run (all four MEASURED values reproduce):

| control | expected, independent derivation | code |
|---|---|---|
| two transverse lines, `k=2` | complement `(C*)^2`, `H = ⟨x^2,y⟩ ≅ Z^2` | `Z^2` ✓ |
| trivial `rho`, `k=1` | `H_1((C*)^2) = Z^2` | `Z^2` ✓ |
| cuspidal cubic base | `B_3^{ab} = Z` (braid relation identifies `x,y`) | `Z` ✓ |
| trefoil cyclic 2-fold | `Z ⊕ Z/|Δ_tref(−1)| = Z ⊕ Z/3` | `Z ⊕ Z/3` ✓ |

The Smith routine was separately checked against a textbook matrix
(`[[2,4,4],[-6,6,12],[10,4,16]]` → `2,2,156`) — MEASURED, correct. The irregular
3-fold value `Z^2` is correct too (the trefoil's 3-fold irregular branched cover
is `S^3`, with 2 branch components upstairs).

**The four controls are sound and the sharp one is genuinely sharp.** The two
defects below are not in the controls' answers but in what they fail to test.

### 3.3 DEFECT 1 — the instrument is FAIL-OPEN on convention

`d2_matrix` walks a relator left-to-right applying `rho[g]` **on the left**, so
the transport of `w = g_1 … g_m` is `rho(g_m) ∘ … ∘ rho(g_1)` — the right-action
/ monodromy convention, i.e. `rho` used as an *anti*-homomorphism. A caller
holding an ordinary left-action homomorphism `L` is passing the wrong datum, the
relator lifts **do not close**, `d_2` is not a boundary map, and the Smith normal
form is meaningless. The code never checked. MEASURED witness, found by search
this lane:

```text
   G = < x, y |  x y x y^-1 x^-1 y^-2 >          k = 5
   rho(x) = (0,2,1,4,3) ,  rho(y) = (3,0,1,2,4)
   left-action rho(w)      = identity      <- rho IS a homomorphism: valid input
   cover_h1 internal lift  = (2,0,3,4,1)   <- does not close
   d_1 o d_2 == 0 ?        False           <- not a chain complex
   cover_h1 RETURNED       Z^1             <- no exception, no warning
```

This is not academic here. The ZvK presentation of `pi_1(A^2 ∖ D)` for
`(9,6,2)` consists of **conjugation relators** `xi_a = w xi_b w^{-1}`
(`[R96] §7 R1`) — exactly the shape that distinguishes the two conventions.
Feeding SIROCCO/ZvK output to the unrepaired instrument would have produced a
meaningless number, and a *torsion-free* number is the "survives" verdict: the
failure mode points toward false survival, not false kill.

### 3.4 DEFECT 2 — the control suite cannot see DEFECT 1

Both relators used by the four controls are invariant under letter-reversal (the
commutator, and the braid relation `xyx = yxy`), and in the trefoil controls
`rho(x), rho(y)` are involutions, for which the conventions coincide outright.
The delivered suite is therefore **convention-blind by construction** — it would
pass identically with the transport walk reversed. A control suite that cannot
fail on the instrument's live failure mode does not calibrate it.

### 3.5 Repair delivered

`box/cover_h1.py` patched additively: the convention is stated in the docstring
with the witness; `lift_closes(...)` is an explicit `d_1 ∘ d_2 = 0` test;
`cover_h1` **raises** unless every relator lifts closed, naming
`to_transport_convention(rho)` (the left-action → transport converter) when the
elementwise inverse does close; and **CONTROL 4** adds the convention
discrimination the old suite lacked.

MEASURED after repair — CONTROLS 1–3 are byte-identical to §3.2, so the repair
is non-breaking, and the new one fires:

```text
== CONTROL 4  convention discrimination (the four controls above are reversal-symmetric and cannot see it)
   left-action input REFUSED         PASS
   after to_transport_convention: H_1 = Z^1  PASS
```

The two conventions do **not** merely differ by a relabelling: `rho` and
`g ↦ rho(g)^{-1}` correspond to subgroups related by a free-group automorphism
that need not descend to `G`, so when both happen to be admissible they can give
different `H^ab`. Declaring the convention is mandatory, not cosmetic.

### 3.6 The kill-power census reproduces

Independently recomputed this lane (MEASURED), with `lift_closes` enforced:

```text
   B_3 -> S_3 :  8 transitive reps,  2 with torsion (25%)   Z^2 x6 ,  Z + Z/2 + Z/2 x2
   B_3 -> S_4 : 54 transitive reps, 30 with torsion (56%)   Z^2 x24 , Z + Z/2 x24 , Z + Z/3 x6
```

`[O] §7`'s figures are confirmed exactly: the razor has real kill power on data
of this shape, and every torsion-free survivor has `rank ∈ {1,2}` — which §3.8
shows is exactly the binding window.

### 3.7 Status at `(9,6,2)`: PENDING-INPUT, not OPEN-for-lack-of-theory

Running HOM-COVER needs a presentation of `pi_1(A^2 ∖ D)`: the eight tangency
transports and the node-fibre word. Those are the content of
`OPEN[REP-96-BM-FACTORISATION]`. The SIROCCO run banked the nine *braids*
(`notes.md:17305-17310`, CENSUS-OK, exponent ledger 16), but no braid words or
transports are on disk here, and Sage 10.9 returned the 4-tuple with **no base
point** — `OPEN[BMFACT-BASEPOINT]`, which infects every labelled transport.

> **Razor (a) at `(9,6,2)`: NOT RUN — PENDING-INPUT.** Typed
> `OPEN[REP-96-BM-FACTORISATION]` + `OPEN[BMFACT-BASEPOINT]`. The instrument is
> now verified and fail-closed, so the razor is *armed*: a one-second
> computation the moment SAGE-NATIVE emits a surviving labelled tuple. It must
> not be run on a reconstructed presentation; that would fill a gap by analogy.

### 3.8 What razor (a) *does* give without transports — and the coupling to (b)

Two facts follow from `INPUT-rho-D` alone, and they are why the razors chain.

> **Lemma HC-1.** In Mode 1, `r(E) <= a`, where `E = F^{-1}(D)`.
> *Proof.* `E = V(h∘F)` is a hypersurface, so it has no isolated points and
> every component meets `F^{-1}(D_0)`. By `[SG]` Lemma 3.3, `F^{-1}(D_0) → D_0`
> is a covering of degree `a`, so it has at most `a` components. ∎

> **Corollary HC-2 (the coupling).** Under `(SRC)`, `rank H_1(V_rho) = r(E) <= a
> <= sigma`. Hence at `(9,6,2)` in Mode 1 (`sigma = 2`): `rank >= 3` is an
> outright kill, and `rank = 2` **forces `a = 2`, hence `b = 0`** — i.e. razor
> (a)'s rank output decides `OPEN[SHEET-LOCATION]` (`[SG] §9.1`) at this
> profile, which is razor (b)'s only free parameter.

A genuine new link between `[O]`'s mechanism and `[SG]`'s open bit, supplied by
the same Smith normal form at no extra cost. It does not fire today: the
presentation is missing.

---

## 4. Task 2(b) — FOUR-BOX EULER, Mode 1 on `(9,6,2)`: RUN

Mode 1 = irreducible `A_F`, i.e. `A_F = D_1` is the whole non-properness set.

### 4.1 The conjugacy-invariant input, itemised

| datum | value | source |
|---|---|---|
| `N` | 4 | residual profile, `[R96] §7 R3` |
| `D` irreducible, rational, one place at infinity | `chi_c(D̃) = 1` | `[R96] §1`; this is `[SG]`'s `(H3)` (`[SG]:23`) |
| affine singularities | 4 ordinary nodes, `r_p = 2`, `nu = 4` | `[R96] §1`, exact: `delta_aff = 4` exhausted |
| generic meridian `g` | a transposition, cycle type `(2,1,1)` | `[R96] §5` — every surviving `(9,6,2)` class |
| local group at a node | two **disjoint** transpositions, `H_p ≅ Z/2 × Z/2` | promoted (`pi1-s4-decision §2`), quoted `[R96] §6` |

All five are conjugacy invariants, so `OPEN[BMFACT-STRAND-VS-BLOCK]` does not
infect the arithmetic (`[G] §3`'s firewall, confirmed). Nothing labelled is used.

### 4.2 The four-box, enumerated rather than assumed

`sigma = #Fix(g) = 2`; `[SG]` Prop 2.4 gives `1 <= a <= sigma <= N − 2 = 2`; and
`a + b = sigma = 2` in `N = a + b + sum_j delta_j e_j` forces
`sum_{e_j>=2} delta_j e_j = 2`, i.e. **exactly one ramified boundary component
with `(delta,e) = (1,2)`**, so `ram = 2` is forced. The only freedom is
`b ∈ {0,1}` — precisely `OPEN[SHEET-LOCATION]`, open at `d = 4` in the
transposition class (`[SG] §9.1`). Both branches are carried:

```text
   branch B0 :  (a,b,ram)  = (2,0,2) ,  B_Y = B_1                (delta,e)=(1,2)
   branch B1 :  (a,b,ram)  = (1,1,2) ,  B_Y = B_1 ⊔ B_0 ,  B_0 with (delta,e)=(1,1)
```

### 4.3 `chi_c(Y)_RH`, from cycle types only

Stratify `A^2 = (A^2∖D) ⊔ D_0 ⊔ Sing D`; `[SG]` Lemma 5.1(a),(b),(c) and
Lemma 3.1 (fibre points = `H_p`-orbits, valid at every `p` since `Y` normal ⟹
unibranch):

```text
   chi_c(D)      = 1 − 4                                  = −3
   chi_c(A^2−D)  = 1 − (−3)                               =  4
   chi_c(V_rho)  = 4 · 4                                  = 16
   c             = #cycles(g) = 3 ;  chi_c(D_0) = −3 − 4  = −7
   c · chi_c(D_0)                                         = −21
   #q^{-1}(Sing D) = 4 nodes × #orbits(Z/2×Z/2) = 4 × 2   =  8
   ------------------------------------------------------------
   chi_c(Y)_RH   = 16 − 21 + 8                            =  3
```

Cross-check (MEASURED): the weighted count
`4·(4 − 7 + 4) = 4 = 4·chi_c(A^2)`, as a finite flat degree-4 map requires.

### 4.4 `chi_c(B_Y)`, computed — the part `(M′)` never names

> **Lemma SG-2.** Suppose every boundary component `B_j` is birational onto `D`
> (`delta_j = 1`), and let `m_Y = #components(B_Y)`. Then
> ```text
>    chi_c(B_Y)  =  m_Y · chi_c(D̃)  −  sum_{p ∈ Sing D} [ m_Y · r_p − c_p + a_p ] ,
> ```
> with `c_p = #q^{-1}(p)` and `a_p = #F^{-1}(p)`.
> *Proof.* Over `D_0`, `B_Y → D_0` is a covering (`[SG]` Lemma 3.3) of the
> smooth `D_0`, so `B_Y` is smooth there and all its singularities lie over
> `Sing D`. Each `B_j` is birational onto `D`, so its normalisation is `D̃` with
> `r_p` branches over `p`; the total branch count of `B_Y` over `p` is `m_Y r_p`
> while its *point* count there is `c_p − a_p` (the fibre points not in `U`).
> Apply `[SG]` 5.1(c) to `⊔_j D̃ → B_Y`. ∎

Because the branch count is what enters, SG-2 handles components meeting each
other automatically; no disjointness hypothesis is needed. Instantiating at
`a_p = 0` — forced, since `a_p <= s_p = #Fix(Z/2 × Z/2) = 0` by `[SG]` Cor 3.2:

```text
   branch B0 (m_Y = 1) :  chi_c(B_Y) = 1 − 4·(1·2 − 2 + 0) =  1
                          B_Y ≅ D̃ ≅ A^1 : the boundary is the normalisation of A_F
   branch B1 (m_Y = 2) :  chi_c(B_Y) = 2 − 4·(2·2 − 2 + 0) = −6
                          each B_j is a 4-nodal rational curve
```

Worth isolating: **if `b = 0`, the boundary divisor of a `(9,6,2)` Keller source
is forced to be the normalisation `A^1` of `A_F`, with no freedom at all** — a
structural fact about `B_Y`, and not in `(M′)`.

### 4.5 Verdict

```text
   branch B0 :  chi_c(Y)_RH = 3   vs   1 + chi_c(B_Y) =  2      gap  1   MISMATCH
   branch B1 :  chi_c(Y)_RH = 3   vs   1 + chi_c(B_Y) = −5      gap  8   MISMATCH
```

> **VERDICT (razor (b), Mode 1, `(9,6,2)`): MISMATCH in every admissible
> branch.** No `U` satisfying `(SRC-OPEN)` exists over the irreducible-`A_F`
> hypothesis. Per `[G]` Card I this is **confirmatory of H2 + `(M′)`**, and it
> is *not* a counterexample and not a new kill of the row. `(9,6,2)` lives in
> the reducible profile (`W = (1,2)`, `[R96] §7 R3`), which is Mode 2.
> `OPEN[MODE1-MATCH-VS-H2]` **does not arise** — there was no match.

### 4.6 THEOREM SG-1 — razor (b) in Mode 1 *is* `(M′)`

The load-bearing negative finding of the lane.

> **Theorem SG-1.** Under Keller + (H2) + (H3), the test
> `chi_c(Y) = 1 + chi_c(B_Y)` is **logically identical** to `(M′)`.
> *Proof.* `chi_c(Y) = chi_c(U) + chi_c(B_Y)` is additivity, so the test says
> exactly `chi_c(U) = 1`. Stratifying `U` (using `q^{-1}(A^2∖D) ⊆ U`, `[SG]`
> Lemma 2.3, and Lemma 3.3):
> `chi_c(U) = N(1 − chi_c(D)) + a·(chi_c(D) − s) + sum_p a_p`. With
> `chi_c(D) = 1 − nu` this is `N·nu + a(1 − nu − s) + sum_p a_p = 1`, i.e.
> `a(nu + s − 1) − sum_p a_p = N·nu − 1`, which is `(M′)` verbatim
> (`[SG]:442`). ∎

Consequences, all of them constraints on how this avenue may be sold:

1. **Razor (b) adds no kill power over `(M′)` in Mode 1.** `[G] §3` typed the
   Mode-1 mismatch as "confirmatory"; SG-1 upgrades that from expectation to
   theorem. §4.5's mismatch is `(M′)`'s `a = 2 ⟹ 2s >= 1 + 2s` contradiction
   (`[R96] §7 R4`) re-expressed, and the branch-B0 gap is the same one unit.
2. **The reduction runs component-wise**, so Mode 2 is likewise not independent
   of the block-free `(M′)`, already collapsed to `chi_2 + sigma_2 = 1` (`[R96]`
   (7.1)). **Path 2 must not count a Mode-2 Euler match as evidence additional
   to (7.1); it is the same equation.** This is the one place where the charged
   avenue, at face value, would have double-counted.
3. **What is genuinely new is Lemma SG-2**: the independent computation of
   `chi_c(B_Y)`, hence the forced isomorphism type of the boundary divisor.
   `(M′)` is a numerical identity in `a, a_p, nu, s`; SG-2 names the object.
   That is what a construction lane can consume and what `[S] §4`'s
   boundary-lattice mechanism needs as input.

Recorded invariant (MEASURED across all rows run): for the transposition class
with `chi_c(D̃) = 1` and `b = 0`, the gap is **exactly 1 for every node count** —
`s = 0`, `3` and `4` all give gap 1. The `b = 1` gap is `2s`.

### 4.7 The 3-cycle class, run for completeness

`[R96] §5`'s surviving classes all have transposition meridians, but the
four-box admits one other cycle type at `N = 4` (`[SG] §6.4`), so it is run
rather than assumed away. For `g` a 3-cycle: `sigma = 1`, `c = 2`, `a = 1`,
`ram = 3`, and `b = 0` is *proved* (`[SG]` Thm 4.3). At a node the two commuting
branch meridians lie in the centraliser of a 3-cycle in `S_4`, namely
`⟨(abc)⟩`, so `H_p = Z/3`, `c_p = 2`, `s_p = 1`, and `a_p ∈ {0,1}` is **not**
forced. MEASURED:

```text
   chi_c(Y)_RH = 16 − 14 + 8 = 10 ;  sum a_p ∈ [0,4] ;  gap ∈ [8,12]  MISMATCH
```

The gap is affine and strictly increasing in `sum a_p`, so the whole
`ACS-FIX-VS-DEFICIT` interval is decided by its endpoints and the branch closes
without declaring `a_p`. Mode 1 dies at `(9,6,2)` for **every** admissible cycle
type, not only the census one.

### 4.8 DEVIATION — the charged `(a,sigma,ram) = (2,2,2)`

`[G]` Card I types the expected four-box as `(2,2,2)`. `sigma` and `ram` are
confirmed and forced. **`a = 2` is not forced**: it is `a = sigma`, i.e. `b = 0`,
i.e. `OPEN[SHEET-LOCATION]` at exactly the profile where `[SG] §9.1` leaves it
open — the same hypothesis `[O] §4` types as `OPEN[ACS-FIX-VS-DEFICIT]`. The
charged expectation silently consumes an open bit. The verdict does not depend
on it (both branches mismatch), but the box should be re-typed
`(a ∈ {1,2}, sigma = 2, ram = 2)`, and `[R96] §7 R3`'s remark
"`a^{(1)} = N − W_1 = 2` and independently `a^{(1)} = #Fix = 2`" read as **one**
derivation: the second is the equality case of the first, not a confirmation.

### 4.9 DEVIATION — no compactification is used, so `OPEN[RH-LINE-AT-INFINITY]` does not arise

`[G]` Card I requires the compactification to be NAMED or the run returns
`OPEN[RH-LINE-AT-INFINITY]`. **No compactification is used anywhere above.**
Every step is `chi_c` on affine varieties via `[SG]` Lemma 5.1, which needs
neither smoothness nor properness nor `chi_c = chi`. Infinity enters at exactly
one place — `chi_c(D̃) = 1`, i.e. `D` rational with **one** place at infinity —
an affine statement about the normalisation of the affine curve (`(H3)`,
`[SG]:23`), verified for this row in `[R96] §1`. Naming `P^2`, `L`, `D̄`,
`delta_inf = 24` or `beta_1 = 25` would import a *projective* place into an
affine computation: the flag/place fallacy the requirement exists to prevent.
The requirement is honoured by not needing it, the token is **not** returned,
and the deviation is in the safe direction. `beta_1`, `delta_inf` and `e(iota)`
appear nowhere in §4's arithmetic.

---

## 5. Task 2(c) — BOUNDARY LATTICE: not reached, and what it would need

### 5.1 The banked lemma, as stated

`Lemma DET-LINF` (`domrina-gap-repair-opus5-20260901.md:141-176`):
`det L̃∞ <= 0` unconditionally, where `X̃` completes the **source** `C̃^2` and `F`
extends to a morphism of projective varieties, `L̃ = X̃ − C̃^2` is the boundary
tree, and `L̃∞ = L̃ − (dicriticals)`. Its proof needs (i) `X̃ − L̃∞` affine,
(ii) `Pic(X̃)` freely generated by the components of `L̃`, plus `L̃∞` connected
and made of smooth rational curves.

### 5.2 Status at `(9,6,2)` Mode 1

Razor (b) has already refuted `(SRC-OPEN)` in Mode 1, so there is no admissible
`U` to complete. **Razor (c): NOT REACHED.** Its input — the dual graph of `L̃`
on a declared completion with its dicritical/non-dicritical split — is not
derivable from `INPUT-rho-D`, since cycle types determine `delta_j` and `e_j`,
not a resolution tree. Typed `OPEN[SOURCE-OPEN-COMPLETION-UNDECLARED]`, carried
to Mode 2, where `[S] §4` correctly makes it wait on a full `phi`.

### 5.3 The empty-`L̃∞` determinant trap — named and refused

A tempting free kill: complete `U ≅ A^2` to `P^2`, declare the boundary line `L`
dicritical, get `L̃∞ = ∅` and `det(∅) = 1 > 0`, contradicting DET-LINF. **This is
refused.** `det` of the empty matrix is a convention, and DET-LINF's proof
explicitly uses `L̃∞` connected and nonempty (Grauert contraction); the lemma
says nothing about the empty case. Running it would be a floor/attainment and
pole/interior violation at once. Recorded so no successor re-imports it.

### 5.4 The one free consequence, stated honestly

Step (i) does give something: `X̃ − L̃∞ = F^{-1}(C^2)` is affine, an affine
surface is not projective, so `L̃∞ ≠ ∅` — **not every boundary component of an
admissible completion is dicritical.** For `X̃ = P^2` with `L̃ = {L}` this forces
`L̃∞ = {L}`, `det = L·L = 1 > 0`, contradiction, so any admissible completion has
`rho(X̃) >= 2`. That merely reproves that a Keller counterexample does not extend
to a morphism `P^2 → P^2` (elementary: such a morphism is finite).
**Consistency check, not new information.**

---

## 6. Task (4) — `OPEN[ACS-FIX-VS-DEFICIT]`, carried

`[O] §4`: `a^{(i)} <= #Fix(meridian_i)` and `a_p <= |Fix(H_p)|`, with equality an
extra hypothesis. This is `[SG]` Cor 3.2 (`a_p = s_p − b_p`) at the generic and
special points respectively, and `[O]`'s independent derivation agrees. It is
carried at every use above:

* §4.2 — `a = sigma` is **not** taken; both `b ∈ {0,1}` are enumerated.
* §4.4 — `a_p = 0` at the nodes is used, and it is *forced*, not assumed:
  `s_p = #Fix(Z/2×Z/2) = 0` and `0 <= a_p <= s_p`. This is the one place where
  the inequality direction alone suffices, and it is the reason the Mode-1
  verdict survives the open bit.
* §4.7 — where `s_p = 1` the interval `a_p ∈ [0,1]` is carried symbolically and
  the branch is decided over the whole interval.
* §7 — `box/covergeo.py` refuses an undeclared `a_p` with `s_p > 0` unless the
  entire interval decides, and refuses a declared `a_p > s_p` outright.

`[O] §4`'s sharper observation is confirmed and worth re-recording because it is
the strongest form of the caution: at the `N = 4` reducible profile,
`W_2 = 1` gives `a^{(2)} = 3`, and **no element of `S_4` has three fixed
points**, so `a^{(i)} = #Fix` is false there and the deficit is at infinity, not
in the monodromy. Any all-`N` statement quoting `a^{(i)} = N − W_i` as a
fixed-point count must carry the inequality. `OPEN[ACS-FIX-VS-DEFICIT]` stays
open; nothing in this lane closes it.

---

## 7. Task (3) — `box/covergeo.py`, delivered

### 7.1 Typed I/O

Input is `INPUT-rho-D` (§2) as dataclasses `Row / Component / SingPoint /
LocalType`, plus a mandatory `source_gate` provenance string. Output per
admissible four-box branch: `chi_c(D)`, `chi_c(D_0)`, `chi_c(V_rho)`, `c`,
`sigma`, `ram`, `sum c_p`, `chi_c(Y)_RH`, `chi_c(B_Y)`, `chi_c(U)`, `gap`, and a
verdict in `{MATCH, MISMATCH, MISMATCH-ON-INTERVAL, OPEN[...]}`.

### 7.2 Fail-closed rules, as implemented

1. cycle type must be a partition of `N`, `sigma >= 1` (box `(U,e=1)` nonempty)
   and some `e_j >= 2` (purity) — else `OPEN[COVERGEO-BAD-CYCLE-TYPE]` /
   `OPEN[COVERGEO-NO-AFFINE-SHEET]` / `OPEN[COVERGEO-UNRAMIFIED]`;
2. `a = sigma` never assumed — all `b` enumerated unless declared **with a
   citation** (`OPEN[COVERGEO-UNCITED-B]`);
3. `a_p > s_p` refused (`OPEN[COVERGEO-AP-EXCEEDS-FIX]`, `[SG]` Cor 3.2);
   undeclared `a_p` is decided over the whole interval or returned
   `OPEN[ACS-FIX-VS-DEFICIT]`;
4. `delta_j > 1` → `OPEN[COVERGEO-DELTA-GT-1]` (Lemma SG-2 does not apply);
5. empty `source_gate` → refuse. The module does **no** polynomial arithmetic,
   so footgun #10 (`squarefree_part()` ≠ `radical()`) cannot fire inside it; the
   guard forces the caller to declare a radical-verified upstream source;
6. footgun #11: the entry point is the public `main()`, the `__main__` guard is a
   convenience, `COVERGEO_FORCE_MAIN=1` is honoured, and `main()` asserts it
   emitted its seal line — a silent empty run with rc=0 is impossible;
7. `E = e(iota)` is a row **label**, never read by any arithmetic; `c_2` is
   refused by construction (§7.4).

### 7.3 Controls — MEASURED, all pass

The suite is deliberately built so that MATCH and MISMATCH are both reachable;
a calculator that can only mismatch is not a calculator.

```text
CTRL-P1  smooth A^1 branch, 3-cycle class (a=1 forced)          MUST MATCH     -> MATCH
CTRL-P2  smooth A^1 branch, transposition: a=2 MUST FAIL,       MISMATCH/MATCH -> as expected
         a=1 MUST MATCH        [ = the SHEET-GATE smooth-A_F law, a = 1 ]
CTRL-962 (9,6,2) four-box (sigma,ram) MUST be (2,2)             -> (2,2)  OK
         every branch MUST MISMATCH                             -> MISMATCH, MISMATCH
CTRL-962b (9,6,2) 3-cycle class                                 -> MISMATCH-ON-INTERVAL, gap ∈ [8,12]
CTRL-64  (6,4,3) negative control MUST NOT MATCH                -> MISMATCH, MISMATCH
CTRL-REJECT  bad cycle type / no source_gate / a_p > s_p / c_2  -> all four RAISE typed OPEN
CTRL-869  S_4 -> S_4/V_4 = S_3 at an affine node: orbit sizes (2,1)  -> reproduces TB-GERM's 10 A_1 points
CONTROLS: ALL PASS
```

`CTRL-P1/P2` are the discriminating pair: they independently re-derive `[SG]
§8`'s "smooth `A_F` ⟹ `a = 1`" law from the Euler side, which is the strongest
available evidence that the engine is not hard-wired to kill.

**DEVIATION on the charged negative control.** `[G] §6` specifies "negative
control `(6,4)` at `E = −3` must not match". Two corrections. (i) The banked
`(6,4,3)` row has `beta_1 = 15` and `e(iota) = 10 − beta_1 = −5`, not `−3`;
`E = −3` is the *deliberately falsified* value in `[R96] §9`'s verification
control for the **CABLE-3 inner-braid divisibility gate** ("confirm both
`E = −5` passes and `E = −3` fails"), a different instrument. (ii) `e(iota)` is
a braid exponent; feeding it to a `chi_c` calculator would identify a cover
series with an Euler number — the flag/place/series fallacy. The control is
therefore implemented on the actual row (`beta_1 = 15`, `delta_aff = 3` nodes,
transposition class), `E = −5` is recorded as a label only, and it MISMATCHES as
required (gaps 1 and 6).

### 7.4 The `(8,6,9)` path — and the REFUTATION of "same Chern species"

`[G] §4` claims the missing `(8,6,9)` input `c_2(T) = chi(O_Z)` and
`chi_c(Y)_RH` are "the same Chern-number species", and charges one pipeline to
serve both. **Refuted as stated**, on the source `[G]` itself cites:

* `chi_c(Y)_RH` is a compactly-supported **topological** Euler characteristic of
  a **non-compact affine** normal surface, computed by stratified additivity. It
  is not a Chern number of anything and uses no compactification (§4.9).
* `tb-g2-finish-opus5-20260901.md:435` fixes the other object exactly:
  `chi(O_Z) = 23 − c_2(T^v)`, where `T` is the rank-2 **Tschirnhausen bundle**
  of the triple plane — not the tangent bundle — and `Z` is **projective and
  singular** (one non-Gorenstein point `C[z,w]/(z,w)^2`, ten `A_1` points). For
  singular `Z`, `chi(O_Z)` is a holomorphic Euler characteristic and `c_2(T^v)` a
  Chern number of a bundle on `P^2`; neither is a topological `chi_c`, and the
  same report says `c_2(T)` "is not fixed by the numerical type".

Identifying them would be a flag/place/series identification and a
pole/interior violation (using a Chern-class identity without checking the
vertex class and the source hypotheses). What **is** genuinely shared is one
layer, and the module implements exactly that and nothing more:
`fibre_partition_over` / `s4_to_s3_orbits` — *conjugacy-invariant local monodromy
→ orbit decomposition → point count and local type*. Run on `(8,6,9)`
(`CTRL-869`, MEASURED): pushing the node-local `⟨(01),(23)⟩ ⊂ S_4` through
`S_4 → S_4/V_4 = S_3` gives orbit sizes `(2,1)` on three sheets, i.e. one `A_1`
point of `Z` over each of the ten affine double points — **reproducing TB-GERM
§7.1's "10 `A_1` points" from the calculator**, which is the positive control the
charge wanted at that row. Asking the module for `c_2` returns
`OPEN[COVERGEO-C2-TSCHIRNHAUSEN]` with the missing inputs named: the singularity
census of `Δ̄` with its local monodromy, `K_Z` or a declared resolution, and the
`Z/3`-cover class. That is `[G] §6`'s own fallback ("or returns OPEN
(curve-dependent)"), reached for a sharper reason than curve-dependence.

---

## 8. What this hands Mode 2 / Path 2 — bounded, not a Path-2 duplicate

Three items, no construction of `D_2` attempted:

1. **Do not double-count.** By THEOREM SG-1 (component-wise form), a Mode-2
   four-box Euler match is the block-free `(M′)`, already collapsed to
   `chi_2 + sigma_2 = 1` (`[R96] §7 (7.1)`). `[S] §4`'s nodal-cubic control
   `t ↦ (t^2−1, t(t^2−1))` with `chi_c(D_2) = 0`, `sigma_2 = 1` attains it, so
   the identity is a must-pass, not a discriminator — `[S]`'s own reading,
   confirmed here by an independent route.
2. **Lemma SG-2 is the new deliverable for Path 2.** Once `D_2`'s type is
   emitted, SG-2 returns `chi_c(B_Y)` and hence the boundary divisor's forced
   isomorphism type — which is precisely the missing input of `[S] §4`'s
   boundary-lattice mechanism and of razor (c). The two meet at `chi_c(B_Y)` and
   at `r(E)` (§3.8), and at no other number.
3. **Razor (a)'s rank decides razor (b)'s free bit** (Cor HC-2). Sequencing:
   BMFACT → HOM-COVER torsion (free kill) → rank (fixes `b`) → four-box Euler
   with `b` no longer open → boundary lattice. Each step consumes the previous
   step's output; none of them is a substitute for the construction.

---

## 9. Typed verdict block

```text
LANE                SOURCE-GATE-962  (retype + three razors, Mode 1 on (9,6,2))

TASK 1  RETYPE      DONE.  Lemma SRC-0 (three Y's are one scheme) PROVED-HERE,
                    UNREVIEWED.  (SRC-OPEN) is the single typed object; the three
                    submissions are consistent and are reconciled by SRC-0.
                    OPEN[REP-96-SOURCE-IS-C2] RETIRED AS MIS-TYPED (asks for an
                    unsatisfiable property); successor OPEN[SOURCE-OPEN-U],
                    alias OPEN[REP-96-A2-OPEN-IMMERSION-BOUNDARY].

TASK 2a HOM-COVER   INSTRUMENT: AUDITED, 4 controls CONFIRMED correct; TWO DEFECTS
                    (fail-open on convention; convention-blind control suite);
                    REPAIRED in box/cover_h1.py, CONTROL 4 added, all pass.
                    B_3 census reproduced exactly (25% / 56% torsion).
                    RUN AT (9,6,2): NOT RUN — PENDING-INPUT.
                    OPEN[REP-96-BM-FACTORISATION], OPEN[BMFACT-BASEPOINT].
                    NEW: Lemma HC-1 (r(E) <= a), Cor HC-2 (rank decides b).

TASK 2b FOUR-BOX    RUN.  chi_c(Y)_RH = 3.  Four-box (a,sigma,ram) = (a,2,2) with
        EULER       a in {1,2}.  b=0: 1+chi_c(B_Y) = 2, gap 1.  b=1: −5, gap 8.
                    VERDICT MISMATCH in every branch, and also in the 3-cycle
                    class over the whole ACS interval (gap 8..12).
                    CONFIRMATORY of H2+(M'), NOT a CE, NOT a new kill.
                    OPEN[MODE1-MATCH-VS-H2] does not arise.
                    THEOREM SG-1: this razor IS (M') — PROVED-HERE, UNREVIEWED.
                    Lemma SG-2 (chi_c(B_Y)) is the razor's only new content.

TASK 2c BOUNDARY    NOT REACHED (no admissible U in Mode 1).  Input not derivable
        LATTICE     from cycle types: OPEN[SOURCE-OPEN-COMPLETION-UNDECLARED].
                    Empty-L-tilde-infinity determinant trap NAMED and REFUSED.

TASK 3  covergeo.py DELIVERED, fail-closed, footguns #10/#11 honoured, controls
                    ALL PASS incl. two MATCH controls, the (9,6,2) four-box, the
                    (6,4) negative control, four rejection probes and CTRL-869.
                    grok §4 "same Chern species": REFUTED AS STATED; the shared
                    layer is implemented, c_2(T^v) refused.

TASK 4  ACS         CARRIED at every use; forced (not assumed) where used;
                    OPEN[ACS-FIX-VS-DEFICIT] remains open.
```

---

## 10. Deviations

1. **§4.8** — the charged four-box `(2,2,2)` is re-typed `(a ∈ {1,2}, 2, 2)`:
   `a = 2` rides `OPEN[SHEET-LOCATION]` / `OPEN[ACS-FIX-VS-DEFICIT]`. Verdict
   unaffected; both branches run.
2. **§4.9** — no compactification is named because none is used;
   `OPEN[RH-LINE-AT-INFINITY]` is **not** returned. Naming one would import a
   projective place into an affine computation.
3. **§7.3** — the charged negative control "`(6,4)` at `E = −3`" is corrected:
   the row's `e(iota)` is `−5`, `E = −3` is `[R96] §9`'s falsified value for a
   *different* gate, and `E` is recorded as a label and never consumed.
4. **§3.5** — `box/cover_h1.py` was modified (additively, non-breaking) rather
   than only reported on, because the defect found is a fail-open that would
   have produced a false *survival* on the very input the charge anticipates.
   The four original controls are byte-identical in behaviour.
5. **§4.6** — the lane reports that its own charged razor is not independent of
   `(M′)`. Reporting this rather than presenting the mismatch as new kill power
   is the deviation that most changes how the avenue should be funded.
6. **§7.4** — the charge's premise that one calculator serves both `(9,6,2)` and
   `(8,6,9)`'s `c_2(T)` is only partly honoured: the shared layer is delivered
   and controlled, the `c_2` half is refused with named missing inputs.

---

## 11. OPEN list

| token | status after this lane |
|---|---|
| `OPEN[SOURCE-OPEN-U]` | **NEW**, replaces `OPEN[REP-96-SOURCE-IS-C2]`. Open in Mode 2; closed NEGATIVE in Mode 1 at `(9,6,2)`, by an argument equivalent to `(M′)`. |
| `OPEN[REP-96-SOURCE-IS-C2]` | RETIRED as mis-typed (§1.4). Not closed — re-homed. |
| `OPEN[REP-96-BM-FACTORISATION]` | unchanged; now also blocks razor (a). |
| `OPEN[BMFACT-BASEPOINT]` | unchanged; infects every labelled transport, hence razor (a), not razor (b). |
| `OPEN[SHEET-LOCATION]` (`b = 0`?) | unchanged; §3.8 shows razor (a)'s rank would decide it at this profile. |
| `OPEN[ACS-FIX-VS-DEFICIT]` | unchanged; carried, not consumed. |
| `OPEN[SOURCE-OPEN-COMPLETION-UNDECLARED]` | **NEW**; razor (c)'s missing input. |
| `OPEN[COVERGEO-C2-TSCHIRNHAUSEN]` | **NEW**; `(8,6,9)`'s `c_2(T^v)` with its missing inputs named. |
| `OPEN[MODE1-MATCH-VS-H2]` | **does not arise** — there was no match. |
| `OPEN[RH-LINE-AT-INFINITY]` | **does not arise** — no compactification used. |
| `OPEN[BMFACT-STRAND-VS-BLOCK]` | untouched; razor (b) is conjugacy-invariant throughout. |

---

## 12. FALLACY-v2 audit

* **Flag/place/series.** Held at four sites: `E = e(iota)` is never an Euler
  number (§7.3, and refused in code); `chi_c` of an affine surface is never a
  Chern number (§7.4); the place at infinity of `D` enters only as `chi_c(D̃)=1`
  and never as `delta_inf`, `beta_1`, `L` or `D̄` (§4.9); `B_Y` is a divisor on
  `Y`, never a dicritical or a Puiseux place of `D`.
* **Carrier/attainment.** HOM-COVER is stated as a floor-side filter, never an
  attainment certificate (`[O]`'s own discipline, kept). `(SRC-OPEN)` is
  necessary-only. One realized `(9,6,2)` representative is not
  `FULL_ACTUAL_EXIT` and no row-level kill is claimed anywhere.
* **Floor/attainment.** The four-box split is a floor; `ram = 2` is proved, not
  capped. `det L̃∞ <= 0` is used as a floor, and its strict form is not asserted.
* **Pole/interior.** The empty-`L̃∞` determinant is refused (§5.3) because the
  vertex class and the source hypotheses of DET-LINF fail there.
* **`sat()` / raw remainder / variable-ring map.** Not applicable: no CAS, no
  Gröbner basis, no polynomial arithmetic. `covergeo.py` does integer arithmetic
  on conjugacy invariants only.
* **Prime label/derivative.** `(M′)` is `[SG]`'s named identity; the prime is a
  label, not differentiation.
* **Target/arrival index.** `a, a_p, sigma, s_p, b, b_p, c, c_p, delta_j, e_j,
  r_p, nu` are kept distinct and defined at first use. The two campaign symbols
  `b` (`[R96] §7 R3`: sheet-location count vs. branched-component count) are not
  merged; only `[SG]`'s sheet-location `b` appears here.
* **No safe replacement ⟹ typed OPEN.** Applied at razor (a) (no presentation),
  razor (c) (no completion) and `c_2(T^v)` (no `K_Z`). No gap filled by cap or
  analogy. No exit-price assertion, so no `charge_basis` line.

---

## 13. Custody and sources

Charged inputs: five hashes in §0, all matching. Campaign documents cited by
file and line are listed in §0. No external literature was fetched and no new
primary source is claimed. The `(9,6,2)` curve data (`p = t^9+12t^5+24t`,
`q = t^6+8t^2`, four nodes, one place at infinity) is `[R96] §1`'s, consumed as
given. Files written or modified: `box/covergeo.py` (new), `box/cover_h1.py`
(additive repair, §3.5), and this report. No canonical ledger was edited, no
charged file modified, no commit, push, AWS action or CAS run.

No `charge_basis` line: this report asserts no new exit price.

<!-- BODY-END -->
