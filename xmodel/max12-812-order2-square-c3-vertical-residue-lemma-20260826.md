# `(8,12)` order-two square fan: vertical `c=3` residue lemma

Date: 2026-08-26

Status: **HAND TWO-GRADE DIVISIBILITY ELIMINATION, CONDITIONAL ON COMPLETE
SOURCE/FABER TIMING AND NONZERO-COEFFICIENT REPLAY.  NO BRANCH VERDICT.**

## Scope

Work on the generic unit-load chart `D(p*k0)`, after the reviewed c1/c2
contact gates.  Normalize a finite leading `A` contact to `a=0`; the only
vertical case not already contained in the reviewed high-contact theorem is

```text
c=3,  r>=2.
```

Indeed the reviewed theorem covers `c>=4,r>=2`, while the registered r=1
separator is a separate predecessor.  This note uses only the pole types and
weights in the frozen horizontal design.  Every conclusion below remains
conditional until the complete source rows verify the timing, coefficients,
and connection bounds.

## Exact two-grade rational coefficients

The frozen universal Laurent receiver makes the pole comparison explicit.
Write

```text
L(sigma)=L+sigma*ell1+sigma^2*ell2+...,
A(sigma)=A0+sigma*A1+sigma^2*A2+...,
C(sigma)=sigma^3*E3+sigma^4*E4+sigma^5*E5+... .
```

For `r=2`, write

```text
R(sigma)=sigma^2*B2+sigma^3*B3+...;
```

for `r>=3` put `B2=0` (and let `B3` denote the possible grade-three
coefficient).  If `H_d` is the rational Laurent coefficient at absolute
grade `d`, direct expansion of the frozen receiver gives

```text
H13 = (3/4)*A0*E3/L,

H14 = (3/4)*((A1*E3+A0*E4)/L-ell1*A0*E3/L^2)
      -(3/8)*B2*A0^2/L^2
      +(5/32)*k0*A0^2/L,

H15 = (3/4)*(
          (A2*E3+A1*E4+A0*E5)/L
         -ell1*(A1*E3+A0*E4)/L^2
         +(ell1^2/L^3-ell2/L^2)*A0*E3)
      -(3/8)*(
          (B3*A0^2+2*B2*A0*A1)/L^2
         -2*ell1*B2*A0^2/L^3)
      -(1/16)*A0^3/L^3
      +(5/32)*(
          (k1*A0^2+2*k0*A0*A1)/L
         -k0*ell1*A0^2/L^2).
```

The registered `kR3`, `kRC`, and `kR2A` terms first occur after grade
fifteen on this cell.  These displays are algebraic consequences of the
frozen common numerator, not a claim that the source rows equal them: the
source-to-Laurent/Faber bridge must still be replayed exactly.

## Clean divisibility proof

Once the exact bridge is licensed, no radical or broad coefficient ideal is
needed.  Polynomiality of `H13` says

```text
L | A0*E3.
```

Both factors on the right are nonzero linear polynomials and `L` is a
squarefree quadratic on `D(p)`.  Hence, over the etale splitting algebra and
up to the deck swap,

```text
L=u*v,  A0=alpha*u,  E3=gamma*v,  alpha*gamma!=0.   (D1)
```

Let `N14=L^2*H14`.  Reducing the displayed formula for `H14` modulo `L`
and using `L|A0*E3` gives

```text
N14 = -(3/8)*B2*A0^2                 (mod L).       (D2)
```

Polynomiality of `H14` requires `L^2|N14`, hence in particular
`L|B2*A0^2`.  At the complementary root `v=0`, `A0` is a unit, so

```text
v | B2.                                             (D3)
```

For `r>=3` this is automatic because `B2=0`; for `r=2` it is exactly the
new constraint supplied by grade fourteen.

Now let `N15=L^3*H15`.  Reduce its displayed expression modulo `v`.
Every summand except the cubic contains at least one of `L`, `A0*E3`, or
`B2`; equations (D1) and (D3) therefore kill all of them.  Thus

