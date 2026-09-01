# BM-FACT-CODEGEN: braid-monodromy decision computation for the realized (9,6,2) curve

Lane: `BM-FACT-CODEGEN`. Date: 2026-09-01. Agent: grok-4.6.
Codegen + desk math. **SIROCCO was not run.** The coordinator runs
`box/bmfact_962.sage monodromy` on AWS (conda env `sage`, SIROCCO
installed) and then `box/bmfact_enum.py` on the JSON.

OPEN targeted: `OPEN[REP-96-BM-FACTORISATION]` (REP-96 §7 R1).

## 0. Hash gate, custody, method

The two charged frozen copies were hashed with `shasum -a 256` **before
any was read**. Both match the charge exactly:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  .../inputs/rep-96-inner-opus5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  .../inputs/encoding-faithfulness-audit-r2-sol56-20260901.md
```

No charged file was edited. `jc2-lean` was not inspected. Campaign
documents consumed on disk and cited by file and section, not re-hashed
as primary: `pi1-s4-decision-opus5-20260831.md` §2 (local braids `(T)` /
`(N_k)`, affine ZvK, no relation at infinity);
`braid-prep-row64-grok46-20260831.md` §4 (Sage 10.8 SIROCCO API, Tietze,
left Hurwitz); Sage 10.8 `zariski_vankampen` HTML (2025-12-27) and the
develop source of `zariski_vankampen.py` (fetched 2026-09-01, which adds
a fifth return value: the geometric-basis base point).

**What was run here.** Two Sage-free programs: `box/bmfact_selfcheck.py`
(sympy resultant, discriminant table) and `box/bmfact_enum.py --selftest`
(class-list expansion, GATE-3 at `k_*=-10`, Pi-tau assertion, positive
and negative controls). Transcripts are §8, verbatim. An independent
lookup-table scan of all `6^9` adjacent-block 9-tuples against CABLE-3
`rho_inf` (not the default selftest) returned 246 product-fixed tuples
of which **144 generate `S_4`**, matching the charged count.

**What was not run.** Sage, SIROCCO, Groebner bases as a decision
procedure (the Sage precheck *will* use a Jacobian ideal on AWS; that is
the coordinator's job). No representation `phi` is claimed; no kill of
`(9,6,2)` is claimed. The outcome of R1 is the coordinator's, after the
JSON exists.

**Ring map, declared once.** Coefficient field `QQ`. Elimination ring
`QQ[coord_x, coord_y][param_t]`, generator order `(coord_x, coord_y)` so
Sage's `x`-projection is the first variable. Polynomials
`p(param_t) - coord_x` and `q(param_t) - coord_y`. Matching names are
not a proof of the map; the generator order and the identity
cross-check in §1 are.

No `charge_basis` line: this report asserts no new exit price.

## 1. The curve and the defining polynomial `F`

The realized `(9,6,2)` curve (AUD §6, re-verified REP-96 §1) is the image
of

```text
q = t^6 + 8 t^2 ,     p = t^9 + 12 t^5 + 24 t ,
(x, y) = (p(t), q(t)) .
```

The identity `p^2 - q^3 - 64 q - 64 t^2 = 0` holds exactly (sympy
expansion, §8). Hence on the curve

```text
x^2 - y^3 - 64 y  =  64 t^2 .
```

`p` is odd, `q` is even, so `t` and `-t` send to `(x,y)` and `(-x,y)`:
as a set, `D` is invariant under `x |-> -x`. It is nevertheless
irreducible: the parametrisation is birational (`gcd(p,p')=1`, the
identity recovers `t^2` and then `t = p / (t^8+12 t^4+24)`), so the
image is an irreducible degree-9 curve.

**Resultant.** `F := Res_t(p-t-x, q-t-y)` is computed in `QQ[x,y]`.
Content 1, bidegree `(deg_x, deg_y) = (6, 9)`, total degree 9,
irreducible over `QQ`. Explicitly

```text
F = x^6 - 3 x^4 y^3 - 192 x^4 y
    + 3 x^2 y^6 + 384 x^2 y^4 + 12288 x^2 y^2 + 32768 x^2
    - y^9 - 192 y^7 - 12288 y^5 - 294912 y^3 - 2359296 y .
```

