# AS109 sextic successor: exact exclusion of the coprime `(5,6)` pair

**Verdict: `EXACT (5,6) EXCLUSION`.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Field: arbitrary characteristic-zero field, after base change to its
  algebraic closure
- Frozen input: the sextic frontier preflight and its landed different-model
  `CONFIRMED` review
- New result: an actual `y`-degree pair `(5,6)` cannot be Keller
- Both `y=0` polynomial boundary equations retained: yes
- Characteristic vector field derived: yes
- Exact bounded primitive / zero-cofactor Darboux search: yes
- Exact weighted pole and polynomial-infinity gates: yes
- Generic support enumeration, exponent rectangle, AWS: none
- Full `y`-degree-at-most-six theorem: not proved; `(4,6)` remains
- New AS109 floor, lift, or JC2 inference: none

The hostile review of the preflight found the identity that changes the
problem:

```text
dI_1 = omega-(2A/5)dI_3.                                (0.1)
```

Thus the apparent Pfaffian survivor actually has three polynomial first
integrals.  The five algebraic equations consisting of those three
integrals and **both** constant-term boundaries define a finite weighted
map.  Equivalently, their weighted leading forms have no common nonzero
point.  This makes the rational depression data polynomial.

The remaining constant Jacobian row then closes the pair at polynomial
infinity: every nonconstant weighted direction has a nonzero leading
`eta` coefficient of degree `10q-1`, while a constant coefficient tuple
has `eta(X')=0`.  Both alternatives contradict `h eta(X')=jbar!=0`.

This eliminates only `(5,6)`.  It does not consume, change, or close the
independent imprimitive `(4,6)` survivor.

## 1. Input and scope

The frozen producer is
`xmodel/as109-sextic-frontier-preflight-20260824.md`.  Its different-model
review `xmodel/as109-sextic-preflight-review-grok-20260824.md` is
`CONFIRMED` and explicitly licenses (0.1) as successor input.  All normal
form identities below are also checked by the new replay.

Work over an algebraically closed characteristic-zero field `k`.  Suppose,
for contradiction, that a Keller pair has actual `y`-degrees `(5,6)`.
The reviewed leading normalization and target alignment give

```text
z=h y+r,                    h in k[x], h!=0,

f=z^5+A z^3+B z^2+C z+D,
g=z^6+P z^4+Q z^3+R z^2+S z+T,                         (1.1)
```

where `r,A,B,C,D` initially lie in `k(x)`, and `P,...,T` are the exact
polynomials in `A,B,C,D` and the constants
`alpha,beta,gamma,delta,epsilon` displayed in parent equation (5.2).
The Jacobian rows are

```text
I_3'=0,       I_2'=0,       omega(X')=0,
h eta(X')=jbar in k*,                 X=(A,B,C,D).      (1.2)
```

The two boundary values

```text
u=f(x,0),                 v=g(x,0)                     (1.3)
```

belong to `k[x]`.  No bound on their or the coefficients' `x`-degrees is
used.

## 2. Third integral and characteristic field

The new weight-nine integral is

```text
I_1 = 24A^3B/125+8alpha A^2B/25+4beta A^3/25
      -4B^3/25-4alpha BC/5-3beta B^2/5
      -18ABC/25-3beta AC/5-4gamma AB/5
      -6A^2D/25-delta A^2/5
      +6CD/5+2gamma D+delta C.                         (2.1)
```

Direct differentiation gives the full-ring identity (0.1).  Consequently
every path satisfying (1.2) also satisfies

```text
I_1=k_1,        I_2=k_2,        I_3=k_3,               (2.2)
```

for constants `k_i`.

On the rank-three locus define the cofactor-minor vector

```text
V_i=(-1)^i det(partial(I_1,I_2,I_3)
                /partial(X_0,...,Xhat_i,...,X_3)),      (2.3)
```

with zero-based indices.  Laplace expansion gives

```text
dI_1(V)=dI_2(V)=dI_3(V)=omega(V)=0.                    (2.4)
```

Thus `X'=lambda V`, and the speed is fixed by

```text
h lambda eta(V)=jbar.                                  (2.5)
```

The replay verifies that `eta(V)` is not the zero polynomial.  The pole
proof below uses the undivided identities (1.2), so it remains valid at
rank-drop points of (2.3).

### 2.1 Bounded exact searches

Give

```text
(A,B,C,D; alpha,beta,gamma,delta)
       weights (2,3,4,5; 2,3,4,5).                     (2.6)
```

An exact linear ansatz over `Q` searched for all weight-nine `H` involving
`X` and weight-two `mu` satisfying

```text
dH-mu dI_3=omega.                                      (2.7)
```

After quotienting the trivial freedom
`(H,mu)->(H+c alpha I_3,mu+c alpha)`, the 26-column system has rank 26 and
the unique solution is

