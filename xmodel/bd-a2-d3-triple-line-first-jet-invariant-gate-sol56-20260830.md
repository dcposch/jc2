# Degree-three triple-line first-jet invariant gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen basis: `7dd85a6598c56fa043dd397382de1c93d846fa39`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Assume the provisional degree-three four-row theorem in
`bd-a2-d3-hodge-level-divisor-sol56-20260830.md`.  At the possible
index-three Halphen fibre the plane cubic is a triple line.  After an
admissible formal change of coordinates and multiplication by a unit, its
degree-three coefficient-base jet has the form

```text
F=x^3+t(xQ(y,z)+G(y,z))+O(t^2),                          (0.1)
```

where `Q` is binary quadratic and `G` is binary cubic.  Normality of the
total surface forces `G!=0`.

For Fisher's ternary-cubic invariant normalization, write

```text
Q=q0 y^2+q1 yz+q2 z^2,
G=b0 y^3+b1 y^2z+b2 yz^2+b3 z^3.
```

Then the first nonzero universal Taylor terms at the rank-one cubic `x^3`
are

```text
[t^3]c4 = 24(6b0b2q2-9b0b3q1-2b1^2q2+b1b2q1
              +6b1b3q0-2b2^2q0),                       (0.2)

[t^4]c6 = -216 Disc_binary(G).                           (0.3)
```

Neither term depends on `F2` or `F3`.  Every positive Hodge-level triple-line
fibre must therefore have a repeated root in `G` and must satisfy (0.2)=0.
Up to `PGL2` on the central line, the surviving first jets are only

```text
G=y^2z,     q2=0;                  or
G=y^3,      with no new first-jet condition on Q.         (0.4)
```

In particular the squarefree transverse first-jet stratum is eliminated
from both Halphen rows before any elimination or AWS computation.  This is a
necessary local invariant theorem.  It does not prove that either stratum in
(0.4) occurs, classify the higher jet, construct a class-`(3,3)` surface or
map, or prove JC2.

## 1. Normal form and normality

Choose the central triple line as `x=0`.  A general first coefficient is

```text
F1=a x^3+x^2L(y,z)+xQ(y,z)+G(y,z).
```

Multiplication by a unit congruent to `1-a t` removes the `x^3` term to first
order.  The determinant-one substitution

```text
x -> x-(t/3)L(y,z)
```

removes the `x^2L` term.  These transformations preserve invariant
valuations and give (0.1).  Before this parameter-dependent change the
global coefficient-base polynomial has degree at most three.  Substitution
can create determined higher powers of `t`, but creates no new parameters;
the leading gate below is insensitive to all `O(t^2)` terms.

Along the generic point of the central line, the total-space Jacobian has

```text
F_t|_(t=x=0)=G(y,z).                                     (1.1)
```

If `G=0`, the whole central line lies in the singular locus, so the
hypersurface fails `R1` and is not normal.  If `G!=0`, only the finite
zero scheme of `G` can be singular on the central line.  Together with a
smooth generic fibre, the hypersurface is regular in codimension one; being
Cartier, it is Cohen--Macaulay and hence `S2`.  Thus the local total surface
is normal.  The gate below uses only the necessary direction `normal =>
G!=0`, but the converse identifies the exact local normality test under
generic smoothness.

## 2. Hessian derivation

For a ternary cubic `U`, put

```text
H(U)=-1/2 det(d^2 U).                                    (2.1)
```

Fisher's Hessian-pencil identity implies

```text
[mu] H(U+mu H(U))   = 3 c4(U) U,
[mu^2]H(U+mu H(U)) = 6 c6(U) U-3 c4(U)H(U).             (2.2)
```

Because the `x^3` coefficient of (0.1) is a unit, equations (2.2) recover
`c4,c6` from the single `x^3` coefficient of the pencil Hessian.  Applying
this to the universal truncated form

```text
U=x^3+t(xQ+G)
```

gives

```text
c4=t^3(0.2)+O(t^4),
c6=-216t^4 Disc_binary(G)+O(t^5).                        (2.3)
```

The binary discriminant convention is

```text
Disc_binary(G)=b1^2b2^2-4b0b2^3-4b1^3b3-27b0^2b3^2
               +18b0b1b2b3.                            (2.4)
```

The higher-jet independence is a polarization argument, not an experimental
truncation.  Apply the formal unit and `x`-translation gauge order by order:
the `x^3` coefficient stays a unit and the `x^2L` direction is removed at
every order.  The resulting coefficients lie in the seven-dimensional
normal slice `xQ+G`; the unit and determinant factors do not change the
leading valuations.  On this slice the universal expansion
`c4(x^3+epsilon V)` vanishes through order two, and
`c6(x^3+epsilon V)` through order three, for arbitrary `V` in the slice.
Polarization therefore kills all lower Taylor tensors there.  In a gauged
arc `x^3+tF1+t^2F2+...`, total `t`-weight three for `c4` can only use three
copies of `F1`; total weight four for `c6` can only use four copies of `F1`.
This proves that (0.2)--(0.3) are unchanged by `F2,F3`.

