# Binding integration: D3 Halphen global positive control

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `c005516819d1cb327659f550d694807c66c347f8`  
Disposition: **PROMOTE CONTROL WITH REVIEW REPAIRS / NON-LOAD-BEARING**

## 0. Binding verdict

Promote the exact global facts about

```text
X={(Sx+Tz)^3+T*S^2*y^3+T^3*x^2*z=0}
  subset P2_[x:y:z] x P1_[S:T].                         (0.1)
```

The surface is integral and normal of class `(3,3)`, and projection
`pi:X->P2` is finite flat of degree three.  Its singular locus consists of the
marked D3 critical-control point and one `D4` rational double point.  The
marked germ has exact shifted weight face

```text
X1^3+t*y^3+t^5
```

for weights `(5,4,3)`, so it realizes the promoted local control and the
`(alpha,eta)=(0,1)` specialization of the still-separately-reviewed universal
weighted normal form.

The dense ramification component has normalization

```text
y^3=-3*q^2*(2*q^2+3)^4/(4*(q^2+1)),                    (0.2)
```

a connected cyclic cubic totally ramified at six places and therefore of
genus four.  Consequently this specific global surface cannot be the middle
surface of an actual proper block **if** an affine target restriction of
`pi` is globally identified with that block's second leg: the actual etale
first-leg image misses ramification, so the genus-four component becomes
boundary, contradicting the morphic rational-forest theorem.

Opus 5 returns `CONFIRM_WITH_CORRECTIONS`.  The corrections strengthen the
proof and narrow the antecedent; none changes the global surface theorem or
genus computation.  This control does not prove that every local survivor
globalizes, eliminate the entire row, construct a first leg, or decide JC2.

## 1. Custody

```text
a9f4c9e9c2f0f35dd93b894b034cf6ced6896ce2e18221305626d09d6f67c96f
  xmodel/bd-a2-d3-halphen-global-positive-control-sol56-20260830.md
e5920c24850f3af6aaaf54c8a724e1981beb34ac53a05655178e45e2539948bd
  xmodel/bd-a2-d3-halphen-global-positive-control-sol56-20260830.md.artifact.json
be9551b7a19d0cf72e8c1f189771b92c78496cf111b578925b65c56957b65485
  ops/d3_halphen_global_control_replay.py

f1a4bbd63362527ecd3c9f9ea0af3ea01a6e0cc0ef67f0839a3c1b3758ee66e3
  xmodel/bd-a2-d3-halphen-global-positive-control-hostile-review-opus5-20260830.md
  raw reviewed body c8d62de1a530d46e90415d9695814f8c4a00a23ba9c99a0152e54924219f8fa2
829483d10daf1de591e24021417e14f0f57f70bb3e2f94fae3d119ecf3d87cf7
  xmodel/bd-a2-d3-halphen-global-positive-control-hostile-review-opus5-20260830.run.v2
```

Root waited for lane exit, read the schema-v2 receipt first, reproduced all
charged and reconstructed custody hashes, stamped the raw report body against
basis `44ac698b0c2061b986e46895cb64ea5c5b441e0c`, and committed and pushed the
receipt atom before reading the review.  `charge_basis_status=ABSENT` is
expected because no exit price was asserted.

## 2. Finite flat normal surface

Expanding (0.1) in `[S:T]` gives binary-cubic coefficients

```text
S^3:  x^3,
S^2T: 3*x^2*z+y^3,
ST^2: 3*x*z^2,
T^3:  z^3+x^2*z.
```

Their ideal has radical `(x,y,z)`, so there is no common projective zero and
`pi` is finite.  The hypersurface is a pure two-dimensional Cohen--Macaulay
effective Cartier divisor in the smooth threefold.  Finite fibres and the
regular two-dimensional target give flatness; the generic binary cubic has
degree three, hence `pi_*O_X` is locally free of rank three.

Exact projective-chart elimination gives only

```text
([0:0:1], T=0),             ([0:1:0], S=0)              (2.1)
```

in the total singular locus.  At the second point the weighted principal part
is `u^2+z^3+x^2*z`; its Milnor algebra has dimension four, and every remaining
term has strictly higher weight, proving analytic type `D4`.  The ample
divisor is connected; a reducible or nonreduced connected hypersurface would
have a positive-dimensional singular intersection, contrary to (2.1).
Alternatively, direct factorization and the irreducible smooth generic cubic
give integrality.  The hypersurface is `S2`, and (2.1) gives `R1`, so it is
normal.

