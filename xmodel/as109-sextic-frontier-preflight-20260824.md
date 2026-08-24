# AS109 sextic-y frontier preflight

**Verdict: `SURVIVING PFAFFIAN GATE`; no sextic theorem yet.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Prime/seed context: `p=109`, `(x-x^109,y)` over `F_109`
- Field calculations: arbitrary characteristic-zero field, temporarily over
  an algebraic closure
- Confirmed input: the corrected quartic theorem and its landed
  different-model `CONFIRMED` review
- Provisional context only: the coordinator-reported quintic closures of
  `(2,5)`, `(3,5)`, and the in-progress `(4,5)` infinity argument
- Generic exponent/support search, exponent rectangles, finite-Witt
  inference, AWS: none
- Exact lift found: no
- New AS109 exclusion claimed: no
- JC2 inference: none

After constant target operations and divisible-degree shears, the only new
coprime leading pair with maximum `y`-degree six is `(5,6)`.  The exact
rational normal form extends substantially: five Jacobian rows integrate,
and the next two rows give polynomial first integrals.  The remaining two
rows are

```text
I_3'=0,       I_2'=0,       omega(X')=0,
h eta(X')=j,                  X=(A,B,C,D).                (0.1)
```

Generically this is a rank-one algebraic Pfaffian foliation on the surface
`I_3=constant,I_2=constant`.  The decisive difference from the corrected
quartic gate is that `omega` is not closed: no third polynomial first
integral, monic depression equation, or pole exclusion follows from the
present calculation.  This is the first exact surviving coprime sextic
object and the narrow next gate.

A full `y`-degree-at-most-six theorem also has an independent imprimitive
branch `(4,6)`.  Its first two leading rows split exactly into a common
quadratic-generator branch and a square-leading branch with constant linear
depression mismatch.  Neither is removed by a target shear.  Thus this file
does **not** claim that all sextic-y Keller pairs are automorphisms and does
not strengthen the banked AS109 quartic exclusion.

## 1. Trust and scope

The quartic producer
`xmodel/as109-quartic-discriminator-gate-20260824.md` and its exact replay
were frozen before this task.  Its different-model review subsequently
landed `CONFIRMED`; this preflight uses only the resulting theorem for pairs
whose two `y`-degrees are at most four.

The quintic statuses supplied by the coordinator are treated as provisional
motivation.  They are not promoted, re-proved, or used to infer a sextic
theorem.  In particular, the unresolved `(4,5)` review state remains an
independent blocker even if both sextic patterns below are later closed.

All target operations below are field-level automorphy tests.  They need not
preserve the integral AS109 seed chart.  No canonical top-level file or
ledger is edited by this gate.

## 2. Exact degree-pair sweep

Let the actual `y`-degrees be `m<=n`.  For leading coefficients `a_m,b_n`,
the highest Jacobian coefficient is

```text
n a_m'b_n-m a_m b_n'=0.                                (2.1)
```

If `m=n`, their ratio is constant and target `GL_2` lowers one degree.  If
`m` divides `n`, unique factorization gives `b_n=k a_m^(n/m)` and the target
shear `g->g-k f^(n/m)` lowers `n`.  The `m=0` branch is triangular (and is
incompatible with an actual degree-six second coordinate).

For `n=6`, this exhausts

```text
(1,6), (2,6), (3,6)       target shears,
(6,6)                      target GL_2,
```

leaving exactly

```text
(4,6)   imprimitive, gcd=2,
(5,6)   primitive/coprime.                              (2.2)
```

Thus `(5,6)` is the only genuinely new coprime pattern.  A full theorem must
nevertheless handle `(4,6)` as well.

## 3. The imprimitive `(4,6)` split

For a genuine `(4,6)` pair, (2.1) and UFD valuations give, after constant
target scaling,

```text
a_4=H^2,                    b_6=H^3,
H in Kbar[x], H!=0.                                      (3.1)
```

Let `a_3,b_5` be the next coefficients and define

```text
N=3a_3H-2b_5.                                            (3.2)
```

