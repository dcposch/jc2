# `(8,12)` order-four/order-two coefficient-infinity source audit

Date: 2026-08-25  
Status: **EXACT SOURCE REDUCTION / STRICT-REES DESIGN; NO SATURATION
VERDICT**

## Verdict

The live nontrivial Kummer clients of the unbounded-total partial-`y`
`(8,12)` cell have enough reviewed source structure to identify their
coefficient-infinity exceptional fibre.

Let the monic leading core have degree

```text
h in L[x],       H=deg h=4U,       u^4=h,
```

and let the class of `h` in `L(x)^*/L(x)^{*4}` have order `e=4` or
`e=2`.  After the reviewed target gauges, the two high-row forms are

```text
e=4:  g=F_12(f),
e=2:  g=F_12(f)+k_10 F_10(f)+k_6 F_6(f)+k_2 F_2(f),
```

where `f` is monic depressed of degree eight.  In the `e=2` client the
three lower Faber constants have positive weights `2,6,10`.  The first
seven tails have weights `13,...,19`.  At every surviving coefficient-
infinity place (`U>=2`) all target loads are regular.  Consequently, after
the charged Rees scaling, every lower Faber term and every target load
vanishes on the exceptional divisor.  On a selected unramified sheet the
seven exceptional equations are **exactly**

```text
r_1(f,F_12(f))=...=r_7(f,F_12(f))=0.                 (0.1)
```

The other sheets are its weighted `mu_e` orbit.  Thus the now-confirmed
general Faber--Mason theorem applies, and the reduced exceptional support
in both `e=4` and `e=2` clients is exactly

```text
K=z^4+p z^2+c z+r,       f=K^2,       g=K^3,          (0.2)
```

projectively `P(2,3,4)`.  This is a reduced-support theorem, not a
statement that the seven-tail ideal is reduced and not an exclusion of a
strict arc.

There are two important differences from cyclic D1 `(9,12)`.

1. The bounded-pole sector has exact total degrees

   ```text
   (deg P,deg Q)=(8(U+1),12(U+1)),
   gcd(deg P,deg Q)=4(U+1).                           (0.3)
   ```

   The classical necessary bound `gcd>=16` for a counterexample closes
   this sector only for `U<=2`.  For `U>=3`, both the bounded-pole sector
   and the strict sector remain live.  One must not copy the D1 inference
   that every client is strict.

2. The terminal tail equation is

   ```text
   8 r_7'=j/u,       j!=0.                            (0.4)
   ```

   If `U=1`, then `dx/u` has a nonzero logarithmic residue at every place
   above `x=infinity`, whereas `d r_7` is exact.  Hence both nontrivial
   Kummer clients with `H=4` are empty before any Rees calculation.  The
   first coefficient-infinity clients that can survive this local test
   have `U>=2`.

No source-typed `(8,12)` full-fibre/Rees compiler currently exists in the
repository.  The reviewed artifacts stop at the universal high-row
integration and two-tail control.  Sections 4--7 below give the exact
compiler contract; a computational verdict still requires emitting and
hashing the seven raw descended tails for a fixed `h` and running the full
saturation on AWS.

## 1. Inventory: what exists and what does not

The relevant frozen/reviewed artifacts are:

