# Map-only AS `p=3,D=7`: an exact depth-six triangular survivor terminal at depth seven

**Producer verdict: THE MAP-ONLY CAP-SEVEN SYSTEM IS NONEMPTY MODULO
`3^6`.  THE DISPLAYED TRIANGULAR RESIDUE HAS NO CAP-SEVEN LIFT MODULO
`3^7`.  THIS DOES NOT CLASSIFY THE FULL CAP-SEVEN LOCUS.**

- Date: 2026-08-24
- Arithmetic: exact integers, reduced modulo `3^6=729` and `3^7=2187`
- Engines: dependency-free Python and independent Singular
- Discovery method: accepted-digit affine recursion; no SAT/SMT verdict is
  used
- Hostile different-model review: not yet run

## 1. The exact map-only point

In `(Z/729Z)[x,y]`, take

```text
P = x + 2x^3 + 441x^5 + 108x^7,
Q = y - 6x^2y + 18x^4y - 27x^6y.
```

Both total degrees are seven and

```text
(P,Q) mod 3 = (x-x^3,y).
```

Coefficientwise reduction of the first derivative modulo 729 gives the
useful representative

```text
P_x = 1 + 6x^2 + 18x^4 + 27x^6              (mod 729),
Q_y = 1 - 6x^2 + 18x^4 - 27x^6.
```

The product of these two displayed representatives is the exact integer
identity

```text
(1+6x^2+18x^4+27x^6)Q_y = 1-729x^12.
```

The literal integer derivative of `441x^5+108x^7` has coefficients 2205
and 756, so the preceding compact product must not be mistaken for a
literal integer determinant.  It does prove

```text
det J(P,Q) = 1                                (mod 729).       (1)
```

For the one-step obstruction, choose the congruent coefficient
`108+2*729=1566` for `x^7` modulo 2187.  With

```text
P_tilde=x+2x^3+441x^5+1566x^7,
```

one has `P_tilde_x=1+6x^2+18x^4+27x^6 mod 2187`, and hence

```text
det J(P_tilde,Q) = 1-729x^12                  (mod 2187).      (2)
```

This is a genuine point of the map-only bounded-degree lift system.  No cap
is imposed on a canonical `(A,B)` gauge.

## 2. Source-honest triangular derivation

For the triangular component write

```text
P_x = 1+3a(x),
Q   = yT(x)+S(x),
deg P <= 7,  deg T <= 6.
```

The target shear `S(x)` is determinant-invisible, so set it to zero.  The AS
special fibre and the fact that `a=U'-x^2` for
`P=x-x^3+3U` give precisely

```text
[x^2]a = -1 mod 3,
[x^5]a =  0 mod 3.                            (2)
```

Conversely these are the only derivative-provenance restrictions on `a`
modulo 243: all other coefficients lift through `U'`, and the two displayed
conditions are exactly the exponents whose derivative multipliers are
divisible by three.

Eliminate `T` without a denominator:

```text
T = (1+3a)^(-1)
  = 1-3a+9a^2-27a^3+81a^4-243a^5             (mod 729).
```

Since `deg a<=6`, the cap condition `deg T<=6` is equivalent to vanishing,
in every degree greater than six, of

```text
H(a)=a^2-3a^3+9a^4-27a^5                     (mod 81).        (3)
```

The accepted-digit recursion starts with `a_0 mod 3`.  Equation (3) modulo
three says `deg(a_0^2)<=6`; because `F_3[x]` is a domain, `deg a_0<=3`.
Together with (2), this leaves exactly

```text
a_0=c0+c1*x-x^2+c3*x^3,   (c0,c1,c3) in F_3^3,
```

only 27 base components.

If an accepted partial coefficient is changed by a new digit

```text
a -> a+3^r*delta,
```

then the next high obstruction is affine:

```text
H(a+3^r*delta)/3^r
  = H(a)/3^r + 2*a_0*delta                    (mod 3).         (4)
```

Thus each component uses one fixed Gaussian matrix, the high-coefficient
map `delta -> high(2a_0 delta)`.  The deterministic replay retains its full
kernel; it does not quotient Hamiltonian, Frobenius, or cap-boundary modes.

The first canonical surviving path found by this recursion is

```text
a = 2x^2+6x^4+9x^6                           (mod 81).        (5)
```

The deterministic compiler begins with 27 base points, retains 3,645 first
digit points, and retains 531,441 second digit points after 1,458 affine
inconsistencies.  At the terminal digit the first survivor occurs after 486
inconsistent inputs.  The enumeration trace SHA-256 printed by the replay is
`1d7ab40f50bfa01e7189e4022742984c12b8fba151bae83f8e332dbc0cdbf35e`.
These counts certify the route to the displayed point; the compiler stops at
that point and does not claim exhaustive enumeration of terminal survivors.

It satisfies (2)--(3), and substitution in the finite inverse gives

```text
T = 1-6x^2+18x^4-27x^6                       (mod 729).
```

Integrating `P_x=1+3a` modulo 729 gives the displayed `P`.  The coefficient
checks use only inverses of 5 and 7 modulo 729; the `x^3` coefficient is the
licensed derivative-multiplier stratum, not a division by three.

## 3. Exact terminal obstruction at depth seven

Using the representative `P_tilde,Q` from (2), every cap-seven lift of this
depth-six residue has the form

```text
P_new=P_tilde+729U,
Q_new=Q+729V,
deg U,deg V <= 7.
```

The special-fibre derivative matrix is the identity.  Therefore

```text
(det J(P_new,Q_new)-1)/729
  = -x^12 + U_x+V_y                         (mod 3).          (6)
```

The divergence of a pair of total degree at most seven has total degree at
most six.  It has no `x^12` coefficient.  Equation (6) is consequently
inconsistent for every cap-seven next digit.  The point (1) is terminal
modulo `3^7`.

This obstruction is both a cap-boundary class and representative-invariant:
changing the depth-six integer representative by multiples of 729 changes
the residual only by the divergence in (6).

## 4. Interpretation and refusal scope

This result proves

```text
FONLY_(3,6)(D=7) is nonempty,
```

and kills one explicit residue in the fibre of the reduction map to depth
six.  It does **not** prove

```text
FONLY_(3,7)(D=7) is empty.
```

Another depth-six residue may have zero Cartier/cap-boundary class.  The
full componentwise accepted-digit compiler must therefore continue through
all 27 base components and all surviving affine carry strata.

The point is not:

- a simultaneous `(A,B)` gauge-cap statement;
- an all-depth compatible tower;
- a polynomial/Tate characteristic-zero lift;
- a counterexample, no-lift theorem, or evidence for/against JC2.

It does not falsify the characteristic-zero expectation that `D=7` is a
negative control.  It falsifies only the stronger finite claim that depth
six would already certify emptiness.  The first possible finite emptiness
certificate has moved to depth seven or later.

## 5. Replays

From the case directory:

```sh
python3 compile_triangular_first_survivor.py
python3 replay_triangular_terminal.py
python3 replay_accepted_digit_trace.py
Singular -q audit_triangular_terminal.sing
shasum -a 256 -c MANIFEST.sha256
```

The compiler enumerates all 27 base components, uses deterministic RREF and
the complete affine nullspace at the first two carry digits, and stops at the
first exact terminal-digit survivor.  It is an existence search, not an
exhaustion of all survivors.  The first replay expands the complete maps,
checks the literal determinant
of the depth-six representative separately, and verifies the clean lifted
representative congruence (2).  The
second independently checks the source derivative conditions, all four
accepted digits in (3)--(5), and the denominator-free inverse.  Singular
checks the exact determinant identity and the special fibre in a separate
CAS.
