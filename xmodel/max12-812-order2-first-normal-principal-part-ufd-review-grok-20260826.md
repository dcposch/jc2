# Hostile review — principal-part formula and exact `k10=0` UFD split of the `(8,12)` order-two first normal gate

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md` |
| Target SHA-256 | `988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5` |
| Overall verdict | **REPAIR** |
| Smallest failing identity | none |
| Smallest missing hypothesis | the displayed reduced-support equality of §4 for `V(Q1*) ∩ V(k10)` after saturation-before-slice |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target and every charged local source; no Singular, Sage, msolve, Lean, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5`,
matching the required pin. Producer verdict language, the target's own
status line, charged review tokens, and the dual-prime endpoint were not
used as evidence. No file other than this review was written.

---

## Verdict

**REPAIR.**

The principal-part identity `(1.1)`, the exact `k10=0` criterion `(2.1)`,
the UFD equivalence `(3.2)`, and every coefficient in the square and
discriminant parameterizations `(3.3)`--`(3.6)` survive a hostile
rederivation. The coefficient of `N^2/K` is `+3/8`, the load term is
`+k10 K^(5/2)`, the polynomial-part convention is the `z`-Laurent
convention at infinity, and substituting `z_Lambda(w)=z0(w)+O(Lambda)`
introduces no hidden order-two term. The map `w0=K^(1/4)=z+O(z^-1)` is
unitriangular on the first seven negative coefficients, and four vanishing
coefficients of the proper fraction `R/K` force the degree-at-most-three
remainder to vanish. The square family solves every row of the first gate
for arbitrary `k10`. The target does not claim nonsquare/`k10!=0`
exclusion, full radical equality, reducedness of `Q1*`, nilpotent
structure, or strict-Rees/order-two closure.

The displayed exact theorem of §4 does not follow as written. Saturation
is taken in the full first-gate space *before* the slice `k10=0`:

```text
Q1* = (Q1 : (p,c,r)^infinity) : (n0,n1,n2,n3,k10)^infinity,
```

and the claim is

```text
support_red(V(Q1*) intersect V(k10))
  = square closure (3.3)|_{k10=0}
    union discriminant closure (3.5).
```

The argument given in §4 proves this equality for the sliced-then-saturated
object `((Q1+(k10)):(p,c,r)^infinity):(n0,...,n3,k10)^infinity`, and proves
that both named closures survive in `Q1*`. It does not control zero-normal
squarefree limits of hypothetical `k10!=0` branches of `V(Q1)`, which §5
explicitly leaves open. That is a missing hypothesis on the displayed
`Q1*` equality, not a false coefficient identity.