| Artifact | SHA-256 | Licensed input |
|---|---|---|
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | residual condition `4|H`; orders `4,2,1`; depression and charged Taylor boundaries |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` | hostile confirmation, including the genuine order-two leaf and monic-core qualification |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | complete high-row Faber landing; target quotient; widths |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | different-model confirmation of that landing |
| `xmodel/max12-general-faber-exceptional-support-mason-20260825.md` | `7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919` | ordinary unloaded seven-tail reduced support |
| `xmodel/max12-general-faber-exceptional-support-mason-review-20260825.md` | `c95524a0a63ea4ab5cfa69eb26799279f330575c0b16f836a46180ebb826c292` | independent exact proof |
| `xmodel/max12-general-faber-exceptional-support-mason-review-grok-20260825.md` | charged target hash `7d5271e8...` and verdict `CONFIRMED` | different-model hostile confirmation |

Repository inventory found no case directory or compiler for a global
`(8,12)` lower fibre, an order-four or order-two Taylor realization, or an
`(8,12)` coefficient-infinity saturation.  In particular, the D1
`compile_gate_v2.py` and its descended tails are type-specific and are not
consumed here.  The fixed-total B8/Artin--Schreier cases are also not this
unbounded-total partial-`y` client.

## 2. Exact Kummer normalization and high-row loads

After harmless nonzero target scalings, the leading coefficients are

```text
[y^8]P=h^2=u^8,       [y^12]Q=h^3=u^12.
```

The reviewed next-row identity and nontrivial Kummer character kill the
depression mismatch.  Hence

```text
z=u(y+R_0),
f(z)=z^8+sum_(i=0)^6 a_i z^i.                         (2.1)
```

Here `R_0` is invariant under the Kummer group.  The coefficient of `y^7`
in `P=f(u(y+R_0))` is

```text
[y^7]P=8u^8R_0=8h^2R_0.                              (2.2)
```

Taylor polynomiality therefore makes `R_0` rational on the base and gives
it finite poles only over zeros of `h`.  Subtracting its polynomial part
at infinity by the source automorphism `(x,y)->(x,y-q(x))` changes only
`R_0`; it leaves `f`, all `a_i`, the Kummer class, and the Keller property
unchanged.  We henceforth take `R_0` regular at infinity.

Let

```text
w=f^(1/8),
H_F(T)=sum_(j=0)^12 h_j T^j,
H_F(w)-g(z(w))=sum_(ell>=1) r_ell w^-ell.             (2.3)
```

The reviewed universal differential identity gives

```text
r_1'=...=r_6'=0,       8r_7'=j/u.                    (2.4)
```

The Kummer character determines the complete allowed load pattern.  If a
generator sends `u` and `z` to `zeta u` and `zeta z`, then `r_ell` has
character `zeta^ell`.  Differential constants are fixed scalars.  Thus

```text
e=4: (r_1,...,r_7)=(0,0,0,mu_4,0,0,R_7),
e=2: (r_1,...,r_7)=(0,mu_2,0,mu_4,0,mu_6,R_7),       (2.5)
```

where `R_7'=j/(8u)` and `R_7` has character `7 mod e`.

The same character filter on the Faber constants, followed by the three
reviewed target gauges at indices `8,0,4`, gives exactly

```text
e=4: H_F(w)=w^12,
e=2: H_F(w)=w^12+k_10 w^10+k_6 w^6+k_2 w^2.          (2.6)
```

No mod-four filter may be imposed on the order-two leaf.  Its three
surviving constants are genuine and must be present away from the Rees
boundary.

## 3. Infinity ramification, the terminal residue, and the bounded split

Put `q=1/x`.  Because `h` is monic of degree `4U`, every place of the
Kummer normalization above `q=0` is unramified.  On a selected sheet put

```text
t=q^Uu,       t(0)=1.                                 (3.1)
```

For the order-four client,

```text
t^4=q^(4U)h(q^-1),
```

whose right side is a unit congruent to one.  For the order-two client,
write `h=v^2` with `v` monic and not a square, choose `u^2=v`, and use

```text
t^2=q^(2U)v(q^-1).
```

Again the right side is a unit congruent to one.  Thus `q` is a uniformizer
on every selected sheet; no fractional valuation is hidden at infinity.
The other sheets are obtained by `t->zeta t`, with `zeta in mu_4` or
`mu_2`.

Equation (2.4) becomes

```text
dR_7/dq=-(j/8) q^(U-2)t^-1.                           (3.2)
```

For `U=1`, the right side has residue `-(j/8)t(0)^-1`, which is nonzero.
The differential of a rational function on a smooth curve has zero residue
at every place.  This contradicts the fact that `R_7` is a Faber-tail
function in the Kummer function field.  Hence `H=4` is impossible on both
nontrivial classes.  For `U>=2`, (3.2) is regular and `R_7` is regular at
infinity.  This proves the regular-load assertion used in the Rees fibre.

