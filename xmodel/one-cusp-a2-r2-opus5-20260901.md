# ONE-CUSP-A2 (r2): the A-degree-2 layer of the horn induction

Lane: ONE-CUSP-A2, round 2. Date 2026-09-01. Desk-scale exact reasoning only;
no CAS was run, no literature was fetched, no charged or canonical file was
edited, `jc2-lean` was not inspected. The only file written is this report.

Contents: 0 inputs/scope; 1 promoted state; 2 the (T,V) chart; 3 why the naive
induction breaks; 4 normal form and the three-cell census; 5 two cells killed;
6 the surviving cell (3,2); 7 verdict; 8 AWS SPEC; 9 open items; 10 successor.

## 0. Input verification and scope

`shasum -a 256` on the four frozen read-only copies returned, before any
mathematical reading,

```text
4009c3abdc16e972aec121206664a21adc81ff8467dfe8d5a0f561e90f3a86d5  theta-reopen-explicit-pullback-sol56-20260831.md
26079008ffeba9b94ecfcc79c63690cc232f7f50f655d477835dc26b80f59cd3  theta-reopen-hostile-review-gpt55-20260831.md
1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb  round1033-theta-staged-sol56-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

All four match the charge exactly. Below they are `theta`, `review`,
`staged`, `integration`.

Scope of the target claim. `OBSTRUCTION[A-DEGREE-TWO]` is the assertion that
the exact system `E=kappa`, `O=0` of `theta:(1.3E)-(1.4)` has no solution with

```text
deg_A P <= 2, deg_A Q <= 2, deg_A R_0 <= 2, deg_A S_0 <= 2.
```

This class is stable under the affine target group `Aff_2(C)` acting on
`(f,g)` (Section 4), so the claim is intrinsically independent of the residue
normalization: it is *not* attached to the minimal residue family (2.2)-(2.5)
of `theta`, nor to any `T_0` stratum. Everything below is proved for arbitrary
residue data unless explicitly flagged.

## 1. Promoted state carried in

Consumed as given, with no re-derivation charged:

1. The ring, the bracket, and the even/odd split. `q=U^2-A-A^2Z`,
   `R=C[A,U,Z]/(q)` (written `RR` below to free `R_0`), `H=A(1+AZ)`,
   `c=2(1+2AZ)`, and the identities `{A,U}=2A^2`, `{A,Z}=4U`, `{U,Z}=c`
   (`theta:51-63`; `review:29-56`). I re-derived (1.3E)/(1.3O) independently
   and confirm them; I also record the compact form used throughout, with
   `J(F,G)=F_A G_Z-F_Z G_A`, `W_A(F,G)=F_A G-F G_A`, `W_Z(F,G)=F_Z G-F G_Z`:

   ```text
   E = 2A^2(P_A S_0 - Q (R_0)_A) + 4H(J(P,S_0)+J(Q,R_0))
       + c(Q (R_0)_Z - P_Z S_0),
   O = 2A^2 W_A(Q,S_0) + 4 J(P,R_0) + 4H J(Q,S_0) - c W_Z(Q,S_0).   (1.1)
   ```

   The second line is the load-bearing structural fact: **`O` never couples
   the even pair `(P,R_0)` to the odd pair `(Q,S_0)`.** This is forced by the
   Galois involution `sigma: U -> -U` being *anti*-Poisson, so that
   `U*O = {P,R_0} + {UQ,US_0}` and `E = {P,US_0} + {UQ,R_0}`.
2. `OBSTRUCTION[A-DEGREE-ZERO]` (`theta:(3.2)`), promoted, and
   `OBSTRUCTION[A-LINEAR-MINIMAL-JET]` (`theta:(3.11)`), promoted as a bounded
   exclusion at `p=Z^2, r=Z^3-Z, T_0=0` (`review:§2-§3`).
3. The degree-8 reframe as routing only (`theta:(3.14)`; `review:§4`;
   `integration:§2` disproof side).
4. The review's diagnosis that the naive leading-term induction breaks at
   `A`-degree two, with the free second-order compensator
   `2(C_2(3Z^2-1)-2Z E_2)` appearing in `[A^1]O` (`review:§6`). Section 3
   confirms this and shows it is very much worse than the review states.
5. The first-jet equation `2(q_1 r' - p' s_1)=kappa` and the immersivity of the
   residue parametrization, i.e. `gcd(p',r')=1` (`theta:1.2`, `theta:§2.1`).

Not used anywhere below: the rank-four field degree, the boundary curve `B`,
the partition table, and `Theta_h`. Those remain at their promoted `OPEN`
status (`theta:§4-§6`; `staged`).

## 2. The (T,V) chart: A-degree becomes a pole order

Everything in this report runs in one chart, which I did not find in the
frozen inputs and which trivializes the "top of the `A`-tower".

**Proposition 2.1 (chart).** `q=U^2-A-A^2Z` is irreducible, so `RR` is a
domain and `A` is a nonzerodivisor. Put `T=1/A` and `V=U/A`. Then

```text
RR[A^-1] = C[T,T^-1,V],     A=T^-1,  U=V T^-1,  Z=V^2-T.      (2.1)
```

*Proof.* Localizing, `U=AV`, and `q=0` becomes `A^2(V^2-Z)=A`, i.e.
`V^2-Z=1/A=T`, so `Z=V^2-T` is redundant and `RR[A^-1]=C[T^{\pm},V]`. The
displayed images satisfy `(VT^-1)^2-T^-1-T^-2(V^2-T)=0`. QED

**Proposition 2.2 (bracket).** In this chart `{V,T}=2T`, hence for all `F,G`

```text
{F,G} = 2T(F_V G_T - F_T G_V) = 2(F_V*De(G) - De(F)*G_V),  De = T*partial_T. (2.2)
```

*Proof.* `{T,U}=-A^{-2}{A,U}=-2`, so `{T,V}={T,UT}=T{T,U}=-2T`. Consistency:
`{V,Z}={V,V^2-T}=-{V,T}=-2T`, which agrees with the direct reduction of
`{U,Z}=2+4AZ`. QED

Two arithmetic checks against the generators, done by hand and both exact:
with `f=A, g=U` formula (2.2) returns `2T^-2=2A^2`; with `f=U, g=Z` it returns
`4V^2T^-1-2 = 2+4AZ`. So (2.2) is the promoted bracket, not a renaming.

Write `v` for the `T`-adic valuation on `C[T^{\pm},V]` and expand
`f=sum_i f_i(V) T^i`. Formula (2.2) gives the exact coefficient law

```text
[T^m]{f,g} = 2 * sum_{i+j=m} ( j f_i' g_j - i f_i g_j' ),  ' = d/dV.  (2.3)
```

Let `sigma: V -> -V`; it fixes `T` and is exactly the Galois involution
`U -> -U`, and it is anti-Poisson.

**Proposition 2.3 (degree dictionary).** For `f=P+UQ` in `RR`:
`v(P) = -deg_A P` and `v(UQ) = -1-deg_A Q`, and these are the even and odd
parts of `f` under `sigma`. Consequently, for every `d>=0`,

```text
deg_A P <= d and deg_A Q <= d   <=>   v(f) >= -(d+1) and f_{-(d+1)} is odd.
```

In particular the `A`-degree-2 class is `{ v(f)>=-3, f_{-3} odd }`, and

```text
v(f) >= 0   <=>   f in C[Z]  (i.e. Q=0 and deg_A P = 0).            (2.4)
```

*Proof.* `P=sum_i C_i(Z)A^i` maps to `sum_i C_i(V^2-T)T^-i`, whose lowest
`T`-power is `T^{-deg_A P}` with coefficient `C_{deg_A P}(V^2) != 0`; likewise
`UQ` maps to `V sum_j D_j(V^2-T) T^{-j-1}`, lowest power `T^{-1-deg_A Q}` with
coefficient `V D_{deg_A Q}(V^2)`. The even/odd parts cannot cancel each other,
so `v(f)=min` of the two. For the equivalence, `v(f)>=-(d+1)` gives
`deg_A P<=d+1` and `deg_A Q<=d`, and `f_{-(d+1)} = C_{d+1}(V^2)+V D_d(V^2)`
is odd exactly when `C_{d+1}=0`. For (2.4), `v(UQ)>=0` forces `deg_A Q<=-1`,
i.e. `Q=0`. QED

Two remarks that matter later. First, `S \ Phi = Spec RR[A^-1]` is
`G_m x A^1`: the interior divisor `Phi=V(A,U)` is exactly `T=infinity`, and the
whole `A`-adic tower of the horn lives at the *opposite* end `T=0`. Second, the
constraint `deg_A <= 2` is a bound on the order of the pole of `f` along the
prime divisor `{T=0}` of a compactification of `S \ Phi`, plus one parity
condition on the leading coefficient. Under the source chart `iota` of
`theta:(3.12)` one has `T=x^-2`, `V=x^-1+xy`, `{x,y}=1`; so `v` is (twice) the
monomial divisorial valuation of `C(x,y)` with `v(x)=-1`, `v(y)=+1`, whose
residue field is `C(xy-bar)`. The `A`-filtration of the horn is therefore a
classical filtration at one divisorial place at infinity of the plane. No flag,
place or series is identified here: `{T=0}`, `Phi`, the target place
`q_infty` of `theta:§4`, and the generic ramified factor of `theta:(1.7)`
remain four distinct objects, and none of them is used below.

## 3. Why the naive leading-term induction breaks at A-degree 2

The review located a free compensator in `[A^1]O` (`review:§6`). The true
situation is stronger and settles the question of bottom-up induction for good.

Write `P=sum C_i A^i`, `Q=sum D_i A^i`, `R_0=sum E_i A^i`, `S_0=sum L_i A^i`
with `C_i,D_i,E_i,L_i in C[Z]`, and abbreviate the level-0 residue data
`p=C_0, q=D_0, r=E_0, s=L_0`. Reading off (1.1) term by term in `A` (each
summand of `E` and of `O` is one of `A^2, H=A+A^2Z, c=2+4AZ` times a
bilinear expression, so this is a finite collection of index shifts, not an
expansion) gives the two support laws:

```text
[A^n]O involves C,E at level <= n+1 and D,L at level <= n;
[A^n]E involves all four at level <= n.
```

and, isolating in each the part where one index is `n+1` resp. `n`:

```text
[A^n]O = 4(n+1)( C_{n+1} r' - p' E_{n+1} ) + M_n,                    (3.1)
[A^n]E = (4n+2)( D_n r' - p' L_n )
         + 2( 2n C_n s' - C_n' s ) + 2( q E_n' - 2n q' E_n ) + Lam_n,  (3.2)
