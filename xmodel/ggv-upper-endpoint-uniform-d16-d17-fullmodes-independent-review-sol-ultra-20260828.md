# Independent uniform full-mode review through `D17`

Date: 2026-08-28  
Method: exact `fractions.Fraction` arithmetic, direct ordinary-`Q[X]`
determinant replay, and a separately derived formal-series calculation

## Verdict

**PASS through `D17`, with an essential causal qualification.**  The claimed
weight-16 numerator, its centered form, the constant-`F8` gauge action, and
the weight-17 invariant are exact.  The born `c16/A^2` term is the indicial
kernel at weight 16.  Therefore `c16` is fixed by same-weight polynomiality;
it is not killed by a later determinant row.  Its apparent weight-17
successor obstruction cancels exactly against the mixed predecessor term.

The proved field-point continuation is

```text
N16=(3/8)B^2+(1/2)c8*B+c16=A^2*M,
K17=(3B+2c8)C-2M in (A^2).
```

## 1. Correct defects and weight-16 pole

Continue the polynomial square-root prefix as

```text
S7=A^2+t/2+(Z/8)t^2+(V/16)t^3+(R/2)t^4
       +(Q/2)t^5+(T/2)t^6+(Y/2)t^7.
```

The next two coefficients of `S7^2` are

```text
[t^8]S7^2=Y/2+T*Z/8+Q*V/16+R^2/4,
[t^9]S7^2=Q*R/2+T*V/16+Y*Z/8.
```

Thus the honest defects are

```text
B=F8-Y/2-T*Z/8-Q*V/16-R^2/4,
C=F9-Q*R/2-T*V/16-Y*Z/8.
```

Put `F=S7^2+epsilon`, where `epsilon=B*t^8+C*t^9+...`.  Through weight 17,

```text
F^(3/2)=S7^3+(3/2)S7*epsilon+(3/8)epsilon^2/S7+...,
F^(1/2)=S7+(1/2)epsilon/S7+... .
```

With `c6=c10=c14=0`, the complete polar coefficient at weight 16 is

```text
polar(g16)=N16/A^2,
N16=(3/8)B^2+(1/2)c8*B+c16.
```

Here the three summands come respectively from `F^(3/2)`,
`c8*t^8*F^(1/2)`, and `c16*t^16*F^(-1/2)`.  The `c4*F12` contribution is
regular, `c12` has no tail, and `c18,c20` have not been born.

The centered variables

```text
Bhat=B+(2/3)c8,
J16=c16-c8^2/6
```

give the exact completed square

```text
N16=(3/8)Bhat^2+J16.
```

## 2. Causal role of `c16`

For

```text
L_n(P)=4*(12-n)*A^3*A'*P-8*A^4*P',
```

one has

```text
L_16(c16/A^2)=0
```

identically.  More generally,

```text
-L_16(N16/A^2)=8*A^2*N16'.
```

This differentiated equation cannot license setting its integration
constant to zero.  The actual causal input is that raw `G16` is a polynomial.
Its characteristic coefficient contains `N16/A^2`, so polynomiality forces

```text
A^2 | N16.
```

Write `N16=A^2*M`.  This condition determines the born scalar `c16` together
with root-value and root-jet compatibilities.  It permits nonzero `c16`; it
does not assume or prove `c16=0`.  The missing degrees 0 and 1 in the raw
window `G16[X^2..X^8]` impose additional regular equations after the pole is
removed, but regular terms cannot cancel an `A`-adic pole.

## 3. Constant-`F8` gauge

Let

```text
Fnew=Fold+mu*t^8
```

and keep the polynomial `G` fixed.  Expressing the old characteristic series
in terms of `Fnew` gives

```text
Bnew   = B+mu,
Cnew   = C,
c4new  = c4,
c8new  = c8-(3/2)mu,
c12new = c12-c4*mu,
c16new = c16-(1/2)c8*mu+(3/8)mu^2.
```

Under the already killed `c6,c10,c14`, the remaining modes through weight 20
are unchanged.  Direct substitution shows

```text
Bhatnew=Bhat,
J16new=J16,
N16new=N16,
Mnew=M.
```

Thus the centering is not cosmetic: it is exactly the quotient by the global
constant-`F8` additive gauge.  The `c12` shear is required for the full-mode
action whenever `c4` is nonzero.

## 4. Weight 17 and the invariant

The needed inverse-prefix coefficients are

```text
(1/S7)_0=1/A^2,
(1/S7)_1=-1/(2*A^4).
```

Exact expansion gives

```text
polar(g17)
 =(3B+2c8)C/(4*A^2)-N16/(2*A^4).
```

The `A^-4` numerator combines

```text
-3B^2/16-c8*B/4-c16/2 = -N16/2,
```

which checks every coefficient and sign.  After `N16=A^2*M`, put

```text
K17=(3B+2c8)C-2M.
```

Then

```text
polar(g17)=K17/(4*A^2).
```

Polynomiality therefore gives `A^2|K17`.  The raw determinant rows recover
the same conclusion in two visible lifts.  If `q17` denotes the unavailable
regular part of `G17`, then

```text
D17(raw)
 =A*A'*K17+2*A^2*K17'
  +20*A^3*A'*q17+8*A^4*q17'.
```

Consequently

```text
D17(raw)=A*A'*K17                         (mod A^2),
```

so squarefreeness gives `K17=A*L`.  Substitution then gives

