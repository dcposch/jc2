# One-parameter source history and type audit

Date: 2026-08-27

Verdict: **PASS.  THE FROZEN SOURCE MAP IS SUFFICIENT FOR THE CHARGED
CLOSURE-FIRST INCIDENCE.**

## History checked

1. The original strict-Rees client charged the `U=2,[6,2]` source and all
   seven finite loads.  Its later erratum is load-bearing: the strict open
   also inverts the nonzero Jacobian constant `j`.
2. The V2 compiler/source review froze the 569 ordinary-tail monomials in
   the ten variables `(a0,...,a6,k10,k6,k2)`.  The JSON has seven row keys,
   correct Faber weights, and is affine-linear in the three lower loads.
3. The one-parameter theorem applies the unit change `J=(1+tau)j` and the
   flat base map `Lambda=tau^3*varrho`.  It retains every load and gives
   exact targets `(0,mu2,0,mu4,0,mu6,J/4)`.
4. The promotion and two independent reviews agree that the operation is
   sequential saturation by `Lambda`, then the Jacobian parameter, before
   taking the `Lambda=0` fibre.  They explicitly forbid solving/projecting
   the target loads before closure.
5. The frozen one-parameter compiler implements that source in
   `Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J]`.  Its prior exact-Q and
   characteristic-32003 AWS jobs reached only the start of the first
   saturation and preserve no endpoint; they are not reused as evidence.
6. The K00 discriminator design supplies the invariant core `M_K00`, the
   final localizer, the noncommutation warning, and the both-outcome scope.

The charged files and hashes are pinned by `SOURCE_CLOSURE.sha256` and are
also checked internally by the new compiler before it emits any Singular
input.

## Type map used here

```text
old one-parameter J  |-->  Jdet  (Jacobian parameter)
collision J1,J2      |-->  no ring variable; no substitution
a_i tail coefficient |-->  C_i
k10,k6,k2            |-->  Lambda^(2,6,10) scaled loads in each tail
mu2,mu4,mu6,Jdet/4   |-->  row targets at Lambda^(14,16,18,19)
```

The rename `J -> Jdet` is alpha-conversion only.  It prevents a notation
collision with the unrelated correction ideals `J1` and `J2`; no formula,
open, or saturation changes.

The invariant K00 core is well typed in the same ring:

```text
(C5,C3,C1,8*C4-3*C6^2,16*C2-C6^3,256*C0-C6^4,
 k6,k2,mu2,mu4,mu6),
```

leaving `Lambda,C6,k10,Jdet` free until the charged boundary/localization
operations.  The compiler independently reduces rows 1--6 to zero and row
7 to `-Lambda^19*Jdet/4` modulo this core before starting either expensive
saturation.

## Order firewall

The mathematical lane constructs

```text
I -> I:Lambda^infinity -> (...):Jdet^infinity
  -> +(Lambda)+M_K00 -> :(C6*k10*Jdet)^infinity.
```

The separate restriction-first ideal is used only to reproduce the known
unit certificate.  It is not fed into `K`, `B`, or `H`.  Thus the implementation
does not silently replace closure-then-restriction by restriction-then-closure.
