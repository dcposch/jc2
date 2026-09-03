# GLOBAL-INTERPOLATION — exact all-branch conditions and a target-independent finite-order algorithm

**Lane/date.** `GLOBAL-INTERPOLATION`, 2026-09-03.  **Status of new work:**
`PROVED-HERE / UNREVIEWED` unless a narrower type is printed.  This report does
not edit a canonical ledger and does not use `jc2-lean`.

## 0. Custody, scope, and verdict

The mandatory hash gate was run before any frozen input was opened.  All six
values matched the charge exactly:

```text
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  time-function-endgame-review-sol56-20260902.md
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  time-function-calibration-d48-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
437c5b45facf61e8e24d5399da50d131310b360f8184667a25c7388c6941c09e  bottom_star.py
```

Consumed from the reviewed input are JAC-FIBRE, D1-PIN, D1-STAR, and the
reviewed form of LOCAL-KELLER/BOTTOM-ODE.  In particular, for
`c=[f,g] in C*` and every simple root `tau_i` of a generic fibre `g-c_2`,

```text
       d/dx f(x,tau_i(x)) = c/g_y(x,tau_i(x)).                 (JF)
```

The exact global answer is as follows.

1. The Lagrange coefficients are the symmetric expressions (1.4) below.
   Equivalently, they are triangular transforms of the moments (1.5).
2. There is an off-by-one in the wording of the charge.  Killing
   `y^(m+1),...,y^(n-1)` gives **`n-m-1`** homogeneous linear identities.
   The total is `n-m` only after the monic normalization `[y^m]f=1` is added.
3. After those identities, the remaining `m+1` coefficients must lie in
   `C[x]=C[t^-1]`.  This means that every positive `t`-coefficient vanishes;
   before Galois descent it also means that every fractional `x`-power
   vanishes.
4. A complete Galois orbit makes the fractional-power cancellation automatic,
   and makes conjugate local equations repetitions.  It does **not** kill an
   invariant integer-order coefficient.  Such coefficients still sum across
   different branch orbits and through every level of the tree.
5. NO-RESIDUE is the logarithmic block of this same global system.  It is
   implied by the conjunction of the high-degree equations and polynomiality
   if logarithms are retained in the coefficient ring.  It is not implied by
   the lower-coefficient test alone, and it must be imposed first if one works
   only in the Puiseux field.
6. A count depending only on `(n,m,M_*,V_*,delta_*,u,v)` does not exist: that
   tuple omits the attained bottom-disc packet, the Galois-orbit partition,
   coefficient sharing, and the tame exponent support.  Exact closed formulas
   are given in section 4 for the minimally **decorated skeleton**.  Any count
   attached to the bare tuple would silently assume the very branch-packet
   information that integration #17 and its review leave open.

The implementation is
`box/globalinterp-drivers-20260902/globalinterp.py`.  It performs exact
truncated Laurent arithmetic, emits an existentially equivalent quadratic
lift, and contains all charged positive controls and a target-independent
negative control.

## 1. The exact global interpolation conditions

### 1.1 Field, roots, primitives, and the target qualification

Put `t=x^-1`.  Fix a generic target `c_2`, and write

```text
 G(x,y) := g(x,y)-c_2 = product_(i=1)^n (y-tau_i(x)),
 D_i    := G_y(x,tau_i) = product_(j != i)(tau_i-tau_j).
```

The polynomial is monic of `y`-degree `n` and the generic fibre is separable.
Choose one common Puiseux field `K=C((t^(1/R)))` containing all roots.  Define

```text
       R_i(x) := c/D_i(x),             F_i'(x)=R_i(x),
       H_i(x) := F_i(x)+a_i.                                  (1.1)
```

Here `a_i` is constant in `x`; section 2 determines which `a_i` are actually
independent.  Initially the primitive may be taken in
`K[log x]`.  Section 3 extracts the exact condition for it to lie in `K`.

There are two logically different uses of what follows.

* **Fixed-target theorem.**  For one generic `c_2`, the conditions below are
  necessary and sufficient for the `H_i` to be the restrictions of a unique
  polynomial in `y` of degree at most `m` whose coefficients are in `C[x]`.
  They imply `[L,g]=c` on that fibre.  They do not, from one numerical target
  alone, prove a two-variable Jacobian identity.
* **Condition on `g` alone across targets.**  Take `c_2=s` transcendental and
  run the same construction over `C(s)`.  After fixing the harmless common
  additive constant, require the recovered coefficients to be independent
  of `s`.  Equivalently, coefficients of `y^j`, `j>=1`, are independent of
  `s`, and the constant coefficient may differ by a function of `s` which is
  removed by subtracting the same constant from all `H_i`.  Then the fibre
  identities hold on a Zariski-dense family and give `[L,g]=c` identically.

The charged lane asks for necessary conditions on a Keller pair, so the first
use already answers (1)-(2).  The second qualification is required before a
finite target computation is advertised as a sufficient `g`-alone Keller
test.

### 1.2 Symmetric coefficient formula

Let

```text
 e_r^(i) := e_r(tau_1,...,hat(tau_i),...,tau_n),
 ell_i(y):= product_(j != i)(y-tau_j)/(tau_i-tau_j).
```