```text
D17(raw)=3*A^2*A'*L                       (mod A^3),
```

and hence `A|L`.  Thus `K17 in (A^2)`.  Regular lower-window equations begin
in `A^3` and do not affect either lift.

The gauge action fixes `3B+2c8`, `C`, and `M`, so it also fixes `K17`.

## 5. Required predecessor cancellation

The formal `c16` mode begins with

```text
g16=c16/A^2,
g17=-c16/(2*A^4).
```

At weight 17 its mixed `i=1,j=16` contribution is

```text
-4*F1'*(c16/A^2)-7*F1*(c16/A^2)'
 =+6*c16*A'/A,
```

where `F1=A^2`.  The new-coefficient contribution is

```text
L_17(-c16/(2*A^4))=-6*c16*A'/A.
```

They cancel exactly.  Therefore a calculation which retains only the second
line manufactures a false successor obstruction.  No `D17` row kills
`c16`.  Once weight-16 polynomiality has combined all three numerator terms
into `N16=A^2*M`, raw `g16` contains the regular quotient `M`; the displayed
`K17` is then the correct remaining weight-17 pole, with no omitted
predecessor correction.

## 6. Literal controls

### 6.1 Exact gauge orbit

Let `S0=A^2+t/2` and

```text
F=S0^2+mu*t^8,
G=S0^3.
```

The additive weight-eight term contributes neither through `F_X` nor through
the factor `(i-8)F_i`, so every raw determinant row vanishes.  Its
characteristic constants are

```text
B=mu,
c8=-(3/2)mu,
c16=(3/8)mu^2,
Bhat=J16=N16=0.
```

The values `mu=1,-1,2` check the linear and quadratic gauge signs.

### 6.2 Weight-16 live residual

Take

```text
F=S0^2+X*t^8
```

and a scalar `s=c8`.  Through weight 15 take the polynomial coefficients of
`F^(3/2)+s*t^8*F^(1/2)`, namely, in addition to `S0^3`,

```text
G8=(3/2)A^2*X+s*A^2,
G9=(3/4)X+s/2,
G10=...=G16=0.
```

Direct ordinary-`Q[X]` recurrence gives

```text
D4=...=D15=0,
D16=(6X+4s)A^2.
```

This catches both the `3B^2/8` and `c8*B/2` coefficients and their signs.

### 6.3 First weight-17 lift

Take

```text
F=S0^2+(A*X)t^8+X*t^9,
c8=c16=0,
G16=(3/8)X^2,
```

with the lower `G` coefficients supplied by `(3/2)S0*((A*X)t^8+X*t^9)`.
Then `D4=...=D16=0`, while

```text
K17=3*A*X^2-(3/4)X^2,
D17=A*A'*K17+2*A^2*K17',
D17=-(3/4)A*A'*X^2                       (mod A^2).
```

### 6.4 Literal second-lift fixture

For a full raw-window control, set `A=X^4-1`, `S0=A^2+t/2`, all
`Z,V,R,Q,T,Y` to zero, and

```text
F8 = 1+(3/2)X^2-2X^4-(1/2)X^6+X^8,
F9 = -(3/16)X^2+(1/2)X^4,
F10=...=F14=0.
```

Use the baseline

```text
G0=A^6, G1=(3/2)A^4, G2=(3/4)A^2, G3=1/8,
G4=...=G7=0,
```

and assign

```text
G8 = 3/2 +(9/4)X^2-6X^4-(21/4)X^6+9X^8
      +(15/4)X^10-6X^12-(3/4)X^14+(3/2)X^16,

G9 = 3/4 +(27/32)X^2-(3/4)X^4+(3/16)X^6
      -(3/4)X^8-(9/32)X^10+(3/4)X^12,

G10=-(9/64)X^2+(3/8)X^4,
G11=G12=G13=G14=G15=0,
G16=(9/8)X^2-(21/32)X^4-(3/8)X^6+(3/8)X^8,
G17=-(21/64)X^2+(3/8)X^4.
```

Here `c8=0`, `c16=-3/8`, and

```text
N16=A^2*M,
M=(9/8)X^2-(21/32)X^4-(3/8)X^6+(3/8)X^8.
```

The invariant has exactly one factor of `A`:

```text
K17=A*L,
L=(45/16)X^2-(63/32)X^4-(21/16)X^6+(3/2)X^8,
L mod A=-15/32+(3/2)X^2 != 0.
```

Direct recurrence evaluation gives `D4=...=D16=0` and the full residual

```text
D17 = -6X+(15/4)X^3+36X^5-(135/8)X^7-54X^9
       +(45/2)X^11+24X^13-(75/8)X^15.
```

Thus this fixture catches the second `A`-adic lift, not merely the first
congruence.  Every displayed polynomial lies inside its authoritative raw
window.

## 7. Scope firewall

This review establishes only the exact uniform full-fixture characteristic
continuation through `D17` on characteristic-zero field points.  It does not
promote the divisibilities to identities of the upstream nonreduced scheme,
does not normalize a carrier, and does not divide by `Bhat`, `C`, `M`, or any
coefficient.  It makes no endpoint-stratum, unrestricted branch-P,
Keller-pair, counterexample, or JC2 claim.

No producer packet or canonical ledger was edited.  No CAS, AWS computation,
floating point, interpolation, or `jc2-lean` artifact was used.
