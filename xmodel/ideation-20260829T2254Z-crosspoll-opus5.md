# Adversarial cross-pollination — Opus 5 — round `20260829T2254Z`

Identity: Opus 5 (equal-standing lane; author of the blind report
`d8e73284…` attacked below).
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
Lifecycle: `ADVERSARIAL_SYNTHESIS_INPUT / NO PROMOTION CLAIMED / NOT A REVIEW`.

## 0. Custody, boundary, and desk receipts

Packet recomputed before use: full
`2cf36dadfea4df017a7c72dee33c43218ddd5a3ea4e9a220908d6d721c76f9cb`,
body `13554` bytes /
`f090063ee7b23b08473cb541fba2c077d94d86295b0e083a1274cc5be69d420d`
(single standalone `<!-- BODY-END -->`). All thirteen files named by the
packet recomputed and matched byte-exactly:

```text
d1cc6a64… state          bc66a627… sol56           72aa958a… sol56-alt
af5eedb7… fable5         d8e73284… opus5 (mine)
6f300d98… unloaded-radical review        e3e84ac9… its integration
7082bf67… R4-00 R1/R2 review             4f891280… its integration
0ee84a0b… all-faces review               7c73616d… its integration
9fab2e96… monomial-chart divisibility    bbe6ac2f… e3m1 G9 rank-one kill
```

I read no artifact created after the packet: no `*-crosspoll-*` peer output,
no prompt, no log, no `.run.v2`, no post-packet report. No web, no AWS, no
commit/push, no canonical edit, no `jc2-lean` access of any kind. Exactly one
file is written, this one.

**Desk work performed** (Python 3.9 stdlib `fractions` only; exact Gaussian
rationals; truncated `Q(i)[[τ]]`; every run under 4 s and far under 1 GiB;
scratch in `/tmp/xp`, nothing else written). One frozen input was read:
`cases/max12_812_order2_u2_62_k00_unloaded_surface_local_v1_20260829/aws_r6b_global_power_v4/prelude_Q.sing`,
recomputed `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`,
identical to the value in my blind §1.1 and in the charged producer's §2.
Receipts appear inline at §3–§5 and are summarised at §9.

No new exit-price assertion is made anywhere in this report, so no
`charge_basis` line appears.

Typing held throughout: a finite jet is not a formal arc, an algebraic germ,
a map, occurrence, attainment, or JC2; a floor is not attainment; equality of
sets is not equality of schemes; `G2-PSC` and `G2-BD` stay distinct; B and S
stay distinct. Grok's lane is `UNAVAILABLE_NO_MODEL_WORK`, not an abstention,
and nothing below attributes any position to it. Post-cutoff results are
never attributed to a blind researcher.

---

## 1. Deduplicated novelty table

`NEW` / `KNOWN` / `DUPLICATE` / `SCOPE-CONFLICT` / `REFUTED`, with
independent convergences and live disagreements preserved.

| Item | Origin | Class | Adjudication |
|---|---|---|---|
| Seven-quadric leading system + degeneracy quartic `Δ` | Opus blind §1.3 | **NEW, SCOPE-REPAIRED** | The exact object survives; the *normal-cone* wording does not. See §2 V3 and §3.3. Repaired name: **seven-quadric leading system**. |
| `Δ` irreducible over `Q`, rational, node + two conjugate cusps | Opus blind §1.4 | **NEW, now CAS-free** | Reproved this round without CAS by inverting the parametrisation (§3.3.4). Independent of the earlier `factorize` call. |
| `I ⊆ J²` | Opus blind §1.2 **and** Sol blind §4 | **KNOWN, INDEPENDENT CONVERGENCE** | Two independent recomputations. It is also the load-bearing half of the sandwich (§2 V2). |
| `J^17 ⊆ I` from four fifth powers | Sol blind §4 | **NEW COMPOSITION, CONFIRMED, SHARPNESS TYPED** | Proof correct. New this round: 17 is *exactly sharp relative to the four certificates alone*, and `N_min ∈ [5,17]` (§3.1). |
| Two-sided valuation sandwich `2v(J) ≤ v(I) ≤ 17v(J)` | Sol blind §4 | **CONFIRMED, HALF VACUOUS** | Upper half is vacuous whenever the load value `L ≤ 17`; that includes the only live ramified cell, where `L = 9` measured (§3.2). |
| `A(x)=x5+16x1−4x3`, `B(x)=x0−4x2+2x4` as linear parts of `f5+2f1`, `f0−4f2` | Opus blind §1.5.1 | **KNOWN object, NEW derivation, INDEPENDENTLY CONFIRMED** | The post-cutoff G9 packet's (2.1) is byte-identical to my blind forms, and its `w_ε` satisfies `A(w)=B(w)=0` — verified here (§4.1). Confirmation, not co-discovery: that packet is post-blind. |
| Normal-order dichotomy `L = 2ρ` **or** `e_ρ` degenerate | this report §3.5 | **NEW** | Three-line lemma unifying `I ⊆ J²` (Sol) with the leading system (Opus). Immune to the standard-basis gap. Verified against the frozen rows. |
| Opus §1.8(c) `Δ`-branch contact prediction | Opus blind §1.8(c) | **REFUTED (self)** | Order-3 coefficient is `0`, not `4i` (§4.2). The orders ≤2 agreement is *identically* the G8 compatibility relation, hence not evidence. |
| `K00-SPLIT-COORDINATE-PREPASS` / `JET-IMAGE` / `RAMFAN` | Opus §6 / Sol-alt §6 / Sol Card C | **DUPLICATE FAMILY — MERGE** | Agreed with the packet. Merged spec at §6.1 (`K00-TC`). |
| Monomial-chart divisibility `[s^{u-2}](f_s g_t − f_t g_s) ∈ (t)` | post-cutoff Sol note | **CONFIRMED, SCOPE DOWNGRADED** | Identity and support lemma independently re-derived. But the hypothesis forces `F,G ∈ K+(x)`, whence `Jac ∈ (x)` in two lines (§5.1). |
| Sol blind (5.1) "first transverse gate `(u−1)(AQ′−P′B)=1`" | Sol blind §5 | **SCOPE-CONFLICT, resolved against the blind form** | True only under the ansatz `a_1=…=a_{u−2}=0`; the general coefficient carries the middle terms. The post-cutoff note supersedes it, and §5.1 supersedes both. |
| Nonlinear rational-termination on the literal nodal chart | Sol blind Card B | **REFUTED CLIENT (a fortiori)** | Dead for a reason more elementary than the note's: §5.1. |
| Pair-square off-diagonal event module | Sol-alt Card 1 | **NEW APPLICATION, first discriminator sharpened** | `Z=(X×_U X)∖Δ` depends only on the étale cover, i.e. on the monodromy group and boundary — it cannot see `J=1` (§5.2.1). Target is numerically `d ≥ s+Σb_i`. |
| `ATYP-COUNT` via asymptotic critical values | Fable §3.1 / Card 3 | **NEW mechanism, TARGET FALSIFIED as stated** | `f = x + x²y + x³y²` is primitive, has **no critical points**, `s=3`, `#atypical=1 < s−1` (§5.2.2). Stage A is answered before it was run. |
| Intermediate block surface `B_K` | Sol-alt Card 2 | **KNOWN direction, SHARPENED here** | `B_K ⊆ C[x,y]` and finiteness over `C[f,g]` both CONFIRMED. The `A²` theorem is the wrong target; the right one is a codim-1 image criterion (§5.3). |
| Collision-partner Galois descent | Opus blind Card C | **LOWER (self)** | The base field is algebraically closed; §5.2.3 states the only surviving typed form and I do not launch it. |
| Tougeron layer on the `e=3` fixture | Fable Card 1 | **POST-EVENT DEFER** | The branch it was to decide is dead at G9. Reactivation condition stated verbatim at §4.5. |
| Avenue 33 period instrument | Fable §3.3 | **SELF-REFUTED, RECORDED** | Agreed; do not re-derive. |
| Avenue 27 PALF sub-lane | Opus / Sol-alt lower; Fable unchanged | **DISAGREEMENT, resolved to LOWER** | The A2-filling category is empty for a submersion; that is a scope fact, not a rank preference. |
| `ADAPTER-PREFLIGHT` checkpoint clause | Opus blind §9 | **REFUTED (self)** | A runner cannot force checkpointing inside one monolithic provider response; the packet says so and it is right (§6.2). |
| Systems: preflight / cap-retry / sectioning / claim-lint | Opus / Sol / Fable / Sol-alt | **SYSTEMS FAMILY — one only** | Selected: sectioned *independent* calls (§6.2). |