**REPAIR**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md` | `988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5` | target (matches required pin) |
| `xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md` | `827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc` | first-gate chart `(1.1)`, divided rows `Theta_ell`, `Q1`/`Q1*`, load exponents |
| `xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md` | `27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | `H_F(w)-g(z(w))` convention, binomial `(7.1)`, common-quartic chart, irrelevant ideal `(p,c,r)` |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md` | `aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495` | `w=K^(1/4)`; load derivative `[K^(j/4)]_-` vanishes iff `K` is square; square locus `c=0`, `p^2=4r` |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | ordinary `(8,12)` ten-tuples; affine in `(k10,k6,k2)` |
| `cases/max12_812_order2_first_normal_jet_20260826/RESULTS.md` | `c474e05fa61be48ed9271c1b5c458a875882d8554163b82566138b4eab5da46a` | dual-prime navigation only; not used as evidence |
| `cases/max12_812_order2_first_normal_jet_20260826/RESULTS.sha256` | `818f5d158af41eb93c7a945f46ad143340e9afaa0086eaabd7869c5a0d1d9715` | companion pin of the dual-prime run |

All eight hashes match the values printed in the target. The named jet
review was not used as algebraic evidence. Dual-prime component counts
and dimensions were not used as evidence for any identity in §§1--4.

---

## Strongest exact theorem that survives

Work over a characteristic-zero field `L` in the first-normal chart of the
charged one-parameter family, with

```text
K = z^4 + p z^2 + c z + r,
N = n3 z^3 + n2 z^2 + n1 z + n0,
f_Lambda = K^2 + Lambda N,
w_Lambda = f_Lambda^(1/8),
w0 = K^(1/4),
H_Lambda(T) = T^12 + Lambda^2 k10 T^10 + O(Lambda^6),
```

and with the frozen sign convention `H(w)-g(z(w))=sum_ell r_ell w^(-ell)`.
Let `[ ]_-^z` be the strictly negative part of a `z`-Laurent series at
infinity after subtracting its polynomial part in `z`. Let `z0(w)` be the
monic inverse of `w0=z+O(z^-1)`. Let `q_ell` be the special fibre of the
divided rows `Theta_ell`, and `Q1=(q_1,...,q_7)`, as in the charged jet
theorem.

1. The coefficient of `Lambda^2` in the full Faber tail is exactly
   ```text
   sum_(ell>=1) q_ell w^(-ell)
     = [ (3/8) N^2/K + k10 K^(5/2) ]_-^z
       evaluated at z=z0(w).                         (1.1)
   ```
   The seven rows of `Q1` are the first seven coefficients of this series.
   The binomial coefficient is `+3/8`, not `-3/8`. The load contribution
   is `+k10 [K^(5/2)]_-^z`. Substitution of
   `z_Lambda(w)=z0(w)+O(Lambda)` changes the `Lambda^2` coefficient only
   in order `>=3`.

2. On the hyperplane `k10=0`,
   ```text
   q1=...=q7=0    iff    K divides N^2 in L[z].     (2.1)
   ```
   Composition by `z0(w)` is unitriangular on the first seven negative
   coefficients, and the first four negative `z`-coefficients of the
   proper fraction `R/K` (where `N^2=A K+R`, `deg R<=3`) are a
   unitriangular transform of the four coefficients of `R`. Four rows
   already give the equivalence; seven are available. Conversely, if
   `K|N^2` then the negative part in `(1.1)` vanishes identically.

3. Over an algebraic closure,
   ```text
   K=prod_a (z-a)^(m_a),
   D_K=prod_a (z-a)^ceil(m_a/2),
   K|N^2    iff    D_K|N.                           (3.2)
   ```
   The odd-multiplicity (squarefree-kernel) degree of a degree-four `K`
   is even, hence `0`, `2`, or `4`. Degree four forces `deg D_K=4` and,
   with `deg N<=3`, forces `N=0`. After removing the zero-normal/load
   section, the remaining geometric points on `k10=0` are exactly:
   - the square closure
     ```text
     K=(z^2+s)^2,
     N=(z^2+s)(alpha z+beta),                       (3.3)
     ```
     equivalently `c=0`, `p^2=4r`, `2 n1=p n3`, `2 n0=p n2`, of
     dimension three on `k10=0`;
   - the discriminant closure
     ```text
     L=z-a,   S=z^2+2 a z+d,
     K=(z-a)^2 (z^2+2 a z+d),
     N=lambda (z-a)(z^2+2 a z+d),                   (3.5)
     ```
     with coordinates `(3.6)`, covering partitions `[2,1,1]` and `[3,1]`,
     of dimension three on `k10=0`.
   The partition `[1,1,1,1]` occurs only with `N=0` and is absent from the
   nonzero first-contact open of the sliced ideal.

4. The same formulae `(3.3)`--`(3.4)` solve every row of `Q1` for
   arbitrary `k10`, because `N^2/K=(alpha z+beta)^2` and
   `K^(5/2)=(z^2+s)^5` are polynomials. This is an exact dimension-four
   family inside `V(Q1)`, and its intersection with both saturation opens
   is nonempty, so the family survives in `Q1*`.

5. Saturation by `(p,c,r)` removes only components supported wholly at
   the weighted-projective origin. Saturation by `(n0,n1,n2,n3,k10)`
   removes only components supported wholly on the zero normal/load
   section. Individual points of those loci that lie on a retained
   component remain as affine-closure points: `s=0` in `(3.3)` and
   `(a,d)=(0,0)` in `(3.5)` are the origin, and `(alpha,beta)=(0,0)` or
   `lambda=0` are zero-normal boundary points of the two named closures.
   The zero section remains mathematically live as higher contact; its
   removal is the definition of the order-one gate.

6. The equality of reduced supports that *does* follow is the
   sliced-then-saturated statement
   ```text
   support_red V( ((Q1+(k10)):(p,c,r)^infinity)
                   :(n0,n1,n2,n3,k10)^infinity )
     = (3.3)|_{k10=0} union (3.5).
   ```
   Both closures embed into `V(Q1*) ∩ V(k10)`. The converse inclusion for
   `Q1*` itself (saturation before the slice) is not proved, because a
   squarefree zero-normal point can lie in `V(Q1*) ∩ V(k10)` only as a
   limit of a `k10!=0` branch of `V(Q1)`, and no such branch is excluded.

This is a principal-part and `k10=0` UFD theorem, plus an exact square
solution of the full first gate. It does not exclude a nonsquare `K` with
`k10!=0`, identify the characteristic-zero radical of `Q1*`, prove
reducedness or nilpotent structure, compute the `Lambda,J`-saturated
divided-family boundary, impose a strict arc, impose the terminal `[6,2]`
passport or either Taylor boundary, exclude order two, close `(8,12)`,
prove maximum twelve, or prove JC2.

---

## Attack 1 — `Lambda^2` identity: coefficient `+3/8`, load `+k10 K^(5/2)`, `z`-polynomial part, no hidden order-two term

**CONFIRMED.** Identity `(1.1)` is exact.

### Binomial at fixed `z`

The charged source-audit expansion `(7.1)` is the binomial series of
`f^(3/2)` at a common quartic. With `f_Lambda=K^2+Lambda N` and
`x=Lambda N/K^2`,

```text
(1+x)^(3/2)
  = 1 + (3/2) x + (3/2)(1/2)/2 x^2 + O(x^3)
  = 1 + (3/2) x + (3/8) x^2 + O(x^3).
