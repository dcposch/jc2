# Hostile review: N5-S2 kill chain (Sol)

Different-model gate. Charged: `xmodel/n5-s2-kill-chain-sol56-20260901.md`
against the reviewed N5 report, the N5 hostile review, and the A1
rowkill/coordinator integration note. Desk-scale exact reasoning.
No CAS. Frozen-input hashes verified before any reading.

## 0. Charge, hashes, and scope

Different-model gate of `xmodel/n5-s2-kill-chain-sol56-20260901.md` (Sol).
The four frozen inputs matched the mandated SHA-256 values before any
source was opened:

```text
363cdd1ce1253b0a7429b231e2151477e3eaaad794710b98b73a9f530537f6d5  n5-s2-kill-chain-sol56-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6  b0-reducible-n5-hostile-review-sol56-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Cite `B0:n`, `REV:n`, `RK:n`, `SOL:n` for those four files. A fact is
*reviewed* only if REV promotes or repairs it; a B0 assertion that REV
withheld is not restored. No CAS. No charged file, canonical ledger, or
`jc2-lean` was edited or inspected.

Sol's own §0 hashes a different third file, the 2026-08-31 N-A rowsweep
coordinator (`126c2d29…`), and cites it as `CNA`. That file is not among
the four charged inputs. Line citations `CNA:44-49` (N-A-RES), `CNA:40`
(bar on unqualified δ-constant π₁-transport), `CNA:76-77` (triangular
reductions), and `CNA:80-83` ((8,4)~(6,4)) are therefore checked against
REV and RK, which carry the same mathematical payload, and are not treated
as an independent promotion. RK already records N5-S2 as
`PROVISIONAL — review pending` (`RK:29,77-82`). This gate is that review.

Desk re-derivation below uses only finite group theory, the Artin action
as Sol states it, and the reviewed N-A-RES scalar gate. Three primary
PDFs were streamed (30s timeout, hashed, not saved) and agree with Sol:

```text
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
Nguyen Van Chau, arXiv:math/0305088v1, Thm 1 / Cor 2.
https://arxiv.org/pdf/math/0305088

0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875
Rick Miranda, Triple Covers in Algebraic Geometry, AJM 107 (1985).
https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf

628cc47f5c183f491620f5ab65f7a34582d70e12274c8e55f0d6b8d66148ef05
Landesman–Vakil–Wood, Compos. Math. 160 (2024), §3 / Thm 3.16.
https://par.nsf.gov/servlets/purl/10612589
```

No new exit-price assertion is made.

**Headline.** Items (1)–(5) all hold. THEOREM[S5-COPRIME-KILL] and the
(6,4) affine-normal-form kill are independently re-derived. S2 remains
OPEN at the narrowed noncoprime cage. Promote the two kills and the
typed OPENs; do not promote a degree pin or a full S2 decision.

## 1. S2 survivor data extraction vs. reviewed N5 report

**Verdict: CONFIRMED.** Sol extracts the reviewed S2 cage and does not
silently restore what REV withheld.

Reviewed ownership (`B0:233-244,506-515`; `REV:38-56,68-78`):

| row | dicritical ownership | `(W,a)` |
|---|---|---|
| P3a | `(2,0,1)` over `D`; one `(1,0,1)` on each of two others | `(2,3),(1,4),(1,4)`, `m=3` |
| P3b | `(2,0,1)` over `D`; both trivials on one other | `(2,3),(2,3)`, `m=2` |

Lemma B is a floor (`REV:48-54,109-120`). On P3, `corr=0` and `μ=2` force
`s=1` as an inequality, not an attainment. Each component is a polynomial
curve, `A^1` normalization, one place at infinity, birational
parametrization. Zero correction on `D` makes `η` immersive, so every
affine singularity of `D` has exactly two smooth branches; contact
`k_z≥1` is an `A_{2k_z-1}` germ with `δ_z=k_z`.

The incidence repair is the S2 instance of `REV:93-95`, read from LOC at
`B0:362-372`, not a transfer of S1 pinning. At a two-branch point of `D`
with `K_p=0`, `a_p=1-Σ_{j≠D} W_j r_{j,p}`. Nonnegativity gives: in P3a at
most one `W=1` component may pass through, and then `a_p=0` with the
fixed letter supplied by the `μ=1` cluster; two such components are
impossible. In P3b the `W=2` companion cannot pass through. In every
allowed case `#Fix(G_p)=1`, so the two branch meridians remain disjoint
transpositions. Sol's claim that this does not change the local `S_5`
constraint is correct.