---

## 2. Typed verdicts

**V1 — `J^17 ⊆ I`: `CONFIRMED` (conditional on the four reviewed fifth-power
certificates).** Proof audited: any generator of `J^17` is a monomial
`f_0^a f_1^b f_2^c f_5^d` with `a+b+c+d=17`; if all four exponents were `≤4`
the total would be `≤16`. Additional typing this round: **17 is exactly sharp
as a consequence of the certificates alone** — in `A=Q[f_0,f_1,f_2,f_5]` with
`I_0=(f_0^5,f_1^5,f_2^5,f_5^5)` every hypothesis holds and
`f_0^4f_1^4f_2^4f_5^4 ∈ J^16∖I_0`. And since the promoted review states the
minimal power is **five**, `f_a^4 ∉ I`, so `J^4 ⊄ I`. Hence
`N_min := min{N : J^N ⊆ I} ∈ [5,17]`, and 17 can be lowered only by new mixed
membership tests, never by re-reading the same certificates.

**V2 — valuation sandwich `2v(J) ≤ v(I) ≤ 17v(J)`: `CONFIRMED, WITH ONE HALF
TYPED VACUOUS`.** Both inclusions transfer to a centered arc under
`v(A)=min{v(a)}` because polynomial coefficients have `v ≥ 0` and
`v(J^k)=k·v(J)`. What follows: linear equivalence of the `I`-adic and
`J`-adic filtrations along any centered arc, with slope window `[2,17]`.
What does **not** follow: equality of integral closures, any Rees-valuation
value, permission to substitute the graph into a mixed loaded row, or a map.
The narrowing is quantitative. Along a source arc the source equation gives
`v(I) = L := min_i ord_τ (target−load)_i`, so the sandwich reads
`L/17 ≤ ρ ≤ L/2` for `ρ := v(J)`. The lower bound is weaker than the trivial
`ρ ≥ 1` whenever `L ≤ 17`. I measured `L = 9` on the only live ramified family
(§4.1), so **the `J^17` half is strictly vacuous there**; it can first bite in
the `K6` (G20), `K2` (G32), `μ` (G43+) and `Jdet` (G57) sectors, and its
strength there is governed by `N_min`, not by 17. The load-bearing half is
`I ⊆ J²`, which gives the ceiling `ρ ≤ L/2`.

**V3 — maximum safe `Δ` theorem: `REPAIRED, NOT WITHDRAWN`.** The safe
statements are

- *(exact, iff)* for the ideal generated by the seven degree-two initial
  forms `Q_1,…,Q_7`: for every char-0 field `K` and every `(S_0,T_0) ∈ K²`
  there is a nonzero `ν ∈ K̄⁴` with `Q_i(ν;S_0,T_0)=0` for all `i` **iff**
  `Δ(S_0,T_0)=0`;
- *(one-way only)* for the true filtered initial ideal `in_J(I)`, hence for
  the normal cone: **if the projectivised fibre is nonempty over `(S_0,T_0)`
  then `Δ(S_0,T_0)=0`.** The converse is **not** claimed.

I supply no filtered-standard-basis certificate and therefore withdraw the
words "the projectivised normal cone … is empty over exactly the complement".
Every application I made uses only the one-way direction (§3.3.3), so nothing
downstream is lost. Full argument and the reason the defect is plausible: §3.3.

**V4 — monomial-chart divisibility: `CONFIRMED, SCOPE MATERIALLY DOWNGRADED`.**
The coefficient identity and the support lemma are both correct and were
re-derived independently here. Two corrections to its billing: (a) the
hypothesis "`f,g` have no negative `s`-powers" is equivalent to
`supp(F),supp(G) ⊆ {B ≤ uA}`, which forces `F,G ∈ K + (x)` and hence
`Jac(F,G) ∈ (x)` in two lines with no `u`, no chart and no coefficient
formula (§5.1); (b) the obstruction is **invariant under `t`-translation**,
which the note conservatively disclaims — the real evasions are boundary
poles and a changed support semigroup.

**V5 — `e=3,m=1` G9 scope: `CONFIRMED AT ITS DECLARED SCOPE, AND NARROWED`.**
I reconstructed the family from a *different* frozen artifact
(`prelude_Q.sing`, not the 569-tail compiler) and reproduced, at eight random
points of the G8-compatible family covering both signs and random
`β, y_{1..4}, z, u, r, h`: all seven rows of order exactly 9, and
`[τ^9] r_6 = ε·i·q³/32` with no dependence on `t, β, y, z, u, r, h`
(§4.1). The producer's `−4 → −3` mutation control also reproduces
(order drops 9→8). Scope stands as written: reduced/field-valued point-set
emptiness of the *stable rank-one G8-compatible family* on `D(q)` at
`e=3,m=1` — not the cell, not other `(e,m)`, not scheme structure, not an
arc statement. New narrowing: on the declared K10 unit open the residual
`e=3,m=1` census is **finite and short** — `{ρ=3 off-fan, ρ=4, ρ=∞}` plus the
prefix cases `ρ≤2` that must be *cited*, not assumed (§4.3).

---

## 3. Mandatory attack 1 — unloaded ideal, Rees sandwich, cone

### 3.1 `J^17` (packet 1.1)

Verdict V1. The pigeonhole is right and the constant is a pigeonhole
constant, exactly as Sol says. My addition is the sharpness dichotomy: no
argument that consumes only `I ⊆ J²` and the four fifth powers can produce
`N < 17`, because the monomial model attains it; and the promoted minimality
of the exponent five gives the matching floor `N_min ≥ 5`. Mixed identities
lower `N` only if actually computed: e.g. any certificate of the form
`f_a^3 f_b^2 ∈ I` for all ordered pairs would drop the pigeonhole threshold
from `4·4+1=17` to `4·2+1=9`. **That is the cheapest possible sharpening and
it is a bounded, preregisterable membership battery, not a theorem.**

### 3.2 The sandwich (packet 1.2)

Verdict V2. Two further hostile points.

