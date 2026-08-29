# Residue A: simultaneous two-parent substitution transport

Date: 2026-08-28  
Producer: `/root/mixed_root_consequence_census` (GPT-5.6)  
Status: **EXACT CONDITIONAL SURVIVOR; NO RESIDUE-A CLOSURE**

## Executive verdict

The two Proposition 9.3 parent equations do not form a coefficient
discriminator.  For the two row-1 parents they are literally the same numerical
equation.

The first genuine coefficient test is the Puiseux substitution from the merge
to both parents.  On the **minimal genome** `m_{G_m}=1`, it can be carried out
exactly.  The result is not a contradiction: there is a coefficient-complete
leading seed over a finite algebraic extension of `K = Q(sqrt(3))`.  A literal
two-correction Laurent certificate below simultaneously produces both rigid
row-1 pole patterns, the rigid merge pattern, and compatible nonzero ODE
constants.

There is no such cyclic certificate over `K` itself.  This is only a descent
obstruction, not a Jacobian-conjecture obstruction, because the ambient
coefficient field is `C`.

The result is **conditional on `m_{G_m}=1`**.  Current canonical state also has
three live `m_{G_m}=2` genomes: `(k_1,l_1)=(2,3),(2,5),(1,2)`.
For those branches the terminal reduced `q` belongs to `h_2`, not `h_1`.
The pole-side `h_1=g^2-s_0f^3` identity used below is automatic there and does
not distinguish them.  Therefore this report neither kills residue A nor
provides a coefficient-complete seed for every surviving genome.

## Scope and firewalls

- No canonical ledger was edited.
- No `jc2-lean` path was entered, listed, searched, read, built, modified,
  statused, or controlled.
- Local computation was limited to the existing exact
  `cases/l1_ode_check.py` run (`0.3 s`) and desk algebra.  No CAS was available
  or needed; no AWS job was needed.
- Every use of Statement 3.9 below requires an auxiliary-`h`-suitable common
  refinement.  The load-bearing rider is explicit in `SIGRAY-AUDIT.md:39-40`.
  The literal Laurent certificate is stronger evidence than merely pretending
  an arbitrary already-chosen `kappa` is simultaneously suitable, but it is
  still only a local formal certificate.
- `mu_edge,i=1` below means the multiplicity of an incoming reduced `p` root.
  Sigray's approximate-root exponent is written `mu_app`; on the minimal
  genome it is `mu_app=3/2`.  These are different quantities.
- The historical two-pole exhibit prints pole `M=2` at
  `SHEET6-2POLE.md:316`; the corrected canonical pole value is `M=1`, from
  `SHEET6-L1.md:88-101` and `SHEET6-A3L1-REVIEW.md:53-65`.

## Source perimeter

Primary statements were read on the printed/PDF pages:

| Source | Use |
|---|---|
| `refs/sigray_full.pdf`, pp. 14-15, St 3.9 | root multiplicity, leading-coefficient and degree transport; auxiliary-`h` rider |
| pp. 18-20, Prop 3.2 / St 3.17 / Prop 4.2 | edge orientation and approximate-root hierarchy |
| p. 25, Prop 5.3 | row-1 pole ODE, squarefreeness and coprimality |
| pp. 39-41, Prop 8.1 / St 8.2 | reduced ODE and factorization `p_h=p^k q` |
| p. 46, table (23) | row-1 `(2,3)` pole data |
| pp. 50-51, Prop 9.3 | the two edgewise numerical equations |

Canonical/generated evidence:

- `SHEET6-L1.md:68-101,266-313,356-378`: the rigid pole, merge and suffix
  patterns and the explicitly open substitution layer.
- `SHEET6-A3L1-REVIEW.md:210-243,318-331`: exact closed forms and suffix
  check.
- `SHEET6-2POLE.md:314-345`: residue-A numerical exhibit.
- `SHEET6-R6.md:1-3,17-32,121-161,163-225`: authoritative live
  `m_{G_m}=2` towers, their common ODE/moduli pin, and the fact that `q` moves
  to `h_2`.
- `cases/l1_ode_check.py:1-27,65-101,449-490`: exact merge/pole-independent
  ODE verifier.  The run reproduced `rho=3/5`, `sigma=3`, `pi=3/2`, `b=2`,
  and `ctilde=-9/5`.
- `ideation-20260828T1707Z-opus5.md:414-455`: `RIGID-TRANSPORT` proposal.
  This report repairs its implicit `m=1` assumption.

The sealed ideation/cross packet hashes were verified before use against
`xmodel/ideation-20260828T1707Z-cross-packet.md`.