```

where `M_n` depends only on levels `<= n` and `Lam_n` only on levels `<= n-1`.

Both displayed formulas were checked against the promoted, independently
reviewed `A`-linear computation. For `n=0`, (3.1) with
`M_0=-2(q's-qs')` reproduces `theta:(3.4)` verbatim at the minimal jet, and for
`n=1`, (3.2) reproduces the review's pre-substitution collection
`-3KC+(3KZ/2)C'-KE'+6D(3Z^2-1)-12ZL+2KZ` (`review:§3`) exactly, with `+2KZ` as
the level-0 remainder. This is the only place the frozen `A`-linear data is
used, and it is used as a control, not as an input.

**Lemma 3.1 (Bezout surjectivity).** If `gcd(p',r')=1` in `C[Z]` then
`(X,Y) -> X r' - p' Y` is surjective onto `C[Z]` with kernel exactly
`{(p'T, r'T) : T in C[Z]}`.

Immersivity of the residue parametrization -- promoted at `theta:§1.2, §2.1` --
is precisely `gcd(p',r')=1`.

**Theorem 3.2 (formal unobstructedness along Phi).** Let `(p,q,r,s)` satisfy
`gcd(p',r')=1` and `2(qr'-p's)=kappa != 0`. Then the constraint system
`E=kappa, O=0` has a solution in the completion

```text
RRhat = C[Z][[A]] + U C[Z][[A]]
```

with that residue datum. The solution set is nonempty at every level and has a
free `C[Z]` at each level; no level is ever obstructed.

*Proof.* The bracket formulas (1.1) are `A`-adically continuous, so
`E=kappa, O=0` in `RRhat` is exactly the sequence of coefficient equations
`[A^0]E=kappa`, `[A^n]E=0` (`n>=1`), `[A^n]O=0` (`n>=0`). `[A^0]E=kappa` is the
residue equation, satisfied by hypothesis. Recur in the order

```text
level 0  ->  (C_1,E_1)  ->  (D_1,L_1)  ->  (C_2,E_2)  ->  (D_2,L_2)  -> ...
```

At the `(C_{n+1},E_{n+1})` step, `M_n` in (3.1) is already determined, and by
Lemma 3.1 the equation `4(n+1)(C_{n+1}r'-p'E_{n+1}) = -M_n` is solvable, with a
free `T in C[Z]`. At the `(D_n,L_n)` step, everything in (3.2) except
`(4n+2)(D_n r'-p'L_n)` is already determined -- `C_n,E_n` were fixed at the
previous step -- and Lemma 3.1 solves it, again with a free `T`. QED

**Corollary 3.3.** No bottom-up induction on the `A`-adic hierarchy can ever
produce an obstruction, at any residue point of the seven-parameter family, at
any `T_0` stratum, and at any level. The mechanism of `theta:(3.10)` -- an
uncancellable leading term in `Z` on one side of `[A^1]O` -- is destroyed at
`A`-degree 2 for a reason that recurs at every higher level: the level-`(n+1)`
even data enters `[A^n]O` *only* through the Bezout combination
`C_{n+1}r'-p'E_{n+1}`, which is a surjection. Symmetrically the level-`n` odd
data enters `[A^n]E` only through `D_n r'-p'L_n`, also a surjection. The
compatible finite layer `theta:(2.9)` is therefore not a coincidence but the
first two steps of Theorem 3.2.

This is the exact answer to "which cancellation becomes possible": *both*
Bezout compensators, not just the one the review displayed, and at every level.
It also relocates the whole problem. A formal solution along `Phi` always
exists; the entire content of any `A`-degree obstruction is **polynomiality**,
i.e. termination of the recursion. Obstructions must therefore be read off the
*top* of the tower, never the bottom.

## 4. The top-down invariant, one unbounded lemma, and a three-cell census

### 4.1 Pole orders and the leading-form equation

For a candidate pair put `alpha = -v(f)`, `beta = -v(g)`. Proposition 2.3 gives
`alpha, beta <= 3` in the `A`-degree-2 class, and `f_{-3}`, `g_{-3}` odd.
Applying (2.3) at `m=-alpha-beta`, where only `(i,j)=(-alpha,-beta)` occurs,

```text
alpha * f_{-alpha} * g_{-beta}' = beta * f_{-alpha}' * g_{-beta}.      (N0)
```

Equivalently `d/dV log( g_{-beta}^alpha / f_{-alpha}^beta ) = 0`, so with
`k0=gcd(alpha,beta)` there is `h in C[V]` and nonzero constants with

```text
f_{-alpha} = c_1 h^{alpha/k0},    g_{-beta} = c_2 h^{beta/k0}.         (4.1)
```

This is the second-order invariant asked for: it is the discriminant-free
integrated form of the leading system, and unlike the bottom-of-tower equations
of Section 3 it admits **no** compensator, because at `A`-degree 2 there is no
level-3 datum to absorb it.

**Parity transfer.** If `u^k` is `sigma`-odd for odd `k`, then `u` is odd:
`sigma(u)^k=(-u)^k` forces `sigma(u)=-zeta u` with `zeta^k=1`, and applying
`sigma` again gives `zeta^2=1`, hence `zeta=1`. So whenever `alpha=3` in (4.1),
`h` is an odd polynomial, `h(0)=0`, `deg h >= 1`.

### 4.2 An unbounded side lemma

**Lemma 4.1 (`OBSTRUCTION[Z-ONLY-COORDINATE]`).** If `f in C[Z] subset RR`
(that is, `Q=0` and `deg_A P = 0`) then `{f,g}=kappa != 0` has no solution
`g in RR`, at **any** `A`-degree of `g`.

*Proof.* Write `f=ph(Z)`. In (1.1) every `Q`-term dies, so `O=-4 ph' (R_0)_A`.
If `ph'=0` then `f` is constant and `{f,g}=0`. So `ph' != 0` and `(R_0)_A=0`,
i.e. `R_0=r(Z)`. Then `E = -ph' [ 4H (S_0)_A + c S_0 ]`. Since a product of two
elements of `C[A,Z]` equals the nonzero constant `kappa`, both factors are
nonzero constants. Writing `S_0=sum_n L_n A^n`,