**Identity substitution, independent of the Sylvester matrix.** Set
`w = x^2 - y^3 - 64 y` and `u = t^2 = w/64`. Then `y = u^3 + 8 u`, so

```text
(w/64)^3 + 8 (w/64) - y  =  0 ,
w^3 + 32768 w - 262144 y  =  0 .
```

The two polynomials are **equal** as elements of `QQ[x,y]`, not merely
associates. `lc_y(F) = -1`, a nonzero constant: no vertical asymptotes,
Sage uses the `x`-projection with no linear change of variables.

**Fibre `x=0`.** `F(0,y) = -y (y^4 + 96 y^2 + 1536)^2`. The simple root
`y=0` is the smooth point `t=0`. The quartic-squared is four double
roots, at `y^2 = -48 \pm 16 sqrt(3)` (two negative reals, four distinct
pure-imaginary `y`). These are the four ordinary nodes, all on `x=0`,
exhausting `delta_aff = 4` (REP-96 §1; AUD §6).

## 2. Discriminant of the `x`-projection, every root

`disc_y F` is a univariate in `x` of degree 16, as required by
`e(rho_inf) = 2 delta_aff + d - 1 = 8 + 8 = 16`. Factorisation over
`QQ`:

```text
disc_y F  =  2^{108} 3^9  ·  x^8  ·  ( 3^9 x^8 + 2^{24}·5·43 x^4 + 2^{47} ) .
```

Square-free support has degree 9: the factor `x` (once, after taking
square-free part) together with an irreducible octic in `x` which is
quadratic in `u = x^4`. The two roots of that quadratic are

```text
u  =  -1803550720/19683  \pm  159383552 sqrt(19) / 19683
```

both nonzero (negative real). Each contributes four distinct fourth
roots of `x`: eight distinct nonzero tangency values. Independently,
`Res_t(p', x-p) = 3^9 · (the same octic)`, degree 8, confirming that
the octic is exactly the tangency locus of `t |-> p(t)` and introduces
no extra finite `x`.

**Verbatim table of every root of `disc_y F`, including infinity.**

| root of `disc_y F` | multiplicity | geometric type |
|---|---:|---|
| `x = 0` | 8 | four ordinary nodes in one fibre; local model `y^2 ~ x^2`, disc valuation 2 per node |
| eight roots of `3^9 x^8 + 2^{24}·5·43 x^4 + 2^{47}` | 1 each | simple vertical tangencies at smooth points, eight distinct fibres |
| `x = infinity` | **not a root** | `lc_y(F) = -1` does not vanish |

Homogenisation: `F_hom(X,Y,Z)|_{Z=0} = -Y^9`. So `Dbar` meets `L_infty`
only at `[1:0:0]`, intersection multiplicity 9, matching
`I(Dbar, L_infty; Q) = d = 9`. The place multiplicity is `a = 3`; this
is a point of the projective curve, not a finite critical value of the
affine `x`-projection. The ramification of `t |-> p(t)` at `t = infinity`
is 8, and is realised as the **product** of the nine finite
geometric-basis braids (`rho_inf`), not as an extra finite root.

This is the REP-96 §1 census, re-derived from `F` rather than from the
parametrisation: eight simple tangency fibres plus one fibre `x=0`
carrying four nodes; exponent ledger `8·1 + 4·2 = 16`. The Sage script
**aborts with the marker `CENSUS-DISAGREES-REP96`** if SIROCCO's
factorisation disagrees. A disagreement would refute REP-96 §1 and must
surface.

## 3. Sage / SIROCCO entry point and conventions

Primary call, identical in shape to the promoted `(6,4)` braid job:

```text
from sage.schemes.curves.zariski_vankampen import braid_monodromy
bm = braid_monodromy(F)     # F in QQ[coord_x, coord_y]
```