## 3. Local face and fibre invariants

On `z=1`, put `X1=x+t`.  The equation is exactly

```text
X1^3+t*y^3+t^3*X1^2-2*t^4*X1+t^5.
```

The weight census for `(5,4,3)` is `{15,17,19}`; the complete weight-15 face
is `X1^3+t*y^3+t^5`.  It is correct to call this the promoted control family.
The labels `(alpha,eta)=(0,1)` belong to the provisional universal weighted
normal form and are imported only through this exact face identity.

Every generic fibre is a cyclic cubic cover of `P1`, so `c4=0`.  In the two
base charts,

```text
c6=216*t^12*(4*t^2+27),
Delta=-27*t^24*(4*t^2+27)^2,

c6_inf=216*u^4*(27*u^2+4),
Delta_inf=-27*u^8*(27*u^2+4)^2.
```

The minimal valuation ledger is `(0,0)` at `t=0`, `(1,2)` at each of the two
finite roots, and `(4,8)` at infinity, summing to minimal discriminant degree
12.  This describes the Jacobian rational elliptic surface with types
`II+II+IV*`; it does not identify the relative minimal model of `X` itself.
Indeed `X` has the nonreduced fibre `3*{x=0}` at `t=0` and no section.

## 4. Ramification component

In the target chart `z=1`, eliminating `F=F_t=0` gives the irreducible plane
curve

```text
B=(x+t)^2*(x-2*t)-2*t^3*x^2=0.
```

Its parametrization

```text
r=2*q^2+3,        x=r*q,        t=r*q/(r-1)
```

is birational, with rational inverse `q=x*t/(x+t)` on a dense open.  Lifting
through `F_t=0` gives (0.2), and substitution also satisfies `F=0`.

The Kummer divisor has valuations

```text
q=0: 2;       2*q^2+3=0: 4 at two places;
q^2+1=0: -1 at two places;       q=infinity: -8.
```

No valuation is divisible by three, so the cover is connected and all six
places are totally ramified.  Riemann--Hurwitz gives

```text
2*g-2=3*(-2)+6*(3-1)=6,             g=4.
```

The target branch divisor is the line `z=0` plus one irreducible degree-eleven
curve.  The ramification divisor has a rational component over the line and
the genuine genus-four component above; (0.2) is not a parametrized proper
sublocus or a multiple cover.

## 5. Proper-block scope

Assume globally that for some affine target chart,

```text
Y=pi^-1(A2),                    g2=pi|Y
```

inside an actual proper factorization.  The block theorem gives
`V=g1(A2) subset Y_sm minus Ram(g2)`.  Resolve the projective surface by a
birational morphism that is an isomorphism over `V`, then make the complement
SNC.  The strict transform of the genus-four ramification closure remains a
curve; its smooth boundary component is its normalization and cannot be
contracted by this morphism.  It is disjoint from `V` and survives every
affine target chart because its target image is not a line.  Thus the boundary
has `tau>=4`, contradicting the corrected morphic forest theorem.

This antecedent is strictly stronger than the local function-field/germ
identification used by the universal weighted obstruction.  Genus four is not
a local germ invariant, so this argument is control-specific.  No conclusion
is licensed from an abstract rational domination of an open surface.

## 6. Replay and disposition

Under SymPy 1.14.0, ordinary, `-O`, and `-OO` replay outputs are byte-identical,
1,148 bytes, SHA-256

```text
ee77940abb31d00eb90880a75f5cbec708e0b7f445757fa96ddde62963650c20.
```

There are zero AST `Assert` nodes, and the denominator mutation exits nonzero.
The script derives the displayed equations, local singular candidates,
binary discriminants, Kummer function and finite-support disjointness.  The
birationality, valuation at infinity, branch ledger, genus, minimal checksum,
normality and proper-block boundary contradiction are report-layer
mathematics, not executable outputs.

Promote this packet as a reviewed global/local positive control and a specific
conditional proper-block negative control.  Do not use it as a second proof of
the family-wide row obstruction.  The row-level proof remains the independent
weighted-boundary theorem and its own review gate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8036`.
- Body SHA-256:
  `7aafee2714cdf0fe95a5f2cbc5d72dd322c37031c34427573b041b609e786c0d`.
- Frozen basis: `c005516819d1cb327659f550d694807c66c347f8`.