Exact genus budget (1.1) is the arithmetic-genus identity for a rational
plane curve, with `δ_aff=r_1+T` and `T:=Σ_{k_z≥2} k_z`. REV permits the
scalar N-A-RES gate `M_∞+2T≤3d-3 ⇒ π_1(C^2-D)=Z` for this singularity
class (`REV:122-136`). The complementary live range (1.2) is therefore
necessary for any still-live S2 candidate.

No reviewed exact degree, delta-sequence, or Puiseux characteristic.
B0's `d=3+2g_L+Σ_∞≥4` is withheld pending generic-line `π_1`-surjection
custody (`REV:99-107,154`). Sol correctly refuses to set `g_L=0` from
rationality of `D`, and correctly uses `d_min` for degree payoffs.
Chau's common leading pair and common physical point `P_∞` are reviewed
(`B0:537-548`; `REV:89,151`) and are not a ROW-NF: `(r,s)`, `m_D`, later
series, and denominator-shedding remain unpinned, so torus vs cable is
undecided. Notation in Sol §0 keeps `t`, `Q̃_∞`, `P_∞`, and the affine
double point `z` distinct (FALLACY-v2 flag/place/series).

Monodromy: unique branched component, other meridians trivial, so `ρ`
factors through `π_1(C^2-D)` onto `S_5` with meridian type `(2,1,1,1)`
(`B0:550-569`; `REV:64-66,146-152`). Transpositions generating a
transitive subgroup of `S_5` yield `S_5`. This is the reviewed S2 packet.
Sol's affine normal form (3.1)–(3.4) is a coordinate normalization of
that packet, not a degree-minimal ROW-NF, and Sol says so.

One documentation note, not a data error: Sol's N-A-RES citation is to
uncharged `CNA:44-49`. The same scalar gate is reviewed at `REV:122-136`
and is the N-A-RES package RK inherits. Consumable.

## 2. THEOREM[S5-COPRIME-KILL]: Hurwitz/cycle machinery at S₅

### 2.1 Orbit enumeration: which ⟨g⟩-conjugacy orbits of transpositions generate S₅?

Assume `g=gcd(d,n)=1` in affine normal form (3.1), with a geometric
transposition tuple `τ=(τ_1,…,τ_d)` generating `S_5` and
`Π=τ_1…τ_d`. After a generic shear, the coprime infinity braid is
`β_∞=δ_d^n` with `δ_d=σ_1…σ_{d-1}` (leading phases
`n(θ+2πj)/d` stay separated; exponent `n(d-1)` matches
`e=d-1+2δ_aff` via `δ_aff=(n-1)(d-1)/2`). Sol uses the right Hurwitz
convention `(x,y)·σ=(y,y^{-1}xy)` and the inverse
`δ̂_d:=δ_d^{-1}`. Direct check at `d=2,3`:

```text
τ · δ̂_d = (Π τ_d Π^{-1}, τ_1, …, τ_{d-1}).
```

Fixedness by `δ̂_d^n` is equivalent to fixedness by `δ_d^n`. Then
`δ̂_d^d` conjugates every entry by `Π`, so `δ̂_d^{nd}`-fixedness says
`Π^n` centralizes `⟨τ_i⟩=S_5`. The centre is trivial, hence
`Π^n=1` (5.1). Sign: `Π` is a product of `d` transpositions, so
`sgn Π=(-1)^d`.

Extend `τ_{j-d}:=Π τ_j Π^{-1}`. Fixedness is `τ_j=τ_{j-n}`: the
bi-infinite sequence is `n`-periodic, and translation by `d` is
conjugation by `Π`. Because `gcd(d,n)=1`, translation by `d` is
transitive on `Z/nZ`, so all entries form a single `⟨Π⟩`-conjugacy
orbit of one transposition. Conjugation acts on edges by
`Π·(ab)=(Π(a) Π(b))`. The generated group is `S_5` iff that edge
orbit is a connected graph on five vertices.

The seven conjugacy classes of `S_5`, with `Π` acting on a 2-set:

| type of `Π` | edge orbits that meet 5 vertices | generates `S_5`? |
|---|---|---|
| `1` | single edges | no |
| `(2)` | size ≤2; stars on 3 letters | no |
| `(2^2)` | e.g. `{(13),(24)}` on 4 letters; `{(15),(25)}` on 3 | no |
| `(3)(1^2)` | triangle on the 3-support; star from one fixed letter misses the other | no |
| `(3)(2)` | the six edges of `K_{3,2}` between the 3-support and the 2-support | yes |
| `(4)(1)` | four-edge star from the fixed letter | yes |
| `(5)` | the 5-cycle of adjacent transpositions, or the diagonal 5-cycle | yes |

For `(3)(2)=(123)(45)`, the orbit of `(14)` is
`(14)→(25)→(34)→(15)→(24)→(35)`. For `(4)(1)=(1234)`, the orbit of
`(15)` is the star at 5. For `(5)=(12345)`, `(12)` gives the boundary
cycle and `(13)` the pentagram. A connected transposition graph on
`n` vertices generates `S_n` (a spanning tree already does). Sol's
table (`SOL:403-413`) matches this enumeration exactly. It is not an
`S_4` subscript change: in `S_4` a 3-cycle's star from the unique
fixed letter meets all four vertices, which is why Theorem A at `S_4`
admits `ord Π=3`; here a 3-cycle has two fixed letters and cannot.

### 2.2 Π-order fork

`Π^n=1` forces `ord(Π)∣n`. Combined with the surviving types:

- `(3)(2)` has order 6, so `6∣n`;
- `(4)(1)` has order 4, so `4∣n`;
- `(5)` has order 5, so `5∣n`.

In particular `n≥4` (none of 1, 2, 3 is a multiple of 4, 5, or 6).
Together with `d>n` this gives `d≥5`. This lower bound is
load-bearing for the nodalization: it is the S5 replacement of
Theorem A's `n≥3`.

### 2.3 Parity constraints

`sgn Π=(-1)^d`. A 3-cycle is even and a transposition odd, so
`(3)(2)` is odd and `d` is odd. A 4-cycle is odd, so `(4)(1)` needs
`d` odd. A 5-cycle is even, so `(5)` needs `d` even. This is Sol's
last column. No generating type has both `d` and `n` odd: the first
two force `n` even, the third forces `d` even. The S4 both-odd kill
is thus included, but is not the mechanism.

Coprime formulae (4.4) are the standard one-pair identities
`δ_∞=(d-n-1)(d-1)/2`, `δ_aff=(n-1)(d-1)/2`, and
`M_∞=mult+β_h-1=(d-n)+d-1=2d-n-1` (chart `(v,u)=(ζ^{d-n},ζ^d)`).
Cross-check against the promoted identity
`C'^2-2δ_aff=3d-2-M_∞` (`REV:130-134`): the coprime nodal Nori
quantity is `B=n+d-1`, hence `M_∞=2d-n-1`, and N-A-RES
`M_∞≤3d-3` is exactly `B>0`.

### 2.4 Verdict on S5-COPRIME-KILL

Keep `p` fixed (same vertical projection, same regular base fibre)
and vary `q` through polynomials of exact degree `n` with fixed
leading coefficient. Coprimality keeps every nearby pair birational
and keeps the infinity germ, hence `δ_∞` and `M_∞`, constant. For
`n≥4` the evaluation maps on `q` separate 1-jets at two points and
values at three: common zeros of `p'` and `q'`, nontransverse double
fibres, and triple fibres are proper closed conditions in the
`q`-space (the S4 coefficient count of 1-jet separation at `n≥3`
applies a fortiori). Sol's writeup of this properness is compressed
relative to that count — "two-point Hermite / three-point value
evaluation" — but the rank is present. The direction `h=t` has
`h^{[1]}(a_z,b_z)=1≠0` at every old pair, so a generic analytic arc
through `q` is immersive with only ordinary nodes for `ε≠0`.

Local intersection conservation on `p^{[1]}=0` (smooth, because the
projection was sheared transverse to both branches) splits a
`k_z`-fold zero of `q^{[1]}` into `k_z` reduced ordered nodes. Global
`δ_aff` is constant, so there are no extra nodes and no loss to
infinity. This is not the barred unqualified δ-constant `π_1`
transport (`RK` inherits that bar from the N-A package): `p` is
fixed, vertical-tangency factors isotope outside the singularity
discs, and inside each disc the two-strand tube has abelian `B_2`,
so the `k_z` node factors are a single conjugate `w_z σ^2 w_z^{-1}`.
ZvK therefore specialises in the allowed direction

