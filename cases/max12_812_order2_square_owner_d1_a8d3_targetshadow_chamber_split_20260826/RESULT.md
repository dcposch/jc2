# Result: D1 `a=8,d=3` target-shadow chamber split

Date: 2026-08-26

Status: **TRIPLE-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact producer theorem

After the frozen square/D1 source gates, in characteristic zero on
`D(p*k0*J)`, the complete seven-equation system has no point in the strict
contact tail

```text
ord(A)=8, ord(C)=11, ord(R)>=8.
```

The proof uses four literal odd Faber equations from the frozen complete
grade-38 parent.  Since their subsystem is empty, no condition on the three
unused even equations is needed.  No leading coefficient of `R` is inverted,
so the conclusion is the entire closed `ord(R)>=8` tail.

## Grade-28 split and terminal identity

Write the leading ordinary numerator of `C` as `c1*z+c0`.  The row-one
grade-28 equation is exactly

```text
[sigma^28] Phi1 = (3/4)*k60*c1.
```

From the literal source rows form

```text
S = Phi7 + (p(sigma)/4)*Phi5
         + (3*p(sigma)^2/32)*Phi3
         + (5*p(sigma)^3/128)*Phi1.
```

Explicit polynomial reduction gives

```text
S = 0 mod sigma^38,
[sigma^38] S = -(3/32)*p*eta*k60*c1*b0.
```

This is the corrected moving-connection residual.  It is read from the
canonical literal rows and does not use the falsified fixed-`z` analytic
bridge.  In the full equations the same combination differs from its source
by the sole odd terminal target `-sigma^38*J/4`.

The exact-`C` locus is the exhaustive scheme-theoretic cover

```text
D(c1)  union  (V(c1) intersect D(c0)).
```

- On `D(c1)`, row one forces `k60=0`, hence the displayed source residual
  vanishes.
- On `V(c1) intersect D(c0)`, the source residual vanishes directly.

On either branch the terminal combination is therefore `-J/4`.  The two
compiled ideals, after adjoining the relevant `C` inverse and inverses for
`p,k0,J`, both contain `1` before radicals.  This is an exact ideal-membership
certificate, not a point sample.

## Complete-source custody

The compiler pins the three characteristic-specific literal parent programs,
their common complete source inventory, the frozen failed-route result, the
corrected moving-connection diagnostic, and the rank-jump producer freeze.
The parent inventory independently enumerates all 17 licensed primitive
families and every source/load/moving-`p`/target jet through grade 38.  The
current compiler imports the four literal odd rows byte-for-byte, uses only
ordinary polynomial rings and explicit `reduce(...,std(ideal(...)))`, and
checks the row-one coefficient, source residual, terminal target, both chart
ideals, and the exact-`C` cover.

Exact `Q` on Box02 and fresh `F_65519`/`F_65521` controls on Box03/r6d each
return rc zero, the terminal PASS marker, empty compiler stderr, no Singular
diagnostic, and zero swap.  Their mathematical stdout is byte-identical.
Launch/resource details are in `AWS_LAUNCH_METADATA.md`; all retrieved bytes
are frozen by `EVIDENCE.sha256`.

## Firewall

This producer closes only the named `a=8,d=3,ord(R)>=8` tail after the cited
source gates and on `D(p*k0*J)`.  On a Keller source `J` is a unit, so the
campaign may later reconcile the common open as `D(p*k0)`, but that global
composition is not asserted here.  This result says nothing about `J=0`,
`p=0`, `k0=0`, an equality or another leading-face chamber, positive-order
load, another D1 region, the whole square component, order two, `(8,12)`,
maximum twelve, or JC2.  Promotion requires an independent hostile review.