```text
4H (S_0)_A + c S_0 = sum_n [ (4n+2) L_n + 4n Z L_{n-1} ] A^n,
```

so `L_0 = -kappa/(2 ph') != 0` and `L_n = -(2nZ/(2n+1)) L_{n-1}` for `n >= 1`.
By induction `L_n != 0` for every `n`, contradicting `S_0 in C[A,Z]`. QED

Lemma 4.1 is genuinely stronger than `theta:(3.2)` in one direction (it puts no
cap on `g`) and weaker in another (it needs `Q_f=0`); the two are complementary
and both are used below. Combining with (2.4): `v(f) >= 0` is impossible, so

```text
alpha >= 1  and  beta >= 1  for every solution, at any A-degree.       (4.2)
```

### 4.3 Affine normal form and the census

The target group `Aff_2(C)` acts by `(f,g) -> (af+bg+e, cf+dg+e')`, replacing
`kappa` by `(ad-bc)kappa != 0`. Each of `P,Q,R_0,S_0` transforms `C`-linearly,
so the `A`-degree-2 class is `Aff_2`-stable, and proving
`OBSTRUCTION[A-DEGREE-TWO]` for normalized pairs proves it outright. No residue
normalization is used or needed.

**Proposition 4.2 (normal form).** Any `A`-degree-2 solution can be moved by
`Aff_2` to one with `alpha > beta >= 1`, hence with

