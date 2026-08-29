# Fable 5 different-model reconstruction — TD12 S17 source bridge (S route)

Lane: Fable 5, equal-standing adversarial reviewer; different-model
reconstruction, not a rubber-stamp of the producer or of Sol's repair map.
Date: 2026-08-29 UTC. Frozen campaign basis, verified at session start and
re-verified immediately before sealing:

```text
40c1ab3448209e3d87173feb947a733f6fe54f7f
```

Quarantined producer evidence (read, not trusted):

```text
3595fb88ef01fe72dce13cbb00b817a75a040f744764a8e34f865450c01b77d1
  xmodel/td12-global-source-bridge-s-opus5-92e-20260829.md   (full file)
c4825be2dc3603031c2aad4caa6eb1cea40e57ae6c01a9d8ce19d1101f3cc2e0
  its true pre-seal body, 42545 bytes (recomputed here, §1.2)
```

Guidance, not premise:

```text
1a6472f8ff8530cc77deee622160e3095fcf12e9c958ba5ac3d27a70fd339ac9
  xmodel/td12-global-source-bridge-s-opus5-internal-audit-sol56-20260829.md
```

Task pin: `55920a2f659833106db79d2a3e338720d6576cac52e8e60f79a7c83432125413`
(`...different-model-review-fable5-40c-20260829.prompt.md`). Desk algebra
only; exact stdlib `Fraction` controls confined to `/tmp` (§9). No web, AWS,
commit, push, canonical edit, or external message. `jc2-lean` was not read,
listed, stat'ed, grepped, built, or touched in any way. Exactly one
repository file written: this report.

## 0. Dispositions

```text
MATHEMATICS  = PASS_WITH_MATERIAL_REPAIRS
               (independently reconstructed from the literal sources;
                every producer theorem survives at its repaired scope;
                C1/C2/D strengthened, translation lemma verified with a
                sharpened invariance range)
CUSTODY      = FAIL_PRODUCER_SEAL_AND_ONE_STALE_CHARGED_HASH
               (two independent defects, §1.2–§1.3; quarantine stands;
                promotion only under a fresh coordinator seal that binds
                the full-file hash)
FLOOR-COORD  = CLOSED_WLOG_UP_TO_EXPLICIT_AUT_EQUIVALENCE at S17 scope;
               the literal fixed-representative question remains OPEN and
               has no remaining operational consumer (§5)
MAXIMUM SAFE DISPOSITION = BRIDGE_AVAILABLE_AT_MAP_LEVEL /
                           VALUE_LEVEL_STILL_OPEN   (confirmed)
```

No exit price is asserted anywhere in this report; `charge_basis=` is
correctly absent.

## 1. Custody

### 1.1 Rehash of every input used

All recomputed with SHA-256 before reading and again before sealing;
identical both times. Full table in §12. Every hash in the producer's §0
recomputes on the 40c basis **except** `ladder/REDUCTION.md` (§1.3). The
wave packet's internal seal (`6730` bytes,
`7a6ce89e9858572b1a7e1cc3c06217145fb7f0e29f2d727b5959c8b0a0abce65`)
recomputes.

### 1.2 Producer seal failure, characterized byte-exactly

The producer file contains the byte string `## Seal` at exactly two
offsets, `42545` and `42816`. Offset `42545` is the only occurrence at a
line start — the actual heading. Offset `42816` is the backticked mention
inside the seal's own definition sentence ("before the literal `## Seal`
heading"). Recomputed:

```text
sha256(bytes[0:42545]) = c4825be2dc3603031c2aad4caa6eb1cea40e57ae6c01a9d8ce19d1101f3cc2e0
sha256(bytes[0:42816]) = c0c03d4edb1838f27ed0f1b86c8041568d41366a94f678209458ca3909831ac0
```

