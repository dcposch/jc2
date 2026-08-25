# Hostile review: localized `w=0` fibre classification

**Reviewer.** Grok 4.6 (required different-model referee). Producer is GPT-family.  
**Target.** `xmodel/max12-912-order3-nu-q8-w0-localized-fibre-classification-20260825.md` and case `cases/max12_912_order3_nu_q8_w0_fibre_stratification_aws_20260825/`.  
**Limitation.** This session used no Bash, no CAS, no network, and wrote/edited no file. SHA-256 values were compared as hex strings already present in the named files; they were not recomputed from bytes. Singular, `generate.py`, and the parent compiler were not re-executed. Polynomial identity of the six specialized rows with a fresh compiler expansion at `w=0` is therefore algorithmic, not numeric.

---

## 1. Charge, scope, and parent identity

The charged statement is only the finite affine chart

```text
w=0,  x5 != 0,  x3-2*x5 != 0
```

in the reviewed `p=1`, `k=0` approximate-cubic quotient (`compile_quotient("approx")`, imposed `(1,3,5,7,2,4)`). The scheme `Y_0` is the `w=0` fibre of the arithmetic source written in the 2026-08-25 scheme-identity gap audit: six divided rows plus

```text
v*x5 - x3 + 2*x5 = 0,
inv*x5*(x3-2*x5) - 1 = 0.
```

The localizer does **not** invert `w`. That is the correct special-fibre chart: the punctured open `inv*w*x5*(x3-2*x5)-1` has no `w=0` point.

Firewall in §§1 and 5 is exact and is **not** discharged: source boundary `x5=0`, `x3-2*x5=0` and their overlap; projective escape of `c,d2,d4,x1,x3,x5`; the `p=0` chart; terminal `r8`; both Taylor families; actual-trajectory landing; arbitrary selected components; all `(9,12)`; max12; Keller; JC2. Item 7 of the gap audit (identity of this source with the global-quotient / primitivity / infinity schemes) remains charged. Composition with the selected-Q8 positive-genus theorem is correctly postponed.

---

## 2. Source, orders, cover, inverses

`generate.py` pins `quotient_compiler.py` at `22b0cdc4…` and the parent `MANIFEST.sha256` at `3d60b567…`, matching the CONFIRMED 2026-08-24 global-quotient review. It refuses any imposed-row mismatch. `specialize_w0` drops monomials with positive `w`-exponent in the compiler’s first coordinate; frozen `input.sing` rows are `w`-free with denominators in `{3^k}`, hence well-defined in characteristics `0`, `127`, and `32003`.

Frozen base ring and generators (Box02 `std`/block and Box03 `slimgb`/`dp` agree on the polynomials):

```text
R = k[c,d2,d4,x1,x3,x5,inv,v]
I_base = (e1,e3,e5,e7,e2,e4, ev, einv)
```

Block order is `(dp(n-1),dp(1))` with `v` last; `dp` replay is total degree with `v` still last. Jacobian is the literal `8×8` of those eight rows in `(c,d2,d4,x1,x3,x5,inv,v)`, not involving dummy inverse variables. `det(J|_{w=0})` equals the specialization of the relative Jacobian of the total space, so “relative” is not a specialization-order cheat.

Every open is a fresh inverse row: `inu*e6-1`, `iq*eq8-1`, `idet*detJ-1`, `irho*e8-1`. No `sat`, `division`, or unrecorded radical. The set-theoretic cover

```text
V(e6) ∪ (D(e6)∩V(Q8)) ∪ (D(e6)∩D(Q8))
```

is an identity of sets on `Y_0`. The `V/D(detJ)` split of the middle term is present over `Q` on both engines. The preregistered `V/D(e8)` split of the last term was run only in `F_127` and `F_32003` (defect D3 below); over `Q` the parent `nonq8` locus is already empty, so the omitted split is mathematically vacuous.

Hardcoded `eq8` is `-Q8` of display (1.2). Associates, so kernels and gcds are unaffected.

Every harvested `singular.stdout` contains exactly one `Q8_W0_FIBRE_STRATUM_PASS` and `original_remainder_zero=1`. That remainder loop tests `reduce(I_j,G)=0` for the stratum generators, including the six source rows and the graph/localizer. All 34 `run.meta` have `rc=0`; all 34 `singular.stderr` are `/usr/bin/time -v` text with `Exit status: 0`.

---

## 3. The isomorphism `A ≅ Q[v]/(Q8)`

Let `A = Q[c,d2,d4,x1,x3,x5,inv,v]/I_base`. The structure map is

```text
φ: Q[v] → A,   v ↦ v.
```

It is **not** the projection `A → Q[v]/(eliminant)`. Direction is therefore: principal domain into the coordinate ring.

From the two characteristic-zero base runs:

| | Box02 `std`/block | Box03 `slimgb`/`dp` |
|---|---|---|
| `dim` | 0 | 0 |
| `vdim` | 8 | 8 |
| GB `size` | 8 | 29 |
| `v`-eliminant | principal, degree 8 | same |
| `gcd(H,H')` degree | 0 | 0 |
| `gcd(H,eq8)` degree | 8 | 8 |
| `factorize(H,1)` | one factor, display (1.2) | same |

So `ker φ = I_base ∩ Q[v] = (H) = (Q8)`, and `dim_Q A = 8 = dim_Q Q[v]/(Q8)`. An injective homomorphism of finite-dimensional `Q`-algebras of equal dimension is an isomorphism. That is linear algebra, not a geometric leap: extra nilpotents or a second component supported on the same `v`-values would raise `vdim`; a collision in the projection would make `deg(H) < vdim`; a proper subalgebra would contradict injectivity of equal-dimensional spaces.