```text
(alpha,beta) in { (3,2), (3,1), (2,1) }.                              (4.3)
```

*Proof.* Swap `f,g` so `alpha >= beta`. If `alpha = beta` then (N0) reads
`Wr(f_{-alpha}, g_{-beta}) = 0`, so `g_{-beta} = lambda f_{-alpha}` for a
nonzero constant and `g - lambda f` has strictly smaller pole order while
staying in the class; one such step suffices. Then (4.2) gives `beta >= 1` and
Proposition 2.3 gives `alpha <= 3`. QED

Three cells. Sections 5 and 6 dispose of two and reduce the third to an
explicit rigid system. Note that (4.3) already forbids `alpha = beta`, which is
the classical "same degree" case; the surviving arithmetic is
`(alpha,beta)=(3,2)` with `gcd = 1`.

## 5. Cells (3,1) and (2,1) are empty

Throughout, `beta=1` forces, by Proposition 2.3 read coefficientwise,

```text
g_{-3}=V L_2(V^2) = 0  =>  L_2=0;
g_{-2}=E_2(V^2)+V L_1(V^2) = 0  =>  E_2=L_1=0;
g_{-1}=E_1(V^2)+V L_0(V^2) != 0.                                       (5.1)
```

### 5.1 Cell (3,1)

Here `alpha=3`, so `f_{-3}` is odd and nonzero, and (4.1) with `k0=1` gives
`f_{-3}=c' k^3` where `k := g_{-1}`. By the parity transfer of §4.1, `k` is
odd, so by (5.1) `E_1=0`. Hence

```text
R_0=r(Z),  S_0=s(Z),   i.e. g has A-degree 0, and k = V s(V^2).       (5.2)
```

Consequently `g^2=(r^2+Hs^2)+U(2rs)` and `g^3=(r^3+3Hrs^2)+U(3r^2s+Hs^3)`
both lie in the `A`-degree-2 class, because `deg_A H = 2`. Now read (2.3) at
`m=-3`, where only `(i,j)=(-3,0)` and `(-2,-1)` occur:

```text
3 f_{-3} g_0' - f_{-2}' g_{-1} + 2 f_{-2} g_{-1}' = 0.
```

Since `f_{-2}' k - 2 f_{-2} k' = k^3 (f_{-2} k^{-2})'`, this integrates once:

```text
f_{-2} = k^2 ( 3c' g_0 + c_3 ),      c_3 in C.                        (5.3)
```

