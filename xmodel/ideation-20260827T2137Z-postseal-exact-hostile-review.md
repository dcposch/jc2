# Post-seal exact hostile review — round `20260827T2137Z`

**Reviewer:** Sol Ultra, independent narrow review.  
**Targets:** (A) the all-`n` Lagrange formula introduced in Opus5's
cross-review of Fable5; (B) the fixed/linear collision in
`ggv-8_28-bi-face-provenance-r0-sol-ultra-20260827.md`.  
**Status:** review only; no canonical file was changed and no JC2 consequence
is claimed.

## 0. Verdict

1. **Formula confirmed, with a notation guard.**  In the campaign's formal
   branch, for every `n >= 0`,

   ```text
   q_n = 2/(n+2) [t^n] phi(t)^(n+2)
       = 2/(n+2) [t^n] F(t)^((n+2)/8),
   ```

   where `phi(t)=F(t)^(1/8)` is the *pre-reversion* series with
   `phi(0)=p`.  Thus the displayed `[t^n]P^(n+2)` is correct only if `P`
   there means `phi(t)`, not the post-reversion series `P(s)`.
   Triangularity and the `mu_4` character law follow exactly.

2. **Algebraicity confirmed; the gate-recursion consequence is too fast.**
   On the frozen window `F_i=0` for `i>=15`, `P(s)` and `Q(s)=P(s)^2` are
   algebraic over the coefficient function field, of extension degree at
   most `14`; hence the raw coefficient sequence `(q_n)` is P-recursive.
   This alone does **not** prove that de Rham obstruction/gate coordinates
   are P-recursive, nor an effective uniform finite gate bound.  That step
   still needs a telescoping or finite reduction theorem compatible with the
   `X`-dependent recurrence and then a parameter-stratum/leading-coefficient
   analysis.

3. **BI-FACE collision confirmed at exactly frozen scope.**  The common raw
   key is genuinely the first-component coefficient of `x^15 y^52`.  The
   upper graph sends it to `[X^15]F_1=0`; the lower FACEPIN graph sends it to
   `-14 a rho`.  Since the lower localizer makes `a rho` a unit, their tensor
   product over the raw ring is the zero ring.  The parallel
   `g_23_80=0=-21 b rho` collision independently gives the same result.
   This separates these two normalized frozen fixtures; it does not separate
   the whole upper branch-P stratum from the lower family after adding
   unrepresented coordinate/normalizer freedom.

## 1. Custody actually checked

The mathematical bytes used here currently hash as follows:

```text
7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compile_lf40.py
bc61e6c33dc450664e1e83a98b9262210242c0713be005c78427161c3d6acc40
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/facepin_substitution.json
27de0604b07634c8c619585317ec0a183c1268494ed582ebf5a472be3ed3e841
  cases/ggv_8_28_lower_facepin_lf40_v1_20260827/compiled/slot_census.json
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

The lower R1 source manifest still has byte hash `70af5634...`.  The upper
`SOURCE.sha256` has legitimately grown for the later prefix lane and now has
byte hash `67c40382...`, not the earlier `324f4293...` recorded by the BI-FACE
producer.  The compiler, raw-system, and common-lattice bytes used in the
coefficient argument are unchanged, so this is a custody-staleness repair,
not a mathematical repair.

## 2. Claim A: exact derivation and hypotheses

Let `R` be a characteristic-zero field (or a Q-algebra in which the needed
units exist), let

```text
F(t)=F_0+F_1 t+... in R[[t]],   F_0=p^8,   p!=0,
```

and let `phi(t)` be the unique formal eighth root with
`phi(0)=p`.  There is a unique `t(s) in sR[[s]]` satisfying

```text
t=s phi(t).
```

Put `P(s)=phi(t(s))`, `Q(s)=P(s)^2=sum_(n>=0) q_n s^n`.  For `n>=1`,
Lagrange--Bürmann gives

```text
q_n = 1/n [t^(n-1)] (F(t)^(1/4))' phi(t)^n
    = 1/(4n) [t^(n-1)] F^((n-6)/8) F'
    = 2/(n(n+2)) [t^(n-1)] (F^((n+2)/8))'
    = 2/(n+2) [t^n] F^((n+2)/8).
