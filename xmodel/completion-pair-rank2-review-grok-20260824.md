# Hostile different-model review — `RANK2-NOGO` (function-field degree two)

| Field | Value |
|---|---|
| Claim | No characteristic-zero plane polynomial Keller map has function-field degree two |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Evidence tier | independent algebra over `C` (same calculation over any field of characteristic not `2`); primary-source comparison; no artifact computation |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family, completion-pair root X) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `dd11599b07eb05591b5c006791005eef19457d8e` |
| Review window (UTC) | 2026-08-24T06:45:00Z – 2026-08-24T07:05:00Z |
| Promotion | **out of scope**. This review does not promote, does not edit shared ledgers, and does not launch descendants |

Producer inputs reread in full before any verdict:

- `xmodel/completion-pair-gate-20260824.md` (SHA-256 `d5027984be4ae4dbe4d0b5f95161d6d57d71ed9b3c086dd6fce2f03190e6c1bc`)
- `xmodel/ideation-20260824T0453Z-synthesis.md` §§3.3 and 5 only (file SHA-256 `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790`, matching the gate header)
- `AUDIT.md` trust-boundary entries that mention function-field degree, normalization, or Keller maps (TRACE-REGULARITY 2026-08-24 and the founding msolve/torus-normalization errata). None of those entries alters the algebra below.

The scoped claim is **known**. Priority is not part of correctness. The producer writeup is a self-contained elementary proof of that known statement, and the independent recalculation agrees with it.

---

## Headline and subclaim table

Let `F=(P,Q):A^2_C -> A^2_C` satisfy `P_x Q_y - P_y Q_x = c in C^*`. Set

```text
A = C[P,Q] ≅ C[u,v],     B = C[x,y],
K = Frac(A),             L = Frac(B),
R = integral closure of A in L,
X = Spec R,              U = Spec B.
```

