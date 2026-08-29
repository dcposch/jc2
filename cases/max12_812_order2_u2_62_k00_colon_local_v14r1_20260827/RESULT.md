# K00 colon-local V14R1: exact local membership with complete witness custody

Date: 2026-08-27

Status: **EXACT PRODUCER PASS; AWAITING DIFFERENT-MODEL HOSTILE REVIEW.**

## Exact statement

Put `R=Q[d0,d1,d2,d3,d4,d5]`, `m=(d0,d1,d2,d3,d4,d5)`, and let
`r1,...,r7` be the exact unloaded frozen tails after the K00 transverse
coordinate change and the normalized slice `C6=1`.  If
`I=(r1,...,r6)`, then

```text
r7 is in I R_m.
```

This is compatible with the separately reviewed V8 theorem that `r7` is
not in `I` in the global polynomial ring: V14R1 exhibits a denominator
which is a unit at `m`.

## Exact witness

The exact-Q colon computation gives

```text
h = 63*d4 + 20,                  h(0)=20 != 0,
h*r7 = u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6,
```

where

```text
u1 = 273/128*d4*d5^2-175/8*d3^2-189/1024*d2*d4+19/64*d4^2
     +147/4*d1*d5+1627/64*d3*d5-689/64*d5^2+23/1024*d0
     -869/2048*d2+423/2048*d4-25/256
u2 = 91/8*d5^3-315/32*d3*d4+7/64*d2*d5+147/16*d4*d5
     +21*d1-21/4*d3+21/16*d5
u3 = -105/128*d4^2-357/8*d3*d5+705/16*d5^2-21/128*d0
     -123/128*d2+27/32*d4-15/32
u4 = -21/4*d4*d5+84*d1-43*d3+65/4*d5
u5 = 35*d5^2+49/16*d2-3/16*d4-5/2
u6 = -147*d3+339/2*d5.
```

The producer replayed this identity exactly.  It then serialized `h` and
the six `u_i`, constructed a new Singular input only from those saved
polynomial bytes and the frozen row prelude, and replayed the identity in a
second process.  The fresh-process residual artifact is the literal
polynomial `0` and its independent unit check passes.

## Complete custody and controls

- The exact-Q run serialized all 36 entries of the `6 x 6` lift matrix as
  separate files.  The six saved `u_i` byte-match column 1 of that matrix.
- The producer independently recomputed the 6-generator colon, the full
  87-generator syzygy module, equality of its seventh-coordinate projection
  with `(I:r7)`, every syzygy identity, and every colon-lift identity.
- The exact-Q endpoint is
  `aws_q_box01_pass/run/RESULT.json`, SHA256
  `28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2`.
- Exact-Q main algebra used 36.94 seconds wall time, 72,256 KiB maximum RSS,
  and zero swap on registered Box01.
- The independently compiled `p=65521` control reached the same local-
  membership and fresh-replay endpoint.  It is navigation only, not a
  characteristic-zero proof.

V14 itself remains custody-failed and non-promotable because its matrix
writer preserved only one row.  V14R1 regenerated the frozen calculation;
it did not infer the missing entries from V14's output.

## Scope firewall

This theorem concerns only the **unloaded**, normalized `C6=1` coefficient
slice and membership in the local ring at the K00 coefficient point.  It
does not establish mixed load/target or Lambda-order reachability, the
closure-first incidence decision, Taylor realization, order two, maximum
twelve, or JC2.  In particular, it removes the pure-coefficient local
obstruction and supplies a unit-denominator deformation relation for the
next mixed `Lambda<=19` syzygy-cokernel calculation.
