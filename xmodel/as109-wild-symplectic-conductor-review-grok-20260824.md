# Hostile different-model review — AS109 wild-symplectic completed-bidisc gate

| Field | Value |
|---|---|
| Claim under review | Frozen AS109 wild-symplectic first gate: on the completed unit bidisc an exact lift is finite étale of rank `p`; special Artin–Schreier translations lift uniquely to a free determinant-one restricted-analytic `C_p` action; unrestricted completed symplectic gauge is a single orbit; the first Witt digit is one divergence-free affine orbit with forced Cartier monomial `[x^{p-1} y] Q1 = 1`; the rational cotangent tower is a control, not a support lower bound |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below; the missing uniformly bounded polynomial-gauge category, and an algebraic boundary conductor, are correctly *not* claimed) |
| Evidence tier | independent commutative algebra of integral Tate algebras `Z_p⟨U,V⟩ → Z_p⟨x,y⟩` (injectivity by reduction, successive `p`-adic division without topological Nakayama, Jacobian criterion, Stacks 0ALJ/09ZL with hypotheses checked); independent first-digit PDE and Cartier-floor argument over `F_p[x,y]` and `F_p[[x,y]]`; a second sparse engine that does not import the producer replay; unmodified rerun of `cases/as109_wild_symplectic_gate_20260824/replay.py` as regression control only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T12:32:00Z – 2026-08-24T12:50:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256 `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`, matches the launch prompt)
- `cases/as109_wild_symplectic_gate_20260824/PREREGISTRATION.md` (SHA-256 `7a1cb33ac03676834adb6d490e1d5f6d31385818be64bd94eede177a18b38864`)
- `cases/as109_wild_symplectic_gate_20260824/replay.py` (SHA-256 `3c8d7d7c0c29d029f0d2bf098adb195f74e9ec85a097e9e9b97d231632bbc01e`)
- `cases/as109_wild_symplectic_gate_20260824/MANIFEST.sha256` (SHA-256 `34ba6939c8daa2c4a386eafdc96d27e457f801d5de631c739ff0b41e2fe91a8c`)

Reviewed AS109 Hensel/degree and `A_infinity` parent reports named by the replay manifest, same charged basis:

- `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` (SHA-256 `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133`) and different-model review `xmodel/as109-degree-cross-review-grok-20260824.md` (SHA-256 `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6`), overall **CONFIRMED**
- `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` (SHA-256 `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b`) and different-model review `xmodel/as109-ainfinity-review-grok-20260824.md` (SHA-256 `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76`), overall **CONFIRMED**

Named control lineage, consumed only as the cotangent representative and as the algebraization negative:

- `xmodel/witt-tate-control-20260824.md` (SHA-256 `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2`) and `xmodel/review-witt-tate-control-claude.md` (SHA-256 `b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2`)
- ideation card `xmodel/ideation-20260824T1205Z-event-synthesis.md` (SHA-256 `9adbbf0326610b455497e1bbefc43933bdb5cae7e3de9bb8f4ab5128deed9834`)

Stacks tags were read at the live pages, not trusted from the citation strings:

- Tag `0ALJ` (Lemma 15.11.4): if `A` is `I`-adically complete, then `(A,I)` is a henselian pair
- Tag `09ZL` (Lemma 15.13.2): for a henselian pair `(A,I)`, finite étale `A`-algebras are equivalent to finite étale `A/I`-algebras via `B ↦ B/IB`

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer, parent-review, and case artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No AWS call was made. The independent engine lived in `/tmp` and was not imported from the registered replay.

Write `p` an odd prime (the compiler samples `p=3,5`; the AS109 seed is `p=109`). Conditionally assume `F=(P,Q)` in `Z_p[x,y]^2` with `F mod p = (x-x^p,y)` and `det J(F)=1` as a polynomial identity. Existence is not inferred. Write `B=Z_p⟨U,V⟩`, `A=Z_p⟨x,y⟩` for the integral Tate algebras of restricted power series, and `α_F: B → A` the substitution `U ↦ P`, `V ↦ Q`. Angle brackets are restricted series: coefficients in `Z_p` tend to `0`. Equivalently

```text
Z_p⟨x,y⟩ = lim_n (Z/p^n Z)[x,y].
```

The predecessor theorems (both confirmed) supply `d=[K(x,y):K(P,Q)] ≥ p` and a residual factor `A_infinity` of rank `d-p` recording negative-valuation sheets. This gate's new content is the completed-bidisc torsor, the completed right-equivalence, and the first-digit Cartier floor.

---

## Promotion

**Accept `GAUGE-TRIVIAL/CONTROL-ONLY` at the stated first-gate scope.**

Under the conditional exact-lift hypothesis, and equally for any determinant-one restricted-analytic lift of the same special fibre:

- The substitution `B → A` is injective. Reduction modulo `p` is `F_p[x,y]` free of rank `p` over `F_p[x-x^p,y]` on `1,x,…,x^{p-1}`. Successive `p`-adic division, using completeness of `B`, torsion-freeness of `A`, and separatedness of `B`, lifts that basis. Topological Nakayama is not used and is not needed. Thus `A` is finite free of rank `p` over `B`, and `det J(F)=1` makes the map finite étale.
- `(B,pB)` is a henselian pair by `0ALJ`. Tag `09ZL` applies with no locality hypothesis on `B`. Special translations `(x,y) ↦ (x+a,y)` lift uniquely to `B`-automorphisms of `A`, the group law lifts, and the special torsor isomorphism lifts to an isomorphism of finite étale `B`-algebras. The three words *unique*, *free*, and *torsor* are separately justified. The chain rule gives `det J(τ_a)=1`.
- The action is restricted-analytic on the closed unit bidisc. It is not a rational or polynomial deck map, does not act on `A_infinity`, and does not prove `d=p`. No hidden completion-to-global step was found.
- Any two determinant-one restricted-analytic lifts with the same special fibre are right-equivalent by a unique `φ ≡ id (mod p)` with `F ∘ φ = G`, `φ` an automorphism, and `det J(φ)=1`. Finite truncations are polynomial over `Z/p^n`. Unrestricted completed cohomology therefore has one orbit; a uniformly bounded representative may still grow with depth.
- The first Witt digit is `N(a)=-1`, `N(b)=0`, `a_x+b_y=0`, `a=c-Δ(P1)`, `b=-Δ(Q1)`, `P1_x+Q1_y=x^{p-1}`, with the displayed signs. Solutions form one affine orbit under divergence-free right gauges. Map corrections and action corrections are related by those formulae, not independent.
- The coefficient `[x^{p-1} y] Q1 = 1` is forced for every first-digit solution, in or out of the registered `y ≤ 1` rectangle, and is invariant under all allowed first-digit gauges. It is a first-digit floor, not an unbounded-growth theorem.
- An independent engine recovers dimensions `16/6/10/10/0` at `p=3` and `24/10/14/14/0` at `p=5`, the displayed carries, the norm/order/determinant identities modulo `p^2`, and the cotangent supports through depths `2–4`. That representative is not minimal.