Sage 10.8 manuals (2025-12-27) document a **4-tuple**
`(list_of_braids, strand_dict, vertical_dict, nstrands)`. The develop
source of `zariski_vankampen.py`, fetched 2026-09-01, returns a
**5-tuple** whose fifth slot is the geometric-basis base point `p1`.
`box/bmfact_962.sage` unpacks both. Cross-check: `AffinePlaneCurve.braid_monodromy()`.
Conjugating words: `conjugate_positive_form`. Discriminant points (not
paired with braids; ask.sagemath.org/question/74927): `discrim((F,))`.

**This is the top hazard class.** The conventions below are pinned to
fetched source, not inferred.

**(B1) Projection.** First generator of the parent ring, if there are no
vertical asymptotes. We force generator order `(coord_x, coord_y)` and
assert `deg_y(F) = 9 = deg(F)`.

**(B2) Base point.** A corrected Voronoi diagram of the discriminant
points in the `x`-plane; `p` is a vertex of the unbounded cell
(`geometric_basis`, `voronoi_cells`). Develop returns
`p1 = p_real + i p_imag`. Sage 10.8 docs omit it: the script FLAGs
`OPEN[BMFACT-BASEPOINT]` if the fifth slot is absent, and does **not**
pretend that y-roots at an auxiliary rational are Sage's strand order.

**(B3) Strand order.** `strand_components` sorts the `QQbar` y-roots of
`F(p1, y)` (`roots_base.sort()`: real part, then imaginary part).
Generator `xi_j` of `F_9`, 1-based, is the meridian of strand `j-1`.
The JSON emits the ordered y-roots.

**(B4) Geometric-basis orientation.** Each returned braid is the
monodromy of one based loop that travels to a bounded Voronoi cell,
runs once around it, and returns. The concatenation of the listed loops
is equivalent to the counterclockwise boundary circuit `E` of the
unbounded cell (`geometric_basis` docstring; `orient_circuit` forces
counterclockwise). The **product of the listed braids, in listed
order**, is therefore the monodromy of a large counterclockwise loop
around all finite discriminant points. This is `rho_inf` in REP-96 §2's
positive-finite-plane convention (as `x` traverses one positive loop,
`x^{k/9} |-> x^{k/9} zeta_9^k`). The enumerator also runs the inverse
product as variant `OPEN[BMFACT-ORIENTATION]`.

**(B5) Positive Artin generator.** `braid_from_piecewise` issues a
positive Tietze letter at a real-part crossing of two `y`-paths when
the currently-left strand has smaller imaginary part at the crossing
(the `sgn` on Im in that function). Sage Tietze:
`BraidGroup(9)([1,2,-1]) = s0 * s1 * s0^{-1}`; letter `k>0` is
generator `s_{k-1}` (strands `k` and `k+1`, 1-based).

**(B6) Artin action on `F_9`.** Matching REP-96 §2's left Hurwitz and
PI1-S4-DECISION §2:

```text
sigma_k :   xi_k     |->  xi_k xi_{k+1} xi_k^{-1}
            xi_{k+1} |->  xi_k
            xi_j     |->  xi_j           (j != k, k+1)
```

Composition: `(beta gamma)` acts as `beta` after `gamma`
(`phi_{beta gamma} = phi_beta o phi_gamma`). A Sage Tietze word is
applied **rightmost letter first**. This is dual to the left Hurwitz
action on tuples used by the enumerator:

```text
sigma_k . (..., t_k, t_{k+1}, ...)
  = (..., t_k t_{k+1} t_k^{-1}, t_k, ...)
```

ZvK: `xi_j = phi_beta(xi_j)` in `pi_1`, i.e. the tuple of images is
Hurwitz-fixed by `beta`. The Sage script emits, for each braid, the
nine Tietze words `phi_beta(xi_1), ..., phi_beta(xi_9)` as JSON lines.

**(B7) Affine, not projective.** `projective=False` (the default)
presents `pi_1(C^2 - D)`, not `pi_1(P^2 - Dbar)`. No relation
`xi_9 ... xi_1 = 1` is imposed.

## 4. ZvK relations from a braid word