The same exactness condition is a useful global prefilter.  In particular,
at a finite zero of `h` of multiplicity exactly four, a local normalization
again makes `dx/u` have a nonzero logarithmic residue, so that divisor
profile is impossible.  Vanishing of residues is only necessary: the full
condition is that the rational differential `dx/u` be exact on the Kummer
curve.

Now let

```text
d_i=max(0,-ord_q(a_i)),       0<=i<=6.                (3.3)
```

The unit twist `t` does not change these pole orders.  Suppose

```text
d_i <= (U+1)(8-i)       for every i.                 (3.4)
```

Since `R_0` is regular, a term indexed by `i` in `[y^ell]P` has pole order
at most

```text
d_i+Ui <= (U+1)(8-i)+Ui=8(U+1)-i<=8(U+1)-ell.
```

Taylor membership puts the coefficient in `L[x]`, so `deg P<=8(U+1)`.
The term `[y^8]P=h^2` has `x`-degree `2H=8U`, and therefore total degree
exactly `8(U+1)`.

For `Q`, use the exact grading

```text
wt(z)=1,       wt(a_i)=8-i,       wt(k_j)=12-j.       (3.5)
```

Every monomial contributing to the `z^s` coefficient of the full (2.6)
has total weight twelve.  The `k_j` are finite scalars, so (3.4) bounds its
pole order after `z=u(y+R_0)` by

```text
12(U+1)-s-(U+1)sum_j e_j(12-j)
 <=12(U+1)-s.                                         (3.6)
```

Thus `deg Q<=12(U+1)`, while `[y^12]Q=h^3` gives equality.  This proves
(0.3).

The classical GGV/Heitmann necessary condition for a counterexample now
has the exact consequence

```text
U=1 or 2: bounded sector (3.4) is counterexample-closed;
U>=3:     (3.4) is degree-identified but not classically closed.       (3.7)
```

The `U=1` nontrivial clients were already excluded more strongly by
(3.2).  For `U=2`, every possible counterexample must satisfy

```text
alpha:=max_i d_i/(8-i)>3.                             (3.8)
```

For `U>=3`, the strict sector `alpha>U+1` is only one part of the client;
the complementary bounded sector remains charged.

## 4. Exact character descent and ordinary-sheet identification

Work over a characteristic-zero constant extension containing the needed
roots of unity.  Let `[a]_e` denote the least residue of `a` modulo `e`.
With the convention that the deck generator sends `t->zeta t` and
`z->zeta z`, write

```text
a_i=t^[-i]_e A_i(q).                                  (4.1)
```

Every `A_i` is invariant.  For the order-two leaf this is just the even/
odd decomposition; for the order-four leaf it is the full four-character
decomposition.  Define the raw descended tail by

```text
D_ell(q,A,k)=t^[-ell]_e
             r_ell(t^[-i]_e A_i,k).                  (4.2)
```

Faber equivariance makes (4.2) invariant, so it lies in the base function
field; powers `t^e` are replaced by the displayed base unit.  If
`gamma_ell` denotes the target in (2.5), put

```text
delta_ell(q)=t^[-ell]_e gamma_ell(q).                 (4.3)
```

The only nonzero constant targets occur at multiples of `e`, so their
twist is one.  The terminal `delta_7` is invariant and regular for `U>=2`.

Equivalently, retain the etale unit `t` and use the ordinary coefficients

```text
C_i=t^[-i]_e A_i.                                    (4.4)
```

Then the seven descended equations `D_ell=delta_ell` are carried by an
invertible etale/unit change of coordinates to the ordinary equations
`r_ell(C,k)=gamma_ell`.  At `q=0` on the selected `t(0)=1` sheet,
`C_i=A_i`.  On another sheet the equations are carried to the first by the
weighted deck action.  This proves, without borrowing a D1 compiler, that
vanishing of the descended exceptional rows is exactly vanishing of the
ordinary rows.