```text
G_0 ↠ G_ε = G_0 / ⟨⟨ [w_z(ξ_z), w_z(υ_z)] : z tangential ⟩⟩.
```

Under `ρ` each pair is a simultaneous conjugate of two disjoint
transpositions, already commuting, so every added commutator dies and
`ρ` factors through `G_ε`. For the nodal nearby curve, `T=0` and
`M_∞=2d-n-1≤2d-2≤3d-3`. Promoted N-A-RES (`REV:122-136`) gives
`π_1(C^2-D_ε)=Z`, which cannot surject onto `S_5`.

This is the S5 run of the Theorem A + nodalization + Nori chain, with
the orbit table redone at `S_5` and N-A-RES in place of the S4
Theorem B. It does not use a resolvent or INF-TRIVIAL. The nearby
curve need not be a Keller component: N-A-RES is a curve-level gate.

**THEOREM[S5-COPRIME-KILL] is CONFIRMED.** Conditional transfers of
the old `(6,3)→(5,3)` and `(6,3)→(8,3)` triangular reductions
(`SOL:477-481`) stay at their row-geometry scope and do not pin S2.

Presentation repair, not a hole: unpack the `q`-space rank as in the
S4 1-jet count if the theorem is restated. The bound `n≥4` from §2.1
is what makes that count available.

## 3. Cable-stratum transport: the (6,4) kill

**Verdict: CONFIRMED as a kill of the affine-normal-form slice; the
slice does sit in the S2 geometric class.** It is not a pin that S2
has these degrees.

In (3.1) with `(d,n)=(6,4)`, one has `g=2`, `d'=3`, `n'=2`. Leading
terms at infinity give three asymptotically separated 2-strand tubes
whose outer braid is `δ_3^2`. Later characteristic exponents refine
only the inner 2-braids (required for birationality, since
`gcd(6,4)=2`); they cannot merge tubes, because they are higher-order
as `ζ→0`. Inner 2-braids preserve each block product
`A=τ_1τ_2`, `B=τ_3τ_4`, `C=τ_5τ_6`. ZvK supplies literal fixedness of
a cable-adapted based tuple, hence equivariance
`(A,B,C)·δ_3^2=(A,B,C)`.

In Sol's convention, `(x,y)·σ=(y,y^{-1}xy)` and `δ_3=σ_1σ_2`. One
`δ_3` sends `(A,B,C)` to `(B,C,C^{-1}B^{-1}ABC)`. A second application
has first component `C`, so `C=A`. The second component then rearranges
to `ABA=BAB`. The third component is redundant given those two (from
`A^2=B^2=1` in the involution cases, and by the braid relation
generally): if `C=A` and `ABA=BAB` then the third slot returns `A`.
So (5.3) is correct in the stated convention. Inverse-braid fixedness
is equivalent.

`A` and `B` are conjugate products of two transpositions, hence both
identity, both 3-cycles, or both type `2^2`.

- Identity: `τ_{2i-1}=τ_{2i}`, at most three edges, too few to
  connect five vertices. (This is S5-specific: three edges *can*
  connect four vertices, which is why the same block system did not
  kill the S4 (6,4) row.)
- 3-cycles: if the supports meet in one letter, conjugate to
  `A=(123)` and `B=(145)` or `(154)`. Direct evaluation:
  `ABA=(1 3 4 5 2)` vs `BAB=(1 5 2 3 4)` in the first subcase, and
  `ABA=(1 3 5 4 2)` vs `BAB=(1 4 2 3 5)` in the second. Both violate
  (5.3). Hence all factors fix a common fifth letter and live on at
  most four letters.
- Type `2^2`: involutions, so `ABA=BAB` iff `(AB)^3=1`. If `A=B`,
  support has four letters. If `A≠B`, two 2-edge matchings have
  product order 3 iff they share exactly one edge (same fixed letter
  and no shared edge: Klein four, order 2; different fixed letters and
  no shared edge: 5-cycle). Shared-edge factorizations are unique as
  disjoint transpositions and preserve the shared 2-set and its
  complementary 3-set, e.g. `A=(12)(34)`, `B=(12)(35)` uses edges
  `(12),(34),(35)`, a disconnected graph.

