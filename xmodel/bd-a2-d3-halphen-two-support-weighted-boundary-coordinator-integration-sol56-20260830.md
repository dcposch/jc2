# Binding integration: D3 two-support Halphen weighted-boundary obstruction

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`  
Disposition: **PROMOTE WITH REVIEW SCOPE REPAIRS**

## 0. Binding verdict

Promote the elimination of the actual-morphic degree-three row

```text
m=3,                 T=t0+t1,       t1!=t0,
local CFS levels=(1,1),             F_(t0)=3L.
```

At the triple-fibre point, the exact level-one, strictly-Henselian-insoluble
model is already at its minimal floor.  Normality and the CFS line moves force
the exact critical cycle

```text
x^3 -> y^3 -> C2*z^3 -> x^3,        C2!=0.
```

The complete lowest face for weights `(x,y,t)=(2,1,3)` is

```text
P=x^3+t*(y^3+q1*x*y)+C2*t^2.                         (0.1)
```

Its curve in `P(2,1,3)` has boundary invariant one for every `q1` and every
`C2!=0`: it is a smooth genus-one curve when `q1^3+27*C2!=0`, and an
irreducible nodal rational curve whose resolution graph has a cycle when
`q1^3+27*C2=0`.  In an actual proper-block occurrence the marked center is a
singular point missed by the everywhere-defined etale first leg.  The
exceptional configuration is therefore boundary for `V=g1(A2)`, contradicting
the binding morphic rational-forest theorem.

The hostile review returns `CONFIRM_WITH_CORRECTIONS`.  Its corrections make
the imported local and occurrence hypotheses explicit; they do not change the
row verdict.  This is not an abstract local-surface theorem, a global
attainment theorem, a polynomial map, or a result about JC2 without the
charged proper-block reduction.

## 1. Frozen evidence and custody

```text
9b232811376194277d4916bc7e42216740c9b9a80430800b1fb6ffba0cf91218
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-obstruction-sol56-20260830.md
c5936d24d784f1a6088d42992f41fcdb05c7b14e158abc56c82d8027154ad6b4
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-obstruction-sol56-20260830.md.artifact.json
204acc292db6d2c1874dd741a637b6a21e5c16c5c49c60389062b3874f7525cc
  ops/d3_halphen_two_support_weighted_boundary_replay.py

3d761eb5110049069d8a5b5eebbc1f180a2a2fb08ea4090b05223d7b9afe2e0c
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-hostile-review-gpt55-20260830.md
  raw reviewed body ee5660318bda0d013bfd4258d8157f1eb05936a22a095f26bd28e9ff345fe566
abbbcb281eaf292d3bd70b26c0e3b24e4172feaa985d4cc3aa9e894f76db09e3
  xmodel/bd-a2-d3-halphen-two-support-weighted-boundary-hostile-review-gpt55-20260830.run.v2
```

Root waited for lane exit, read the schema-v2 receipt before the report,
reproduced the prompt, adapter, launcher, reconstructed Seatbelt profile,
validator, appendix, composed model prompt, report and log hashes, stamped the
raw report body against basis
`5775cfc63803dbb99b6d4574f8e91e201790f3c0`, and committed and pushed the
custody atom before reading the report.  Receipt `charge_basis_status=ABSENT`
is expected because the reviewer asserted no exit price.

## 2. Exact CFS interface

Write the charged raw local model

```text
F=x^3+t*F1+t^2*F2+t^3*F3,
F1=a*x^3+ell*x^2*y+m*x^2*z
   +x*(q0*y^2+q1*y*z+q2*z^2)+H(y,z).                   (2.1)