The next Jacobian row is exactly

```text
[y^8]J
 =5a_4'b_5-4a_4b_5'+6a_3'b_6-3a_3b_6'
 =H(2H N'-5N H').                                       (3.3)
```

Consequently

```text
(N^2/H^5)'=0,                 N^2=kappa H^5.             (3.4)
```

This gives two genuinely different branches.

1. If `kappa=0`, then `N=0`.  The top two rows are compatible with a common
   quadratic generator

   ```text
   z=H y^2+r y+s,
   a_3=2Hr,                   b_5=3H^2r.                 (3.5)
   ```

   Lower rows must decide the even/odd residual coupling; this preflight
   does not derive that full normal form.

2. If `kappa!=0`, UFD valuations in (3.4) force
   `H=h^2` and `N=lambda h^5` for `h in Kbar[x]` and
   `lambda in Kbar^*`.  The linear depressions for leading terms
   `h^4 y^4,h^6 y^6` then differ by the constant

   ```text
   a_3/(4h^3)-b_5/(6h^5)=lambda/12.                     (3.6)
   ```

   Unlike the consecutive `(5,6)` case, adding a multiple of the
   degree-four coordinate cannot alter the degree-five coefficient of the
   degree-six coordinate.  The mismatch cannot be target-sheared away.

Equation (3.4) is a precise discriminator, not a closure theorem.  The two
branches are the imprimitive sextic resurrection conditions.

## 4. Leading normalization for `(5,6)`

Write a genuine coprime pair as

```text
f=a_5y^5+a_4y^4+...,             g=b_6y^6+b_5y^5+....
```

The top row is

```text
[y^10]J=6a_5'b_6-5a_5b_6'=0.                            (4.1)
```

UFD valuations give, after constant target scaling,

```text
a_5=h^5,                       b_6=h^6,
h in Kbar[x], h!=0.                                      (4.2)
```

The next row is

```text
[y^9]J
 =h^10 (6(a_4/h^4)'-5(b_5/h^5)').                      (4.3)
```

Hence

```text
6a_4/h^4-5b_5/h^5=constant
                  =30(r_f-r_g),                         (4.4)
```

where `r_f=a_4/(5h^4)` and `r_g=b_5/(6h^5)` are the two
depression shifts.  The allowed target addition `g->g+lambda f` changes the
left side of (4.4) by exactly `-5lambda`.  It therefore aligns the shifts
before a common variable is introduced.

With `z=hy+r`, there are exact rational functions
`A,B,C,D,P,Q,R,S,T in Kbar(x)` such that

```text
f=z^5+A z^3+B z^2+C z+D,
g=z^6+P z^4+Q z^3+R z^2+S z+T.                         (4.5)
```

This is an identity in `Kbar(x)[y]`, not a claim that the rational source
change is a polynomial automorphism.

## 5. All nine normal-form rows

The chain rule gives `J_(x,y)=h J_(x,z)`.  The coefficients of
`J_(x,z)(f,g)` from `z^8` through `z^0` are

```text
E8 = 6A'-5P',
E7 = 6B'-5Q',
E6 = -3AP'+4PA'+6C'-5R',
E5 = -3AQ'-2BP'+4PB'+3QA'+6D'-5S',
E4 = -3AR'-2BQ'-CP'+4PC'+3QB'+2RA'-5T',
E3 = -3AS'-2BR'-CQ'+4PD'+3QC'+2RB'+SA',
E2 = -3AT'-2BS'-CR'+3QD'+2RC'+SB',
E1 = -2BT'-CS'+2RD'+SC',
E0 = -CT'+SD'.                                         (5.1)
```

The first five equations integrate exactly to

```text
P = 6A/5+alpha,
Q = 6B/5+beta,
R = 3A^2/25+4alpha A/5+6C/5+gamma,
S = 6AB/25+4alpha B/5+3beta A/5+6D/5+delta,
T = -4A^3/125-2alpha A^2/25+6AC/25+2gamma A/5
    +3B^2/25+3beta B/5+4alpha C/5+epsilon,              (5.2)
```