Let `F_9 = < xi_1, ..., xi_9 >` be the free group on meridians of a
generic fibre `{x = p1} \ D`, ordered as in (B3). For each geometric-basis
braid `beta`, Zariski–van Kampen imposes

```text
xi_j  =  phi_beta(xi_j)     for j = 1, ..., 9
```

in `pi_1(C^2 - D)`. On a representation sending every meridian to a
transposition, this is exactly Hurwitz-fixedness of the 9-tuple.

**Local forms, cited from PI1-S4-DECISION §2 (re-derived there, not
consumed as an inference from an acquisition).** A simple vertical
tangency is locally `x - x_0 = y^2`; the local braid is a conjugate of
a single `sigma_i`; both generator relations collapse to

```text
(T)     xi_a  =  xi_b
```

the two meridians of the colliding sheets. An ordinary node (`A_1`,
`k=1`) with the vertical line transverse to both branches has local
braid a conjugate of `sigma_i^2`; the relations collapse to

```text
(N_1)   [ xi_a , xi_b ]  =  1
```

satisfied by disjoint transpositions. Four commuting `sigma_i^2` in one
fibre are four such pairs, on four disjoint (after transport) 2-sets of
strands.

The Sage script does **not** rewrite SIROCCO's words into `(T)` / `(N_1)`
by hand. It emits the full Artin automorphisms and the
`conjugate_positive_form` splitting, and it **validates the census**:
eight factors of tangency type (exponent 1, permutation a transposition,
CPF a single `sigma_i`) in eight distinct fibres, plus one factor of
node-fibre type (exponent 8, permutation the identity, CPF four
commuting `sigma_i^2`). Exponent ledger 16. Any other shape prints

```text
CENSUS-DISAGREES-REP96
```

and aborts. That is the load-bearing check that REP-96 §1 survived
contact with the actual braid monodromy.

## 5. Why the affine computation suffices

The projection `pr|_D : D -> C`, `(x,y) |-> x`, is proper of degree 9:
`deg_y F = 9` and `lc_y(F)` is a unit of `QQ`. A generic fibre meets `D`
in nine points; `pi_1` of the complement of those nine points in the
fibre is `F_9`. The discriminant `Delta subset C` is finite, of
cardinality 9 (square-free support of `disc_y F`). A geometric basis of
`pi_1(C \ Delta, p1)` therefore presents all finite monodromy.

The loop around a large circle in the `x`-plane is the product of that
geometric basis (B4). Its braid is `rho_inf`. In the ZvK presentation of
the **affine** complement this loop does not add a generator or a
relation beyond the product of the local relations: it *is* that
product. The extra relation `xi_9 ... xi_1 = 1` is the relation at
infinity in `P^2`, and presents `pi_1(P^2 - Dbar)`, which is the wrong
group for `phi : pi_1(C^2 - D) -> S_4`. This is Oka's Remark 3 as used
in PI1-S4-DECISION §2 (the cuspidal-cubic witness that the projective
relation kills a generator the affine group retains). Affine ZvK is
exactly the presentation the representation question lives on.

The place at infinity of `D` is visible in the affine data as the
permutation of `rho_inf`: one place iff that permutation is a 9-cycle.
The Sage script warns (does not census-abort) if the product
permutation is not a 9-cycle.

## 6. Correspondence: REP-96 `(X, Y, T_1)` and the `xi`-tuples

REP-96 §5, hard-coded in `bmfact_enum.py`, six classes:

```text
noncst-T :  X=(3 4) Y=(2 3) Pi=(2 4) ,
            T_1 = ((1 3),(1 4),(1 3))  or  ((1 4),(1 3),(1 4))
noncst-4c:  X=(1 2 3 4) Y=(1 2 4 3) Pi=(3 4) ,
            T_1 = ((1 2),(2 3),(3 4)) , ((2 3),(3 4),(1 4)) ,
                  ((3 4),(1 4),(1 2)) , ((1 4),(1 2),(2 3))
```

Each is a 24-element `S_4`-conjugacy orbit: 144 tuples. Verified here:
braid relation `XYX = YXY`, `Pi = XYX`, `prod T_1 = X`, GATE-3
`T_1 = delta_3^{k_*} . c_h(T_1)` at `k_* = -10`, image `S_4` by (3.2),
orbits of size 24, union 144, pairwise disjoint.

