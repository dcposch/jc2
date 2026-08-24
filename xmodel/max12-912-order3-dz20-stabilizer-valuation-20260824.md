# `(9,12)` order-three DZ20 stabilizer/valuation exclusion

Date: `2026-08-24`  
Status: **PRODUCER-EXACT / HOSTILE DIFFERENT-MODEL REVIEW REQUIRED**  
Verdict: the coprime spectral fibre with nontrivial order-three Kummer class
and `k=mu=nu=0` has no rational trajectory. The common-factor/noncoprime
spectral stratum is explicitly not consumed.

## 1. Exact scope and predecessors

Let `K=C(x)` and let `L=K(u)`, where `u^3=h`, the class of `h` has exact order
three in `K^*/K^{*3}`, and `sigma(u)=zeta*u`. The reviewed maximum-twelve
preflight supplies:

- the primitive `(9,12)` leading powers and history residue `3|deg h`;
- `delta=0` on the nontrivial order-three branch;
- the covariant depressed coordinate `z=uy+A/9` and both retained Taylor
  boundary families.

The different-model-confirmed Faber theorem supplies monic depressed cores
`f,g` of degrees `9,12`, the character-compatible order-three lower system

```text
r1=r2=r4=r5=r7=0,  r3=mu,  r6=nu,
r8=u^2*R,           9*h*R'+6*h'*R=j != 0.
```

This report treats only `k=mu=nu=0` and the spectral branch on which `f,g`
are coprime and

```text
deg_z(g^3-f^4)=16.                                      (1.1)
```

The exact spectral identity and degree `16` are reproduced by
`cases/max12_912_order3_fibre_20260824/order3_fibre.py`. They remain a named
producer input until separately reviewed. Nothing below discards or weakens
the original Taylor boundaries; rather, the contradiction occurs before they
are needed.

Not covered: a common-factor/noncoprime spectral stratum; nonzero `k`, `mu`,
or `nu`; the order-one polynomial core; the `(8,12)` cell; maximum-twelve
coverage; or JC2.

## 2. The exact passport

Put

```text
W=g^3-f^4,              beta=g^3/f^4,
B=3*g_z*f-4*g*f_z.
```

The Keller equation makes `f,g` coprime on the named spectral branch, and
`W` is nonzero by (1.1). Direct differentiation gives

```text
beta_z=g^2*B/f^5.                                      (2.1)
```

At infinity, `beta-1=W/f^4` has order `20`. Hence its derivative has order
`21`. Comparing degrees in (2.1) gives `deg_z B=0`; since `W` is nonzero,
`B` is a nonzero element of `L`.

Equation (2.1) now proves, without a genericity assumption, that every zero
of `g` and every zero of `f` is simple. At a finite root of `W`, neither
`f` nor `g` vanishes and `beta_z` is nonzero, so all sixteen finite points
over `1` are unramified. Infinity is the unique point of index `20` over
`1`. Thus `beta` is a degree-`36` Belyi map with exact passport

```text
0:         3^12,
infinity:  4^9,
1:         (20,1^16).                                  (2.2)
```

The ramification check is sharp:

```text
12*(3-1)+9*(4-1)+(20-1)=24+27+19=70=2*36-2.
```

In particular there are no unrecorded branch values.

## 3. Stabilizer-aware isotrivial descent

There are finitely many complex Belyi maps with passport (2.2), up to source
Mobius transformation. The factorization of the zero and pole divisors of
`beta` recovers the monic pair `(f,g)`, so the normalized equality pairs also
form finitely many source-affine orbits.

Fix one constant representative `(F,G)` with both coordinates monic and
depressed. The unique index-20 point fixes source infinity. Depression removes
translation, so every pair in this orbit is

```text
f(z)=lambda^-9*F(lambda*z),
g(z)=lambda^-12*G(lambda*z).                            (3.1)
```

Let `D` be the source stabilizer of this pair. It fixes infinity and preserves
the depressed zero/pole divisors, so it is a finite cyclic scaling group
`mu_e`. A deck group acts freely on a generic fibre, hence `e|36`. The local
expansion `beta-1=c*z^-20+...` also gives `e|20`. Therefore

```text
e | gcd(36,20)=4,              e in {1,2,4}.             (3.2)
```

The quotient parameter

```text
eta=lambda^e                                                   (3.3)
```

belongs to `L`. This can be seen without a coarse-moduli assumption. If
`F_i,G_j` are the nonleading coefficients, then the coefficients of (3.1)
are constant multiples of `lambda^{-(9-i)}` and
`lambda^{-(12-j)}`. The gcd of all nonzero exponent differences is exactly
the stabilizer order `e`; a Bezout combination of those coefficients recovers
`lambda^e` in `L`.

The depressed Kummer coordinate has the covariance

```text
sigma(f)(z)=f(zeta^-1*z),       sigma(g)(z)=g(zeta^-1*z).
```

Comparing (3.1) before and after `sigma`, modulo the stabilizer, gives

```text
sigma(eta)=zeta^(-e)*eta.                              (3.4)
```

Choose `a in {1,2}` with `a=-e mod 3`. Since the eigenspaces of the cyclic
Kummer extension are `K,uK,u^2K`, (3.4) gives

```text
eta=u^a*v,                    v in K^*.                 (3.5)
```