The unique interpolant of `y`-degree `<n` is

```text
 L(x,y) = sum_i H_i ell_i(y) = sum_(q=0)^(n-1) A_q(x)y^q.     (1.2)
```

Since

```text
 product_(j != i)(y-tau_j)
   = sum_(q=0)^(n-1) (-1)^(n-1-q)e_(n-1-q)^(i)y^q,
```

the coefficients are exactly

```text
 A_q = (-1)^(n-1-q) sum_(i=1)^n
             H_i e_(n-1-q)^(i) / D_i,       0 <= q < n.      (1.3)
```

This is the requested expression in symmetric functions of all roots and the
time functions.  It is linear in the `H_i` and hence in the integration
constants, but rational and generally nonlinear in the tame root data.

For later use, write

```text
 G(y)=sum_(j=0)^n (-1)^j e_j(tau)y^(n-j),     e_0=1,
 M_r := sum_i H_i tau_i^r/D_i.                               (1.4)
```

Expanding at `y=infinity` gives the exact generating identity

```text
 L(y)/G(y) = sum_i H_i/[D_i(y-tau_i)]
           = sum_(r>=0) M_r y^(-r-1),                         (1.5)
```

and hence the triangular conversion

```text
 A_q = sum_(j=0)^(n-q-1) (-1)^j e_j M_(n-q-j-1).              (1.6)
```

Equations (1.3) and (1.4)-(1.6) are equivalent.  Formula (1.3) is best for
displaying every level of the tree; the moments are best for the degree test.

### 1.3 The exact degree equations

Assume Moh's monic normalization `[y^m]f=1`, with `m<n`.  Then

```text
 M_r = 0,     0 <= r <= n-m-2,
 M_(n-m-1) = 1.                                             (DEG)
```

The first range is empty when `m=n-1`.  These identities are equivalent to

```text
 A_(n-1)=...=A_(m+1)=0,       A_m=1.                         (1.7)
```

Proof: (1.6) is triangular with diagonal coefficient `e_0=1`.  Successively,
`A_(n-1)=M_0`, `A_(n-2)=M_1-e_1M_0`, and so on.  Once the first
`n-m-1` moments vanish, `A_m=M_(n-m-1)`.

Thus:

```text
 high-degree homogeneous equations : n-m-1,
 monic affine normalization         : 1,
 total displayed in (DEG)           : n-m.
```

If only `deg_y L=m` is required, without a prescribed leading coefficient,
the exact condition is the `n-m-1` vanishings together with the open condition
`M_(n-m-1) != 0`.  Calling all `n-m` equations “degrees to kill” is false.

An occasionally useful check is the universal root identity

```text
 sum_i tau_i^r/D_i = 0  (0<=r<=n-2),       =1  (r=n-1).       (1.8)
```

It shows, for `m>=1`, that adding the same constant to all `H_i` changes only
the constant coefficient of `L` and never changes (DEG).

### 1.4 Exact polynomiality of the remaining coefficients

After (DEG), the remaining condition is exactly

```text
             A_q in C[x]=C[t^-1],             0<=q<=m.       (POLY)
```

In a common uniformizer `z=t^(1/R)`, a Laurent series belongs to `C[x]` iff
its support is contained in

```text
                { -Rd : d in Z_>=0 }.                         (1.9)
```

Accordingly, before using symmetry, (POLY) is the coefficient family

```text
 [z^k]A_q=0 for every k not in {-Rd:d>=0},       0<=q<=m.     (1.10)
```

After correct Galois descent, nonmultiples of `R` vanish automatically and
this reduces to

```text
              [t^h]A_q=0,       h=1,2,...,  0<=q<=m.         (1.11)
```

There is no extra finiteness condition on negative `t`-orders: an element of
`C((t))` already has only finitely many negative terms.  If one also imposes a
total-degree cap `deg_x A_q<=d_q`, add
`[t^-h]A_q=0` for `h>d_q`; this is stronger than the polynomiality requested
in the charge and is not silently assumed here.

Equations (DEG), (1.3), and (POLY), with the equivariant constants of section
2 and NO-RESIDUE of section 3, are the exact global conditions.

## 2. What is local, what Galois symmetry supplies, and what is global

### 2.1 Exact tree factorization

Let `T_g` be the rooted cluster tree of the `n` roots.  For a leaf `i` and an
internal vertex `v` on its path to the root, let `S_v(i)` be the leaves in the
children of `v` other than the child containing `i`.  Every `j!=i` lies in
exactly one such `S_v(i)`.  Therefore

```text
 D_i = product_(v on path(i)) product_(j in S_v(i))(tau_i-tau_j),             (2.1)

 sum_(r>=0)e_r^(i) Z^r
     = product_(v on path(i)) product_(j in S_v(i))(1+Z tau_j).               (2.2)
```

These two factorizations are exact, not leading-order analogies.  Substitution
in (1.3) proves immediately that every Lagrange coefficient sees every level:
the denominator contains the first separation of `i` from every other leaf,
and the numerator contains all the same sibling packets.

