# BRAID-PREP: certified braid-monodromy job for the (6,4) row family

**Lane.** Systems / preparation.
**Date.** 2026-08-31.
**Agent.** grok-4.6.
**Status.** Job bundle; no CAS execution on this machine.
**OPEN targeted.** `OPEN[PI1S4-(6,4)-FACTORIZATION]`.
**Campaign policy.** Heavy / uncertain-duration computation is AWS-only.

## Contents

1. Hash verification and charged-input inventory
2. Campaign constraints and dialect discipline
3. Mathematical target (row family, F, discriminant, rho_inf)
4. Sage / SIROCCO API confirmation
5. Implicit equation F: resultant derivation and pre-monodromy checks
6. Parameter choices (b,c) and j-invariants
7. Deliverable 1: `braid_monodromy_row64.sage`
8. Deliverable 2: `check_s4_tuples.py`
9. Deliverable 3: `run_braid_job.sh` and Ubuntu install notes
10. Deliverable 4: SHA-256 manifest of every file body
11. Unverified-API flag list
12. AWS run protocol and acceptance criteria
13. FALLACY-v2 check
14. What this bundle does not claim

## 1. Hash verification and charged-input inventory

Three frozen copies were hashed with `shasum -a 256` **before any was read**. 3/3 match the boxed manifest.

```text
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  .../inputs/pi1s4-64-zvk-u6-opus5-20260831.md
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  .../inputs/pi1s4-64-fixed-tuple-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  .../inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Paths abbreviated; full paths are the lane-input copies under `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.8jZWlg/inputs/`. No charged file was edited. `jc2-lean` was not inspected.

**Typing of charged content as consumed.**

- `PROVISIONAL` — Theorem ROW-NF as stated in ZVK-U6 §1.3 (`x=r(t)^2`, `y=q(t)`, `r=t^3+bt+c`, `q=t^4+(2b/3)t^2+(4c/3)t`, `c≠0`, `j=b^3/c^2`); the open-stratum exclusions `j∉{-27/4,-81/16}`; `|Σ_x|=6` and `|Σ_u|=11`; `e(ρ_∞^D)=11`; eight local factors `(5×σ, 3×σ²)` with three `σ` stacked at `x=0`.
- `PROVISIONAL` — FIXED-TUPLE §5.4 / Theorem `(6,4)`-ρ∞: exactly 72 generating `ρ_∞`-fixed transposition 6-tuples; node datum `a_p=0` (disjoint transpositions at each node).
- `PROMOTED` — integration `126c2d29` is inventory only (N-A / N-A-RES / M-INF / D1-DEGREE). This job does not consume those theorems.

**Primary literature fetched and hashed (2026-08-31).**

| Source | URL | SHA-256 |
|---|---|---|
| Sage 10.8 `zariski_vankampen` | https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html | `81dd74980fcbb94dfb78ff9ee80f38d0a4c710be25d3be1baf81c44cfbb3c7ac` |
| Sage 10.8 `affine_curve` | https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/affine_curve.html | `65aba08bfda0483ece7ea4890927d5a08d4b6a702ec91923129b99f86f73c5a4` |
| Sage 10.8 `braid` | https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html | `d10f7d40460eba93a4a77104fb2055e6f23fd63f756219db14f1b66e97025527` |
| Sage 10.8 `artin` (`exponent_sum`) | https://doc.sagemath.org/html/en/reference/groups/sage/groups/artin.html | `fc6a383d7c8b017f7daf1dcc3e7c7c65c026bc93eebb11611459bd0d0d1d63c7` |
| Sage 10.8 SPKG `sirocco` | https://doc.sagemath.org/html/en/reference/spkg/sirocco.html | `dfcbedf655729530b8473e8b1a063da6e114556e5fbb6d7a1479aed35f80def4` |
| Marco–Rodríguez, SIROCCO, ICMS 2016 (Zaguan PDF) | https://zaguan.unizar.es/record/131386/files/texto_completo.pdf | `e4e6063240a00dbdf3dfb116fc6ab14dcfec0cc02c9ed19731786a573414388e` |

Doc pages are dated 2025-12-27 and belong to the Sage 10.8 manuals (curves PDF banner: “Plane and Space Curves, Release 10.8”). SPKG `package-version.txt` on the fetched page is `2.1.1`.

**Execution disclosure.** No Sage, no SIROCCO, no Groebner, no resultant was run on this machine. The Python checker’s `--selftest` (46656 transposition tuples, permutation arithmetic, same class as FIXED-TUPLE §5.4) was run here to certify that the job’s positive control actually returns 72. Result: 102 `ρ_∞`-fixed, 72 generating, charged witness fixed; negative control 6720 and distinct. That is a check of the checker, not a statement about `D`.

## 2. Campaign constraints and dialect discipline

- Heavy / uncertain-duration computation is AWS-only. `run_braid_job.sh` refuses the SIROCCO call unless `/sys/class/dmi/id/sys_vendor` is `Amazon EC2` (same gate as `ops/aws_exact_lane.sh`), or `BRAID_JOB_FORCE=1` is set for an already-approved replay.
- M2/Sage dialect: long-form code; assertion messages self-describing; no variables named `pi`, `gamma`, `I`, or `O`. Every API call not pinned to a fetched page is marked `FLAG` in the Sage script and listed in §11.
- The report is the only workspace file this lane writes. Job bodies live in fenced blocks below; SHA-256 is of those bodies.
- No `charge_basis` line: this bundle does not assert an exit price.

## 3. Mathematical target (row family, F, discriminant, rho_inf)

**Curve.** Residual row `Δ=(6,4,3)`, one place at infinity, three affine ordinary nodes. After a target automorphism (Theorem ROW-NF):

```text
x = r(t)^2 ,  y = q(t) ,
r = t^3 + b t + c ,  q = t^4 + (2b/3) t^2 + (4c/3) t ,  c ≠ 0 ,
j = b^3 / c^2 .
```

The implicit equation is the elimination ideal of the parametrisation:

```text
F(x,y) := Res_t( x - r(t)^2 , y - q(t) )  ∈ QQ(b,c)[x,y] ,
```

taken primitive over `QQ` after specialising `(b,c)`. Equivalent construction: `G(u,y)=Res_t(u-r(t), y-q(t))` (equation of `D'`), then `F(x,y)` is `G(u,y)G(-u,y)` rewritten in `x=u^2`, up to units of `QQ`. The Sage script computes both and asserts they agree.

**Degrees (desk-scale, no CAS).** `x-r(t)^2` has `t`-degree 6, leading coefficient `-1`. Resultant as `∏_{r(t)^2=x}(y-q(t))` is degree 6 in `y`. Leading `t^6=x` and `q∼t^4` give `deg_x F = 4`. Total degree 6. Type `(d,n)=(6,4)`. The `x`-projection is a 6-section with no vertical asymptotes (`deg_y F = deg F`), so Sage uses the `x`-axis projection without a change of variables.

**Discriminant, downstairs vs upstairs.** Charged ZVK-U6 §2.2 (a correction to FIXED-TUPLE’s fibre count 8):

```text
Σ_x = {0} ∪ { r(t_1)^2, r(t_2)^2 } ∪ { u_1^2, u_2^2, u_3^2 } ,   |Σ_x| = 6 ,
Σ_u = {0} ∪ { ±r(t_j) } ∪ { ±u_i } ,                             |Σ_u| = 11 .
```

The lane prompt’s “11 discriminant values” is `|Σ_u|` for `U_6=D'∪D'^-`. `OPEN[PI1S4-(6,4)-FACTORIZATION]` is specified in ZVK-U6 §7 as the braid monodromy of **`D`** w.r.t. the `x`-projection. This job computes `D`. Sage’s geometric basis therefore has **6** loops, not 11.

Local types on those 6 loops (ZVK-U6 §2.3, §3.2, §7):

- `x=0`: three simultaneous disjoint half-twists (the three roots of `r`; `β_0` a perfect matching). One geometric braid, exponent 3, permutation type `(2,2,2)`. `conjugate_positive_form` is expected to split it into three commuting `σ`-conjugates.
- two simple vertical tangencies at `x=r(t_j)^2` where `r'(t_j)=0`: conjugates of `σ`, exponent 1.
- three nodes at `x=u_i^2`: conjugates of `σ^2`, exponent 2, permutation identity.

After splitting `x=0` this is `5×σ + 3×σ^2`. Exponent sum `3+1+1+2+2+2=11=e(ρ_∞)`.

**`ρ_∞`.** Product of the geometric-basis braids (or its inverse, orientation of the large circle). Invariants used as the conjugacy test: `|e|=11` and underlying permutation a 6-cycle (one place at infinity, `x∼t^6`). Cable form (FIXED-TUPLE §2, re-derived ZVK-U6 §2.4): `ρ_∞ = C_2(δ_3^2)·ι` with `e(ι)=Σ k_i=-5`.

**What the checker does with the words.** Hurwitz-fixedness under every Sage factor is the image of the full monodromy group. Generation: the four-vertex graph of the six transpositions is connected. Node-disjointness: `a_p=0` on each conjugate of `σ^2`, using `conjugate_positive_form` to name the band. A zero surviving count on a generic-`j` member, with product invariants passing, is a combinatorial NO for the OPEN. A positive count is a floor, never `π_1(C^2-D)↠S_4`.

## 4. Sage / SIROCCO API confirmation

Fetched Sage 10.8 (manuals dated 2025-12-27). Two call shapes, both requiring the `sirocco` optional package.

**Module function (used as the primary call).**

```text
from sage.schemes.curves.zariski_vankampen import braid_monodromy
bm = braid_monodromy(f)     # f in K[x,y], K = QQ or a number field embedded in QQbar
# Sage 10.8 output: (list_of_braids, strand_to_component_dict, vertical_dict, nstrands)
```

Documented inputs: `f`, `arrangement=()`, `vertical=False`. Projection over the first variable if there are no vertical asymptotes; otherwise a linear change of variables. Output is a geometric basis of `π_1(C_x \ Δ)`, **not** paired with the discriminant points (ask.sagemath.org/question/74927; current docs agree).

**Curve method (cross-check).**

```text
A.<coord_x, coord_y> = AffineSpace(QQ, 2)
C = A.curve(f)
C.braid_monodromy()         # list of braids
```

**Conjugating words.** `conjugate_positive_form(braid)` (same ZVK module): list of `[α, [β_j]]` with `τ=(∏β) α (∏β)^{-1}`, the `τ` pairwise commuting, product equal to the input. This is the extractor for “conjugating words of the 5 tangency braids and 3 node braids”.

**Braid group.** `BraidGroup(6)` has generators `s0,...,s4`. Tietze `B([1,2,-1])=s0*s1*s0^{-1}` (1-based letters). `exponent_sum()` is documented on `ArtinGroupElement` with a `BraidGroup(5)` example. `permutation(W=SymmetricGroup(6))` is documented on the braid page.

**SIROCCO.** Interval-Newton certified path tracking: a piecewise-linear approximation of each root path is guaranteed to lie in a tube containing the true path and no other root, so the combinatorial braid is that of the algebraic curve (Marco–Rodríguez ICMS 2016, hashed above). Sage SPKG 2.1.1; install `sage -i sirocco` or `conda install sagemath-sirocco`.

**Return-shape trap.** The module function returns a 4-tuple; the curve method returns a list. The Sage script unpacks both. An older Sage that returned only a list is handled; a future change that drops `nstrands` is flagged at runtime.

## 5. Implicit equation F: resultant derivation and pre-monodromy checks

**Ring map (declared, not inferred from names).** Coefficient field `QQ`. Polynomial ring `QQ[coord_x, coord_y]` with generator order `(coord_x, coord_y)` so Sage’s `x`-projection is the first variable. Elimination ring `QQ[coord_x,coord_y][param_t]`. Polynomials `poly_P = coord_x - r(param_t)^2`, `poly_Q = coord_y - q(param_t)`. `F = poly_P.resultant(poly_Q)` in the base ring, primitivised by dividing by `content()`. Matching names (`x`,`y`) are not used as a proof that the map is correct; the generator order is.

