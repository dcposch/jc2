# Erratum: AS F-only post-D10 D9/D8 omitted Frobenius cross-carry

**Status: SOURCE-HONEST RETRACTION; PRODUCER EXACT; HOSTILE REVIEW PENDING.**

## Headline

Quarantine the compatibility claims and censuses in
`xmodel/as-fonly-d7-postd10-d98-f3-20260824.md`.  Its generator included the
divided linear term `L/3` from the six degree-six Frobenius first-digit
directions, but then formed the following degree-nine/eight residual from
`M` alone.  It omitted the single-cross term

```text
[K_Frob/3] mod 3.                                  (1)
```

This term is nonzero in exact integer witnesses.  Therefore the frozen
inhomogeneous columns, the vertical `50939/177147` compatibility census,
the `g`-endpoint `954/4374` census, and their rank-stream hashes are
retracted.  The frozen bytes are not mutated.

## Exact source

For

```text
P=x-x^3+3U+9C,  Q=y+3V+9D,
L=U_x+V_y-x^2,
K=(U_x-x^2)V_y-U_yV_x,
```

the integer identity is

```text
det J(P,Q)-1=3L+9(K+C_x+D_y)+27M+81N.             (2)
```

The reviewed first-digit equations make `L=3L1`.  After solving the next
accepted row, `E=L1+K+C_x+D_y=3E1`, the following residual is

```text
(det J(P,Q)-1)/27 = E1+M+3N.                       (3)
```

Write `U=U0+UF`, `V=V0+VF`, where every derivative of the degree-six
Frobenius part is divisible by three.  Modulo three, the omitted single
cross in `E1` is

```text
K_Frob/3 =
 (UF_x/3) V0_y +(U0_x-x^2)(VF_y/3)
 -(UF_y/3)V0_x-U0_y(VF_x/3).                       (4)
```

The product of two Frobenius derivatives remains divisible by three after
division and vanishes in (4).  Formula (4) can reach total degree eight
against a degree-four base term, and degree nine against the `g x^5` term.

## Smallest witnesses

For the frozen vertical fiber-count-one representative

```text
(P,Q,R,T,s,w,h)=(0,0,0,1,0,0,0),
f_b=u6_6=1,
```

the integer representatives are

```text
U0=2x^4,  V0=x^2y+x^3y,  UF=x^6,  VF=0.
```

Direct expansion gives

```text
[(K(U0+UF,V0)-K(U0,V0))/3] mod 3
   =2x^7+2x^8.                                     (5)
```

In particular, the omitted degree-eight coefficient is `2`, so the frozen
vertical affine column and every compatibility count derived from it are
wrong.

On the `g=1` endpoint take the previously omitted pure Frobenius direction
`UF=y^6` and `V0=x^2y+x^5`.  Then

```text
[(K(UF,V0)-K(0,V0))/3] mod 3 =2xy^6+2x^4y^5.       (6)
```

which has total degree nine.  Thus the claims that the two old D9 rows
force `f_c=f_d=0`, and that the remaining system is the displayed
`13 x 14` system, are also invalid.

## Preservation table

Preserved:

- the consumed, different-model-confirmed D10 gate;
- the integer orientation (2) and the accepted `L/3` degree-five row;
- the vertical degree-nine global section, because no single Frobenius
  cross can exceed degree eight when the degree-five base layer is zero;
- the six vertical degree-eight unit pivots, triangular coordinate change,
  `7 x 5` **coefficient matrix**, and its geometric rank loci.  Formula (4)
  changes only the inhomogeneous column.

Retracted:

- the assertion that the frozen vertical degree-eight column was the exact
  source column;
- all frozen vertical compatibility counts, fiber histograms,
  representatives, and the hash `d7910730...`;
- the `g`-endpoint equations `g f_c=g f_d=0`, the `13 x 14` reduction, all
  its compatibility counts/histograms, and the hash `119580e2...`;
- the statement that the four displayed Frobenius variables were the only
  relevant degree-six directions.  The pure directions `u6_0,v6_6` enter
  (4), as witness (6) shows.

No other producer or canonical ledger is changed by this erratum.  The
correct successor must regenerate every affected inhomogeneous row from
(2)--(4), retain all six Frobenius directions, and only then repeat the
literal-F3 census or advance a divided carry.  No lift, no-lift, full-D7,
characteristic-zero, counterexample, or JC2 inference survives from the
retracted counts.