**Do not promote this to:** a global/rational/`A^2` deck action; `A_infinity=0`; `d=p`; a fixed-support exclusion; a theorem that every exact polynomial lift has unbounded support; a `p=109` computation; a lift construction; or any JC2 decision.

**Keep the successor as a new category, not a deeper unrestricted cohomology run.** The smallest valid successor is one of: (i) minimal support/degree *inside the unique completed orbit*, with a uniform bound on admissible polynomial gauges and compatibility across depth; (ii) an algebraic boundary conductor invariant under a specified bounded polynomial equivalence. Only a proof that those minima escape every fixed bound would close a fixed-support AS109 lift.

---

## Quarantine

No result here proves or disproves JC2. Producer JSON `verdict: GAUGE-TRIVIAL/CONTROL-ONLY` was not used as evidence for étaleness, `09ZL`, or the Cartier floor; those were re-derived. The registered replay is a first-digit compiler, not a checker of Henselian pairs. The completed `C_p` action lives on the integral unit bidisc and is compatible with the confirmed residual factor `A_infinity` of the global formal generic algebra; it is not the missing descent key of the `A_infinity` parent. Moskowicz, TDU at `td=109`, and the independent `deg_y ≤ 5` frontier are not consumed. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed identity `det J=1` that this gate consumes.

---

## Scope (not enlarged)