```

For `n=0` the same formula reads `q_0=F_0^(1/4)=p^2` and is direct.
These hypotheses hold in the campaign field `L=K(X)(p)`, `p^4=H`, because
`F_0=H^2=p^8` and `p` is a unit in the function field.  No convergence or
generic-root hypothesis is used.

### Exact implications

For `n>0`, the only occurrence of the new coefficient `F_n` in
`[t^n]F^((n+2)/8)` is its linear occurrence.  Therefore

```text
q_n = (1/4) p^(n-6) F_n + R_n(F_1,...,F_(n-1)),
```

which is the required triangular law (`p^(n-6)=p^(n+2)/H^2`).  If the deck
action fixes every `F_i` and sends `p` to `zeta p`, uniqueness gives
`sigma(phi)=zeta phi`; hence

```text
sigma(q_n)=zeta^(n+2) q_n.
```

Thus both triangularity and the advertised character are confirmed, not
merely checked at small `n`.

### Algebraicity and the remaining scope gap

Substitution of `t=sP(s)` gives the exact equation

```text
P^8 = F(sP) = sum_(i=0)^d F_i s^i P^i.
```

It is a nonzero polynomial equation in `P` of degree at most `max(8,d)`.
For the frozen `d<=14` window, `[K(X,s,P):K(X,s)]<=14`, and the subelement
`Q=P^2` has degree at most `14`.  In characteristic zero an algebraic
univariate formal series is D-finite, so `(q_n)` satisfies an effectively
computable P-recurrence over the coefficient function field.

The cross-review then applies this recurrence to quantities of the form
`lambda_(n mod 4)(q_n)` without proving compatibility.  A recurrence for
`q_n` has coefficients depending on `X`; a de Rham quotient or residue
projection is only constant-field linear and in general does not commute
with multiplication by those coefficients.  A Picard--Fuchs/creative-
telescoping argument may well supply a recurrence for the obstruction
pairings, but it is an additional theorem.  Even after that, propagation
from finitely many zero values is pointwise only after the forward leading
coefficient is nonzero; a uniform family bound requires constructible
control of order and singular indices.  Accordingly:

```text
raw q_n P-recursive                         CONFIRMED
gate/residue coordinates P-recursive        OPEN (plausible, not automatic)
effective pointwise N0                      CONDITIONAL on that recurrence
uniform stratum/family N0                    OPEN
```

## 3. Claim B: raw-map replay

For an ordered raw first-component monomial `f_i_j x^i y^j`, the upper
compiler's literal chart is

```text
F^U=t^8 f(t^3 X,t^-1),
f_i_j x^i y^j -> f_i_j t^(8+3i-j) X^i.
```

The raw blob contains `f_15_52` with stored upper weight
`8+3*15-52=1`.  The frozen upper fixture has

```text
A=X^4-1,  H=A^2,  F_1=H=A^2,
```

so its graph relation is

```text
f_15_52=[X^15]A^2=0.
```

The lower compiler ignores the stored upper weight and recomputes, from the
same raw exponents,

```text
F^L=tau^8 f(tau^-4 xi,tau),
f_i_j x^i y^j -> f_i_j tau^(8-4i+j) xi^i.
```

Thus the same slot has lower weight `8-4*15+52=0`.  FACEPIN fixes

```text
F^L_0=a xi^2 (xi-rho)^14,
f_15_52=[xi^15]F^L_0=-14 a rho,
```

exactly as serialized in `facepin_substitution.json`.  The lower
Rabinowitsch relation inverts
`a*b*rho*f_0_8*g_0_12`; in a commutative ring every factor of an invertible
product is itself invertible.  Hence `a rho` is a unit, and in characteristic
zero the two graph relations imply the unit equation

```text
0=-14 a rho.
```

Therefore

```text
U_lin tensor_(R_raw) L_lin = 0.
```

No localization can restore a point; the localization is what makes the
nonzero lower coefficient fail closed.  Independently, the same replay for
the ordered second component gives upper
`g_23_80=[X^23](3/2)A^4=0` and lower
`g_23_80=[xi^23]b xi^3(xi-rho)^21=-21b rho`, another unit contradiction.

### Maximum licensed scope

The conclusion is exactly the emptiness of the fibre product of the two
**given graph parametrizations over the given ordered 442-slot raw ring**.
It does not invalidate either compiler alone, and it does not show that an
arbitrary upper branch-P face and the family-pinned lower face are globally
incompatible.  A broader claim would have to introduce and track any allowed
common coordinate action, upper quartic parameters, normalizer/gauge cover,
and their effect on both coefficient maps.  The current upper client fixes
`A=X^4-1` and `F_1=H` literally, while the lower client fixes a nonzero
characteristic root in the same raw coordinates; those exact frozen choices
are what the collision separates.

No heavy computation was used in this review.
