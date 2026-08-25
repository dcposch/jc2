# Preregistration: D1 weighted coefficient-infinity Rees gate

Date: 2026-08-25  
Execution: **registered Amazon EC2 only**  
Status: **SOURCE DESIGN; NO EXCEPTIONAL-DIVISOR OR DEFORMATION VERDICT**

## 1. Exact question

This is the boundary successor to the reviewed D1 degree split.  Work over a
finite characteristic-zero constant field extension and retain the exact
eight descended Faber rows.  Give the coefficient/load coordinates weights

```text
w(A_i)=9-i (0<=i<=7),  w(k)=6,
w(mu)=15, w(nu)=18, w(rho)=20,
```

where `rho` homogenizes the affine target `R8=1`.  Row `R_l` has weight
`12+l`.  Introduce a Rees scale `e` by

```text
B_i=e^(9-i) A_i,  K=e^6 k,
M=e^15 mu, N=e^18 nu, R=e^20.
```

After multiplying row `l` by `e^(12+l)`, weighted homogeneity gives the
same polynomial row in `(B,s,K,M,N,R)`.  An actual fixed-load coefficient
pole at `s=1` has

```text
p=max_i d_i/(9-i),  d_i=-v_(s-1)(A_i),
```

and lies in this boundary only when `p>3`.  On a ramified chart write
`p=m/n` in lowest terms, `s-1=tau^n`, `e=tau^m`.  Then

```text
B_i(tau)=tau^(m(9-i))*A_i(1+tau^n),
B_i(zeta*tau)=zeta^(m(9-i))*B_i(tau) for zeta^n=1.
```

Thus allowed jet exponents are congruent to `m(9-i) mod n`.  The compiler
may never replace this by an unproved ordinary-power `B_i(e)` ansatz.  The
active leading set `S` satisfies `n | gcd(9-i:i in S)`; in particular
`n<=9`, but `m` is unbounded.  Every denominator `n`, coordinate axis, and
change of the maximizing set is a separate chart.

## 2. First exact gate: exceptional divisor

For a section with fixed finite `(k,mu,nu)`, the exceptional divisor has

```text
s=1, K=M=N=R=0.
```

The first AWS job must:

1. reconstruct the exact eight rows from the independently replayed V2
   compiler and verify every monomial has weight `12+l`;
2. remove only the affine `-1` in `R8`, replacing it conceptually by `-R`;
3. saturate by the irrelevant ideal `(B0,...,B7)` and compute the full
   characteristic-zero minimal-prime support of the eight exceptional rows
   in `B0,...,B7`;
4. compare it by two ideal containments with the monic depressed cubic-power
   graph

   ```text
   C=z^3+p*z+q,
   f=C^3=z^9+B7*z^7+...+B0;
   ```

5. report every additional component rather than saturating it away.

The projective cube graph includes the squarefree locus, the
discriminant-zero double-root locus, and both `p=0`/`q=0` axes.  The affine
origin `(p,q)=(0,0)` is a required negative control: it solves the raw cone
but has no nonzero leading coefficient, hence is removed by irrelevant-ideal
saturation.  No localization by `p*q*Disc(C)` is allowed in the coverage
computation.  The global saturation and all eight `B_i!=0` charts must agree
on coverage.  A modular decomposition is navigation only.

## 3. Fixed-slope normal deformation gate

Only after the exceptional support is certified may a normal Kuranishi
compiler be consumed.  For each fixed coprime `(m,n)`, it must impose the
equivariance above, compile through `tau`-order `20m`, quotient tangent
motion coming from the moving common cubic `C(tau)`, and retain the complete
normal space on each rank/Fitting stratum.  The source-typed expected first
charged Rees weights are

```text
K at 6;
M at 15: a normal phi_9 can enter through L_K(phi_9);
N at 18: Q(phi_9) and L_K(phi_12) can enter;
R at 20: Q(phi_10), L_K(phi_14), and licensed cross terms can enter.
```

This schedule is a preregistered hypothesis, not a result, and does not make
the fixed-slope jet bound uniform: `m` is unbounded.  The compiler must prove
from the sparse row AST that there is no unforced normal term before the
charged order.  It must split at least

```text
mu != 0;  mu=0,nu != 0;  mu=nu=0,
```

and the squarefree, double-root, both axes, rank-zero, and every new Fitting
stratum.  A surviving truncated arc must be substituted into all eight
original unscaled rows on its explicit `(m,n)` ramified chart.  No finite
whole-boundary theorem follows without a separately proved finite-slope or
formal-smoothness/finite-determinacy argument.

## 4. Exact firewall

- The exceptional-divisor equality alone does not exclude a pole arc.
- An associated-graded common cubic is not a persistent common-cubic
  trajectory; the latter would have zero source bracket, but persistence is
  exactly what the Kuranishi gate must decide.
- The existing `(6,9)` common-cubic theorem and the fixed-total-D12 binary
  cubic calculations do not cover this unbounded-total coefficient-infinity
  divisor.
- A calculation at `s=1`, a generic squarefree point, one integral slope, or
  one load stratum is not whole-boundary coverage.
- The shifted affine row `R8=T8-1`, an unsaturated cone containing the
  origin, and a non-equivariant ramified jet are mandatory negative controls.
- No modular point, sampled rank, generic standard basis, or truncated arc
  is a D1 trajectory, exclusion, counterexample, or JC2 theorem.

## 5. Frozen parents

- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py`
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py`
- `xmodel/max12-912-order3-d1-classical-degree-split-20260825.md`
- `xmodel/max12-912-order3-d1-classical-degree-split-review-20260825.md`