But `(g^3)_{-3}=k^3`, `(g^3)_{-2}=3k^2 g_0` and `(g^2)_{-2}=k^2`, so (5.3) says
exactly that

```text
ft := f - c' g^3 - c_3 g^2   satisfies  v(ft) >= -1,
```

while `ft` is still in the `A`-degree-2 class and `{ft,g}={f,g}=kappa`. If
`v(ft)=-1` then `alpha=beta=1` and one more `Aff_2` step (Proposition 4.2)
gives `fh` with `v(fh)>=0`; by (2.4), `fh in C[Z]`. Lemma 4.1 now contradicts
`{fh,g}=kappa`. Cell `(3,1)` is empty.

### 5.2 Cell (2,1)

Here `alpha=2`, so `D_2=0`, `f_{-3}=0` and
`f_{-2}=C_2(V^2)+V D_1(V^2) != 0`. Equation (4.1) with `(alpha,beta)=(2,1)`
gives `f_{-2}=c_0 k^2`, `k=g_{-1}`. No parity is available here (a square
carries none), so `E_1` need not vanish; but by (5.1)
`R_0=r+A E_1`, `S_0=s`, whence

```text
g^2 = ( (r+A E_1)^2 + H s^2 ) + U ( 2 (r+A E_1) s ),
```

whose four coefficient polynomials have `A`-degrees `2` and `1`. So `g^2` is in
the class, and `ft := f - c_0 g^2` has `v(ft) >= -1`, is in the class, and
satisfies `{ft,g}=kappa`. Exactly as in §5.1, one further `Aff_2` step and
(2.4) produce `fh in C[Z]` with `{fh,g}=kappa`, contradicting Lemma 4.1. Cell
`(2,1)` is empty.

### 5.3 What the two kills share

Both use the same three-step pattern, which is the promotable technique of this
report: (i) the leading-form equation (N0) identifies `f_{-alpha}` with a power
of `g_{-beta}`; (ii) because `beta | alpha`, that power is realized by an actual
element `g^{alpha/beta}` of `RR` which happens to stay inside the `A`-degree-2
class -- this is where the truncation is exploited, and it is exactly the step
Section 3 shows can never be done from the bottom; (iii) subtracting it is a
*nonlinear* automorphism of the constraint (`{g^k,g}=0`), so the pole order
drops without touching `kappa`, and the descent terminates on Lemma 4.1.

Step (ii) is available precisely when `beta` divides `alpha`. This is why the
census (4.3) has exactly one survivor.

## 6. The surviving cell (3,2)

### 6.1 Rigid structure forced by the leading forms

`beta=2` gives `L_2=0` and `g_{-2}=E_2(V^2)+V L_1(V^2) != 0`. `alpha=3` gives
`f_{-3}=V D_2(V^2)` odd and nonzero. With `gcd(3,2)=1`, (4.1) reads

```text
f_{-3}=c_1 h^3,      g_{-2}=c_2 h^2,      c_1 c_2 != 0,
```

and the parity transfer makes `h` odd, say `h=V eta(V^2)` with
`eta in C[Z]`. Then `h^2` is even, so `g_{-2}` is even, so `L_1=0`. Comparing
coefficients (`V^2 = W`, then rename `W` to `Z`):

```text
S_0 = s(Z)                     (g has odd part of A-degree 0),
E_2 = c_2 Z eta^2,   D_2 = c_1 Z eta^3,   equivalently  Z D_2^2 = mu E_2^3
with mu=c_1^2/c_2^3.                                                   (6.1)
```

Three consequences worth isolating: `deg_A S_0 = 0`; `E_2` is `Z` times a
square and `D_2` is `Z` times a cube; and in particular `Z` divides both. The
relation `Z D_2^2 = mu E_2^3` is the exact "second-order invariant" for this
cell -- it is the resultant-free integrated form of the leading system and it
is not absorbable, because there is no level-3 datum.

Control. With `S_0=s`, the four summands of (1.1) cap at `deg_A O <= 3` and
`deg_A E <= 5`. Reading off `[A^5]E` gives
`-D_2 E_2 + 3Z D_2 E_2' - 2Z D_2' E_2 = 0`, and substituting (6.1) makes every
term cancel identically. So `[A^5]E` is *equivalent* to (N0). I did this
substitution by hand in both directions; it is a nontrivial check that the
`(T,V)` machinery of Section 2 and the direct `A`-expansion of (1.1) agree.

### 6.2 The next two structural equations

`[A^3]O` is, after dividing by `4`,

```text
2 Wr(C_2,E_2) + D_2 s + 3Z D_2 s' - Z D_2' s = 0,   Wr(u,v)=uv'-u'v.  (6.2)
```

Substituting (6.1) turns (6.2) into a first-order linear equation for `C_2`
whose homogeneous solution is proportional to `E_2`; integrating it once gives
the complete solution

```text
2 c_2 C_2 = Z eta ( 3 c_1 s + c_5 eta ),      c_5 in C.               (6.3)
```

So `C_2` is *determined* by the pair `(eta,s)` up to a single constant, and
`Z | C_2`. Together with `L_2=0` this says the whole level-2 datum
`(C_2,D_2,E_2,L_2)` vanishes at `Z=0` and is a function of `(eta,s,c_1,c_2,c_5)`
alone.