If a bottom disc `B` has radius `delta_1`, centre `w_B`, and `a_1=eV_2(B)`
roots

```text
 tau_i=w_B+c_i t^delta_1+higher,       i in B,
```

then the part of (2.1) internal to `B` begins with

```text
 t^((a_1-1)delta_1) p_(g,B)'(c_i),
 p_(g,B)(pi)=product_(i in B)(pi-c_i).                         (2.3)
```

The other factors in (2.1) are products at the ancestor radii.  They are units
after their forced powers are removed, shared by all bottom descendants of
the relevant ancestor, and begin contributing corrections at the positive
junction gaps `|delta_bottom-delta_ancestor|`.  This is precisely the outer-factor contribution
which the hostile review found missing from the restricted local recurrence.

### 2.2 The genuinely local block and BOTTOM-ODE

In the completed chart of one bottom disc, put

```text
 x=t^-1,  y=w_B(t)+pi t^delta_1,
 f=t^lambda_f Phi,       g=t^lambda_g Gamma.
```

The reviewed coordinate calculation and D1-PIN give the exact necessary
identity for an existing Keller pair

```text
 (lambda_f Phi+t Phi_t)Gamma_pi
   -(lambda_g Gamma+t Gamma_t)Phi_pi = -c,                    (LOCAL-KELLER)
```

because `lambda_f+lambda_g=delta_1-1`.  Its leading term, with
`p_f=Phi_0`, `p_g=Gamma_0`, is

```text
 d p_f p_g' - e p_g p_f' = kappa,
 deg p_g=eV_2,  deg p_f=dV_2,
 kappa=-ec/lambda_g=c(d+e)/(1-delta_1)=cde/q !=0.             (BOTTOM-ODE)
```

This is **local to one completed bottom disc**.  It implies the reviewed
squarefreeness, coprimality, STAR-RESIDUE, STAR-SUM, and dessin conditions.
In the interpolation language, the leading local star values interpolate to
`p_f`; differentiating the branch values by (JF) supplies the displayed
Wronskian.  Thus the leading local block of the global branchwise system
reproduces BOTTOM-ODE exactly.

What does not follow is the converse used in the refuted lane: an arbitrary
solution of LOCAL-KELLER in `C[[t^(1/R)]][pi]` need not be the restriction of
a polynomial in `C[x,y]`.  Equations (DEG) and (POLY) are the missing global
conditions.

### 2.3 Exactly what Galois symmetry gives for free

Let `Gamma=mu_R` act by `z -> omega z` and permute the roots.  Once
NO-RESIDUE holds, primitives can be chosen equivariantly.  Indeed the
difference between two conjugate primitives is constant, and averaging over
the finite group removes the resulting additive cocycle.  With that choice,

```text
 gamma(tau_i)=tau_(gamma i),  gamma(F_i)=F_(gamma i),
 a_(gamma i)=a_i.                                             (2.4)
```

Consequently there is exactly one free integration constant per Galois orbit
of branches.  If `O` is such an orbit, each orbit contribution

```text
 M_(r,O)=sum_(i in O)H_i tau_i^r/D_i
```

is `Gamma`-invariant.  Therefore

```text
 [z^k]M_(r,O)=0 unless R divides k,                            (2.5)
```

and the analogous assertion holds for the orbit contribution to every
`A_q`.  This is the exact automatic cancellation of fractional powers.  It
occurs **inside each complete Galois orbit**; cancellation between unrelated
orbits is not needed for descent.

The stabilizer of a bottom disc gives more local structure.  If its image on
the centred coordinate is `pi -> chi pi` of order `Delta`, monicity gives

```text
 p_g(chi pi)=chi^a p_g(pi),       p_f(chi pi)=chi^b p_f(pi),
 a=eV_2, b=dV_2.                                             (2.6)
```

Thus their supports lie in one residue class modulo `Delta`.  The nonzero
constant Wronskian gives `Delta | a+b-1`; for `Delta>1` it gives the reviewed
zero-root dichotomy.  Since the roots of `p_g` are simple, its nonzero roots
come in `Delta`-cycles and at most one root is zero, hence
`a=0 or 1 (mod Delta)`.  These are Galois/star constraints, not additional
copies of the global interpolation equations.

Symmetry gives only the following for free:

* conjugate discs have conjugate, hence redundant, local equations;
* constants and tame coefficients are identified according to their orbit;
* nontrivial-character, fractional-power terms have zero orbit trace;
* the support congruences such as (2.6) hold.

It does **not** force the coefficient of `t^h` for an integer `h`, does not
relate two distinct Galois orbits, and does not turn a formal tail into a
polynomial tail.

### 2.4 The genuinely global blocks

The following conditions cannot be checked in one bottom chart.

1. Every moment in (DEG) is a sum over all `n` roots.  Its invariant
   coefficient may cancel between different Galois orbits; no symmetry forces
   that cancellation.
2. Formula (1.3) uses `e_r^(i)` and `D_i`, whose tree factorizations (2.1)-(2.2)
   contain siblings at all levels.  At a level junction the same outer unit is
   seen by several descendant bottom discs, so their nominal local parameters
   are shared.