One odd prime in the analytic theorem; compiler primes `{3,5}` only; one seed `(x-x^p,y)`; exact coefficient ring `Z_p` for a hypothetical polynomial lift, or the restricted Tate algebra for completed lifts; the closed unit bidisc, not `A^2`. Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce. No construction, no `p=109` enumeration, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Substitution `Z_p⟨U,V⟩ → Z_p⟨x,y⟩` is injective. Reduction modulo `p` is `F_p[x,y]` free of rank `p` over `F_p[x-x^p,y]` on `1,…,x^{p-1}`. Successive division lifts that basis: completeness of `B`, torsion-freeness of `A`, and separatedness of `B` are the actual hypotheses, not topological Nakayama. Finite free plus `det J=1` gives finite étale | **CONFIRMED** | a nonzero restricted `f` with `f(P,Q)=0`; `T^p-T+U` failing to present `F_p[x]` over `F_p[U]`; a relation `∑ b_i x^i=0` with some `b_i` not in `∩ p^n B`; `p`-torsion in `A`; applying Nakayama to a module not known to be finitely generated; `B` failing to be noetherian, blocking finite presentation |
| 2 | `(B,pB)` is a henselian pair. `09ZL` is an equivalence, so each special translation lifts uniquely, the group law lifts, and the special torsor map lifts to an isomorphism. The action is a free constant-`C_p` torsor action, not a mere list of automorphisms | **CONFIRMED** | `B` not `p`-adically complete; `09ZL` requiring a local Henselian ring rather than a pair; special translations failing to be `B/pB`-algebra maps; Aut of the special fibre larger than `C_p`; the product isomorphism lifting only as a morphism, not an iso; “free” asserted from a list of automorphisms without the torsor map |
| 3 | Chain rule gives `det J(τ_a)=1` on the restricted bidisc. The action supplies neither a rational/polynomial deck map, an action on `A_infinity`, nor `d=p`. No hidden completion-to-global step | **CONFIRMED** | `det J(F)(τ_a)` a nonunit; coordinates of `τ_a` claimed to lie in `Z_p[x,y]` or `Q_p(x,y)`; the bidisc action identified with `Aut_M(L)`; residual negative-valuation sheets placed on the unit bidisc; a sentence asserting `d=p` from finite étale rank `p` of `A/B` |
| 4 | Multivariate Hensel (equivalently `09ZL` sections) gives a unique `φ ≡ id (mod p)` with `F ∘ φ = G`. It is an automorphism of determinant one. Uniqueness applies to the inverse equations in the identity residue class. `Z_p⟨x,y⟩/p^n = (Z/p^n)[x,y]` in the exact sense used. Honest conclusion: one unrestricted completed gauge orbit; uniformly bounded representatives may still grow | **CONFIRMED** | composition order `φ ∘ F = G` treated as right equivalence; a second identity-residue solution of `F(H)=F`; `det J(φ)` only a unit, not `1`; restricted series with infinitely many coefficients nonzero modulo `p^n`; raw finite-depth support sold as an invariant of the completed orbit |
| 5 | Independently: `N(a)=-1`, `N(b)=0`, `a_x+b_y=0`, `a=c-Δ(P1)`, `b=-Δ(Q1)`, `P1_x+Q1_y=x^{p-1}`, with `c=((x+1)^p-x^p-1)/p mod p`. All first-digit solutions form one affine orbit under exactly the allowed divergence-free right gauges. Map corrections and action corrections are conjugate, not two cohomologies | **CONFIRMED** | `τ^p(x)=x+p(1+N(a))` with the wrong additive `1`; `c` missing the `-1` in the numerator; `a=Δ(P1)-c`; Keller row `P1_x+Q1_y=-x^{p-1}`; a first-digit solution not differing from the cotangent control by a divergence-free pair |
| 6 | `[x^{p-1} y] Q1 = 1` for every first-digit solution, including outside `y ≤ 1` and under all allowed gauges. Characteristic-`p` differentiation, higher `y` rows, and polynomial versus formal primitives supply no loophole. First-digit floor, not unbounded growth | **CONFIRMED** | `P1_x` contributing to `x^{p-1}` from an `x^p` term; a `y ≥ 2` term contributing to the `y^0` row of `Q1_y`; a divergence-free pair with `[x^{p-1} y] s ≠ 0`; the floor promoted to a depth-uniform support theorem |
| 7 | Independent engine at `p=3,5`: dimensions `10/10/0` and `14/14/0`, displayed carries, norm/order/determinant identities modulo `p^2`, cotangent tower depths `2–4` with the displayed supports. That representative is not minimal | **CONFIRMED** | affine dimension not equal to the kernel dimension; Cartier coefficient not a pivot of value `1`; `c` different from `x+x^2` or `x+2x^2+2x^3+x^4`; cotangent Jacobian not `1-p^n x^{n(p-1)}`; the tower sold as a minimal-orbit support law |
| 8 | `GAUGE-TRIVIAL/CONTROL-ONLY` is the exact admissible result. Global deck action, `A_infinity=0`, fixed-support exclusion, `p=109` brute force, lift construction, and JC2 stay quarantined. Smallest successor is a uniformly bounded polynomial-gauge category or an algebraic boundary conductor | **CONFIRMED** | the gate concluding `CONTRADICTION` or `FINITE-MIXED-CLASS`; unrestricted deeper cohomology licensed as an invariant; a global deck or `d=p` inference; a `p=109` run licensed by the first-digit floor |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a sign, a forced coefficient, or a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | prompt, `MANIFEST.sha256`, and replay `input_sha256` not applicable (producer is an output of the freeze) |
| `cases/as109_wild_symplectic_gate_20260824/PREREGISTRATION.md` | `7a1cb33ac03676834adb6d490e1d5f6d31385818be64bd94eede177a18b38864` | prompt and `MANIFEST.sha256` |
| `cases/as109_wild_symplectic_gate_20260824/replay.py` | `3c8d7d7c0c29d029f0d2bf098adb195f74e9ec85a097e9e9b97d231632bbc01e` | prompt and `MANIFEST.sha256` |
| `cases/as109_wild_symplectic_gate_20260824/MANIFEST.sha256` | `34ba6939c8daa2c4a386eafdc96d27e457f801d5de631c739ff0b41e2fe91a8c` | prompt |
| `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` | `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` | replay `input_sha256` |
| `xmodel/as109-degree-cross-review-grok-20260824.md` | `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6` | replay `input_sha256` |
| `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` | `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` | replay `input_sha256` |
| `xmodel/as109-ainfinity-review-grok-20260824.md` | `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76` | replay `input_sha256` |
| `xmodel/witt-tate-control-20260824.md` | `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2` | replay `input_sha256` |
| `xmodel/review-witt-tate-control-claude.md` | `b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2` | replay `input_sha256` |
| `xmodel/ideation-20260824T1205Z-event-synthesis.md` | `9adbbf0326610b455497e1bbefc43933bdb5cae7e3de9bb8f4ab5128deed9834` | replay `input_sha256` |

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_wild_symplectic_gate_20260824/replay.py
```

Exit code 0. JSON `verdict` is `GAUGE-TRIVIAL/CONTROL-ONLY`. Stdout SHA-256 `5b69df7db6a68e9f5652dd4be2ebac4bcb1c5ed96f5f4d826164a1f7cc4b86f1`. The script writes no files.

The registered program is a finite first-digit / cotangent-control suite, not a checker of `0ALJ`, of `09ZL`, of injectivity of Tate substitution, or of the Cartier identity outside its rectangle. It samples only `p in {3,5}` and depths `{2,3,4}`. Those Booleans were discarded as evidence for the étale/torsor/floor claims; every numbered claim below is re-derived independently. Process remark, non-blocking: `linear_window` sets `"affine_mod_gauge_dimension": 0` by writing the constant `0` after identifying the gauge kernel with the nullspace of the same divergence matrix. That identification is mathematically correct (claim 5); it is not an independent cohomology computation.

A second engine, written for this review and not imported from the registered script, used only `math.comb` and integer dictionaries, with a reversed-column Gauss elimination and `Q1`-first / `y`-major monomial order. It recorded zero failures on: special-fibre reduction of `x^n` for `n ≤ 3p+1` at `p=3,5,7`; vanishing of `X^p-X+U` at `U=x-x^p`; first-digit identities (4.1)–(4.3) and invariance/determinants modulo `p^2` for the cotangent control; binomial carries; `N(c)=-1` by evaluation at `0`; closed-form window dimensions `2p+4` free / rank `2p`; registered dimensions `(16,6,10)` and `(24,10,14)`; Cartier forced on every solvable window with `1 ≤ y ≤ 5` and `x ≤ p+y` at `p=3,5,7`; inconsistency of the `y=0` window; cotangent Jacobians `1-p^n x^{n(p-1)}` through depth `5`; restricted-series truncation `Z_p⟨x⟩/p^n = (Z/p^n)[x]` on the geometric series `∑ p^j x^{j(p-1)}`; and first-digit right-equivalence `F ∘ φ = G` for a divergence-free gauge, with two-sided inverse modulo `p^2`.

Scratch engine SHA-256 `8bcbc2c534383a2ab9fe16e099ee4a1e42febe380b445264b7140de0f87bc8b3` (outside the repository; not a freeze input).

---

## Independent recomputation

### 1. Tate-algebra map and basis — CONFIRMED

Assume the exact-lift hypothesis, or more generally a pair `F=(P,Q)` in `A^2` with Gauss norm `≤ 1`, `F ≡ (x-x^p,y) (mod p)`, and `det J(F)=1`. Polynomials with `Z_p` coefficients have Gauss norm `≤ 1`, so substitution of restricted series in `U,V` at `(P,Q)` lands in `A`. The structure map `α_F: B → A` exists.

Injectivity, independently of freeness. Suppose `f(P,Q)=0` with `f ∈ B`. Reduce modulo `p`: the image in `F_p[x,y]` is `f̄(x-x^p,y)=0`. The elements `x-x^p` and `y` are algebraically independent over `F_p`, so `f̄=0` and `f ∈ pB`. Torsion-freeness of `A` (coefficients in the domain `Z_p`) gives `f_1(P,Q)=0` with `f=p f_1`. Iterate. Separatedness `∩_n p^n B = 0` forces `f=0`.

Special fibre. Restricted series modulo `p` are polynomials:

```text
A/pA = F_p[x,y],     B/pB = F_p[U,V],
```

and `α_F` reduces to `U ↦ x-x^p`, `V ↦ y`. Set `g=x-x^p`. Then `x` satisfies the monic relation `T^p - T + g = 0`. Polynomial division by this monic polynomial writes every element of `F_p[x]` uniquely as `∑_{i=0}^{p-1} b_i(g) x^i`. Linear independence over `F_p(g)` is the degree-`p` minimal polynomial (derivative `-1 ≠ 0`, so separable Artin–Schreier). Base change along `F_p[g] → F_p[g,y]` gives

```text
F_p[x,y] ≅ F_p[U,V][X] / (X^p - X + U),     X ↦ x, V ↦ y,
```

free of rank `p` on `1,x,…,x^{p-1}`. This is (1.1). The second engine reduced `x^n` via `x^p = x-g` through `n ≤ 3p+1` at `p=3,5,7` and reconstructed `x^n`.

Spanning before reduction, without topological Nakayama. Let `f ∈ A`. Its reduction in `F_p[x,y]` expands uniquely as `∑_{i=0}^{p-1} b̄_i x^i` with polynomial coefficients `b̄_i ∈ F_p[U,V]`. Lift those finitely many coefficients arbitrarily to `b_i^{(0)} ∈ Z[U,V] ⊂ B`. Then `f - ∑ b_i^{(0)} x^i` lies in `pA`. Torsion-freeness puts `f_1 := p^{-1}(f - ∑ b_i^{(0)} x^i)` in `A`. Iterate. The series `b_i = ∑_{k ≥ 0} p^k b_i^{(k)}` is `p`-adically Cauchy in `B`. Completeness of `B` (equivalently `B = lim (Z/p^n)[U,V]`) supplies the limit. For each `n` only the terms `k < n` matter modulo `p^n`, and each `b_i^{(k)}` is a polynomial, so `b_i` is restricted. The identity `f = ∑_i b_i x^i` is the `p`-adic limit in the complete ring `A`. Finite generation of `A` as a `B`-module is the output of this construction, not an input. Topological Nakayama (a finitely generated module over a complete ring, or a complete finitely generated module) is therefore not applicable a priori and is not used.

Independence. If `∑_{i=0}^{p-1} b_i x^i = 0` in `A`, special-fibre independence gives every `b_i ∈ pB`. Divide the relation by `p` in the torsion-free ring `A` and repeat. Then each `b_i` lies in `∩_n p^n B`. Separatedness of the `p`-adic filtration on `B` gives `b_i=0`.

Thus `A` is finite free of rank `p` over `B` on `1,…,x^{p-1}`. In particular `A = B[x]` as a `B`-algebra, with `y` the unique `B`-linear combination of those powers. Finite free implies faithful, recovering injectivity.

Finite presentation and étaleness. The ring `B = Z_p⟨U,V⟩` is noetherian (Tate; equivalently, Weierstrass preparation for restricted series over a complete DVR). A finite type algebra over a noetherian ring is of finite presentation (Stacks Tag `00FP`(3)). Module-finiteness supplies finite type, hence finite presentation as an algebra. Relative Kähler differentials: `P` and `Q` are the images of `U` and `V`, so `dP = P_x dx + P_y dy = 0` and `dQ = 0` in `Ω_{A/B}`. These are algebraic identities (polynomial Leibniz). The matrix of the two relations is `J(F)`, of determinant `1`, hence invertible over `A`, so `dx=dy=0` and `Ω_{A/B}=0`. Finite, finitely presented, flat (free), and unramified (`Ω=0`) is finite étale. Because `A` is already module-finite, there is no escape into the “huge algebraic Kähler module of a Tate algebra over `Z_p`”: `Ω_{A/B}` is a finitely generated `A`-module, and here it vanishes.

The same argument applies verbatim to a restricted-analytic lift, not only a polynomial one: the special fibre and the identity `det J=1` are all that enter.

### 2. Étaleness and torsor lifting — CONFIRMED

Henselian pair. The ring `B` is `p`-adically complete. Tag `0ALJ` states: if `A` is `I`-adically complete, then `(A,I)` is henselian. Taking `A=B` and `I=pB`, the pair `(B,pB)` is henselian. The tag does not require `B` local and does not require `I` to be a maximal ideal. The cited proof uses only `A = lim A/I^n` and successive lifting of coprime monic factorizations.

Finite-étale equivalence. Tag `09ZL` states: for a henselian pair `(A,I)`, the functor `B ↦ B/IB` is an equivalence between finite étale `A`-algebras and finite étale `A/I`-algebras. Fully faithfulness is proved by matching morphisms with idempotents of the tensor product and uniquely lifting those idempotents (Tag `09XI`); essential surjectivity produces a finite étale lift of any finite étale special algebra. The pair here is `(B,pB)`. The algebra `A` is finite étale over `B` by claim 1, so the functor applies to it. No extra finiteness, no locality, and no “Henselian local ring” hypothesis is missing.

*Unique.* Special automorphisms `τ̄_a: (x,y) ↦ (x+a,y)` for `a ∈ F_p` are `B/pB`-algebra automorphisms of `A/pA`: they fix `y` and send `x-x^p` to `(x+a)-(x+a)^p = x-x^p`, using `a^p=a`. Fully faithfulness of `09ZL` gives a unique `B`-algebra automorphism `τ_a` of `A` reducing to `τ̄_a`. The special group law `τ̄_a ∘ τ̄_b = τ̄_{a+b}` therefore lifts: both `τ_a ∘ τ_b` and `τ_{a+b}` reduce to the same special automorphism, so they coincide. In particular `τ_1^p = id` as automorphisms of `A`, not merely modulo `p^2`. Uniqueness is uniqueness of morphisms in the finite-étale category over `B`, not uniqueness among arbitrary ring automorphisms of `A`.

The special automorphism group is exactly `C_p`, not larger: any `F_p[U,V]`-automorphism of `F_p[x,y]` must send `x` to another root of `T^p-T+U`, and those roots are precisely `x+a` for `a ∈ F_p`, all already in `F_p[x]`. Thus `Aut_B(A) ≅ Aut_{B/pB}(A/pA) ≅ C_p`.

*Torsor.* The special map of finite étale `B/pB`-algebras

```text
A/pA  ⊗_{B/pB}  A/pA   →   ∏_{a ∈ F_p} A/pA,
      f ⊗ g          ↦   (f · τ̄_a(g))_a
