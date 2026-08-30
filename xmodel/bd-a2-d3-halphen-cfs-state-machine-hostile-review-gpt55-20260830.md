# Hostile review: D3 Halphen CFS state machine

Date: 2026-08-30  
Reviewer: GPT-5.5 hostile review pass  
Scope: only the six charged files and the CFS primary source were used; no
`jc2-lean`, q6 report, sibling prompt, sibling log, sibling report, sibling
receipt, Git state, or canonical artifact was inspected or modified.

## Custody

The six charged SHA-256 hashes match exactly:

```text
be42d2cf894d92928978935381028dbf5ae7ba1d3598a3474d7c1460a7b6dee9
  xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md
148ddb5e532b28a23361866f671984bd22a1b395a836484043f6f82c6001c1bf
  xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md.artifact.json
2570d44ec3c31b4b559299099be196dd52b13b7ba1cfe4539043f96fc823ee9c
  ops/d3_halphen_cfs_state_machine_replay.py
7e73b7a6ebd1c4f6529c8c4502e150de1a8b4e4664d03323bfc8631b03ab08c5
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md
a389b0a700a96f1ac68f3123f19fc7fa502e31b305e0973f164e50c5d6c585bd
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md.artifact.json
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
```

Primary source used for CFS assertions: J. E. Cremona, T. A. Fisher,
M. Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings of elliptic
curves*, arXiv:0908.1741, especially Lemma 3.2, Theorem 3.5,
Theorem 4.3, Definition 5.1, Lemmas 5.2--5.4, Proposition 5.6, and
Lemma 5.8.  Authoritative restatement used for the LLR Lie-lattice theorem:
Cambridge Core, *Values of zeta functions of arithmetic surfaces at s=1*,
Theorem 33 citing Liu--Lorenzini--Raynaud Theorem 3.1.

No exit-price assertion is made; receipt status `ABSENT` is expected.

## Itemized audit

1. **CONFIRM_WITH_CORRECTIONS: theorem interface.**

The exact plane level-two input is not proved by the state-machine packet.  It
is supplied by the promoted coordinator integration: the four-row table gives
the one-point triple-fibre row exact local CFS level `2`
(`xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md:29`),
and Section 5 asserts the LLR/Fisher/CFS identification making the local CFS
level exactly the Hodge/GR length
(`...coordinator-integration-sol56-20260830.md:203`).

The minimal Halphen floor-one input is CFS, not the Hodge table alone.  CFS
Theorem 3.5 says a `K^sh`-insoluble non-singular degree-three model has minimal
level at least one and exactly one when residue characteristic does not divide
three; CFS Proposition 5.6 and Lemma 5.4 give the critical-model route to that
statement.  The strict-Henselian insolubility itself is a promoted Halphen-row
input, recorded in the coordinator theorem as the locally insoluble triple
fibre (`...coordinator-integration-sol56-20260830.md:203`) and restated in the
state-machine inputs
(`xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md:67`).

CFS Theorem 4.3 applies over the complex DVR once the generic plane cubic is
non-singular and `v(F)=0`: it does not assume solubility, and completeness is
not an extra hypothesis in the theorem statement.  Lemma 5.8 does use
`K^sh`-insolubility and Hensel lifting; over `C((t))`, residue characteristic is
zero and the residue field is algebraically closed.  Correction: the safe local
theorem must explicitly include generic non-singularity and strict-Henselian
insolubility as dependencies.  They are not consequences of the coefficient
display alone.

2. **CONFIRMED: raw first-jet branches.**

The first-jet gate is used only as a first-order gate.  It formally removes
`a x^3` and `x^2L` to first order
(`xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md:63`),
but it warns that this parameter-dependent gauge creates determined higher
`t`-powers and no new parameters (`...first-jet-invariant-gate...md:70`).  The
state-machine packet correctly returns to the raw degree-three coefficient
model

```text
F=x^3+tF1+t^2F2+t^3F3,
F1=a x^3+ell x^2y+m x^2z+x(q0 y^2+q1 yz+q2 z^2)+H(y,z).
```

It keeps `a,ell,m` and raw `F2,F3` coefficients.  The provisional gate leaves
exactly `H=y^2z,q2=0` and `H=y^3`
(`...first-jet-invariant-gate...md:153`, `...first-jet-invariant-gate...md:160`).
No later argument treats the gauged `O(t^2)` terms as free or discards raw
higher coefficients.

3. **CONFIRMED: forced line cycle.**

For the raw model,

```text
L_x(F)=t^-1 F(tx,y,z),
L_y L_x(F)=t^-2 F(tx,ty,z).
```