*(i) The sandwich is not independent of the leading-form analysis.* The half
that does the work, `2ρ ≤ L`, is exactly the order estimate in my Lemma
(§3.5): `r_i = Q_i(e;S,T) + (deg ≥3 in e)` gives `ord r_i ≥ 2ρ` directly.
So Sol's lower bound and my `Q` are the same fact seen from two sides; the
Lemma additionally identifies the *equality case*, which the sandwich cannot.
This is a genuine convergence, not two results.

*(ii) The convention needs the arc centered, and `ρ=∞` must be typed.* If the
arc lies on the graph then `v(J)=v(I)=∞` and the source degenerates to
"load equals target identically". That is a legitimate stratum and neither
the sandwich nor the Lemma says anything about it; it must be carried in any
census as a separate case (§4.3).

### 3.3 Separating the seven quadrics from `in_J(I)` (packet 1.3) — the
attack the packet demanded on my own object

**3.3.1 What is certainly true.** `(f_0,f_1,f_2,f_5,d_3,d_4)` is a triangular
polynomial coordinate system, so writing `e=(e_0,e_1,e_2,e_5)`,
`(S,T)=(d_4,d_3)` is an exact change of variables. `I ⊆ J²` and
`I ⊄ J³` hold (recomputed). In degree 2 there is **no** defect: any
`F=Σ h_i r_i ∈ I` has `J`-order-2 part `Σ h_i(e=0)·Q_i` with
`h_i(e=0) ∈ Q[S,T]`, so
`in_J(I)_2 = Q[S,T]·⟨Q_1,…,Q_7⟩` exactly.

**3.3.2 Where the defect can live, and why it is likely.** New initial forms
can appear in degrees `≥3`: whenever a combination `Σ h_i r_i` has `J`-order
`≥3`, its initial form is a new element of `in_J(I)` unless it already lies in
`(Q)`. Equivalently, `(Q) = in_J(I)` iff `r_1,…,r_7` are a standard basis for
the `J`-adic filtration, iff every syzygy of the `Q_i` over `Q[S,T][e]` lifts.
Over the generic point the seven quadrics have `vdim 16` and `h`-vector
`(1,4,6,4,1)` — the numerics of a complete intersection of **four** quadrics.
So generically three of the seven are redundant and the syzygy module is
large; there is no reason for all of it to lift. **I therefore treat
`(Q) ⊊ in_J(I)` as the default and the equality as an unproved claim.** The
burden is mine and I do not discharge it here (a filtered standard basis is
not desk-scale).

**3.3.3 What survives, and why the applications are unaffected.** Since
`(Q) ⊆ in_J(I)`, we get `V(in_J(I)) ⊆ V(Q)`, hence

```text
projectivised normal cone nonempty over (S0,T0)  ==>  Δ(S0,T0) = 0,
```

and my blind §1.8(a) — "admissible recentering targets lie on the quartic" —
consumes exactly this direction, as an **upper bound** on the admissible
locus. It is unaffected. What is lost is the claim that every point of `Δ=0`
is admissible; the true locus may be a proper closed subset of the quartic,
possibly only the node and the two cusps. Blind §1.5's identifications
(items 1–3) are statements about `Q` and are untouched. Blind §1.8(b) is
untouched. Blind §1.8(c) is refuted for an unrelated reason (§4.2).

**3.3.4 A defect-immune replacement, and one CAS-free upgrade.** The
Lemma of §3.5 uses **only** the initial forms of the seven chosen generators,
so it is immune to the standard-basis question entirely. Separately, my blind
claim "`Δ` is irreducible over `Q`" rested on a `factorize` call; it is now
CAS-free: inverting the blind parametrisation gives

```text
λ = 12T(3S+4)/(36T² − S),
```

verified exactly at six sample values, so `λ ↦ (S(λ),T(λ))` is birational
onto its image; since `deg_λ S = 4`, that image has degree 4 `= deg Δ` and is
irreducible, hence `Δ` is irreducible. (Consistency check: numerator and
denominator of the inverse vanish simultaneously exactly at `3S+4=0`,
`27T²+1=0` — the two cusps.)

### 3.4 Auditing the elimination `iff` (packet 1.4)

- *Saturation and properness.* Saturating `(Q)` by `(e_0,e_1,e_2,e_5)^∞`
  removes components in the zero section; the projection
  `P³ × A²_{(S,T)} → A²` is proper, so the image of `V_+(Q)` is closed and is
  cut out by the elimination ideal. The `iff` for the seven-quadric system is
  therefore sound as a statement about **sets**. It says nothing about scheme
  structure or multiplicity of `Δ`, and I claim nothing there.
- *Base change.* `K/Q` is flat, so saturation and elimination commute with
  it; the statement holds over every char-0 field with roots taken in `K̄`.
- *Irrelevant components.* Handled by the saturation, which is the only
  reason the answer is a curve rather than all of `A²`.
- *`h`-vector.* `(1,4,6,4,1)` is generic data over `Q(S,T)`; it is **not** a
  statement at special `(S,T)`, and in particular not at the node, where the
  degenerate locus is a 2-plane. Nobody should read the generic `h`-vector as
  a fibre invariant.
- *Singularity and parametrisation.* The node/cusp classification and the
  genus are properties of the plane quartic `Δ`, i.e. of the **tangential**
  plane, and are now CAS-free for irreducibility (§3.3.4).
- *`P_0` and the polar rank fan.* `P_0 = {e_0=4e_2, e_5=−2e_1}` lives in the
  **normal** `A⁴_e`; the fan `u²+64v²` is the `2×2`-minor ideal of the polar
  map restricted to `P_0`, so `(u,v)` are normal coordinates. The tangential
  `(S,T)` and the normal `(u,v)` share the constant 64 and are **different
  objects**. I flagged this trap in the blind report and re-flag it: the
  post-cutoff G9 fixture makes the confusion tempting, because its tangential
  leading slope is `ε·8i` *and* its normal point sits at `u = ε·8i·v`. Those
  two `ε`'s being equal is an *observed* coincidence in one frozen family, not
  a derived coupling; §4.4 gives the discriminator.

### 3.5 The cleanest joint descendant (packet 1.5)

Not the normal-cone atlas, and not `N_min`. It is this, which costs three
lines and needs neither a standard basis nor a Rees computation.

> **Lemma (leading normal form).** Let `K` have characteristic zero and let
> `d(τ) ∈ K[[τ]]^6` be centered. Put `(S,T)=(d_4,d_3)`,
> `e = (f_0,f_1,f_2,f_5)(d(τ))`, `ρ = ord_τ e` (assume `ρ<∞`), `e_ρ ≠ 0` its
> leading coefficient, and `(S_0,T_0)=(S(0),T(0)) = (0,0)` for a centered arc.
> Then for each `i`,
>
> ```text
> ord_τ r_i(d(τ)) ≥ 2ρ,      [τ^{2ρ}] r_i(d(τ)) = Q_i(e_ρ; S_0,T_0).
> ```
>
> **Corollary (normal-order dichotomy).** With `L := min_i ord_τ r_i(d(τ))`,
> either `L = 2ρ`, or `e_ρ` is a common zero of `Q_1,…,Q_7` at `(S_0,T_0)`
> — in which case `Δ(S_0,T_0)=0`. At the campaign's centre `(0,0)` the
> degenerate locus is exactly the 2-plane `P_0`, i.e. the campaign's
> four-plane `A=B=0`.

