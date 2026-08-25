# Preregistration: exact-Q `modStd` b=1 loaded saturation

Date: 2026-08-25  
Scope: producer-internal exact characteristic-zero accelerator; no theorem from a modular trace alone.

## Source and chart

Use the pinned corrected-Q8 approximate-cubic compiler and impose exactly
`I=(e1,e3,e5,e7,e2,e4)`.  On the doubled normal-rank-drop support set
`d4=1`, `d2=2+u`, put `A=x3-2*x5` and form the selected localizer ideal

```text
J = I + (inv*w*x5*A-1)
```

over `Q(c)[inv,w,u,x1,x3,x5]`, with `inv` in the first elimination block.
This is the generic finite-`c` b=1 stratum.  Exceptional finite values of `c`
must be recovered in the separate polynomial-parameter lane; coefficient
infinity is not represented here.

## Distinct algorithm

Load Singular `modstd.lib` and compute `GJ=modStd(J,1)` over characteristic
zero.  Contract `inv` and impose the landing centre
`w=u=x1=x3=x5=0`, again using `modStd`.  This is a genuine rational
multi-modular reconstruction path, distinct from direct `std`, `slimgb`, and
the unsafe msolve `-g` short circuit.

Before the full source, run a tiny `Q(c)` control and require a rational basis
whose original generators reduce to zero.  For the source run require:

1. every original generator of `J` reduces to zero modulo reconstructed `GJ`;
2. every contraction generator reduces to zero modulo reconstructed `GC`;
3. every landing generator reduces to zero modulo reconstructed `GL`;
4. the complete reconstructed rational bases are printed with stable markers;
5. if `GL=(1)`, print a `lift`-based exact membership residual for `1` in the
   landing ideal and require the residual to be zero.

The `modStd` trace, good-prime count, or a candidate unit without all checks is
nonpromotional.  Even `landing_empty=1` is scoped only to this generic-`c`,
b=1, finite selected centre and does not exclude other rank-drop points,
exceptional `c`, arbitrary coefficient infinity, Taylor/terminal realization,
general `(9,12)`, maximum twelve, or JC2.