Every case is intransitive. The whole `(6,4)` affine-normal-form
cable dies, including every inner word and in particular
`Δ=(6,4,3)`.

Does this slice embed in S2? S2 is the class of irreducible polynomial
curves with `A^1` normalization, one place at infinity, only
two-smooth-branch affine singularities, and an `S_5` transposition
representation with disjoint local pairs. Affine normal form (3.1) is
available on that class. The pair `(6,4)` is a coordinate slice with
`g≥2`. N-A-RES does *not* kill the interesting point of the slice:
the old nodal type `Δ=(6,4,3)` has `(δ_∞,δ_aff,M_∞)=(7,3,16)` and
`3d-2=16`, so it lies on the live side of (1.2). The braid argument
is necessary, not a restatement of N-A-RES. The coprime formula
`M_∞=2d-n-1=7` is false here; Sol does not use it.

The `(8,4)` inheritance (`SOL:533-537`) is only the already-recorded
target equivalence of the *explicit N=4 families* (`RK:50-53`:
`Δ=(8,4,6,3) ⟺ deg(P-Q^2)=6`). Sol bounds it as a conditional
row-geometry consequence and does not claim every S2 curve of degree
pair `(8,4)` dies. `(8,6)` and `(9,6)` remain untouched. Correct
scope.

Triangular Aut cannot drop `(6,4)` by subtracting a polynomial in
`q` from `p`: `deg q^2=8>6`. If some other Aut produces a coprime
pair, §2 already kills it.

## 4. Resolvent impossibility at S₅ and typed replacements

**Verdict: CONFIRMED.** There is no `S_4→S_3`-style quotient, and the
typed replacements do not presently kill the noncoprime residue.

Normal subgroups of `S_5` are `1`, `A_5`, `S_5`. `A_5` is simple. A
normal subgroup meeting `A_5` trivially injects into `S_5/A_5≅C_2`,
hence has order at most 2. An order-2 normal subgroup is central, but
`Z(S_5)=1`. The only nontrivial proper quotient is therefore `C_2`.
There is no homomorphism `S_5↠S_3` and no analogue of
`S_4/V_4≅S_3`. The N=4 chain "transpositions in a triple cover to a
normal triple plane" stops at the first arrow.

Permutation resolvents, recomputed here:

- Natural `S_5/S_4`, degree 5: a transposition has type `1^3 2`. This
  is the original cover.
- Sign, degree 2: type `2`. Loses the `A_5` layer. For even `d`,
  `sgn ρ(γ_∞)=(-1)^d=1`, so sign-triviality of the infinity meridian
  is not full INF-TRIVIAL: `Π` may still be a nontrivial even
  permutation.
- Six Sylow 5-subgroups, degree 6: `|S_5|=120`,
  `|N_{S_5}(C_5)|=20`, index 6. Involutions in `AGL(1,5)` have
  natural type `1\,2^2`, not `1^3 2`, so a transposition normalizes
  no Sylow 5-subgroup, has no fixed point on the six, and has type
  `2^3`. Kernel is normal, cannot be `A_5` (not contained in a
  stabilizer of order 20), hence the action is faithful.
- 2-subsets, degree 10: `(12)` fixes `{1,2}` and the three pairs in
  `{3,4,5}`, and swaps `{1,j}↔{2,j}` for `j=3,4,5`, type `1^4 2^3`.
  Faithful (kernel cannot contain `A_5`).

Neither associated cover is a simply branched triple cover. Calling
either "the `S_5` quotient" would confuse an associated cover with a
normal quotient. Sol's table (`SOL:139-153`) is correct.

If full INF-TRIVIAL holds, Riemann existence plus miracle-flatness
(normal surface, regular 2-dimensional base) gives a flat degree-5
cover of `P^2` branched simply along `D̄`, and the trace discriminant
forces `O(D̄)≅(det E)^2`, hence `d` even — the same parity already
read from `sgn`. For even `d` this is not a contradiction. Miranda's
binary-cubic theory is degree 3 (hashed PDF above; Introduction /
Theorem 1.1). Casnati's degree-5 theory, in the Casnati–Ekedahl form
recorded by Landesman–Vakil–Wood Theorem 3.16 (hashed; generalizes
Casnati Theorem 3.8), parametrizes *Gorenstein* covers by a rank-4
bundle `E`, a rank-5 bundle `F`, and an alternating section whose
4×4 Pfaffians cut out the cover. Normality of `X` does not by itself
make the isolated points over `P_∞` Gorenstein. Structure data is not
a classification of Pfaffian discriminants with a prescribed rational
one-place branch curve. Chisini-type uniqueness, even when its
hypotheses hold, is uniqueness from a branch curve, not nonexistence.

