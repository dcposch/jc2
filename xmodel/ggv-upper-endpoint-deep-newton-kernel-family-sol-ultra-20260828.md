# Deep `A|V0` Newton faces, endpoint residues, and a two-parameter kernel family

Date: 2026-08-28  
Lane: deep upper-endpoint research (Sol Ultra)  
Status: **NEW UNIVERSAL REDUCTIONS + EXACT HOMOGENEOUS FAMILY; ENDPOINT LOCUS NOT EXCLUDED**

## 1. Verdict

The surviving active deep branch is not rigid near the known literal point.
That point lies on an exact two-parameter family of raw homogeneous solutions
through D22.  Every member has an auxiliary weight-22 coefficient in the
one-dimensional endpoint kernel, so none solves `D22=1`, but the family
decisively shows that the existing tangent obstruction is not an isolation
theorem.

There is also a new universal reduction at a common root of `A` and
`S=V0/A`.  On the exact-`D=0`, active-`c2` successor already reviewed through
D13, polynomiality of `G15` and `G14` forces

```text
P1(alpha)=0,
F7(alpha)=0
```

at every simple root `alpha` of `A` with `S(alpha)=0`.  The next Newton face
is even and quartic.  It gives an explicit finite residue map `rho_alpha`;
the endpoint equation requires

```text
I_A(alpha)/8 + gamma = rho_alpha,       I_A'=A.          (E_alpha)
```

The same global modes `c14,c16,c18,c20` must also equal four recursively
computed local face values at every such root.  For two common roots, taking
differences in `(E_alpha)` eliminates both the endpoint integration constant
and an optional `c22`.  This is a small exact interpolation problem and is
the cleanest next elimination target.

These statements do **not** exclude the entire deep locus.  Local face data
can vary from root to root, and no argument below proves that the resulting
finite compatibility system is inconsistent.

## 2. Hypotheses and notation

Work over a characteristic-zero field.  Let `A` be a monic squarefree
quartic and use the reviewed active deep prefix

```text
F0=A^4,
F1=A^3 S,
F2=A^2(S^2+Z)/4,
F3=A(SZ+AU)/8,
64F4=Z^2+AR,
S^2-2Z=AQ.
```

On the exact successor used here,

```text
D=R-4SU=0,
P=256F5-RS+2S^2U=A P1,
E=2048F6-2SP1-4QSU-8U^2=A e1,
L=QS+4U=A ell,
J=P1-SQ^2/2.
```

The characteristic is the complete fixed schedule

```text
G=F^(3/2)+sum_(m=2,4,...,20) c_m t^m F^((12-m)/8).
```

All claims about `G_n` use the complete characteristic, not a replay with
inactive modes deleted.  The common-root theorem assumes the raw
coefficients through `G21` are polynomials; raw degree windows can only add
constraints.

## 3. First root-local scaling: a fourth power

Let `alpha` be a simple root of `A`, put `X=alpha+epsilon`, write
`A=epsilon*a(epsilon)`, and scale `t=epsilon*tau`.  Then

```text
epsilon^-4 F(X,epsilon*tau)
 = (a^2+aS*tau/2+Z*tau^2/8)^2
   + epsilon*(a^2 U*tau^3/8+aR*tau^4/64)
   + sum_(i>=5) epsilon^(i-4) F_i*tau^i.
```

Because `S^2-2Z=AQ`, the leading face at `epsilon=0` is

```text
(a(0)+S(alpha)*tau/4)^4.                              (N1)
```

Thus the active deep lift changes the old square face into a fourth power.
If `S(alpha)` is a unit, `(N1)` retains a nonconstant linear factor.  If
`S(alpha)=0`, it collapses to the constant `a(0)^4`; that degeneration is
not itself a contradiction and requires a new Newton scale.

## 4. Common-root Newton cascade

Assume now `A(alpha)=S(alpha)=0`.  Squarefreeness makes `epsilon` a local
uniformizer.  The reviewed lifts give

```text
ord(Z)>=1, ord(U)>=1, ord(R)>=2, ord(F6)>=1.
```

Here `ord(F6)>=1` follows from `E=Ae1`, since all other terms in `E` vanish
to order at least two at the common root.

### 4.1 The slope `3/5` face forces `P1(alpha)=0`

If `P1(alpha)` were nonzero, then

```text
F5 = A P1/256 + O(epsilon^3)
```

has exact order one.  For the scaling `t=epsilon^(3/5)*tau`, the only terms
on the lower face of `F` are `F0=A^4` and `F5 t^5`.  Consequently the most
singular term of `G15` is the three-`F5` contribution from `F^(3/2)`:

```text
binom(3/2,3) F5^3/A^6
 = -P1(alpha)^3/(16*256^3*a(0)^3) * epsilon^-3 + O(epsilon^-2).
```