```

is an isomorphism because `F_p[x]/F_p[x-x^p]` is the Galois `C_p`-cover given by Artin–Schreier translations, and adjoining `y` is a base change. Both source and target already exist as finite étale `B`-algebras (`A ⊗_B A` is finite étale over `B`; a finite product of copies of `A` is finite étale over `B`). Fully faithfulness lifts the special isomorphism uniquely to a `B`-algebra morphism, and lifts the inverse; uniqueness of the identity morphism implies the lift is an isomorphism. Essential surjectivity of `09ZL` is not required for this step.

*Free.* For a finite constant group scheme, that isomorphism is the definition of a `G`-torsor over `Spec B`: equivalently, `C_p × Spec A → Spec A ×_{Spec B} Spec A` is an isomorphism, which is freeness plus transitivity. Freeness is not inferred from “a list of `p` automorphisms”. The group scheme is the constant group `Z/pZ` over `Spec B`, because the labels `a ∈ F_p` and the lifted group law are the constant group law.

The producer’s wording “free constant-`C_p` torsor action on the completed bidisc, not merely a list of automorphisms” therefore survives the three-word attack.

### 3. Symplectic determinant and firewall — CONFIRMED

Chain rule, recomputed. The identity `F ∘ τ_a = F` is the statement that `τ_a` is a `B`-algebra automorphism. Differentiating,

```text
J(F)(τ_a) · J(τ_a) = J(F).
```

Taking determinants and using `det J(F)=1` as an identity in `A` (polynomial, or restricted) gives `det J(τ_a)=1`. There is no unit-versus-one gap: the identity is `1 · det J(τ_a) = 1`.

Firewall. Coordinates of `τ_a` lie in `A = Z_p⟨x,y⟩` by construction. They need not lie in `Z_p[x,y]` or in `Q_p(x,y)`. The cotangent control of claim 7 exhibits an explicit generator

```text
τ(x,y) = (t,  y g'(t)/g'(x)),
```

where `t` is the unique restricted root of `g(t)=g(x)` congruent to `x+1` and `g=x-x^p`. Differentiating `g(t)=g(x)` gives `t' = g'(x)/g'(t)`, so the `y`-factor `g'(t)/g'(x)` is exactly the unique choice making `det J(τ)=1`. This is a rational expression in `t`, and `t` itself is restricted-analytic, not polynomial (the Newton polygon of `g(T)-g(x)` at the residue `x+1` produces an infinite Witt tower). The same formula is the inverse limit of the finite cotangent maps. It is a valid symplectic deck map on the unit bidisc and is not an algebraic endomorphism of `A^2`.