The first reduction is `H`; for both `y^2z` and `y^3` its singular locus is the
line `y=0`.  The second reduction is exactly

```text
z^2(q2*x+C2*z),       C2=[z^3]F2.
```

If this form is nonzero, its singular locus is exactly `z=0`.  The next CFS
line move gives

```text
L_z L_y L_x(F)=t^-3 F(tx,ty,tz)=F,
```

using only spatial homogeneity of every `Fi`.

The contradiction with CFS Theorem 4.3 is legitimate.  The plane model has
level two while its minimal floor is one, so it is nonminimal.  Theorem 4.3
says the ternary-cubic minimisation procedure reaches `v(F)>=1` within at most
four iterations for a nonminimal positive-level model.  The nonzero central
form would put the algorithm in a three-cycle with `v(F)=0` forever.  There is
no alternate singular locus in these reductions, and coordinate choices moving
the unique singular line differ only by integral equivalence.  Therefore

```text
q2=0,      C2=0
```

is forced.

4. **CONFIRMED: level drop and double-root death.**

Once `q2=C2=0`, the second moved model is divisible by `t`, and

```text
M=t^-1 L_y L_x(F)=t^-3 F(tx,ty,z)
```

is integral.  Since line moves preserve level and division by the common
coefficient factor drops level by one, `M` has level one.  The promoted minimal
floor is also one, so `M` is minimal; `K^sh`-insolubility is preserved by
`K`-equivalence.  CFS Lemma 5.8 then forces the reduction of `M` to be a
nonzero scalar times a cube.

In the double-root branch,

```text
M0=x^3+m x^2z+q1 xyz+y^2z+R xz^2+U yz^2+C3 z^3.
```

Over the residue field `C`, a scalar cube with `x^3` coefficient one can be
written `(x+alpha y+beta z)^3`.  The zero `x^2y` coefficient gives
`alpha=0`; then the `y^2z` coefficient is zero, contradicting the displayed
coefficient one.  There is no missed scalar cube or residue-field loophole,
and no nonminimal level-one loophole because level one is the minimal floor.

5. **CONFIRMED: triple-root first cube.**

For `H=y^3`,

```text
M0=x^3+m x^2z+q1 xyz+R xz^2+U yz^2+C3 z^3.
```

Comparing with `(x+alpha y+beta z)^3`, the zero `x^2y` coefficient again gives
`alpha=0`.  Hence `q1=U=0`, while `m=3 beta`, `R=3 beta^2`, and `C3=beta^3`.
Writing `beta=s`,

```text
q1=0,      U=0,      R=3s^2,      C3=s^3,      m=3s.
```

Together with `q2=0`, this leaves `Q=q0 y^2`.  Under the stabilizer of
`G=y^3`, this has only the zero orbit and the nonzero `y^2` type, subject to
the normalization caveat in item 7.

6. **CONFIRMED: critical flags.**

After imposing the first cube equations and setting `X=x+s z`, the first line
move along `X=0` has transverse reduction

```text
y^3+b y^2z+c yz^2+d z^3
```

with

```text
b=Q021-s q0,
c=U3+s^2 ell-s M111,
d=-s^3 a+s^2 V-s R3.
```

It is a cube exactly when

```text
3c=b^2,      27d=b^3.
```

Putting `lambda=b/3` and shifting `Y=y+lambda z`, the intermediate coefficient
of `Y z^2` in the next central form is

```text
theta=c-2 lambda b+3 lambda^2,
```

which vanishes from `3c=b^2`.  The final central reduction is exactly

```text
z^2(kappa X+eta z)
```

where

```text
kappa = 3a s^2+2ell s lambda+q0 lambda^2
        -2V s-M111 lambda+R3,

eta = -A s^3-P s^2lambda-T s lambda^2-B lambda^3
      +V3 s^2+M3 s lambda+Q3 lambda^2.
```

Since the next model is still minimal, level one, and `K^sh`-insoluble, CFS
Lemma 5.8 forces this reduction to be a nonzero cube.  For `z^2(kappa X+eta z)`
that is precisely

```text
kappa=0,      eta!=0.
```

These conditions force `s!=0`: if `s=0`, then `d=0`, so `b=0` and
`lambda=0`; then `kappa=R3`, so `kappa=0` gives `R3=0`, and every term of
`eta` vanishes, contradicting `eta!=0`.

7. **CONFIRM_WITH_CORRECTIONS: constant normalizations.**

The normalization `m=3, ell=0` is a plane-coordinate normalization on the
`s!=0` chart.  Scaling `z` makes `m=3`, and then the constant shear
`z -> z-(ell/3)y` kills `ell` while preserving `H=y^3` and `Q=q0y^2`.