## 1. Numerical parent match: symmetric and coefficient-free

For each row-1 pole parent,

```text
Q(P_i) = (D, deg p, nu, M, kappa-bar) = (2,2,2,1,5),
mu_edge,i = 1,  n_i = 5.
```

At the merge the reduced degrees are `(dp,dq)=(6,10)`.  Proposition 9.3
therefore gives, on both edges,

```text
6/10 = 1*(1+5)/(5+5),
D_merge = (2+5*2)/2 = 6,
kappa-bar_merge = (5+5)/2 = 5,
i_merge = 2.
```

There is no `a_i`, pole-root scale, or leading coefficient in these
equalities.  Re-running them twice cannot kill the cell.

## 2. The `m=1` issue: attempted promotion and exact failure

It is tempting to argue as follows.  If the first top relation is

```text
(g_F^+)^2 = s_0 (f_F^+)^3,
```

then, writing `f_F^+=(xi^delta P)^2`, unique factorization gives
`g_F^+=gamma (xi^delta P)^3`, `gamma^2=s_0`.  For
`h_1=g^2-s_0f^3`, the full transformed identity is

```text
J(f_F,h_{1,F}) = 2 g_F xi^{-u}.
```

Its first possible nonzero term has the same exponent and polynomial shape as

```text
(f_F^+)^(3/2) xi^{-u}
  = xi^(3 delta-u) P^3.
```

This **does not prove** that the bracket of the two leading patterns
`J(f_F^+,h_{1,F}^+)` is nonzero.  A higher leading part of `h_{1,F}^+` may be
a pure power of `P`, have zero bracket with `f_F^+`, and leave the displayed
nonzero term to lower `xi` layers.  That is precisely Proposition 4.2's
continuation alternative.

`SHEET6-R6.md` supplies literal surviving instances:

| genome | `h_1` at `G_m` | terminal member carrying `q` |
|---|---|---|
| minimal, `m=1` | `P q` | `h_1` |
| `m=2`, `(2,3)` | scalar `P^3` | `h_2=P^4 q` |
| `m=2`, `(2,5)` | scalar `P^5` | `h_2=P^6 q` |
| `m=2`, `(1,2)` | scalar `P^4` at its staged level | `h_2`, with dead-member datum `P q` |

Thus `m_{G_m}=1` is not forced.  In the remainder it is an explicit genome
assumption.  Under that assumption, `mu_app=3/2`, `i=2`, and

```text
k = i*(mu_app-1) = 2*(3/2-1) = 1,
```

so Proposition 8.1(ii) identifies the terminal pattern as `p_{h_1}=P q`.

## 3. Rigid normalized merge

Put `r=sqrt(3)` and work first over `K=Q(r)`.  Fix the scale `sigma=3`:

```text
a_+ = (3+r)/2,     a_- = (3-r)/2,     b=2,
t=z^3,
P(z)=(t-a_+)(t-a_-)=z^6-3z^3+3/2,
R(z)=z(t-2),
q(z)=P(z)R(z)=z P(z)(z^3-2).
```

All roots are nonzero and simple, `a_+ != a_-`, and `b` is neither `a_+`
nor `a_-`.  Direct expansion gives the exact reduced ODE certificate

```text
(3/5) P q' - P' q = (-9/5) P.                 (M-ODE)
```

For a chosen direction representative `c_i^3=a_i`, define

```text
d_i := P'(c_i) = 3 c_i^2(a_i-a_j)
     = +3 r c_+^2  or  -3 r c_-^2.
```

Since `q=P R`,

```text
e_i := q'(c_i) = d_i R(c_i)
     = 3 a_i(a_i-a_j)(a_i-2) = 9/2             (E)
```

for **both** signs.  The last equality is elementary:
`a_+(a_+-2)=r/2` and `a_-(a_--2)=-r/2`.

## 4. Literal simultaneous substitution certificate (`m=1`)

### 4.1 Coefficient field and the square-root congruence

The common first correction must solve

```text
A(z)^2 == -(4/3) R(z)  (mod P(z)).              (SQUARE)
```

This equation is simultaneous: one polynomial `A` is evaluated on both
incoming cubic root orbits.

An explicit solution field is

```text
L_0 = K(i,u),        i^2=-1,       u^2=3+2r.
```

Set

```text
s_- = (2/3)u,
s_+ = i(2-r)s_-,
S(t) = s_- + (s_+-s_-)*(t-a_-)/(a_+-a_-),
A(z) = z^2 S(z^3).
```

Then

```text
s_i^2 = -(4/3)*(a_i-2)/a_i,
```

