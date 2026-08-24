# AS109 wild-symplectic conductor — completed-bidisc first gate

Date: 2026-08-24T12:27:19Z  
Basis commit: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **FROZEN PRODUCER / HOSTILE REVIEW REQUIRED**  
Verdict: **`GAUGE-TRIVIAL/CONTROL-ONLY` AT THE REGISTERED FIRST GATE**

## 0. Verdict

Conditionally assume, for an odd prime `p`, an exact polynomial lift

```text
F=(P,Q) in Z_p[x,y]^2,
F mod p=(x-x^p,y),                  det J(F)=1.
```

The finite-analytic assertion in the ideation card is correct.  On the
closed unit bidisc, `F` is finite etale of rank `p`; the special
Artin--Schreier translations lift uniquely to a free, determinant-one
restricted-analytic `C_p` action.  This is an action on the completed unit
bidisc only.  It does **not** descend to a rational or polynomial deck action,
does not remove `A_infinity`, and does not imply that the global generic degree
is `p`.

There is also an important category correction.  Any two determinant-one
restricted-analytic lifts with this special fibre are right-equivalent by a
unique near-identity restricted-analytic symplectomorphism.  Their deck
actions are conjugate.  Thus unrestricted completed cohomology has one orbit;
support becomes a possible obstruction only after the allowed gauges are
given a uniform polynomial support/degree bound, or after an algebraic
boundary conductor is defined.  A finite-level cohomology quotient without
that extra bound cannot supply such an invariant.

At the first Witt digit, the proposed equations are correct.  The full
registered coefficient rectangle has one affine orbit under the
divergence-free gauge for both `p=3` and `p=5`.  It nevertheless has a common
support floor: every solution contains `x^(p-1)y` in `Q1` with coefficient
one.  The rational cotangent control realizes exactly that floor and passes
through depths `2,3,4`.  No genuinely mixed gauge class appears at this gate.

This is a scoped analytic/control theorem, not a proof that all exact lifts
have unbounded polynomial support.  No proof or counterexample to JC2 follows.

## 1. Finite free rank `p` on the unit bidisc

Put

```text
B=Z_p<U,V>,       A=Z_p<x,y>,       U |-> P, V |-> Q,
```

where angle brackets denote restricted power series.  Reduction modulo `p`
gives

```text
A/pA = F_p[x,y]
     = F_p[U,V,X]/(X^p-X+U),        X |-> x, V |-> y.       (1.1)
```

Hence `A/pA` is free over `B/pB` on `1,x,...,x^(p-1)`.

The same elements form a basis before reduction.  For any `f in A`, reduce
modulo `p`, expand it in that special basis, lift the finitely many
coefficients to `B`, subtract, and divide the residual by `p`.  Iteration
gives convergent coefficient series in the `p`-adically complete ring `B`, so
the displayed elements span `A`.  If

```text
sum_(i=0)^(p-1) b_i x^i=0,
```

then special-fibre independence gives every `b_i in pB`.  Divide the relation
by `p` in the `p`-torsion-free ring `A` and repeat.  Since `B` is `p`-adically
separated, every `b_i` is zero.  Therefore

```text
A is finite free of rank p over B.                              (1.2)
```

This direct basis lift closes the potential topological-Nakayama/flatness
gap; flatness is not assumed.

In `Omega_(A/B)`, the equations `dP=dQ=0` and the unit matrix determinant
`det J(F)=1` force `dx=dy=0`.  Since `A` is finite free and finitely presented
over the noetherian ring `B`, it follows that `A/B` is finite etale.

## 2. Unique lifted `C_p` action and volume

