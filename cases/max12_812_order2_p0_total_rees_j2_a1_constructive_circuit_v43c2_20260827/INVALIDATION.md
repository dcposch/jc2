# V43C1/C2 crossed-assumption invalidation

Date: 2026-08-27

Status: **EXACT NEGATIVE RESULT FOR THE PROPOSED CONSTRUCTIVE DERIVATION.**

## Result

The proposed V43C1/V43C2 certificate tree does not currently derive
`a1^104` in the frozen raw ordered-`a1`, `rho=0`, grade-through-19 ideal.
At its final split it tries to combine

```text
left:  a1^46 modulo (e0,e1),
right: a1^57 modulo (e0,G),       G=e1-4*a1*ell1,
split: e1*G=(32/3)*Tg12_2 modulo e0.
```

The right certificate in fact still contains a nonzero multiplier of the old
assumption `e1`.  The strict `CombineBranches` guard is correct to reject it.

Write `Z` for the `e1` multiplier immediately after the earlier `a1^18`
checkpoint.  The frozen v4 AWS run expanded `Z` exactly and found 24,429
nonzero terms:

```text
Z root                         170
expanded term count            24429
expanded polynomial SHA-256    3c4dcc5f62f3c501f08581369525ca088b15a4ec3d3fa6f56251da288e229a72
peak sparse terms              24429
unique visited DAG nodes       61
evaluated node calls           92
```

After the exponent-three `ell1` clearing, the inherited `e1` multiplier is

```text
a1^2 * Z * K,
K = a1^36 + a1^18*m*ell1 + (m*ell1)^2,
```

where `m` is the `ell1` multiplier in the `a1^18` certificate.  The subsequent
linear `Q0` clearing multiplies it by one more `a1`, giving arithmetic-DAG root
642.  The factor `K` is nonzero without expansion because
`K|_(ell1=0)=a1^36`.  Since `Q[X19_rho0]` is a domain, `a1^3*Z*K` is nonzero.
It cannot be silently deleted or passed through the branch-combination rule.

## Consequence and firewall

- The V43C1 expanded job had not reached a verdict; this report identifies the
  exact guard at which that unchanged program must fail if allowed to finish.
- V43C2 v1 was a packaging failure, v2 exposed the crossed label, v3 reached
  its registered 14-GiB resource gate without a verdict, and v4 supplied the
  exact 24,429-term countercertificate to the proposed early cancellation.
- The proposed explicit special-fibre exponent `M=104` is therefore
  unavailable from this derivation.  Consequently the conditional V43G4
  converter exponent `4+6*M=628` is also unavailable from this derivation.
- This does **not** invalidate the reviewed V42 set-theoretic/radical cascade,
  the exact V43G4 identity `5*t^6*a1^4 in J`, or the possibility of a corrected
  explicit special-fibre certificate.

## Clean successor

The defect is a missing change of assumption basis on the second branch, not
evidence that the branch theorem is false.  Before clearing `ell1^3`, use

```text
e1  = G  + 4*a1*ell1,
ee0 = Q0 - 4*aa0*ell1,
Q0  = ee0+4*aa0*ell1.
```

Thus

```text
c_e1*e1 + c_ee0*ee0 + c_ell*ell1
= c_e1*G + c_ee0*Q0
  + (c_ell + 4*a1*c_e1 - 4*aa0*c_ee0)*ell1.
```

A successor must serialize and replay this exact `RebaseAssumptions` rule,
remove both old labels before any `ClearPower`, reject mutations of each
signed `4`, and retain every existing clear/branch guard.

## Frozen evidence

- V3 source manifest SHA-256:
  `f82c4c12f98eecd14b7fb5a167bf42feb47b2873bf9435b14b1147afd68926de`
- V3 stop record SHA-256:
  `1580c6c8c0a97e20d1c31e50948b5c1af216e5d824d7f75160b06bf37ea9433d`
- V3 failure-evidence manifest SHA-256:
  `37946eefba5b3c42dec8fed4956fcc9d8adee0d056ee8b18251ca1d415fc6b41`
- V4 source manifest SHA-256:
  `71b7fcc0efaffacf913d2b71427ef19edd23b38a6a23dc91eb2b4cc10fc8dd73`
- V4 producer SHA-256:
  `1a21fd304579b5da1dd8df020bb066a74dbc8d4c8f6f3ac32932bacc105c8e75`
- V4 stderr SHA-256:
  `8b7a83b33b95a36213c1e247a55dad7a9651c0d8ad4ad1fc08546b038b99d2d1`
- V4 failure-evidence manifest SHA-256:
  `bef7f72a556a470b95dff05796937f8410347045f44b787f5050e09fc93d4ac8`