The further normalization of a nonzero `q0` to `1` is not a pure plane
stabilizer normalization if the already normalized coefficients of `t y^3` and
`t 3x^2z` are to remain fixed.  It uses local base-parameter freedom:

```text
t_old=q0^-3 t,      y_old=q0 y,      z_old=q0^3 z.
```

Therefore the literal shard `q0=1` is legitimate only in a local chart where
the base parameter may be rescaled by a nonzero constant.  If a global
coordinate or marked base datum is frozen, the honest nonzero shard is the
principal open `q0!=0`, not the equation `q0=1`.  The producer says this in
Section 4, but the theorem headline must be read with that qualification.

8. **CONFIRM_WITH_CORRECTIONS: positive control and global closure.**

For

```text
F=(x+t z)^3+t y^3+t^3x^2z,
```

the forced lowered model is

```text
M=(x+z)^3+t y^3+t^2x^2z.
```

In `X=x+z`,

```text
M=X^3+t y^3+t^2(X-z)^2z.
```

The CFS critical valuations are exactly

```text
X^3:0, y^3:1, X^2z:2, Xz^2:2, z^3:2,
all other ternary-cubic coefficients: infinity.
```

This is CFS critical in residue characteristic zero, so `M` has level one and
the original `F` has exact level two.  The generic cubic over `C((t))` is
smooth: `F_y` forces `y=0`; at `z=0`, `F_x` is nonzero; with `z=1` and
`x=t(r-1)`, the two remaining fibre derivatives are

```text
3r^2+2t^2(r-1),      3r^2+t^2(r-1)^2,
```

whose difference is `t^2(r-1)(r-3)`, and neither `r=1` nor `r=3` solves the
first expression in `C((t))`.  Local normality follows from the hypersurface
being `S2` and regular at the generic point of the central line, where
`F_t|_(t=x=0)=y^3` is nonzero generically.

For the separate global homogenization

```text
G=(S*x+T*z)^3+T*S^2*y^3+T^3*x^2z
```

in `P2 x P1`, the following cheap exact facts hold.

- `G` is bidegree `(3,3)`.
- The total hypersurface is normal: the singular locus is finite.
- The total singular points are
  `([0:0:1],[1:0])` and `([0:1:0],[0:1])`.
- At `([0:0:1],[1:0])`, with `S=z=1`, the local equation is
  `(x+t)^3+t y^3+t^3x^2`; it is isolated and not Du Val by multiplicity.
- At `([0:1:0],[0:1])`, with `T=y=1` and `u=S`, the local equation is
  `u^2+x^2z+z^3+3uxz^2+3u^2x^2z+u^3x^3`; the quadratic variable splits and
  the principal ADE type is `D4`, so this point is Du Val.
- On the affine chart `S=1`, direct Hessian-pencilling gives
  `c4=0`, `c6=216 t^12(4t^2+27)`, and
  `Delta=-27 t^24(4t^2+27)^2`.
- Homogenized:

```text
c4=0,
c6=216 S^4 T^12(4T^2+27S^2),
Delta=-27 S^8 T^24(4T^2+27S^2)^2.
```

- Removing the exact level-two factor at `T=0` gives the Jacobian discriminant
  proportional to `S^8(4T^2+27S^2)^2`: smooth Jacobian at `T=0`, two `j=0`
  finite additive fibres with discriminant order `2`, and a `j=0` fibre at
  `S=0` with orders compatible with type `IV*`.
- The plane fibre at `T=0` is the triple line `x^3`; the fibre at `S=0` is
  `z(z^2+x^2)`, three concurrent lines; the two finite singular plane fibres
  occur at `4T^2+27S^2=0` and are cuspidal.  The total surface is smooth at
  those two cuspidal fibre points because the base derivative is nonzero there.

These facts are compatible with the promoted four-row surface theorem: the
extra finite cuspidal fibres are not total-space singularities, and the
infinity singularity is Du Val, so neither is an immediate extra GR-defect
point.  This is not a proof of the binding dominant-`A2` interface and not a
polynomial map.  Cheap rationality was not certified by the local state
machine; the closure is a plausible index-three Halphen candidate, but a
resolution or explicit birational parametrization is still required for a
standalone rationality certificate.

9. **CONFIRM_WITH_CORRECTIONS: replay.**

The literal default command

```text
python3 ops/d3_halphen_cfs_state_machine_replay.py
```

fails in this environment because `python3` cannot import `sympy`.  Under an
isolated SymPy 1.14.0 interpreter,