## 3. Exact first-jet classification

At a point of Hodge colength `k>=1`, the Hodge/invariant theorem gives

```text
v(c4)>=4,             v(c6)>=6.                          (3.1)
```

Thus both displayed leading terms in (2.3) must vanish.  Equation (0.3)
forces `Disc_binary(G)=0`.  Since normality excludes `G=0`, the binary cubic
has either a double and a simple root or one triple root.

In the double-root orbit take `G=y^2z`.  Substitution in (0.2) gives

```text
[t^3]c4=-48q2,                                         (3.2)
```

so `q2=0`.  Geometrically, `Q` vanishes at the double-root point on the
central line.  In the triple-root orbit take `G=y^3`; both (0.2) and (0.3)
vanish identically.  This proves (0.4).

For the one-point Halphen row, `k=2`.  Since the residue characteristic is
zero, Cremona--Fisher--Stoll Lemma 3.2 and the Hodge-lattice identification
show that level two forces the necessary bounds

```text
v(c4)>=8,             v(c6)>=12.                         (3.3)
```

The converse is false in general because the minimal invariants may
themselves vanish.  No equivalence is used here.  The usually displayed
discriminant condition `v(Disc)>=24` is then
automatic from `c4^3-c6^2=1728 Disc`; it need not be imposed as a third
generator in the elimination ideal.  The next computation should therefore
solve only the remaining coefficients of `c4 mod t^8` and `c6 mod t^12` on
the two normal forms (0.4), retaining the finitely many original degree-three
base coefficients and every higher term induced by the normalization,
followed by actual minimisation of every survivor.

## 4. Executable replay

The replay is

```text
ops/d3_triple_line_first_jet_invariant_replay.py
SHA-256 08c523e2b2dade813d5c12652bfc501ec02de80470f44e3763571387940e852c
```

It uses SymPy `1.14.0` only to perform exact polynomial differentiation,
determinants, coefficient extraction, and factorization.  It derives
(0.2)--(0.3) from (2.1)--(2.2), verifies the binary discriminant identity,
fixes the normalization with `H(xyz)=-xyz`, `c4(xyz)=1`, `c6(xyz)=-1`, and
checks squarefree, double-root, and triple-root controls.  It contains zero
Python AST `assert` nodes.

Run:

```bash
d3jet_tmp=$(mktemp -d)
python3 ops/d3_triple_line_first_jet_invariant_replay.py > "$d3jet_tmp/ordinary.json"
python3 -O ops/d3_triple_line_first_jet_invariant_replay.py > "$d3jet_tmp/O.json"
python3 -OO ops/d3_triple_line_first_jet_invariant_replay.py > "$d3jet_tmp/OO.json"
cmp "$d3jet_tmp/ordinary.json" "$d3jet_tmp/O.json"
cmp "$d3jet_tmp/ordinary.json" "$d3jet_tmp/OO.json"
shasum -a 256 "$d3jet_tmp/ordinary.json"
```

All three outputs are byte-identical, 919 bytes, with SHA-256

```text
d2da55b85ef0da6eaefd8a1ed38a0c33546a4a82522d6d1c1ebac3ad3c69eede.
```

The mutation

```text
python3 ops/d3_triple_line_first_jet_invariant_replay.py --mutate-disc-sign
```

exits nonzero with `FAIL:binary discriminant sign/control failed`.

## 5. Disposition and firewalls

1. Hostile-review the normal-form transformation, Hessian normalization,
   Taylor-weight argument, and the inference from positive level.
2. On `G=y^2z,q2=0`, use the remaining stabilizer and admissible Smith slopes
   before forming any large ideal.
3. On `G=y^3`, compare directly with the critical insoluble ternary cubics of
   Cremona--Fisher--Stoll; a level-one critical normal form may reduce the
   level-two search to one further admissible transformation.
4. Keep the soluble no-multiple-fibre one-point row separate: its local model
   is level two but its minimal-level floor is zero, whereas the Halphen
   torsor has minimal level one.

Firewalls:

- `G` is the transverse binary first jet, not a plane component or a branch
  count.
- A repeated root of `G` is necessary, not an attained singularity type.
- Formal invariant divisibility does not prove total-space normality unless
  the explicit `G!=0` and generic-smoothness tests are retained.
- Level, Hodge colength, local geometric genus, fibre multiplicity, and
  discriminant order remain distinct quantities even where exact theorems
  relate them.
- No finite jet is an arc-existence theorem, effective global surface, map,
  counterexample, or proof of JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8949`.
- Body SHA-256:
  `69b1cbe29074593f628b8ba2c3a8ff330dcc31ba351570af0f7b28017602e89f`.
- Frozen basis: `7dd85a6598c56fa043dd397382de1c93d846fa39`.