```text
H=I_1,                    mu=-2A/5.                    (2.8)
```

The characteristic derivation `V` was then searched for homogeneous
zero-cofactor Darboux polynomials through weight nine, excluding polynomials
of the parameters alone.  The exact kernel nullities for weights `1,...,9`
are

```text
0,0,0,0,0,0,1,1,2.                                    (2.9)
```

They are accounted for by `I_3` at weight seven, `I_2` at weight eight,
and `I_1, alpha I_3` at weight nine.  Hence this bounded search finds no
fourth low-weight integral.  No nonzero-cofactor Darboux search is needed
for the closure below, and no claim is made beyond the registered bound.

## 3. The weighted binary-form identity

For the pole calculation retain only the highest variable-weight parts.
Define homogeneous binary forms

```text
F(t,z)=z^5+A t^2z^3+B t^3z^2+C t^4z+D t^5,

G(t,z)=z^6+(6A/5)t^2z^4+(6B/5)t^3z^3
       +(3A^2/25+6C/5)t^4z^2
       +(6AB/25+6D/5)t^5z
       +(-4A^3/125+6AC/25+3B^2/25)t^6.                (3.1)
```

Use the scaled leading integrals

```text
K_3=-2A^2B+5AD+5BC,
K_2=3A^4-20AB^2-20A^2C+50BD+25C^2,
K_1=12A^3B-10B^3-45ABC-15A^2D+75CD,                  (3.2)
```

so that `I_3^top=6K_3/25`, `I_2^top=3K_2/125`, and
`I_1^top=2K_1/125`.  Finally put

```text
H_10=4A^3C-30AC^2-15B^2C+25ABD+125D^2.                (3.3)
```

Exact expansion gives the central identity

```text
J_(t,z)(F,G)
 = (42/25)K_3 t^6z^3+(24/125)K_2 t^7z^2
   +((18/125)K_1+(84/125)A K_3)t^8z
   +(6/125)H_10 t^9.                                   (3.4)
```

It also follows conceptually by evaluating the nine reviewed Jacobian rows
on the weighted radial vector

```text
W=(2A,3B,4C,5D).                                       (3.5)
```

In particular,

```text
eta^top(W)=6H_10/125.                                  (3.6)
```

## 4. Binary common-factor lemma

The following lemma simultaneously controls finite poles and polynomial
infinity.

**Lemma.** If `K_1=K_2=K_3=0` and `F,G` have a common finite root
`z=r t`, then `A=B=C=D=r=0`.  If only `K_1=K_2=K_3=H_10=0`, then
`A=B=C=D=0`.

For the first statement, the linear form `L=z-r t` divides both binary
forms.  Their Jacobian is therefore divisible by `L`.  By (3.4) it is
`(6/125)H_10 t^9`; since `L` is not associated to `t`, this forces
`H_10=0`.  The second statement begins at this point.  Equation (3.4) now
gives `J_(t,z)(F,G)=0`.

Euler's identities imply

```text
t J_(t,z)(F,G)=5F G_z-6G F_z=0.                        (4.1)
```

Over `k(t)[z]`, this says `(F^6/G^5)_z=0`.  Both sides are monic with
degrees `30`, so `F^6=G^5`.  Unique factorization and `gcd(5,6)=1` give

```text
F=L_0^5,                    G=L_0^6                    (4.2)
```

for a monic linear `L_0` in `z`.  The missing `z^4` coefficient of the
depressed `F` forces `L_0=z`.  Hence `A=B=C=D=0`; a common root in the
first statement then gives `r^5=0`.

No genericity, smoothness, or division by a coefficient variable enters
the lemma.

## 5. Both boundaries give polynomial depression data

At a finite place let

```text
q=max{0,-v(r),-v(A)/2,-v(B)/3,-v(C)/4,-v(D)/5}.        (5.1)
```

If `q>0`, pass harmlessly to a finite ramified local extension so the
weighted initial coefficients are defined.  At least one of
`(r_0,A_0,B_0,C_0,D_0)` is nonzero.  Because the right sides of (1.3) and
(2.2) are regular, their highest-pole parts give

```text
F(1,r_0)=0,          G(1,r_0)=0,
K_3=K_2=K_1=0.                                          (5.2)
```

Terms containing `alpha,beta,gamma,delta,epsilon` have strictly lower
variable weight and do not occur in (5.2).  The common-factor lemma says
that the initial tuple is zero, a contradiction.  Therefore

```text
r,A,B,C,D in k[x].                                      (5.3)
```

Both boundary equations are essential to this inference.  With all
integration parameters zero, the line `A=B=C=0` lies on all three integral
levels.  For nonzero `r`,