for constants `alpha,beta,gamma,delta,epsilon in Kbar`.  Target
translations of `f` and `g` can remove `delta` and `epsilon`, respectively,
but retaining them makes the covariance of the exact equations visible.

## 6. Two polynomial first integrals

After (5.2), the next row is `E3=I_3'`, with

```text
I_3 = -12A^2B/25-4alpha AB/5-3beta A^2/5
      +6AD/5+delta A+6BC/5+2gamma B+3beta C+4alpha D.
                                                               (6.1)
```

The following row is `E2=I_2'`, with

```text
I_2 = 9A^4/125+4alpha A^3/25-12AB^2/25-12A^2C/25
      -4alpha AC/5-6beta AB/5-3gamma A^2/5-2alpha B^2/5
      +6BD/5+delta B+3C^2/5+2gamma C+3beta D.            (6.2)
```

Thus any Keller path has `I_3=k_3,I_2=k_2` for constants `k_3,k_2`.
These are genuine polynomial first integrals; no division or generic-rank
hypothesis enters their derivation.

## 7. The first surviving Pfaffian equation

Write

```text
E1=omega_A A'+omega_B B'+omega_C C'+omega_D D',
E0=eta_A A'+eta_B B'+eta_C C'+eta_D D'.                (7.1)
```

Exact substitution in (5.1) gives

```text
omega_A = 24A^2B/125+8alpha AB/25-18BC/25
          -3beta C/5-4gamma B/5,
omega_B = -12B^2/25-6AC/25-4alpha C/5-6beta B/5,
omega_C = -6AB/25-4alpha B/5+3beta A/5+6D/5+delta,
omega_D = 6A^2/25+8alpha A/5+6C/5+2gamma,              (7.2)

eta_A = 12A^2C/125+4alpha AC/25-6C^2/25-2gamma C/5,
eta_B = -6BC/25-3beta C/5,
eta_C = -6AC/25-4alpha C/5,
eta_D = 6AB/25+4alpha B/5+3beta A/5+6D/5+delta.         (7.3)
```

The Keller equations are precisely

```text
dI_3(X')=0,        dI_2(X')=0,        omega(X')=0,
h eta(X')=jbar!=0.                                      (7.4)
```

This is generically a determined rational vector field up to the time
factor `jbar/h`.  Indeed, with all integration constants zero, at

```text
A=B=C=0,       D=1,
```

the four row covectors `dI_3,dI_2,omega,eta` form the diagonal matrix with
diagonal `6/5`, so

```text
det(dI_3,dI_2,omega,eta)=(6/5)^4!=0.                   (7.5)
```

Thus (7.4) defines a rank-one algebraic foliation on a Zariski-open part of
the two-dimensional level surface of `I_3,I_2`; `eta` fixes its
parametrization.

The first obstruction to repeating the quartic proof is exact and visible:

```text
partial_B(omega_A)-partial_A(omega_B)
 =24A^2/125+8alpha A/25-12C/25-4gamma/5,               (7.6)
```

which is not identically zero.  Therefore `omega` is not itself the
differential of a polynomial or rational first integral by the immediate
quartic mechanism.  This does not prove that no integrating factor or first
integral exists on the `I_2,I_3` level surfaces; finding one, or proving none
can support a rational Keller trajectory, is the next exact gate.

## 8. Why pole-integrality stops here

At `y=0`, the original polynomial constant terms give two algebraic
equations

```text
f(x,0)=r^5+A r^3+B r^2+C r+D,
g(x,0)=r^6+P r^4+Q r^3+R r^2+S r+T.                   (8.1)
```

Together with `I_3=k_3,I_2=k_2`, these are four algebraic equations for the
five initially rational quantities `r,A,B,C,D`.  In the quartic gate, the
remaining Jacobian row integrated to a fifth algebraic equation, and
elimination produced a monic polynomial for `r`.  Here the remaining row is
the non-closed Pfaffian equation `omega(X')=0`; it supplies no fifth
algebraic relation presently.