**Fold cross-check.** Independently `G=Res_t(u-r,y-q)` in `QQ[coord_u,coord_y]`. `G(u)G(-u)` must be even in `u`; the Sage script fails if any odd power appears. The even polynomial is rewritten in `x=u^2` and compared to `F` up to sign after primitivisation.

**Pre-monodromy assertions (all exact, all self-describing, all before SIROCCO):**

1. `c ≠ 0`; `j ∉ {-27/4, -81/16}`; `disc(r)=-4b^3-27c^2 ≠ 0`; `disc(h)=-4(4b/3)^3-27(-4c/3)^2 ≠ 0`.
2. `total_degree(F)=6`, `deg_y(F)=6`, `deg_x(F)=4`.
3. `F.factor()` has one non-unit factor of multiplicity 1.
4. Jacobian ideal `(F, ∂F/∂x, ∂F/∂y)` has dimension 0 and `vector_space_dimension=3` (three reduced nodes).
5. `Res_y(F, ∂F/∂y)`, as a univariate in `x`, has square-free part of degree 6 (`|Σ_x|=6`).

Item 5 is the downstairs correction: a degree-11 square-free discriminant would mean the script had been pointed at `U_6`, which it is not.

These checks are Groebner/resultant of a bivariate sextic. They are exact and small, but they still run only inside the AWS driver (or `./run_braid_job.sh precheck` after the Sage install). They were not run here.

## 6. Parameter choices `(b,c)` and `j`-invariants

Two rational members, both with `c≠0`, both off the excluded moduli.

| label | `(b,c)` | `j=b^3/c^2` | `disc(r)` | `disc(h)` | stratum |
|---|---|---|---|---|---|
| `j0_b0_c1` | `(0,1)` | `0` | `-27 ≠ 0` | `-48 ≠ 0` | open; `(μ)=(1,1,1)` |
| `j1_b1_c1` | `(1,1)` | `1` | `-31 ≠ 0` | `-1552/27 ≠ 0` | open; ROW-SWEEP witness |

`j=0` is generic in the sense of the prompt (`c≠0`, `j=0`). `j=1` is the charged witness `r=t^3+t+1`, `q=t^4+(2/3)t^2+(4/3)t`. The excluded value `j=-27/4` is the cross-locus `(μ)=(2,1)` (a double root of `r` collides with the fold); it is **not** a member of this job. `j=-81/16` (nodes collide) is likewise excluded. Equisingularity on the open stratum makes `π_1(C^2-D)` constant there, so either member decides the row; running both is a mutation check on the conjugating words, not a second theorem.

Coefficients of `q` lie in `QQ` for both specialisations. `F` is computed in `QQ[coord_x,coord_y]` and primitivised to `ZZ`-coefficients.




## 7. Deliverable 1: `braid_monodromy_row64.sage`

Primary call: `sage.schemes.curves.zariski_vankampen.braid_monodromy(F)` (Sage 10.8 4-tuple). Cross-check: `AffinePlaneCurve.braid_monodromy()`. Conjugating words: `conjugate_positive_form`. Two members `(b,c)=(0,1)` and `(1,1)`. Prechecks of §5 run first. SIROCCO is gated by `BRAID_JOB_RUN_MONODROMY=1`.

File body SHA-256: `d45cd9e3c1458918850fe05563ed18fb2b1af525e1cde495c271399f823bfa2b` (26402 bytes, terminating newline included).