No action on `A_infinity`. The confirmed parent splitting

```text
L ⊗_M E  ≅  E^p × A_infinity
```

records residual geometric roots of negative source valuation, i.e. points off the integral unit bidisc. The Tate algebra `A` sees only the closed unit bidisc. A `B`-automorphism of `A` cannot move those residual sheets. Compatibility with `d ≥ p` and with a possibly nonzero `A_infinity` is exact.

No hidden completion-to-global step was found. Finite étale rank `p` of `A` over `B` is a statement about functions on the unit bidisc. The global generic degree `d` counts all geometric sheets of `A^2 → A^2`, including residual and polar ones. The producer never identifies the two. The `A_infinity` parent’s descent key — a rational element of `Aut_M(L)` acting as the displayed `p`-cycle — is not supplied by `09ZL` on Tate algebras.

### 4. Completed right-equivalence — CONFIRMED

Let `F` and `G` be determinant-one restricted-analytic lifts of the same special map. Solve `F(X,Y)=G(x,y)` in `A^2` with `(X,Y) ≡ (x,y) (mod p)`.

The special Jacobian of either lift is `I_2`: `∂(x-x^p)/∂x = 1-p x^{p-1} ≡ 1 (mod p)` and `∂y/∂y=1`. At the initial point `(x,y)` one has `F(x,y) ≡ G(x,y) (mod p)` and `det J(F)(x,y)=1`, a unit. The ring `A` is `p`-adically complete, so the pair `(A,pA)` is henselian by `0ALJ`. Multivariate Hensel (Newton iteration `b_{n+1}=b_n - J(F)^{-1}(F(b_n)-G)`, which stays in `A` because `det J(F)=1` supplies an everywhere inverse) produces a unique solution `φ=(X,Y)` in the identity residue class.

Equivalently, by `09ZL`: both structure maps `α_F, α_G: B → A` make `A` finite étale over `B` with the same special fibre, so the identity of `A/pA` is a map of `B/pB`-algebras from `(A,F)` to `(A,G)` and lifts uniquely to a `B`-algebra map `φ: (A,F) → (A,G)`. In space language, `φ(f)=f ∘ φ_space`, and `φ ∘ α_F = α_G` is `F ∘ φ_space = G`. Composition order is right equivalence.

Reverse `F` and `G` to obtain `ψ` with `G ∘ ψ = F` and `ψ ≡ id (mod p)`. Then `F ∘ (φ ∘ ψ) = F` and `F ∘ id = F`, both in the identity residue class, so uniqueness gives `φ ∘ ψ = id`. Similarly `ψ ∘ φ = id`. Thus `φ` is an automorphism of `A`. Uniqueness of the inverse equations is the same uniqueness, applied to `F(H)=F` and to `G(H)=G` in the identity class; it is not a separate lemma with weaker hypotheses.

