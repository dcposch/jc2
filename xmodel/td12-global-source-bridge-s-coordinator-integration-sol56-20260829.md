# Coordinator integration — TD12 sibling/S17 source bridge

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`  
Lifecycle: `PROMOTED_MAP_AND_FLOOR_BRIDGE / VALUE_LEVEL_OPEN`

## 0. Evidence, custody, and disposition

Quarantined Opus 5 producer:

```text
3595fb88ef01fe72dce13cbb00b817a75a040f744764a8e34f865450c01b77d1
  xmodel/td12-global-source-bridge-s-opus5-92e-20260829.md
  true pre-seal body 42545 / c4825be2dc3603031c2aad4caa6eb1cea40e57ae6c01a9d8ce19d1101f3cc2e0
```

Sol internal audit:

```text
1a6472f8ff8530cc77deee622160e3095fcf12e9c958ba5ac3d27a70fd339ac9
  xmodel/td12-global-source-bridge-s-opus5-internal-audit-sol56-20260829.md
  body d0c1c700e60b88e64a3e317d1a0b9d09fcf2943988a5151ca7c5bc14534cf631
```

Independent Fable 5 reconstruction:

```text
40438835f4e24cdb87b2911e3676a8696399f1b9507550cd97f87d75605d7976
  xmodel/td12-global-source-bridge-s-opus5-different-model-review-fable5-40c-20260829.md
  body 39244 / e6f86217a33ab8bf5045bf9ced953f8eefb8bf0abd4fd9aa658f349b460fc7c0
```

The different-model review reconstructed the mathematics from the literal
sources and returned `PASS_WITH_MATERIAL_REPAIRS`. Its lane is `DONE`, exit
zero, with stable declared inputs and `charge_basis_status=ABSENT`.

The producer remains quarantined for two custody defects. Its seal tool
matched the seal text's self-mention instead of the actual heading, and its
charged `ladder/REDUCTION.md` hash was copied from basis `76c746f6` rather
than recomputed at its stated basis. The correct current content hash is
`29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b`.
The consumed mathematical passages are unchanged, so neither defect changes
the theorem. This freshly sealed integration is binding.

Disposition:

```text
PROMOTE THE REPAIRED SHEAR/FLOOR/SIBLING/DEGREE MAP-LEVEL THEOREM
CLOSE FLOOR-COORD OPERATIONALLY BY AN EXPLICIT SOURCE-TRANSLATION GAUGE
REQUIRE GAUGE SERIALIZATION FOR FUTURE VALUE PACKETS
KEEP OCCURRENCE, VALUES, PAIRREF, CAP, AND TERMINAL DEVIATION OPEN
```

## 1. Repaired shear and floor bridge

For a chart polynomial `h^F`, put

```text
Q_c(xi,eta)=xi^n h^F(xi,c+xi*eta)
           =sum_(k>=0) xi^k P_k(c+xi*eta).
```

If `l=mult(P_0,c)`, then

```text
ord_c(P_k)>=l-k for all k
  iff [xi^s]Q_c=0 for s<l,
ord_xi(Q_c)=l,
p_(h,F*c)(eta)=[xi^l]Q_c
  =sum_(k=0)^l [(z-c)^(l-k)]P_k(z) * eta^(l-k).