Squarefreeness of `H` then makes `Q[v]/(Q8)` reduced, hence `A` reduced. Over `Qbar` one obtains eight distinct points. Irreducibility of `Q8` (one Singular factor of degree 8 on both engines) makes `A` a degree-eight field; as a `Q`-scheme `Y_0` is then a single closed point of residue degree 8. The eight contacts are geometric.

The same numerical invariants hold for `loaded` and `q8_smooth` on both engines, and for `q8` on Box02. Independently, the **printed** reduced basis of `q8_w0_q8_Q_std_block_box02_v1` (`print_basis=yes`) is a shape lemma:

```text
G[1] = Q8(v)
G[2]…G[9] = (nonzero Q-constant)·{inu,inv,x5,x3,x1,d4,d2,c} + Q[v]_{<8}
```

Leading coefficients `960740352, 1259712, 100, 50, 25, 440, 440, 71280` are nonzero in `Q`, so every coordinate is uniquely a polynomial in `v` modulo `Q8`. That is constructive generation/surjectivity for `D(e6)∩V(Q8)`. With `nu0` and `nonq8` both the unit ideal, this is all of `Y_0`. The producer’s §4 never cites this basis; the dimension argument already suffices.

Eliminant degree plus vector-space dimension would fail to give a scheme isomorphism if one of them were missing (e.g. squarefree degree-8 eliminant with `vdim>8` is a non-reduced thickening or a fibre of the projection). Both are present and equal, and the kernel is exactly `(Q8)`, not merely its radical. The attacked inference **survives**.

---

## 4. Units, emptiness, modular controls

`(I_base,e6)=(1)` on both char-0 engines (`dim=-1`, `size=1`, `vdim=0`). Thus `e6=r6|_{w=0}` is a unit in `A` scheme-theoretically, without reducedness. `D(e6)` retains length 8, same eliminant.

`nonq8 = (I_base, inu*e6-1, iq*eq8-1)` is the unit ideal on both engines: no loaded non-Q8 point. `q8_singular` is the unit ideal and `q8_smooth` has length 8, so `detJ` does not vanish on `Y_0`. In a reduced Artin `Q`-algebra that is the unit condition. §4’s parenthetical `(I_base,Q8,detJ)` is not the computed ideal (defect D1); adjoining `inu*e6-1` is harmless because `e6` is already a unit, and `1∈√I` implies `I=(1)`.

`F_127` and `F_32003` reproduce dimension, length 8, squarefreeness, `gcd(-,Q8)=8`, and every emptiness. Over `F_127`, factors are `v+60`, `v-58`, `v-26`, and a quintic: roots `26,58,67` with `67≡-60`. No rational-root discard: aggregate demands `vdim=8` and full Q8-gcd. Over `F_32003` the split is `1+7`. These reductions **do not** give a modular irreducibility witness (defect D2).

---

## 5. Aggregate 34-run inventory

`aggregate.py` independently lists 34 tags: Box02 18 (`std`/block, `Q` and `127`), Box03 16 (`slimgb`/`dp` over `Q`, `slimgb`/block at `32003`). Finite modes `{base,loaded,q8,q8_smooth}` → 14 length-eight Q8 rows; empty modes `{nu0,q8_singular,nonq8,*_smooth/singular, nonq8_rho*}` → 20 unit ideals. Harvested `aggregate.json` matches that matrix, including per-file sha256 strings that agree with `MANIFEST.sha256` and the corresponding `run.meta` on every spot-check performed. Hosts are `ip-172-30-0-186` / `ip-172-30-0-249`, Singular 4.3.2.

Box03 has no char-0 `q8` row; the theorem table does not need one (`q8_smooth` is the displayed Q8-smooth line). Aggregate does **not** parse `rational_factor_entries` or the printed octic (defect D2).

---

## 6. Defects (all repairable; none break (1.3))

1. **Source-fidelity.** §4 writes the Q8-singular ideal as `(I_base,Q8,detJ)`. The script computes `(I_base, inu*e6-1, eq8, detJ)`. Conclusion stands, but the citation is false as written.
2. **Irreducibility custody.** Squarefreeness is fail-closed (`gcd(H,H')=0` in the aggregate). Irreducibility over `Q` is a human reading of Singular `factorize` on two Groebner bases from the **same** CAS. Reductions split (`1+1+1+5`, `1+7`), so they do not certify irreducibility. Aggregate never asserts `rational_factor_entries=1`. The field statement needs a gated factor count or a second system.
3. **Preregistration completeness.** The `V(e8)∪D(e8)` split of non-Q8 was not run over `Q`. Vacuous given `nonq8=(1)`, but not as preregistered.
4. **Unused constructive certificate.** The shape-lemma basis that actually exhibits generation is printed only for `q8` (and `q8` mod 127), not for `base`, and is not used in §4.
5. **Transitive fibre pin.** `run.meta` hashes the quotient compiler and its MANIFEST, not `order3_fibre.py` (`a4fdac5d…`). Runtime `load_parent()` would have failed on mismatch; the specialized polynomials are frozen in `input.sing`. Still a custody hole.
6. **Q8 sign.** Generator emits `-Q8`. Harmless up to units; should be displayed consistently.
7. **Reviewer-side.** Hashes and compiler expansion at `w=0` were not independently recomputed in this session.

No mathematical hole was found in the scheme isomorphism, the unit claims, the emptiness of unloaded and loaded non-Q8 loci, or the stated scope.

CONFIRMED_WITH_REPAIRS