`[A^4]E` is the first equation reaching level 1. Writing
`G := E_1-E_2'` and `F := D_1-D_2'` (these are exactly the `T`-coefficients
`g^{ev}_{-1}` and `f^{od}_{-2}` of Section 2, which is why they group), the
equation collapses to

```text
3 c_1 eta ( 2Z G' eta - G eta - 2Z G eta' )
   = 2 c_2 ( 2Z F' eta - 3F eta - 8Z F eta' ).                        (6.4)
```

**Proposition 6.1 (a parity-of-degree rigidity).** In (6.4), put
`e=deg eta`, `gamma=deg G`, `phi=deg F`. Every term on the left has degree
`gamma+2e` with combined leading coefficient
`3c_1 eta_e^2 G_gamma (2 gamma - 1 - 2e)`, and every term on the right has
degree `phi+e` with combined leading coefficient
`2 c_2 eta_e F_phi (2 phi - 3 - 8e)`. Both bracketed integers are **odd**,
hence nonzero. Therefore either

```text
F = G = 0,     i.e.  E_1 = E_2',  D_1 = D_2',
```

or `F,G` are both nonzero and `phi = gamma + e`, with the leading-coefficient
relation `3 c_1 eta_e G_gamma (2 gamma - 2e - 1) = 2 c_2 F_phi (2 gamma - 6e - 3)`.

This is the exact analogue, one level up, of the mechanism `theta:(3.9)-(3.10)`
that closed the `A`-linear case: a degree balance forced by a parity that no
choice of coefficients can break. It does not yet close the cell, because there
are still compensators available at levels 0 and 1.

### 6.3 What remains, exactly

After (6.1), (6.3), and Proposition 6.1, the free data of cell `(3,2)` is

```text
eta, s, C_0, C_1, D_0=q, D_1, E_0=r, E_1  in C[Z];   c_1,c_2,c_5,kappa in C,
```

with `c_1 c_2 kappa != 0` and `eta != 0`, and the remaining equations are

```text
[A^n]O = 0  for n = 0,1,2;      [A^n]E = 0 for n = 1,2,3;   [A^0]E = kappa,
```

i.e. seven equations, `[A^3]O`, `[A^4]E`, `[A^5]E` having been consumed above.
This is not a dimension-count kill: eight unknown polynomials against seven
equations, all of unbounded degree. `[A^0]O` and `[A^0]E` are the promoted
residue relations `4(C_1 r' - p' E_1) = 2(q's-qs')` and `2(qr'-p's)=kappa`;
`[A^1]O` is the equation carrying the free Bezout compensator
`8(C_2 r' - p' E_2)` of Section 3, now with `C_2, E_2` already pinned by (6.1)
and (6.3), so it is no longer free -- it has become a genuine constraint on
`(eta,s,C_1,E_1,q,r,p)`. That reversal is the structural gain of this section
and is where a closing argument should be sought.

I did not close cell `(3,2)` inside the budget. Per the fail-closed rule it is
typed `OPEN` in Section 7 and specified for exact computation in Section 8. No
consistent stratum was found; nothing here is a counterexample cell.

## 7. Verdict at A-degree 2

```text
OBSTRUCTION[A-DEGREE-TWO]:  NOT PROVED.  Reduced to exactly one cell.
No consistent stratum found; no counterexample cell to flag.
```

Established, and offered for promotion:

1. **Proposition 2.1-2.3 (the `(T,V)` chart).** `RR[A^-1]=C[T^{\pm},V]` with
   `{V,T}=2T`; the `A`-degree filtration of the horn is a pole-order
   filtration at one divisorial place, and `deg_A <= 2` for all four
   coefficients is exactly `v(f) >= -3` together with `f_{-3}` odd. Verified
   against the promoted generator brackets in two independent instances.
2. **Theorem 3.2 (formal unobstructedness along `Phi`).** For every immersive
   residue point satisfying the first-jet equation, the system `E=kappa, O=0`
   is solvable in `C[Z][[A]] + U C[Z][[A]]`, level by level, with a free
   `C[Z]` at each level. *Scope*: assumes `gcd(p',r')=1`, which is the promoted
   immersivity of the companion parametrization.
3. **Corollary 3.3.** No bottom-up induction can ever obstruct. Both the even
   and the odd hierarchies carry a surjective Bezout compensator at every
   level, so the mechanism of `theta:(3.10)` is not merely broken at
   `A`-degree 2 -- it is unavailable at every level above 1. Any `A`-degree
   obstruction is a **termination** statement about the Theorem 3.2 recursion,
   to be read off the top of the tower.
4. **Lemma 4.1 (`OBSTRUCTION[Z-ONLY-COORDINATE]`).** No `f in C[Z]` has a mate,
   at any `A`-degree of `g`. Unbounded on the `g` side; complementary to, not
   contained in, `theta:(3.2)`.
5. **Proposition 4.2 + Section 5.** In the `A`-degree-2 class every solution is
   `Aff_2`-equivalent to one with `(alpha,beta) in {(3,2),(3,1),(2,1)}`, and
   the cells `(3,1)` and `(2,1)` are **empty**. These two kills are
   unconditional: they use no residue normalization, no `T_0` stratum choice,
   and no companion-curve interface.
