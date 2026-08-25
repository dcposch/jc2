# Maximum-12 `(9,12)` order-three unordered critical-value norm

**Status: producer-exact stratification checkpoint; hostile review required.**

## Result

On the reviewed `k=mu=0, nu!=0` landing, normalize the constant `nu` to one
and write `rho=r8`, `p=a7/3`.  The quadratic Wronskian is

```text
B=54*z^2+18*p+60*rho=54*(z^2-s),
s=-(a7+10*rho)/9.
```

Reduce in the quadratic coefficient algebra `z^2=s`:

```text
f^4 = F0+F1*z,
g^3 = G0+G1*z.
```

Then the resultant with the two unordered roots of `B`, after its explicit
leading scalar/content, is

```text
C(T)=Norm(g^3-T*f^4)=C0+C1*T+C2*T^2,
C0=G0^2-s*G1^2,
C1=-2*(G0*F0-s*G1*F1),
C2=F0^2-s*F1^2.
```

With `E=G0*F1-G1*F0`, exact polynomial algebra gives

```text
disc_T C = 4*s*E^2,
C(1)=Norm((g^3-f^4) mod B).
```

This eliminates the field-of-definition ambiguity caused by choosing one
root of `B`.  On the open set `s*Norm(F)!=0`, the following four leaves are
disjoint and exhaustive:

1. `W0=W1=0`: both critical points lie over `beta=1` (the reviewed full-
   absorption branch);
2. `Norm(W)=0` but `(W0,W1)!=(0,0)`: exactly one lies over `1`;
3. `Norm(W)!=0` and `E=0`: the two distinct critical points have the same
   non-`1` value;
4. `Norm(W)*E!=0`: neither is absorbed and their values are unequal.

The loci `s=0` and `Norm(F)=0` are retained separately.  On `s=0`, `B` has a
double root and one splits further by whether `W0` vanishes.  `Norm(F)=0`
records a `B`-root on `f`; the actual-Keller coprimality firewall may be
applied only with its reviewed hypotheses.

## Why the representation is small

Expanding `C(T)` in the eight raw coefficients and `rho` produces coefficient
polynomials with up to roughly 200,000 monomials.  The quadratic-pair
representation is exact and source-replayable: the base reductions of `f`
and `g` have only `10/11` and `44/27` even/odd terms, while the replay hashes
the exact `f^4` and `g^3` pairs.  This is the proof-carrying input for later
leaf ideals; it does not hide a selected algebraic root.

The parity locus is a positive control: `f` is odd and `g` is even, so
`F1=G1=0` and `E=0`, placing parity in the equal-value leaf without claiming
that it is the whole leaf.

## Scope and next gate

This report proves only the coefficient-field case split.  It does not empty
the one-absorption, equal-value, double-root-off-`W`, or generic leaves; it
does not transport the Taylor boundaries or terminal ODE.  The next exact
gate is to attach the original seven fibre rows and both Taylor families to
each leaf, then use cube-divisor or four-point Hurwitz genus before any broad
primary decomposition.

Replay:

```sh
python3 cases/max12_912_order3_critical_value_norm_20260824/replay.py \
  | diff -u cases/max12_912_order3_critical_value_norm_20260824/replay.json -
```
