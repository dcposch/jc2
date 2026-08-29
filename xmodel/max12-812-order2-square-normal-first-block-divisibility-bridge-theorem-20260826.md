# Order-two square-normal first-block divisibility bridge

Date: 2026-08-26

Status: **PROVISIONAL ELEMENTARY THEOREM; DIFFERENT-MODEL HOSTILE REVIEW
REQUIRED BEFORE PROMOTION OR SOURCE-FAN USE.**

## 1. Algebraic statement

Let `k` be a field and let

```text
Q=z^4+q2*z^2+q1*z+q0,
N=n3*z^3+n2*z^2+n1*z+n0.
```

Write the Euclidean division

```text
N^2=AQ+R,                 R=r3*z^3+r2*z^2+r1*z+r0,
```

and expand at infinity

```text
N^2/Q=A+sum_{j>=1} h_j*z^(-j).
```

Then

```text
h1=r3,
h2=r2,
h3=r1-q2*r3,
h4=r0-q2*r2-q1*r3.                              (1.1)
```

Consequently the following are equivalent:

```text
h1=h2=h3=h4=0;
h1=...=h7=0;
Q divides N^2 in k[z].                            (1.2)
```

If `Phi1,...,Phi7` are any ordinary-Faber rows obtained from
`h1,...,h7` by the reviewed lower-unitriangular Laurent-to-ordinary
connection, their simultaneous vanishing is equivalent to (1.2) as well.
Only the unitriangular diagonal-one property is used here.

## 2. Proof

For the coefficients needed below,

```text
1/Q=z^(-4)*(1-q2*z^(-2)-q1*z^(-3)+O(z^(-4))),
```

multiplication by `R` gives (1.1).  The map

```text
(r3,r2,r1,r0) -> (h1,h2,h3,h4)
```

is triangular with diagonal one.  Thus its first four outputs vanish if
and only if `R=0`, which is exactly `Q|N^2`.  If `R=0`, every negative
coefficient vanishes.  This proves (1.2).  A lower-unitriangular connection
with diagonal one preserves vanishing of every initial block, proving the
ordinary-row assertion.

Four rows are sharp: taking `R=1` gives `h1=h2=h3=0` and `h4=1`.

## 3. Exact factor-type classifier

Factor in the UFD `k[z]`

```text
Q=product_f f^(e_f),
Q_half=product_f f^(ceil(e_f/2)).
```

Unique factorization gives

```text
Q|N^2  iff  Q_half|N.                             (3.1)
```

In particular:

1. If `Q` is squarefree, `deg(Q_half)=4>deg(N)`, so `N=0`.
2. If

   ```text
   Q=A^2*D,
   deg(A)=1, deg(D)=2, gcd(A,D)=1, D squarefree,
   ```

   then `Q_half=A*D` has degree three, so

   ```text
   Q|N^2  iff  N=M*A*D                            (3.2)
   ```

   for a unique scalar `M in k`.
3. If the factor type is more degenerate, (3.1) gives a larger kernel and
   must be routed separately.  Examples include two double factors
   (`Q_half` has degree two), a triple plus a simple factor (`Q_half` has
   degree three), and a quadruple factor (`Q_half` has degree two).

The hypotheses `gcd(A,D)=1` and squarefreeness of `D` are essential.  For
example, if `D=B^2`, then `Q=A^2*B^2` only requires `A*B|N`, not
`A*D|N`.

## 4. Repeated-`A` incidence chart

On the depressed repeated-root incidence write

```text
A=z-a,
D=A^2+4*a*A+E,
Q=A^2*D,
N=M*A*D.                                           (4.1)
```

The conditions

```text
E != 0,                  (4*a)^2-4*E != 0
```

make `A` coprime to `D` and `D` squarefree.  Thus (3.2) identifies exactly
the nonzero first square-normal kernel on this factor-type incidence open.
The coefficient expansion of (4.1) is the central specialization of the
exact affine-Faber coordinates used in the promoted delayed-`A` theorem.
This statement is on the incidence chart; it does not assert that the root
coordinate `a` is a globally regular function of quartic coefficients.

## 5. Literal square-normal consequence

In characteristic zero, for a source expansion

```text
C=Q^2+epsilon^d*N+higher,
```

the first unloaded quadratic Laurent term is

```text
(3/8)*epsilon^(2d)*N^2/Q.                          (5.1)
```

At a grade where no load, target, or lower correction ties (5.1), vanishing
of the complete first four—and hence first seven—ordinary source rows is
equivalent to `Q|N^2`.  Therefore the first square-normal block has the
finite routing:

```text
squarefree Q                 -> zero normal direction;
Q=A^2 D, D squarefree        -> N=M A D repeated-A kernel;
more degenerate Q            -> separate collision/Pell/p=0/D=0 receiver.
```

At tied grades the statement remains the algebraic description of the
unloaded summand, but forcing must be retained and predecessor reduction is
mandatory.  Successive corrections and the literal two-sided total-Rees
overlap are not proved by this first-block lemma.

## 6. Controls and firewall

- Squarefree control: `Q=z^4-1`, `N=z^3` gives nonzero remainder and a
  nonzero first block.
- Repeated-`A` control: `Q=z^2*(z^2+p)`, `N=z*(z^2+p)` satisfies
  `Q|N^2` identically.
- Four-row sharpness: remainder `R=1` evades the first three coefficients
  but not the fourth.
- Degenerate-factor control: `Q=A^2*B^2`, `N=A*B` shows why squarefree `D`
  cannot be omitted from (3.2).

This theorem is a first-block divisibility and routing bridge only.  It does
not prove higher-jet absorption, a relative Newton cone, a Rees kernel or
torsion statement, a literal source/affine-Faber overlap, total fan coverage,
order two, `(8,12)`, maximum twelve, or JC2.