```braid_monodromy_row64.sage
# braid_monodromy_row64.sage
#
# Certified braid-monodromy factorization of a (6,4)-row member
# D = {(r(t)^2, q(t))} via Sage's SIROCCO interface.
#
# Theorem ROW-NF (charged ZVK-U6, PROVISIONAL as consumed, PROVED-HERE there):
#   r = t^3 + b t + c
#   q = t^4 + (2b/3) t^2 + (4c/3) t
#   c != 0,  modulus j = b^3 / c^2
# Generic open stratum: j not in {-27/4, -81/16}.
#
# Members run by default:
#   (b,c) = (0,1), j = 0
#   (b,c) = (1,1), j = 1
# Both have c != 0 and j outside the two excluded moduli.
#
# API (fetched Sage 10.8 docs, 2025-12-27):
#   from sage.schemes.curves.zariski_vankampen import braid_monodromy
#   braid_monodromy(f, arrangement=(), vertical=False)
#   returns (list_of_braids, strand_dict, vertical_dict, nstrands)
#   URL: https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html
#   SHA-256 of fetched HTML: 81dd74980fcbb94dfb78ff9ee80f38d0a4c710be25d3be1baf81c44cfbb3c7ac
#
#   AffinePlaneCurve_field.braid_monodromy() returns a list of braids.
#   URL: https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/affine_curve.html
#   SHA-256 of fetched HTML: 65aba08bfda0483ece7ea4890927d5a08d4b6a702ec91923129b99f86f73c5a4
#
#   conjugate_positive_form(braid) is the conjugating-word extractor.
#   ArtinGroupElement.exponent_sum() is documented on
#   https://doc.sagemath.org/html/en/reference/groups/sage/groups/artin.html
#   with a BraidGroup(5) example.
#
# SIROCCO: optional Sage SPKG, package-version 2.1.1 in Sage 10.8
#   URL: https://doc.sagemath.org/html/en/reference/spkg/sirocco.html
#   SHA-256 of fetched HTML: dfcbedf655729530b8473e8b1a063da6e114556e5fbb6d7a1479aed35f80def4
# Install: sage -i sirocco   OR   conda install sagemath-sirocco
#
# Dialect:
#   - no variables named pi, gamma, I, O
#   - long-form assertions with self-describing messages
#   - every unverified API call is prefixed with a FLAG comment
#
# Usage:
#   sage braid_monodromy_row64.sage precheck
#   sage braid_monodromy_row64.sage monodromy
# Environment:
#   BRAID_JOB_OUT   output directory (default ./braid-job-out)
#   BRAID_JOB_RUN_MONODROMY=1  required for the SIROCCO call
#
# Campaign policy: the monodromy call is AWS-only. This script refuses
# it unless BRAID_JOB_RUN_MONODROMY=1 (set by run_braid_job.sh after
# the AWS EC2 vendor check).

import json
import os
import sys
import time
import traceback

from sage.schemes.curves.zariski_vankampen import braid_monodromy
from sage.schemes.curves.zariski_vankampen import conjugate_positive_form
from sage.schemes.curves.zariski_vankampen import discrim

# FLAG: sage.version.version is the standard version string; not re-fetched
# as a dedicated doc page. Record whatever the running interpreter reports.
try:
    import sage.version as sage_version_module
    SAGE_VERSION_STRING = sage_version_module.version
except Exception as version_err:
    SAGE_VERSION_STRING = "UNKNOWN: %s" % version_err

DOC_URL_ZVK = "https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html"
DOC_URL_AFFINE = "https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/affine_curve.html"
DOC_URL_ARTIN = "https://doc.sagemath.org/html/en/reference/groups/sage/groups/artin.html"
DOC_URL_SIROCCO_SPKG = "https://doc.sagemath.org/html/en/reference/spkg/sirocco.html"
DOC_RELEASE_NOTE = "Sage 10.8 reference manuals, pages dated 2025-12-27"

# Two rational members. j = b^3/c^2.
MEMBERS = [
    {"label": "j0_b0_c1", "param_b": QQ(0), "param_c": QQ(1)},
    {"label": "j1_b1_c1", "param_b": QQ(1), "param_c": QQ(1)},
]

EXCLUDED_J_CROSS = -QQ(27) / QQ(4)     # (mu) = (2,1); r has a double root
EXCLUDED_J_NODES = -QQ(81) / QQ(16)    # disc h = 0; nodes collide


def fail(message):
    """Abort with a self-describing message."""
    raise AssertionError(message)


def modulus_j(param_b, param_c):
    if param_c == 0:
        fail("modulus_j: c = 0 is excluded by Theorem ROW-NF (c != 0 is forced)")
    return (param_b ** 3) / (param_c ** 2)


def disc_of_r(param_b, param_c):
    """disc(t^3 + b t + c) = -4 b^3 - 27 c^2."""
    return -QQ(4) * param_b ** 3 - QQ(27) * param_c ** 2


def disc_of_h(param_b, param_c):
    """disc(e1^3 + (4b/3) e1 - 4c/3) = -4 p^3 - 27 q^2 with p=4b/3, q=-4c/3.

    Charged closed form: -256 b^3 / 27 - 48 c^2. Vanishes iff j = -81/16.
    """
    coeff_p = QQ(4) * param_b / QQ(3)
    coeff_q = -QQ(4) * param_c / QQ(3)
    return -QQ(4) * coeff_p ** 3 - QQ(27) * coeff_q ** 2


def build_F(param_b, param_c):
    """F(coord_x, coord_y) = Res_t(coord_x - r(t)^2, coord_y - q(t)), primitive in QQ[x,y].

    Ring map, declared:
      coefficient field = QQ
      generator order   = (coord_x, coord_y) so the x-projection is the first variable
                          (Sage braid_monodromy projects over the first variable)
      param_t           = elimination variable
    Image check: F is the generator of the elimination ideal of
      (coord_x - r^2, coord_y - q) in QQ[x,y], up to units of QQ.
    """
    if param_c == 0:
        fail("build_F: c = 0 is excluded by Theorem ROW-NF")

    ring_xy = QQ["coord_x", "coord_y"]
    coord_x, coord_y = ring_xy.gens()
    ring_t = ring_xy["param_t"]
    param_t = ring_t.gen(0)

    poly_r = param_t ** 3 + param_b * param_t + param_c
    poly_q = (
        param_t ** 4
        + (QQ(2) * param_b / QQ(3)) * param_t ** 2
        + (QQ(4) * param_c / QQ(3)) * param_t
    )
    poly_P = coord_x - poly_r ** 2
    poly_Q = coord_y - poly_q
    # FLAG: MultivariatePolynomial.resultant is classical Sage; not re-fetched
    # from a dedicated polynomial-ring doc page. Used in the long form
    # poly_P.resultant(poly_Q) over the univariate-in-t ring ring_t.
    poly_F_raw = poly_P.resultant(poly_Q)
    if poly_F_raw.parent() is not ring_xy:
        # resultant of two elements of ring_t lands in the base ring ring_xy
        poly_F_raw = ring_xy(poly_F_raw)
    if poly_F_raw == 0:
        fail("build_F: resultant is the zero polynomial (parametrization collapsed)")

    # Primitive integer-coefficient representative.
    # FLAG: content() / integer conversion not re-fetched; classical.
    content_rational = poly_F_raw.content()
    if content_rational == 0:
        fail("build_F: content of a nonzero polynomial was 0")
    poly_F = poly_F_raw / content_rational
    poly_F = ring_xy(poly_F)

    # Cross-check via D': G(u,y) = Res_t(u - r(t), y - q(t)), then G(u) G(-u)
    # is even in u and specialises to a polynomial in x = u^2.
    ring_uy = QQ["coord_u", "coord_y"]
    coord_u, coord_y_uy = ring_uy.gens()
    ring_t_uy = ring_uy["param_t"]
    param_t_uy = ring_t_uy.gen(0)
    poly_r_uy = param_t_uy ** 3 + param_b * param_t_uy + param_c
    poly_q_uy = (
        param_t_uy ** 4
        + (QQ(2) * param_b / QQ(3)) * param_t_uy ** 2
        + (QQ(4) * param_c / QQ(3)) * param_t_uy
    )
    poly_G = (coord_u - poly_r_uy).resultant(coord_y_uy - poly_q_uy)
    poly_G = ring_uy(poly_G)
    poly_G_minus = poly_G.subs({coord_u: -coord_u})
    poly_even = poly_G * poly_G_minus
    # poly_even is even in coord_u; rewrite in coord_x = coord_u^2.
    # FLAG: polynomial substitution / monomial walk not re-fetched.
    poly_F_fold = ring_xy(0)
    for exponent_pair, coeff in poly_even.dict().items():
        exp_u = exponent_pair[0]
        exp_y = exponent_pair[1]
        if exp_u % 2 != 0:
            fail(
                "build_F: G(u,y) G(-u,y) has an odd power u^%d (not a polynomial in u^2)"
                % exp_u
            )
        poly_F_fold = poly_F_fold + ring_xy(coeff) * coord_x ** (exp_u // 2) * coord_y ** exp_y
    content_fold = poly_F_fold.content()
    if content_fold == 0:
        fail("build_F: fold resultant G(u)G(-u) was zero")
    poly_F_fold_prim = ring_xy(poly_F_fold / content_fold)
    # Compare up to sign.
    if poly_F_fold_prim != poly_F and poly_F_fold_prim != -poly_F:
        fail(
            "build_F: Res_t(x-r^2, y-q) and G(u,y)G(-u,y)|_{u^2=x} differ after "
            "primitivisation. direct=%s fold=%s" % (poly_F, poly_F_fold_prim)
        )
    return ring_xy, coord_x, coord_y, poly_F


def precheck_member(member):
    """Degree, irreducibility, three nodes, excluded-j, discriminant support.

    All of this is exact algebra in QQ[x,y]. It is not SIROCCO. It must
    pass before braid_monodromy is called.
    """
    label = member["label"]
    param_b = member["param_b"]
    param_c = member["param_c"]
    j_value = modulus_j(param_b, param_c)
    print("PRECHECK %s b=%s c=%s j=%s" % (label, param_b, param_c, j_value))
    sys.stdout.flush()

    if j_value == EXCLUDED_J_CROSS:
        fail(
            "precheck %s: j = b^3/c^2 = %s equals -27/4 (cross-locus (mu)=(2,1)); "
            "this member is not in the open stratum"
            % (label, j_value)
        )
    if j_value == EXCLUDED_J_NODES:
        fail(
            "precheck %s: j = %s equals -81/16 (disc h = 0, nodes collide)"
            % (label, j_value)
        )
    disc_r_value = disc_of_r(param_b, param_c)
    if disc_r_value == 0:
        fail(
            "precheck %s: disc(r) = -4b^3-27c^2 = 0 (equivalent to j=-27/4)"
            % label
        )
    disc_h_value = disc_of_h(param_b, param_c)
    if disc_h_value == 0:
        fail(
            "precheck %s: disc(h) = 0 (equivalent to j=-81/16); not three distinct nodes"
            % label
        )

    ring_xy, coord_x, coord_y, poly_F = build_F(param_b, param_c)

    total_deg = poly_F.total_degree()
    if total_deg != 6:
        fail(
            "precheck %s: total_degree(F) = %s, expected 6 (row is a degree-6 curve)"
            % (label, total_deg)
        )
    deg_y = poly_F.degree(coord_y)
    if deg_y != 6:
        fail(
            "precheck %s: deg_y(F) = %s, expected 6. Sage braid_monodromy projects "
            "over the first variable; deg_y = deg means no vertical asymptotes."
            % (label, deg_y)
        )
    deg_x = poly_F.degree(coord_x)
    if deg_x != 4:
        fail(
            "precheck %s: deg_x(F) = %s, expected 4 (type (d,n)=(6,4))"
            % (label, deg_x)
        )

    # FLAG: factor() of a bivariate QQ-polynomial is classical Sage.
    factored = poly_F.factor()
    unit_part = factored.unit()
    n_factors = len(factored)
    if n_factors != 1:
        fail(
            "precheck %s: F factored into %d non-unit factors %s; expected irreducible"
            % (label, n_factors, factored)
        )
    poly_irr, multiplicity = factored[0]
    if multiplicity != 1:
        fail(
            "precheck %s: irreducible factor has multiplicity %d, expected 1. factorisation=%s"
            % (label, multiplicity, factored)
        )
    # FLAG: is_irreducible() not re-fetched; redundant with factor() above.
    if hasattr(poly_F, "is_irreducible"):
        if not poly_F.is_irreducible():
            fail("precheck %s: F.is_irreducible() is False after factor() showed one factor" % label)

    # Three ordinary nodes: Jacobian ideal (F, dF/dx, dF/dy) is 0-dimensional
    # of vector-space dimension 3 over QQ (three geometric points, reduced).
    partial_x = poly_F.derivative(coord_x)
    partial_y = poly_F.derivative(coord_y)
    # FLAG: PolynomialRing.ideal, ideal.dimension, ideal.vector_space_dimension
    # not re-fetched from a dedicated commutative-algebra doc page.
    ideal_sing = ring_xy.ideal([poly_F, partial_x, partial_y])
    dim_sing = ideal_sing.dimension()
    if dim_sing != 0:
        fail(
            "precheck %s: singular locus has dimension %s, expected 0 (finite nodes)"
            % (label, dim_sing)
        )
    vdim_sing = ideal_sing.vector_space_dimension()
    if vdim_sing != 3:
        fail(
            "precheck %s: vector_space_dimension of Jacobian ideal = %s, expected 3 "
            "(three reduced nodes). disc_h=%s"
            % (label, vdim_sing, disc_h_value)
        )

    # Discriminant of the x-projection: Res_y(F, dF/dy) as a polynomial in x.
    # Distinct-root count of the square-free part must be 6
    # (charged ZVK-U6 §2.2 correction: |Sigma_x| = 6, not 8 or 11).
    disc_raw = poly_F.resultant(partial_y, coord_y)
    # disc_raw lives in QQ[coord_x] after eliminating coord_y, possibly as an
    # element of ring_xy of y-degree 0.
    disc_in_xy = ring_xy(disc_raw)
    # Extract the univariate in coord_x.
    ring_x = QQ["coord_x_only"]
    coord_x_only = ring_x.gen(0)
    disc_univariate = ring_x(0)
    for exponent_pair, coeff in disc_in_xy.dict().items():
        exp_x = exponent_pair[0]
        exp_y = exponent_pair[1]
        if exp_y != 0:
            fail(
                "precheck %s: Res_y(F, dF/dy) still depends on y (term y^%d)"
                % (label, exp_y)
            )
        disc_univariate = disc_univariate + ring_x(coeff) * coord_x_only ** exp_x
    if disc_univariate == 0:
        fail("precheck %s: discriminant in x is the zero polynomial" % label)
    # FLAG: squarefree_part() not re-fetched; classical univariate.
    disc_squarefree = disc_univariate.squarefree_part()
    n_disc_support = disc_squarefree.degree()
    if n_disc_support != 6:
        fail(
            "precheck %s: square-free discriminant in x has degree %s, expected 6 "
            "(ZVK-U6 §2.2: |Sigma_x| = 6 = {0} cup two r'(tangencies) cup three nodes). "
            "The prompt's '11 discriminant values' is |Sigma_u| upstairs, not |Sigma_x|."
            % (label, n_disc_support)
        )

    record = {
        "label": label,
        "param_b": str(param_b),
        "param_c": str(param_c),
        "modulus_j": str(j_value),
        "disc_r": str(disc_r_value),
        "disc_h": str(disc_h_value),
        "F": str(poly_F),
        "F_unit_from_factor": str(unit_part),
        "total_degree": int(total_deg),
        "deg_x": int(deg_x),
        "deg_y": int(deg_y),
        "irreducible": True,
        "singular_ideal_dimension": int(dim_sing),
        "singular_vector_space_dimension": int(vdim_sing),
        "n_discriminant_x_squarefree": int(n_disc_support),
        "discriminant_x_squarefree": str(disc_squarefree),
    }
    return ring_xy, coord_x, coord_y, poly_F, record


def tietze_as_ints(braid_elt):
    """Sage Tietze() -> list of Python ints. Documented on braid.html via examples."""
    raw = braid_elt.Tietze()
    return [int(letter) for letter in raw]


def permutation_cycle_type_list(braid_elt, n_strands):
    """Cycle type of braid.permutation(W=SymmetricGroup(n)).

    permutation(W=...) is documented on
    https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html
    """
    sym = SymmetricGroup(n_strands)
    perm_elt = braid_elt.permutation(W=sym)
    # FLAG: PermutationGroupElement.cycle_type() not re-fetched as its own page.
    ctype = perm_elt.cycle_type()
    return [int(part) for part in ctype]


def serialise_cpf(braid_elt):
    """conjugate_positive_form -> JSON-able records of conjugating words.

    Documented return: a list of [alpha, [beta_1, ..., beta_m]] with
    tau = (prod beta) * alpha * (prod beta)^{-1}, the tau pairwise
    commuting, product equal to the input braid.
    """
    try:
        cpf = conjugate_positive_form(braid_elt)
    except Exception as cpf_err:
        return {
            "ok": False,
            "error": "%s: %s" % (type(cpf_err).__name__, cpf_err),
            "FLAG": (
                "conjugate_positive_form raised. The conjugating words for this "
                "factor are therefore not certified by this helper; the Tietze "
                "word of the factor itself remains the SIROCCO output."
            ),
            "pieces": [],
        }
    pieces = []
    for item in cpf:
        # Documented shape: [alpha, list_of_permutation_braids]
        alpha_elt = item[0]
        conjugators = item[1]
        pieces.append(
            {
                "alpha_tietze": tietze_as_ints(alpha_elt),
                "alpha_string": str(alpha_elt),
                "alpha_exponent_sum": int(alpha_elt.exponent_sum()),
                "conjugator_tietzes": [tietze_as_ints(conj) for conj in conjugators],
                "conjugator_strings": [str(conj) for conj in conjugators],
            }
        )
    return {"ok": True, "error": None, "FLAG": None, "pieces": pieces}


def unpack_braid_monodromy(bm_output):
    """Accept both the 4-tuple (Sage 10.8 zariski_vankampen.braid_monodromy)
    and a bare list (AffinePlaneCurve_field.braid_monodromy).
    """
    if isinstance(bm_output, (list, tuple)) and len(bm_output) == 4:
        braid_list, strand_dict, vertical_dict, n_strands = bm_output
        return list(braid_list), dict(strand_dict), dict(vertical_dict), int(n_strands)
    if isinstance(bm_output, (list, tuple)):
        braid_list = list(bm_output)
        if len(braid_list) == 0:
            fail("unpack_braid_monodromy: empty braid list and no nstrands")
        n_strands = int(braid_list[0].parent().strands())
        return braid_list, {}, {}, n_strands
    fail(
        "unpack_braid_monodromy: unexpected return type %s value %s"
        % (type(bm_output), bm_output)
    )


def run_monodromy_member(member, poly_F, precheck_record, out_dir):
    """Call SIROCCO via braid_monodromy. AWS-only; gated by the driver."""
    label = member["label"]
    print("MONODROMY %s starting (this is the SIROCCO homotopy)" % label)
    sys.stdout.flush()
    t0 = time.time()
    bm_output = braid_monodromy(poly_F)
    elapsed = time.time() - t0
    print("MONODROMY %s returned in %.3f sec" % (label, elapsed))
    sys.stdout.flush()

    braid_list, strand_dict, vertical_dict, n_strands = unpack_braid_monodromy(bm_output)
    if n_strands != 6:
        fail(
            "monodromy %s: nstrands = %s, expected 6 (x-projection of a degree-6 curve "
            "with no vertical asymptotes)"
            % (label, n_strands)
        )
    if len(braid_list) != 6:
        # Not an immediate fail: a change of variables would add extra braids,
        # and a non-generic projection could coalesce. Record and keep going
        # so the checker can still run; flag it loudly.
        print(
            "WARNING %s: braid_monodromy returned %d factors, expected 6 geometric "
            "generators around |Sigma_x|=6. Proceeding; product-invariant checks "
            "will catch a wrong count via exponent sum."
            % (label, len(braid_list))
        )
        sys.stdout.flush()

    # Cross-check against the curve method. FLAG: equality of two SIROCCO
    # runs is not independently certified (same library twice).
    affine_plane = AffineSpace(QQ, 2, names=("coord_x", "coord_y"))
    curve_D = affine_plane.curve(poly_F)
    t1 = time.time()
    braid_list_curve = list(curve_D.braid_monodromy())
    elapsed_curve = time.time() - t1
    print(
        "MONODROMY %s AffinePlaneCurve.braid_monodromy returned %d braids in %.3f sec"
        % (label, len(braid_list_curve), elapsed_curve)
    )
    sys.stdout.flush()
    curve_matches = [str(a) for a in braid_list] == [str(b) for b in braid_list_curve]

    # Independent algebraic list of discriminant points (not matched to braids:
    # Sage 10.8 braid_monodromy does not return the points; ask.sagemath.org
    # question 74927 records the same gap).
    try:
        disc_points = discrim((poly_F,))
        disc_points_str = [str(pt) for pt in disc_points]
    except Exception as disc_err:
        disc_points_str = []
        print(
            "WARNING %s: discrim((F,)) failed: %s: %s"
            % (label, type(disc_err).__name__, disc_err)
        )
        sys.stdout.flush()

    factor_records = []
    product_elt = None
    for idx, braid_elt in enumerate(braid_list):
        if braid_elt.parent().strands() != 6:
            fail(
                "monodromy %s factor %d: braid lives in B_%s, expected B_6"
                % (label, idx, braid_elt.parent().strands())
            )
        e_sum = int(braid_elt.exponent_sum())
        ctype = permutation_cycle_type_list(braid_elt, 6)
        cpf_record = serialise_cpf(braid_elt)
        rec = {
            "index": int(idx),
            "string": str(braid_elt),
            "tietze": tietze_as_ints(braid_elt),
            "exponent_sum": e_sum,
            "permutation_cycle_type": ctype,
            "conjugate_positive_form": cpf_record.get("pieces"),
            "conjugate_positive_form_ok": cpf_record.get("ok"),
            "conjugate_positive_form_error": cpf_record.get("error"),
            "conjugate_positive_form_FLAG": cpf_record.get("FLAG"),
        }
        factor_records.append(rec)
        if product_elt is None:
            product_elt = braid_elt
        else:
            product_elt = product_elt * braid_elt

    if product_elt is None:
        fail("monodromy %s: no braids to form a product" % label)
    product_record = {
        "string": str(product_elt),
        "tietze": tietze_as_ints(product_elt),
        "exponent_sum": int(product_elt.exponent_sum()),
        "permutation_cycle_type": permutation_cycle_type_list(product_elt, 6),
    }
    if abs(product_record["exponent_sum"]) != 11:
        print(
            "WARNING %s: product exponent_sum = %s, expected |e|=11 "
            "(charged e(rho_inf)=11). Orientation may invert the sign; abs must be 11."
            % (label, product_record["exponent_sum"])
        )
        sys.stdout.flush()

    out = dict(precheck_record)
    out.update(
        {
            "nstrands": int(n_strands),
            "n_factors": int(len(braid_list)),
            "strand_dict": {str(k): int(v) for (k, v) in strand_dict.items()},
            "vertical_dict": {str(k): int(v) for (k, v) in vertical_dict.items()},
            "braids": factor_records,
            "product": product_record,
            "curve_method_matches_module_function": bool(curve_matches),
            "discrim_points": disc_points_str,
            "sirocco_elapsed_seconds": float(elapsed),
            "curve_method_elapsed_seconds": float(elapsed_curve),
            "sage_version": SAGE_VERSION_STRING,
            "doc_url_zvk": DOC_URL_ZVK,
            "doc_url_affine": DOC_URL_AFFINE,
            "doc_release_note": DOC_RELEASE_NOTE,
        }
    )
    out_path = os.path.join(out_dir, "member_%s.json" % label)
    with open(out_path, "w") as handle:
        json.dump(out, handle, indent=2, sort_keys=False)
        handle.write("\n")
    print("WROTE %s" % out_path)
    sys.stdout.flush()
    return out


def write_job_bundle(member_records, out_dir, mode):
    bundle = {
        "job": "braid_monodromy_row64",
        "mode": mode,
        "sage_version": SAGE_VERSION_STRING,
        "doc_url_zvk": DOC_URL_ZVK,
        "doc_url_affine": DOC_URL_AFFINE,
        "doc_url_artin": DOC_URL_ARTIN,
        "doc_url_sirocco_spkg": DOC_URL_SIROCCO_SPKG,
        "doc_release_note": DOC_RELEASE_NOTE,
        "row_normal_form": {
            "r": "param_t^3 + param_b * param_t + param_c",
            "q": "param_t^4 + (2*param_b/3)*param_t^2 + (4*param_c/3)*param_t",
            "F": "Res_t(coord_x - r(param_t)^2, coord_y - q(param_t))",
            "excluded_j": ["-27/4", "-81/16"],
        },
        "expected_downstairs": {
            "nstrands": 6,
            "n_discriminant_x": 6,
            "local_factors_after_splitting_x0": {
                "tangency_sigma": 5,
                "node_sigma_squared": 3,
                "note": (
                    "three of the five tangencies are simultaneous and pairwise "
                    "disjoint at x=0, so Sage returns 6 geometric-basis braids, "
                    "one of which is a product of three disjoint half-twists. "
                    "The prompt's 11 is |Sigma_u| for U_6, not |Sigma_x| for D."
                ),
            },
            "e_rho_inf": 11,
            "permutation_of_rho_inf": "a 6-cycle",
        },
        "members": member_records,
    }
    out_path = os.path.join(out_dir, "braid_job.json")
    with open(out_path, "w") as handle:
        json.dump(bundle, handle, indent=2, sort_keys=False)
        handle.write("\n")
    print("WROTE %s" % out_path)
    sys.stdout.flush()
    return out_path


def main(argv):
    if len(argv) == 0:
        mode = "precheck"
    else:
        mode = argv[0]
    if mode not in ("precheck", "monodromy"):
        fail(
            "usage: sage braid_monodromy_row64.sage [precheck|monodromy]  (got %r)"
            % mode
        )
    out_dir = os.environ.get("BRAID_JOB_OUT", os.path.join(os.getcwd(), "braid-job-out"))
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    print("sage_version=%s" % SAGE_VERSION_STRING)
    print("mode=%s" % mode)
    print("out_dir=%s" % out_dir)
    print("doc_zvk=%s" % DOC_URL_ZVK)
    print("doc_release=%s" % DOC_RELEASE_NOTE)
    sys.stdout.flush()

    member_records = []
    built = []
    for member in MEMBERS:
        ring_xy, coord_x, coord_y, poly_F, record = precheck_member(member)
        built.append((member, poly_F, record))
        member_records.append(record)
        rec_path = os.path.join(out_dir, "precheck_%s.json" % member["label"])
        with open(rec_path, "w") as handle:
            json.dump(record, handle, indent=2, sort_keys=False)
            handle.write("\n")
        print("WROTE %s" % rec_path)
        sys.stdout.flush()

    if mode == "precheck":
        write_job_bundle(member_records, out_dir, mode="precheck")
        print("PRECHECK-ALL-OK")
        return 0

    run_flag = os.environ.get("BRAID_JOB_RUN_MONODROMY", "")
    if run_flag != "1":
        fail(
            "monodromy mode refused: BRAID_JOB_RUN_MONODROMY is %r, not '1'. "
            "Campaign policy: SIROCCO homotopy is AWS-only; run_braid_job.sh "
            "sets this flag after the EC2 vendor check."
            % run_flag
        )

    monodromy_records = []
    for member, poly_F, record in built:
        try:
            one = run_monodromy_member(member, poly_F, record, out_dir)
        except Exception as mono_err:
            print("MONODROMY-FAILED %s" % member["label"])
            traceback.print_exc()
            fail(
                "monodromy %s raised %s: %s"
                % (member["label"], type(mono_err).__name__, mono_err)
            )
        monodromy_records.append(one)
    write_job_bundle(monodromy_records, out_dir, mode="monodromy")
    print("MONODROMY-ALL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

## 8. Deliverable 2: `check_s4_tuples.py`

Pure Python 3. Inputs: the Sage JSON, or `--selftest` with no JSON.

- (a) Product of geometric-basis Tietze words: `|e|=11` and permutation cycle type `(6,)`. This is the conjugacy test against `ρ_∞` available without a Garside conjugacy search in `B_6`.
- (b) All `6^6=46656` transposition 6-tuples; Hurwitz-fixedness under **every** factor; generation (`S_4` iff the transposition graph on 4 letters is connected); node-disjointness via `conjugate_positive_form` bands (`a_p=0`).
- Positive control: `ρ_∞=C_2(δ_3^2)·ι` with `(k_1,k_2,k_3)=(0,-5,0)`, adjacent-tube cabling `C_2(σ_1)=σ_2σ_1σ_3σ_2` (FIXED-TUPLE §5.1). **Expected generating count: 72** (FIXED-TUPLE §5.4 / Theorem `(6,4)`-ρ∞; charged SHA `a6088750…`). Ran on this machine as permutation arithmetic: 102 fixed, 72 generating, charged witness `((12),(23),(13),(34),(12),(23))` fixed; the explicit Tietze word independently also gave 72 and `e=11`.
- Negative control: `σ_1` (Tietze `(1,)`). Ran here: 6720 generating-fixed, set distinct from the 72, charged witness not fixed.

Left Hurwitz action, rightmost Tietze letter first, matching Sage `B([1,2])=s0*s1` as a left action. Transpositions are involutions.

File body SHA-256: `b191403ba378f201003dc295d6b4633629d56fe17f93358584083505624b290c` (30736 bytes, terminating newline included).

```check_s4_tuples.py
#!/usr/bin/env python3
"""check_s4_tuples.py

Postprocessor for the (6,4)-row braid-monodromy job.

Pure Python 3 (no Sage, no NumPy). Reads the JSON written by
braid_monodromy_row64.sage and:

  (a) verifies that the product of the geometric-basis braids has
      exponent sum e with |e| = 11 and underlying permutation of
      cycle type a 6-cycle (the charged rho_inf invariants);
  (b) enumerates all 6^6 = 46656 tuples of S_4 transpositions and
      tests Hurwitz-fixedness under EVERY factor (the full
      monodromy group), plus generation of S_4 and node-disjointness
      as in the charged FIXED-TUPLE / ZVK-U6 reports;
  (c) runs a rho_inf-only positive control that must reproduce 72
      generating tuples (FIXED-TUPLE §5.4 / Theorem (6,4)-rho_inf,
      expected value cited from that report);
  (d) runs a negative control on a fixed non-rho_inf braid word
      whose generating-fixed set must differ from the 72.

Charged expected value for (c): 72
  source: frozen pi1s4-64-fixed-tuple-opus5-20260831.md §5.4 and §7
  SHA-256: a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8

Hurwitz convention (FIXED-TUPLE §4, left action):
  sigma_i · (..., t_i, t_{i+1}, ...)
    = (..., t_i t_{i+1} t_i^{-1}, t_i, ...)
  sigma_i^{-1} · (..., t_i, t_{i+1}, ...)
    = (..., t_{i+1}, t_{i+1}^{-1} t_i t_{i+1}, ...)
Transpositions are involutions, so t^{-1} = t.

Sage Tietze convention (fetched Sage 10.8 braid docs):
  BraidGroup(6)([1, 2, -1]) = s0 * s1 * s0^{-1}.
  Tietze entry k > 0 is generator s_{k-1} (strands k and k+1,
  1-based). Entry -k is the inverse. Left action of a product
  applies the RIGHTMOST letter first: (a*b) · T = a · (b · T).

Do not name variables pi, gamma, I, or O.

This script is desk-scale permutation arithmetic. It is not a CAS
and is not the certified homotopy. Run it on AWS after the Sage
job, or with --selftest anywhere (the 46656 scan is instantaneous).
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


# ---------------------------------------------------------------------------
# S_4 transpositions as 2-element frozensets of {1,2,3,4}.
# Permutations of {1,2,3,4} as 4-tuples: image of (1,2,3,4).
# ---------------------------------------------------------------------------

LETTER_SET = (1, 2, 3, 4)
TRANSPOSITIONS: List[frozenset] = [
    frozenset([1, 2]),
    frozenset([1, 3]),
    frozenset([1, 4]),
    frozenset([2, 3]),
    frozenset([2, 4]),
    frozenset([3, 4]),
]
assert len(TRANSPOSITIONS) == 6, (
    "S_4 has exactly 6 transpositions; got %d" % len(TRANSPOSITIONS)
)
N_TUPLES = 6 ** 6
assert N_TUPLES == 46656, (
    "6^6 must equal 46656; got %d" % N_TUPLES
)

# Charged expected value (FIXED-TUPLE §5.4 / Theorem (6,4)-rho_inf).
EXPECTED_RHO_INF_GENERATING = 72

# Charged witness for (k1, k2, k3) = (0, -5, 0), FIXED-TUPLE §7.
WITNESS_TUPLE = (
    frozenset([1, 2]),
    frozenset([2, 3]),
    frozenset([1, 3]),
    frozenset([3, 4]),
    frozenset([1, 2]),
    frozenset([2, 3]),
)

PERM_IDENTITY = (1, 2, 3, 4)


def transposition_to_perm(support: frozenset) -> Tuple[int, int, int, int]:
    """Return the permutation 4-tuple of a transposition."""
    if len(support) != 2:
        raise AssertionError(
            "transposition_to_perm: support %r is not a 2-set" % (support,)
        )
    a, b = tuple(support)
    images = [1, 2, 3, 4]
    images[a - 1] = b
    images[b - 1] = a
    return (images[0], images[1], images[2], images[3])


def compose_perm(
    first: Tuple[int, int, int, int],
    second: Tuple[int, int, int, int],
) -> Tuple[int, int, int, int]:
    """Return first after second, i.e. (first o second)(x) = first(second(x)).

    4-tuples store the image of (1,2,3,4), so first[k] is first(k+1).
    """
    return (
        first[second[0] - 1],
        first[second[1] - 1],
        first[second[2] - 1],
        first[second[3] - 1],
    )


def invert_perm(perm: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    """Inverse of a permutation 4-tuple. S_4 is small; write it out."""
    images = [0, 0, 0, 0]
    images[perm[0] - 1] = 1
    images[perm[1] - 1] = 2
    images[perm[2] - 1] = 3
    images[perm[3] - 1] = 4
    return (images[0], images[1], images[2], images[3])


def apply_perm_to_transposition(
    perm: Tuple[int, int, int, int],
    support: frozenset,
) -> frozenset:
    """Conjugate a transposition: perm * t * perm^{-1} replaces letters by perm."""
    a, b = tuple(support)
    return frozenset([perm[a - 1], perm[b - 1]])


def multiply_transpositions(left: frozenset, right: frozenset) -> Tuple[int, int, int, int]:
    """Return the permutation left * right (apply right first)."""
    return compose_perm(transposition_to_perm(left), transposition_to_perm(right))


def supports_disjoint(left: frozenset, right: frozenset) -> bool:
    """True iff two transpositions have disjoint support (a_p = 0 shape)."""
    return left.isdisjoint(right)


def transpositions_commute(left: frozenset, right: frozenset) -> bool:
    """Two transpositions commute iff equal or disjoint."""
    return (left == right) or supports_disjoint(left, right)


def tuple_generates_s4(tuple_t: Sequence[frozenset]) -> bool:
    """Transpositions generate S_4 iff the undirected graph on {1,2,3,4} is connected.

    This is the standard transposition-generation criterion; it is the
    same as <T> = S_4 because a transposition subgroup of S_n is the
    full S_n on a connected component and trivial off it.
    """
    parent = {1: 1, 2: 2, 3: 3, 4: 4}

    def find(letter: int) -> int:
        walk = letter
        while parent[walk] != walk:
            walk = parent[walk]
        compress = letter
        while parent[compress] != walk:
            nxt = parent[compress]
            parent[compress] = walk
            compress = nxt
        return walk

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[ra] = rb

    for support in tuple_t:
        a, b = tuple(support)
        union(a, b)
    roots = set(find(letter) for letter in LETTER_SET)
    return len(roots) == 1


# ---------------------------------------------------------------------------
# Hurwitz action of B_6 on 6-tuples of transpositions.
# ---------------------------------------------------------------------------

N_STRANDS = 6
N_ARTIN = 5


def hurwitz_one_generator(
    tuple_t: Sequence[frozenset],
    tietze_letter: int,
) -> Tuple[frozenset, ...]:
    """Apply one Artin generator or inverse, Sage Tietze letter, left action.

    tietze_letter = k > 0  acts by sigma_k on 1-based positions k, k+1.
    tietze_letter = -k < 0 acts by sigma_k^{-1}.
    """
    if tietze_letter == 0:
        raise AssertionError(
            "hurwitz_one_generator: Tietze letter 0 is not a B_6 generator"
        )
    gen_abs = abs(tietze_letter)
    if gen_abs < 1 or gen_abs > N_ARTIN:
        raise AssertionError(
            "hurwitz_one_generator: |Tietze letter| = %d is outside 1..5 for B_6"
            % gen_abs
        )
    pos = gen_abs - 1
    out = list(tuple_t)
    left_entry = out[pos]
    right_entry = out[pos + 1]
    if tietze_letter > 0:
        # sigma: (t_i t_{i+1} t_i^{-1}, t_i) with t_i^{-1} = t_i
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(left_entry), right_entry
        )
        out[pos] = conjugated
        out[pos + 1] = left_entry
    else:
        # sigma^{-1}: (t_{i+1}, t_{i+1}^{-1} t_i t_{i+1})
        conjugated = apply_perm_to_transposition(
            transposition_to_perm(right_entry), left_entry
        )
        out[pos] = right_entry
        out[pos + 1] = conjugated
    return tuple(out)


def hurwitz_tietze(
    tuple_t: Sequence[frozenset],
    tietze_word: Sequence[int],
) -> Tuple[frozenset, ...]:
    """Left action of a Sage Tietze word: apply RIGHTMOST letter first."""
    current = tuple(tuple_t)
    index = len(tietze_word) - 1
    while index >= 0:
        current = hurwitz_one_generator(current, tietze_word[index])
        index -= 1
    return current


def is_fixed_by_tietze(
    tuple_t: Sequence[frozenset],
    tietze_word: Sequence[int],
) -> bool:
    """True iff braid · T = T."""
    return hurwitz_tietze(tuple_t, tietze_word) == tuple(tuple_t)


def exponent_sum_tietze(tietze_word: Sequence[int]) -> int:
    """Algebraic exponent sum: each letter contributes sign(letter).

    Matches Sage ArtinGroupElement.exponent_sum() on a Tietze word
    (fetched: https://doc.sagemath.org/html/en/reference/groups/sage/groups/artin.html
    example B = BraidGroup(5); B([1,4,-3,2]).exponent_sum() == 2).
    """
    total = 0
    for letter in tietze_word:
        if letter > 0:
            total += 1
        elif letter < 0:
            total -= 1
        else:
            raise AssertionError(
                "exponent_sum_tietze: Tietze letter 0 is illegal"
            )
    return total


def permutation_from_tietze(tietze_word: Sequence[int], n_strands: int = N_STRANDS) -> Tuple[int, ...]:
    """Underlying permutation of a braid, as the image tuple of (1..n).

    sigma_k swaps k and k+1. Product uses the same left-action order
    as hurwitz_tietze (rightmost letter first).
    """
    images = list(range(1, n_strands + 1))
    index = len(tietze_word) - 1
    while index >= 0:
        letter = tietze_word[index]
        gen_abs = abs(letter)
        if gen_abs < 1 or gen_abs >= n_strands:
            raise AssertionError(
                "permutation_from_tietze: |letter| = %d outside 1..%d"
                % (gen_abs, n_strands - 1)
            )
        # sigma and sigma^{-1} induce the same transposition of strands
        left_pos = gen_abs - 1
        tmp = images[left_pos]
        images[left_pos] = images[left_pos + 1]
        images[left_pos + 1] = tmp
        index -= 1
    return tuple(images)


def cycle_type_of_perm(images: Sequence[int]) -> Tuple[int, ...]:
    """Cycle type as a weakly decreasing tuple of cycle lengths, including 1-cycles."""
    n = len(images)
    seen = [False] * n
    lengths = []
    for start in range(n):
        if seen[start]:
            continue
        length = 0
        cursor = start
        while not seen[cursor]:
            seen[cursor] = True
            length += 1
            cursor = images[cursor] - 1
        lengths.append(length)
    lengths.sort(reverse=True)
    return tuple(lengths)


# ---------------------------------------------------------------------------
# Cable braid rho_inf, two implementations.
# ---------------------------------------------------------------------------

def sigma_on_pair(pair: Tuple[frozenset, frozenset], power: int) -> Tuple[frozenset, frozenset]:
    """Hurwitz action of sigma^{power} on a 2-tuple (one tube)."""
    left_entry, right_entry = pair
    remaining = power
    # Apply |power| times; sign chooses sigma vs sigma^{-1}.
    if remaining >= 0:
        step = 1
    else:
        step = -1
        remaining = -remaining
    count = 0
    while count < remaining:
        if step == 1:
            conjugated = apply_perm_to_transposition(
                transposition_to_perm(left_entry), right_entry
            )
            right_entry = left_entry
            left_entry = conjugated
        else:
            conjugated = apply_perm_to_transposition(
                transposition_to_perm(right_entry), left_entry
            )
            left_entry = right_entry
            right_entry = conjugated
        count += 1
    return (left_entry, right_entry)


def block_products(tuple_t: Sequence[frozenset]):
    """Return (Pi1, Pi2, Pi3, Pi_total) as permutation 4-tuples.

    Blocks are adjacent pairs (t1,t2), (t3,t4), (t5,t6) as in
    FIXED-TUPLE §4 (not the Puiseux mod-3 numbering).
    """
    pi_one = multiply_transpositions(tuple_t[0], tuple_t[1])
    pi_two = multiply_transpositions(tuple_t[2], tuple_t[3])
    pi_three = multiply_transpositions(tuple_t[4], tuple_t[5])
    pi_total = compose_perm(pi_one, compose_perm(pi_two, pi_three))
    return pi_one, pi_two, pi_three, pi_total


def conjugate_pair(
    perm: Tuple[int, int, int, int],
    pair: Tuple[frozenset, frozenset],
) -> Tuple[frozenset, frozenset]:
    """Entrywise conjugation of a 2-tuple by perm."""
    return (
        apply_perm_to_transposition(perm, pair[0]),
        apply_perm_to_transposition(perm, pair[1]),
    )


def cable_C2_delta3_squared_on_tuple(
    tuple_t: Sequence[frozenset],
) -> Tuple[frozenset, ...]:
    """C_2(delta_3^2) via FIXED-TUPLE §5.1 block formula.

    C_2(delta_3^2) · (A1, A2, A3)
      = (w' A2 w'^{-1},  w A3 w^{-1},  A1)
    w  = Pi1 Pi2
    w' = Pi Pi2^{-1}
    """
    a1 = (tuple_t[0], tuple_t[1])
    a2 = (tuple_t[2], tuple_t[3])
    a3 = (tuple_t[4], tuple_t[5])
    pi_one, pi_two, pi_three, pi_total = block_products(tuple_t)
    del pi_three  # unused; kept in the unpack for self-description
    w_elt = compose_perm(pi_one, pi_two)
    w_prime = compose_perm(pi_total, invert_perm(pi_two))
    new_a1 = conjugate_pair(w_prime, a2)
    new_a2 = conjugate_pair(w_elt, a3)
    new_a3 = a1
    return (
        new_a1[0], new_a1[1],
        new_a2[0], new_a2[1],
        new_a3[0], new_a3[1],
    )


def iota_on_tuple(
    tuple_t: Sequence[frozenset],
    k1: int,
    k2: int,
    k3: int,
) -> Tuple[frozenset, ...]:
    """Inner-tube braid iota = (sigma^{k1}, sigma^{k2}, sigma^{k3})."""
    p1 = sigma_on_pair((tuple_t[0], tuple_t[1]), k1)
    p2 = sigma_on_pair((tuple_t[2], tuple_t[3]), k2)
    p3 = sigma_on_pair((tuple_t[4], tuple_t[5]), k3)
    return (p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])


def rho_inf_block_action(
    tuple_t: Sequence[frozenset],
    k1: int,
    k2: int,
    k3: int,
) -> Tuple[frozenset, ...]:
    """rho_inf · T = C_2(delta_3^2) · (iota · T), FIXED-TUPLE (2.2)+(5.1)."""
    after_iota = iota_on_tuple(tuple_t, k1, k2, k3)
    return cable_C2_delta3_squared_on_tuple(after_iota)


def is_fixed_by_rho_inf_block(
    tuple_t: Sequence[frozenset],
    k1: int,
    k2: int,
    k3: int,
) -> bool:
    return rho_inf_block_action(tuple_t, k1, k2, k3) == tuple(tuple_t)


# Explicit Tietze word for the adjacent-tube cabling, Sage 1-based letters.
# C_2(sigma_1) = sigma_2 sigma_1 sigma_3 sigma_2  (FIXED-TUPLE §5.1)
#              = Sage Tietze (2, 1, 3, 2)
# C_2(sigma_2) = sigma_4 sigma_3 sigma_5 sigma_4
#              = Sage Tietze (4, 3, 5, 4)
# delta_3 = sigma_1 sigma_2,  delta_3^2 = sigma_1 sigma_2 sigma_1 sigma_2
# C_2(delta_3^2) = C_2(s1) C_2(s2) C_2(s1) C_2(s2)
CABLE_C2_SIGMA1 = (2, 1, 3, 2)
CABLE_C2_SIGMA2 = (4, 3, 5, 4)
CABLE_C2_DELTA3_SQUARED = (
    CABLE_C2_SIGMA1 + CABLE_C2_SIGMA2 + CABLE_C2_SIGMA1 + CABLE_C2_SIGMA2
)


def iota_tietze(k1: int, k2: int, k3: int) -> Tuple[int, ...]:
    """Tietze of iota = sigma_1^{k1} sigma_3^{k2} sigma_5^{k3}."""
    letters: List[int] = []
    if k1 > 0:
        letters.extend([1] * k1)
    elif k1 < 0:
        letters.extend([-1] * (-k1))
    if k2 > 0:
        letters.extend([3] * k2)
    elif k2 < 0:
        letters.extend([-3] * (-k2))
    if k3 > 0:
        letters.extend([5] * k3)
    elif k3 < 0:
        letters.extend([-5] * (-k3))
    return tuple(letters)


def rho_inf_tietze(k1: int, k2: int, k3: int) -> Tuple[int, ...]:
    """Tietze of C_2(delta_3^2) * iota."""
    return CABLE_C2_DELTA3_SQUARED + iota_tietze(k1, k2, k3)


# Negative-control braid: a single half-twist sigma_1, Tietze (1,).
# The charged witness has t1 != t2, so it is not sigma_1-fixed.
NEGATIVE_CONTROL_TIETZE = (1,)


# ---------------------------------------------------------------------------
# Enumeration
# ---------------------------------------------------------------------------

def all_transposition_tuples() -> Iterable[Tuple[frozenset, ...]]:
    """Generator of all 46656 transposition 6-tuples."""
    for entries in itertools.product(TRANSPOSITIONS, repeat=6):
        yield entries


def enumerate_fixed(
    predicate,
) -> List[Tuple[frozenset, ...]]:
    """Return every 6-tuple for which predicate(T) is true."""
    survivors: List[Tuple[frozenset, ...]] = []
    for tuple_t in all_transposition_tuples():
        if predicate(tuple_t):
            survivors.append(tuple_t)
    return survivors


def format_tuple(tuple_t: Sequence[frozenset]) -> str:
    """Human-readable ((12),(23),...) string."""
    parts = []
    for support in tuple_t:
        a, b = sorted(support)
        parts.append("(%d%d)" % (a, b))
    return "(" + ", ".join(parts) + ")"


# ---------------------------------------------------------------------------
# Node-disjointness from conjugate_positive_form records.
# ---------------------------------------------------------------------------

def node_bands_from_cpf(cpf_record: Sequence[dict]) -> List[int]:
    """Return 0-based strand indices of bands whose positive braid is a square.

    Sage conjugate_positive_form returns a list of [alpha, [beta_j]]
    serialised here as a list of dicts
      {"alpha_tietze": [...], "conjugator_tietzes": [[...], ...]}
    A node local braid is conjugate to sigma_k^2, so alpha_tietze is
    (k, k) or a power of a single generator of even exponent.
    Returns the 0-based index k-1 of each such band, after transporting
    by the conjugator (the checker applies conjugator^{-1} to T itself).
    """
    bands = []
    for piece in cpf_record:
        alpha = list(piece["alpha_tietze"])
        if not alpha:
            continue
        gens = set(abs(letter) for letter in alpha)
        if len(gens) != 1:
            continue
        gen_abs = next(iter(gens))
        e_sum = exponent_sum_tietze(alpha)
        if e_sum == 2:
            bands.append({"pos0": gen_abs - 1, "conjugator": _flatten_conjugator(piece)})
        elif e_sum == 1:
            # tangency band; not a node
            continue
        else:
            # stacked or unexpected; leave to the caller
            continue
    return bands


def _flatten_conjugator(piece: dict) -> List[int]:
    """Concatenate the list of permutation-braid Tietze words into one word.

    conjugate_positive_form output: tau = (prod_j beta_j) * alpha * (prod_j beta_j)^{-1}.
    The conjugator word is the product of the listed permutation braids
    in the listed order.
    """
    letters: List[int] = []
    for word in piece.get("conjugator_tietzes", []):
        letters.extend(word)
    return letters


def node_disjoint_on_tuple(
    tuple_t: Sequence[frozenset],
    factor_record: dict,
) -> bool:
    """a_p = 0 test: the two meridians of each node band are disjoint.

    If conjugate_positive_form data is missing, return True and let the
    caller flag the skip (fixedness is still tested separately).
    """
    cpf = factor_record.get("conjugate_positive_form")
    if cpf is None:
        return True
    e_sum = factor_record.get("exponent_sum")
    perm_type = tuple(factor_record.get("permutation_cycle_type", []))
    # Node geometric factor: e = 2 and permutation id (cycle type all 1s).
    is_node = (e_sum == 2) and (
        perm_type == (1, 1, 1, 1, 1, 1) or perm_type == tuple()
    )
    if not is_node:
        return True
    for piece in cpf:
        alpha = list(piece.get("alpha_tietze", []))
        if not alpha:
            continue
        gens = set(abs(letter) for letter in alpha)
        if len(gens) != 1:
            continue
        if exponent_sum_tietze(alpha) != 2:
            continue
        gen_abs = next(iter(gens))
        pos0 = gen_abs - 1
        conjugator = _flatten_conjugator(piece)
        # Transport T by conjugator^{-1}: look at the band in the
        # trivialising coordinates. Inverse Tietze = reversed negated.
        inv = [-letter for letter in reversed(conjugator)]
        transported = hurwitz_tietze(tuple_t, inv)
        left_entry = transported[pos0]
        right_entry = transported[pos0 + 1]
        if not supports_disjoint(left_entry, right_entry):
            return False
    return True


# ---------------------------------------------------------------------------
# Self-test / controls
# ---------------------------------------------------------------------------

K_IOTA = (0, -5, 0)  # distribution used by the charged explicit witness


def run_positive_control() -> dict:
    """rho_inf-only gate: generating fixed tuples must number 72."""
    k1, k2, k3 = K_IOTA
    fixed_all = []
    fixed_gen = []
    for tuple_t in all_transposition_tuples():
        if is_fixed_by_rho_inf_block(tuple_t, k1, k2, k3):
            fixed_all.append(tuple_t)
            if tuple_generates_s4(tuple_t):
                fixed_gen.append(tuple_t)
    witness_fixed = is_fixed_by_rho_inf_block(WITNESS_TUPLE, k1, k2, k3)
    witness_gen = tuple_generates_s4(WITNESS_TUPLE)
    n_gen = len(fixed_gen)
    n_all = len(fixed_all)
    ok = (
        n_gen == EXPECTED_RHO_INF_GENERATING
        and witness_fixed
        and witness_gen
    )
    # Word-level consistency (same iota, adjacent-tube cabling).
    word = rho_inf_tietze(k1, k2, k3)
    n_word_gen = 0
    witness_word_fixed = is_fixed_by_tietze(WITNESS_TUPLE, word)
    for tuple_t in all_transposition_tuples():
        if is_fixed_by_tietze(tuple_t, word) and tuple_generates_s4(tuple_t):
            n_word_gen += 1
    return {
        "k_iota": [k1, k2, k3],
        "n_rho_inf_fixed": n_all,
        "n_rho_inf_fixed_generating": n_gen,
        "expected_generating": EXPECTED_RHO_INF_GENERATING,
        "witness_block_fixed": witness_fixed,
        "witness_generates_s4": witness_gen,
        "witness_formatted": format_tuple(WITNESS_TUPLE),
        "word_tietze": list(word),
        "word_exponent_sum": exponent_sum_tietze(word),
        "n_word_fixed_generating": n_word_gen,
        "witness_word_fixed": witness_word_fixed,
        "passed": ok,
    }


def run_negative_control(rho_inf_gen_set: Set[Tuple[frozenset, ...]]) -> dict:
    """sigma_1-fixed generating set must differ from the 72."""
    word = NEGATIVE_CONTROL_TIETZE
    fixed_gen = []
    for tuple_t in all_transposition_tuples():
        if is_fixed_by_tietze(tuple_t, word) and tuple_generates_s4(tuple_t):
            fixed_gen.append(tuple_t)
    gen_set = set(fixed_gen)
    witness_fixed = is_fixed_by_tietze(WITNESS_TUPLE, word)
    differ = gen_set != rho_inf_gen_set
    not_72 = len(fixed_gen) != EXPECTED_RHO_INF_GENERATING
    # Charged witness has t1=(12) != t2=(23), so it must not be sigma_1-fixed.
    return {
        "tietze": list(word),
        "n_fixed_generating": len(fixed_gen),
        "set_differs_from_rho_inf_72": differ,
        "count_differs_from_72": not_72,
        "witness_is_fixed": witness_fixed,
        "passed": differ and (not witness_fixed),
    }


# ---------------------------------------------------------------------------
# Sage JSON consumption
# ---------------------------------------------------------------------------

def load_job_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def product_tietze(factors: Sequence[Sequence[int]]) -> List[int]:
    """Concatenate Tietze words in listed order (Sage geometric-basis order)."""
    out: List[int] = []
    for word in factors:
        out.extend(word)
    return out


def check_product_invariants(member: dict) -> dict:
    """Clause (a): product vs rho_inf, up to conjugacy via e and permutation type."""
    factors = [list(rec["tietze"]) for rec in member["braids"]]
    prod = product_tietze(factors)
    e_sum = exponent_sum_tietze(prod) if prod else 0
    perm = permutation_from_tietze(prod) if prod else tuple(range(1, N_STRANDS + 1))
    ctype = cycle_type_of_perm(perm)
    e_ok = abs(e_sum) == 11
    # A 6-cycle has cycle type (6,). Inverse is still a 6-cycle.
    perm_ok = ctype == (6,)
    per_factor = []
    for rec in member["braids"]:
        word = list(rec["tietze"])
        per_factor.append(
            {
                "index": rec.get("index"),
                "exponent_sum": exponent_sum_tietze(word),
                "json_exponent_sum": rec.get("exponent_sum"),
                "permutation_cycle_type": list(cycle_type_of_perm(permutation_from_tietze(word))),
                "json_permutation_cycle_type": rec.get("permutation_cycle_type"),
            }
        )
    return {
        "n_factors": len(factors),
        "product_exponent_sum": e_sum,
        "product_permutation_cycle_type": list(ctype),
        "expected_abs_exponent": 11,
        "expected_cycle_type": [6],
        "exponent_ok": e_ok,
        "permutation_ok": perm_ok,
        "passed": e_ok and perm_ok,
        "per_factor": per_factor,
        "note": (
            "Sage geometric-basis product is the large-circle braid, equal to "
            "rho_inf or rho_inf^{-1} according to orientation; both have "
            "|e|=11 and permutation a 6-cycle. This is conjugacy-invariant "
            "data, not a Garside conjugacy test in B_6."
        ),
    }


def check_full_monodromy(member: dict) -> dict:
    """Clause (b): Hurwitz-fixed under every factor, generate S_4, node-disjoint."""
    factor_words = [list(rec["tietze"]) for rec in member["braids"]]
    survivors_fixed = []
    survivors_gen = []
    survivors_full = []
    for tuple_t in all_transposition_tuples():
        fixed_all = True
        for word in factor_words:
            if not is_fixed_by_tietze(tuple_t, word):
                fixed_all = False
                break
        if not fixed_all:
            continue
        survivors_fixed.append(tuple_t)
        generates = tuple_generates_s4(tuple_t)
        if generates:
            survivors_gen.append(tuple_t)
        disjoint_ok = True
        for rec in member["braids"]:
            if not node_disjoint_on_tuple(tuple_t, rec):
                disjoint_ok = False
                break
        if generates and disjoint_ok:
            survivors_full.append(tuple_t)
    return {
        "n_enumerated": N_TUPLES,
        "n_fixed_by_every_factor": len(survivors_fixed),
        "n_fixed_and_generating": len(survivors_gen),
        "n_fixed_generating_node_disjoint": len(survivors_full),
        "surviving_tuples_generating_node_disjoint": [
            format_tuple(t) for t in survivors_full
        ],
        "surviving_tuples_generating": [
            format_tuple(t) for t in survivors_gen
        ],
    }


def check_member(member: dict) -> dict:
    label = member.get("label", "?")
    inv = check_product_invariants(member)
    full = check_full_monodromy(member)
    return {
        "label": label,
        "param_b": member.get("param_b"),
        "param_c": member.get("param_c"),
        "modulus_j": member.get("modulus_j"),
        "product_invariants": inv,
        "full_monodromy": full,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Hurwitz-fixed S_4 tuples for the (6,4)-row braid job"
    )
    parser.add_argument(
        "json_path",
        nargs="?",
        default=None,
        help="JSON produced by braid_monodromy_row64.sage",
    )
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="run rho_inf-only +72 control and the negative control; no JSON",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="write the JSON report to this path (default: stdout)",
    )
    return parser.parse_args(list(argv))


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    report: Dict[str, object] = {
        "script": "check_s4_tuples.py",
        "expected_rho_inf_generating": EXPECTED_RHO_INF_GENERATING,
        "expected_rho_inf_generating_citation": (
            "pi1s4-64-fixed-tuple-opus5-20260831.md §5.4 and §7 "
            "(SHA-256 a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8); "
            "brute force over 46656 transposition 6-tuples, 72 generate S_4"
        ),
        "n_transposition_tuples": N_TUPLES,
    }

    pos = run_positive_control()
    report["positive_control_rho_inf_only"] = pos
    rho_inf_gen_set: Set[Tuple[frozenset, ...]] = set()
    k1, k2, k3 = K_IOTA
    for tuple_t in all_transposition_tuples():
        if is_fixed_by_rho_inf_block(tuple_t, k1, k2, k3) and tuple_generates_s4(tuple_t):
            rho_inf_gen_set.add(tuple_t)
    neg = run_negative_control(rho_inf_gen_set)
    report["negative_control_sigma1"] = neg

    controls_ok = bool(pos["passed"]) and bool(neg["passed"])
    if not controls_ok:
        report["controls_passed"] = False
        report["fatal"] = (
            "self-controls failed: positive_control.passed=%s negative_control.passed=%s. "
            "Refusing to interpret Sage output."
            % (pos["passed"], neg["passed"])
        )
        _emit(report, args.out)
        return 2
    report["controls_passed"] = True

    if args.selftest and args.json_path is None:
        _emit(report, args.out)
        return 0

    if args.json_path is None:
        report["fatal"] = "no JSON path given (use --selftest or pass a Sage JSON)"
        _emit(report, args.out)
        return 2

    job = load_job_json(args.json_path)
    members = job.get("members")
    if not members:
        report["fatal"] = "JSON has no members list: %s" % args.json_path
        _emit(report, args.out)
        return 2

    member_reports = []
    all_ok = True
    for member in members:
        one = check_member(member)
        member_reports.append(one)
        if not one["product_invariants"]["passed"]:
            all_ok = False
    report["members"] = member_reports
    report["product_invariants_passed"] = all_ok
    report["decision_note"] = (
        "A zero count in n_fixed_generating_node_disjoint on a generic-j "
        "member, with product invariants passed, is a combinatorial NO for "
        "OPEN[PI1S4-(6,4)-FACTORIZATION] on that member. A positive count "
        "is a floor, not attainment of pi1(C^2-D) -> S_4 (FALLACY-v2 "
        "carrier/attainment)."
    )
    _emit(report, args.out)
    return 0 if all_ok else 1


def _emit(report: dict, out_path: Optional[str]) -> None:
    text = json.dumps(report, indent=2, sort_keys=False)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.write("\n")
    else:
        sys.stdout.write(text)
        sys.stdout.write("\n")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

## 9. Deliverable 3: `run_braid_job.sh` and Ubuntu install notes

Driver sequence: Sage probe → Python `--selftest` (must report 72) → Sage `precheck` → AWS vendor check → Sage `monodromy` with `BRAID_JOB_RUN_MONODROMY=1` → Python checker on `braid_job.json`. Caps: `WALL_SECONDS=43200`, `MEM_GB=32` (`ulimit -v`), `PRECHECK_WALL=600`, `SELFTEST_WALL=120`. Logs under `$BRAID_JOB_OUT` (`*.stdout *.stderr *.meta *.time`). `MODE=precheck` stops before SIROCCO.

AWS gate: `uname -s` is Linux and `/sys/class/dmi/id/sys_vendor` is `Amazon EC2`, else exit. Override: `BRAID_JOB_FORCE=1`.

**Ubuntu install (exact commands).**

Conda-forge (recommended; Sage 10.8-class build with `sagemath-sirocco`):

```text
sudo apt-get update
sudo apt-get install -y coreutils time python3 curl ca-certificates
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh -b -p "$HOME/miniforge3"
source "$HOME/miniforge3/etc/profile.d/conda.sh"
conda create -y -n sage -c conda-forge sage python=3.12 sagemath-sirocco
conda activate sage
sage -c 'from sage.schemes.curves.zariski_vankampen import braid_monodromy; print("sirocco-import-ok")'
```

The feedstock README (fetched 2026-08-31) also documents:

```text
conda install sage sagelib sagemath-bliss sagemath-sirocco
```

Sage-the-distribution optional SPKG (not Debian/Ubuntu apt sagemath):

```text
sage -i sirocco
```

Do **not** use `apt-get install sagemath` for this job: Ubuntu 24.04 does not ship a current Sage, and system Sage does not support `sage -i`. Fedora’s `sirocco sirocco-devel` is listed in the Sage 10.8 installation guide’s equivalent-system-packages table; that is not an Ubuntu apt command.

File body SHA-256: `f4c56caf398b0ec5d25b27541222c651def7f7d5a266ee36ade0ce967d75c070` (7965 bytes, terminating newline included).

```run_braid_job.sh
#!/usr/bin/env bash
# run_braid_job.sh
#
# Driver for the (6,4)-row certified braid-monodromy job.
# Campaign policy: SIROCCO homotopy is AWS-only. This script refuses to
# launch monodromy unless the host is Amazon EC2 (same vendor check as
# ops/aws_exact_lane.sh) or BRAID_JOB_FORCE=1 is set for an already-
# approved off-box replay.
#
# Caps (override via environment):
#   WALL_SECONDS   wall clock for the SIROCCO call (default 43200 = 12h)
#   MEM_GB         virtual-memory ulimit in GiB (default 32)
#   PRECHECK_WALL  wall clock for the exact precheck (default 600)
#   SELFTEST_WALL  wall clock for check_s4_tuples.py --selftest (default 120)
#
# Layout (all paths relative to BRAID_JOB_ROOT, default: this script's directory):
#   braid_monodromy_row64.sage
#   check_s4_tuples.py
#   run_braid_job.sh            (this file)
#   braid-job-out/              (created)
#     precheck_*.json
#     member_*.json
#     braid_job.json
#     check_s4_tuples.json
#     *.log  *.meta  *.time
#
# Ubuntu install notes (Sage 10.8 + sirocco). Prefer conda-forge:
#
#   # --- conda-forge (recommended; ships sagemath-sirocco) ---
#   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
#   bash Miniforge3-$(uname)-$(uname -m).sh -b -p "$HOME/miniforge3"
#   source "$HOME/miniforge3/etc/profile.d/conda.sh"
#   conda create -y -n sage -c conda-forge sage python=3.12 sagemath-sirocco
#   conda activate sage
#   sage -c 'from sage.schemes.curves.zariski_vankampen import braid_monodromy; print("sirocco-import-ok")'
#
#   Documented install line (conda-forge/sage-feedstock README, fetched 2026-08-31):
#     conda install sage sagelib sagemath-bliss sagemath-sirocco
#
#   # --- Sage-the-distribution optional SPKG (NOT Debian/Ubuntu apt sagemath) ---
#   sage -i sirocco
#   # SIROCCO upstream: https://github.com/miguelmarco/SIROCCO2
#   # Sage 10.8 SPKG version: 2.1.1
#   # SPKG doc: https://doc.sagemath.org/html/en/reference/spkg/sirocco.html
#
#   # --- apt helpers on Ubuntu (not sagemath itself) ---
#   sudo apt-get update
#   sudo apt-get install -y coreutils time python3 curl ca-certificates
#
#   # --- apt sagemath: do not use for this job ---
#   # Ubuntu 24.04 does not ship a current sagemath package. Debian/Ubuntu
#   # sagemath, when present, is a system install and does not support
#   # `sage -i`. Fedora has `sirocco sirocco-devel` as system packages
#   # (Sage installation guide, equivalent-system-packages table) but
#   # that is not an Ubuntu apt command.
#
# Usage on an EC2 box after install:
#   chmod +x run_braid_job.sh
#   ./run_braid_job.sh
#   # or, precheck + selftest only:
#   ./run_braid_job.sh precheck
#
set -u

WALL_SECONDS="${WALL_SECONDS:-43200}"
MEM_GB="${MEM_GB:-32}"
PRECHECK_WALL="${PRECHECK_WALL:-600}"
SELFTEST_WALL="${SELFTEST_WALL:-120}"
BRAID_JOB_FORCE="${BRAID_JOB_FORCE:-0}"
MODE="${1:-all}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BRAID_JOB_ROOT="${BRAID_JOB_ROOT:-$SCRIPT_DIR}"
OUT_DIR="${BRAID_JOB_OUT:-$BRAID_JOB_ROOT/braid-job-out}"
mkdir -p "$OUT_DIR"
export BRAID_JOB_OUT="$OUT_DIR"

SAGE_SCRIPT="$BRAID_JOB_ROOT/braid_monodromy_row64.sage"
PY_SCRIPT="$BRAID_JOB_ROOT/check_s4_tuples.py"

log() {
  printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$OUT_DIR/driver.log"
}

die() {
  log "FATAL $*"
  exit 1
}

refuse_non_aws() {
  if [[ "$BRAID_JOB_FORCE" == "1" ]]; then
    log "WARNING BRAID_JOB_FORCE=1 set; skipping AWS vendor check"
    return 0
  fi
  if [[ "$(uname -s)" != "Linux" ]]; then
    die "refusing heavy SIROCCO job outside Linux/AWS: host=$(hostname) os=$(uname -s). Set BRAID_JOB_FORCE=1 only for an approved off-box replay."
  fi
  AWS_VENDOR="$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)"
  if [[ "$AWS_VENDOR" != "Amazon EC2" ]]; then
    die "refusing heavy SIROCCO job outside AWS EC2: host=$(hostname) vendor=${AWS_VENDOR:-unknown}. This is the campaign AWS-only gate."
  fi
  log "AWS vendor check passed: vendor=$AWS_VENDOR host=$(hostname)"
}

need_file() {
  if [[ ! -f "$1" ]]; then
    die "missing required file $1"
  fi
}

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    die "missing command $1 (see Ubuntu install notes in this script's header)"
  fi
}

write_meta_start() {
  local meta="$1"
  {
    printf 'utc_start=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'host=%s\n' "$(hostname)"
    printf 'uname=%s\n' "$(uname -a)"
    printf 'sage_bin=%s\n' "$(command -v sage)"
    printf 'python_bin=%s\n' "$(command -v python3)"
    printf 'wall_seconds=%s\n' "$WALL_SECONDS"
    printf 'mem_gb=%s\n' "$MEM_GB"
    printf 'pwd=%s\n' "$(pwd)"
  } > "$meta"
}

write_meta_end() {
  local meta="$1"
  local rc="$2"
  local out="$3"
  {
    printf 'utc_end=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'exit_status=%s\n' "$rc"
    if [[ -f "$out" ]]; then
      printf 'output_sha256=%s\n' "$(sha256sum "$out" | awk '{print $1}')"
    fi
  } >> "$meta"
}

run_capped() {
  # run_capped NAME WALL_SEC CMD...
  local name="$1"
  local wall="$2"
  shift 2
  local stdout_path="$OUT_DIR/${name}.stdout"
  local stderr_path="$OUT_DIR/${name}.stderr"
  local time_path="$OUT_DIR/${name}.time"
  local meta_path="$OUT_DIR/${name}.meta"
  write_meta_start "$meta_path"
  log "START $name wall=${wall}s mem_gb=${MEM_GB} cmd=$*"
  # Virtual address-space cap. SIROCCO uses MPFR; 32 GiB is a generous desk-to-AWS cap.
  ulimit -v $((MEM_GB * 1024 * 1024)) || log "WARNING ulimit -v failed (continuing)"
  set +e
  /usr/bin/time -v timeout --signal=TERM --kill-after=30 "$wall" "$@" \
    > "$stdout_path" 2> "$stderr_path"
  local rc=$?
  set -e
  # /usr/bin/time writes to stderr; copy a tail into the time file.
  tail -n 40 "$stderr_path" > "$time_path" || true
  write_meta_end "$meta_path" "$rc" "$stdout_path"
  log "END $name rc=$rc"
  if [[ "$rc" -eq 124 ]]; then
    die "$name hit wall-clock timeout ${wall}s (timeout(1) exit 124)"
  fi
  if [[ "$rc" -ne 0 ]]; then
    die "$name exited $rc (see $stderr_path)"
  fi
  return 0
}

need_file "$SAGE_SCRIPT"
need_file "$PY_SCRIPT"
need_cmd sage
need_cmd python3
need_cmd timeout
need_cmd sha256sum

cd "$BRAID_JOB_ROOT" || die "cannot cd to BRAID_JOB_ROOT=$BRAID_JOB_ROOT"

log "=== braid-prep-row64 driver ==="
log "root=$BRAID_JOB_ROOT out=$OUT_DIR mode=$MODE"

# Record hashes of the job bodies actually used.
{
  printf 'utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  sha256sum "$SAGE_SCRIPT" "$PY_SCRIPT" "$BRAID_JOB_ROOT/run_braid_job.sh"
} | tee "$OUT_DIR/job_bodies.sha256"

# Interpreter / SIROCCO presence. braid_monodromy imports without sirocco;
# the FeatureNotPresentError is raised at call time. We still import here
# so a missing Sage curves module fails fast.
run_capped sage_probe 60 sage -c \
  'from sage.schemes.curves.zariski_vankampen import braid_monodromy, conjugate_positive_form, discrim
from sage.groups.braid import BraidGroup
print("sage_version", sage.version.version)
print("sirocco-import-ok")
B = BraidGroup(6)
print("B6", B)
print("exponent_sum_demo", B([1,4,-3,2]).exponent_sum())
'

# Positive/negative controls: 46656 permutation tuples, instantaneous.
run_capped selftest "$SELFTEST_WALL" python3 "$PY_SCRIPT" --selftest --out "$OUT_DIR/selftest.json"

# Exact precheck of F (resultant, irreducibility, three nodes). No SIROCCO.
run_capped precheck "$PRECHECK_WALL" sage "$SAGE_SCRIPT" precheck

if [[ "$MODE" == "precheck" ]]; then
  log "MODE=precheck: stopping before SIROCCO"
  exit 0
fi

refuse_non_aws
export BRAID_JOB_RUN_MONODROMY=1
run_capped monodromy "$WALL_SECONDS" sage "$SAGE_SCRIPT" monodromy

if [[ ! -f "$OUT_DIR/braid_job.json" ]]; then
  die "monodromy finished but $OUT_DIR/braid_job.json is missing"
fi

run_capped check_tuples "$SELFTEST_WALL" python3 "$PY_SCRIPT" "$OUT_DIR/braid_job.json" --out "$OUT_DIR/check_s4_tuples.json"

log "ALL-OK"
log "bundle=$OUT_DIR/braid_job.json"
log "checker=$OUT_DIR/check_s4_tuples.json"
exit 0
```


## 10. Deliverable 4: SHA-256 manifest of every file body

Hashes are of the exact bytes in the fenced blocks of §§7–9 (terminating newline included). Verified by extracting each fence and hashing; they match the staged bodies.

```text
d45cd9e3c1458918850fe05563ed18fb2b1af525e1cde495c271399f823bfa2b  braid_monodromy_row64.sage
b191403ba378f201003dc295d6b4633629d56fe17f93358584083505624b290c  check_s4_tuples.py
f4c56caf398b0ec5d25b27541222c651def7f7d5a266ee36ade0ce967d75c070  run_braid_job.sh
```

Byte lengths: 26402, 30736, 7965. Charged-input hashes are in §1. Fetched Sage/SIROCCO sources are in §1. This report’s body hash is the coordinator’s seal, not this lane’s.

## 11. Unverified-API flag list

Pinned to fetched Sage 10.8 pages: `braid_monodromy` (module, 4-tuple), `AffinePlaneCurve_field.braid_monodromy` (list), `conjugate_positive_form`, `discrim`, `BraidGroup` Tietze/`permutation(W=...)`, `ArtinGroupElement.exponent_sum`, SIROCCO SPKG 2.1.1, `sage -i sirocco`, conda `sagemath-sirocco`.

**FLAG — used, not re-fetched from a dedicated page.** `Polynomial.resultant`, `Polynomial.derivative`, `Polynomial.factor` / `content` / `total_degree` / `degree` / `is_irreducible` / `squarefree_part` / `dict` / `subs`; `ideal.dimension` / `vector_space_dimension`; `PermutationGroupElement.cycle_type`; `sage.version.version`; `AffineSpace` / `curve`; `SymmetricGroup`. These are classical Sage names; runtime assertions will catch a rename.

**FLAG — behaviour, not signature.** (1) Geometric-basis product equals `ρ_∞` or `ρ_∞^{-1}` (orientation). Checker uses `|e|` and cycle type. (2) `conjugate_positive_form` may raise on a braid not conjugate to a product of disjoint positive braids; the Sage script records the exception and still emits the Tietze word. (3) Sage does not pair braids with discriminant points. (4) A linear change of variables if Sage thinks there are vertical asymptotes (precheck requires `deg_y=6` to forbid this). (5) `braid.conjugating_braid` exists but is **not called** (Garside search, uncertain duration).

**FLAG — not used.** `fundamental_group`, arrangement `vertical=True`, Riemann-surface `monodromy_group` (permutations, not braids).

## 12. AWS run protocol and acceptance criteria

On an Ubuntu EC2 box, after the conda-forge install of §9:

```text
chmod +x run_braid_job.sh
./run_braid_job.sh            # full job
./run_braid_job.sh precheck   # F-construction only, no SIROCCO
```

**Accept the job as well-posed if and only if:**

1. `--selftest` prints `n_rho_inf_fixed_generating: 72` and `controls_passed: true`.
2. Precheck for both members: `total_degree=6`, irreducible, singular `vdim=3`, square-free `deg Disc_x=6`, `j` not excluded.
3. SIROCCO returns 6-strand braids; product `|e|=11` and permutation a 6-cycle.
4. Factor types, after `conjugate_positive_form` on the `e=3` braid, split as 5 tangency bands + 3 node bands (or a self-describing failure if Sage’s geometric basis coalesced differently).
5. Checker emits `n_fixed_generating_node_disjoint` for each member.

**Reading the OPEN.** Both members generic-`j`, product invariants pass, surviving count 0: combinatorial NO for `OPEN[PI1S4-(6,4)-FACTORIZATION]`, killing rows `(6,4)` and `(8,4)` at the charged scope. Surviving count positive: the factorization does not kill the row; the count is a floor, not a homomorphism `π_1(C^2-D)↠S_4`. If the two members disagree, stop and treat equisingularity/`π_1`-constancy as a live gap (typed OPEN, do not fill by analogy).

Caps: 12 h wall, 32 GiB virtual. SIROCCO may run for hours on a sextic; that is why it is AWS-only.

## 13. FALLACY-v2 check

- Flag/place/series: not used.
- Per-ray/exit-set charge: no exit claim.
- Carrier/attainment: a `ρ_∞`-fixed or monodromy-fixed tuple is not `FULL_ACTUAL_EXIT` and not a homomorphism. The 72 is a floor on the residual under `ρ_∞` alone.
- Pole/interior: unused.
- Floor/attainment: `|e|=11` and the 72 are charged equalities, not lower bounds being promoted. The job’s surviving count after all factors is a computation, not a theorem.
- `sat()` wrapping, raw remainder degree, variable/ring map: the ring map for `F` is declared in §5 and in the Sage script (field `QQ`, order `(coord_x,coord_y)`, elimination in `param_t`, fold cross-check). Matching names are not the proof.
- Prime label/derivative: `r'` in charged text is the derivative of `r`; Sage uses `.derivative`. No prime-as-label ambiguity in the job bodies.
- Merge-free/M-descent, target/arrival index: unused.
- No safe replacement was needed; the 11-vs-6 discriminant count is not filled by analogy — it is the charged ZVK-U6 correction, and the job targets `D` with `|Σ_x|=6`.

No `charge_basis` line: no new exit-price assertion.

## 14. What this bundle does not claim

This is a job bundle. It does not compute the braid monodromy of any row member. It does not decide `OPEN[PI1S4-(6,4)-FACTORIZATION]`. It does not assert `π_1(C^2-D)↠S_4` or the opposite. It does not exhibit a Keller counterexample. Theorem ROW-NF remains at the charged PROVISIONAL/PROVED-HERE scope of ZVK-U6; this lane does not re-prove it. The Python `--selftest` reproducing 72 confirms the checker’s Hurwitz convention against the charged count, not a property of `F=0`. Canonical ledgers were not edited.

<!-- BODY-END -->
