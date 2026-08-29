# Hostile review: finite ends, marked asymptotic components, and monodromy

**Reviewer:** Sol Ultra, independent hostile pass  
**Date:** 2026-08-27  
**Target:** `xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md`  
**Target SHA-256:** `0f201502716ca9c9bf33718412739e0254981c2eb7204657dc78ee7fbcd653c1`  
**Scope:** the stated finite-end identity, its primary-source provenance, the
component-degree congruence, the residue-A `169 -> 48` census, and the claimed
monodromy perimeter.  No `20260827T2137Z` peer-ideation report was read.  No
canonical ledger, AWS lane, or `jc2-lean` object was touched.

## Verdict

**CONFIRMED WITH TWO NON-LOAD-BEARING TYPING REPAIRS.**

1. The finite-end mass identity is not new: it is the **second equation printed
   as `(4.4)` on p. 305** of Chau 1999.  The paper also prints a different
   local-degree formula as `(4.4)` on p. 304, so page and formula must accompany
   the equation number.  Chau's Theorem C is exactly the claimed two-coordinate
   coupling after multiplying both sides by `-1`.
2. The normalization-degree divisibility and marked-type congruence are correct.
   The primary theorem first supplies a possibly non-birational polynomial
   parametrization; one short normalization-descent step, omitted in the target,
   is needed before writing `deg(f o nu_j)=alpha*h_j`.
3. The residue-A census is exactly `169 -> 48`.  This is a **necessary parity
   filter** on the old unmarked rows, not an if-and-only-if marked-component
   realization theorem.  All 48 rows have the previously banked transitive
   unmarked tuple witnesses, so the filter does not kill the family.
4. The no-imprimitivity/no-degree-bound conclusion is correct in its stated
   `T-RH`-only scope.  The scalable control proves survival of `S_d`; it does not
   separately construct `A_d`, so “cannot exclude `A_d/S_d`” should be read as
   “cannot exclude the large primitive `A_d`-or-`S_d` alternative.”

**Promotable content:** only the marked-component divisibility as a cheap
necessary filter, together with Chau's already-known mass coupling.  Nothing in
this report promotes a family exclusion, a primitive-monodromy obstruction, a
degree bound, or a construction of the normalized components of `A(F)`.

## 1. Primary-source custody

### 1.1 Chau 1999: the vertical identity and Theorem C

The checked repository PDF is

```text
refs/chau1999_apm71_full.pdf
SHA-256 ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
```

In Section 4.3, Chau takes a generic level `P=c`, its compact normalization
`V`, and the meromorphic extension of `Q`.  He explicitly says that the degree
on a finite branch at infinity is the topological degree of the restriction to
the corresponding punctured disc.  Riemann--Hurwitz then gives, on p. 305,

```text
chi({P=c}) = deg_geo(F) - sum_{gamma in b_P(c)} deg_gamma(F).
```

This is the target's identity.  If `D=deg_geo(F)` and a finite end `S` has
`Q-b=t^e * unit`, then `deg_gamma(F)=e`.  Since the smooth generic affine fibre
is connected, `chi=1-b1`, hence

```text
sum_S e_S = D + b1(P^{-1}(c)) - 1.
```

There is a bibliographic trap: p. 304 labels the generic/special local degree
formula in Lemma 4.3 as `(4.4)`, and p. 305 again labels the generic-fibre Euler
formula `(4.4)`.  The target gives p. 305 and quotes the formula, so its use is
unambiguous and correct; future pins should say “the second printed (4.4),
p. 305.”

Theorem C on pp. 287--288 states

```text
deg P * (chi_Q - D) = deg Q * (chi_P - D).
```

Equivalently,

```text
deg P * (D-chi_Q) = deg Q * (D-chi_P).
```

Thus, with `M_f=D-chi_f`, `M_g=D-chi_g`,
`deg P=B*alpha`, and `deg Q=B*beta`, it gives

```text
M_f/alpha = M_g/beta.
```

The target's attribution to Theorem C is exact.

Primary record: N. V. Chau, *Non-zero constant Jacobian polynomial maps of
C^2*, Ann. Polon. Math. 71 (1999), 287--310,
<https://doi.org/10.4064/ap-71-3-287-310>.

### 1.2 Component degrees

Chau's 1999 Theorem 4.4(E1) states the coordinate-degree ratio for each
dicritical polynomial parametrization.  The later primary statement is even
more explicit: Theorem 1 of
<https://arxiv.org/pdf/math/0305088> says that when