No characteristic mode can cancel it.  At weight 15 the only other mode on
the same congruence class is `m=10`, and its one-`F5` contribution has only
order `epsilon^-2`; odd modes do not exist.  Polynomiality of `G15` therefore
forces

```text
P1(alpha)=0.                                           (N2)
```

### 4.2 The slope `4/7` face forces `F7(alpha)=0`

After `(N2)`, `F5` has order at least two.  If `F7(alpha)` were nonzero, the
next lower face under `t=epsilon^(4/7)*tau` would contain only `F0` and
`F7 t^7`.  The most singular term in `G14` would be

```text
binom(3/2,2) F7^2/A^2
 = 3F7(alpha)^2/(8a(0)^2) * epsilon^-2 + O(epsilon^-1).
```

The born `c14 F^(-1/4)` term has only an order-one pole, and no odd mode is
available.  Hence polynomiality of `G14` forces

```text
F7(alpha)=0.                                           (N3)
```

Equivalently, over the squarefree root algebra,

```text
gcd(A,S) divides P1 and F7.
```

This is field/radical divisibility, not a nonreduced scheme-membership
claim.

## 5. The surviving even face and its endpoint residue

After `(N2)` and `(N3)`, use `t=epsilon^(1/2)*tau` and normalize
`z=tau^2/a(0)`.  The lower face of `epsilon^-4 F` is

```text
p_alpha(z)
 = (1-Q(alpha) z/16)^2
   + e1(alpha) z^3/2048
   + F8(alpha) z^4.                                   (P_alpha)
```

All odd-index terms lie one half-step above this face.  Put

```text
d_k=c_(2k),
C_alpha(z)=p_alpha(z)^(3/2)
  + sum_(k=1,...,10) d_k z^k p_alpha(z)^((6-k)/4).     (C_alpha)
```

For `r>6`, the face coefficient `[z^r]C_alpha` is the leading coefficient
of the possible pole `A^(6-r)` in `G_(2r)`.  Therefore polynomiality through
`G20` imposes

```text
[z^7]C_alpha=...=[z^10]C_alpha=0.                      (R7--R10)
```

Since `p_alpha(0)=1`, the coefficient `d_r` occurs with coefficient one for
the first time in row `r`.  Thus `(R7--R10)` recursively and uniquely
prescribes `d7,d8,d9,d10`, i.e. `c14,c16,c18,c20`, from

```text
Q(alpha), e1(alpha), F8(alpha), c2,c4,c6,c8,c10,c12.
```

These four prescribed values must agree at every common root because the
modes are global scalars.  After those rows are killed, define

```text
rho_alpha=[z^11]C_alpha.                               (rho)
```

Then the local characteristic has

```text
lim_(X->alpha) A(X)^5 g22(X)=rho_alpha.                (L22)
```

This formula converts the deep local branch into a finite exact residue
map with only a quartic power-series calculation through `z^11`.

## 6. Global particular-versus-kernel compatibility

For any coefficient `R(X)` placed in the absent raw `G22` receiver, the
same-row operator is

```text
L22(R)=-40A^3 A'R-8A^4R',
-A L22(R)=8(A^5R)'.                                   (O22)
```

With the campaign sign convention `D22=-L22`, the target `D22=1` is
equivalent to

```text
A^5 g22=I_A/8+gamma,        I_A'=A,                    (T22)
```

where `gamma` is the homogeneous-kernel scalar.  At a common root, `(L22)`
and `(T22)` give the necessary equality

```text
I_A(alpha)/8+gamma=rho_alpha.                          (E_alpha)
```

An optional `c22 t^22 F^(-5/4)` shifts every `rho_alpha` by the same scalar
`c22`.  It is exactly another presentation of the `A^-5` kernel and can be
absorbed into `gamma`.  In particular, for two common roots `alpha,beta`,

```text
(I_A(alpha)-I_A(beta))/8 = rho_alpha-rho_beta,          (E_ab)
```

independently of `gamma` and `c22`.

There is an additional pole fact worth retaining.  At every simple root of
`A`, the numerator `N=I_A/8+gamma` is either nonzero, giving an exact
order-five pole, or vanishes to exact order two because `N'=A/8`, giving an
exact order-three pole.  The target particular solution is never regular at
an `A`-root.

### What two or more common roots currently imply

Equations `(R7--R10)` at each root, followed by `(E_ab)`, are explicit
interpolation conditions.  They are not automatically contradictory:
`Q(alpha)`, `e1(alpha)`, and `F8(alpha)` may vary.

Two useful conditional exclusions do follow immediately:

1. If two common roots have identical triples
   `(Q(alpha),e1(alpha),F8(alpha))`, then their residues agree, so the
   endpoint requires `I_A(alpha)=I_A(beta)`.  A quartic with distinct
   critical values excludes this.
2. In the exact family of Section 7 with `s=0`, all four roots have the same
   face data and the same residue.  They would require `I_A` to take one
   value at all four roots.  This is impossible: if `I_A-c` vanished at all
   roots, it would be `A` times a linear polynomial; differentiating at the
   simple roots would force that linear polynomial to vanish at four points.