6. **Section 6.** Cell `(3,2)` is rigid: `S_0` has `A`-degree `0`;
   `E_2=c_2 Z eta^2`, `D_2=c_1 Z eta^3` (so `Z D_2^2 = mu E_2^3`);
   `2c_2 C_2 = Z eta (3 c_1 s + c_5 eta)`; and by Proposition 6.1 either
   `E_1=E_2', D_1=D_2'`, or `deg(D_1-D_2') = deg eta + deg(E_1-E_2')`.

Guardrail audit. `{T=0}`, `Phi`, the target place `q_infty`, and the generic
ramified factor of `theta:(1.7)` were kept distinct and none was used. No pole
identity, no valuation floor, and no partition row was invoked; `Theta_h` does
not appear. `Aff_2` was declared as a group action on the *target*, with its
effect on `kappa` (multiplication by the determinant) stated, not assumed away.
The `[A^5]E`-vs-(N0) collapse and the two generator-bracket evaluations are
displayed controls, not restatements. Where a full expansion would have been
needed to decide a cancellation -- the level-`<= 1` remainders `M_n`, `Lam_n`
of (3.1)-(3.2) and the bulk of `[A^n]O`, `[A^n]E` for `n <= 3` -- I derived
only the leading structure by hand and specified the bulk in Section 8 rather
than displaying it. No exit price is asserted.

## 8. AWS SPEC for the bulk expansions

Two exact finite computations. Neither was run on this machine.

### SPEC-1 (verification of the coefficient laws)

*Ring.* `Lam = Q[ c(i,k), d(i,k), e(i,k), l(i,k) : 0<=i<=5, 0<=k<=8 ][A,Z]`,
degree-reverse-lex, `A` and `Z` last. Set
`C_i = sum_k c(i,k) Z^k` and likewise `D_i,E_i,L_i`; set
`P=sum_{i<=5} C_i A^i`, `Q=sum D_i A^i`, `R_0=sum E_i A^i`, `S_0=sum L_i A^i`;
`H=A+A^2 Z`, `c=2+4AZ`. Form `E` and `O` by (1.1) with `d/dA`, `d/dZ` the
ordinary partials in `Lam`.

*What to check* (each is a polynomial identity in `Lam`, so the verdict is
`0` or a nonzero witness, never a heuristic):

1. `[A^n]O - 4(n+1)(C_{n+1} r' - p' E_{n+1})` involves no `c(n+1,*)` and no
   `e(n+1,*)`, for `n=0..4`; and involves no `d(j,*)`, `l(j,*)` with `j>n`.
2. `[A^n]E` involves no level-`(n+1)` symbol, and
   `[A^n]E - (4n+2)(D_n r' - p' L_n) - 2(2n C_n s' - C_n' s)
    - 2(q E_n' - 2n q' E_n)` involves no level-`n` symbol, for `n=1..4`.
3. With `L_1=L_2=0`, `deg_A <= 2`: `deg_A O <= 3`, `deg_A E <= 5`;
   `[A^3]O` equals four times the left side of (6.2); `[A^5]E` equals
   `4(-D_2E_2+3Z D_2E_2'-2Z D_2'E_2)`; and after the substitution
   `E_2 -> c_2 Z eta^2`, `D_2 -> c_1 Z eta^3` (with `eta` generic of degree
   `<=3`) `[A^5]E` reduces to `0`.
4. `[A^4]E`, after the same substitution and with `G=E_1-E_2'`,
   `F=D_1-D_2'`, equals a nonzero constant multiple of
   `3c_1 eta(2ZG'eta-Geta-2ZGeta') - 2c_2(2ZF'eta-3Feta-8ZFeta')`.

Bilinear arithmetic only; expected to be minutes, not hours. A nonzero witness
in any item falsifies the corresponding displayed law in Sections 3 or 6, and
must be reported before any downstream use.

### SPEC-2 (decide cell (3,2) over a degree box)

*Model.* Fix integers `(e, sig, N)`. Unknown coefficient vectors over `Q`:
`eta` of degree `e`, `s` of degree `sig`, and `C_0, C_1, D_0, D_1, E_0, E_1`
of degree `<= N`; scalars `c_1, c_2, c_5, kap`. Substitute

```text
L_2=L_1=0, L_0=s,   E_2=c_2 Z eta^2,   D_2=c_1 Z eta^3,
2 c_2 C_2 = Z eta (3 c_1 s + c_5 eta).
```

To avoid denominators, carry `Cb_2 := 2c_2 C_2` and multiply each equation by
the smallest power of `2c_2` that clears it; record that power explicitly.

*Ideal.* `I` = the ideal generated by all `Z`-coefficients of
`[A^n]O` (`n=0,1,2`), `[A^n]E` (`n=1,2,3`), and `[A^0]E - kap`, inside
`Q[all coefficient symbols, c_1, c_2, c_5, kap]`.

*Decision.* Compute `Isat = I : (c_1 c_2 kap eta_e)^infinity`, where `eta_e` is
the top coefficient of `eta`. Report `EMPTY` iff `Isat = (1)`. Per the frozen
`sat()` convention: extract the ideal component of the returned object, assert
its ring by name and generator order before use, and reject any `?`-style
batch error.