The induced deck action on the common-quartic parameters is

```text
e=4: (p,c,r)->(zeta^2 p,zeta^3 c,r),
e=2: (p,c,r)->(p,-c,r).                               (4.5)
```

This is the weight `(2,3,4)` action reduced modulo `e`.

## 5. The exact strict-Rees gate

Faber homogeneity gives

```text
r_ell(lambda^(8-i)a_i,
      lambda^2 k_10,lambda^6 k_6,lambda^10 k_2)
 =lambda^(12+ell)r_ell(a,k).                          (5.1)
```

The `k` arguments are omitted in the order-four client.  Normalize
coefficient infinity by

```text
B_i=Lambda^(8-i)A_i.                                  (5.2)
```

The exact descended Rees equations are

```text
Phi_ell=
D_ell(q,B,Lambda^2 k_10,Lambda^6 k_6,Lambda^10 k_2)
-Lambda^(12+ell)delta_ell(q)=0,       1<=ell<=7.      (5.3)
```

For `e=4`, delete the three `k` arguments.  Since all `delta_ell` are
regular and all displayed exponents are positive, setting
`q=Lambda=0` in (5.3) gives exactly the ordinary unloaded system (0.1).
This is the promised source-typed identification; it is not merely an
analogy with `(9,12)`.

For a rational coefficient pole let

```text
alpha=max_i d_i/(8-i)=m/n>U+1,       gcd(m,n)=1.
```

On `q=epsilon^n`, take `Lambda=epsilon^m`.  The single algebraic chart

```text
Lambda=q^(U+1)rho                                      (5.4)
```

encodes every strict slope by
`rho=epsilon^(m-(U+1)n)->0`.  Substitution in (5.3) gives

```text
Psi_ell=
D_ell(q,B,
      q^(2(U+1))rho^2 k_10,
      q^(6(U+1))rho^6 k_6,
      q^(10(U+1))rho^10 k_2)
-q^((U+1)(12+ell))rho^(12+ell)delta_ell(q).           (5.5)
```

Again the `k` arguments are absent for `e=4`.  With

```text
I=(Psi_1,...,Psi_7),
K_strict=I:(q rho)^infinity,
H_strict=(K_strict+(q,rho)):(B_0,...,B_6)^infinity,  (5.6)
```

one has the fail-closed implication

```text
H_strict=(1)  =>  no strict formal/Puiseux, hence no rational,
                   coefficient-infinity branch for that fixed source. (5.7)
```

Both `q` and `rho` must be saturated before the boundary is taken.  A
`rho`-unit branch has slope exactly `U+1` and must not be counted as strict.
Conversely, `H_strict!=1` gives only algebraic boundary accessibility.  It
does not produce a rational constant-field section or satisfy the Taylor
boundaries.

## 6. Common-quartic reduced support and chart/denominator audit

The confirmed general Faber--Mason theorem applied to (0.1) gives (0.2).
Expanding the square gives the exact triangular parametrization

```text
B_6=2p,
B_5=2c,
B_4=p^2+2r,
B_3=2pc,
B_2=c^2+2pr,
B_1=2cr,
B_0=r^2.                                              (6.1)
```

Thus the reduced exceptional cone is a prime copy of `A^3`, and its
weighted projectivization is `P(2,3,4)`.  Useful triangular normal
coordinates are

```text
p=B_6/2,       c=B_5/2,       r=(B_4-p^2)/2,
x_3=B_3-2pc,
x_2=B_2-c^2-2pr,
x_1=B_1-2cr,
x_0=B_0-r^2.                                          (6.2)
```

The reduced boundary is `x_3=x_2=x_1=x_0=0`; its irrelevant ideal is
`(p,c,r)`.  The normal variables in (6.2) must remain in the deformation
calculation.  Standard fail-closed projective coverage uses the three
charts `p!=0`, `c!=0`, and `r!=0`, imposed only after forming the interior
saturation (5.6).  Saturating by `pcr` alone loses every coordinate
boundary.