The typed replacements are therefore exactly Sol's three OPENs on the
cover side — `OPEN[N5-S2-QUINTIC-PLANE]` (Gorenstein or an extension
of the Pfaffian theory, then classify), `OPEN[N5-S2-INF-TRIVIAL-CABLE]`
(sign insufficient), and the instruction that a pinned row proving
INF-TRIVIAL rather than killing the tuple must invoke the quintic-plane
question, not the S4 triple-plane theorem — plus the geometric
`OPEN[N5-S2-ROW-PIN]` of §5. No safe replacement presently kills all
noncoprime S2 rows.

## 5. OPEN scoping: residual cage and row-pin

### 5.1 OPEN[PI1-S5-NODAL-NONCOPRIME]

**Verdict: CONFIRMED as a necessary-only cage; killed strata are
correctly excluded and not over-excluded.**

The residual question (`SOL:546-556`) asks for an irreducible
polynomial curve in degree-minimal affine normal form (3.1),
`d>n≥1`, `g=gcd(d,n)≥2`, two-smooth-branch affine singularities,
`M_∞+2T≥3d-2`, and a surjection `π_1(C^2-D)↠S_5` sending meridians
to transpositions and local branch pairs to disjoint transpositions,
with no polynomial target automorphism yielding a coprime pair or
the killed affine-normal-form pair `(6,4)`.

Necessary-only is explicit (`SOL:558-559`): no Keller realization is
claimed. Strictly narrower than B0's DQ-1 (`B0:615-620`) by the
removal of `g=1`. Not a single numerical row.

Exclusions:
- Coprime: `g≥2` plus the Aut-to-coprime clause. Any curve that is
  coprime in some affine normal form dies by §2; the Aut clause
  catches coordinate changes that produce `(C1)`.
- `(6,4)`: explicit Aut clause. This includes the old `Δ=(6,4,3)`
  type and any Aut-image, in particular the explicit N=4 `(8,4)`
  family, but *not* an arbitrary `(8,4)` that is not Aut-equivalent
  to `(6,4)`.
- Affine line: omitted by `d>n≥1` and generation.
- N-A-RES-killed rows: the inequality `M_∞+2T≥3d-2` is the
  complement of the promoted scalar gate, using `2T` at the scalar
  level (`REV:122-136`), not the theorem-level `4T`.

What remains, correctly: other noncoprime pairs in degree-minimal
coordinates, including `(8,6)` and `(9,6)`, and any `(8,4)` not
Aut-equivalent to `(6,4)`. Odd `d` is kept: sign already forbids
INF-TRIVIAL, but the representation is of the affine complement.
P3a and P3b share the same `D`-question (trivial extra meridians).

The cage is not a realization list and does not reintroduce B0's
withheld degree floor.

### 5.2 Row-pin OPEN

**Verdict: CONFIRMED as the first missing geometric tool.**

`OPEN[N5-S2-ROW-PIN]` (`SOL:563-568`) asks, in degree-minimal target
coordinates, for either an exact degree/delta-sequence list for `D`
(approximate-root remainders and the infinity multiplicity sequence)
or a degree cap making that list finite, derived from reviewed N=5
Keller data. Without it there is no licensed infinity word on which
to run the §5.2 block-product analysis, no fold relation, and no
value of `ρ(γ_∞)` for the projective-cover route. Once a row is
pinned, the next fork Sol writes is the right one: compute the
iterated-cable braid and decide the tuple (model: §5.2); if that
proves INF-TRIVIAL rather than killing, invoke the quintic-plane
OPEN, not the S4 triple-plane theorem.

B0's DQ-3 (a Jelonek-type `deg A_F≤N-1`) would kill the whole
reducible-with-trivial case at N=5, but it is UNVERIFIED
(`B0:634-642`; no hashed source). Sol does not consume it. Fail-closed
is correct. S1 is a different singularity class and is correctly
handed off as `OPEN[PI1-S5-CUSP]` (`REV:154-160`), unworked here.