*Box.* `e in {0,1,2}`, `sig in {0,...,4}`, `N in {3,...,6}`; also run the
branch `F=G=0` of Proposition 6.1 separately, i.e. with
`E_1 = E_2'`, `D_1 = D_2'` substituted, where the free data collapses to
`eta, s, C_0, C_1, D_0, E_0`.

*Controls (both mandatory).*
- *Negative control.* Run the identical pipeline on cell `(3,1)`
  (`E_1=E_2=L_1=L_2=0`, `D_2=c' Z s^3` from §5.1) over the same box. Section 5
  proves it is empty, so the pipeline must return `EMPTY`; anything else means
  the pipeline is wrong, not that Section 5 is.
- *Positive control.* Adjoin level-3 unknowns `C_3, D_3, E_3, L_3` of degree
  `<= N` and drop the truncation. Theorem 3.2 guarantees solutions exist, so
  the pipeline must return `NONEMPTY`; an `EMPTY` here means the model or the
  saturation is over-constrained.

*Reading the verdict.* `EMPTY` on the whole box is **evidence only**: the
degrees of `eta, s, C_i, D_i, E_i` are not bounded by anything promoted, so no
finite box can prove `OBSTRUCTION[A-DEGREE-TWO]`. `NONEMPTY` anywhere is a live
counterexample-search cell at degree 8 and must be lifted to an exact witness
`(P,Q,R_0,S_0)`, re-verified directly in `E=kappa, O=0`, and flagged
immediately.

## 9. Open items, typed

```text
OPEN[A2-CELL-32]
```
Cell `(alpha,beta)=(3,2)` of the census (4.3). Rigidified in Section 6 down to
eight polynomials and seven equations, with `C_2, D_2, E_2` pinned by
`(eta,s,c_1,c_2,c_5)` and `L_1=L_2=0`. The `beta | alpha` descent of §5.3 is
unavailable because `2` does not divide `3`. The most promising closing point
is `[A^1]O`: its Bezout compensator `8(C_2 r' - p' E_2)` is no longer free
there, so it is now a constraint linking the level-2 profile `(eta,s)` to the
residue data `(p,q,r,s)` and to `(C_1,E_1)`.

```text
OPEN[A-DEGREE-TWO]
```
The headline claim. It is now exactly `OPEN[A2-CELL-32]`: cells `(3,1)` and
`(2,1)` are closed unconditionally, and the census (4.3) is exhaustive.

```text
OPEN[A-DEGREE-D-CENSUS]
```
The general layer. At `deg_A <= d` one has `alpha, beta <= d+1` and the same
`Aff_2` normal form `alpha > beta >= 1`, so the census has `binom(d+1,2)` cells.
The §5.3 descent needs `g^{alpha/beta}` to stay inside the class, and the class
is **not** multiplicatively closed: for `g` of `A`-degree `0`, `g^k` has
`A`-degree `2*floor(k/2)`, so the descent is licensed only when
`2*floor((alpha/beta)/2) <= d`. That is automatic for `d=2` but must be checked
cell by cell for `d >= 3`. Do not extend §5 by analogy.

```text
OPEN[Z-ONLY-STRENGTHENING]
```
Lemma 4.1 handles `Q_f=0`, `deg_A P_f = 0` with `g` unbounded. Whether the same
`L_n` recursion closes `f` of `A`-degree `0` with `Q_f != 0` and `g`
unbounded is untested; if it does, `theta:(3.2)` upgrades from a two-sided cap
to a one-sided one.

Everything else stays where the frozen packets left it:
`OPEN[THETA-EXPLICIT-PULLBACK]`, `OPEN[THETA-TARGET-B]`,
`OPEN[THETA-STAGE0-MARKED-SNC]`, `Theta_f, Theta_g` UNCOMPUTED, no partition
row selected. Nothing in this report touches the rank-four field degree, the
boundary curve, the cusp/node census, or the general-fibre interfaces.

Execution gaps disclosed: no CAS was run, so every identity above is hand
derivation plus the displayed controls; SPEC-1 is the intended independent
check of the coefficient laws (3.1), (3.2), (6.2), (6.4) and of the
`[A^5]E`-vs-(N0) collapse.

## 10. Successor

1. Attack `OPEN[A2-CELL-32]` at `[A^1]O` with `C_2, D_2, E_2` pinned, using
   Proposition 6.1 to split into the two branches `F=G=0` and
   `phi = gamma + e`. This is a bounded desk task, not a search.
2. Run SPEC-1 first (it validates the machinery), then SPEC-2 with both
   controls. Treat any `NONEMPTY` as a degree-8 counterexample-search cell and
   escalate before continuing.
3. Re-pose the all-degrees thread for the coordinator. Corollary 3.3 says the
   one-cusp horn induction is **not** a leading-term induction and never can
   be; it is a termination statement for the Theorem 3.2 recursion. The
   `integration:§2` disproof-side entry "the one-cusp constraint system
   (degree-8 reframe) as the sharpest typed search space" should carry that
   correction, together with the `(T,V)` chart, which makes the search space a
   pole-order problem at one divisorial place rather than an `A`-adic one.

<!-- BODY-END -->