```text
deg P=K*alpha,  deg Q=K*beta,  gcd(alpha,beta)=1,
```

each irreducible component of the nonproper set has a polynomial
parametrization whose leading coordinate degrees are `m*alpha` and
`m*beta`.  The fetched PDF has SHA-256
`8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f`.

The source parametrization need not itself be the normalization map.  Let
`nu_j:A^1_s -> A_j` be the normalization and let a source parametrization
factor generically through it by a polynomial `s=r(t)` of degree `rho`.
Then

```text
deg p(t) = rho * deg(P o nu_j),
deg q(t) = rho * deg(Q o nu_j).
```

The source ratio therefore descends to

```text
deg(P o nu_j) / deg(Q o nu_j) = alpha/beta.
```

Both degrees are positive integers, so coprimality gives uniquely

```text
k_j=deg(P o nu_j)=alpha*h_j,
l_j=deg(Q o nu_j)=beta*h_j,
h_j >= 1.
```

This repairs the one omitted step without changing the conclusion.

### 1.3 Fibre deficit equals nonproperness

Proposition 6 of Jelonek 1993 says that a dominant polynomial map is proper
at `q` exactly when its finite fibre has full generic multiplicity.  For a
Keller map every affine local multiplicity is one.  Therefore

```text
delta(q)=D-#F^{-1}(q)
```

is precisely the nonproper fibre deficit.  The checked primary PDF is
<https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf>, pp. 261--262.

## 2. Independent derivation of the finite-end formula

Let the compact generic fibre have genus `g`, let it have `p` pole punctures
and `r` finite-end punctures, and let the pole orders be `m_i`.  The restriction
of the other coordinate has degree `D`; hence `sum_i m_i=D`.  The Keller
condition makes the restriction unramified at every affine point.  Its complete
ramification divisor is therefore supported at punctures and has degree

```text
sum_poles (m_i-1) + sum_finite (e_S-1)
= (D-p) + (sum_S e_S-r).
```

Riemann--Hurwitz gives

```text
2g-2 = -2D + (D-p) + (sum_S e_S-r),
```

so

```text
sum_S e_S = D + 2g+p+r-2
           = D + b1(C)-1.
```

For a generic target point `q=(a,b)` on `A(F)`, the complete fibre of the
degree-`D` map on the compactified vertical fibre consists of the affine
preimages, each of multiplicity one, plus the finite boundary ends above `q`.
Consequently

```text
delta(q)=D-#F^{-1}(q)=sum_{S above q} e_S.
```

This independently recovers both the local deficit formula and Chau's global
identity.

## 3. What the local inertia does and does not record

At a generic transverse intersection with `A_j`, a boundary end has local
normal form `z=t^e*unit`.  It contributes an `e`-cycle to the meridian.  An
affine preimage contributes a fixed sheet.  Hence

```text
index(sigma_q) = sum(e-1),
delta(q)       = sum(e).
```

For `e=1`, the missing boundary sheet is also a fixed point of `sigma_q`.
Thus the ordinary conjugacy class cannot distinguish it from an affine sheet
that extends across `q`.  This is a genuine information loss, not merely a
naming convention.  A marked profile must retain at least

```text
(boundary e=1 fixed points) versus (affine fixed points),
```

as well as all nontrivial boundary cycles.

Three levels must remain separate:

1. **Component:** an irreducible normalized component `A_j`; its generic
   whole marked profile is constant away from finitely many exceptional points.
2. **Branch value:** one point of `A_j intersect {P=a}`.  A single branch value
   may carry several boundary ends/cycles.
3. **Source sheet:** one of the `D` sheets of the Keller cover over the target
   complement.  The `alpha*h_j` branch values belonging to `A_j` are not a
   block of these `D` sheets.

The target keeps these levels separate.  “Component block” is safe only as
shorthand for a braid orbit of **branch values**; it must never be imported as
a block system for source-sheet monodromy.

## 4. Marked component congruence

Fix a generic vertical line.  It meets `A_j` in exactly
`k_j=alpha*h_j` distinct transverse points.  The unordered marked profile is
constant on the generic locus of `A_j`; tangential continuation may permute
its ends but cannot change the profile.  Therefore, for every fixed complete
marked profile `tau`,

```text
n_tau = sum_{j: tau_j=tau} k_j
      = alpha * sum_{j: tau_j=tau} h_j,
```

and hence `alpha | n_tau`.