3. Each polynomial-tail equation (1.11) is an invariant sum over all branch
   orbits.  A separate local polynomial in `pi` can have an infinite `t`-tail
   even when LOCAL-KELLER holds.
4. The finite set of orbit constants `a_O` must solve every order of all these
   identities simultaneously.  A different constant for every formal branch
   is not permitted.

This is the corrected replacement for DISC-COUPLING: first take the trace over
each Galois orbit, then sum the invariant orbit contributions, retaining the
outer factors from every ancestor.  No resonance pattern is assumed.

## 3. NO-RESIDUE at all orders

### 3.1 Branchwise equation

Write

```text
 1/D_i = rho_i x^-1 + (terms with exponent != -1).
```

Since `c!=0`, a Puiseux primitive in (1.1) exists exactly when

```text
                 rho_i=[x^-1](1/D_i)=0                       (NO-RESIDUE)
```

for every branch.  In `z=t^(1/R)` this is `[z^R](1/D_i)=0`, because
`dx=-R z^(-R-1)dz`.  All other monomials integrate inside the Puiseux field;
the `z^R` term alone produces `log z` (equivalently `log x`).  Galois conjugate
branches have the same residue, so there is one independent scalar equation
per Galois branch orbit, although a fail-closed program may print all `n`.

This is an all-orders statement in the sense relevant here: the full product
`D_i` includes every Puiseux coefficient capable of contributing to `z^R`.
A leading valuation check is insufficient if higher products can reach that
exponent.  The truncation guard in the driver is chosen from the valuation of
`D_i^-1`; an input that stops before the residue coefficient is known fails
closed.  More explicitly, if `gamma_i=ord_t D_i`, then `D_i^-1` begins at
`t^-gamma_i` and the residue lies at relative depth
`max(0,1+gamma_i)`.  At a proper frontier the reviewed identity
`gamma_i=-delta_i^0` makes this `max(0,1-delta_i^0)`.

### 3.2 Its exact logical position inside the global system

If residues are not set to zero, write a primitive in the differential
extension as

```text
 H_i=H_i^P+c rho_i log x.
```

The logarithmic part of the Lagrange interpolant is

```text
 c log x * R(y),       R(y)=sum_i rho_i ell_i(y),  deg_y R<n. (3.1)
```

Suppose the high coefficients satisfy (DEG) **including their logarithmic
parts**, and the remaining `m+1` coefficients satisfy (POLY), which excludes
logs.  Then every coefficient of `R(y)` is zero.  Evaluation at `y=tau_i`
gives `R(tau_i)=rho_i`, so every residue is zero.  Therefore:

```text
 (DEG)+(POLY), interpreted in K[log x], implies NO-RESIDUE.    (3.2)
```

On the other hand, (POLY) for the lower `m+1` coefficients alone does not
control a logarithm sitting in a high coefficient.  More importantly, the
usual algorithm defines `F_i` in the Puiseux field before it forms the
interpolant.  In that implementation NO-RESIDUE is an independent
well-formedness equation and must be imposed first.  Thus it is logically
redundant in the full log-aware global system, but computationally independent
and not replaceable by a local regularity assertion.

## 4. The finite-order algorithm and exact counts

### 4.1 Why the bare Moh tuple has no exact unknown count

**PROVED-HERE / UNREVIEWED (information obstruction).**  There is no function

```text
 U_Q=U_Q(n,m,M_*,V_*,delta_*,u,v)
```

which equals the number of independent tame unknowns through order `Q` for
every realisation of that skeleton.

The reason is visible without a dimension computation.  The promoted skeleton
data give only a capacity such as

```text
                  sum_B V_2(B) <= u;                          (4.1)
```

they do not give the attained packet of bottom discs.  The reviewed `D=105`
row, for example, has `u=20,V_2=1`; `k=20` is permitted, not attained.  A
one-disc packet and a twenty-disc packet have different sets of local tail
coefficients and different junction sharing, yet the printed Moh tuple is the
same.  Even after `k` is supplied, the tuple does not say whether those discs
form one Galois orbit or several, so it does not determine the number of
integration constants or the number of conjugate equations.  Finally, as the
hostile review stressed, `delta_1-delta_2` being a displayed outer activation
does not prove that it is the first exponent in every inner tail.  The tame
support semigroup is also missing.

The level numbers along one distinguished chain,

```text
 a_r = n V_(r+1)/d_(r+1),       b_r = m V_(r+1)/d_(r+1),      (4.2)
```

give cluster sizes, not the full set partition of all `n` leaves.  Therefore a
closed number asserted from the bare tuple would conflate a representative
chain with the full actual branch packet, contrary to the campaign guardrail.

The minimal exact finite input is a **decorated skeleton to order `Q`**:

```text
 D_Q = (bare Moh tuple,
        rooted cluster tree on n labelled leaves,
        cyclic Galois action and orbit/stabilizer data,
        truncated Puiseux template tau_i(z) for every leaf,
        declarations identifying shared tame coefficients,
        target order Q and sufficient valuation guard).         (4.3)
```

This is not extra geometry invented by the algorithm.  It is precisely the
data needed to say what the phrase “the tame coefficients as unknowns” means.
The shipped emitter therefore requires this finite branch decoration and
refuses a bare skeleton rather than reporting it as an exact branch system.