**`T_2, T_3` are not in the charged display.** CABLE-3 determines them
from `T_1` and `iota` once a split of `iota` among the three tubes is
chosen. The ordered product `beta = iota_2 iota_3 iota_1` is pinned to
`delta_3^{k_*}`; the distribution is not. We declare

```text
iota  =  ( delta_3^{k_*} ,  1 ,  1 ) ,
T_3   =  delta_3^{k_*} . T_1 ,
T_2   =  delta_3^{k_*} . c_{XY}(T_1) .
```

This split reproduces block products `(X, Y, X)` on every expanded
tuple. Typed `OPEN[BMFACT-IOTA-SPLIT]` for any other split with the same
ordered product.

**Tube embedding.** Adjacent blocks, as in the promoted `(6,4)` job:
strands `(1,2,3) = T_1`, `(4,5,6) = T_2`, `(7,8,9) = T_3`. REP-96 §2's
Puiseux labelling is residue-mod-3: `B_i = { j : j ≡ i mod 3 }`. These
are different embeddings of `B_3^3` in `B_9`. Typed
`OPEN[BMFACT-TUBE-EMBEDDING]`. Both readings are encoded: `BLOCK` uses
adjacent; `SAGE-NATIVE` ignores the tubular labelling and works in
Sage's strand order.

**Strand order vs tubular order.** Sage's `xi_1..xi_9` are meridians at
a finite Voronoi vertex, ordered by `QQbar.sort` of `y`. REP-96's 9-tuple
is the tubular (large-`R`) ordering. They differ by the braid taking the
finite fibre to the tube regime. Typed `OPEN[BMFACT-STRAND-VS-BLOCK]`.
The enumerator therefore runs two variants, not one silently chosen
identification.

**Orientation.** Sage's product is the counterclockwise large loop.
REP-96's `k_* = -10` is the Puiseux winding sign. If those disagree, the
inverse product is the other reading. Typed `OPEN[BMFACT-ORIENTATION]`.
Both are run when JSON is present.

**A period remark in REP-96, typed `OPEN` and not consumed.** REP-96 §3
says the GATE-3 table is 12-periodic and that `k = -7,...,-12` repeat
`k = -1,...,-6`, which would send `k_* = -10` to the `k = -4` row
(`const-4c + noncst-T`, 72 generating). The **class list actually
printed** is `noncst-T + noncst-4c`, 144 tuples, and GATE-3 holds on
those six representatives at `k_* = -10` (and also at `k = -2`, because
those particular `T_1` are extra-symmetric). The remark is therefore
false as a map of table rows, and the class list is correct at the
stated `k_*`. We hard-code the class list, verify GATE-3 at `-10`, and
do not transport the `-10 |-> -4` identification.

**Pi-tau pin, assertion not filter.** REP-96 §7 R1: grouping the `x=0`
fibre gives `Pi in V_4 * tau` with `tau` the meridian of the smooth
point `t=0`. On every `(9,6,2)` class `Pi` is a transposition, so
`tau = Pi` or `tau` disjoint from `Pi`: two of six transpositions.
Verified on all 144 conjugates (selftest). When Sage JSON is present,
the leftover strand of the node-fibre braid (the unique strand not in
the four CPF pairs) is `tau`; the enumerator **asserts** that each
survivor's `tau` is one of the two, and does not drop survivors on
failure. A failure is `PI-TAU-PIN-ASSERTION-FAIL`, a class-list / fibre
inconsistency, not a silent filter.

## 7. Deliverables and AWS protocol

**(1) `box/bmfact_962.sage`.** Modes `precheck` and `monodromy`.
Precheck is exact algebra in `QQ[x,y]`: resultant, closed-form identity,
bidegree, irreducibility, Jacobian length 4, `deg disc_y F = 16`,
square-free support 9, valuation 8 at `x=0`. Monodromy is SIROCCO,
gated by `BRAID_JOB_RUN_MONODROMY=1`. Output: `bmfact_962.json` (bundle)
and `bmfact_962.jsonl` (one JSON line per braid, plus meta / product /
census). Loud abort on census disagreement.