## 6. FALLACY-v2 checks

- **Flag/place/series.** `t`, `Q̃_∞`, `P_∞`, and the affine double
  point `z` stay distinct (`SOL:21-25`). Chau's leading pair is not
  used as a ROW-NF. For `g=1` no later term is invoked to shed a
  denominator; for `g≥2` the gcd tower is typed unpinned. Pass.
- **Per-ray/exit-set.** No exit-price claim; no `charge_basis` line.
  Pass.
- **Carrier/attainment.** S2 and both residual OPENs are necessary
  cages. No Keller map is asserted to realize them. Pass.
- **Pole/interior.** `M_∞=mult+β_h-1` is the promoted cluster
  identity, applied after the one-place vertex class in the `X=1`
  chart. Coprime one-pair data are not used on cables. Pass.
- **Floor/attainment.** `s=1` is forced by `corr≥μ(s-1)` at
  `corr=0`, not by reading a floor as equality. N-A-RES is used as
  an implication, not as attainment of `3d-3`. Pass.
- **`sat()`, raw remainder, variable/ring map.** Sol refuses
  `p=r^2` and `deg(p-q^2)=6` without delta-sequence data, and
  declares the (3.1) coordinate changes. Pass.
- **Prime label, merge-free, target/arrival.** Not in play, except
  that `d` and `d_min` are kept distinct. Pass.

No gap is filled by cap or analogy. Unsettled cable rows stay OPEN.

## 7. Item verdicts and promotion recommendation

| item | verdict |
|---|---|
| (1) S2 data extraction vs. reviewed N5 | **CONFIRMED** |
| (2) S5-COPRIME-KILL (orbits, Π-order, parity, nodalization) | **CONFIRMED** |
| (3) (6,4) cable-stratum transport / embedding in S2 | **CONFIRMED** (affine-normal-form slice; not a degree pin) |
| (4) Resolvent impossibility and typed replacements | **CONFIRMED** |
| (5) OPEN cage and ROW-PIN scoping | **CONFIRMED** (necessary-only; killed strata excluded) |

**Overall: CONFIRMED-AS-CHARGED.** Promote:

- THEOREM[S5-COPRIME-KILL]: no S2 representation when `gcd(d,n)=1`
  in affine normal form (3.1) (equivalently, after a coordinate
  choice with a single Puiseux pair at infinity);
- the (6,4) affine-normal-form cable kill, including every inner
  word, by the block-product calculation of §3;
- absence of an `S_5↠S_3` resolvent, the permutation-resolvent
  table, and the typed cover-side OPENs
  `N5-S2-QUINTIC-PLANE` and `N5-S2-INF-TRIVIAL-CABLE`;
- residual
  `OPEN[PI1-S5-NODAL-NONCOPRIME] + OPEN[N5-S2-ROW-PIN]`,
  necessary-only, for both P3a and P3b.

Do **not** promote: a decision of S2; any exact degree, delta-sequence,
or ROW-NF for the N=5 branched component; reuse of the S4 triple-plane
theorem; a general (8,4) kill beyond Aut-equivalence to (6,4); B0's
withheld transversal-genus degree floor; B0 DQ-3; any S1 analysis.

Two documentation notes, not restatements of the theorems: (i) Sol
cites N-A-RES and the (8,4)~(6,4) transport by line number in the
uncharged 2026-08-31 N-A rowsweep coordinator; the same content is
reviewed in REV and recorded in RK. (ii) The `q`-space properness in
§2.4 is compressed; the S4 1-jet count at `n≥4` unpacks it.

S1 remains `OPEN[PI1-S5-CUSP]`. RK's provisional N=5 bullet
(`RK:77-82`) may now drop the provisional tag on the two kills and
the residual cage; S2 itself stays OPEN.

Primary sources independently hashed in this lane are listed in §0.
Cycle-type computations in §2–§4 are desk-derived and are not
attributed to those PDFs. Miranda and Landesman–Vakil–Wood are used
only to delimit cover-structure theorems, matching Sol's non-use of
them as a kill. Chau is used only as the reviewed common-leading-pair
pin already confirmed by REV.

<!-- BODY-END -->