### 4.2 Order-by-order construction

Choose `z` so that `x=z^-R`, with `R` divisible by every denominator in the
decorated data.  For a requested last exponent `Q`, do the following.

1. **Validate custody of the packet.**  Check the number of roots, leading
   separations at every declared tree vertex, closure under the permutation
   `z->omega z`, the declared coefficient identifications, and separability.
   A partial Galois orbit is an input error, not a failed Jacobian equation.
2. **Build all-level denominators.**  Form every difference and the products
   `D_i=product_(j!=i)(tau_i-tau_j)`, retaining valuations rather than dividing
   by a raw truncated polynomial.  Formula (2.1) records which level supplies
   each factor.
3. **Invert with a guard.**  Compute `W_i=D_i^-1` far enough to know every
   coefficient through `z^(Q+R)` needed below.  Unit leaders are recorded and
   saturated/nonzero.  If the supplied root series do not determine that
   range, stop with `INSUFFICIENT-GUARD`.
4. **Impose NO-RESIDUE.**  Emit `[z^R]W_i=0`, orbit-reduced if requested.
5. **Integrate coefficientwise.**  If
   `H_i=sum_q h_(i,q)z^q`, then

   ```text
        q h_(i,q) = -c R [z^(q+R)]W_i,       q != 0,           (4.4)
   ```

   while `h_(i,0)=a_O` for the Galois orbit `O` of `i`.  Equation
   (4.4) also shows directly why `[z^R]W_i=0` is the unique logarithmic
   obstruction.
6. **Form symmetric conditions.**  Compute either (1.3), or the moments
   `M_0,...,M_(n-1)`.  Emit (DEG) coefficient by coefficient in increasing
   `z`-order.  After (DEG), polynomiality may equivalently be tested on

   ```text
                 M_(n-m-1),...,M_(n-1) in C[x].               (4.5)
   ```

   This is because (1.6), restricted to the remaining `m+1` entries, is a
   unit-triangular transformation with `e_j in C[x]`.  Formula (4.5) is often
   cheaper than explicitly expanding every `e_r^(i)`.
7. **Project characters before counting.**  Check that nontrivial Galois
   characters cancel.  Then emit only the invariant, integer-order equations.
   Sum the surviving invariant contributions across distinct orbits; do not
   set each orbit contribution to zero separately.
8. **Sort by level junction.**  In a bottom chart, mark

   ```text
       J(edge)=R|delta_child-delta_parent|,
       J_r=R|delta_bottom-delta_r| for a bottom-to-ancestor table.             (4.6)
   ```

   At `J_r` activate the outer factors and shared symbols belonging to level
   `r`.  The absolute value makes this independent of the two opposite level
   index conventions present in the charge and frozen examples.  The equation
   order is still its actual `z`-order; the junction label is provenance, not
   a replacement order.

All arithmetic in these steps is finite for fixed `Q`.  Failing at a finite
order proves failure of the all-order condition.  Passing says only “survives
through `Q`”.

### 4.3 Closed-form intrinsic condition counts

Let `h` be the number of Galois orbits on branches.  For an invariant Laurent
series `S`, let `ell(S)` be its first retained `z`-exponent, and define

```text
 N_R(a,Q) := max(0, floor(Q/R)-ceil(a/R)+1).                  (4.7)
```

There are `d_0:=n-m` moment identities in (DEG), including the monic one.  If
`ell_r=ell(M_r-target_r)`, their exact raw coefficient count through `Q` is

```text
 C_deg(Q) = sum_(r=0)^(d_0-1) N_R(ell_r,Q).                  (4.8)
```

For the remaining coefficient `A_j`, let `beta_j` be its first retained
exponent.  The monic series identity `A_m=1` has already killed every tail of
`A_m`; counting it again as polynomiality would duplicate an equation.  For
the additional coefficients `A_0,...,A_(m-1)`, after Galois descent the
forbidden polynomial tail consists of the positive multiples of `R`, so

```text
C_poly(Q) = sum_(j=0)^(m-1)
   max(0, floor(Q/R)-max(1,ceil(beta_j/R))+1).                (4.9)
```

Before descent, replace the last count by the cardinality of all exponents in
the window which are not in `-R Z_>=0`; those equations are covariance checks
as well as polynomiality equations.  The independent residue count is

```text
 C_res=h                                                        (4.10)
```

once the guard reaches `z^R`; branchwise output contains `n` equations but
`n-h` are Galois repetitions.  Thus the intrinsic raw count is

```text
              C(Q)=C_res+C_deg(Q)+C_poly(Q).                 (4.11)
```

This counts equations, not their rank or ideal height.

If every identity is represented on one common finite invariant exponent set
`Lambda` and `Lambda_bad` is its forbidden positive-order subset, the same
deduplicated count has the compact form

```text
 C=h+(n-m)|Lambda|+m|Lambda_bad|.                            (4.11a)
```

At an allowed order there are `n-m` degree/monic equations; at a forbidden
order the `m` lower coefficients add to a total of `n`.  The residue term `h`
is included once, not once per series order.

