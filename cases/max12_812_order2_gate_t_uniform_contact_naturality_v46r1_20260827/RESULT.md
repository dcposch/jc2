# Gate T uniform contact naturality V46R1 root-map repair

Date: 2026-08-27

Status: **ADDITIVE PRODUCER PASS; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW OF
R1.**  The hostile-reviewed V46 source-naturality freeze remains promoted at its exact
formula/schema scope.  This directory repairs only the shifted-root coordinate block
that the V46 Grok review marked `GAP`.

## Review-directed repair

The frozen V46 review

```text
13450b727aad5a27f40ba22333b91b03765009a41de8aa36c330a5cd02347e71
  xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46-hostile-review-grok-20260827.md
```

confirmed V0, V1, V3, V4, and infrastructure sufficiency.  Its sole gap was a mixed
coordinate witness: V46 wrote D1 names in `C_jet` while retaining the raw-total `/2`,
inverted R in D1 coordinates while displaying its raw-total determinant, and pasted
rather than computed the determinant strings.

`SCHEMA_R1.json` leaves every V46 source formula, tail, support, and endpoint record
immutable and splits the root interface into two typed maps:

```text
raw total:
  A+/- = ac +/- lambda*az
  C+/- = (ec +/- lambda*ez)/2
  R+/- = rs/4 +/- lambda*cs
  determinants = (-2 lambda0, -lambda0/2, -lambda0/2)

after the total-to-D1 jet map:
  A+/- = AcD1 +/- lambda*AzD1
  C+/- = CcD1 +/- lambda*CzD1
  R+/- = BcD1 +/- lambda*BzD1
  determinants = (-2 lambda0, -2 lambda0, -2 lambda0).
```

The factors `ez,ec -> 2*CzD1,2*CcD1` and `rs -> 4*BcD1` make the two displays commute
exactly.  The source identity itself uses no root map or `rho` inversion.

## Executed result

The desk verifier returned

```text
PASS-UNIFORM-CONTACT-NATURALITY-V46R1-ROOT-REPAIR
```

in 4.247 seconds.  It rechecked the complete frozen V46 V0/V1/V3/V4 core and added:

- a complete weight/load/nonlinearity scan of all 569 tails, all denominators powers
  of two, and explicit target-scale custody;
- the actual D1 `a=7` load-tie representative `(a,c,r;T)=(7,8,7;26)`, all seven rows
  and 189 coefficients over `F_1000003`, in addition to the ordinary V46 `a=6`
  representative.  Its exact maxima are
  `p/A/C=1,R=0,k10=0,k6=1,k2=0`, with `k6` active and `k2` inactive;
- Hensel recurrence through depth 10 on both decks;
- raw-total and mapped-D1 root maps through depth 3 on both decks, 48 explicit
  raw/D1 commutation equalities and 96 triangular inversion equalities;
- all six leading Jacobians computed from matrices on both decks rather than pasted;
  and
- twelve factor-conflation mutations: wrongly retaining `/2` on mapped-D1 C, wrongly
  retaining `/4` on mapped-D1 R, or pasting the raw determinant pair into the D1 map
  all fail already at the leading block.

## Scope

R1 supplies one unambiguous shifted-root interface on `D(rho)`.  It does not change
the reviewed conclusion that serial `ACT-TOT-G22/G24+` exporters can leave the
mathematical critical path.  Per-endpoint manifests, chamber-compiler semantic checks,
generated contact-specific alias maps, and the reviewed D1 endpoints remain finite
linker obligations.  The `(8,3,8)` endpoint remains confirmed-but-unpromoted, so no
eleven-family union is promoted.

Nothing here applies at `rho=0`, to equality faces, positive-order leading loads,
`k=0`, unlisted contacts, staged Rees or terminal/Taylor receivers, either global `G2`
obligation, Gate T, order two, maximum twelve, JC2, or a counterexample.

## Immutable evidence

```text
0f6bec4983bc8d682b64db5ac23f2d1bb64b8613e2812e95f2cab2b041494b44  SCHEMA_R1.json
7c571dcd5c545bba64569fe38f826b3b33cac455540f22cecd1c35b37bc88c85  verify_uniform_naturality_r1.py
fd50f3d70b0ebdbecf1307891a9b017f264dc22e5e1fc4bc2a8839b5fdbbfe6a  run_v0_v4_r1/result.json
```