Determinants in `F ∘ φ = G` give `det J(F)(φ) · det J(φ) = det J(G)`, hence `det J(φ)=1`.

Equation (3.3). By definition, a restricted series has coefficients tending to `0` in `Z_p`, so for each `n` only finitely many coefficients are nonzero modulo `p^n`, and those form a polynomial over `Z/p^n`. Conversely, a compatible system of polynomials over `Z/p^n` is a restricted series. This is the exact identification used: every finite truncation of `φ` is a polynomial map over `Z/p^n` of Jacobian determinant `1`, and the inverse truncation is likewise a polynomial. Support of those truncations need not be bounded independently of `n`. The second engine checked the geometric series `∑ p^j x^{j(p-1)}` has, modulo `p^n`, precisely the terms `j < n`.

Honest conclusion. The completed symplectic gauge groupoid on determinant-one restricted-analytic lifts of the fixed special fibre is transitive, with unique near-identity arrows. Unrestricted completed cohomology therefore has a single orbit. A finite-depth support statistic of a representative is not an invariant of that orbit. A uniformly bounded polynomial representative of the same orbit is a different, still-open problem; the cotangent tower shows that at least one representative grows linearly in depth, and does not show that every representative does.

### 5. First Witt digit — CONFIRMED

Write `τ(x,y)=(x+1,y)+p(a,b)` modulo `p^2`, with `a,b ∈ F_p[x,y]`, and

```text
Δf = f(x+1,y)-f(x,y),     Nf = ∑_{i ∈ F_p} f(x+i,y).
```

Iteration modulo `p^2`. One has `a(τ(x),τ(y)) ≡ a(x+1,y) (mod p)`, so

```text
τ^k(x) = x + k + p ∑_{i=0}^{k-1} a(x+i,y)  (mod p^2),
τ^k(y) = y + p ∑_{i=0}^{k-1} b(x+i,y)      (mod p^2).
```

At `k=p`, using `τ^p = id` exactly from claim 2,

```text
x + p(1+N(a)) ≡ x,     y + p N(b) ≡ y  (mod p^2),
```

hence `N(a)=-1` and `N(b)=0` in `F_p[x,y]`. The additive `1` is the sum of the special translations and is not optional.

Jacobian of `τ` modulo `p^2`:

```text
J(τ) = [[1+p a_x, p a_y],[p b_x, 1+p b_y]],
det J(τ) = 1 + p(a_x+b_y).
```

The identity `det J(τ)=1` forces `a_x+b_y=0`.

Carry polynomial. Over `Z[x]`,

```text
(x+1)^p - x^p - 1 = ∑_{k=1}^{p-1} binom(p,k) x^k
```

is divisible by `p` but, for `0<k<p`, not by `p^2`. Reducing

```text
c(x) = ((x+1)^p - x^p - 1)/p
```

modulo `p` yields `c ∈ F_p[x]`. Directly: `binom(p,k)/p = (p-1)⋯(p-k+1)/k!`. This produces `c=x+x^2` at `p=3` and `c=x+2x^2+2x^3+x^4` at `p=5`.

Invariance `F ∘ τ = F` modulo `p^2`. Write `P=x-x^p+p P1` and `Q=y+p Q1`. Then `(x+1+p a)^p ≡ (x+1)^p (mod p^2)`, so

```text
P(τ)-P = p(a - c + Δ(P1))  (mod p^2),
Q(τ)-Q = p(b + Δ(Q1))      (mod p^2).
```

Vanishing gives `a = c - Δ(P1)` and `b = -Δ(Q1)`. Signs match the producer.

Keller row. Expanding `det J(F)` modulo `p^2`:

```text
P_x = 1 - p x^{p-1} + p P1_x,   Q_y = 1 + p Q1_y,
det = 1 + p(P1_x + Q1_y - x^{p-1}).
```

The identity `det=1` forces `P1_x+Q1_y = x^{p-1}`.

Compatibility. Differentiating the integral formula for `c` gives `c_x = Δ(x^{p-1})` as an identity over `Z`. Then

```text
a_x + b_y = c_x - Δ(P1_x) - Δ(Q1_y) = Δ(x^{p-1}) - Δ(P1_x+Q1_y) = 0,
```

using that `Δ` commutes with partials. Telescoping over `Z`,

```text
∑_{i=0}^{p-1} ((x+i+1)^p - (x+i)^p - 1) = (x+p)^p - x^p - p,
```

and `(x+p)^p = x^p + p^2(⋯)`, so `N(c) ≡ -1 (mod p)`. Also `NΔ = 0` because translation by `p` is the identity on `F_p[x,y]`. Thus (4.2) and (4.3) imply (4.1).

Gauges versus map corrections. A source change `φ = id + p(r,s)` with `r_x+s_y=0` has `φ^{-1} = id - p(r,s)` modulo `p^2`. Conjugation of the action is

```text
φ^{-1} ∘ τ ∘ φ = (x+1,y) + p(a - Δ(r), b - Δ(s)).
```

Replacing `(P1,Q1)` by `(P1+r,Q1+s)` changes `(a,b)` by `(-Δ(r),-Δ(s))` via (4.2). Differences of solutions of the linear equation (4.3) are exactly the pairs with vanishing divergence. The first-digit solution space is therefore a torsor under the first-digit symplectic gauges: one affine orbit. Map corrections (`P1,Q1`) and action corrections (`a,b`) are two presentations of the same affine space, related by (4.2), not two independent cohomologies.

Precision, non-blocking. Once gauges are identified with `ker(div)` on the same coefficient window, “quotient dimension `0`” is the tautology that an affine space modulo its translation space is a point. The load-bearing first-digit content is solvability of (4.3) and the Cartier floor of claim 6, not a mysterious vanishing of mixed classes. The producer’s wording “one affine gauge orbit” and “no genuinely mixed gauge class” is the tautology stated honestly, not a computational discovery of a hidden invariant.