Assume `[L:K]=2` for contradiction.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `dP,dQ` basis of `Omega^1_B` ⇒ `P,Q` algebraically independent; `A ≅ C[u,v]`; `L/K` finite separable | **CONFIRMED** | algebraic relation `f(P,Q)=0`; infinite or inseparable extension |
| 2 | `R` is finite as an `A`-module | **CONFIRMED** | failure of Japanese / Noether finiteness for this pair |
| 3 | Canonical inclusion `R subset B` | **CONFIRMED** | an integral element of `L` over `A` not in `B` |
| 4 | Zariski Main: `U -> X` is a quasi-compact open immersion, dense and birational, with `X -> Spec A` integral (finite) | **CONFIRMED** | `Spec B -> Spec A` not quasi-finite; normalization-in-`X` not the open-immersion compactification |
| 5 | Normal surface `R` is Cohen–Macaulay; miracle flatness at primes of `R` plus finite-flat-over-local ⇒ `R` finite locally free over `A`; Quillen–Suslin (or, after the rank-two split, `Pic(A)=0`) ⇒ finite free of rank `[L:K]` | **CONFIRMED** | dimension drop on a fibre; `R_q` not CM; rank-one summand not free |
| 6 | `R^* = B^* = C^*` | **CONFIRMED** | a nonconstant unit of `R` or of `B` |
| 7 | If `D=X-U` is nonempty then it has a codimension-one component (normal Hartogs / `S_2`) | **CONFIRMED** | a nonempty purely codimension-two complement with `R ≠ B` |
| 8 | Divisor localization: `O(X)^* -> O(U)^* -> ⊕_i Z[D_i] -> Cl(X) -> Cl(U) -> 0` with first map an isomorphism and `Cl(U)=0`, hence `⊕_i Z[D_i] ≅ Cl(X)`; no nonzero principal Weil divisor supported on the boundary | **CONFIRMED** | a nonconstant unit of `U`; nonzero `Cl(A^2)` |
| 9 | `omega_R = Hom_A(R,A)` identifies with the codifferent; rank-one reflexive, not automatically invertible | **CONFIRMED** | unused in the rank-two contradiction; recorded only as perimeter |
| 10 | `2` invertible ⇒ `R = A·1 ⊕ ker(Tr_{R/A})`; `Pic(A)=0` ⇒ `ker(Tr)=A z`; `Tr(z)=0` ⇒ `b=0` in `z^2=h+b z`; `R ≅ A[T]/(T^2-h)` | **CONFIRMED** | reduced-trace convention `Tr(1)=1`; nontrivial Picard class; nonzero linear term surviving |
| 11 | `h` nonzero and nonconstant; normality ⇒ `h` squarefree | **CONFIRMED** | `h` a square in `C`; `h=0`; `z/q` integral but not in `R` |
| 12 | `Omega_{R/A} ≅ (R/(2z)) dz`; non-étale locus of `X -> Spec A` is `V_X(z)` | **CONFIRMED** | extra Kähler relation from `dh`; annihilator not `(z)` |
| 13 | Open immersion ⇒ `Omega_{B/A} ≅ B ⊗_R Omega_{R/A}`; Keller ⇒ `B/(2z)B=0` ⇒ `z ∈ B^*=C^*`; `Tr(z)=2z=0` ⇒ `z=0` | **CONFIRMED** | cotangent sequence not left-exact on an open immersion; scalar trace `Tr(c)=c` |
| 14 | Squarefree factorization `h=c q_1…q_s`; unique `E_i=V_X(q_i,z)`; `div_X(q_i)=2 E_i`; each `E_i ⊂ D` | **CONFIRMED** | split (unramified) prime over `q_i`; extra height-one component of `div(q_i)`; `E_i` meeting `U` |
| 15 | Hostile loci: localization at `A`-primes, miracle flatness, `Tr(1)=2`, scalar trace, non-Gorenstein duality, codimension-two complement, ramified/unramified sheet sharing | **CONFIRMED** (no error found) | any of those actually breaking a numbered step |
| H | Headline: no characteristic-zero plane polynomial Keller map has function-field degree two | **CONFIRMED** | a gap in 10–14; a characteristic-zero counterexample of mapping degree two |

All remarks below are non-blocking. None changes a coefficient, a module identification, or a verdict.

---

## Independent recalculation

### 1. Algebraic independence, finiteness, `R ⊂ B`

The Jacobian matrix of `(P,Q)` with respect to `(x,y)` is invertible in `B`, so

```text
Omega_{B/C} = B dx ⊕ B dy
            = B dP ⊕ B dQ.
```

If `f(P,Q)=0` were a nonzero algebraic relation, then `f_u dP + f_v dQ = 0` in `Omega_{L/C}`, contradicting linear independence of `dP,dQ` over `L` in characteristic zero. Thus `C[u,v] -> A`, `u ↦ P`, `v ↦ Q` is an isomorphism, `trdeg(K/C)=2=trdeg(L/C)`, and `L/K` is finite. Characteristic zero ⇒ separable. (Jacobian invertibility also gives separability directly: `Omega_{B/A}=0`.)

`A` is a finitely generated domain over a field, hence Japanese. The integral closure of a Japanese domain in a finite separable extension is a finite module (Noether). So `R` is finite over `A`.

Any `α ∈ L` integral over `A` satisfies a monic equation with coefficients in `A ⊂ B`. `B=C[x,y]` is a UFD, hence normal, so `α ∈ B`. Thus `R ⊂ B`.

### 2. Canonical open immersion

`Spec B -> Spec A` is of finite type, affine (hence separated), and étale by the Jacobian criterion

```text
J(F) invertible  ⇔  Omega_{B/A}=0  ⇔  B/A unramified,
```

and a finite-type unramified flat map of smooth `C`-schemes of equal dimension is étale. Étale of finite type ⇒ quasi-finite.