Accordingly, this preflight has **not** shown

```text
r,A,B,C,D in Kbar[x].                                   (8.2)
```

Without (8.2), poles in the rational normal form can in principle cancel
against `h` in `h eta(X')=jbar`; the polynomial-unit contradiction used at
degrees three and four is unavailable.  A valid closure must do one of the
following:

1. produce a third algebraic first integral (possibly after an integrating
   factor or modulo `dI_2,dI_3`) and recover a monic eliminant for `r`;
2. prove directly, by weighted-projective infinity or valuation analysis,
   that (7.4) and the polynomial boundary data (8.1) admit no rational pole;
3. classify all rational integral curves of the foliation and show that none
   has `eta(X')!=0` with the required boundary data.

The ODE alone genuinely does not close.  With all integration constants
zero, the rational path

```text
A=B=C=0,             D=x^-5,             h=x^11         (8.3)
```

has `I_2'=I_3'=omega=0` and `h eta(X')=-6`.  Thus it solves the full
Pfaffian system with a nonzero constant last row.  It does **not** give a
polynomial Keller pair: choosing `r=-x^-1` makes the first boundary value in
(8.1) equal to zero, but the second is `-x^-6/5`, still with a pole.  This
negative control isolates the missing ingredient exactly: the two polynomial
boundary equations must be used together to rule out rational trajectories.

This is a precise obstruction gap, not evidence for a lift or a
counterexample.

## 9. Exact replay and controls

Run:

```text
python3 cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py
```

The standalone standard-library replay uses exact `Fraction` arithmetic in
a formal coefficient/differential algebra.  It checks:

- the complete degree-pair classification at `n=6`;
- the factorization (3.3) and the cross-multiplied first integral (3.4);
- the `(5,6)` depression invariant and exact `-5lambda` target shift;
- all rows (5.1), all five substitutions (5.2), and their exact vanishing;
- `E3=dI_3`, `E2=dI_2`, every coefficient of `omega,eta`, the nonzero
  exterior component (7.6), and the rank control (7.5).
- the rational Pfaffian trajectory (8.3) and its exact failure of the second
  polynomial boundary condition.

Exact tame controls exercise every divisible sextic shear:

```text
J(x+y,   y+(x+y)^6)=1,
J(x+y^2, y+(x+y^2)^3)=1,
J(x+y^3, y+(x+y^3)^2)=1.
```

The exact rejection

```text
J(x+y^5,y+y^6)=1+6y^5
```

shows that a superficial `(5,6)` shape is not enough.

Expected top-level output is

```text
verdict = SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE
full_sextic_theorem_proved = false
enumeration_run = false
lift_found = false
jc2_inference = false
```

No finite formal support in the replay is used as a search cap.

## 10. Campaign consequence and next gate

The confirmed quartic conclusion remains unchanged: an exact AS109 lift must
have correction `y`-degree at least five in one coordinate.  This preflight
does **not** raise that floor to seven, because neither the provisional
quintic family nor the two sextic patterns is fully closed here.

Conditional on later promotion of all quintic work, the sextic frontier is
now exactly:

- the `(4,6)` split (3.4), with common quadratic-generator and constant
  mismatch branches;
- the `(5,6)` Pfaffian foliation (7.4), with the pole/integrability gap in
  Section 8.

The fastest next exact attack is a weighted-projective pole analysis of
(7.4) together with (8.1), in parallel with a lower-row compiler for the two
`(4,6)` branches.  Neither should block on review of the provisional
quintic argument.

No result in this file proves or disproves JC2, constructs a lift, or infers
anything from finite-field or finite-Witt data.

## 11. Provenance hashes

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | present exact replay before report freeze |
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | confirmed theorem consumed |
| `xmodel/as109-quartic-review-grok-20260824.md` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | different-model review, `CONFIRMED` |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | AS109 context only; no new Hensel inference |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | AS109 context only |

No parent, review, canonical file, ledger, or AWS resource was edited.