*Proof.* `r_i = Q_i(e;S,T) + C_i` with `C_i` of `e`-degree `≥3`; `ord C_i ≥
3ρ > 2ρ` since `ρ ≥ 1`; `Q_i` is `e`-homogeneous of degree 2 with coefficients
in `Q[S,T]`, so its `τ^{2ρ}` coefficient is `Q_i(e_ρ;S_0,T_0)`. ∎

Three consequences that are worth more than the atlas:

1. **It explains, uniformly in `r`, `(e,m)` and load face, why every K00 cell
   reports the same leading four-plane.** No per-cell computation is needed:
   whenever the load calendar puts `L` strictly above `2ρ`, the leading normal
   coefficient is forced into `P_0`.
2. **It gives a ceiling `ρ ≤ L/2`** with `L` read from the calendar — turning
   "which normal orders are possible" from a search into arithmetic (§4.3).
3. **It is immune to §3.3's gap**, because it consumes only the generators'
   initial forms.

**Desk verification against the frozen rows** (`prelude_Q.sing`, exact):

```text
A. centre (0,0), e_3 ∈ P_0, random otherwise (4 trials):  min ord = 7  ( > 6 )
B. centre (0,0), e_3 random ∉ P_0        (4 trials):      min ord = 6  ( = 2ρ )
C. recentred at 5 points with Δ ≠ 0, e_3 arbitrary:       min ord = 6  ( = 2ρ )
   (S0,T0) ∈ {(1,0),(2,1),(3,−2),(−1,1),(5,3)}, Δ = 2, −212, −5756, −440, −31026
```

B and C are the sharpness and the `Δ`-gate contrapositive respectively, and
both are exactly as predicted. Ranking of the packet's four candidates:
**(1) normal-order dichotomy + a load-order table** (desk, immediate);
(2) filtered standard basis (the only thing that would upgrade V3 to an iff —
AWS, preregister); (3) `N_min` (only matters where the `J^17` half is
non-vacuous, i.e. `L>17`); (4) normal-cone atlas (premature without (2)).

---

## 4. Mandatory attack 2 — the ramified frontier after the cutoff

### 4.1 Verifying the G9 theorem from a second artifact

I rebuilt the packet's rank-one family in split coordinates and evaluated the
**frozen unloaded rows of `prelude_Q.sing`** — a different frozen artifact
from the 569-tail compiler the producer used — along it. Results, exact:

```text
banked fixture (ε=+1,t=q=1,β=0,α=−4,X=24i,y=0,z=(−1088i,0,0,0,0,0)):
  ord_τ r_1..r_7  =  9,9,9,9,9,9,9
  [τ^9] r_6 = i/32                       (packet (4.1) at ε=+1,q=1: i/32)

8 random members of the G8-compatible family, both signs, random
β, y_1..y_4, free z, and random u, r, h at τ^6, τ^7, τ^8:
  min ord = 9 in every case;  [τ^9] r_6 = ε·i·q³/32 in every case,
  independent of t, β, y, z, u, r, h.

producer mutation control: α = −3t² instead of −4t²  ->  min ord drops 9 → 8.
```

This is an **independent cross-artifact confirmation of the provisional G9
kill's central coefficient and of two of its four control classes.** It is not
a hostile review of that packet (I did not reconstruct its G8 factorisation
from the tails, and I am not its assigned reviewer), and it does not promote
it. It does raise my confidence in `G9_6 = ε·i·q³/32` substantially.

It also measures the number the sandwich needs: **`L = 9` exactly** on this
family, since the unloaded rows vanish to order exactly 9 and the source is
`R(d) + τ⁶k10(τ)A10(d) = 0`. Two facts follow at once and were not previously
recorded: `ord_τ A10(d(τ)) = 3` on this family (otherwise the six non-row-6
G9 equations would be unsolvable), confirming the "K10 cubic" reading; and
`ρ = 3` with `2ρ = 6 < 9 = L`, so the Lemma's hypothesis holds **strictly**.

The Lemma's prediction is then confirmed on real data: the fixture's leading
normal coefficient is

```text
e_3 = (32i, −1, 8i, 2),   e_0 − 4e_2 = 0,   e_5 + 2e_1 = 0,
(u,v) = (8i, 1),          u² + 64v² = 0,
A(w) = w_5+16w_1−4w_3 = 0,  B(w) = w_0−4w_2+2w_4 = 0.
```

So `e_3 ∈ P_0` exactly, and it sits on the rank fan — which is precisely why
the producer calls this stratum "stable rank one".

### 4.2 Does `Δ` contact have explanatory content after the row-six unit?

**Both, and the split is sharp.**

*The part that is not evidence.* Write the packet's parametrisation
`S = ε8i·t·τ + ατ²`, `T = t·τ + βτ²`. Then
`S − ε8i·T = (α − ε8iβ)τ²`, and the G8 compatibility relation (0.1) is
`α − ε8iβ = −4t²`, i.e.

```text
S = ε·8i·T − 4T² + O(τ³)  is *identically* the G8 compatibility relation,
```

while the leading slope `S/T → ε8i` is the nodal tangent cone `S²+64T²`.
Therefore the agreement of the fixture with my blind branch expansion at
orders 1 and 2 is **not** independent evidence for anything: it is the
campaign's own G8 equation restated. Any reading of the round that treats it
as convergence is wrong, and I am the person most likely to have made that
error.

*The part that is refuted.* My blind §1.8(c) predicted the `T³` coefficient
`±4i`. The fixture's is `0`. Substituting the fixture gives, exactly,

```text
Δ(S,T) = 64τ⁴(1 + 6iτ − τ²),      ord_τ Δ = 4,
```

matching the packet's test datum. So `ord Δ = 4` **records a failed order-3
tangency**: contact with one nodal branch of order exactly 3, transversality
to the other. `§1.8(c)` is `REFUTED`; blind §1.8(a) and (b) are untouched.
This is my blind Card A's third named outcome ("contact strictly between"),
delivered without launching the card.

*A representative hazard I must report.* The "tangential trajectory" of an arc
is only defined once a splitting is chosen, and the two natural choices — the
packet's surface parameters `(S,T)` and the split coordinates `(d_4,d_3)` —
differ at order `τ^ρ = τ³`, which changes `Δ` at order `τ^{ρ+1} = τ⁴`, exactly
where the answer lives. Computed in both:

```text
(S,T) representative:      Δ = 64τ⁴ + 384i τ⁵ − 64τ⁶            ord 4
(d_4,d_3) representative:  Δ = 320τ⁴ + 2560i τ⁵ − …             ord 4
```

The leading coefficient is representative-dependent (64 vs 320); only its
**nonvanishing**, and the statement `ord Δ ≥ ρ+1`, are invariant. Any future
card must report `ord Δ` with its representative named. Nothing in the packet
or in my blind report said this.

*The part that survives as content.* `e_ρ ∈ P_0` and `e_ρ` on the rank fan
are not accidents and are not restatements of G8 — they are the Lemma's
conclusion, and they hold for **every** cell with `L > 2ρ`, uniformly in
`r`, `(e,m)` and load face. That is the explanatory content, and it survives
the row-six unit intact.

### 4.3 The exact unexamined `e=3,m=1` strata

On the declared K10 unit open, with `L = 9` measured (§4.1) and
`ρ ≤ L/2 = 4.5`:

| Stratum | Status |
|---|---|
| `ρ ≤ 2` | Must be **cited** from the cell prefix (the all-faces producer starts its normal part at `τ³`). I do not assume it; if the citation is absent this is an open stratum, not a closed one. |
| `ρ = 3`, `e_3 ∈ P_0` **on** the fan (`u=±8iv`) | Killed at G9 by the provisional packet, both signs, on `D(q)`. |
| `ρ = 3`, `e_3 ∈ P_0` **off** the fan | **OPEN.** This is the only remaining `ρ=3` case; `e_3 ∈ P_0` is forced by the Lemma, so it is a 2-parameter family modulo scale, i.e. a `P¹` minus two points. |
| `ρ = 4` (any direction in `P_0∖0`) | **OPEN.** Forced into `P_0` because `L=9 > 8`. |
| `ρ = 5` or more | **EXCLUDED** by `2ρ ≤ L = 9`. |
| `ρ = ∞` (arc on the graph) | **OPEN and separately typed**: then `R(d) ≡ 0` and the source degenerates to `k10·A10(d) ≡ 0`; neither the sandwich nor the Lemma applies. |

This replaces "classify the other `e=3,m=1` rank strata", which reads
open-ended, with a four-line finite list and an a priori ceiling on `ρ`. A
full `G0–G9` fan is already running provisionally and I do not duplicate it;
what I add is the list it must be checked against for completeness.

### 4.4 The `ε`-coupling discriminator

The fixture has the *same* `ε` in its tangential slope `S/T → ε8i` and in its
normal point `u = ε8iv`. Either the packet's ansatz derived that coupling from
an earlier grade, or it assumed it. The cheapest discriminator is one run of
the same replay with the two signs **decoupled** (tangential `+`, normal `−`):
if the low grades still solve, the coupling is an ansatz restriction and a
whole mirror family is unexamined; if they fail, the coupling is derived and
the census of §4.3 is complete as written. Seconds of compute; it must be
answered before anyone calls the `e=3,m=1` rank-one analysis exhaustive.

### 4.5 Tougeron / algebraization: stop, with a stated reactivation condition

Stop all Tougeron and algebraization work on the `e=3,m=1` stable rank-one
branch: it is empty at G9, so there is no jet to extend and the `2e+1`
stopping-grade question is moot there. The blind card that proposed it was
written before the kill and is not in error; it is superseded by events.

**Reactivate only when all four hold simultaneously:** (i) a *constructible*
transition survivor — a nonempty image, not a nonempty fibre; (ii) a typed
finite system with a declared unknown list and a frozen source hash; (iii) a
verified rank `r` and minor order `e_r` over the localised ring, with the
pivot certificate; (iv) a certified syzygy for every residual row, so that
Tougeron applies to a minimal subsystem rather than to an overdetermined one.
Absent (iv) the correct output is the obstruction series, which is what the
row-six units already are. Building the `tougeron_check` tool before a
survivor exists is building a decision procedure for an empty input.

### 4.6 Reranking the ramification calendars and the source arrow

1. **Normal-order dichotomy + load-order table** (§3.5, §7 L1). Converts the
   per-`(e,m)` geometry into arithmetic. Cheapest, highest leverage.
2. **`e=3,m=1` residual census** (§4.3, §7 L2), including the `ε`-decoupling
   check and the `ρ=∞` stratum.
3. **General `(e,m,h)` calendars.** Only after 1; the Lemma predicts the
   geometry is `(e,m)`-independent and that only `L` varies, which is exactly
   the claim that makes the calendar a table instead of a family of solves.
4. **Source completeness / other supports / `C6=0`.** Still the binding
   constraint on meaning; still with no owner.
5. **Reachability.** Unchanged as the dominant gap. **Closing an atlas
   without an actual-map-to-source arrow is not JC2, and nothing in this
   round moves that arrow one step.** I say this plainly because this round
   produced an unusual amount of confirmatory K00 arithmetic and that is
   exactly when the arrow gets forgotten.
6. **All-order lifting**, 7. **algebraization**: both premature; see §4.5.

---

## 5. Mandatory attack 3 — proof side: QCS and selector

### 5.1 Monomial-chart divisibility: verified, then reduced to two lines

*Identity.* With `f=Σa_k(t)s^k`, `g=Σb_k(t)s^k`,
`[s^{u-2}](f_sg_t − f_tg_s) = Σ_{k+l=u-1}(k a_k b_l' − l a_k' b_l)`, since
`f_sg_t` contributes at `k−1+l=u−2` and `f_tg_s` at `k+l−1=u−2`. **Correct.**

*Support.* `x^Ay^B ↦ t^A s^{uA−B}`; for `1 ≤ k ≤ u−1`, `uA−B=k` with `A=0`
forces `B=−k<0`. So `A ≥ 1` and `t | a_k, b_k` there; every surviving summand
has `i≥1` or `j≥1`. **Correct.** Hence the coefficient lies in `(t)` and
cannot equal `1`. **The theorem is CONFIRMED.**

*Maximum scope, hostilely.* The hypothesis "no negative `s`-powers for both
`F` and `G`" says exactly `supp(F), supp(G) ⊆ {(A,B) : B ≤ uA}`. Setting
`A=0` forces `B=0`, so `F(0,y)` and `G(0,y)` are constants, i.e.
`F = c + xP`, `G = c' + xQ`. Then

```text
Jac(F,G) = (P+xP_x)(xQ_y) − (xP_y)(Q+xQ_x) ∈ (x),
```

so it is not a nonzero constant. **Two lines, no chart, no `u`, no
coefficient formula.** The elaborate identity is therefore not where the
content is; the content is entirely in how strong the regularity hypothesis
is. Billing should be `NEW EXACT GENERALIZATION, ELEMENTARY AT ITS OWN
HYPOTHESIS`, and the design lesson — that this chart is empty of Keller pairs
and so can carry no information about `STRICT-COLLIDE-POLY` — is the real
output. That lesson is *strengthened*, not weakened, by the simplification.

*Do translated or iterated charts evade it?* **`t`-translation does not.**
Replacing `x = t s^u` by `x = (t+c)s^u` leaves every `s`-exponent unchanged,
so the hypothesis is translation-invariant and the conclusion becomes
`(t+c) | coefficient`, still incompatible with `1`. The genuine evasions are
(i) allowing a boundary pole in `f` or `g` — which is what an actual
counterexample will do at a pole vertex, (ii) ramifying `s ↦ σ^e` or passing
to an iterated/Puiseux chart, where the support semigroup (2.1) is replaced
and the exponent bookkeeping must be redone from scratch. I checked (ii)
enough to see that the naive transfer fails and that no claim should be made
without redoing it.

*Positive residue.* The two-line form is an **actual-map** statement: for
every Keller pair and every `u ≥ 2`, `F` and `G` cannot both be regular in
the literal chart, i.e. at least one has a boundary pole there. The campaign
has very few actual-map statements; this one should be filed as such rather
than only as a refutation of a client.

### 5.2 Three QCS mechanisms compared

**5.2.1 Pair-square off-diagonal module.** Two objections before any
compactification work, both cheaper than the invariance check the card
proposes.