The coefficient of `z^16` in `W` is a nonzero constant multiple of
`lambda^-20`. It is also a nonzero constant multiple of `r8`. Put

```text
N=20/e.
```

Then for a constant `C in C^*`,

```text
r8=C*eta^-N.
```

Combining this with `r8=u^2*R` and `u^3=h` gives the complete stabilizer
table

| `e` | `N=20/e` | `a=-e mod 3` | `S=(aN+2)/3` | exact descent |
|---:|---:|---:|---:|---|
| 1 | 20 | 2 | 14 | `R=C*h^-14*v^-20` |
| 2 | 10 | 1 | 4 | `R=C*h^-4*v^-10` |
| 4 | 5 | 2 | 4 | `R=C*h^-4*v^-5` |

Uniformly,

```text
R=C*h^-S*v^-N.                                        (3.6)
```

This is the stabilizer correction missing from the naive assertion
`R=C*h^6*a^20`: all three possible twists are retained.

## 4. Finite-zero balances

Let `p` be a finite zero of the polynomial `h`, let

```text
m=ord_p(h)>0,             r=ord_p(R),
n=ord_p(v).
```

If the first terms of the terminal ODE do not cancel, its left side has order
`m+r-1` and leading coefficient proportional to `9r+6m`. Since its right side
is the nonzero constant `j`,

```text
r=1-m.                                                   (4.1)
```

Using (3.6), `r=-S*m-N*n`, so

```text
N*n=-(S-1)*m-1.                                         (4.2)
```

For the three stabilizers, integrality of `n` gives respectively

```text
13m+1=0 mod 20,
 3m+1=0 mod 10,
 3m+1=0 mod 5.
```

Each has the unique solution

```text
m=3 mod N.                                              (4.3)
```

The apparent smallest solution `m=3` is not a solution of the ODE: substituting
`r=1-m=-2` makes `9r+6m=0`. After this cancellation, the next possible order
is at least `m+r=1`, so it cannot equal `j`.

The only other local possibility is cancellation from the outset,
`9r+6m=0`, hence `r=-2m/3`. This requires `3|m`; after cancellation the next
possible order is at least

```text
m+r=m/3>0,
```

again impossible. Therefore every finite zero uses the noncancelled balance
and satisfies

```text
m>3.                                                     (4.4)
```

More sharply, the first possible multiplicities are `23,13,8` for
`e=1,2,4`.

## 5. No hidden divisor of `v`

Let `p` be a finite point with `h(p)!=0`. If `n=ord_p(v)` is nonzero, then by
(3.6)

```text
r=ord_p(R)=-N*n.
```

The term `9hR'` has strictly smaller order than `6h'R`, namely `r-1`, and
cannot cancel. Equality to a nonzero constant would force `r=1`. But
`r` is a multiple of `N in {20,10,5}`, a contradiction. Hence `v`, and
therefore `R`, has no finite zero or pole away from the finite zeros of `h`.

Write

```text
D=deg h,             s=# distinct finite zeros of h.
```

Summing (4.1) over the zeros gives

```text
sum_(finite p) ord_p(R)=s-D,
ord_infinity(R)=D-s.                                    (5.1)
```

## 6. Infinity closes the trajectory

At infinity, write the leading behaviours

```text
h ~ c*x^D,                R ~ d*x^(s-D).
```

The top degree on the left of the terminal ODE is `s-1`, with coefficient

```text
9*(s-D)+6*D = 3*(3s-D).                                (6.1)
```

By (4.4), every finite multiplicity is strictly greater than three, so

```text
D>3s.
```

Thus (6.1) is nonzero. Equality to the degree-zero constant `j` forces
`s=1`. The reviewed history residue says `3|D`. Since the constant field is
`C`, a single-root polynomial of degree divisible by three is a cube:

```text
h=c*(x-b)^D in K^{*3},
```

contradicting the assumption that the Kummer class has order three.

Therefore no trajectory exists in the exact scope of Section 1.

## 7. Positive-control reconciliation

The terminal ODE alone remains noncontradictory. For

```text
h=x^2*(x-1)^4,          R=C/(x*(x-1)^3),
```

direct logarithmic differentiation gives

```text
9*h*R'+6*h'*R=-3C.
```

This control is rejected only after the DZ/stabilizer descent. Its local
differences `ord R-6 ord h` are `-13,-27,40` at `0,1,infinity`; in particular
it fails the trivial-stabilizer modulus at the two finite zeros. More
intrinsically, its finite multiplicities `2,4` violate the exact congruences
in (4.3) for every possible stabilizer. The report therefore does not revive
the earlier false terminal-valuation inference.

## 8. Portable replay and conclusion

Run:

```sh
python3 cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.py
```

The pure-stdlib case checks the stabilizer table, all three congruences, the
`m=3` cancellation, the general cancelled balance, the regular-point divisor
argument, the infinity coefficient, and the terminal positive control.

**Producer conclusion.** Conditional on the named spectral input (1.1), the
coprime `k=mu=nu=0` order-three lower fibre has no rational trajectory. The
argument is independent of Taylor enumeration and is stabilizer-aware.

**Do not promote to:** the common-factor/noncoprime spectral stratum, any
nonzero invariant-load fibre, the order-one polynomial core, emptiness of
`(9,12)`, maximum-twelve automorphy, a counterexample, or JC2. Hostile
different-model review is required before this producer conclusion is used as
a theorem input.