```text
D=-r^5       gives F(1,r)=0,       G(1,r)=-r^6/5,
D=-5r^5/6    gives G(1,r)=0,       F(1,r)= r^5/6.       (5.4)
```

Taking `r=-x^-1` and `h=x^11` produces the corresponding exact one-boundary
Pfaffian controls; each missing boundary retains a pole.

### 5.1 Finite-map / monic certificate

The independent exact Singular replay forms the ideal of the five
polynomials in (5.2) over `Q`.  It finds

```text
dimension = 0,
quotient vector-space dimension = 126,
r^21 belongs to the leading ideal.                      (5.5)
```

The length `126=5*6*7*8*9/(1*2*3*4*5)` is the weighted complete-intersection
number.  Thus the full map

```text
(r,A,B,C,D) -> (f(x,0),g(x,0),I_3,I_2,I_1)             (5.6)
```

is finite after the lower-weight parameter terms are restored.  Filtered
division gives at most 126 module generators.  Cayley-Hamilton therefore
supplies a monic eliminant of degree at most 126 for each of
`r,A,B,C,D` over the algebra generated by the five displayed values.
This is the algebraic counterpart of the valuation proof of (5.3); no huge
expanded eliminant is needed.

## 6. Polynomial infinity closes `(5,6)`

Now all coefficient variables are polynomials.  If at least one of
`A,B,C,D` is nonconstant, set

```text
q=max{deg(A)/2,deg(B)/3,deg(C)/4,deg(D)/5}>0.           (6.1)
```

Let `(a,b,c,d)` be the nonzero weighted leading tuple.  Equations (2.2)
give

```text
K_1(a,b,c,d)=K_2(a,b,c,d)=K_3(a,b,c,d)=0.              (6.2)
```

The second part of the common-factor lemma says
`H_10(a,b,c,d)!=0`.  By (3.6), the coefficient of degree `10q-1` in the
last row is exactly

```text
(6q/125) H_10(a,b,c,d),                                (6.3)
```

which is nonzero.  Since a positive integer degree occurs among variables
of weights at most five, `q>=1/5`, hence `10q-1>0`.  Lower parameter terms
cannot cancel (6.3).  Consequently `eta(X')` is a nonconstant polynomial.
The product

```text
h eta(X')=jbar in k*                                   (6.4)
```

cannot hold because `h` is a nonzero polynomial.

If all four coefficient variables are constant, then `X'=0` and
`eta(X')=0`, contradicting (6.4) directly.  These alternatives exhaust the
case.  Therefore no characteristic-zero Keller pair has actual
`y`-degrees `(5,6)`.

## 7. Exact replay

Run, without network access:

```text
python3 cases/as109_sextic_56_next_gate_20260824/verify_sextic_56_gate.py
Singular -q cases/as109_sextic_56_next_gate_20260824/verify_weighted_finiteness.sing
```

The standard-library Python replay uses exact `Fraction` sparse polynomial
arithmetic.  It reconstructs (2.8) by linear solve rather than merely
checking a copied primitive; derives the characteristic minors; verifies
(2.4), the bounded Darboux nullities, (3.4), and both one-boundary controls.
The Singular replay independently checks (5.5) and the zero-dimensional
`(K_1,K_2,K_3,H_10)` infinity certificate, whose quotient length is 42.

Expected verdicts are

```text
EXACT-(5,6)-EXCLUSION
EXACT-WEIGHTED-(5,6)-CERTIFICATE
```

## 8. Campaign consequence and quarantine

The coprime sextic branch is closed.  Conditional on the already landed
quintic theorem, the only new maximum-`y`-degree-six blocker is now the
imprimitive `(4,6)` family.  Since that family remains alive, this report
does **not** prove a full degree-at-most-six theorem and does not raise the
reviewed AS109 correction floor from six to seven.

No result here constructs or excludes an arbitrary-support AS109 lift,
uses finite-Witt evidence, proves or disproves JC2, or makes a priority
claim.

## 9. Provenance hashes

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | frozen parent |
| `xmodel/as109-sextic-preflight-review-grok-20260824.md` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | landed `CONFIRMED`; (0.1) consumed |
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | frozen parent replay |
| `cases/as109_sextic_frontier_preflight_20260824/FREEZE.sha256` | `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab` | frozen parent manifest |
| `cases/as109_sextic_56_next_gate_20260824/verify_sextic_56_gate.py` | `cab6e8597403f5c19d03fcf2da42c37ee3523ce7de2e825812ba1a5cbc47d5d0` | exact successor replay |
| `cases/as109_sextic_56_next_gate_20260824/verify_weighted_finiteness.sing` | `0b0c36722f64365ddb0e1c891569124a658c86a77a967c415a5f41da631f61ca` | independent exact Groebner certificate |

No parent, review, canonical top-level file, ledger, or AWS resource was
edited by this lane.