*(a) It cannot see `J=1`.* `Z=(X×_U X)∖Δ` with `X=F^{-1}(U) → U` finite étale
of degree `d` is determined by the monodromy representation and by `U`; it is
degree `d(d−1)` étale over `U`. Nothing in its construction distinguishes a
Keller cover from any other finite étale cover of the same `U` with the same
group. Therefore no invariant of `Z` alone can prove QCS, and the Jacobian
hypothesis must enter through the boundary of the chosen compactification.
The card must say where, in advance.

*(b) Its target is a numerical inequality that can be tested today.* From the
promoted margin `Ξ = E_gen − (s−1) = d − s − Σ_i b_i`,

```text
E_gen ≥ s−1    ⟺    Ξ ≥ 0    ⟺    d ≥ s + Σ_i b_i.
```

So the entire pair-square programme targets one inequality among already
promoted entry data. **Before constructing any chain complex, evaluate
`d − s − Σ b_i` on the campaign's own families** — in particular on `U1*(R)`
(type `(2,3)`, `R` poles, `td = 4R`). If, on the intended reading of `b_i`,
that family gives `Ξ = 0` identically, then QCS is *sharp* on a known
infinite family, every proof of it must be sharp, and any argument producing a
strict inequality is thereby refuted. If it gives `Ξ < 0` anywhere on a
source-compatible member, QCS as stated is false. This is hours of arithmetic
with no topology, and it discriminates the card's whole premise. I flag that I
have not confirmed the definition of `b_i` from source and that the reading
must be pinned before the number is believed.

**5.2.2 ACV separation `#atypical ≥ s−1`: falsified as stated, at desk cost.**
The card correctly demands a control battery first. I ran the battery by hand
and it terminates immediately. Take

```text
f = x + x²y + x³y²  =  x(1 + w + w²),      w := xy.
```

- `∇f = (1+2w+3w², x²(1+2w))`. If `x=0` then `w=0` and the first entry is `1`;
  if `1+2w=0` then `w=−1/2` and the first entry is `3/4`. **`f` has no
  critical points**, so it is compatible with being a component of a Keller
  pair on exactly the count that matters (`J=1 ⟹ ∇f ≠ 0`).
- For `c ≠ 0` the fibre is parametrised bijectively by
  `w ∈ C ∖ {ω, ω̄}` (the roots of `1+w+w²`), via `x = c/(1+w+w²)`,
  `y = w(1+w+w²)/c`. So the generic fibre is `C` minus 2 points, connected —
  `f` is **primitive** — with `s = 3` places at infinity.
- `(x,y) ↦ (λx, y/λ)` fixes `w` and sends `f ↦ λf`, so all fibres over `C*`
  are isomorphic and the family is locally trivial there.
- `F_0 = {x=0} ⊔ {xy=ω} ⊔ {xy=ω̄}` has `χ = 1`, versus generic `χ = −1`. So
  `#atypical = 1`.

Hence `#atypical = 1 < 2 = s−1`. Under the natural reading of `s` (places at
infinity of the generic fibre), **`#atypical ≥ s−1` is false for primitive,
critical-point-free polynomials.** Consequences: Fable's stage A is answered
before it is run; the battery should be *narrowed* to the class where the
statement could still hold (both members of an actual pair, `J=1`), because
the critical-point-free class alone is already too big; and any ACV proof must
consume the partner `g`, not only `f`. If `s` in the campaign means something
other than places at infinity, this counterexample must be re-typed rather
than discarded — I declare the reading rather than infer it.

**5.2.3 Galois/function-field obstruction (my blind Card C): LOWERED by me.**
The packet's objection is correct and I accept it: the base field is already
algebraically closed, so a descent argument has no field to descend along
unless it is typed over a genuinely non-closed field. The only version I can
type is: work over the function field `C(c)` of the *value* line, where the
quotient-line data at a moving atypical value `c` is defined over a finite
extension of `C(c)`, and ask whether zero excess forces two colliding lines
into a nontrivial quadratic extension of the field generated by the profile
data over `C(c)`. Conjugacy would then be forced by the Galois action on the
`c`-family, not read off one square-root model — which was the defect the
packet names. **I do not launch this.** It is strictly weaker than §5.2.1's
numerical test and than §5.3, and it must not be given a proof slot ahead of
them.

### 5.3 The intermediate block surface, attacked and sharpened

Fix a counterexample `F=(f,g)` of minimal topological degree `d`, an
intermediate field `C(f,g) ⊆ K ⊆ C(x,y)` from a nontrivial monodromy block,
`B_K` the integral closure of `C[f,g]` in `K`, `Y_K = Spec B_K`,
`g_1 : A² → Y_K`, `g_2 : Y_K → A²` with `F = g_2∘g_1`.

- **`B_K ⊆ C[x,y]`: CONFIRMED.** Elements of `B_K` are integral over
  `C[f,g] ⊆ C[x,y]`, lie in `K ⊆ Frac(C[x,y])`, and `C[x,y]` is normal.
  Properness of `F` is *not* used. Sol-alt's one-line justification is
  correct.
- **Finiteness of `B_K` over `C[f,g]`: CONFIRMED.** `C[f,g]` is a finitely
  generated domain over a field of characteristic zero and `K/C(f,g)` is
  finite, so the integral closure is a finite module (Noether). So `g_2` is
  **finite** and `Y_K` is a normal affine surface.
- **`g_1 : A² → Y_K` finite: NOT AVAILABLE.** It would require `x,y` integral
  over `C[f,g]`, i.e. exactly the properness that fails. This is the honest
  gap and the card must not paper over it.
- **The `A²` target is the wrong one.** `(x,y) ↦ (x²,y²)` factors through the
  quadric cone `Spec C[x², xy, y²]`, which is normal, finite over
  `Spec C[x²,y²] = A²`, dominated by `A²`, and **not** `A²`. So "every
  intermediate normal surface is `A²`" is false without Keller and is
  therefore at least as hard as the Keller input it must consume.
- **A strictly weaker sufficient hypothesis.** `J(F)=1` makes `F` étale, so
  `d(g_2)∘d(g_1)` is invertible; hence `dg_1` is injective, and at every
  **smooth** point of `Y_K` in the image of `g_1` the tangent map `dg_2` is an
  isomorphism, i.e. `g_2` is étale there. `Y_K` is a normal surface, so
  `Sing(Y_K)` is **finite**. Therefore `g_2` is étale away from
  `Sing(Y_K) ∪ (Y_K ∖ g_1(A²))`. By Zariski–Nagata purity (target `A²`
  regular, source normal), the branch locus of `g_2` is pure of codimension 1
  or empty. So:

  > **If `g_1(A²)` contains every codimension-1 point of `Y_K`, then `g_2` is
  > finite étale over `A²`, hence an isomorphism (`π_1^{ét}(A²_C)=1`), hence
  > the block is trivial.**

  This needs **no `A²`-recognition theorem at all**. The single missing
  hypothesis is that `g_1` does not miss a curve in `Y_K` — which is precisely
  an Avenue-7 nonproperness statement about `A(F)`, and is *weaker* than
  properness of `F`. Whether it is weaker than JC2 itself is the open
  question, and it should be attacked directly rather than through surface
  classification.

  Two guards: the argument uses only `Y_K` normal (so `Sing` is finite) and
  `A²` regular; it does **not** assume `Y_K` smooth, and it does not assume
  `g_1` surjective, only codim-1 dominance. It is invalid the moment anyone
  substitutes "finite" for "dominant" on `g_1`.

