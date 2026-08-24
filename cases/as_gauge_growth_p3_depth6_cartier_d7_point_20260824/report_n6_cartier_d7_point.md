# Depth-six Cartier gate for the frozen cap-seven point

**Producer verdict: THE FROZEN DEPTH-FIVE MINIMUM-CAP POINT IS TERMINAL
MODULO `3^6`, AT EVERY CAP.  THIS DOES NOT EMPTY THE DEPTH-SIX SYSTEM.**

- Date: 2026-08-24
- Source point: `B_(3,5)(7,7)` witness frozen separately
- Arithmetic: exact integers modulo 729, followed by the first residue
  modulo 3
- Engines: integer-only Python and independent Singular
- Different-model hostile review: not yet run

## 1. Exact first unfulfilled determinant digit

Use exactly the integer representatives `A,B` in the frozen depth-five
minimum-seven package.  They satisfy

```text
det J(A,B)=1 mod 243.
```

Define

```text
R = (det J(A,B)-1)/243 mod 3.
```

Exact expansion gives

```text
R = x^10+x^8+x^7y+x^7-x^6y^3-x^6y+x^5y-x^3y
      +x^2y^3-x^2y^2+xy^3+xy^2+xy-x-y^3+y^2+y+1.
```

In particular

```text
[x^2y^2]R = -1 != 0 in F_3.                            (1)
```

## 2. Cartier-cokernel obstruction

Every possible next gauge digit has the form

```text
A_new=A+243U,
B_new=B+243V.
```

Because `A=x mod 3` and `B=y mod 3`, differentiation gives

```text
(det J(A_new,B_new)-1)/243
   = R + U_x + V_y mod 3.                              (2)
```

The coefficient of `x^2y^2` in `U_x` would come from `x^3y^2` and is
multiplied by `3=0`.  The same coefficient in `V_y` would come from
`x^2y^3` and is again multiplied by three.  Thus `x^2y^2` is a Cartier
cokernel monomial for the divergence map in characteristic three.  Equation
(1) cannot be changed by any `U,V`, of any degree.  Hence this frozen point
has no symplectic gauge lift modulo 729 at any cap.

## 3. Representative invariance

Changing the chosen depth-five integer representatives by multiples of 243
is exactly the substitution in (2).  Therefore the class of `R` modulo
`im(partial_x)+im(partial_y)` and, specifically, coefficient (1), is
independent of the representatives.  The terminality statement belongs to
the residue class modulo 243, not to a serialization accident.

## 4. Scope and next discriminator

This kills one explicit point of `B_(3,5)(7,7)`.  It does **not** show

```text
B_(3,6)(7,7)=empty,
```

because another depth-five cap-seven residue class may have zero Cartier
class and satisfy the depth-six support rows.  The next exact search should
therefore intersect the full depth-five cap-seven solution scheme with:

1. vanishing of every Cartier row of `(det J-1)/243 mod 3`;
2. the cap-seven image of the next divergence digit; and then
3. the depth-six `P,Q` support rows.

If that intersection is empty, repeat at caps eight, nine, and ten.  Do not
spend further work trying to repair this frozen residue.

No compatible tower, polynomial/Tate lift, no-lift theorem, `A_infinity`,
or Jacobian-conjecture conclusion is made.

## 5. Replay

```sh
python3 replay_n6_cartier_d7_point.py
Singular -q audit_n6_cartier_d7_point.sing
shasum -a 256 -c MANIFEST_n6_cartier_d7_point.sha256
```

The Python replay reconstructs the entire source point and both depth-five
determinants before computing `R`.  Singular independently verifies the
identity `det J(A,B)-1=243R mod 729`.