A useful normalized special case starts after all earlier leading orders have
been discharged and retains the invariant `t`-orders `0,1,...,K`.  Every
moment identity is checked at `K+1` orders; after deduplicating the already
monic `A_m`, polynomiality adds `K` positive orders for each of the `m` lower
coefficients.  Then

```text
       C(K) = h + (n-m)(K+1) + mK
            = h + (n-m) + nK.                                (4.12)
```

The same formula at a level junction uses `Q=J_r` in (4.8)-(4.11).  Notice
that if `J_r` is not divisible by `R`, the first fractional outer activation
need not add a global invariant equation at that exact exponent: its conjugate
orbit sum is zero by (2.5).  It does add active symbols and can enter later
integer orders through products.  This is why a local “one condition per disc
at the first resonance” is not a valid global count.

### 4.4 Closed-form unknown counts for the decorated skeleton

Let `Z_Q` be the set of independent declared tame symbols which valuation
arithmetic says can affect an equation through `Q` (including the inverse and
integration guard), and let `u_0` count unspecialized leading/star parameters.
Then, with `c` normalized, the intrinsic unknown count is exactly

```text
              U(Q)=h+u_0+|Z_Q|.                              (4.13)
```

If `c` is an unknown nonzero scalar, add one and saturate at `c`; if affine
coordinate or scalar normalizations have not been fixed, list their gauge
dimension separately rather than pretending that it is an equation.

For a coefficient order `q`, let `A_q` be the set of active coefficient slots
before Galois identification.  In the free-tail model,

```text
 p_q=|A_q/Gamma|,        |Z_Q|=sum_(q active through Q)p_q.   (4.14)
```

Declared sharing across descendants replaces orbit classes by the indicated
equivalence classes.  At a junction, (4.14) gives the exact increment: count
the newly active child slots modulo Galois and shared-outer identifications.
This is the requested closed form at every level junction.  It is a function
of the decorated tree; equations (4.1)-(4.2) prove why it cannot be reduced to
the bare tuple.

### 4.5 The first possible overdetermined order — only a counting bound

Define

```text
 Q_count := min{Q in the ordered invariant/junction support : C(Q)>U(Q)},     (4.15)
```

after fixing gauges consistently on both sides.  This is the first order at
which the number of printed intrinsic equations can exceed the number of
unknowns.  It is a **COUNTING-BOUND**, not a kill theorem.

In the stationary normalized model `|Z_K|=u_0+pK`, (4.12) gives, when
`n>p`,

```text
 K_count=max(0, floor((u_0-(n-m))/(n-p))+1).                  (4.16)
```

If `n<=p` and the inequality does not already hold at `K=0`, this linear
count alone never crosses.  Formula (4.16) is conditional on the stationary
support hypothesis and is printed as such.

A “kill by counting” needs substantially more than (4.15): on every surviving
component, after saturating all discriminants, denominator leaders, `c`, and
degree leaders, one must prove that the new equations have ideal height (or
independent transverse rank) greater than the available component dimension.
One must first remove Galois repetitions, algebraic identities such as (1.8),
gauge directions, and auxiliary variables.  More equations than variables can
be duplicate or identically zero; only an empty saturated ideal, an explicit
incompatible coefficient, or a valid componentwise codimension proof kills.

### 4.6 Why the emitted system can be linear/quadratic exactly

The intrinsic expressions contain products of up to `n-1` differences.  The
driver does not discard higher-degree monomials.  It introduces named
auxiliaries and uses the following quadratic straight-line lift:

```text
 difference nodes                  linear;
 product chains for D_i            P_new=P_old*(tau_i-tau_j);
 inverse coefficients              D_i W_i=1;
 NO-RESIDUE                         [z^R]W_i=0;
 integration                       q h_(i,q)=-cR w_(i,q+R);
 powers of a root                  T_(i,r)=tau_i*T_(i,r-1);
 interpolation/evaluation          H_i=sum_(r=0)^m A_r*T_(i,r);
 monic normalization               A_m=1.                      (4.17)
```

Every multiplication equation is bilinear.  Polynomial coefficient variables
`A_r` are created only on the allowed support (1.9), so the evaluation equation
simultaneously imposes the degree and polynomiality conditions.  Conversely,
given the original products and interpolant all auxiliaries have their stated
values.  Thus the lift is existentially equivalent at the retained order; it
is not a quadratic approximation and does not claim that the eliminated ideal
is generated by quadrics in the original tame variables.  The driver reports
intrinsic counts separately from lifted equation/auxiliary counts.

## 5. Exact controls

### 5.1 A common automorphism lemma

All four positive controls are polynomial automorphisms.  Put `u=f,v=g` and,
on `v=c_2`, write the inverse as `(x,y)=(X(u),Y(u))`.  Differentiating the
inverse and using `J=[f,g]` gives

```text
       g_y(X(u),Y(u))=J X'(u),       J dx/g_y=du.              (5.1)
```

