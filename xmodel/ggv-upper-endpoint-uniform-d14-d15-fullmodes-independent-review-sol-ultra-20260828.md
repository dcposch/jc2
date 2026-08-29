# Independent uniform full-mode review through `D15`

Date: 2026-08-28  
Method: exact `fractions.Fraction` sparse arithmetic and hand recurrence; no CAS

## Verdict

**PASS, with a necessary causal correction for `c14`.**  The honest `D14`
defect contains the previously omitted `T/2`.  The `D14` and `D15` square
congruences have signs `-3` and `+3/4`, respectively.  The born negative mode
`c14` is forced to zero by polynomiality at weight 14; it is not killed by a
successor determinant row.  Its apparent two weight-15 contributions cancel
exactly.

This is a characteristic-zero field-point continuation only.

## 1. Honest defects

Put

```text
B0=A^2+t/2+(Z/8)t^2+(V/16)t^3+(R/2)t^4
        +(Q/2)t^5+(T/2)t^6.
```

Then

```text
[t^7]B0^2 = T/2+Z*Q/8+V*R/16,
[t^8]B0^2 = Z*T/8+V*Q/16+R^2/4.
```

Hence the correct defects are

```text
e7  = F7-T/2-Z*Q/8-V*R/16,
e80 = F8-Z*T/8-V*Q/16-R^2/4.
```

Writing `F=B0^2+epsilon`, the terms relevant through weight 15 follow from

```text
F^(3/2)=B0^3+(3/2)B0*epsilon+(3/8)epsilon^2/B0+O(t^16 regular,t^21),
F^(1/2)=B0+(1/2)epsilon/B0+O(epsilon^2),
(F^(-1/4))_0=A^(-1),
(F^(-1/4))_1=-1/(4*A^3).
```

## 2. Weight 14

With the complete mode schedule retained and the prior conclusions
`c6=c10=0`, the only polar terms are

```text
polar(g14)=3*e7^2/(8*A^2)+c14/A.
```

The other causal contributions are regular: `c4*F10` and `c8*T/2`.
The `c12` mode has no weight-14 tail, and `c16,c18,c20` have not been born.

For

```text
L_n(P)=4*(12-n)*A^3*A'*P-8*A^4*P',
D_n(raw)=-L_n(polar mismatch),
```

the square part gives

```text
-L_14(3*e7^2/(8*A^2))
  =6*A^2*e7*e7'-3*A*A'*e7^2,
```

whereas

```text
L_14(c14/A)=0
```

identically.  Any unavailable regular `G14` term contributes a multiple of
`A^3`, so the literal-row congruence is

```text
D14(raw) = -3*A*A'*e7^2                 (mod A^2).
```

Since `A=X^4-1` is squarefree, a characteristic-zero field point satisfies
`A|e7`; write `e7=A*U`.  The square pole is then regular, leaving `c14/A`.
Because raw `G14` is a polynomial, this forces

```text
c14=0.
```

This is a same-weight polynomiality determination, not an assumption and not
a consequence of applying `L_14` to its kernel.  The absent constant slot of
the raw window `G14[X^1..X^10]` adds a regular scalar equation but cannot
change the divisibility or the `c14` conclusion.

## 3. Weight 15

Before the `D14` substitutions, the complete polar coefficient is

```text
polar(g15)
 =-3*e7^2/(16*A^4)
  +3*e7*e80/(4*A^2)
  +c8*e7/(2*A^2)
  -c14/(4*A^3).
```

After `e7=A*U` and the causally established `c14=0`, put

```text
h=(3/4)*U*e80+(1/2)*c8*U.
```

Then

```text
polar(g15)=-3*U^2/(16*A^2)+h/A,

-L_15(polar(g15))
  =(3/4)*A*A'*U^2-3*A^2*U*U'
   +4*A^2*A'*h+8*A^3*h'.
```

Regular lower-window mismatches begin in `A^3`.  Therefore

```text
D15(raw) = +(3/4)*A*A'*U^2              (mod A^2).
```

Squarefreeness again gives `A|U`; write `U=A*Y`.  Thus

```text
e7=A^2*Y,
F7=T/2+Z*Q/8+V*R/16+A^2*Y.
```

The genuine next square defect is now

```text
e8=e80-Y/2
  =F8-Y/2-Z*T/8-V*Q/16-R^2/4.
```

The new regular part of `g15` can be written either as

```text
-3*Y^2/16+(3/4)*Y*e80+(1/2)*c8*Y
```

or as

```text
(3/4)*Y*e8+(3/16)*Y^2+(1/2)*c8*Y.
```

Consequently `c8` is not killed.  Its coupling `c8*Y/2` survives in the
regular `G15` determination and, in particular, in the missing-constant-slot
compatibility for `G15[X^1..X^9]`.  No division by a coefficient of `Y` is
licensed.

## 4. Required predecessor cancellation

It is incorrect to inspect only the new weight-15 coefficient and claim

```text
-L_15(-c14/(4*A^3))=+3*c14*A'
```

as a raw successor obstruction.  The same characteristic mode already has
`g14=c14/A`.  Its mixed `i=1,j=14` contribution is

```text
-2*F1'*(c14/A)-7*F1*(c14/A)'=+3*c14*A',
```

while its `i=0,j=15` contribution is

```text
L_15(-c14/(4*A^3))=-3*c14*A'.
```

They cancel exactly.  Thus the complete `c14*t^14*F^(-1/4)` mode is
determinant-null at its successor as it must be.  The valid causal statement
is: polynomiality fixes `c14=0` at weight 14, after which `D15` forces the
second factor of `A` in `e7`.

## 5. Exact controls and scope

For a constant defect `e7=lambda`, the polar obstruction has

```text
D14=-3*lambda^2*A*A',
```

so `lambda=-1,1,2` checks the negative sign and square scaling.  After
`e7=A*U`, the constant choice `U=lambda` has leading successor residue

```text
D15=+(3/4)*lambda^2*A*A'                (mod A^2),
```

checking the positive sign.  A `c14`-only successor mutation must give zero
when both its weight-14 and weight-15 coefficients are retained; omitting
either one is a useful negative control for the predecessor audit.

No endpoint equation, `D16` or later obstruction, scheme-theoretic
divisibility, unrestricted branch-P exclusion, Keller-pair theorem, or JC2
conclusion is claimed here.  No repository producer, canonical ledger, CAS,
AWS job, or `jc2-lean` artifact was used or modified in this derivation.