The same conclusion holds after forgetting some marking: the count of an
unmarked type is a sum of marked-type counts, each divisible by `alpha`.
Likewise, the total number of marked boundary cycles of any chosen length is
divisible by `alpha`, after weighting each component by its fixed multiplicity
of such cycles.  None of these congruences identifies a source-sheet block.

Grouping the local deficits also gives

```text
M_f = sum_j k_j*delta_j = alpha * sum_j h_j*delta_j,
M_g = sum_j l_j*delta_j = beta  * sum_j h_j*delta_j,
```

which agrees exactly with Theorem C.  This is a consistency check, not a
second independent exclusion.

## 5. Residue-A census: exact `169 -> 48`

The banked clean control has `D=6`, normalized degree pair
`(alpha,beta)=(2,3)`, and x-side unmarked branch-value counts

```text
(2)^a (2,2)^b (2,2,2)^c,
a+2b+3c=42.
```

A fresh integer enumeration gives 169 nonnegative solutions.  The component
congruence forces every count of a fixed marked profile to be even.  Under the
clean no-sharing control, forgetting any `e=1` marking cannot spoil this
necessity, so `a,b,c` must all be even.  Put

```text
(a,b,c)=2(A,B,C).
```

Then

```text
A+2B+3C=21.
```

For `C=0,...,7`, the numbers of possible `B` are

```text
11, 10, 8, 7, 5, 4, 2, 1,
```

whose sum is exactly `48`.  The proposed negative control
`(a,b,c)=(0,3,12)` satisfies `a+2b+3c=42` but fails the parity condition.

Independent replay of

```text
cases/grok_monodromy.py
SHA-256 c8380e47a3e734d4dc1ca321cb9e895a9e4d7780bec46d73dbc426ed5f459fd7
```

returned `52 checks, 0 FAIL`, including `169 / 169` explicit transitive
unmarked witnesses.  Hence every one of the 48 parity survivors already has
an unmarked transitive witness.  In particular `(42,0,0)` survives and the
banked witness generates full `S_6`.

The logical status is therefore:

```text
odd a or b or c  => impossible under the stated clean component control;
all even         => survives this necessary filter only.
```

Evenness does not manufacture the normalized components, attach all `e=1`
ends, establish horizontal compatibility, or realize a Keller map.  In the
proposed filter, “retain iff even” is an operational row-retention rule, not a
mathematical sufficiency claim.

## 6. Primitive-monodromy and degree stress test

For every `D>=2`, consider

```text
g_D(z)=z^D-Dz
```

on `P^1`, and remove infinity and the `D-1` roots of `z^(D-1)=1` from the
source.  The finite critical points are simple and have pairwise distinct
critical values `-(D-1)zeta`.  Thus the restricted map has no ramification on
the affine punctured source, while each removed finite end has `e=2`.  The
source has first Betti number `D-1`, and

```text
sum e = 2(D-1) = D + (D-1) - 1.
```

Every finite inertia is a transposition.  The cover is connected, hence its
transposition graph is connected; transpositions along a connected graph
generate `S_D`.  This establishes, for arbitrarily large `D`, that the mass
identity alone neither bounds degree nor forces imprimitivity.

This control is intentionally not a Keller surface map.  Its exact force is
refutational: any argument using only `T-RH` and ordinary local inertia cannot
derive a degree bound or an imprimitive monodromy theorem.  It demonstrates
`S_D`, not a separate `A_D` family.  At the residue-A passport level the
stronger parity condition also leaves the full-`S_6` row `(42,0,0)`, so the
new congruence does not itself create a primitive-group kill.

## 7. Final disposition

```text
T-RH / Chau p.305:                  CONFIRMED, KNOWN.
Two-coordinate mass coupling:       CONFIRMED, Chau Theorem C.
Normalization degree alpha*h_j:     CONFIRMED after one descent sentence.
Marked-profile divisibility:         CONFIRMED, promotable as NECESSARY.
Residue-A 169 -> 48:                 CONFIRMED exactly.
48 survivors marked-realizable:      NOT CLAIMED and NOT PROVED.
Family kill / degree bound:           NO.
T-RH -> imprimitive monodromy:        REFUTED by scalable S_D control.
```

The clean campaign action is to add the parity/congruence filter to a future
**fully marked** Avenue-25 component CSP.  It should remain dormant as a proof
avenue until a complete boundary book supplies every finite end, especially
`e=1`, and assigns those ends to normalized components of `A(F)`.