- **The Jacobian factor argument if `Y_K ≅ A²`: CONFIRMED but now
  secondary.** Then `F = g_2∘g_1` with both factors polynomial maps,
  `Jac(g_2)(g_1)·Jac(g_1) = 1` forces both to be units, and degrees multiply,
  contradicting minimality. Correct — but reaching `Y_K ≅ A²` is the hard
  part, and the codim-1 criterion bypasses it entirely.

### 5.4 One launch, one falsifier, one bypass; and the preserved gap

- **Proof launch:** §5.3's codim-1 image criterion (`L4`). It consumes `J=1`
  essentially, it is desk-scale, and both outcomes are informative.
- **Falsifier:** §5.2.2's control class, narrowed to pairs, plus §5.2.1's
  numerical margin evaluation (`L3`). Either can kill a QCS half in hours.
- **Bypass:** the pole-incidence boundary complex with a suspension onto
  `H_1(F)`, gated on one common labelled surface/boundary packet. Unchanged,
  unfunded, and explicitly *not* the pair-square as currently specified.
- **Preserved gap, stated so it is not absorbed:** there is still **no**
  reviewed arrow from an arbitrary minimal Keller counterexample to a bounded
  `td`/type/entry/U1 client, no all-`td` coverage theorem, no actual-map
  source packet for the conditional td12 laboratory, and no owner for source
  completeness. Nothing in this round touches any of these. A `PASS` on `L4`
  would give primitivity of minimal-`td` monodromy — which constrains the
  selector but does **not** supply it.

---

## 6. Mandatory attack 4 — mathematical and campaign software

### 6.1 The merged transition compiler `K00-TC/v1`

One tool, three front ends retired. Smallest reusable core:

- **Representation.** Split coordinates `(e_0,e_1,e_2,e_5; S,T)` as the
  internal normal form (my `K00-SPLIT-COORDINATE-PREPASS`), justified because
  the change of variables is a triangular polynomial automorphism, so
  emptiness verdicts are invariant by construction. Its payoff is now
  concrete rather than cosmetic: by §3.5 the leading stage becomes evaluation
  of seven fixed quadratic forms and a `7×4` polar matrix, not a Gröbner
  rediscovery of `I ⊆ J²` at every cell.
- **Certificate vocabulary.** Sol-alt's, verbatim and unextended:
  `EMPTY_TRANSITION`, `PROPER_NONEMPTY_FINITE_JET_IMAGE`,
  `DOMINANT_FINITE_JET_TRANSITION`, `UNKNOWN`. **No `ARC` token exists in the
  vocabulary.** This is the single most valuable line in the three proposals.
- **Memoisation keys.** Sol's `(e, m, load calendar)`, extended by the two
  numbers the Lemma makes decisive: `ρ` (normal order) and
  `L = min_i ord_τ(target−load)_i`, with the resonance flag `L = 2ρ`.
- **Mandatory controls per run.** Old-pass fixture; one planted coefficient
  mutation; the open-locus control (`q=0` must change the verdict); custody
  fail-closed on every input hash.

**Acceptance, before any new mathematics is trusted, exactly as the packet
requires:** (i) reproduce the promoted `e=2,m=1` G7 emptiness on the declared
opens; (ii) reproduce `G9_6 = ε·i·q³/32` on both signs. I have already shown
(ii) is reachable from the frozen prelude in seconds of stdlib arithmetic
(§4.1), so this acceptance test is cheap and non-negotiable. If either
verdict differs, the compiler is wrong and is discarded, not tuned.

### 6.2 Exactly one campaign-systems trial

**Selected: `SECTIONED-INDEPENDENT-CALLS/v1`** (Fable's card, corrected).

Comparison, with my own blind card judged first:

- *My `ADAPTER-PREFLIGHT` checkpoint clause is **refuted**.* I proposed that
  each lane "checkpoint at 80% of its declared budget". A runner cannot force
  a model to checkpoint inside one monolithic provider response; the packet
  says so and it is correct. That clause is withdrawn.
- *Provider preflight: `NO_CHANGE`.* It cannot restore an exhausted balance,
  and the 402 lane was already typed correctly and cost no verdict. Fable's
  evidence for this is right and my blind card overvalued it.
- *One-shot cap retry:* pays full cost again with no guarantee, and cannot
  produce partial value from the first attempt.
- *Claim-contract lint:* useful, but it addresses ingestion hygiene, not the
  observed 76-minute total loss. Deferred, not rejected.
- *Sectioned independent calls:* the only option that converts a ceiling into
  partial value, and it does so **without** any intra-response mechanism —
  each section is its own call with its own immutable artifact, and a final
  assembly step seals the body.

**Offline stub acceptance test** (synthetic fixtures only; no live provider;
`jc2-lean` untouched): a three-section task run against a stub that fails
inside section 3. Assert (1) sections 1 and 2 exist on disk with correct byte
counts and parse; (2) a `TRUNCATED_AFTER_SECTION_2` receipt names the failure
point; (3) an uncapped rerun yields a byte-identical prefix for sections 1–2
and a sealed full body; (4) a mutated section hash fails closed; (5) total
suite under 10 s. Five mechanical assertions.

**Rollback:** the sectioned path is opt-in per lane; reverting is deleting one
flag, and no mathematical artifact depends on it. **Measured success
criterion:** over the next three long-form lanes, recovered-report rate
(currently 0 of 1) and duplicated token cost; abandon if duplicated cost
exceeds 20% with no recovery event. **Non-blocking:** no mathematics waits on
it, and the licensed `QCS-GLUE-OR-KILL` retry may proceed under a plain hard
output bound in the meantime.

---

## 7. Launch portfolio (four, spanning proof, falsification, K00, source)

**L1 — `K00-NORMAL-ORDER-DICHOTOMY/v1` (K00, desk).**
*Content:* prove the Lemma and Corollary of §3.5 in the frozen coordinates;
emit the load-order table `ord_τ A10|, A6|, A2|` at the base centre for each
`(e,m)` in the calendar; tabulate `L` and the ceiling `ρ ≤ L/2` per cell.
*Dependencies:* the frozen prelude and the load compiler; **not** the radical
certificates, **not** the standard-basis question, **not** any review outcome.
*Owner/reviewer:* producer Fable or Sol; hostile review by a different model
(not me — I am the source of the Lemma). *Placement:* desk, seconds; no AWS.
*Outcomes:* a complete table collapses the per-cell geometry to arithmetic;
a cell where `L = 2ρ` is a **resonance** and must be computed the old way —
that is a real negative and it localises exactly where. *Stop:* stop at the
first cell whose load order cannot be read exactly; return typed `OPEN`.

**L2 — `K00-E3M1-RESIDUAL-CENSUS/v1` (falsification, desk → preregister AWS).**
*Content:* the four-line census of §4.3, plus the `ε`-decoupling discriminator
of §4.4, plus explicit typing of the `ρ=∞` stratum.
*Dependencies:* L1's ceiling; the provisional G9 packet **provisionally** (it
is producer-unreviewed and this card fails closed if its review fails); the
cell prefix citation for `ρ ≤ 2`. *Owner/reviewer:* producer any non-Sol lane;
hostile review different model. *Placement:* desk for the census and the sign
check; preregister AWS only if the `ρ=4` solve swells. *Outcomes:* all strata
empty ⇒ the `e=3,m=1` cell closes on its declared opens (a finite-jet
statement, nothing more); any survivor ⇒ the first ramified stratum that is
not rank-one, and the census tells you which. *Stop:* do not extrapolate in
`e`; do not call any survivor an arc.