```text
N15 = -(1/16)*A0^3                   (mod v).       (D4)
```

The right side is nonzero because `A0=alpha*u` and `u` is a unit at `v`.
But polynomiality of `H15` would require `L^3|N15`, in particular
`v|N15`.  This contradiction eliminates both `r=2` and `r>=3` at once.
The argument descends from the etale splitting algebra because the original
polynomiality conditions and the contradiction are preserved by faithfully
flat base change.

## First root allocation

The unique relative grade-three term is `AC/L`.  Over the etale root algebra
write `L=u*v`.  Vanishing with nonzero linear `A,C` forces, up to the deck
swap,

```text
A=A_u*u,  C=C_v*v,  A_u*C_v!=0.                    (1)
```

The exact displays above show that the first connection correction to this
polynomial quotient has at most a simple pole and the second has at most a
double pole.  Equivalently, before denominator motion its numerator contains
one factor `L`, so the `j`-th connection term has pole order at most `j`.

## Local pole interpretation for `r>=3`

At relative grade four, the loaded `kA2=k0*A0^2/L` term and first `AC`
corrections have at most a simple pole.  At relative grade five,

```text
A3=A^3/L^3=A_u^3/v^3                              (2)
```

has a triple pole at the `C`-root `v=0`.  The competing terms at that grade
have pole order at most two there:

- the second connection corrections to `AC/L` have order at most two;
- first corrections to `A2` have order at most two;
- `RA2` first appears only when `r=3`, and `R*A^2/L^2=R/v^2` has order at
  most two.

No other registered lower-hull term reaches this grade.  Hence the triple
coefficient in (2) is unmatched and forces `A_u=0`, contradicting (1).

## Local pole interpretation at `r=2`

Here `RA2` joins `A2` at relative grade four.  At `v=0`, the exact
grade-fourteen coefficient has order-two principal part

```text
-(3/8)*A_u^2*B2(v=0)/v^2.
```

All its other terms have at most a simple pole.  Polynomiality therefore
forces `B2(v=0)=0`; since `B2` is linear, it shares the factor `v`.  In the
short notation `R=B2`, this is the statement suggested by

```text
RA2=R*A^2/L^2=R/v^2.                               (3)
```

After that constraint, (3) has only a simple pole.  Its first correction at
relative grade five has order at most two: differentiating `L^-2` once can
remove at most one further factor of `v`, and a correction to `R` can remove
the one base factor but still leaves only `v^-2`.  The second `AC` connection
and first `A2` connection also have order at most two.  The triple pole (2)
is therefore again unmatched and gives the same contradiction.

The deck-conjugate orientation exchanges `u,v` and has the identical proof.

## Exact client acceptance test

A thin dual-field source client should fail closed unless it verifies:

1. the complete seven source rows and lower-unitriangular Laurent/Faber bridge
   through absolute grades thirteen, fourteen, and fifteen;
2. the grade-thirteen `AC/L` root-allocation equation with both orientations;
3. the common-denominator reductions (D2) and (D4), including every displayed
   correction term and the nonzero coefficient `-1/16`;
4. for `r=2`, grade fourteen forces (D3), while for `r>=3` the symbolic
   specialization `B2=0` reaches the same grade-fifteen contradiction;
5. symbolic translation in `r>=3`, rather than sampling finitely many `r`;
6. moving `p,k0` and every correction that can reach these grades, plus a
   wrong-grade or omitted-connection negative control;
7. exact `Q` as the characteristic-zero endpoint and one good-prime software
   control.

No radical or twelve-coefficient global membership is needed if these local
principal-part identities and the etale/deck overlap are certified exactly.

## Firewall

This conditional lemma addresses only the vertical `a=0,c=3,r>=2` source
faces on `D(p*k0)`.  It does not prove the r=1 predecessor, horizontal
finite-`a` fan, `p=0`, `k0=0`, ramified slopes, exact-square zero section,
terminal/Taylor receivers, fan exhaustiveness, order two, maximum twelve, or
JC2.