```

Therefore

```text
(K^2+Lambda N)^(3/2)
  = K^3 (1 + Lambda N/K^2)^(3/2)
  = K^3 + (3/2) Lambda K N + (3/8) Lambda^2 N^2/K + O(Lambda^3).
```

The coefficient is `+3/8`, not `-3/8`. As a `z`-Laurent series at
infinity the expansion is valid: `N/K^2=O(z^-5)`, so the binomial is
`z^-1`-adically convergent. The constant term `K^3` is a polynomial of
degree `12`. The linear term `(3/2) K N` is a polynomial of degree at
most `7`. The Faber polynomial, being the `z`-polynomial part of
`f^(3/2)`, removes both. The quadratic remainder is therefore
`[(3/8) N^2/K]_-^z`.

### Load term and sign of `H-g`

The charged family scales the first active lower load as `Lambda^2 k10`,
and the next loads as `Lambda^6 k6` and `Lambda^10 k2`. The charged
convention from source-audit `(2.3)` is

```text
H_F(w) - g(z(w)) = sum_(ell>=1) r_ell w^(-ell).
```

Thus the `k10` contribution to the tail is
`Lambda^2 k10 (w^10 - F_10(f)(z(w)))`. At `Lambda=0`,
`w0^10=K^(10/4)=K^(5/2)`, and `F_10(K^2)` is the `z`-polynomial part of
`K^(5/2)`, so

```text
k10 (w0^10 - F_10(K^2)) = k10 [K^(5/2)]_-^z.
```

The sign is positive. The original audit identity `(7.2)` claiming
`F_10(K^2)=K^5` is false and is not used: the erratum replacement is
exactly this negative part `[K^(j/4)]_-` with `w=K^(1/4)`. The
`O(Lambda^6)` remainder in `H_Lambda` cannot contribute at order two.

### Polynomial-part convention in `z`, then evaluation at `z0(w)`

Let `Phi(z)` be a `z`-Laurent series at infinity, written
`Phi=P+R` with `P` a polynomial in `z` and `R=O(z^-1)`. The monic inverse
satisfies `z(w)=w+O(w^-1)`, so `R(z(w))=O(w^-1)`. In particular, for
`Phi=f^(3/2)=w(z)^12`,

```text
w^12 = P(z(w)) + R(z(w)),
```

hence `P(z(w))=w^12+O(w^-1)`. So `P` *is* the degree-twelve Faber
polynomial of `f`, and the tail `w^12-P(z(w))` equals `R(z(w))`. The
`z`-polynomial-part convention is the Faber convention. Evaluating
`[ ]_-^z` at `z=z0(w)` is therefore the correct conversion from a
`z`-remainder to a `w`-series.

### No hidden order-two term from `z_Lambda(w)`

At the inverse point one has the identities of functions of `w`,

```text
f_Lambda(z_Lambda(w)) = w^8,
```

hence

```text
f_Lambda(z_Lambda)^(3/2) = w^12,
f_Lambda(z_Lambda)^(5/4) = w^10.
```

Write the `z`-Laurent decomposition

```text
f_Lambda^(3/2)
  = K^3 + (3/2) Lambda K N
    + Lambda^2 ( [(3/8)N^2/K]_+^z + [(3/8)N^2/K]_-^z )
    + O(Lambda^3).
```

Evaluating at `z=z_Lambda(w)` and subtracting the polynomial part (which
is `g` through order two) yields

```text
w^12 - [f_Lambda^(3/2)]_+^z (z_Lambda)
  = [f_Lambda^(3/2)]_-^z (z_Lambda)
  = Lambda^2 [(3/8)N^2/K]_-^z (z_Lambda) + O(Lambda^3).