**L3 — `QCS-MARGIN-AND-COUNT-FALSIFIER/v1` (falsification/proof, desk).**
*Content:* (a) pin the definition of `b_i` from source, then evaluate
`Ξ = d − s − Σb_i` on `U1*(R)` and every reviewed control (§5.2.1); (b) run
the narrowed ACV battery on *pairs*, using §5.2.2 as the standing negative
control for the unpaired class. *Dependencies:* promoted Section-7 identities
only. *Owner/reviewer:* falsifier owned by a different model than any prover,
per Fable's correct rule. *Placement:* desk. *Outcomes:* `Ξ = 0` on an
infinite family ⇒ QCS is sharp and no strict-inequality proof can work;
`Ξ < 0` on a source-compatible member ⇒ QCS false as stated; `#atypical ≥ s−1`
failing on a *pair* ⇒ P2b dead and QCS must be re-decomposed. *Stop:* stop at
the first refutation; do not start a chain-complex construction from this card.

**L4 — `BLOCK-DESCENT-CODIM1/v1` (proof + source completeness, desk).**
*Content:* §5.3. Prove the codim-1 criterion cleanly; then attack the single
missing hypothesis (does `g_1` miss a curve in `Y_K`?) directly against
`A(F)`. Secondary deliverable: file §5.1's two-line actual-map statement as a
source-completeness fact. *Dependencies:* none unreviewed. *Owner/reviewer:*
prover and falsifier in different lanes; the falsifier looks for a normal
affine `Y_K`, finite over `A²`, dominated by `A²` with a missed curve.
*Placement:* desk commutative algebra. *Outcomes:* criterion + hypothesis ⇒
minimal-`td` monodromy is primitive, giving Avenue 26 a real client and
constraining (not supplying) the selector; a countermodel ⇒ the block-descent
selector dies cleanly and Avenue 30/31 inherits an explicit boundary object.
*Stop:* stop if any step assumes `F` proper, `g_1` finite, or `Y_K` smooth.

**Dependencies among launches:** L2 consumes L1's ceiling; L1, L3, L4 are
mutually independent and may start in parallel. None waits on the R4-00
review, which continues in the background and is unaffected by this report.

---

## 8. Stop / defer list

- **Stop:** Tougeron and algebraization on the `e=3,m=1` stable rank-one
  branch (§4.5); the Avenue-33 period instrument (self-refuted, recorded);
  the degree-six PALF / `A2`-filling comparison (category empty for a
  submersion); nonlinear rational-termination on the literal nodal chart
  (§5.1); my blind checkpoint-at-80% clause (§6.2); my blind §1.8(c)
  branch-contact prediction (§4.2).
- **Defer:** filtered standard basis for `in_J(I)` (the only route to
  upgrading V3 to an iff — preregister AWS, do not launch blind);
  `N_min` sharpening (only matters where `L > 17`); the normal-cone atlas;
  claim-contract lint; the pair-square chain complex until §5.2.1's number is
  in hand; Galois descent (§5.2.3), which I lower myself.
- **Continue unchanged:** R4-00 R1/R2 hostile review; the provisional
  `G0–G9` `e=3` fan; a named-but-unfunded owner on reachability; one owner at
  specification intensity on source completeness.

---

## 9. Desk receipt summary

```text
prelude_Q.sing        5b0a77e6…  (matches blind §1.1 and producer §2)
Δ on packet series    Δ = 64τ⁴(1+6iτ−τ²), ord 4                    [matches packet]
Δ, split repr.        ord 4, leading 320 (vs 64) — repr.-dependent  [new hazard]
fixture normal order  ρ = 3;  e_3 = (32i,−1,8i,2) ∈ P_0;  u²+64v² = 0
frozen rows on fixture ord = 9 for all seven;  [τ⁹]r_6 = i/32
family, 8 random pts  min ord 9;  [τ⁹]r_6 = ε·i·q³/32 in every case
mutation α:−4 → −3    min ord 9 → 8                        [producer control 2]
Lemma test A/B/C      ord 7 / 6 / 6  as predicted (13 trials)
Δ parametrisation     Δ(S(λ),T(λ)) ≡ 0;  λ = 12T(3S+4)/(36T²−S)  ⇒ irreducible
```

All runs: Python 3.9 stdlib, exact, < 4 s each, `/tmp/xp` only.

---

## 10. Synthesis recommendation (under 300 words)

The round's real content is smaller and better than it looks. Three of the
five headline items shrink under attack: my quartic is a theorem about the
seven-quadric **leading system**, not the normal cone, until someone produces
a filtered standard basis; the `J^17` half of the valuation sandwich is
strictly vacuous in the only live ramified cell, where I measured `L = 9`; and
the monomial-chart obstruction reduces, at its own hypothesis, to
`F,G ∈ K+(x) ⇒ Jac ∈ (x)`. My own blind branch-contact prediction is refuted:
the fixture's agreement with the quartic at orders 1–2 is *identically* the
G8 compatibility relation, and the order-3 coefficient is wrong.

What grew is one three-line lemma. `I ⊆ J²` plus the seven initial forms give
a dichotomy — either `L = 2ρ`, or the leading normal coefficient lies in the
degenerate cone, which at the base point is exactly the campaign's four-plane
`A=B=0`. It is immune to the standard-basis gap, it explains uniformly why
every cell reports the same plane, it caps the normal order at `L/2`, and it
turns "classify the remaining `e=3,m=1` strata" into a four-line finite list.
It checks out against the frozen rows in thirteen trials, and a second
artifact independently reproduces `G9_6 = ε·i·q³/32`.

Fund L1 and L2 on the K00 side, L3 and L4 on the proof side; L3 and L4 are
hours of arithmetic that can each kill a programme. Take one systems trial —
sectioned independent calls — and nothing else. And keep saying the
uncomfortable thing: every K00 result this round, including mine, is a
statement about a normalized finite source datum, and no arrow yet sends an
actual polynomial Keller map to one.

## 11. Nonclaims

This report proves and disproves nothing about JC2. It closes no cell, no
`(e,m)`, no load face, no support, and no atlas; it promotes nothing and is
not a hostile review of any packet. §4.1 is an independent desk reproduction
of two coefficients and one control of a `PRODUCER_UNREVIEWED` result, not its
review and not its promotion. §3.3 withdraws a claim of mine and replaces it
with a strictly weaker one; no downstream use is repaired by analogy. §5.2.2's
counterexample is stated under a declared reading of `s` and must be re-typed,
not discarded, if that reading is wrong. §5.3's criterion has one explicitly
unproved hypothesis and is not a proof of primitivity. A finite jet is not a
formal arc, an algebraic germ, an attained source point, a polynomial map, a
counterexample, or JC2; a floor is not attainment; equality of sets is not
equality of schemes; `Δ` is a locus on the tangential plane and is not the
normal rank fan `u²+64v²`. No exit price is derived or asserted. No
formalization evidence was inspected or consumed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `53234`.
- Body SHA-256:
  `647bca6600e31816c1f7ac14f2b061d7be574cf653d7102ac063375627d0346b`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