**(2) `box/bmfact_enum.py`.** Pure Python. Hard-coded six classes.
`--selftest` runs GATE-3, 144-expansion, Pi-tau assertion, positive
control (product only: 144 generating), negative control (projective
relation `xi_1...xi_9 = 1`: 0). With JSON: variant `BLOCK` and
`BLOCK-inverse` on the 144 reconstructed 9-tuples against every Sage
braid; optional `--sage-native` brute-forces all `6^9` maps in Sage
strand order (product-only must match 144 if the conjugacy class of
Sage's product is the CABLE-3 class). Prints per-class counts, total
survivors, and surviving `phi` verbatim.

**(3) This derivation.** Conventions cited; OPENs typed, not filled.

**(4) `box/bmfact_selfcheck.py`.** Sympy; no Sage. Transcript §8.

**AWS run.** Conda env `sage`, package `sagemath-sirocco` (same install
as the `(6,4)` braid job). Then:

```text
sage box/bmfact_962.sage precheck
BRAID_JOB_RUN_MONODROMY=1 sage box/bmfact_962.sage monodromy
python3 box/bmfact_enum.py --selftest
python3 box/bmfact_enum.py "$BRAID_JOB_OUT/bmfact_962.json"
# optional, slower:
python3 box/bmfact_enum.py "$BRAID_JOB_OUT/bmfact_962.json" --sage-native
```

Acceptance: precheck OK; census marker `CENSUS-OK` (or the loud abort);
enumerator selftest `SELFTEST-OK` with positive 144 and negative 0;
JSON path prints per-class counts and a decision line
(`KILL` / `SURVIVORS` / inverse-only) **in each named variant**, never
as an unlabelled identification of Sage strands with tubes.

A zero in **every** variant, with census OK and product a 9-cycle of
exponent `\pm 16`, is a representation-level kill of this curve. A
nonzero in any variant is an explicit `phi` on `pi_1(C^2-D)`, the
campaign's first, and is not a Keller map (`OPEN[REP-96-SOURCE-IS-C2]`
remains). `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`.

## 8. Self-check transcripts, verbatim

### 8.1 `python3 box/bmfact_selfcheck.py`