and, at `t=a_i`,

```text
A(z)^2 = z^4 s_i^2 = z a_i s_i^2
       = -(4/3) z(a_i-2) = -(4/3)R(z).
```

Because `P=(t-a_+)(t-a_-)` is squarefree, this proves `(SQUARE)`.
Consequently

```text
C(z) := (R(z)+(3/4)A(z)^2)/(2P(z))
```

is a literal polynomial in `L_0[z]`.  This quotient is the division
certificate; no denominator vanishes on either orbit.

### 4.2 Two-correction Laurent certificate

Use the common ramified parameter `Z=x^(1/42)`.  The merge has
`kappa=21`, the row-1 parent has twice that denominator, and Proposition
9.3 has `n=5`.  Thus the parent coordinate is

```text
z = c_i + Z^(-5) eta.
```

Define the following exact truncated Laurent pair:

```text
f_* = Z^12 P^2 + Z^2 A,
g_* = Z^18 P^3 + (3/2) Z^8 P A + Z^(-2) C.
```

The exponent-26 terms of `g_*^2` and `f_*^3` cancel.  At the next common
exponent,

```text
g_*^2-f_*^3
 = Z^16 P^2 R
   + Z^6 (3 P A C-A^3)
   + Z^(-4) C^2.                                (H-CERT)
```

The first term is exactly the minimal-genome merge pattern
`p_{h_1}=P q=P^2R`.  This is the requested literal substitution certificate,
not just a repeated Q-ratio equation.

### 4.3 Both row-1 parents from the same `A`

Choose `c_i^3=a_i` and put

```text
W_i := -A(c_i)/d_i^2.
```

Substitution in `f_*` and `g_*` gives the parent leading polynomials

```text
F_i(eta) = d_i^2 (eta^2-W_i),
G_i(eta) = d_i^3 eta (eta^2-(3/2)W_i).           (POLE)
```

Thus `W_i` is the square of the usual pole-root scale.  Every lower
coefficient is present; the two parent patterns are not independently made
monic and then compared after the fact.

From `(SQUARE)` and `e_i=d_iR(c_i)=9/2`,

```text
d_i^5 W_i^2 = -6.                               (MATCH)
```

The row-1 pole ODE is therefore

```text
2 F_i G_i' - 3 F_i' G_i = 3 d_i^5 W_i^2 = -18  (P-ODE)
```

for **both** parents.  The two pole constants agree; they are not asserted
to equal the reduced merge constant `-9/5`.  The factor between them is a
normalization/transport factor, not an inconsistency.

Finally, the pole `h_1` pattern is

```text
H_i := G_i^2-F_i^3
     = d_i^6 W_i^2 (W_i-(3/4)eta^2)
     = d_i*((9/2)eta^2-6W_i).                   (H-POLE)
```

Its leading coefficient is `(9/2)d_i=d_i e_i`, exactly the coefficient of
`(z-c_i)^2` in `Pq`.  This is the Statement 3.9 leading-coefficient match for
`h_1`; the `f` and `g` matches are respectively `d_i^2` from `P^2` and
`d_i^3` from `P^3`.

### 4.4 Field eliminants and side conditions

The two parent coefficients obey

```text
(W_+/W_-)^6 = -(a_-/a_+)^10 = -(2-r)^10.        (ELIM-W)
```

If literal pole roots `theta_i` are adjoined with `theta_i^2=W_i`, then

```text
(theta_+/theta_-)^12 = -(2-r)^10.               (ELIM-ROOT)
```

This polynomial has nonzero, separable roots in an algebraic closure: its
constant is nonzero and its derivative cannot vanish at a nonzero root.
Likewise, choose any nonzero cube roots `c_i` and use the displayed formula
for `W_i`; all denominators are nonzero because
`a_i`, `a_i-a_j`, `a_i-2`, `c_i`, and `d_i` are nonzero.  The pole patterns
are squarefree and coprime: their squared nonzero root radii are `W_i` and
`(3/2)W_i`, while `0` occurs only in `G_i`.

There is no descent to `K` in this normalization.  Indeed

```text
s_+^2/s_-^2 = -(2-r)^2.
```

If both correction values lay in the real field `K`, this would make `-1`
a square in `K`.  Equivalently, taking cubic norms of `(SQUARE)` on the two
components gives a ratio `-(2-r)^2`, again not a square in the real quadratic
field.  This explains, rather than contradicts, the explicit adjunction of
`i` above.

The direction representatives themselves also need an extension: if
`c_+` were in `K`, then
`Norm_K/Q(c_+)^3=Norm_K/Q(a_+)=3/2`, impossible because `3/2` is not a
rational cube.  None of these descent failures is fatal over `C`.