So the recorded pair (`42816`, `c0c03d4e...`) is the prefix ending at the
seal's **self-mention**: the producer's tooling matched the last occurrence
of the literal, and the sealed range includes the seal heading plus its
first paragraph. Under the seal's own definition the body is `42545` bytes
with hash `c4825be2...` — exactly as the task states. The mathematics
content is unaffected (the body is intact and deterministic), but the
document is not internally sealed. Note the campaign promoted this bridge
under short-id `c0c03d4e`, i.e. under the malformed range; the durable
object identifier must be the full-file hash `3595fb88...` with true body
`c4825be2...`. Recommended convention fix: define the body by a unique
sentinel line (as Sol's audit and the coordinator files already do), or by
"first occurrence of the heading at line start" — never by a bare substring
that the seal text itself contains.

### 1.3 Second custody defect: stale charged hash (missed by Sol's audit)

The producer's §0 charges

```text
d409510a3df418f402a80cc954f646d35a054e9055783fadc0aaa234bb49b242  ladder/REDUCTION.md
```

and claims all §0 hashes were "recomputed identically before reading and
before sealing" on basis `92ebe92a`. False for this entry:

- at the producer's declared basis `92ebe92a` (and at `40c1ab34`) the file
  is blob `c0dfd44a...` with content SHA-256
  `29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b`;
- `d409510a...` is the content hash of blob `038fdc95...`, the version at
  `76c746f6` — two commits before the producer's basis;
- provenance of the error: `bb70bc4b...`
  (`td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md`,
  itself at basis `76c746f6`) charges `ladder/REDUCTION.md` at exactly
  `d409510a...`, correctly for *its* basis. The producer evidently copied
  that line forward instead of recomputing.

Materiality: none for content. The passages the producer consumed (the
GGV22 dichotomy "`max(deg P, deg Q) >= 125` or degree pair `(72,108)` or
its transpose" and the "not load-bearing in the sheet/book reduction and
cannot be used globally" classification) are byte-identical in both blob
versions — verified by direct comparison; the `76c746f6 -> 92ebe92a` drift
touched only the U1/U2 labelled-route sections. But the defect impeaches
the producer's custody-discipline claim independently of the seal bug, and
Sol's internal audit did not catch it.

## 2. Source verification (refs/sigray_full.pdf, `9bf9f032...`)

Read directly from the pinned PDF at printed pages 5–18 (printed = PDF page
numbers; verified). Every producer citation checked:

1. **Notation 1.3 (p. 5).** Jacobian pair means `J(f,g) = ⊖`, the free
   `C*`-constant glyph. So "`J(f,g) = 1`" in the reconstruction below is a
   WLOG target scaling (`g -> g/c` is a `𝔎`-move preserving the Notation
   2.1 class, degrees, and supports). The producer's Theorem C states
   `J = 1` without flagging this; harmless, now flagged (repair R10).
2. **Notation 2.1 (p. 7).** `(f,g) ~ (f*,g*)` iff `(f*,g*) = 𝔎∘(f,g)∘𝔏`
   with `𝔎, 𝔏` automorphisms; almost normalized = lexicographically minimal
   `(deg f, deg g)` in the class; almost normalized counterexample = not an
   automorphism. Two-sided class — load-bearing for §4.
3. **Lemma 2.1 (pp. 8–9).** (i) corners `(k_f,l_f) ∈ N_f`,
   `(k_g,l_g) ∈ N_g`, all four positive, rectangle confinement; (ii)
   `k_f/k_g = l_f/l_g`; (iii) `k_f < k_g`, `l_f < l_g`, `l_f <= k_f`,
   `l_g <= k_g`; (iv) `k_g/k_f ∉ N*`. Proof prints
   `f^+_{(1,1)} = ⊖ x^{k_f} y^{l_f}` (single monomial) and, on p. 9, uses
   `[A, Proposition 17.4]` **only** for `w = (w_1,w_2)` with
   `w_1, w_2 > 0` — producer blocker B4 confirmed at the source.
4. **Notation 2.3 (p. 9).** Normalized counterexample = almost normalized
   counterexample *admitting* (i)–(iv). No linear-change-of-variables form
   is required by the definition — load-bearing for §4 (affine `𝔏` is
   admissible).
5. **Notation 2.4 (p. 9).** Prints `(i) α/β = k_f/k_g` — my independent
   page extraction concurs with the producer's bbox reading; with
   `k_f < k_g` this gives `α < β`, so type `(2,3)` means
   `k_g/k_f = l_g/l_f = 3/2`. Cross-check via (iv) as in the producer
   §0.1: agrees.
6. **Statement 3.1 (p. 10).** Form (3): `y = Σ_{j=0}^∞ c_j x^{−j/κ}` —
   the sum starts at `j = 0`; no positive-exponent prefix terms exist.
   Load-bearing for Theorems B and for §4 (T5).
7. **Notations 3.4/3.5 (p. 12).** `ν_F := e_{j−1}/e_j`,
   `κ_F := κ/e_j`; hence `κ_F/ν_F = κ/e_{j−1} ∈ N` and `ν_F | κ_F` — the
   producer's `17 | κ_F` pin is exact. With the cell's
   `k̄_F = κ_F(1−u) = 13`: `u = 1 − 13/κ_F ∈ [4/17, 1)` and
   `κ_F u = κ_F − 13 ∈ Z`, so `κ_F σ ∈ Z` for every `σ = J − um`.
8. **Notation 3.8 (p. 12).** `F ∗ c` is defined only if some branch `P`
   through `F` has `c_n = c`. **Statement 3.18 (p. 18)** sharpens this: if
   `F ∗ c` exists then `c` is a root of `p_F`; a nonzero root admits the
   step only after the unique `ν_F`-th root-of-unity twist. This is the
   exact source form of blocker B3.
9. **Notation 3.9 (p. 13** — producer cites p. 12, off by one**).**
   `η_F := x^{π(F)}(y − Σ_{j<π(F)} c_j x^{−j})`; so the prefix `φ` has
   exponents in `(−u, 0]`, exactly as Theorem B's proof needs.
10. **Statement 3.7 (5), Notation 3.10 (largest index), Notation
    3.11/Statement 3.8 (`D_{h,F} := κ_F d_{h,F} ∈ Z`), Proposition 3.1
    (∗)(∗∗) (pp. 13–15).** All as the producer states.
11. **Statement 3.9 and its proof (p. 15).** The three print defects are
    real and exactly as described: the display prints `p_j(x^{−κ}η + c)`
    with upper limit `l`, and the next sentence prints `a_l x^{(n−l)κ}η^l`,
    while the same proof prints the genuine stacked fraction in
    `s < (n−l)/κ = d − l/κ` and the identity `η_G = x^{1/κ}(η_F − c)`.
    The corrections `x^{−1/κ}`, `x^{(n−l)/κ}`, upper limit `n` are forced.
    Producer's §0.1 heading says "Two literal errata" but lists three
    repairs; Sol's count of three is right (repair R10).
12. **Proposition 4.1 (p. 18).** Hypothesis (7) `(g−b)_F^+ ≢ c ∈ C`,
    display (8), and the proof line — which prints
    `J(f^F(ξ,η),(g−b)(ξ,η)^F) = ⊖ξ^{−n/κ}` **with** the `⊖` glyph. The
    producer's §0 perimeter quote dropped the glyph (the known pdftotext
    hazard); immaterial once `J = 1` is fixed, now recorded (R10).
13. **Statements 3.10, 3.11, 3.13, Notations 3.13/3.14 (p. 16).** As
    cited; Notation 3.13 (`p_F := p_{f,F}`) and `d_F > 0` justify the
    producer's hostile-attack-6 reply: for `F ∈ T_a^+` the tops of `f` and
    `f − a` coincide.

Campaign inputs were consumed at recorded scope and re-verified where load
bearing: the `(E_s)` convolution and `s*` (rederived from scratch below,
identical to `1a602643...` §2.3 as audited in `876d1717...` §2); the cell
tuple and rigid template (`9a9e948c...`, `52ffafa2...`); the `(C)`/`(V)`
laws and §8.4 level-1 asymmetric exhibit (`1a602643...`); route separation
(`79df783a...`); `NO_FORMAL_CASCADE_KILL_IN_WINDOW` and the "target `s*`,
not `s = i+1` or `r+1`" stop order (`97ba497f...`); the wave-packet
deliverables 1–3 and the "do not merely restate `PAIRREF_ABSENT`"
instruction (`7af80df7...`).

## 3. Reconstruction of the mathematics, at repaired scope

Everything in this section was re-derived by hand from the §2 sources and
spot-checked with exact `Fraction` controls (§9). Notation: for
`0 ≠ h ∈ C[x,y]` and `u ∈ R_{≥0}`,
`σ_h(u) := min{J − um : (J,m) ∈ supp h}` and `h_u^↓` the sum of the terms
attaining it; at a vertex, `ξ := x^{−1/κ}`, `n := κ d_{h,F}`,
`P_k := p_{h,n−k}`.

### 3.1 Shear scheme (producer Theorem A) — sound after normalization repair

The corrected St 3.9 display gives exactly
`h^G(ξ,η) = h^F(ξ, c + ξη)` (A1). The producer's (A2) as printed —
"`ξ^l | h^F(ξ, c+ξη)`" — is ill-typed: `h^F` is Laurent in `ξ` and `ξ` is
a unit. Sol's normalization is the right repair and I verify it:

```text
Q_c(ξ,η) := ξ^n h^F(ξ, c+ξη) = Σ_{k≥0} ξ^k P_k(c+ξη) ∈ C[ξ,η],
[ξ^s η^m] Q_c = P_{s−m}^{(m)}(c)/m!,
ladder  ord_c(P_k) ≥ l−k for all k   ⇔   [ξ^s]Q_c = 0 for s < l
        ⇔   d_{h,F∗c} ≤ d_{h,F} − l/κ      (St 3.9(iii) gives equality),
p_{h,F∗c}(η) = [ξ^l] Q_c = Σ_{k=0}^{l} v_{c,k} η^{l−k},
v_{c,k} = [(z−c)^{l−k}] P_k(z),        l := mult(P_0, c),
```

with `ord_ξ Q_c = l` exactly (the `η^l`-coefficient at `ξ^l` is
`P_0^{(l)}(c)/l! ≠ 0`, which is St 3.9(ii)'s `a_l = b_l`). (A4): the shear
`(ξ,η) ↦ (ξ, c+ξη)` has Jacobian determinant `ξ`, so
`J_{ξ,η}(f^G,g^G) = ξ·[J_{ξ,η}(f^F,g^F)](ξ, c+ξη)`; with
`J_{ξ,η}(f^F,g^F) = −κ ξ^{κu−κ−1}` (sign and exponent re-derived from
`x = ξ^{−κ}`) this is exactly `u ↦ u + 1/κ`. Cell consistency:
`mult(λ_f p(η^{17})^i, c_±) = i` since `t − B_±` has the simple factor
`(η − c_±)` — so `l = i` and (A3) is the recorded `(C)` law verbatim. The
`(V)` rider stays tree-conditional (Not 3.8 + St 3.18); the producer's
negative control (double root that is not a branch coefficient) is the
right guard.

### 3.2 Branch-free Newton floor (producer Theorem B) — sound

Verified: with `y = φ(x) + ηx^{−u}`, prefix exponents in `(−u,0]` (§2
items 6, 9), a monomial `x^J y^m` contributes cross terms of exponent
`J − um' − Σ j_i > J − um` for `m' < m` (each `j_i < u`), so the least
exponent of `h^F` is `σ_h(u)`, attained only by pure `η^m` terms, and
`p_{h,min}(η) = h_u^↓(1,η) ≠ 0` (distinct face points have distinct `m`).
Machine control TEST A. The proof in fact needs only `j < u`, so it is
robust even beyond form (3). `u = 0` endpoint: trivially true (empty
prefix) though the producer's slope-`1/u` sentence does not cover it;
S17 has `u ≥ 4/17` (repair R8). The §4-Remark formula
`σ_{h−a}(u) = min(σ_h(u),0)` has an immaterial corner case when
`h(0,0) = a` exactly (R9).

### 3.3 Floor dichotomy (producer Theorem C) — C1/C2 strengthened, C5 rescoped

**Strengthening.** C1 and C2 need no chart, no tree, and no rationality:
for the weight `w(x^Jy^m) = J − um`, every term of `f_x g_y − f_y g_x` has
`w ≥ σ_f(u) + σ_g(u) − 1 + u`, and cancellation preserves levels; since
the polynomial `1` has its only term at level 0:

```text
(C1)  σ_f(u) + σ_g(u) ≤ 1 − u    for every real u ≥ 0;
(C2)  the bottom graded piece of J(f,g) is J(f_u^↓, g_u^↓), so
      J(f_u^↓,g_u^↓) = 1 if Γ(u) = 0 and = 0 if Γ(u) > 0,
      Γ(u) := (1−u) − σ_f(u) − σ_g(u).
```

The producer's convolution route agrees where both apply: I rederived
`Σ_{j+k=m}(j p_{f,j} p_{g,k}' − k p_{f,j}' p_{g,k}) = κ·[m = κ(1−u)]`
from `dx∧dy = x^{−u}dx∧dη` alone, identical to the charged `1a602643...`
§2.3, and its least-index row is `κ(σ_f P G' − σ_g P' G) = κ·[Γ=0]`.
Machine control TEST B (eight values of `u` on a genuine Jacobian pair,
plus an identically-`Γ=0` pair).

**(C3)** — cell-lattice scope, arithmetic verified: on the `κ_F`-lattice
(`κ_F σ_h(u) ∈ Z` by §2 item 7), the floor row of `(E_s)` sits at

```text
K_P + K_G = (D_F − κ_F σ_f(u)) + (D_g − κ_F σ_g(u)) = s* + κ_F Γ(u),
s* = D_F + D_g − k̄_F = (85i − 26)/2  (type (2,3), r = 3i/2, i even),
```

so `s*` is exactly `κ_F Γ(u)` rows above the floor and `s*` rows below the
ceiling, and the two ends coincide with the Keller row exactly when
`Γ(u) = 0` resp. `s* = 0`. The clean form of the producer's §5.4
non-absorbability remark: the floor row of the convolution involves *only*
the two floor polynomials, so when `Γ(u) = 0` the compatibility
`J(f_u^↓,g_u^↓) = 1` constrains the two minimal faces themselves and no
choice of other graded pieces can alter it.

**(C4)** — sound with integer-cleared powers (repair R2): from
`σ_f P G' = σ_g P' G` with `σ_f σ_g ≠ 0`, setting
`(a,b) := (κ_F σ_f, κ_F σ_g) ∈ Z²`, the exact statement is
`a·div(p_{g,min}) = b·div(p_{f,min})` as divisors on `A¹`, equivalently
`p_{g,min}^a = c · p_{f,min}^b` in `C(η)*`; "homothetic faces" is the
divisor/UFD statement, not fractional polynomial powers.

**(C5)** — scope repair (R3): false for arbitrary Jacobian pairs
(`(f,g) = (x,y)` has `Γ ≡ 0`); the `Γ → ∞` limit needs `l_f, l_g ≥ 1`,
i.e. Lemma 2.1 scope (normalized counterexample). `Γ(0) =
1 − ord_x f − ord_x g ∈ {0,1}` is correct (`ord_x f + ord_x g ≤ 1` from
`J = 1`). "{Γ=0} is an interval containing 0" does **not** follow from
convexity alone (`|u−1|` is a convex counterexample); it is a consequence
of Theorem D's equality classification and belongs there.

### 3.4 Floor rigidity (producer Theorem D) — core sound, sign repair

Re-derived in full. For `u = q/p > 0` in lowest terms the minimal faces
are `x^A y^B Φ(τ)`, `x^C y^D Ψ(τ)`, `τ = x^q y^p`, and

```text
J(f_u^↓, g_u^↓) = x^{A+C−1} y^{B+D−1}
  [ (AD−BC) ΦΨ + (Ap−Bq) τ Φ Ψ' + (qD−pC) τ Φ' Ψ ]
```

(machine control TEST C, 40 random tuples). `Γ(u) = 0` forces the bracket
times the monomial to equal `1`; exponent counting kills `n ≥ 1`
survivors, leaves `A+C = B+D = 1` with `AD ≠ BC`, and the top bracket
coefficient `±(1 + p·degΨ + q·degΦ) ≠ 0` forces `Φ, Ψ` constant. Repaired
orientation statement (R4):

```text
(f_u^↓, g_u^↓) = (c₁x, c₂y) with c₁c₂ = 1,   or   (c₁y, c₂x) with c₁c₂ = −1.
```

Consequence `x | f` (resp. `x | g`): repaired step (R5) — `σ_f(u) = 1`
means `J − um ≥ 1` on all of `supp f`; a point `(0,m)` would give
`−um ≤ 0 < 1`. Then `Γ(0) = 0` and `{Γ = 0} = [0, u_max]` with the
producer's `u_max` bounds, at Lemma 2.1 scope. Extension (new, free): for
irrational `u > 0` the minimal face is a single lattice point on each
side, and the same classification holds with `Φ, Ψ` trivially constant —
so D covers every real `u > 0`.

### 3.5 Sibling floor identity (producer Theorem E) — sound with Sol's qualifiers

Immediate from Theorem B: floors depend only on `supp(h)` and the height,
and `π(F∗c) = π(F) + 1/κ` for every admissible `c`; the top-`ξ` part of
the shear is `c`-free (leading Taylor coefficients only). Qualifiers
adopted (R7): deeper-level equalities hold only where both towers exist at
a common height on the same lattice; `ρ` is compared only where C4 defines
it (`σ_f σ_g ≠ 0`); row-distance equality presupposes one `κ_F`; no
occurrence is supplied. It equates sibling *floors*, never positive-order
sibling values; the `1a602643...` §8.4 exhibit
(`v_{S₊,1} ≠ 0 = v_{S₋,1}`) survives verbatim, so Galois conjugacy of the
two evaluations remains unforced.

### 3.6 Degree floors (producer Theorem F) — sound, one prose repair

`deg_η f^F = deg_y f` (the `η^{l_f}` coefficient is
`f_{l_f}(x)x^{−l_f u} ≠ 0`), every `p_{f,j}` has `deg_η ≤ deg_y f`, and
`deg_η p_{f,F} = deg_η(λ_f p^i) = 68i` from the cell. With Lemma 2.1(iii)
`l_f ≤ k_f` and the corner monomial `f^+_{(1,1)} = ⊖x^{k_f}y^{l_f}`:

```text
l_f ≥ 68i,   k_f ≥ 68i,   deg f = k_f + l_f ≥ 136i          (no type input),
type (2,3):  l_g, k_g ≥ 102i,   deg g = (3/2) deg f ≥ 204i.
```

Repair R6: producer remark 2's first sentence must read "only the g-side
bounds need the type" (the theorem display and following sentence already
have the correct logic). The transposed `T_{x,a}` variant is safe as
stated (and can be sharpened by `+ l_f` trivially). The GGV22 comparison
is verified in *both* REDUCTION.md versions (§1.3), remains observation
only, and GGV22 stays non-load-bearing.

### 3.7 The two sibling evaluations vs independent generic coefficients

The reconstruction confirms the exact coupling status: (A3) makes
`v_{S_±,k} = [(η−c_±)^{i−k}]P_k` two evaluations of **one** parent family
`P_k` — they are not independent unknowns, and no formal jet is called a
source coefficient anywhere in this reconstruction (the wave packet's
prohibition). In the other direction, the window equations force no
additional relation at `k = 1` (the consumed §8.4 exhibit), and Theorem E
couples only the floor end of the family, which the value vectors do not
see. Both failure modes of the fallacy list — treating the vectors as
independent generics, and inventing a conjugacy/trace/norm lock — are
avoided.

### 3.8 Interfaces

Completion = Notation 3.9 (verified literal); coefficient functionals =
Statement 3.7(5); parent-to-child map = the corrected Statement 3.9
display (§3.1, closed form); the first-child vector *is* the child's own
top polynomial in the sense of Notation 3.10; `(V)` is tree-conditional
via Notation 3.8 with the Statement 3.18 root-of-unity twist; occurrence
is never claimed or used — every cell-specific statement is conditional on
a hypothetical normalized counterexample realizing the cell. No pair-only
constructor, occurrence theorem, source value, or uniform cap is inferred
anywhere.

## 4. The generic source translation, independently tested

For `c ∈ C` define `(f_c, g_c)(x,y) := (f, g)(x+c, y)`, i.e. composition
with `τ_c = (x+c, y) ∈ Aut(C²)` on the source (`𝔏`) side. Claims tested
one by one:

- **(T1) Jacobian.** `det Dτ_c = 1`, so
  `J(f_c,g_c) = J(f,g)∘τ_c = J(f,g)`; Keller condition and the `J = 1`
  normalization are preserved. Machine control TEST D.
- **(T2) Nonautomorphism.** `(f_c,g_c) = (f,g)∘τ_c` is bijective iff
  `(f,g)` is; counterexample-hood is preserved.
- **(T3) Almost normalized.** Same Notation 2.1 class (`τ_c` is an `𝔏`),
  and `deg f_c = deg f`, `deg g_c = deg g` (affine change), so
  lexicographic minimality is preserved.
- **(T4) Normalized leading type.** `supp f_c ⊆ {(r,m) : r ≤ J, (J,m) ∈
  supp f}`, so the Lemma 2.1 rectangles survive; the entire right edge
  `x^{k_f}y^m` coefficient column is unchanged (only `J = k_f`
  contributes), in particular the corner coefficient; likewise for `g`.
  Hence the same `(k_f,l_f,k_g,l_g)`, the same (i)–(iv), and the same
  type `(2,3)`. Since Notation 2.3 requires only *admitting* (i)–(iv)
  (§2 item 4), `(f_c,g_c)` is again a normalized counterexample of the
  same type. Machine control TEST D.
- **(T5) Tree and S17-cell transport.** Branches biject via
  `y_c(x) = y(x+c)`. In form (3), the coefficient at exponent height
  `j''/κ < 1` receives corrections only from heights `j''/κ − n`, `n ∈
  N*`, which are `< 0`: none exist. So **every** Puiseux coefficient at
  heights `< 1` is unchanged; contact orders `O(P,P*)` are unchanged
  (first-disagreement index is preserved by the triangular corrections);
  Puiseux characteristics, `ν_F`, `κ_F`, and `k̄_F` at heights `< 1` are
  unchanged; fibre values are unchanged. The S17 cell has
  `u = 1 − 13/κ_F < 1`, so its vertex, prefix, and height transport
  identically. Chart comparison at the cell: the prefix and `u` being
  equal, `h_c^{F_c}(x,η) − h^F(x,η) = Σ h_{Jm}[(x+c)^J − x^J](φ +
  ηx^{−u})^m`, and in particular the **top row is exactly invariant**:
  `d_{h_c,F_c} = d_{h,F}` and `p_{h_c,F_c} = p_{h,F}`. Hence `P_0 = λ_f
  p^i`, the reduced `p`, its roots `A, B_±`, the directions, `D_F`, `X`,
  `dp`, `dq`, `E`, `k̄` — the entire recorded tuple — transport with
  identical literal parameters, and (hypothetical) occurrence transports
  in both directions. Machine control TEST E.
- **(T6) Invariance range of the graded pieces (sharpened here).** The
  corrections decompose into an integer-drop family (re-expansion of
  `(x+c)^J` and of the `η`-scale), first touching the `κ_F`-lattice at
  graded offset `κ_F ≥ 17`, and a prefix-difference family at offset
  `k̄_F + κ_F j_min` where `j_min > 0` is the least positive prefix
  exponent (absent for a constant prefix). Both exceed `k̄_F = 13`, so
  the first possible mix on the integer lattice is at offset
  `min(κ_F, ⌈k̄_F + κ_F j_min⌉) ≥ 14`, and

  ```text
  P_k and G_k are translation-invariant for 0 ≤ k ≤ k̄_F = 13,
  ```

  on both sides, for every `c`. (TEST E exhibits the exact first-mix
  offset in a toy where the leading fractional term is killed by a
  constant top row — the bound is a floor, not the exact locus.)
  Consequently, when `i ≤ 13` (in particular at the transparency-minimal
  `i = 12`), the entire first-child value family `v_{S_±,k}`, `k = 0..i`,
  is translation-invariant; for `i ≥ 14` the entries with `k ≥ 14`
  transform by an explicit triangular map determined by `c` and the
  prefix.
- **(T7) Finite exceptional set and the σ-riders.** Writing
  `f = Σ_m f_m(x)y^m`, the corner makes `f_{l_f} ≠ 0 ≠ g_{l_g}`. For

  ```text
  c ∉ E := Z(f_{l_f}) ∪ Z(g_{l_g}),      |E| ≤ k_f + k_g,
  ```

  the coefficients of `x^0y^{l_f}` in `f_c` and `x^0y^{l_g}` in `g_c` are
  `f_{l_f}(c) ≠ 0`, `g_{l_g}(c) ≠ 0`. Hence `ord_x f_c = ord_x g_c = 0`
  **and**, for every `u > 0`, `σ_{f_c}(u) ≤ −u·l_f < 0` and
  `σ_{g_c}(u) ≤ −u·l_g < 0`, so C4's nonzero-σ rider is automatic at
  every positive height. Machine control TEST D (`(x−2) | f` correctly
  lands in `E`).

**Consequence.** In the translated representative, `Γ(0) = 1` and, by
Theorem D's contrapositive, `Γ(u) > 0` for every `u ≥ 0` — at every
vertex of every tree. The floor row is never the inhomogeneous Keller
row; the floor faces satisfy the C4 divisor homothety at every vertex.

**Serialization.** The single constant `c` determines the entire
transport (charts, trees, triangular corrections). Any future `PairRef`,
completion, or value vector frozen in a chosen gauge must carry: the
representative-choice statement (`(f,g) replaced by (f∘τ_c, g∘τ_c)`,
`c ∉ E`), the value of `c` over the declared coefficient field, and — if
values at graded offsets `≥ 14` are transported rather than recomputed —
the correction jets to the needed order. Two lanes touching one S route
state must share one recorded `c`; a silent per-lane "generic" choice
would break value-level comparability. No such value-level object exists
on the basis, so there is no present conflict.

## 5. `FLOOR-COORD` disposition

- **As the producer posed it** (decide `ord_x f = ord_x g = 0`, i.e.
  `Γ(0)`, for the fixed literal normalized pair): **OPEN and not
  derivable on the basis.** The producer's consistency scenario is
  re-verified: `f = x·f̃` forces `f̃(0,y)·g_y(0,y) ≡ 1`, so `g(0,y)` is
  affine and the fibre `{f = 0}` stays smooth with disjoint components —
  no easy contradiction; Lemma 2.1 never asserts `(0,m) ∉ N_f`.
- **As an S17 operational fork: CLOSED, WLOG, up to the explicit
  Aut-equivalence of §4.** `Γ(0)` is not an invariant of the
  counterexample — it is a property of the chosen representative, movable
  within the Notation 2.1/2.3 class by `τ_c` while every recorded S17
  object (cell tuple, `p`, `A`, `B_±`, charges, T1 template, window
  structure, `(E_s)`, and the graded pieces through offset 13) transports
  identically. Every recorded S17 consumer quantifies over "a hypothetical
  normalized counterexample realizing the cell", so the representative may
  be chosen with `ord_x f = ord_x g = 0` and both σ-riders. Sol's §4 is
  therefore **confirmed**, with the (T6) invariance range added and the
  serialization duty made precise.
- The producer's proposed descendant `TD12-S17-FLOOR-COORD/v1` should
  **not** launch: its outcome (a) (`Γ > 0` everywhere, floor always the
  C4 homothety) is delivered WLOG by §4; its outcome (b) is voidable by
  gauge choice and has no surviving consumer; deciding the literal
  question would settle a gauge label, not a route.
- What the WLOG does **not** do: pin `κ_F` or `u` (blocker B2 stands);
  supply any value `v_{S_±,k}`, `k ≥ 1`; supply occurrence, a `PairRef`,
  or a kill; make `ρ(u) = σ_g(u)/σ_f(u)` gauge-free (it is an invariant
  of the pair *together with* the recorded `c`).

## 6. Maximum safe S17 theorem (one statement)

> **Theorem S17\* (reconstructed source bridge, S route).** Let `(f,g)`
> be a normalized counterexample (Notation 2.3) with `J(f,g) = 1` (target
> scaling). Then:
>
> **(0) Gauge.** For every `c` outside the explicit finite set
> `E = Z(f_{l_f}) ∪ Z(g_{l_g})` (`|E| ≤ k_f + k_g`), the pair
> `(f_c,g_c) = (f,g)∘τ_c` is again a normalized counterexample of the
> same type with the same `(k_f,l_f,k_g,l_g)`; all Puiseux data at
> heights `< 1`, all contact orders, and every S17-cell datum (prefix,
> `u`, `κ_F`, `ν_F = 17`, `k̄_F = 13`, `p`, `A`, `B_±`, `D_F = 17i`,
> tops `P_0 = λ_f p^i`, `G_0 = c_g p^r`) transport identically, together
> with the graded pieces `P_k, G_k` for `0 ≤ k ≤ 13`; and
> `ord_x f_c = ord_x g_c = 0` with `σ_{f_c}(u), σ_{g_c}(u) < 0` for all
> `u > 0`.
>
> **(1) Shear.** At every vertex, descent is the single substitution
> `η ↦ c + ξη` on `(f^F, g^F)`; with `Q_c := ξ^n h^F(ξ, c+ξη)`,
> `ord_ξ Q_c = l = mult(p_{h,F}, c)`, the vanishing ladder
> `ord_c P_k ≥ l−k` is equivalent to St 3.9(iii) whenever `F∗c` is
> defined, and `p_{h,F∗c} = [ξ^l]Q_c` with coefficients
> `v_{c,k} = [(η−c)^{l−k}]P_k`; the Keller identity transports with the
> exact factor `ξ`, i.e. `u ↦ u + 1/κ`.
>
> **(2) Floor.** At every vertex the least chart exponent is `σ_h(u)` and
> the floor polynomial is `h_u^↓(1,η)` — independent of branch, fibre
> value, and prefix.
>
> **(3) Dichotomy.** For every real `u ≥ 0`:
> `σ_f(u) + σ_g(u) ≤ 1 − u`, and `J(f_u^↓, g_u^↓) = 1` if `Γ(u) = 0`,
> `= 0` if `Γ(u) > 0`. On the cell lattice the floor row of `(E_s)` sits
> `κ_F Γ(u)` rows below `s* = D_F + D_g − k̄_F`; when `Γ(u) = 0` the row
> at `s*` is the jet-free face identity `J(f_u^↓,g_u^↓) = 1`, which
> involves only the two floor polynomials and cannot be absorbed by any
> other graded data.
>
> **(4) Rigidity.** For `u > 0`, `Γ(u) = 0` iff
> `(f_u^↓, g_u^↓) = (c₁x, c₂y)`, `c₁c₂ = 1`, or `(c₁y, c₂x)`,
> `c₁c₂ = −1`; then `x` divides one member, `Γ(0) = 0`, and
> `{Γ = 0} = [0, u_max]`. If `Γ(u) > 0` and `σ_f σ_g ≠ 0`, the floor
> faces obey `κ_Fσ_f · div(p_{g,min}) = κ_Fσ_g · div(p_{f,min})`.
>
> **(5) Sibling floors.** The two `ν = 17` children (and the
> `A`-child) have identical floor data at every common height on the
> common lattice: `σ`, floor polynomial, `Γ`, and (where defined) `ρ`
> coincide on the nose. This couples only the floor end; it forces no
> relation among `v_{S_±,k}`, `k ≥ 1`, and no Galois conjugacy.
>
> **(6) Degree floors.** If a vertex `F ∈ T_{y,a}` realizes the sibling
> cell with full index `i`, then `deg_y f ≥ 68i`, `deg_x f ≥ 68i`,
> `deg f ≥ 136i`, and under type `(2,3)`: `deg g = (3/2)deg f ≥ 204i`
> (`deg_y g, deg_x g ≥ 102i`). Floors, not ceilings.
>
> **(7) Consequence in the gauge of (0).** `Γ(u) > 0` at every `u ≥ 0`,
> so the floor row is never the inhomogeneous Keller row and the case-(4)
> divisor homothety holds at every vertex; the `Γ = 0` compatibility of
> (3) is never cashable in WLOG coordinates, and the operational
> `FLOOR-COORD` fork is closed. Value-level data (`v_{S_±,k}`, `k ≥ 1`)
> remain open; any frozen value artifact must serialize the gauge
> constant `c` (§4, Serialization).

## 7. Material repairs (all required before promotion)

- **R1** (A2/A3 typing): state the ladder and extraction on
  `Q_c = ξ^n h^F(ξ, c+ξη)`; never write `ξ^l | h^F` for Laurent `h^F`.
- **R2** (C4 powers): integer exponents after clearing by `κ_F`; divisor
  form; no fractional polynomial powers.
- **R3** (C5 scope): normalized-counterexample scope (needs
  `l_f, l_g ≥ 1`); "interval contains 0" moves to Theorem D.
- **R4** (D orientation): `(c₁x, c₂y), c₁c₂ = 1` or `(c₁y, c₂x),
  c₁c₂ = −1`.
- **R5** (D's `x | f` step): argue via `J − um ≥ 1` at every support
  point; "taking m = 0" is not the argument.
- **R6** (F prose): "only the g-side bounds need the type".
- **R7** (E qualifiers): common height/lattice, `ρ` only where defined,
  no occurrence.
- **R8** (B endpoint): `u = 0` case holds trivially but needs its own
  sentence; S17 unaffected.
- **R9** (§4 Remark corner case): `σ_{h−a}(u) = min(σ_h(u),0)` fails
  when `h(0,0) = a`; immaterial to every use.
- **R10** (citation hygiene): Notation 3.9 is on p. 13; §0.1 heading
  miscounts three errata as two; the Prop 4.1 proof-line quote dropped
  the `⊖` glyph; `J = 1` is a normalization of Notation 1.3's
  `J(f,g) = ⊖`.

Custody repairs: re-seal under the sentinel-line convention; replace the
promoted short-id `c0c03d4e` by the full-file identifier `3595fb88...`
(true body `c4825be2...`); correct the `ladder/REDUCTION.md` charge to
`29270ff6...` at basis.

## 8. Exact blockers (none removed, one demoted)

- **B1** Ceiling caps: unchanged; `deg_y f` has floors (Theorem F) and no
  ceiling; the `1a602643...` §8.3 dimension counts stay quarantined per
  `876d1717...` §5.
- **B2** `κ_F` unpinned: `u = 1 − 13/κ_F`, `κ_F ∈ 17N`; neither `σ`
  values nor `Γ` are numerically evaluable. The §4 WLOG does not pin
  `κ_F`.
- **B3** `(V)` needs a real tree direction: Notation 3.8 requires a
  branch with `c_n = c`; Statement 3.18 adds the unique `ν_F`-th
  root-of-unity twist. Any descendant applying `(V)` must first discharge
  this.
- **B4** `[A, Prop 17.4]` is applied by the source only for `w` in the
  open positive quadrant; no upgrade of C4 to a full Newton-polygon
  homothety without obtaining its hypotheses.
- **B5** Occurrence: nothing here or in the producer proves the cell
  occurs; all cell statements are conditional.
- **B6** `s*` distance (demoted from a fork to a fact): in WLOG
  coordinates `Γ(u) > 0` always, the Keller row sits strictly between
  floor and ceiling, and the intermediate rows remain unavailable; the
  homogeneous cascade stays stopped (`97ba497f...`), and the only
  formal target remains `s*`.
- Former `FLOOR-COORD`: no longer a blocker (§5); replaced by the
  serialization duty of §4.

## 9. Machine controls (exact, stdlib `Fraction`, `/tmp` scratch only)

```text
/tmp/td12-s17-fable5-40c/check.py
TEST A  Theorem B floor: least exponent = σ_h(u), floor poly = minimal
        face, nontrivial 3-term prefix, u = 3/2                     PASS
TEST B  C1/C2 on the Jacobian pair (x+y², y+(x+y²)²) at 8 values of
        u, and on the identically-Γ=0 pair (x, y+x⁵) at 5 values    PASS
TEST C  Theorem D quasi-homogeneous bracket, 40 random tuples       PASS
TEST D  translation: J preserved; deg_x/deg_y and right-edge
        coefficient column preserved; rectangle preserved;
        (x−2)|f lands in the exceptional set                        PASS
TEST E  chart transport under translation: top row invariant; first
        differing graded offset = κ (integer-drop family) in a toy
        whose constant top kills the leading fractional term —
        consistent with the (T6) floor "invariant through k̄_F"      PASS
```

No conclusion rests on these controls alone; they guard the hand algebra
above.

## 10. Nonclaims

Not claimed, not implied: any value `v_{S_±,k}` or `v_{B,k}` for
`k ≥ 1`; a pair-only constructor; an occurrence theorem or witness; a
`PairRef`, completion instance, germ, landing, or counterexample; a
uniform support/degree cap or any ceiling; sibling independence *or*
forced conjugacy; any identification of the `ν=25` B and `ν=17` S states;
any route kill, `td` exclusion, exit price, charge, or flag (the reviewed
`4+4` and `8` are consumed, not re-derived; `charge_basis` absent); any
reopening of the homogeneous window cascade, EN/splice, or Avenue 27; any
JC2 conclusion in either direction; any software promotion or AWS
license. GGV22 remains exactly as recorded in `ladder/REDUCTION.md`
(both versions, §1.3): not load-bearing, no branch opened or closed.

## 11. Smallest nonduplicate descendant

```text
TD12-S17-WLOG-GAUGE-SERIALIZATION/v1      (desk, one output file)
  input   : this review §4–§6; the S17 cell constants (17, 13, k̄_F)
            only; no route data, no PairRef, no i, no occurrence.
  task    : (a) record the standing S17 gauge convention: statements may
            assume ord_x f = ord_x g = 0 and σ_f(u), σ_g(u) < 0 (u > 0)
            for a normalized representative, citing Theorem S17*(0);
            (b) amend the TD12-S17-SIBLING-PARENT-PAIRPACK/v1 input
            schema (876d1717 §6.2) with mandatory fields: gauge constant
            c over the declared field, exceptional-set certificate
            c ∉ Z(f_{l_f}) ∪ Z(g_{l_g}), and the invariance statement
            "P_k, G_k gauge-invariant for k ≤ 13; corrections serialized
            for k ≥ 14";
            (c) retire TD12-S17-FLOOR-COORD/v1 (never launched) and file
            the literal ord_x question as OPEN_NO_CONSUMER.
  outputs : one schema/convention packet; fail-closed states
            GAUGE_UNRECORDED, EXCEPTIONAL_SET_UNCERTIFIED,
            INVARIANCE_RANGE_EXCEEDED.
  cost    : desk. No CAS, no AWS, no new mathematics required.
```

The route-separated `TD12-S17-SIBLING-PARENT-PAIRPACK/v1` remains the
next *source* deliverable, now to be launched only with the amended
schema. The `ν=25` B analogue of Theorem F and of the §4 gauge remains a
separate lane and is deliberately not computed here.

## 12. Charged hashes (recomputed before reading and before sealing)

```text
3595fb88ef01fe72dce13cbb00b817a75a040f744764a8e34f865450c01b77d1  xmodel/td12-global-source-bridge-s-opus5-92e-20260829.md
1a6472f8ff8530cc77deee622160e3095fcf12e9c958ba5ac3d27a70fd339ac9  xmodel/td12-global-source-bridge-s-opus5-internal-audit-sol56-20260829.md
55920a2f659833106db79d2a3e338720d6576cac52e8e60f79a7c83432125413  xmodel/td12-global-source-bridge-s-opus5-different-model-review-fable5-40c-20260829.prompt.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
7af80df724d880a47452de96a731ff1c4e17b8244fdbae8fc76eb1461e7bcc22  xmodel/post1224-next-wave-packet-20260829T1335Z.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b  ladder/REDUCTION.md   (basis 40c1ab34 = basis 92ebe92a, blob c0dfd44a)
```

Also examined for §1.3 via `git cat-file` (not a working-tree read): blob
`038fdc95...` of `ladder/REDUCTION.md` at `76c746f6`, content SHA-256
`d409510a3df418f402a80cc954f646d35a054e9055783fadc0aaa234bb49b242`.
Hash-verified but not consumed:
`9677e2edf9848e81beac51cc9ed091c13cd934f912bc337b6ab8e25a5da86861`
(`xmodel/roundview-20260829T1335Z-92ebe92a.md`). Producer body pins
recomputed in §1.2. Frontier `FLOOR-COORD` mentions in `COORDINATION.md`,
`PROGRESS.md`, `AUDIT.md`, `notes.md` were located by grep to confirm this
review is the gate they name; none is a mathematical premise. The
`FALLACY-v2` guardrail was supplied in-conversation and applied; no
`charge_basis` line is declared because no exit price is asserted.

<!-- END-SEALED-BODY::td12-global-source-bridge-s-opus5-different-model-review-fable5-40c-20260829 -->

## Seal

Body = all bytes of this file strictly before the unique sentinel line
`<!-- END-SEALED-BODY::td12-global-source-bridge-s-opus5-different-model-review-fable5-40c-20260829 -->`
(sentinel chosen precisely to avoid the producer's self-referential
`## Seal` substring failure characterized in §1.2).

- Body byte count: `39244`.
- Body SHA-256:
  `e6f86217a33ab8bf5045bf9ced953f8eefb8bf0abd4fd9aa658f349b460fc7c0`.
- Frozen Git basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