```text
=== (9,6,2) curve identity ===
p^2 - q^3 - 64 q - 64 t^2 = 0
p' = 3*(3*t**8 + 20*t**4 + 8)
gcd(p, p') = 1
gcd(p', q') = 1

=== resultant F = Res_t(p-x, q-y) ===
content(F) = 1
deg_x = 6 deg_y = 9 total_degree = 9
is_irreducible over QQ = True
F =
  x**6 - 3*x**4*y**3 - 192*x**4*y + 3*x**2*y**6 + 384*x**2*y**4 + 12288*x**2*y**2 + 32768*x**2 - y**9 - 192*y**7 - 12288*y**5 - 294912*y**3 - 2359296*y

=== identity substitution cross-check ===
G := (x^2-y^3-64y)^3 + 32768(x^2-y^3-64y) - 262144 y
content(G) = 1
F == G is True

=== leading coefficient in y (vertical asymptotes?) ===
lc_y(F) = -1
lc_y(F) is the nonzero constant -1: no vertical asymptotes.
Sage braid_monodromy therefore projects over the first variable
without a linear change of coordinates.

=== F(0,y): the unique affine fibre carrying the four nodes ===
F(0,y) = -y*(y**4 + 96*y**2 + 1536)**2
y^2-values of the four nodes: [-48 - 16*sqrt(3), -48 + 16*sqrt(3)]
  y^2 = -48 - 16*sqrt(3) = -48 - 16*sqrt(3) numerical (-75.71281292110204+0j)
  y^2 = -48 + 16*sqrt(3) = -48 + 16*sqrt(3) numerical (-20.287187078897965+0j)

=== disc_y F  (affine discriminant of the x-projection) ===
content(disc_y F) = 6387498691658813263272859953002446848
deg(disc_y F) = 16
disc_y F = 6387498691658813263272859953002446848*x**8*(19683*x**8 + 3607101440*x**4 + 140737488355328)
sqf_list = (6387498691658813263272859953002446848, [(19683*x**8 + 3607101440*x**4 + 140737488355328, 1), (x, 8)])
content factorization: {2: 108, 3: 9}
octic = 3^9 x^8 + 3607101440 x^4 + 140737488355328
  19683 = {3: 9}
  3607101440 = {2: 24, 5: 1, 43: 1}
  140737488355328 = {2: 47}

=== every root of disc_y F, including infinity ===
Finite roots:
  (N) x = 0 with multiplicity 8.
      Geometric cause: four ordinary nodes, all on the line x=0.
      Each node is two smooth branches with non-vertical tangents,
      local model y^2 ~ x^2, disc valuation 2 per node, total 8.
      Square-free support still includes x=0 (once).
  (T) the eight simple vertical-tangency values: x^4 in
         -1803550720/19683 - 159383552*sqrt(19)/19683
          numerical (-126926.15538437027+0j) is_zero False
         -1803550720/19683 + 159383552*sqrt(19)/19683
          numerical (-56333.583476575724+0j) is_zero False
      Two distinct nonzero (negative real) values of x^4, each with
      four distinct fourth roots: eight distinct nonzero x.
      Multiplicity 1 each. Square-free. Confirmed by
      Res_t(p', x-p) = 19683 * octic, degree 8.
      Res_t(p', x-p) = 19683*(19683*x**8 + 3607101440*x**4 + 140737488355328)
  No other finite roots: deg disc = 8 + 8 = 16 = 2 delta_aff + d - 1.
Infinity:
  lc_y(F) = -1 does not vanish, so x=infinity is not a root of
  the affine polynomial disc_y F.
  F_hom(X,Y,Z) |_{Z=0} = -y**9
  Dbar meets L_infty only at [1:0:0], intersection multiplicity 9.
  (Place multiplicity a = 3; this is not an affine discriminant root.)
  The ramification of t |-> p(t) at t=infinity is 8, realised as
  the product of the nine finite geometric-basis braids (rho_inf),
  not as an extra finite critical value.

verbatim table:
  root                multiplicity   geometric type
  ------------------- -------------- ------------------------------
  x = 0               8              four A1 nodes, one fibre
  eight roots of      1 each         simple vertical tangencies
  3^9 x^8 + 2^{24}*5*43 x^4 + 2^{47}
  x = infinity        (not a root)   lc_y(F)=-1; accounted in rho_inf
  total affine degree 16             = 8*1 + 4*2

SELFCHECK-OK
```

### 8.2 `python3 box/bmfact_enum.py --selftest`

The JSON dump is long; the decision lines are:

```text
expanded conjugacy orbits: 144 (expect 144)
Pi-tau pin assertion passed=True (NOT used as a filter)
POSITIVE CONTROL generating=144 expected=144 passed=True
NEGATIVE CONTROL projective-product=1 count=0 expected=0 passed=True
SELFTEST-OK
```

GATE-3 at `k_* = -10` holds on all six charged representatives; `T_1`
products equal `X`. Allowed `tau` by class: `{(1 3),(2 4)}` on both
`noncst-T` reps (where `Pi = (2 4)`), and `{(1 2),(3 4)}` on all four
`noncst-4c` reps (where `Pi = (3 4)`). Two of six, as claimed.

Independent of the reconstructed 144, a lookup-table scan of all
`6^9 = 10 077 696` adjacent-block transposition 9-tuples against
CABLE-3 `rho_inf` with `iota = (delta_3^{-10}, 1, 1)` returned
**246 product-fixed, of which 144 generate `S_4`**. The charged 144
are therefore the complete generating set in that embedding, not a
proper subset. (Default `--selftest` does not rerun this scan; it is
desk-confirmed and optional via `--brute-block`.)

## 9. SHA-256 of emitted scripts

Computed with `shasum -a 256` after the last byte was written. Terminating
newlines included.