## 5. Why the certificate does not distinguish the live `m=2` towers

The pole identity

```text
g_i^2-s_0f_i^3
 = nonzero scalar * (eta^2-(4/3)W_i)
```

depends only on the row-1 pole ODE.  `SHEET6-R6.md:30-32,207-225` already
records exactly this degree-2 `h_1` pattern on the `(2,3)`, `(2,5)` and
`(1,2)` towers.  Hence it contains no information about `(k_1,l_1)`.

At `G_m` in those towers, `h_1` is still **alive** and has a pure-power
pattern.  The resonant factor `R` first appears in terminal `h_2`.  Imposing
`(SQUARE)` there would silently replace the `m=2` genome by the minimal
`m=1` genome.  It is therefore not licensed.

The corresponding `m=2` discriminator must start from

```text
h_2 = h_1^(k_1) - s_1 f^(l_1)
```

with the staged pure-power `h_1` coefficient retained, and derive the first
Laurent diagonal on which the `h_2` residual `P^k q` appears.  The three
branches require separate systems.  R6's exact echo calculation shows that
the common ODE constraints `b=2 sigma/3` and `a_1a_2=sigma^2/6` are absorbed,
not contradictory.

## 6. Exact next jet datum not fixed here

Even on the minimal genome, `(H-CERT)` is a leading formal seed, not a full
Keller germ.  It has not imposed the full equation `J(f,g)=1` beyond the
already-checked reduced ODE.

Write a full merge expansion as

```text
f = sum_j Z^j f_j(z),       g = sum_j Z^j g_j(z).
```

After `z=c_i+Z^(-5)eta`, a Taylor coefficient of order `r` in the
`Z^j` layer contributes on the parent diagonal `j-5r`.  The certificate
fixes the complete leading diagonals `2` for `f`, `3` for `g`, and `6` for
`h_1`.  The first unpinned parent-jet polynomials are therefore exactly

```text
F_i^[1](eta) = sum_(j-5r=1) f_j^(r)(c_i)/r! * eta^r,
G_i^[1](eta) = sum_(j-5r=2) g_j^(r)(c_i)/r! * eta^r,
H_i^[1](eta) = sum_(j-5r=5) h_{1,j}^(r)(c_i)/r! * eta^r.
```

These are the coefficients of `Z^1`, `Z^2`, and `Z^5`, respectively,
immediately below the displayed pole-leading coefficients `Z^2 F_i`,
`Z^3 G_i`, and `Z^6 H_i`.  Neither Proposition 9.3 nor Statement 3.9 fixes
them; Statement 3.9 fixes only the top corner of a leading diagonal.
Moreover `H_i^[1]` is not independent: it must be the coefficient induced
from `F_i^[1]` and `G_i^[1]` by `h_1=g^2-f^3`.

Those three diagonals must now be solved simultaneously for `c_+` and `c_-`,
with

```text
h_1=g^2-f^3
```

and the next nonzero coefficient of the transformed Jacobian imposed before
elimination.  A source theorem specifying the allowed cyclic characters of
the omitted `f_j,g_j` layers would turn these displayed sums into a finite
coefficient system; no such statement is currently pinned in the residue-A
artifacts.

For an exact lift implementation, use `(SQUARE)` as the seed ideal, replay
`(H-CERT)` by direct substitution, introduce the next omitted `f` and `g`
Laurent polynomials with the required cyclic characters, and eliminate only
after both parent substitutions have been imposed.  A unit ideal would kill
the minimal genome; a reduced point or smooth component would extend this
seed.  The `m=2` genomes need their own `h_2` versions first.

## 7. Scope-correct conclusion

| target | result |
|---|---|
| two Proposition 9.3 row-1 equations | identical; no coefficient content |
| minimal `m_{G_m}=1` simultaneous parent transport | **SURVIVES**, with the explicit `A,C,f_*,g_*` certificate |
| descent of that normalized certificate to `Q(sqrt(3))` | **NO**; finite complex extension required |
| live `m_{G_m}=2` branches | **NOT DISTINGUISHED** by the `h_1` calculation |
| whole residue-A panel | **OPEN** |

The clean next proof/disproof task is therefore not another Q-level parent
match.  It is either (a) the next Jacobian jet of the explicit minimal seed,
or (b) preferably, the three staged `h_2` substitution systems for the live
`m=2` genomes, because those are outside the certificate proved here.

## Seal note

The immutable SHA-256 of this report is printed in the producer handoff after
the final byte-level audit; it is intentionally not self-embedded.