### 6. Forced support floor — CONFIRMED

Look at the coefficient of the monomial `x^{p-1}` (i.e. `y^0`) in (4.3), working in characteristic `p`, for an arbitrary pair of polynomials or formal series `(P1,Q1)`.

A monomial `x^i y^j` in `P1` contributes `i x^{i-1} y^j` to `P1_x`. Matching `x^{p-1}` requires `i=p` and `j=0`, with coefficient `p=0`. Every `x^p y^j` term likewise contributes `0`. Thus `P1_x` cannot contribute to `x^{p-1}`.

A monomial `x^i y^j` in `Q1` contributes `j x^i y^{j-1}` to `Q1_y`. Matching `x^{p-1} y^0` requires `i=p-1` and `j-1=0`, hence `j=1`, with coefficient `1`. Higher `y` rows produce positive powers of `y`. In characteristic `p`, `∂_y(y^{1+p m}) = y^{p m}`, never `y^0` for `m ≥ 1`. Thus

```text
[x^{p-1} y] Q1 = 1
```

is forced, with no contribution from any other monomial, in `F_p[x,y]` and in `F_p[[x,y]]` alike. Restricted series have the same monomial-wise derivatives.

Gauge invariance. For `r_x+s_y=0`, the coefficient of `x^{p-1}` is `[x^{p-1} y] s`, because `r_x` again cannot produce `x^{p-1}`. The homogeneous equation therefore forces `[x^{p-1} y] s = 0`. No allowed first-digit gauge moves the Cartier coefficient.

The `y=0` window is inconsistent: `Q1_y=0` and `P1_x` still cannot supply `x^{p-1}`. So the floor is not an artifact of truncating at `y=1`; omitting `y` makes (4.3) unsolvable. The registered rectangle is the smallest one containing both the cotangent control `Q1=x^{p-1} y` and the unavailable formal `x`-primitive `x^p/p` (which is not an element of `F_p[x]`, and whose characteristic-`0` avatar `x^p/p` is not integral).

Polynomial versus formal primitives. An `x`-primitive of `x^{p-1}` is `x^p/p`, not integral. A `y`-primitive is `x^{p-1} y`, which is integral and is the forced term. Adding a closed form is adding a gauge, which cannot cancel the coefficient.

This is a statement about the first Witt digit of every integral (or restricted-analytic) lift. It is not a theorem that polynomial support of an exact lift is unbounded, and it is not a depth-uniform lower bound on higher digits. The producer keeps that distinction.

The second engine forced the Cartier coefficient on every solvable window with `1 ≤ ymax ≤ 5` at `p=3,5,7`, including `xmax = p+ymax`, and recorded inconsistency at `ymax=0`.

### 7. Independent finite compiler / control — CONFIRMED

Registered window: `0 ≤ deg_x ≤ p`, `0 ≤ deg_y ≤ 1` independently in `P1,Q1`. That is `4(p+1)` variables.

Closed form, not the producer’s RREF. Write `P1 = ∑_{i=0}^p (A_i + B_i y) x^i` and `Q1 = ∑_{i=0}^p (C_i + D_i y) x^i`. In `F_p`,

```text
P1_x = ∑_{i=1}^{p-1} i (A_i + B_i y) x^{i-1},
Q1_y = ∑_{i=0}^p D_i x^i.
```

The equation `P1_x+Q1_y = x^{p-1}` becomes:

- `i A_{i+1} + D_i = 0` for `i=0,…,p-2` (`i+1` invertible);
- `D_{p-1} = 1` (Cartier);
- `D_p = 0`;
- `i B_i = 0` for `i=1,…,p-1`, hence `B_1=⋯=B_{p-1}=0`;
- `B_p` is killed by `p=0` and is free.

Free variables: `A_0,A_p,B_0,B_p`, all `p+1` of the `C_i`, and `D_0,…,D_{p-2}`. Count: `2p+4`. Rank: `4p+4-(2p+4)=2p`. Affine dimension equals kernel dimension. Cartier is a pivot of value `1`.

| `p` | variables | rank | affine = kernel | quotient | Cartier |
|---:|---:|---:|---:|---:|---|
| 3 | 16 | 6 | 10 | 0 | `D_2=1` |
| 5 | 24 | 10 | 14 | 0 | `D_4=1` |
| 7 | 32 | 14 | 18 | 0 | `D_6=1` (extra, not registered) |

Hand row reduction at `p=3` is the six equations `A_1+D_0=0`, `2A_2+D_1=0`, `D_2=1`, `D_3=0`, `B_1=0`, `2B_2=0`. At `p=5` the ten equations are `A_1+D_0=0`, `2A_2+D_1=0`, `3A_3+D_2=0`, `4A_4+D_3=0`, `D_4=1`, `D_5=0`, and `B_1=B_2=B_3=B_4=0`. The independent reversed-column engine reproduced the same ranks and the forced coefficient, with `Q1` ordered first.

Carries, independently: `binom(3,1)/3=1`, `binom(3,2)/3=1`; `binom(5,k)/5` for `k=1,2,3,4` equals `1,2,2,1`. Cotangent control `P1=0`, `Q1=x^{p-1} y` lies in the window and satisfies (4.3). First-digit action for that control: `a=c`, `b=-Δ(x^{p-1} y)`. The engine checked `N(a)=-1`, `N(b)=0`, `div(a,b)=0`, `F ∘ τ = F` modulo `p^2`, and both Jacobians equal to `1` modulo `p^2`, at `p=3,5,7`.

Cotangent tower. Over `Z`, `S_n = ∑_{j=0}^{n-1} p^j x^{j(p-1)}` and `g'=1-p x^{p-1}` satisfy `g' S_n = 1 - p^n x^{n(p-1)}` as an identity of polynomials. Thus `F_n=(x-x^p, y S_n)` has Jacobian `1` modulo `p^n`. Supports of `Q` at depths `2,3,4`:

```text
p=3: {0,2}, {0,2,4}, {0,2,4,6} in x, always y-degree 1,
p=5: {0,4}, {0,4,8}, {0,4,8,12} in x, always y-degree 1.
```