```

The imported Hodge theorem supplies exact plane level one at `t0`; the
triple-fibre torsor is strictly-Henselian insoluble, so CFS Theorem 3.5 makes
one the minimal floor.  Generic nonsingularity, `v(F)=0`, integrality and
normality remain hypotheses throughout the moves.

If `H=0`, then `F_t` vanishes generically along the central singular line and
the total hypersurface has a codimension-one singular locus, contradicting
normality.  Thus `H!=0`.  The first line move

```text
E1=t^-1*F(t*x,y,z)
```

is an integral minimal level-one model.  CFS Lemma 5.8 forces its nonzero
reduction to be a cube, normalized over `C` to `H=y^3`.  The second line move
has reduction

```text
(E2)_0=z^2*(q2*x+C2*z),              C2=[z^3]F2.       (2.2)
```

The case `q2=C2=0` is not a survivor: then every coefficient of `E2` is
divisible by `t`, and scalar division lowers level one to level zero,
contradicting the insoluble floor.  Since the nonzero form (2.2) must itself be
a cube, precisely

```text
q2=0,                                C2!=0.             (2.3)
```

The next line move gives

```text
t^-1*E2(x,y,t*z)=t^-3*F(t*x,t*y,t*z)=F,
```

where the last equality is exact spatial homogeneity.  This is the charged
three-cycle; it is not a generic statement about arbitrary ternary cubics.

## 3. Complete weighted face and boundary invariant

At `p=([0:0:1],t=0)`, use `z=1` and weights `(2,1,3)`.  The only prospective
term below weight six is `t*q2*x`, killed by (2.3).  At weight six the complete
list is `x^3`, `t*y^3`, `t*q1*x*y`, and `C2*t^2`; every other raw term has
weight at least seven.  This proves (0.1) without a hidden equal-weight term.

The curve `C={P=0}` avoids both quotient coordinate points of `P(2,1,3)`.
On the ordinary chart `y=1`, set

```text
W=2*C2*t+(1+q1*x).
```

Then

```text
W^2=(1+q1*x)^2-4*C2*x^3,
Disc_x=-16*C2*(q1^3+27*C2).                            (3.1)
```

Off the equality locus, (3.1) has four branch places after including infinity,
so `C` is smooth of genus one.  On the equality locus, `q1!=0` and

```text
27*h(x)=(q1*x+3)^2*(4*q1*x+3),
h''(-3/q1)=-2*q1^2/3!=0.
```

Thus `C` is irreducible rational with one ordinary node.  In the ordinary
`y`-chart, the strict-transform germ at that node is `uv+phi(r)=0`.
Normality excludes `phi=0`; after a unit, `phi=r^n`, `n>=1`.  Resolving joins
the two branches of the same global component through either two parallel
edges (`n=1`) or an `A_(n-1)` chain (`n>=2`).  The dual multigraph therefore
retains a cycle.  Hence `tau=1` in both coefficient strata.

## 4. Actual-block transfer and exact scope

At the marked target point,

```text
F(t;0,0,1)=t^2*(C2+C3*t),              C2!=0.           (4.1)
```

Weierstrass preparation makes the completed incidence finite after shrinking
the target neighborhood.  In an actual occurrence it has the same function
field as the intermediate block; uniqueness of integral closure identifies
the normal local germs.  Equation (4.1) does not assert global finiteness of
the projective incidence.

The charged block theorem gives an everywhere-defined quasi-finite etale open
map

```text
g1:A2 -> V=g1(A2) subset Y_sm minus Ram(g2).
```

The singular center `p` is outside `V`, so every divisor above it is boundary
in a smooth SNC completion of `V`.  Apply the corrected rational-forest
theorem to the morphism `g1:A2->V` itself.  It forbids both positive-genus
boundary components and cycles in the boundary dual multigraph, including
parallel edges.  Section 3 contradicts it.

The conclusion is licensed only when all of the following remain visible:

```text
smooth generic cubic;
normal local total incidence;
exact plane CFS level one;
strict-Henselian-insoluble minimal floor one;
actual local incidence/function-field identification with the proper block;
the everywhere-defined morphic first leg and its open image V.
```

A finite formal jet or an abstract normal surface does not supply these
hypotheses.  Rational domination in place of the morphism does not suffice.

## 5. Replay and controls

The replay is optimization-stable under SymPy 1.14.0.  Ordinary, `-O`, and
`-OO` runs give the same 547-byte output with SHA-256

```text
d3a35f87dc841f0cdc4a6d613281999982ccea3d7813f2f4a6f07605eba07700.
```

It has zero AST `Assert` nodes.  The mutation
`--mutate-discriminant-sign` exits nonzero.  The executable layer checks the
line-move expansions, exact cycle, complete weighted face, square completion,
discriminant, nodal factorization, quotient-point avoidance and diagonal
control.  It does not prove the CFS theorems, strict-Henselian insolubility,
normality of the strict transform, Morse reduction, graph topology, integral
closure transfer, block theorem or forest theorem.

The local control

```text
x^3+t*y^3+t^2*z^3
```

is normal, generically smooth and critical, and lies in the smooth genus-one
face stratum.  It prevents the false claim that CFS minimization and raw base
degree three alone kill the row.  It does not contain the distinct second
support, globalize the four-row surface, or define a proper block.

## 6. Promotion and successor

Promote the maximum-safe theorem in Section 0 and mark the
`m=3,T=t0+t1` row **eliminated inside the actual normal morphic proper-block
scope**.  Stop local coefficient and weighted-boundary work on this row.

The one-point Halphen row `m=3,T=2t0` has an analogous provisional universal
obstruction but its Fable review failed operationally with no report; it is
not promoted by this integration.  Research capacity moves to the two
sectioned rows.  Reviews of shared interfaces may run in the background and
do not block provisional successors.

No global surface occurrence, Keller map, counterexample or JC2 conclusion is
asserted here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8946`.
- Body SHA-256:
  `15a668ebc5760615add4263daf61901d867115a0ab6fce9bc4ab5e26b178345a`.
- Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`.