For a rational strict slope `m/n`, the active leading weights force

```text
n divides gcd({2 if p!=0},{3 if c!=0},{4 if r!=0}).  (6.3)
```

Consequently:

```text
p*c!=0 or c*r!=0:              n=1;
c=0, p!=0 (r arbitrary):       n divides 2;
p=r=0, c!=0:                   n divides 3;
p=c=0, r!=0:                   n divides 4.           (6.4)
```

This reduces denominators to at most four but leaves the numerator `m`
unbounded.  In lowest terms, `n=2` forces `m` odd, `n=3` forces
`gcd(m,3)=1`, and `n=4` forces `m` odd.  Under
`epsilon->omega_n epsilon`, the limiting quartic is fixed by the weighted
`mu_n` action precisely on the strata in (6.4).

The Rees ramification `n` and the Kummer order `e` are independent.  The
unit `t(q)` is unramified and becomes `t(epsilon^n)`; it introduces no new
fractional valuation.  The full local extension may have composite degree,
while the Kummer sheets continue to be related by (4.5).

## 7. Why reduced support is not an exclusion

At a common quartic write `f=K^2+E`.  At zero scaled Faber loads,

```text
f^(3/2)=K^3+(3/2)K E+(3/8)K^-1 E^2
         -(1/16)K^-3 E^3+... .                        (7.1)
```

The constant and linear terms are polynomials in `z`, so the differential
of the seven-tail map vanishes in every coefficient direction along the
whole common-quartic locus.  The derivatives in the three order-two load
directions also have zero tails:

```text
F_10(K^2)=K^5,       F_6(K^2)=K^3,       F_2(K^2)=K. (7.2)
```

Thus neither client is linearly transverse at its exceptional support.  A
fixed jet cannot replace the exact saturation without a separate finite-
determinacy theorem.  Scheme thickness, normal Kuranishi equations, and
the charged Taylor boundaries are the actual next obstruction.

## 8. Prioritized next gates

1. **Exact-differential prefilter, all `h`.**  Before any Gröbner work,
   test whether `dx/u` is exact on the order-four or order-two Kummer
   normalization.  The `H=4` and finite multiplicity-four residue
   exclusions above are immediate instances.  This can remove whole
   source profiles rather than individual coefficient branches.
2. **`U=2` strict saturation.**  Here the bounded sector is classically
   closed, so (5.6) is a complete remaining coefficient-pole gate for each
   source profile.  Emit independent order-four and order-two compilers;
   the latter must retain all three `k` loads and `mu_2,mu_4,mu_6`.
3. **`U>=3` two-lane attack.**  Run (5.6) on the strict sector while, in
   parallel, seeking a new obstruction for the exact bounded degrees
   `(8(U+1),12(U+1))`.  A strict-saturation success alone cannot close
   these clients.
4. **AWS implementation contract.**  Reconstruct and hash all seven raw
   tails; verify (4.2) monomial by monomial; verify (5.1); recover (6.1) as
   the boundary radical; test sequential saturation by `q` and `rho`;
   retain all loads as polynomial variables for a uniform theorem; cover
   the three projective charts after interior saturation; include a
   slope-`U+1` negative control and synthetic strict arcs on the `p`, `c`,
   and `r` strata.  Every CAS/solver run belongs on registered AWS, not on
   the local workstation.

## Scope firewall

This report proves the local source typing of the coefficient-infinity
exceptional equations and their reduced common-quartic support.  It proves
the exact bounded-pole degree formula, closes only its `U<=2` portion by
the cited classical necessary condition, and excludes the nontrivial
`H=4` clients by the terminal differential residue.  It designs, but does
not compute, the exact strict saturation.

It does not prove that the seven-tail ideal is reduced, exclude a strict
arc for `U>=2`, solve the bounded sector for `U>=3`, classify the exact
differential condition globally, discharge either Taylor-boundary family,
turn a Puiseux arc into a rational trajectory, close the order-one leaf,
close the whole `(8,12)` cell, close maximum twelve, or prove/disprove JC2.