Let `S=Spec A` and let `S'` be the normalization of `S` in `U=Spec B`. Because `U` is integral and dominant over `S`, this `S'` is `Spec R`. Stacks Project Tag `02LR` (Zariski Main, normalization form; accessed 2026-08-24T06:52Z at https://stacks.math.columbia.edu/tag/02LR): a quasi-finite separated morphism `X -> S` factors as a quasi-compact open immersion into the normalization of `S` in `X`, followed by an integral morphism. Finiteness of `R` over `A` was already obtained from the Japanese property, so `X -> Spec A` is finite. Same fraction field ⇒ `j: U -> X` is dense and birational.

This is the exact object licensed by synthesis §3.3. The parenthetical producer sentence “JC2 for this pair is exactly `j(U)=X`” is slightly short: `j(U)=X` is finiteness of `B` over `A`, and one still uses that a finite étale cover of `A^2_C` is trivial. That sentence is not used in the rank-two contradiction.

### 3. Cohen–Macaulay to finite free

`R` is a normal domain of dimension two, hence `R_1+S_2`, hence Cohen–Macaulay as a ring. The finite dominant map `X -> Spec A` is equidimensional of relative dimension zero: `A` is normal, so going-down plus incomparability give `ht(q)=ht(q ∩ A)` for every prime `q` of `R`.

Miracle flatness is a statement about *local* homomorphisms (Stacks Tag `00R4`, accessed 2026-08-24T06:52Z, https://stacks.math.columbia.edu/tag/00R4): if `(A_p, p A_p) -> (R_q, q R_q)` has `A_p` regular, `R_q` Cohen–Macaulay, and `dim R_q = dim A_p + dim R_q/p R_q`, then `R_q` is flat over `A_p`. The dimension formula holds because both local rings have dimension equal to the height, and the closed fibre is artinian. Flatness of `R` over `A` is local on the source, so `R` is flat over `A`. A finite flat module over a local ring is free, so `R_p` is free over `A_p`. Thus `R` is finite projective over `A`. Quillen–Suslin then makes it free of rank `[L:K]`.

Hostile check on “localization over `A`-primes”: applying miracle flatness directly to the possibly *semi-local* ring `R_p` is the wording one should not use. The correct localization is at primes `q` of `R`. The producer’s phrase “every localization of `R` above it” is the `R_q` form. After flatness, finite-flat-over-local supplies freeness of `R_p` without a separate Auslander–Buchsbaum computation. Equivalence-in-spirit with Auslander–Buchsbaum (`pd=0` for a maximal Cohen–Macaulay module over a regular local ring) is harmless.

For the rank-two argument one does not need full Quillen–Suslin: after the trace split, the complementary summand is projective of rank one and `Pic(C[u,v])=0` (`C[u,v]` is a UFD, and regular so `Pic=Cl=0`).

### 4. Units, Hartogs, localization sequence

`C^* ⊂ R^* ⊂ B^*`. Units of `C[x,y]` are `C^*`. So `R^*=B^*=C^*`.

If `D=X-U` were nonempty of codimension at least two, algebraic Hartogs for a normal Noetherian domain (Stacks Tag `031T`(2): `R = ∩_{ht p=1} R_p`, accessed 2026-08-24T06:53Z, https://stacks.math.columbia.edu/tag/031T) would give `Γ(X,O_X)=Γ(U,O_U)`, i.e. `R=B`, hence `D` empty. So every nonempty complement has a Weil prime divisor.

For a normal Noetherian integral scheme and `U=X-∪ D_i` with `D_i` the codimension-one components of the complement, the Weil-class exact sequence is

```text
O(X)^*  ->  O(U)^*  ->  ⊕_i Z[D_i]  ->  Cl(X)  ->  Cl(U)  ->  0
```

(Hartshorne, *Algebraic Geometry*, II.6.5 for the class-group surjection with kernel generated by the `D_i`; the kernel of `⊕ Z[D_i] -> Cl(X)` is identified with `O(U)^*/O(X)^*` by taking `div` of functions regular and invertible on `U`). Here the unit map is `C^* -> C^*`, an isomorphism, and `Cl(U)=Cl(A^2)=0`. Therefore `⊕_i Z[D_i] ≅ Cl(X)`: there is no nonzero principal Weil divisor supported on the boundary.

Producing a boundary class is not an obstruction. The rank-two argument produces a relation.

Codimension-two pieces of `D` (isolated points) do not appear in the sequence and do not affect Hartogs. They are not a gap.

### 5. Dualizing module (perimeter only)

`A` is regular Gorenstein, `R` finite free over `A`, so `omega_R ≅ Hom_A(R,A)` as an `R`-module. Separability of `L/K` makes the trace pairing `L × L -> K` nondegenerate, and

```text
Hom_A(R,A)  ≅  { ℓ in L : Tr_{L/K}(ℓ R) ⊂ A }  = D^{-1}_{R/A}.
```

This is rank-one reflexive. It is invertible if and only if `R` is Gorenstein. The producer correctly refuses to treat it as Cartier in general rank.

In rank two, `R=A[z]/(z^2-h)` is a hypersurface, hence Gorenstein. The rank-two contradiction never uses `omega_R`.

### 6. Trace split and monogenic presentation

`R` is finite free of rank two over `A`. Field trace satisfies `Tr_{L/K}(1)=2`, a unit of `A`. The `A`-linear form `Tr_{R/A}` is the restriction of field trace (characteristic polynomial of multiplication, coefficients in `A` because `R` is integral over `A`). Projection `(1/2) Tr` splits the unit section:

```text
R = A·1  ⊕  M,    M = ker(Tr_{R/A}).
```

`M` is projective of rank one. `Pic(A)=0`, so `M=A z` for some `z ∈ R`. In the basis `(1,z)`,

```text
z^2 = h + b z,    h,b ∈ A.
```

Multiplication by `z` has matrix, with respect to `(1,z)`,

```text
( z·1    z·z )  =  ( 0    h )
                   ( 1    b )
```

whose trace is `b`. But `z ∈ M`, so `Tr(z)=0`, hence `b=0`. Thus

```text
R ≅ A[T]/(T^2 - h),    T ↦ z.
```

Hostile check on trace conventions: the argument uses `Tr(1)=2`, not a reduced trace with `Tr(1)=1`. If `z` were a scalar `c ∈ A`, then `Tr(c)=2c`; the later contradiction `2z=0 ⇒ z=0` likewise uses `Tr(1)=2`. A convention `Tr(c)=c` would be an error; it is not the convention in use.

`h ≠ 0`: otherwise `R ≅ A[T]/(T^2)` is not a domain. `h` is not a nonzero constant: every element of `C^*` is a square, so `T^2-h` would split and `R ⊗_A K ≅ K×K` would not be a field. (Over a non-algebraically closed field of characteristic zero the same conclusion holds for a different reason: a constant non-square `h` would adjoin a constant not in `k`, hence not lie in `L=k(x,y)`.)

Squarefreeness. Suppose an irreducible `q ∈ A` satisfies `q^2 | h`. Then `z/q ∈ L` satisfies the monic equation `T^2 - h/q^2 = 0` over `A`, so is integral over `A`, hence lies in `R=A ⊕ A z`:

```text
z/q = a + b z,    a,b ∈ A.
```

Multiply by `q`: `z = a q + b q z`. Linear independence of `{1,z}` over `A` gives `a q = 0` and `1-b q = 0`. The first forces `a=0`; the second forces `q` to be a unit, a contradiction. So `h` is squarefree in the UFD `A`.

### 7. Kähler differentials

With `R=A[T]/(T^2-h)`,

```text
Omega_{R/A} = (R dT) / ( d(T^2-h) ).
```

In `Omega_{R/A}` one has `dh=0`, so `d(T^2-h)=2 T dT`. Thus

```text
Omega_{R/A} ≅ (R / (2z)) dz.
```

Since `2` is a unit, the annihilator is `(z)`. The non-étale locus of `π: X -> Spec A` is `V_X(z)`.

### 8. Base change and the unit/trace contradiction

`j: U -> X` is an open immersion of finite presentation, hence étale. The cotangent sequence

```text
B ⊗_R Omega_{R/A}  ->  Omega_{B/A}  ->  Omega_{B/R}  ->  0
```

has `Omega_{B/R}=0`, and the first arrow is an isomorphism because `R -> B` is étale. Therefore

```text
Omega_{B/A} ≅ B ⊗_R (R/(2z)) dz  ≅  (B/(2z B)) dz.
```

Keller is `Omega_{B/A}=0`, so `B/(2z)B=0`. `B` is a domain and `z ≠ 0`, so `2z` is a unit of `B`, hence `z ∈ B^*=C^*`. Then `z=c ∈ C^* ⊂ A` lies in `ker(Tr)`, so `Tr(c)=2c=0`, so `c=0`, contradicting that a unit is nonzero.

This already kills both the empty-boundary case (`R=B`, finite étale of degree two) and the nonempty-boundary case. Hartogs and the class-group sequence are not required for the primary contradiction.

### 9. Alternative principal relation `div_X(q_i)=2 E_i`

Write the squarefree factorization `h = c q_1 ⋯ q_s` in `A`, with `s ≥ 1` and the `q_i` pairwise non-associate irreducibles. Fix `i`. Localize `A` at the height-one prime `(q_i)`: `A_{(q_i)}` is a DVR with uniformizer `t=q_i`, and `h = t · u` with `u = c ∏_{j≠i} q_j` a unit in `A_{(q_i)}`. Then

```text
R ⊗_A A_{(q_i)}  ≅  A_{(q_i)}[z] / (z^2 - u t).
```

The polynomial `T^2 - u t` is Eisenstein at `t`, hence irreducible; the extension of fraction fields is ramified of index two, and the integral closure is already this quadratic order. The unique maximal ideal is `(z)`, a uniformizer, and `t = z^2 u^{-1}`, so `v(q_i)=2`. The prime of `R` is `(q_i, z)`, and

```text
R/(q_i,z) ≅ A/(q_i)
```

is a domain of dimension one, confirming height one. Uniqueness: a finite extension of DVRs that is Eisenstein has a unique prime in the integral closure.

Any other height-one prime `𝔭` of `R` lies over a height-one prime `(f)` of `A` (incomparability). If `f` is not associate to `q_i`, then `q_i` is a unit in `A_{(f)}`, hence in `R_𝔭`, so `v_𝔭(q_i)=0`. Therefore

```text
div_X(q_i) = 2 E_i,    E_i = V_X(q_i, z).
```

Étaleness on `U` is `V_X(z) ∩ U = ∅`, so `E_i ⊂ V_X(z) ⊂ D`. Thus `2 E_i` is a nonzero principal divisor supported on the boundary, contradicting injectivity of `⊕ Z[D_j] -> Cl(X)`. Equivalently, `q_i` is regular and nonvanishing on `U`, hence a unit of `B`, hence constant, contradicting that `q_i` is a nonconstant irreducible of `A` and that `P,Q` are algebraically independent.

Hostile check on a ramified boundary sheet sharing a target value with an unramified source sheet: in degree two a ramified fibre is `Spec k[z]/(z^2)`, a single point of multiplicity two. It cannot contain an unramified point of `U`. An unramified closed fibre consists of two reduced points, both in `U` (generic degree two, `j` injective). Those two geometric sheets do not meet `V(z)`. There is no mixed fibre. The warning is real in higher rank and empty here.

### 10. Characteristic zero versus `C`

The producer writeup is over `C`. The same calculation works over any field `k` of characteristic not `2`: `k[x,y]^*=k^*`, `Pic(k[u,v])=0`, `Tr(1)=2`, Japanese finiteness, miracle flatness, Zariski Main Tag `02LR`, and the Eisenstein computation are field-independent. Connell–van den Dries reduction plus Lefschetz also specialize the characteristic-zero statement to `C`. Headline CONFIRMED as stated.

---

## Hostile loci, explicitly

- **Localization over `A`-primes.** Miracle flatness is applied at `R_q`, not at the semi-local `R_p`. Finite flat over a local ring then frees `R_p`. No error.
- **Miracle flatness.** Hypotheses hold: `A_p` regular, `R_q` CM, equidimensional finite map. Tag `00R4`. No error.
- **`Tr(1)=2`.** Used correctly in the splitting and in `Tr(c)=2c`. No error.
- **Scalar trace.** A constant `c` has trace `2c`, not `c`. The contradiction `z ∈ C^* ∩ ker(Tr)` uses this. No error.
- **Non-Gorenstein duality.** Not used. Rank-two `R` is Gorenstein anyway. No error.
- **Codimension-two complement.** Independently impossible in rank two: the `z`-unit argument does not mention `D`. Hartogs is used only to know that a nonempty `D` has a divisor, which the alternative `div(q_i)=2E_i` form needs. No error.
- **Shared ramified/unramified sheets.** Impossible for a quadratic Eisenstein fibre. No error.
- **`div_X(q_i)=2E_i`.** Rechecked by Eisenstein and by the absence of other height-one primes over `q_i`. No error.

Non-blocking wording nits, none of which is a gap: Quillen–Suslin is stronger than needed after the rank-one split; “Auslander–Buchsbaum equivalently miracle flatness” conflates two neighbouring theorems; “JC2 is exactly `j(U)=X`” omits triviality of finite étale covers of `A^2`.

---

## Knownness (not a correctness input)

The theorem is **known**. A quadratic extension in characteristic not `2` is Galois, and the Galois case of the Jacobian conjecture is a theorem:

- L. Andrew Campbell, “A condition for a polynomial map to be invertible,” *Math. Ann.* **205** (1973), 243–248. https://eudml.org/doc/162494 (DOI 10.1007/BF01349234). Complex maps; several complex variables. Accessed 2026-08-24T06:51Z.
- Michael Razar, “Polynomial maps with constant Jacobian,” *Israel J. Math.* **32** (1979), 97–106. https://doi.org/10.1007/BF02764906 . Accessed 2026-08-24T06:50Z.
- David Wright, “On the Jacobian conjecture,” *Illinois J. Math.* **25** (1981), 423–440. https://doi.org/10.1215/ijm/1256047158 . Algebraic proof, any characteristic-zero field; first page and the Galois discussion accessed via Project Euclid 2026-08-24T06:51Z.
- Hyman Bass, Edwin H. Connell, David Wright, “The Jacobian conjecture: Reduction of degree and formal expansion of the inverse,” *Bull. Amer. Math. Soc. (N.S.)* **7** (1982), 287–330, Theorem 2.1: if `char=0` then “`k(X)` Galois over `k(F)`” implies invertibility. PDF https://www.ams.org/journals/bull/1982-07-02/S0273-0979-1982-15032-7/S0273-0979-1982-15032-7.pdf accessed 2026-08-24T06:54Z.

S. Yu. Orevkov, “On three-sheeted polynomial mappings of `C^2`,” *Math. USSR Izv.* **29** (1987), 587–596 (Russian original *Izv. Akad. Nauk SSSR Ser. Mat.* **50** (1986)), Theorem 1.1, records `N≠2` as already well-known and cites Bass–Connell–Wright Theorem 2.1(a)⇔(g); he also gives a compactification-and-`π_1` argument. PDF https://www.math.univ-toulouse.fr/~orevkov/jc86.pdf accessed 2026-08-24T06:53Z.

These are different from Wang’s theorem (polynomial *total* degree `≤ 2`; S. S. Wang, *J. Algebra* 1980, reproduced as Bass–Connell–Wright (2.4)), and different from Keller’s birational case `[L:K]=1` (O.-H. Keller, *Monatsh. Math. Phys.* **47** (1939), 299–306).

Vitushkin produced *rational* (not polynomial) generically two-to-one maps with constant Jacobian, with a pole along a line; see the summary in Wikipedia “Jacobian conjecture” (accessed 2026-08-24T06:50Z, https://en.wikipedia.org/wiki/Jacobian_conjecture) citing Vitushkin, *Math. Notes* **47** (1990). That example shows the polynomial hypothesis is essential and that a purely local-analytic obstruction is insufficient. The producer argument uses `B=C[x,y]` at the unit step, which is exactly the polynomial input.

The producer proof does not cite this literature. It is a valid elementary specialization (global monogenic presentation plus units of `C[x,y]`), not a restatement of simple connectivity of `C^2`. Correctness is independent of priority.

Orevkov’s `N≠3` theorem is outside this review’s scope. Synthesis §5 licensed only a rank-two/three schema and a stop at the first exact separator; the producer stopped at rank two, as required.

---

## Scope exclusions

- Not a proof of JC2. Ranks `≥ 3` are untouched by this certificate.
- No degree bound on `P,Q`, no compactification, no GGV/Sigray receiver, no class/canonical positivity.
- No claim that the argument is new.
- TRACE-REGULARITY in `AUDIT.md` (regularity of the first `d` field-power traces equivalent to integrality) is a different, unbounded reformulation; it is not used and is not confirmed or refuted here.
- Founding `AUDIT.md` errata (msolve unit-basis short circuit; torus normalization not in the trust boundary) do not meet this algebra.
- Characteristic two is excluded: the splitting `R=A ⊕ ker(Tr)` and `Omega ≅ R/(2z)` both use that `2` is a unit.
- This review does not promote the result, does not edit `AUDIT.md` / `COORDINATION.md` / `PROGRESS.md`, and does not launch a rank-three or one-boundary descendant.

---

## Sources

| Source | URL | Access (UTC) |
|---|---|---|
| Stacks Tag `02LR` (ZMT, open immersion into normalization) | https://stacks.math.columbia.edu/tag/02LR | 2026-08-24T06:52Z |
| Stacks Tag `02LQ` (ZMT section) | https://stacks.math.columbia.edu/tag/02LQ | 2026-08-24T06:52Z |
| Stacks Tag `00R4` (miracle flatness) | https://stacks.math.columbia.edu/tag/00R4 | 2026-08-24T06:52Z |
| Stacks Tag `031T` (normal domain = intersection of height-one localizations) | https://stacks.math.columbia.edu/tag/031T | 2026-08-24T06:53Z |
| Hartshorne II.6.5 (Weil class-group localization) | print | standard |
| Bass–Connell–Wright 1982, Thm 2.1 and (2.4) | https://www.ams.org/journals/bull/1982-07-02/S0273-0979-1982-15032-7/S0273-0979-1982-15032-7.pdf | 2026-08-24T06:54Z |
| Campbell 1973 | https://eudml.org/doc/162494 | 2026-08-24T06:51Z |
| Razar 1979 | https://doi.org/10.1007/BF02764906 | 2026-08-24T06:50Z |
| Wright 1981 | https://doi.org/10.1215/ijm/1256047158 | 2026-08-24T06:51Z |
| Orevkov 1987 / 1986 | https://www.math.univ-toulouse.fr/~orevkov/jc86.pdf | 2026-08-24T06:53Z |
| Wikipedia, Jacobian conjecture (Galois case, Vitushkin rational degree-two example) | https://en.wikipedia.org/wiki/Jacobian_conjecture | 2026-08-24T06:50Z |

---

## File digest

SHA-256 of the UTF-8 bytes strictly above the preceding `---` (everything before this section):

```text
9e18aa5adabf9544db3bd2e610a5850c1234aebbe80bbe26547c4eb539fc25ab
```