The ring `B` is `p`-adically complete, so `(B,pB)` is a Henselian pair
([Stacks, Tag 0ALJ](https://stacks.math.columbia.edu/tag/0ALJ)).  The
finite-etale lifting equivalence
([Stacks, Tag 09ZL](https://stacks.math.columbia.edu/tag/09ZL)) is fully
faithful.  Consequently every special automorphism

```text
bar(tau)_a: (x,y) |-> (x+a,y),        a in F_p,
```

lifts uniquely to a `B`-automorphism `tau_a` of `A`.  Uniqueness lifts the
group law and gives `tau_1^p=1`.  The special torsor isomorphism

```text
A_bar tensor_(B_bar) A_bar  ->  product_(a in F_p) A_bar
```

lifts to an isomorphism of finite-etale `B`-algebras.  The action is therefore
a free constant-`C_p` torsor action on the completed bidisc, not merely a list
of automorphisms.

Since `F o tau_a=F`, the chain rule gives

```text
J(F)(tau_a) J(tau_a)=J(F),       det J(tau_a)=1.          (2.1)
```

Thus the action is volume preserving.

### Completion firewall

The coordinates of `tau_a` lie in `Z_p<x,y>` and need not lie in
`Z_p[x,y]` or `Q_p(x,y)`.  The construction sees only integral unit-disc
sheets.  It neither acts on the residual factor `A_infinity` of the global
formal generic algebra nor proves that the analytic action descends to
`Aut_(K(P,Q)) K(x,y)`.  This is fully compatible with the reviewed global
degree bound `d>=p` and with a nonzero `A_infinity`.

## 3. Completed right-equivalence is transitive

Let `F` and `G` be any two determinant-one restricted-analytic lifts of the
same special map.  In `A=Z_p<x,y>`, solve

```text
F(X,Y)=G(x,y),             (X,Y)=(x,y) mod p.             (3.1)
```

The special Jacobian of `F` is the identity, so multivariate Hensel gives a
unique solution `phi=(X,Y)` congruent to the identity.  Reversing `F,G` gives
`psi`.  Both `phi o psi` and the identity solve `F(H)=F` in the identity
residue branch; uniqueness gives `phi o psi=id`, and similarly
`psi o phi=id`.  Hence

```text
F o phi=G,          phi in Aut Z_p<x,y>,          phi=id mod p.  (3.2)
```

Taking determinants in (3.2) gives `det J(phi)=1`.  The two lifted deck
actions are conjugate by `phi`.

Moreover

```text
Z_p<x,y>/p^n = (Z/p^n)[x,y],                              (3.3)
```

because a restricted series has only finitely many coefficients nonzero
modulo `p^n`.  Thus every finite truncation of `phi` is a polynomial
symplectomorphism, although its support need not be uniformly bounded in
`n`.  This is why literal finite-depth cohomology classes disappear, while a
**uniformly bounded representative/gauge** problem remains meaningful and
open.

## 4. Independent mod-`p^2` derivation

Write

```text
tau(x,y)=(x+1,y)+p(a,b) mod p^2,
Delta f=f(x+1,y)-f(x,y),
N f=sum_(i in F_p) f(x+i,y).
```

Iteration gives

```text
tau^p(x)=x+p(1+N(a)),       tau^p(y)=y+pN(b) mod p^2,
```

and the Jacobian is `1+p(a_x+b_y)`.  Therefore

```text
N(a)=-1,             N(b)=0,             a_x+b_y=0.       (4.1)
```

Now write

```text
P=x-x^p+pP1,          Q=y+pQ1,
c(x)=((x+1)^p-x^p-1)/p mod p.
```

Expanding `F o tau=F` gives

```text
a=c-Delta(P1),        b=-Delta(Q1),                         (4.2)
```

while the first Keller row is

```text
P1_x+Q1_y=x^(p-1).                                    (4.3)
```

Differentiating the integral definition of `c` gives
`c_x=Delta(x^(p-1))`, so (4.2)--(4.3) imply the divergence row in (4.1).
Telescoping gives `N(c)=-1`, and `N Delta=0`, proving the norm rows.

A source change `id+p(r,s)` with `r_x+s_y=0` changes `(a,b)` by the
`Delta`-coboundary of `(r,s)` (up to the harmless convention for which side
is conjugated).  Differences between any two solutions of (4.3) are exactly
such divergence-free pairs.  Thus the first-digit solution space is one
affine gauge orbit.

There is nevertheless a forced common monomial.  In the coefficient of
`x^(p-1)` in (4.3), `P1_x` cannot contribute: its only possible source is
`x^p`, whose derivative is zero in characteristic `p`.  Hence

```text
[x^(p-1)y] Q1 = 1.                                      (4.4)
```

This is the first Cartier/divergence support floor.  It is shared by the
single orbit, not a new mixed quotient class.

## 5. Exact `p=3,5` compiler

The preregistered rectangle was `0<=deg_x<=p`, `0<=deg_y<=1` independently
in `P1,Q1`.  Deterministic row reduction over `F_p` produced:

| `p` | variables | divergence rank | affine dimension | gauge-kernel dimension | quotient dimension | (4.4) forced |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 16 | 6 | 10 | 10 | 0 | yes |
| 5 | 24 | 10 | 14 | 14 | 0 | yes |

The compiler independently obtained

```text
p=3: c=x+x^2,
p=5: c=x+2x^2+2x^3+x^4,
```

and checked (4.1)--(4.3), exact invariance modulo `p^2`, determinant one for
both the quotient map and action, and order `p` from the norm equations.

## 6. Rational cotangent control

Put `g=x-x^p`, `g'=1-px^(p-1)` and

```text
S_n=sum_(j=0)^(n-1) p^j x^(j(p-1)),
F_n=(g,y S_n) mod p^n.
```

Then exactly over the integers

```text
det J(F_n)=(1-px^(p-1))S_n
          =1-p^n x^(n(p-1)),                              (6.1)
```

so `F_n` has determinant one modulo `p^n`.  At the first digit it has

```text
P1=0,       Q1=x^(p-1)y,
a=c,        b=-Delta(x^(p-1)y),                           (6.2)
```

and realizes (4.4).  The replay checked depths `2,3,4` for `p=3,5`.  Its
`Q` supports are respectively

```text
p=3: {0,2}, {0,2,4}, {0,2,4,6} in x,
p=5: {0,4}, {0,4,8}, {0,4,8,12} in x,
```

always with `y`-degree one.

At the inverse limit, if `t` is the unique restricted-analytic root
congruent to `x+1` of `g(t)=g(x)`, the deck generator is

```text
tau(x,y)=(t, y g'(t)/g'(x)).                              (6.3)
```

Equation (6.3) makes the category boundary visible: it is a valid symplectic
deck map on the unit bidisc and need not be a rational or polynomial map.

The linear support growth of this representative is a control, not a lower
bound for the whole orbit beyond the forced first digit.  Proving such a
lower bound remains the substantive avenue.

## 7. Stop and resurrection rule

The registered output is `GAUGE-TRIVIAL/CONTROL-ONLY`:

* finite-etale rank `p`, the free lifted action, and volume preservation hold;
* the first-digit equations and forced Cartier monomial hold;
* the full registered first-digit quotient has no mixed class;
* the cotangent tower is recovered;
* no depth-uniform support obstruction is proved.

Do not continue by computing deeper unrestricted cohomology and calling raw
support differences invariant.  A successor must first preregister one of:

1. minimal support/degree **within the unique orbit**, including a uniform
   bound on admissible polynomial gauges and compatibility across depth; or
2. an algebraic boundary conductor invariant under a specified bounded
   polynomial equivalence.

Only a proof that those minima escape every fixed bound would close a
fixed-support AS109 lift.  Nothing here licenses a `p=109` computation.

## 8. Replay and provenance

Run:

```bash
python3 cases/as109_wild_symplectic_gate_20260824/replay.py
```

The replay uses Python's standard library only, runs in under one second, and
prints the complete deterministic JSON record.  It imports no campaign
solver and writes no files.

The frozen input hashes are printed by the replay.  The two primary general
algebra dependencies used above are Stacks Tags `0ALJ` and `09ZL`; all
campaign-specific predecessor claims retain the scopes of their reviewed
reports.