The engine verified the exact integer Jacobian through depth `5` and the inverse-unit identity `g' S_n ≡ 1 (mod p^n)`. Linear growth of this representative is a control. Claim 4 forbids treating it as a lower bound on the completed orbit beyond the first-digit floor.

Precision, non-blocking. The compiler flag `action_order_p_from_norm_equations` is the first-digit shadow of `τ^p=id`. Exact order `p` is the uniqueness in claim 2, not the truncated norm identities. The producer’s scope line `finite_etale_action_theorem_is_symbolic_not_sampled` records this correctly.

### 8. Scope and stop — CONFIRMED

The preregistered stop outcomes were `COMPLETION-GAP`, `FINITE-MIXED-CLASS`, and `GAUGE-TRIVIAL/CONTROL-ONLY`. Claims 1–4 close the completion/action theorem, so the first stop is not taken. Claims 5–6 give a single first-digit orbit sharing a Cartier monomial, so the mixed-class stop is not taken. The cotangent control passes. The admissible result is exactly `GAUGE-TRIVIAL/CONTROL-ONLY`.

Quarantine, checked against the body:

- Global / rational / polynomial deck action: firewalled in §2 and exhibited as non-algebraic in (6.3). Compatible with the confirmed `A_infinity` parent, whose descent key remains unearned.
- `A_infinity=0` and `d=p`: finite étale rank `p` on the unit bidisc is not finiteness of the formal fibre algebra `R[X,Y]/(P-pS,Q-pT)` over `R=Z_p[[S,T]]`, and is not vanishing of negative-valuation residual roots.
- Fixed-support exclusion: the Cartier monomial is one forced first-digit term, not a depth-uniform support obstruction, and not a bound on polynomial degree of an exact lift.
- `p=109` brute force: the compiler window at `p=109` would have `4·110=440` first-digit variables and is not licensed; the analytic theorem is already uniform in odd `p`.
- Lift construction: none. The cotangent tower is a restricted-analytic control, already reviewed as nonpolynomial.
- JC2: none.

Smallest valid successor, stated precisely. Do not compute deeper unrestricted cohomology and treat raw support differences as invariants: claim 4 says those differences are gauge. A successor must preregister one of:

1. a uniformly bounded polynomial-gauge category inside the unique completed orbit, with a support/degree bound independent of Witt depth and a compatibility rule across truncations, and then prove that every orbit representative in that category escapes the bound; or
2. an algebraic boundary conductor, defined on a specified bounded polynomial equivalence, invariant under that equivalence, and nonzero on the AS109 special fibre.

Either is a new paper. The first-digit floor is an input to (1), not a substitute for it.

---

## Dependency and Tate-algebra caveats

- Logical dependency for claims 1–8 is the exact-lift hypothesis (or the restricted-analytic analogue with `det J=1`), standard commutative algebra of complete rings, and the two Stacks tags with the hypotheses checked above. Finite presentation uses noetherianness of the Tate algebra plus Tag `00FP`(3), not a rigid-geometry black box.
- Digit carries of the AS109 Hensel erratum are irrelevant. This gate consumes packed `det J=1`.
- The completed bidisc is the integral unit polydisc. Residual sheets of the confirmed parent live at negative Gauss valuation after localizing the formal tube at `(p)`. The two categories do not mix.
- Classical Galois Keller, TDU, Moskowicz, and bounded-`y` automorphy theorems are not inputs.
- The all-Witt / Tate control is the cotangent representative of claims 6–7, already confirmed as a nonpolynomial inverse limit. This gate does not widen that control into a polynomial lift.

---

## Exact scope exclusions

Do not read this file, or the producer, as any of the following:

- a construction of an exact polynomial lift, series lift, or complex point;
- a proof that no exact lift exists;
- a rational or polynomial `C_p` deck transformation, or an element of `Aut_M(L)`;
- `A_infinity=0`, `d=p`, or finiteness of the formal fibre algebra over `Z_p[[S,T]]`;
- a fixed-support exclusion, a uniformly bounded-degree obstruction, or a theorem that every exact lift has unbounded polynomial support;
- a `p=109` computation or an AWS search;
- a mixed first-digit gauge class, or a licence to treat finite-depth support as completed-gauge invariant;
- a JC2 proof or counterexample.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a nonexistence theorem, a global degree theorem, or a JC2 decision.

The smallest precision a reader could miss, and that this review therefore isolates, is that “quotient dimension `0`” at the first Witt digit is the tautology that solutions of one linear PDE form a torsor under its kernel. The load-bearing first-digit theorem is the forced Cartier monomial, which is an invariant of that torsor and survives every larger `y`-window.

The smallest genuinely missing objects remain exactly those named in producer §7: a uniformly bounded polynomial-gauge category in which minima can be compared across depth, or an algebraic boundary conductor. Either would be a new paper. Unrestricted completed cohomology, residue-ball Hensel, and `09ZL` on the bidisc do not supply them.

A completion error that was available — invoking topological Nakayama for a module not known to be finitely generated, or citing a Henselian-*local*-ring form of `09ZL` against the non-local ring `Z_p⟨U,V⟩` — is not committed. The successive-division basis lift and the pair-form of `09ZL` exist precisely to block those errors.

---

## Promotion advice

Accept internally as an exact, hostile-confirmed first gate

```text
exact AS109 lift
  =>  finite étale rank-p C_p-torsor on the completed unit bidisc,
      unique near-identity completed symplectic right-equivalence,
      first Witt digit one divergence-free orbit with [x^{p-1} y] Q1 = 1,
      and none of this is a global deck, an A_infinity kill, or a support obstruction.
```

Record it as `GAUGE-TRIVIAL/CONTROL-ONLY`. Do **not** promote it into `APPROACHES.md` as a kill of avenue 19, as `d=p`, as a fixed-support exclusion, as a `p=109` licence, or as any JC2 implication. Do **not** answer it by computing unrestricted deeper cohomology or by launching AWS. Successor work that wants a contradiction must bring one of the two resurrection categories in producer §7; this gate correctly refuses to invent them.