Thus the natural time value is exactly `u_i=f(x,tau_i)`, with zero integration
constant.  Also `1/g_y=J^-1 du_i/dx`; the derivative of a Puiseux series has no
`x^-1` coefficient, because the only putative source is the derivative of an
`x^0` term.  NO-RESIDUE therefore holds branchwise.  Uniqueness of the
degree-`<n` interpolant recovers `f` exactly.

The following table records all coefficients, in order `A_0,...,A_(n-1)`:

| `(f,g)` | `J` | `(m,n)` | `X(u),Y(u)` on `g=c_2` | recovered coefficients |
|---|---:|---:|---|---|
| `(y,x+y^3)` | `-1` | `(1,3)` | `c_2-u^3,u` | `(0,1,0)` |
| `(y,x+y^5)` | `-1` | `(1,5)` | `c_2-u^5,u` | `(0,1,0,0,0)` |
| `(y+x^2,x+(y+x^2)^2)` | `-1` | `(1,2)` | `c_2-u^2,u-(c_2-u^2)^2` | `(x^2,1)` |
| `(x+y^5,y+(x+y^5)^3)` | `+1` | `(5,15)` | `u-(c_2-u^3)^5,c_2-u^3` | `A_0=x,A_5=1`, all others zero |

Every entry satisfies (DEG), (POLY), and NO-RESIDUE identically over
`C(c_2,x)`, not merely to the test truncation.

For `(y,x+y^k)`, the roots are
`tau_i=zeta_i(c_2-x)^(1/k)` and
`-1/g_y(tau_i)=d tau_i/dx`.  The exponents of `1/g_y` are
`-(k-1)/k-l`, `l>=0`, so `-1` never occurs for `k=3,5`.

For the raw quadratic control, with `r=(c_2-x)^(1/2)`,

```text
 tau_pm=-x^2 +/- r,       H_pm=+/- r,
```

and the interpolant is `y+x^2`.  Its denominator exponents are
`-1/2-l`, so again there is no residue.  If the strict total-degree Moh gauge
is desired, the determinant-one shear used in the charged control gives

```text
 f~=y+(x+y)^2=y^2+(2x+1)y+x^2,
 g~=x+y+f~^2,
 (A_0,A_1,A_2,A_3)=(x^2,2x+1,1,0).                           (5.2)
```

### 5.2 The five-bottom-disc composition control

For `f=x+y^5`, `g=y+f^3`, let `u=f`.  On the target fibre,

```text
 y=c_2-u^3,       x=u-(c_2-u^3)^5.                           (5.3)
```

The last polynomial has degree 15, giving the fifteen branches.  With
`t=x^(-1/15)`, choose `beta^5=1` and `omega^3=beta`.  Direct reversion gives

```text
 tau_(beta,omega)
   = -beta t^-3 + omega/(5 beta^4)t^11 + higher.              (5.4)
```

Hence there are exactly five bottom discs indexed by `beta`, three branches
per disc.  The `mu_15` action is transitive on all fifteen branches and the
order-three subgroup stabilizes a bottom disc.  Moreover

```text
 1/g_y=du/dx=(omega/15)x^(-14/15)+0*x^-1+O(x^(-17/15)).       (5.5)
```

The interpolant of the values `u_i=x+tau_i^5` is exactly `x+y^5`.  This control
is outside NU-TWO but exercises precisely the global orbit trace, five-disc
coupling, degree cutoff, and no-residue paths required here.

### 5.3 A target-independent negative control

Take

```text
                  g=y^2-x^2-x,
 tau_pm=+/-(x^2+x+c_2)^(1/2).
```

Then

```text
 1/g_y(tau_pm)
  = +/-[ (1/2)x^-1-(1/4)x^-2+(3/16-c_2/4)x^-3+... ].         (5.6)
```

NO-RESIDUE fails at exactly `t=x^-1` order `1`, with residues `+1/2` and
`-1/2`, independently of the target.  For a putative `m=1` interpolant and
`c=1`, a primitive on the plus branch is

```text
 H=(1/2)log(2sqrt(x^2+x+c_2)+2x+1).
```

The interpolant slope contains `(log x)/(2x)`; the two integration constants
can change only its nonlogarithmic part.  Thus the global polynomiality test
fails at the same first logarithmic order.  This is a rigorous condition on
`g` alone.

For comparison only, the seven charged two-tower **pairs** fail already in the
leading bottom chart: the corrected reviewed values have
`lambda_f+lambda_g != delta_1-1` and bottom-bracket degrees
`2,3,4,2,2,5,2`.  The old driver omitted the centre-root contribution to
`lambda_g`; its printed lambda table must not be reused.  Those rows disprove
the supplied pairs, not the possibility of some different mate for the same
`g`, so they are not used as the target-independent negative control.

## 6. Delivered driver and verification

The driver is `box/globalinterp-drivers-20260902/globalinterp.py`, SHA-256

```text
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588
```

Its principal commands are

```text
python3 box/globalinterp-drivers-20260902/globalinterp.py example
python3 box/globalinterp-drivers-20260902/globalinterp.py emit INPUT.json --order Q --format json
python3 box/globalinterp-drivers-20260902/globalinterp.py controls
python3 box/globalinterp-drivers-20260902/globalinterp.py selftest
```