```text
884cadc767b759a0af197a2a577511e74b4759e8e834b0100d03c15bee7d350c  box/bmfact_962.sage
b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b  box/bmfact_enum.py
e268585f4c4d945dba0ad42880763b2bee646bddd6dd19c532593c43a90e45fa  box/bmfact_selfcheck.py
```

Byte counts: 33723, 41367, 7047.

## 10. Typed OPENs, what this does not claim

Raised here, not filled:

* `OPEN[BMFACT-BASEPOINT]` — Sage 10.8 4-tuple omits `p1`; develop 5-tuple includes it. Script unpacks both.
* `OPEN[BMFACT-STRAND-VS-BLOCK]` — Sage `QQbar.sort` at `p1` versus REP-96 tubular order.
* `OPEN[BMFACT-TUBE-EMBEDDING]` — adjacent blocks versus residue-mod-3.
* `OPEN[BMFACT-IOTA-SPLIT]` — distribution of `iota` among tubes; only the ordered product is pinned.
* `OPEN[BMFACT-ORIENTATION]` — Sage product versus inverse.
* REP-96 §3's map `k=-10 |-> k=-4` of table rows is **not** used; the class list is verified at `k_*=-10` directly.

Not claimed: a representation `phi` (needs SIROCCO); a kill of `(9,6,2)`
at representation level (same); a Keller map; `Y ~ C^2`; anything about
the companion component `D_2`. Passing GATE-3 is a necessary condition
already in REP-96, not existence of `phi`. The 144 are
`REPRESENTATIVE` group-theoretic data, not `FULL_ACTUAL_EXIT`.

## 11. FALLACY-v2 audit

* **Flag/place/series.** The place at infinity is one place of
  multiplicity `a=3`, contact `d=9`, characteristic `beta_1=25`, second
  Puiseux exponent `k_*=-10`. Affine nodes are four ordinary double
  points at finite `t`, all on `x=0`. The `a=3` Puiseux conjugates are
  one place (AUD §2, honoured).
* **Floor/attainment.** `deg disc_y F = 16` is an equality with a
  complete factorisation, not a bound. The 144 is an exact count in the
  declared embedding (class-list expansion *and* a `6^9` scan).
* **Carrier/attainment.** The class list is group-theoretic residual
  data. A Sage survivor, if any, is a representation of
  `pi_1(C^2-D)`, not a Keller map.
* **Per-ray/exit-set charge.** No exit price; no `charge_basis` line.
* **Pole/interior.** No pole identity is used. The infinity contribution
  to the discriminant is read off `lc_y(F)` and `F_hom|_{Z=0}`, after
  checking the vertex is `[1:0:0]`.
* **Prime label/derivative.** `p'`, `q'`, `F_y` are derivatives.
  `Pi`, `Pi_i`, `X`, `Y` are labels.
* **Variable/ring map.** Declared in §0: `QQ`, generator order
  `(coord_x, coord_y)`, elimination in `param_t`, image check the
  identity substitution.
* **`sat()` / raw remainder.** Not in play on this machine. The Sage
  precheck's Jacobian ideal is exact bivariate algebra on AWS, ring
  asserted `QQ[coord_x,coord_y]`, positive control length 4, negative
  control would be a wrong length.
* **Not filled by cap or analogy.** Family-3 cabling, the `(6,4)`
  adjacent-pair formula, and Sage 10.8's 4-tuple are not transported
  as if they were the `(9,6)` or develop API. Where a convention is
  ambiguous, an `OPEN` is typed and both readings are encoded.

**Review routing.** The SIROCCO run is the decision. The cheapest
independent check of this codegen, before AWS, is the selftest already
run: 144 / 0. The cheapest check after AWS is the census marker, then
the product-only count in Sage strand order (must be 144 if the
conjugacy class matches, possibly 72 if the period-remark reading had
been the truth, which it is not on the class list).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `27300`.
- Body SHA-256:
  `f961eacd1c5957176c79c16688854a270ce3bc9219c48a29e704d4d8f047e5fa`.
- Frozen basis: `9268111d6f45d5e76340945992c42a71dccf4e33`.