```text
uv run --with sympy==1.14.0 python ...
uv run --with sympy==1.14.0 python -O ...
uv run --with sympy==1.14.0 python -OO ...
```

the three outputs are byte-identical, 1130 bytes, with SHA-256

```text
52c7b6445a61ae5f518b46aa93d971603b1a0d4d7c1445767c047904c2df701a.
```

The mutation

```text
uv run --with sympy==1.14.0 python ops/d3_halphen_cfs_state_machine_replay.py --mutate-cycle-scale
```

exits nonzero with

```text
FAIL:three-line CFS cycle identity failed
```

The AST guard is real: the script parses its own source and counts zero
`ast.Assert` nodes, so `-O` and `-OO` do not remove checks.  The replay derives
the coefficient identities by symbolic expansion against expected formulas; it
does not derive the CFS theorems, the Hodge theorem, strict-Henselian
insolubility, or the first-jet gate.  It also checks only a concise derivative
certificate for local normality, not a full global singular-locus calculation.
Those are acceptable boundaries, but the artifact should not be read as
self-contained executable proof of the theorem interface.

10. **CONFIRMED: correct price.**

The surviving result is a necessary local constructible gate.  It is not global
attainment, not an arc theorem, not a dominant `A2` map, not a counterexample,
and not JC2.  The positive control proves nonemptiness of the local state
machine and shows that CFS minimisation plus raw base degree three alone does
not kill the Halphen row.

The cheapest decisive global obstruction, if this local theorem is promoted,
is no longer another local CFS move.  Start with the homogenized positive
control and then with the two normalized shards.  Compute the global
resolution/GR trace and binding polarization over the declared open, verify
that the base GR divisor is exactly the promoted length-two subscheme and that
all other singularities are Du Val or total-smooth, and only then test the
dominant-rational-`A2` interface.  If the positive control already fails that
global interface, it is the cheapest obstruction; if it passes, it becomes the
sharpest negative control for eliminating the remaining constructible family.

## Maximum-safe theorem

Let `K=C((t))` or the corresponding complex DVR fraction field, and let

```text
F=x^3+tF1+t^2F2+t^3F3
```

be a raw spatially homogeneous ternary cubic with non-singular generic fibre,
central reduction `x^3`, exact CFS level two, and `K^sh`-insoluble minimal
floor of level one.  Assume the provisional first-jet gate leaves only the two
branches

```text
H=y^2z, q2=0;      or      H=y^3.
```

Then the double-root branch is empty.  In the triple-root branch the following
conditions are necessary:

```text
q2=0, C2=0,
q1=0, U=0, R=3s^2, C3=s^3, m=3s,
s!=0,
```

and, after `X=x+s z`,

```text
b=Q021-s q0,
c=U3+s^2 ell-s M111,
d=-s^3 a+s^2 V-s R3,
3c=b^2,
27d=b^3,
lambda=b/3,
kappa=0,
eta!=0,
```

with

```text
kappa = 3a s^2+2ell s lambda+q0 lambda^2
        -2V s-M111 lambda+R3,

eta = -A s^3-P s^2lambda-T s lambda^2-B lambda^3
      +V3 s^2+M3 s lambda+Q3 lambda^2.
```

On the local coordinate/base-rescaling chart, this reduces to normalized first
jet shards `m=3, ell=0, q0=0` and `m=3, ell=0, q0=1`.  With a globally frozen
base coordinate, the second shard is instead the principal open `q0!=0`.

The family

```text
F=(x+t z)^3+t y^3+t^3x^2z
```

is an exact local survivor of this necessary gate.  No global surface,
dominant affine-plane parametrization, polynomial map, counterexample, or JC2
conclusion follows from the local theorem.

## Exact dependencies

- Charged state-machine producer:
  `xmodel/bd-a2-d3-halphen-cfs-state-machine-sol56-20260830.md`.
- Charged first-jet gate, still provisional:
  `xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md`.
- Charged promoted coordinator integration:
  `xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md`.
- CFS level definition and minimisation source:
  `https://arxiv.org/pdf/0908.1741`.
- LLR Lie-lattice theorem as used by the promoted integration:
  `https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/values-of-zeta-functions-of-arithmetic-surfaces-at-s1/9BAF5F5B623566BF815941227D0D4A65`.
- Interpreter dependency for replay reproduction in this environment:
  SymPy 1.14.0 is required; default `python3` here does not provide it.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16611`.
- Body SHA-256:
  `4e5466c57ae109e6ab9a2acbc756d62791f0e359c138c18082ea93f2a29326d1`.
- Frozen basis: `0975a0d8291db09817993b8c167e55fcb39c78f2`.
