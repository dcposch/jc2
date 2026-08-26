# TD6 FIRST generic-surjectivity corollary

Date: 2026-08-26

Status: **EXACT LINEAR-ALGEBRA COROLLARY OF HOSTILE-REVIEWED INPUTS; REVIEW
OF THIS FORMULATION PENDING.**

Let

```text
K = E(C,V,U)
```

be the generic symbolic-center field of the fixed source-typed A3/F1 TD6
slice.  After the 3,470-row transport echelon, the packed FIRST system has 132
unknown source-lift coefficients and exactly 38 nonzero equations.  Its base
coefficient map

```text
A0 : K^132 -> K^38
```

has rank 38.  Equivalently, `A0` is surjective and its cokernel is zero.
This rank, the absence of any dependent FIRST row, and the exact source replay
are independently confirmed in

```text
3f62b23d43e134eedb53ecd6e78511ca10606f46e6c0007d510596d9516bd93b
  xmodel/td6_v82s2_kernel_dead_first_hostile_review_v2_20260826.md.
```

## Corollary

On the generic rank-38 open, the FIRST conormal vanishes for **every
well-typed square-zero perturbation of this same source presentation**, not
only for the 22 q axes or the two transport-kernel dead-stretch axes already
tested.

Indeed, write a licensed first-order perturbation and a base solution as

```text
A = A0 + eps*A1,       b = b0 + eps*b1,       x = x0 + eps*x1,
eps^2 = 0,             A0*x0 = b0.
```

The coefficient of `eps` is the equation

```text
A0*x1 = b1 - A1*x0.
```

Because `A0` is surjective, the right-hand side has a solution for every
well-typed pair `(A1,b1)`.  Thus no FIRST compatibility functional exists:
`coker(A0)=0`.  This proof includes the varying-matrix term `A1*x0`; omitting
it would not be a source-valid linearization.

The reviewed V78 q-axis and V82S2 `d10,d15` calculations remain load-bearing
source-ancestry controls.  They prove that the advertised perturbations were
actually inserted, that their direct/source columns are nonzero where claimed,
that omission changes those columns, and that the varying echelon was replayed.
They are not the mathematical reason the final FIRST conormal is zero.  The
reason is full row rank.  The reviewed V78 input is

```text
a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861
  xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md.
```

Combining this corollary with the separately reviewed V81C transport theorem

```text
dfac352887f645a9dd1f03a32b4701372b32de3a445bfd496c74109e64381ebb
  xmodel/td6_v81c_dead_transport_rank_hostile_review_20260826.md
```

shows that FIRST removes no vector from the 24-dimensional transport kernel
`Q22 + d10 + d15`.  Exactly those 24 directions survive the cumulative
transport-plus-FIRST gate.

## Rank-drop and scope firewall

This is a generic-field statement, or equivalently a statement on the open
where the source chart is legal and a 38-by-38 maximal minor of `A0` is
nonzero.  It does **not** assert surjectivity on the rank-drop divisor or after
specializing a denominator/pivot factor to zero.  Those fibres require raw
reconstruction; their cokernel can grow.

“Every perturbation” means every square-zero deformation that preserves this
licensed FIRST row/column presentation and carries all direct, transported,
and varying-matrix terms.  It does not cover a new chart, a new equation, an
unlicensed source coefficient, a perturbation that changes the presentation,
or a nonlinear deformation.

The corollary says nothing about previous, pole, current, second order,
Kuranishi/Fitting zero loci, a neighborhood or family, the full TD6 source,
SP-2, or JC2.  Operationally, further isolated FIRST-axis computations on the
same generic rank-38 presentation are redundant.  The next information can
first occur at previous/pole/current, on a rank-drop fibre, or at higher order.