Input contains the bare skeleton, common denominator, truncation window, all
`n` branch templates, optional exact contact orders, tame `tail_from` slots,
and orbit metadata.  A verified orbit reuses one constant; an unverified orbit
is conservatively counted branchwise.  `bottom_delta_index` declares which
endpoint is bottom, so the output keeps absolute radii separate from positive
edge-gap junction orders.

`polynomial_mode=moh_total_degree` is exact in Moh's monic total-degree gauge
and uses `deg_x A_r<=m-r`.  The mode
`coefficient_polynomiality_only` requires explicit finite `x_degree_cap(s)`;
one run is a bounded slice of bare (POLY), and the full existential condition
is the union over finite caps.  This distinction prevents an unstated degree
bound from being used on the raw quadratic control.

The emitter reports direct condition-slot counts, lifted raw/deduplicated
counts, equation degree, unknown type, counts at each coefficient order and
level gap, precision guards, inequations, and either a sampled rank lower
bound or symbolic ambient Jacobian rank.  A nonlinear input expression is
retained and flagged; it is never projected to degree two.

**UNREVIEWED COMPUTATION.**  Independent reruns in this lane gave:

```text
controls: 40 checks, 0 failures
selftest: 50 checks, 0 failures
example:  36 lifted equations / 35 deduplicated, 27 auxiliaries+unknowns,
          all degrees <=2, exact ambient symbolic Jacobian rank 26
```

The example itself is a useful warning: its raw lifted equation count exceeds
its variable count, yet its rank does not and the control has a solution.
Auxiliary/raw counting is not a kill certificate.

## 7. Bounded residual and FALLACY-v2 audit

`OPEN[PACKET-COUNT-AUGMENTATION(Q)]` is the only open raised here.  For a fixed
requested order `Q`, supply the actual packet of at most `u` bottom discs,
their weights, the cyclic action on at most `n` leaves, the finite retained
exponent set `Lambda_Q`, and the ancestor-sharing equivalence relation.  If
`L_Q=|Lambda_Q|`, there are at most `n L_Q` raw branch-tail slots before
sharing.  Once this finite decoration is supplied, (4.7)-(4.15) and the driver
give exact raw counts.  The open is the finite enumeration/lift from a bare
Moh tuple to those decorations, not an unbounded claim that a bare-tuple
formula already exists.

Guardrail audit:

* **Flag/place/series.**  Branches `tau_i`, bottom discs, tree vertices,
  completed-chart series, and physical places are never identified.  A
  representative Moh chain is not treated as the full branch packet.
* **Carrier/attainment and floor/attainment.**  `sum_B V_2(B)<=u` is used only
  as a cap.  No value of the number of discs, including the reviewed `k=20`,
  is asserted attained.
* **Galois/orbit charge.**  Only a declared complete orbit is traced; distinct
  invariant orbit contributions remain coupled.  Fractional cancellation is
  not promoted to integer-tail cancellation.
* **Raw remainder and rings.**  The base is `C(s)((z))`, `x=z^-R`; unit leaders
  and separations are explicit inequations.  A vanished leader is a new
  stratum.  The quadratic lift is existential, not a claim about the
  eliminated generator degree.
* **Prime/derivative.**  `p_g'` and `p_f'` mean `d/dpi`; `F_i'` means branchwise
  `d/dx`.  No prime label is inferred to be a derivative without declaration.
* **Counting.**  Raw slots, deduplicated expressions, ambient Jacobian rank,
  ideal height, and emptiness are kept distinct.

No exit-price assertion is made, so no `charge_basis` line is emitted.

## 8. Typed conclusion

```text
REVIEWED INPUT
  JAC-FIBRE; D1-PIN; the exact necessary LOCAL-KELLER identity;
  BOTTOM-ODE and its corrected normalization.

PROVED-HERE / UNREVIEWED
  symmetric coefficient formula (1.3); moment form (1.4)-(1.6);
  n-m-1 high-degree vanishings plus one monic normalization;
  exact C[x] support test; orbit trace/descent statement;
  all-level tree factorization; log-block implication;
  impossibility of a bare-skeleton unknown count; conditional formulas
  (4.7)-(4.16); exact automorphism controls and the g-alone negative control.

ALGORITHM / UNREVIEWED
  exact finite-order quadratic lift with valuation guard, orbit constants,
  order/junction counts, rank diagnostics, and fail-closed higher-degree flag.

COUNTING-BOUND ONLY
  Q_count is the first possible raw excess.  A kill requires componentwise
  height/rank or an empty saturated ideal; raw excess is not enough.

CONTROLS
  (y,x+y^3), (y,x+y^5), (y+x^2,x+(y+x^2)^2), and
  (x+y^5,y+(x+y^5)^3) recover f exactly and satisfy DEG/POLY/NO-RESIDUE.
  The composition has five bottom discs, three branches each.
  g=y^2-x^2-x fails at [x^-1](1/g_y)=+/-1/2, t-order 1.

NOT CLAIMED
  sufficiency from one numerical target; attainment of a Moh skeleton or
  branch packet; independence of raw equations; termination after a finite
  passing truncation; a skeleton-only count using omitted packet data.
```

<!-- BODY-END -->