The unrestricted common-root branch still needs elimination of the varying
face data, not an assertion that `(E_ab)` alone is inconsistent.

## 7. Exact two-parameter homogeneous family

Let `s,q` be constants with `q!=0` and define

```text
H=(A+s t/4)(A+s t/4-q t^2/16),
F=H^2.
```

Its reduced-prefix data are

```text
S=s,
Q=q,
Z=(s^2-Aq)/2,
U=-qs/4,
R=-q s^2,
P1=s q^2/2,
F4=(Z^2+AR)/64,
F5=sq(Aq-s^2)/512,
F6=s^2 q^2/4096,
F7=F8=...=0.
```

They satisfy `D=E=L=J=0` identically.  Choose modes

```text
c2=q,
c6=q^3,
c14=-(6139/2^34) q^7,
c18=(16369/2^47) q^9,
c4=c8=c10=c12=c16=c20=0.                              (M)
```

Then

```text
G0,...,G12 are polynomials,
G13=...=G21=0,
D0=...=D22(raw)=0,
g22=(9207/2^57) q^11 A^-5.                            (K)
```

Here is a short proof that this is a family, rather than finite-sample
evidence.  First take `s=0,q=1` and put `z=t^2/A`.  Then

```text
F=A^4(1-z/16)^2,
G=A^6 C(z),
```

where the modes `(M)` give

```text
[z^7]C=...=[z^10]C=0,
[z^11]C=9207/2^57.
```

Thus the prefix through weight 21 is polynomial and the first omitted term
is exactly the kernel in `(K)`.  Replacing `A` by `A+s t/4` is an exact shear
and produces the displayed `H`; the polynomial prefix remains of `t`-degree
at most 12, while the tail still begins at weight 22.  Finally replacing
`t^2` by `q t^2` multiplies the weight-`2k` mode and coefficient by `q^k`.
This proves `(M)` and `(K)` over the ground field without choosing a square
root of `q`.

Each characteristic summand satisfies the determinant PDE separately:

```text
F_X(12G-tG_t)+(tF_t-8F)G_X=0
```

for `G=t^m F^((12-m)/8)`, because `8(12-m)/8=12-m`.  Hence truncating the
polynomial prefix gives every raw determinant row through D21, while the
omitted weight-22 kernel also gives homogeneous D22.

This family contains the known literal point at `(s,q)=(1,1)`.  The
one-parameter subfamily `q=s^2` is the obvious `t`-rescaling orbit, but the
full `s,q` family supplies a second independent direction.

## 8. Why the old tangent obstruction is automatic

Write the determinant as

```text
mathcal D=F_X(12G-tG_t)+(tF_t-8F)G_X.
```

At the literal point, exact evaluation at `(X,t)=(0,8)` gives

```text
F=9,       F_X=0,       tF_t-8F=0,
G=1309349, G_X=0,       12G-tG_t=0.
```

Therefore `delta mathcal D(0,8)=0` for **every** perturbation: all four base
multipliers in the product rule vanish.  The exact tangent dual

```text
y(D_n[X^0])=8^(n-22)
```

is simply `8^-22 delta mathcal D(0,8)`.  Its contradiction with a unit
`D22[X^0]` target is consequently an automatic rank-zero phenomenon, not
evidence that the literal point is isolated.  The exact two-parameter family
makes this failure of the isolation interpretation concrete.

A meaningful local test must start at second order, allow the common
critical point to move, and quotient the two family directions.  A relaxed
quadratic-column screen can be useful as a discriminator, but consistency of
that relaxation would still need the Veronese/rank-one constraints before it
could assert a genuine second-order arc.

## 9. Reproducibility and scope

Frozen checker:

```text
cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828/
  verify_deep_newton_kernel_family.py
```

Checker SHA-256:

```text
0b873f2b4e0cdd4f55312dea6bf2d69d4fcbb3bb03c5725c082028148847c99f
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828/verify_deep_newton_kernel_family.py
```

Expected marker:

```text
PASS_EXACT_DEEP_NEWTON_KERNEL_FAMILY
```

The checker pins the reviewed literal-tail recurrence, replays exact
`t`-scaling and a nontrivial `q!=s^2` family member, verifies every raw row
through D22 for that mutation, checks the endpoint operator and literal
rank-zero evaluation, and independently computes two exact even-face
residues.  The universal statements in Sections 3--7 are algebraic proofs;
the sample replays are mutations, not the basis for universal quantifiers.

No endpoint solution, counterexample, emptiness theorem for the full deep
locus, unrestricted branch-P theorem, Keller theorem, or proof/disproof of
JC2 follows.  The concrete successor is the finite multi-root face system
`(R7--R10)+(E_ab)`, with separate handling of roots where `S` is a unit.