```

The charged jet theorem gives `z_Lambda(w)=z0(w)+O(Lambda)` (the first
variation `z1=-N/(2 K K')` exists and is regular as a series in `w`).
Composing a `Lambda^2` coefficient that is already a `z`-Laurent series
with `z0+O(Lambda)` produces

```text
Lambda^2 [(3/8)N^2/K]_-^z (z0(w)) + O(Lambda^3).
```

The same argument applies to the load: `f_Lambda^(5/4)=K^(5/2)+O(Lambda)`,
so `Lambda^2 k10 [f_Lambda^(5/4)]_-` differs from
`Lambda^2 k10 [K^(5/2)]_-^z (z0)` by `O(Lambda^3)`.

Equivalently, in coordinates: if `Phi(Lambda,z)=Lambda^2 Psi(z)+O(Lambda^3)`
with `Psi` independent of `Lambda`, then
`Phi(Lambda, z0+Lambda z1+...)=Lambda^2 Psi(z0)+O(Lambda^3)`. The
order-one vanishing of the unloaded tail (charged Jacobian identity
`(7.1)`, polynomial constant and linear terms) is what makes `Phi` start
at `Lambda^2`; once that is granted, moving `z` cannot create a new
order-two term. The second-order Taylor terms of the *polynomial* part
along `z_Lambda` are already absorbed by the identity
`f_Lambda(z_Lambda)^(3/2)=w^12` and do not leak into the remainder.

Thus `(1.1)` holds, and the seven rows of `Q1` are the first seven
`w`-coefficients of the right-hand side.

---

## Attack 2 — unitriangular map on seven coefficients; four coefficients of `R/K` kill the remainder

**CONFIRMED.** Criterion `(2.1)` is exact on `k10=0`.

### Expansion of `w0` and `z0`

```text
K = z^4 (1 + p z^-2 + c z^-3 + r z^-4),
w0 = K^(1/4) = z (1 + p z^-2 + c z^-3 + r z^-4)^(1/4).
```

The binomial `(1+u)^(1/4)=1+(1/4)u+O(u^2)` with `u=O(z^-2)` produces no
constant term (depression kills `z^-1` in `K/z^4`, and `z·u^2` starts at
`z^-3`). Explicitly

```text
w0 = z + (p/4) z^-1 + (c/4) z^-2 + O(z^-3) = z + O(z^-1).
```

The monic inverse is `z0(w)=w+O(w^-1)`, uniquely determined as a
`w`-Laurent series.

### Unitriangularity on seven negative coefficients

Let `S(z)=sum_(k>=1) a_k z^-k`. Substitute `z0(w)=w (1+O(w^-2))`. Then

```text
z0(w)^-k = w^-k (1+O(w^-2))^-k = w^-k + O(w^-(k+2)).
```

The coefficient of `w^-m` in `S(z0(w))` depends only on `a_1,...,a_m`:
`z0^-k` starts at order `k`, so there is no leakage from `a_(m+1)` or
higher into the first `m` `w`-coefficients. Ordering `(a_1,...,a_7)` to
`(q_1,...,q_7)`, the map is triangular with ones on the diagonal
(`q_m=a_m` plus a polynomial in `a_1,...,a_(m-1)` and the coefficients of
`z0`). It is an automorphism of `A^7`. Vanishing of `q_1,...,q_7`
therefore forces vanishing of `a_1,...,a_7`, and in particular of
`a_1,...,a_4`.

On `k10=0` the series in `(1.1)` is `(3/8)[N^2/K]_-^z` evaluated at
`z0(w)`. In characteristic zero, `3/8≠0`, so the first seven negative
`z`-coefficients of `N^2/K` vanish.

### Proper fraction `R/K`

Divide `N^2=A K+R` in `L[z]` with `deg R<=3`. Then
`N^2/K=A+R/K` and `[N^2/K]_-^z=[R/K]_-^z`. Write
`R=r3 z^3+r2 z^2+r1 z+r0` and

```text
K = z^4 (1 + p z^-2 + c z^-3 + r z^-4),
R/K = (r3 z^-1 + r2 z^-2 + r1 z^-3 + r0 z^-4)
      (1 + p z^-2 + c z^-3 + r z^-4)^-1.
```

The inverse of the monic leading-one factor is `1+O(z^-2)` (again no
`z^-1` term, by depression). The first four negative coefficients of
`R/K` are therefore

```text
[z^-1] = r3,
[z^-2] = r2,
[z^-3] = r1 + r3 · (coefficient of z^-2 in the inverse),
[z^-4] = r0 + (linear combination of r2, r3).
```

This `4×4` map, ordered `(r3,r2,r1,r0)`, is unitriangular with diagonal
one because `K` is monic of degree four. Vanishing of the first four
negative coefficients forces `R=0`, hence `K|N^2`.

The same `4×4` block is closed under composition with `z0` (Attack 2
first paragraph with `m=4`), so four vanishing *`w`*-coefficients already
suffice. Seven rows are surplus. Conversely, if `K|N^2` then `N^2/K` is a
polynomial, the negative part in `(1.1)` is identically zero, and every
`q_ell` vanishes, not merely the first seven.

No completeness issue arises from the infinite tail of `1/K`: once `R=0`
the entire negative series vanishes. The origin `(p,c,r)=(0,0,0)` is
`K=z^4`, still monic of degree four, and the same `4×4` is the identity.

---

## Attack 3 — `K|N^2 iff D_K|N`; partitions; every coefficient of `(3.3)`--`(3.6)`

**CONFIRMED.** The UFD classification and both parameterizations are
exact, including depression.

### Valuations

Over an algebraic closure, `K=prod_a (z-a)^(m_a)`. For each root,

```text
m_a <= 2 v_a(N)    iff    v_a(N) >= ceil(m_a/2).
```

The right-hand side is `D_K|N` with the displayed `D_K`. Over `L[z]`
itself, the same statement holds with irreducible factors in place of
linear factors: `L[z]` is a UFD in characteristic zero. This is `(3.2)`,
including every repeated-root profile. When `N=0` both sides hold for
every `K`, so `[1,1,1,1]` with `N=0` is included in `K|N^2` and is
removed only by the nonzero-normal saturation, not by the UFD relation.

### Even degree of the odd-multiplicity kernel

The target's phrase “squarefree kernel of `K` has even degree `0`, `2`,
or `4`” is the odd-multiplicity part (the product of `(z-a)` over `a`
with `m_a` odd), not the radical. Degree of `K` is even, the even-multiplicity
contribution is even, hence the number of odd-multiplicity roots is even.
The five partitions of four and their kernels are:

| partition | odd-kernel degree | `deg D_K` | `N` on `k10=0` |
|---|---|---|---|
| `[4]` | `0` | `2` | square family, `s` a square |
| `[2,2]` | `0` | `2` | square family |
| `[3,1]` | `2` | `3` | discriminant family, `S(a)=0` |
| `[2,1,1]` | `2` | `3` | discriminant family, `S` squarefree |
| `[1,1,1,1]` | `4` | `4` | forces `N=0` |

Degree four of `D_K` with `deg N<=3` forces `N=0`, as claimed. After
removing the zero-normal/load section, only the square and discriminant
closures remain as geometric points of the *sliced* first-contact locus.

### Square closure `(3.3)`--`(3.4)`, including depression

A monic quartic square is `(z^2+a z+b)^2`. Expanding,

```text
z^4 + 2a z^3 + (a^2+2b) z^2 + 2 a b z + b^2.
```

Depression kills the `z^3` coefficient, so `2a=0`, hence `a=0` in
characteristic zero. Thus `K=(z^2+s)^2` with `s=b`, and

```text
p=2s,    c=0,    r=s^2,    p^2=4r,
```

which is the erratum square locus `(E.2)`. For this `K`,
`D_K=z^2+s` (two double roots if `s≠0`; `D_K=z^2` if `s=0`). With
`deg N<=3` one has `N=(z^2+s)(alpha z+beta)`, which is `(3.3)`. Expanding,

```text
N = alpha z^3 + beta z^2 + s alpha z + s beta,
```

so `n3=alpha`, `n2=beta`, `n1=s alpha`, `n0=s beta`. Then
`2 n1=2 s alpha=p n3` and `2 n0=2 s beta=p n2`, which is `(3.4)`.
Conversely, `c=0` and `p^2=4r` give `s=p/2`, and the two linear
relations reconstruct `N=(z^2+s)(n3 z+n2)`.

On `k10=0` the free parameters are `(s,alpha,beta)`, or equivalently
`(p,n3,n2)`: dimension three in `(p,c,r,n0,...,n3,k10)`.

### Discriminant closure `(3.5)`--`(3.6)`, including depression

If the odd kernel has degree two, write `K=L^2 S` with `L` monic linear
and `S` monic quadratic (squarefree off the `[3,1]` stratum; sharing a
root with `L` on that stratum). Put `L=z-a` and
`S=z^2+sigma z+d`. Then

```text
K = (z^2-2 a z+a^2)(z^2+sigma z+d).
```

The `z^3` coefficient is `sigma-2a`. Depression forces `sigma=2a`, which
is the displayed formula for `S`. Expanding the product,

```text
(z^2-2 a z+a^2)(z^2+2 a z+d)
  = z^4 + (d-3 a^2) z^2 + 2 a (a^2-d) z + a^2 d.
```

(The two `z^3` contributions `2a` and `-2a` cancel.) This is

```text
p = d-3 a^2,
c = 2 a (a^2-d),
r = a^2 d,
```

matching the first three lines of `(3.6)`.

Now `D_K=L S` in both remaining partitions: for `[2,1,1]` one has
`D_K=(z-a)S`; for `[3,1]` one has `S=(z-a)(z-b)` and
`D_K=(z-a)^2(z-b)=(z-a)S`. Since `deg D_K=3=deg N` (unless `N=0`),
necessarily `N=lambda L S`, which is `(3.5)`. Expanding,

```text
(z-a)(z^2+2 a z+d)
  = z^3 + a z^2 + (d-2 a^2) z - a d,
```

so

```text
n3 = lambda,
n2 = a lambda,
n1 = (d-2 a^2) lambda,
n0 = -a d lambda,
```

matching the rest of `(3.6)`, together with `k10=0`. Free parameters
`(a,d,lambda)`: dimension three on the `k10=0` slice.

When `d=a^2`, `S=(z+a)^2` and `K=(z^2-a^2)^2`, which is the square
locus with `s=-a^2`. Then
`N=lambda(z-a)(z+a)^2=(z^2-a^2)(lambda z+lambda a)`, a proper subfamily
of `(3.3)`. The discriminant closure meets the square locus and is not
equal to it. On `[3,1]`, `S(a)=0` gives `d=-3 a^2`, and
`S=(z-a)(z+3a)` as required by `-(a+b)=2a`.

The `[1,1,1,1]` case has `D_K=K` of degree four, hence `N=0` only, and
is absent from the nonzero first-contact *open* of the sliced ideal, as
claimed.

Every displayed coefficient in `(3.3)`--`(3.6)` matches the expansion.
Depression is forced, not optional, in both families.

---

## Attack 4 — saturations: components versus points; equality after saturation-before-slice

**REPAIR.** The geometric meaning of both saturations is correctly
stated. The displayed reduced-support equality for `Q1*` does not follow
from the `k10=0` analysis when saturation is taken before the slice.

### Components versus individual points

Multi-generator saturation has the standard semantics, already recorded
in the charged jet theorem:

```text
V((I:m^infinity):n^infinity)
  = closure( V(I) \ (V(m) union V(n)) ).
```

Components supported wholly on `V(m)` or `V(n)` are deleted. Points of
`V(m)` or `V(n)` that lie on a component *not* contained in that locus
are restored by taking closure.

- `(p,c,r)^infinity` is the irrelevant ideal of the weighted cone
  `P(2,3,4)`, as in source-audit `(6.1)`--`(6.2)`. It removes only
  components supported at the vertex. It is not saturation by the product
  `p c r`, which would delete the coordinate faces.
- On the square family, `s=0` is exactly `(p,c,r)=(0,0,0)`. The family
  is not contained in the vertex (`s` is free), so it is not deleted, and
  the point `s=0` remains as an affine-closure point. The source open
  `s≠0` is the complement of the vertex *inside* the family, not a
  deletion of the component.
- On the discriminant family, `(a,d)=(0,0)` is likewise the vertex.
  Same distinction.
- `(n0,n1,n2,n3,k10)^infinity` removes components supported wholly on
  the zero normal/load section. The square family is not so supported
  (`(alpha,beta)` is free, and `k10` is free in the full gate). The
  discriminant family is not so supported (`lambda` is free). The points
  `(alpha,beta)=(0,0)` and `lambda=0` remain as affine-closure points of
  those two components. The source first-contact open is
  `(alpha,beta)≠(0,0)` and `lambda≠0`.
- The whole 3-space `{N=0, k10=0, K arbitrary}` *is* supported on
  `V(mN)` and *is* a closed subset of `V(Q1)` (if `N=0` and `k10=0` then
  `(1.1)` vanishes for every `K`). As a component of the sliced ideal
  `Q1+(k10)` it is deleted by `mN`-saturation. That is the correct
  isolation of contact order one. The zero section remains live as
  higher-contact geometry of the divided Rees family; its removal here
  is only the definition of the gate.

This part of §4 is exact, and it is the right distinction between
removing a component and excluding an individual affine-closure point.

### Why the displayed equality does not follow for `Q1*`

The object `Q1*` is formed in the full first-gate space, with `k10` still
a coordinate. Then one intersects with `V(k10)`. As closed sets,
`V(Q1*) subset V(Q1)`, so every point of `V(Q1*) ∩ V(k10)` lies in
`V(Q1) ∩ V(k10)`. By `(2.1)` that slice is

```text
(3.3)|_{k10=0}  union  (3.5)  union  Z,
```

where `Z={N=0, k10=0, K arbitrary}`. The two named closures already
contain the *non-squarefree* part of `Z`: `lambda=0` in `(3.5)` is every
depressed quartic with a repeated root (any such quartic is
`(z-a)^2(z^2+2 a z+d)` after depression), and `alpha=beta=0` in `(3.3)`
is every square quartic with `N=0`. The complement

```text
Z_sf := { N=0, k10=0, K squarefree of degree four }
```

is the residual piece.

Slicing first, then saturating, deletes `Z_sf`. Indeed, inside
`V(k10)` one has `U_0 := (V(Q1) ∩ V(k10)) \ (V(mK) ∪ V(mN))` equal to
the two named families minus the origin and minus their zero-normal
boundaries. The discriminant of `K` vanishes on both families, so the
closure of `U_0` cannot meet `Z_sf`. This proves

```text
support_red V( ((Q1+(k10)):(p,c,r)^infinity)
                :(n0,n1,n2,n3,k10)^infinity )
  = (3.3)|_{k10=0} union (3.5).
```

Both families have points in both saturation opens, so neither is
deleted, which is the target's ⊇ direction and is correct for `Q1*`
as well: the square and discriminant closures embed into
`V(Q1*) ∩ V(k10)`.

Saturating *before* the slice is a different operation. A point of
`Z_sf` lies in `V(Q1*)` if and only if it lies in
`cl(V(Q1) \ (V(mK) ∪ V(mN)))`. It cannot be approached from within
`U_0`, as just shown. Any approximating net in the complement of
`V(mK) ∪ V(mN)` must therefore have `k10≠0`. Existence of such a net is
precisely a `k10≠0` branch of `V(Q1)` specializing to a squarefree
zero-normal point. Section 5 of the target states that no such branch is
excluded: cancellation of the first seven coefficients of `(1.1)` at a
nonsquare `K` with `k10≠0` is an unproved finite Padé lemma.

The target's ⊆ justification — “every point on the `k10=0` slice
satisfies `(2.1)`” — only returns the larger set
`(3.3)|_{k10=0} ∪ (3.5) ∪ Z`. Passing from that set to the two named
closures uses deletion of `Z_sf`, which is legitimate after slicing and
not justified for `Q1*`. The missing hypothesis is therefore:

```text
either form the colon of the sliced ideal Q1+(k10),
or exclude k10!=0 specializations onto Z_sf.
```

Without one of those, the displayed equality

```text
support_red(V(Q1*) intersect V(k10))
  = (3.3)|_{k10=0} union (3.5)
```

is an overclaim. It is not a false coefficient identity, and no
counterexample is produced (producing one would be the Padé lemma's
counterexample, which is out of scope and computationally forbidden
here). The claim as written does not follow.

The rest of the saturation paragraph — source opens versus affine
closures, higher-contact liveness of the zero section, reduced-support
rather than reducedness of the scheme — is correctly delimited.

---

## Attack 5 — square family solves the full first gate; no overclaim of Padé, radical, reducedness, or closure

**CONFIRMED** for the square solution and the firewall.
**REPAIR** does not come from this attack: the target does not claim the
forbidden extras.

On `(3.3)`,

```text
N^2/K = (z^2+s)^2 (alpha z+beta)^2 / (z^2+s)^2
      = (alpha z+beta)^2,
```

a polynomial, so `[(3/8)N^2/K]_-^z=0`. For the load,

```text
K^(5/2) = ((z^2+s)^2)^(5/2) = (z^2+s)^5,
```

a polynomial of degree ten. Equivalently, the monic fourth root is the
Laurent series `w0=z(1+s z^-2)^(1/2)`, and

```text
w0^10 = z^10 (1+s z^-2)^5 = (z^2+s)^5,
```

the same polynomial. Hence `[K^(5/2)]_-^z=0` for every `k10`. Both
summands of `(1.1)` vanish, so every `q_ell` vanishes. The family
`(3.4)` with `k10` free is an exact dimension-four closed subset of
`V(Q1)`. It meets both saturation opens (`s≠0` and `(alpha,beta)≠(0,0)`),
so its closure survives in `Q1*`. This is a solution of the full first
gate, not merely of the `k10=0` slice.

The target states, in §5, that this does *not* exclude cancellation of
the first seven coefficients of `(1.1)` at a nonsquare `K` with
`k10≠0`. Dual-prime bases are charged as navigation only and are not
used to identify the characteristic-zero radical, the number of
components of `Q1*`, or reducedness. Section 4 explicitly refuses
equality of nonreduced ideals, exclusion of embedded components, and
scheme multiplicities. Section 6 and the closing paragraph refuse a
strict arc, the terminal `[6,2]` passport, either Taylor boundary,
exclusion of order two, closure of `(8,12)`, maximum twelve, and JC2.

Those refusals are accurate. The only overclaim found in the note is the
displayed reduced-support equality of §4 for the *already saturated*
scheme `Q1*` after intersecting with `k10=0` (Attack 4). That is a
missing hypothesis, not a claim of nonsquare exclusion, radical
equality, reducedness, nilpotents, or order-two closure.

---

## Attacks that failed to break a numbered coefficient identity

Reading `(1.1)` with coefficient `-3/8` (the binomial of `(1+x)^(3/2)`
is `+3/8`; charged `(7.1)` has the same sign). Taking the load term as
`-k10 K^(5/2)` (the frozen convention is `H-g`, so the sign is
positive). Treating `[ ]_-^z` as a `w`-remainder taken before inverting
(the `z`-polynomial part *is* the Faber polynomial because
`z(w)=w+O(w^-1)`, and `R(z(w))` is already the `w`-tail). Extracting a
hidden order-two term from `z_Lambda=z0+Lambda z1` (the remainder
already starts at `Lambda^2`, and `f_Lambda(z_Lambda)^(3/2)=w^12`
identically). Claiming the first seven `w`-coefficients mix in `a_8` and
higher (the substitution `z0=w+O(w^-1)` gives a closed unitriangular
`7×7` block). Claiming four coefficients of `R/K` are insufficient
because `1/K` has an infinite tail (the `4×4` is invertible, and `R=0`
kills the tail). Missing the partition `[2,1,1]` by reading “squarefree
kernel” as the radical of degree three (the odd-multiplicity kernel has
degree two). Dropping depression in `(3.5)` (the coefficient `2a` is
forced by vanishing of `z^3`). Forgetting that `[1,1,1,1]` satisfies
`K|0` (it does; it is removed by `mN`-saturation, not by `(3.2)`).
Treating `s=0` or `(a,d)=(0,0)` as deleted by `(p,c,r)^infinity` (those
are vertices of retained components). Claiming the square family fails
for `k10≠0` (both summands of `(1.1)` are polynomials). Importing dual
primes as a characteristic-zero radical statement (the target forbids
this). Importing a strict arc, `[6,2]`, a Taylor boundary, or order-two
closure (none is used).

---

## Required repair

Replace the displayed equality of §4 by the sliced-then-saturated
statement, which is what the argument proves:

```text
support_red V( ((Q1+(k10)):(p,c,r)^infinity)
                :(n0,n1,n2,n3,k10)^infinity )
  = square closure (3.3)|_{k10=0}
    union discriminant closure (3.5).
```

Keep the paragraph that both closures meet both saturation opens, so
neither is deleted, and that their affine closures may retain `s=0`,
`(a,d)=(0,0)`, `(alpha,beta)=(0,0)`, and `lambda=0`. State separately
that both closures embed into `V(Q1*) ∩ V(k10)`, and that equality for
`Q1*` itself requires either the sliced colon above or exclusion of
`k10≠0` specializations onto squarefree zero-normal points — which is
the Padé lemma already listed as the next exact gate.

Do not otherwise reopen `(1.1)`, `(2.1)`, `(3.2)`--`(3.6)`, the square
solution of the full first gate, or the firewall.

---

## Scope that remains open

Whether a nonsquare `K` with `k10≠0` can cancel the first seven
coefficients of `(1.1)`. The characteristic-zero radical of `Q1*`, its
reducedness, embedded primes, and nilpotent structure. The
`Lambda,J`-saturated divided-family boundary. Higher-contact jets,
including the zero section. Either Taylor family. The terminal `[6,2]`
passport. Emptiness or nonemptiness of a strict arc. Closure of order
two, of `(8,12)`, of maximum twelve, or of JC2.

REPAIR