```

This is the typed repair of the producer's Laurent-divisibility wording.
The shear `(xi,eta)->(xi,c+xi*eta)` has determinant `xi`, so the Keller
identity transports with the exact factor and the height changes by
`u->u+1/kappa`. Cell occurrence remains a hypothesis.

For any real `u>=0`, define

```text
sigma_h(u)=min{J-u*m:(J,m) in supp(h)},
Gamma(u)=(1-u)-sigma_f(u)-sigma_g(u).
```

The least chart exponent is exactly `sigma_h(u)` and its floor polynomial is
the minimal Newton face `h_u^down(1,eta)`, independent of branch, fibre value,
and prefix. For every normalized counterexample,

```text
sigma_f(u)+sigma_g(u) <= 1-u,
J(f_u^down,g_u^down)=1  if Gamma(u)=0,
J(f_u^down,g_u^down)=0  if Gamma(u)>0.
```

On the cell lattice the floor row is `kappa_F*Gamma(u)` rows below the
inhomogeneous landing row. If `Gamma=0`, the compatibility is a face-only
identity and cannot be absorbed by other graded pieces.

At `u>0`, equality is rigid:

```text
(f_u^down,g_u^down)=(c1*x,c2*y), c1*c2=1,
or (c1*y,c2*x), c1*c2=-1.
```

Otherwise, when both floor orders are nonzero, the two floor divisors are
proportional after clearing by the integral `kappa_F` weights. Fractional
polynomial powers are not asserted.

## 2. Sibling cell and explicit translation gauge

For `tau_c(x,y)=(x+c,y)`, source composition

```text
(f_c,g_c)=(f,g) o tau_c
```

preserves the Jacobian, counterexample status, degrees, normalized type, the
right-edge coefficient columns, and lexicographic minimality. Outside the
finite set

```text
E=Z(f_(l_f)) union Z(g_(l_g)),       |E|<=k_f+k_g,
```

it also gives

```text
ord_x(f_c)=ord_x(g_c)=0,
sigma_(f_c)(u)<0 and sigma_(g_c)(u)<0 for every u>0.
```

Branches transport by `y_c(x)=y(x+c)`. All Puiseux data below height one,
contact orders, and every recorded S17 cell datum transport identically. In
particular the prefix, height, `kappa_F`, `nu_F=17`, `kbar_F=13`, reduced
`p`, its three roots, `D_F=17i`, and the tops `P_0=lambda_f p^i`,
`G_0=c_g p^r` are unchanged. The graded pieces `P_k,G_k` are invariant for
`0<=k<=13`; pieces at `k>=14` transform by an explicit triangular correction
depending on `c` and the prefix.

Thus the literal fixed-representative question remains open, but
`FLOOR-COORD` is closed as an operational fork: every S17 argument may choose
this explicit equivalent normalized representative. In that gauge
`Gamma(u)>0` for all `u>=0`, so the floor is never the inhomogeneous Keller
row. This does not supply the unavailable intermediate rows.

Every future S17 `PairRef`, completion, or value packet must serialize the
gauge constant `c`, certify `c notin E`, and either stay within the invariant
range `k<=13` or serialize the triangular corrections. Two lanes using one
route state must share the same gauge.

## 3. Sibling equality and degree floors

The two `nu=17` children and their A sibling have identical floor data at
every common height on the common lattice: `sigma`, floor polynomial,
`Gamma`, and, where defined, the floor-divisor ratio agree. This couples only
the floor end. It supplies neither independence nor conjugacy of the
positive-order evaluations; those are evaluations of the same parent family.

At an actual S17 occurrence with full index `i`, the chart degree gives

```text
deg_y(f)>=68i,
deg_x(f)>=68i,
deg(f)>=136i.
```

Under normalized type `(2,3)`,

```text
deg_y(g),deg_x(g)>=102i,
deg(g)=(3/2)deg(f)>=204i.
```

These are lower floors, never degree ceilings or occurrence statements.

## 4. Binding repairs, blockers, and next interface

The producer's mathematical prose is repaired as follows: normalize the
shear with `Q_c`; use integer-cleared divisor powers; restrict the large-u
claim to normalized-counterexample scope; correct the swapped-orientation
Jacobian sign; prove `x|f` by the full support inequality; state that only
the g-side degree bounds use type `(2,3)`; and retain common-height/lattice
and tree-occurrence riders.

The following remain open:

- no theorem forces an S17 occurrence or selects td12/U1 from a minimal
  counterexample;
- `kappa_F` and the height remain unpinned;
- no positive-order sibling value, serialized `PairRef`, source cap, or
  completion instance exists;
- the reviewed map-level theorem does not construct the terminal reduced
  deviation with `O=13-D`.

Consequently the general first-resonance derivative lemma yields S `j=13`
only conditionally after that last recurrence is typed. Do not launch a
separate residue calculation. The narrow source deliverable remains a
route-separated S parent PairPack with the gauge fields above; at the global
route level the missing arrow remains actual td12/U1 landing/occurrence.

No route kill, ceiling, exit price, counterexample, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7175`.
- Body SHA-256:
  `dcc03cbcacae146eefa57c4c3f82c7406134577aae46484b7de4a28b0d707cd7`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
