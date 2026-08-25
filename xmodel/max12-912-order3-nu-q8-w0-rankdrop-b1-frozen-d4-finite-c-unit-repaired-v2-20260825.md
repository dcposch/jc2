# Selected Q8 `b=1`: repaired frozen-`d4` finite-`c` landing unit

Date: 2026-08-25  
Status: **PRODUCER-EXACT ONE-ENGINE ENDPOINT; FRESH REVIEW PENDING**

This is a nonmutating scope repair of
`max12-912-order3-nu-q8-w0-rankdrop-b1-frozen-d4-finite-c-unit-20260825.md`
(SHA256 `c8e295f0fe7257c09285b2b6aaec963e93a285f862682a25d66567421ddf1bf4`).
The original bytes remain frozen.  The companion source-scope erratum is
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_saturation_aws_20260825/PARAM_SCOPE_ERRATUM.md`
(SHA256 `f037354da93c13ac077addb337bd4de864ec4cf71fd9faf97e979b773dd7dbe9`).

## Exact conclusion

From the pinned six quotient rows `(e1,e3,e5,e7,e2,e4)`, substitute

```text
d4=1,  d2=2+u,  A=x3-2*x5
```

and work in `Q[w,u,x1,x3,x5,c]`, with `c` a polynomial variable.  Compute

```text
C       = I : (w*x5*A)^infinity
GC      = std(C)
Landing = GC + (w,u,x1,x3,x5)
GL      = std(Landing).
```

The frozen Box02 `std/dp` endpoint exits rc0 and prints

```text
landing_empty=1
C_PARAMETER_BASIS_BEGIN
GL[1]=1
C_PARAMETER_BASIS_END
Q8_W0_RANKDROP_B1_PARAMETER_SATURATION_PASS
```

Thus `Landing=(1)`.  Since `c` remains a ring variable and the centre does
not set `c`, no finite geometric value of `c` occurs at this selected landing
centre in the frozen `d4=1` slice.  There is no division by a polynomial in
`c`.

This does **not** assert `GC=(1)` or global selected-open emptiness for every
finite `c`.  The marker name `C_PARAMETER_BASIS` is historical: it encloses
`GL`, not `GC` or `C`.  The older phrase “removing the finite exceptional-`c`
debt in that slice” is licensed only with “at this landing centre” appended.

## Custody and trust tier

The one-host manifest is
`PARAM_BOX02_RESULT.manifest.sha256` (SHA256
`5c3fa2d4235b4b21f4c9754e0038a94ce874ca14dfcdbf14ed99e29cfe588ac9`),
frozen by `PARAM_BOX02_RESULT.freeze.sha256` (SHA256
`a716262617be8fa35eaab82f18f0f3909b7217b8567d17b2ce0fa1f768ecbdcb`).
Input SHA256 is
`58c2fa57f7d4511b3df76f74c84759ea88534c6b9ddac0c39ef82b43aa02f946`;
stdout SHA256 is
`98950fa27f11b9a15902a4af17173d60f2b97acfcdb0d4778dc09510c38215ff`.
The endpoint records wall `1:07:11`, user `4026.60s`, maximum RSS `41820
KiB`, zero swaps, empty generator stderr, and no diagnostic pattern.

This is one AWS host, one `std/dp` algorithm/order, and no original-generator
cofactor identity.  Its in-run files do not pin a Box02 version capture.
Independent Box03 and polynomial-`c` `modStd` endpoints are pending and are
not silently counted here.

## Firewall and next gate

The frozen main preregistration's phrase “decisive ... for arbitrary
ramification at `b=1`” is superseded.  The smallest geometric successor is

```text
d4=1+v, d2=2+v+u,
C=I:(w*x5*(x3-2*x5))^infinity,
Landing=C+(v,w,u,x1,x3,x5)
```

over `Q[c,...]`.  Moving `d4`, the full rank-drop line/full `Hsrc`,
coefficient and other projective infinity, terminal/Taylor realization,
trajectories, all `(9,12)`, maximum twelve, and JC2 remain open.
