# D125 cross-review: the two coefficients called e

2026-09-07. **REFUTED implication, not a source exclusion.** Fable cross §3 conflates two distinct coefficients. Its numerical controls test two separate correct identities but do not justify their composition. The target constant does not decide the claimed full-ideal membership.

## Exact source comparison

The accepted moving-face normalization, §2, fixes `d=[g]B=5k²/9` and `[A,B]=−5k³g²/9`. The low-jet producer §1 and independent gate §3 instead define `e=[p]B`. Explicitly:

| Symbol | Literal coefficient | Degree-deficit weight |
| --- | --- | --- |
| k | [g²p]A | 12 |
| x,y | [gp²]A,[p³]A | 12,12 |
| d | [g]B=5k²/9 | 24 |
| e | [p]B | 24 |

With `a=[p]A`, the homogeneous parts are `A₁=ap`, `B₁=dg+ep`, `A₃=kg²p+xgp²+yp³`, and `B₃=b21 g²p+b12 gp²+b03 p³`. Differentiation, with `[A,B]=A_g B_p−A_p B_g`, gives

    r0 = −da,
    r_gp = 2ke−2dx−2a b21,
    r_p2 = xe−3dy−a b12,
    r_g2 = −kd+5k³/9 = 0 identically.

Here d and e are the indicated coefficients; the full derivatives B_g and B_p need not be constant. On k≠0 the already accepted low equations give `a=0`, `9e=5kx`, `x²=3ky`.

Fable's control.py lines70 and81–83 call **B10** “e” while verifying the g² coefficient `−A21·B10` and the axis restriction. Lines85–92 then introduce a scalar “e” satisfying `9e=5kx`, which is the source's **B01**. Nothing there tests or establishes B10=B01. The whole code was read statically, not executed.

## Correct identity and failed inference

In the localized low quotient, and hence every further source quotient,

    L := −k+2x−3y
       = −(x−k)²/k
       = −(9e−5k²)²/(25k³),     e=[p]B.

Thus the square identity is valid. Reading the target `−5k³/9` fixes **d**, not e; it supplies no equality e=d and no conclusion L=0. Matching weights cannot repair this: under `wt(Aij)=15−i−j`, `wt(Bij)=25−i−j`, both d and e have weight24, while x,y,k have weight12.

A degree-three exact negative control is `k=1`, `A=g²p`, `B=5g/9`. Then `d=5/9`, `a=x=y=e=0`; the complete bracket is `−5g²/9`, all displayed saturated low equations hold, but `L=−1`. This checks the precise insufficient premises only: it lacks the full prescribed outer faces and polynomial-lift rows, is **not** a full-source point, and decides no full ideal.

There is a separate scheme-theoretic caveat. In an arbitrary further quotient, L=0 is equivalent to `(9e−5k²)²=0`, not necessarily `9e=5k²`. The latter equivalence is valid at field points or in a reduced quotient; the low quotient being a domain does not make every full-source quotient reduced. No conclusion on full-ideal membership or its radical is established here.

## Custody and stop

Exact six input hashes and whole-read/static-code scope are in `box/d125-cross-e-coefficient-discriminator-20260907/inputs.json`. No mathematical code was run; the displayed differentiation and negative control are hand algebra of degree≤3. No AWS/CAS, full-source arithmetic, live Volta work, canonical edits or new theorem search. This report corrects one proposed arrow only. All task writers are terminal at handoff; no promotion or follow-on execution is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3278`.
- Body SHA-256:
  `ec7eeeb684b26e91093c051b756b0171a48d2ad9d5cca15c21165fe3065dcca2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
