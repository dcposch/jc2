# Hostile review — `(8,12)` order two: exact-square affine-`mu2` support

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-exact-square-affine-mu2-support-theorem-20260826.md` |
| Target SHA-256 | `75c7ec8431781d466501da9bf97f909e05392c0cafc2d37ff200dacc2d497365` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged artifacts were opened only because they are named; no producer status line, no `PASS` token, no proposed-component label, and no printed radical/standard basis is evidence |
| Method | source reading, SHA-256 of the target and the six charged pins, hand derivation of every displayed identity, and independent reconstruction of the seven tails from the logarithmic-differentiation recurrence; no Singular, Sage, SymPy, msolve, Lean, or CAS Groebner/radical |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`75c7ec8431781d466501da9bf97f909e05392c0cafc2d37ff200dacc2d497365`,
matching the required pin. Independently recomputed SHA-256 of the six
artifacts pinned in target §1 match those pins. Every path named in the
charged `EVIDENCE.sha256` and `FREEZE.sha256` rehashes to the printed
digest. Producer verdict language, the target's own status line, the
string `PASS_AFFINE_MU2_PROBE`, the printed radical and `minAssGTZ`
output, and both exact-Q and `F_65521` endpoint tokens were not used as
evidence. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

The seven negative Laurent coefficients of
`H=sqrt(Q)*(Q^2+beta*Q+gamma)` are the index-shifted combination
`E_ell=a_(10+ell)(5/2)+beta*a_(6+ell)(3/2)+gamma*a_(2+ell)(1/2)`.
Integer-content denominators are exactly those of `(3.1)`. The affine
receiver is `E1=E3=E4=E5=E6=E7=0` together with `E2-1024*mu2=0`; it is
not `E2=mu2`.

On `D(c)` the first two odd integerized rows force
`beta=5*Delta/8` and `gamma=(15*Delta^2+40*p*c^2)/128`. The next two odd
rows collapse to the displayed `F5,F7`. For `p!=0` the polynomial identity
`3*p*F5+F7=32*p*c^4` forces `c=0`. For `p=0` one has `F7=E4=0`
identically after that substitution, while `F5=8*(3*c^4-40*r^3)` and
`E6=-3840*r^4` force first `r=0` then `c=0`. There is no reduced point on
`D(c)`.

On `c=0` the identity `h4=-(p/2)*h2` is exact. On `D(p)` it forces
`mu2=0` and returns the charged seven-zero-tail square/Chebyshev
classification. At `p=c=0` the six non-target rows reduce to a single
equation `E6=-256*r^2*(5*r^2+8*r*beta+16*gamma)=0`; the `r=0` slice is
the square limit with `mu2=0`, and the `r!=0` slice is the displayed
affine component with factor `32` in `mu2`.

The three displayed component ideals are prime, their overlaps are
contained in the union, and the union is the reduced support over a
characteristic-zero algebraic closure. The scheme-independent equality
`(2.3)` follows by Nullstellensatz from that classification, not from the
exact-Q stdout. The `(r,t)` parametrization, the generalized-Pell
remainder, and `h10=-r^4*(t-r)/512` are correct algebraic identities on
the new component; `h10` is not a source equation of `(2.1)`.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-exact-square-affine-mu2-support-theorem-20260826.md` | `75c7ec8431781d466501da9bf97f909e05392c0cafc2d37ff200dacc2d497365` | target (matches required pin) |
| `cases/max12_812_order2_exact_square_affine_mu2_20260826/RESULT.md` | `55adc49f379b36b425322218ccdfed9a6359ed6e6e41713543125da01f3f1f95` | named producer result; opened only because it is charged; its radical, `PASS` token, and the mislabelled equation `E2=mu2` are not evidence |
| `cases/max12_812_order2_exact_square_affine_mu2_20260826/EVIDENCE.sha256` | `f285b6df59805fa6291eef974ad45c4d05db9942a7e28482b362174e568273ef` | named evidence list; every listed file rehashes; not used as a calculation |
| `cases/max12_812_order2_exact_square_affine_mu2_20260826/FREEZE.sha256` | `88440f2a46078f0c9708587ea6db8c6d4f3e5f306affe35c94d2da521e8d4e5e` | named freeze list; every listed file rehashes |
| `cases/max12_812_order2_exact_square_affine_mu2_20260826/compile_affine_mu2.py` | `4eb04bca26c3bee1c76534f8fc02efdbb982316071e583676b65fb395f5f2c4b` | named compiler; the line `ideal I=E1,E2-1024*mu2,E3,E4,E5,E6,E7` is the affine equation actually emitted |
| `xmodel/max12-812-order2-exact-square-affine-mu2-hand-elimination-20260826.md` | `20cc74b60fdf0b599094c8b5d6cf61e48773391d3c861409ef0e20f4a8a85ff2` | charged hand elimination; identities rederived, not trusted from the page |
| `xmodel/max12-812-order2-exact-square-pell-chebyshev-support-theorem-20260826.md` | `523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf` | charged seven-zero-tail square/Chebyshev classification, used only after `c=0` and `mu2=0` |

All seven hashes match the values printed in the target. The
characteristic-65521 lane is a software control only and is not used.

The algebraic input actually used is: the recurrence for
`(1+p t^2+c t^3+r t^4)^alpha` already derived in the charged seven-zero-tail
theorem; the branch `sqrt(Q)=z^2+O(1)`; the integer-content convention
`(3.1)`; and the set-theoretic statement of that seven-zero-tail theorem
on `c=0`.

---

## Strongest exact theorem that survives

Work over a field `K` of characteristic zero. Write

```text
Q = z^4 + p z^2 + c z + r,
Delta = p^2 - 4 r,
H = sqrt(Q) (Q^2 + beta Q + gamma),
```

in the formal branch `sqrt(Q)=z^2+O(1)` at infinity, and let `h_ell` be
the coefficient of `z^{-ell}` in `H`. Integerize by `(3.1)`, and let `I`
be the ideal

```text
I = (E1, E2 - 1024 mu2, E3, E4, E5, E6, E7)
```

in `K[mu2, gamma, beta, r, c, p]`. After base change to an algebraic
closure, the reduced support of the affine receiver `(2.1)` is exactly

```text
V(c, mu2, Delta)
  union
V(c, mu2, 16 beta - 5 Delta, 256 gamma - 5 Delta^2)
  union
V(p, c, 5 r^2 + 8 r beta + 16 gamma,
      32 mu2 - r^2 (5 r + 4 beta)).
```

Equivalently, writing `I_square`, `I_Chebyshev`, `I_affine` for the three
displayed component ideals,

```text
rad(I) = I_square intersect I_Chebyshev intersect I_affine.
```

Each of those three ideals is prime. The third component is the only
reduced support not already present in the seven-zero-tail receiver
`h1=...=h7=0`. On that third component the rational parametrization
`(4.1)` and the identities `(4.2)` and the generalized-Pell remainder
are correct; `(4.2)` is not a row of `(2.1)`.

This is the exact seven-row affine Laurent receiver on the chart
`k10=1`. It does not classify `k10=0`, does not pull the identity back
through a literal total-Rees source or a target/deck tie, does not impose
correction jets, the terminal `[6,2]` passport, or either Taylor family,
does not construct or exclude a strict arc, and does not close order two,
`(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — seven Laurent coefficients, integer denominators, affine equation

**CONFIRMED.** The affine equation is `E2-1024*mu2=0`. The producer
label `E2=mu2` in charged `RESULT.md` (1) is false for the integerized
numerators and is discarded.

Logarithmic differentiation of `g^alpha` with `g=1+p t^2+c t^3+r t^4`
gives the recurrence

```text
n a_n(alpha)
  = p (2(alpha+1)-n) a_(n-2)
  + c (3(alpha+1)-n) a_(n-3)
  + r (4(alpha+1)-n) a_(n-4),
```

with `a_0=1` and `a_n=0` for `n<0`. Characteristic zero inverts every
`n=1,...,17` needed below. With `t=z^{-1}` one has
`H=z^{10} g^{5/2}+beta z^6 g^{3/2}+gamma z^2 g^{1/2}`, so

```text
h_ell = a_(10+ell)(5/2) + beta a_(6+ell)(3/2) + gamma a_(2+ell)(1/2).
```

Clearing denominators of these seven polynomials over
`Z[p,c,r,beta,gamma]` produces exactly the contents

```text
256, 1024, 512, 2048, 2048, 32768, 4096
```

claimed in `(3.1)`. In particular `h2=E2/1024`, so the affine row
`h2=mu2` integerizes as `E2-1024*mu2`. The other six rows of `(2.1)`
are `E1=E3=E4=E5=E6=E7=0`. Independently reconstructed integerized
numerators match the seven polynomials frozen in
`aws_q_v2/compiled/affine_mu2_q.sing`; those polynomials are used below
only after this reconstruction.

The first three, rewritten in `Delta`, are the hand expansions

```text
E1 = c (15 Delta^2 - 48 beta Delta + 128 gamma - 40 p c^2),
E2 = (-5 Delta^3 + 24 beta Delta^2 - 128 gamma Delta
      + 120 p Delta c^2 - 192 beta p c^2 - 40 c^4),
E3 = c (-15 p Delta^2 + 48 beta p Delta - 128 gamma p
      + 20 (3 p^2 - 4 r) c^2 - 32 beta c^2),
```

with `E1,E2,E3` the integerized numerators (denominators `256,1024,512`
already divided out). Direct expansion of the right-hand sides in
`(p,c,r,beta,gamma)` matches the reconstructed polynomials.

---

## Attack 2 — `D(c)` elimination: `beta,gamma,F5,F7`, the `p!=0` combination, the `p=0` slice

**CONFIRMED.** No component is lost by dividing the odd rows by `c`, nor
by the displayed linear combination, nor by using `E6` at `p=0`.

On `D(c)` set `Fj=Ej/c` for `j` odd. Then `Ej=0` if and only if `Fj=0`.
The combination of the first two odd integerized rows is the polynomial
identity

```text
F3 + p F1 = 4 c^2 (5 Delta - 8 beta),
```

which is `4 c^2 (5 p^2 - 20 r - 8 beta)` as in the charged hand
elimination. Thus `F1=F3=0` forces `beta=5 Delta/8`. Substituting into
the displayed form

```text
F1 = 15 Delta^2 - 40 p c^2 - 48 Delta beta + 128 gamma
```

gives `gamma=(15 Delta^2 + 40 p c^2)/128`, which is `(3.2)`.

Substitution of these two formulae into the reconstructed `F5` and `F7`
is elementary and yields exactly

```text
F5 = 5 Delta^3 + 40 p Delta c^2 + 24 c^4,
F7 = -5 p (3 Delta^3 + 24 p Delta c^2 + 8 c^4).
```

Write `inner=3 Delta^3 + 24 p Delta c^2 + 8 c^4`, so `F7=-5 p * inner`.
The polynomial identity

```text
3 p F5 + F7 = 32 p c^4
```

holds after the substitution (the displayed combination `(3.7)` is this
identity divided by `3 p` when `p!=0`). Characteristic zero makes `32`
a unit. On `D(p)` one obtains `c^4=0`, contradicting `D(c)`. No
division by `3` is required as a field hypothesis: the cleared form
already kills `c` on `D(p)`. If `Delta=0` then `F5=24 c^4`, which is
likewise nonzero on `D(c)`, so no square branch survives on this open.

It remains to put `p=0`. Then `Delta=-4 r`, `(3.2)` becomes
`beta=-5 r/2`, `gamma=15 r^2/8`, and

```text
F5 = 8 (3 c^4 - 40 r^3),     F7 = 0.
```

After the same substitution the even non-target rows specialize to
`E4=0` identically and

```text
E6 = -3840 r^4.
```

Thus `E6=0` forces `r=0`, and then `F5=24 c^4=0` forces `c=0`, again
contradicting `D(c)`. (The leftover of `F5=0` alone, `3 c^4=40 r^3`, is
killed by `E6` and is not a component.) The odd row `E7` is identically
zero at `p=0` after `(3.2)`, so it does not supply a further condition
and does not hide one. This exhausts both `p` cases. Every point of
`(2.1)` therefore has `c=0`.

Characteristic zero is used to invert `2,3,5,8,16,32,128` in the
intermediate formulae and to conclude `c^4=0` from `32 c^4=0`. Geometric
base change is as stated.

---

## Attack 3 — `c=0`: `h4=-(p/2) h2`, the `D(p)` reduction, and the `p=0` six-row analysis

**CONFIRMED.** The factor in `mu2` is `32`, not `1024`.

On `c=0` put `T=z^2+p/2` and `D=Delta/4`, so `Q=T^2-D`. Then `H` is odd
in `T`. Expanding `T^{-1}=z^{-2}-(p/2) z^{-4}+(p/2)^2 z^{-6}+O(z^{-8})`
and `T^{-3}=z^{-6}+O(z^{-8})`, and using that `T^{-5}` cannot contribute
before `z^{-10}`, one has

```text
h2 = X,     h4 = -(p/2) X,     h6 = (p/2)^2 X + Y
```

through `z^{-7}`, where `X=[T^{-1}]H` and `Y=[T^{-3}]H`. In particular
`h4=-(p/2) h2`, which is `(3.5)`. Equivalently, at the integerized level,
`E4|_{c=0}=-p E2|_{c=0}`, because `E4/2048=-(p/2)(E2/1024)`. This is an
identity of the reconstructed polynomials, not a consequence of the
receiver.

On `D(p)` the identity forces `mu2=h2=0`. The receiver then becomes
the seven-zero-tail system `h1=...=h7=0` on `c=0`. The charged
square/Chebyshev theorem supplies exactly the first two components of
`(2.2)`. (Independently: odd tails vanish on `c=0`; the two even
conditions `X=Y=0` split into `D=0` with free `(beta,gamma)`, which is
the square locus `Delta=0`, and `D!=0` with `beta=5 D/4=5 Delta/16` and
`gamma=5 D^2/16=5 Delta^2/256`, which is the Chebyshev locus; both
require `mu2=0`.)

At `p=c=0` one has `Q=z^4+r`. The series `sqrt(Q)` is even in `z` and
supported in degrees `2,-2,-6,-10,...`. Multiplication by the even
polynomial `Q^2+beta Q+gamma` therefore produces no odd negative powers
and no `z^{-4}` term through `z^{-7}`. Directly from the reconstructed
polynomials, and independently from the binomial expansion of
`(1+r z^{-4})^{1/2}`,

```text
E1=E3=E4=E5=E7=0,
E6 = -256 r^2 (5 r^2 + 8 r beta + 16 gamma),
E2 =  64 r (5 r^2 + 6 r beta + 8 gamma),
```

with `E2=1024 mu2`. All six non-target rows were checked: five vanish
identically, and the sixth is `E6`. If `r=0`, then `E6=0` and `E2=0`,
so `mu2=0`, `Q=z^4` is square, and `(beta,gamma)` remain free. That is
the square limit, already present in the first component of `(2.2)`.
If `r!=0`, then `E6=0` is equivalent to `5 r^2+8 r beta+16 gamma=0`.
Substituting `16 gamma=-5 r^2-8 r beta` into `E2` gives

```text
5 r^2 + 6 r beta + 8 gamma
  = (r/2) (5 r + 4 beta),
mu2 = r (5 r^2 + 6 r beta + 8 gamma) / 16
    = r^2 (5 r + 4 beta) / 32,
```

which is the third component of `(2.2)`. The factor is `32`, matching
`E2/1024` rather than the integerized numerator `E2`.

---

## Attack 4 — primeness, overlaps, union, exact-Q stdout versus validation

**CONFIRMED** for the numbered claims. The exact-Q stdout and the
validator do **not**, by themselves, prove `(2.3)`. The equality is
nevertheless true.

Write the three displayed ideals in `K[mu2,gamma,beta,r,c,p]`:

```text
I_square     = (c, mu2, Delta),
I_Chebyshev  = (c, mu2, 16 beta - 5 Delta, 256 gamma - 5 Delta^2),
I_affine     = (p, c, 5 r^2 + 8 r beta + 16 gamma,
                    32 mu2 - r^2 (5 r + 4 beta)).
```

Each is a graph over a polynomial ring in characteristic zero, hence
prime:

- `I_square`: `c=mu2=0` and `r=p^2/4`, quotient isomorphic to `K[gamma,beta,p]`;
- `I_Chebyshev`: `c=mu2=0`, `beta=5 Delta/16`, `gamma=5 Delta^2/256`, quotient isomorphic to `K[p,r]`;
- `I_affine`: `p=c=0`, `gamma=-(5 r^2+8 r beta)/16`, `mu2=r^2(5 r+4 beta)/32`, quotient isomorphic to `K[r,beta]`.

The units used are powers of two and the coefficient `5`; all are
invertible in characteristic zero.

Overlaps are contained in the union and do not add a fourth component.

- Square meet Chebyshev: `c=mu2=Delta=0` forces `beta=gamma=0`. This is
  the curve of square points with Chebyshev ratios, already in both.
- Square meet affine: `p=c=0` and `Delta=0` force `r=0`, then
  `16 gamma=0` and `mu2=0`, with `beta` free. This is a line in the
  square limit `Q=z^4`.
- Chebyshev meet affine: `p=c=0` forces `beta=-5 r/4`, `gamma=5 r^2/16`,
  `mu2=0`, which is the slice `t=0` of `(4.1)` and is the charged
  Chebyshev family at `p=0`.

Set-theoretically, Attacks 2--3 give
`V(I)_red=V(I_square) union V(I_Chebyshev) union V(I_affine)` after
geometric base change. Each component lies in `V(I)` by substitution
(square and Chebyshev by the seven-zero-tail theorem plus `mu2=0`;
affine by the `p=c=0` specialization). The intersection `J` of the three
primes is radical. Nullstellensatz over an algebraic closure of
characteristic zero therefore yields `rad(I)=J`, which is `(2.3)`. Both
sides are defined over `Q`, so the equality of radicals descends to `Q`.

The exact-Q compiler asks Singular for `rad(I)`, for `J`, for both
reductions, and for `minAssGTZ`. The frozen exact-Q stdout prints
`AFFINE_MU2_EXPECTED_SOLUTIONS=1`, `RAD_IN_EXPECTED=1`,
`EXPECTED_IN_RAD=1`, `MINASS_COUNT=3`, and
`ENDPOINT=PROPOSED_THREE_COMPONENT_UNION`. Those strings are not a proof.
The AWS validator that emits `PASS_AFFINE_MU2_PROBE` checks only
compiler and engine return codes, uniqueness of the two scope sentinels
`PROBE_DONE=1` and the firewall sentence, and absence of diagnostic
tokens; it does **not** check the two containments, the associated-prime
count, or the endpoint tag. Finite-field agreement is a software control
only. The printed `minAss` generators are a different spanning set of the
same three primes in characteristic zero (`beta^2-5 gamma` in place of
`256 gamma-5 Delta^2` on the Chebyshev component, and a pair equivalent
to `2 T` rather than `T=32 mu2-r^2(5 r+4 beta)` on the affine
component); they are not used.

---

## Attack 5 — `(r,t)` parametrization, generalized-Pell remainder, `h10`

**CONFIRMED.** Equation `(4.2)` is an identity on the new component and
is not promoted to a row of `(2.1)`.

Put `t=5 r+4 beta`. Solving with the affine relation
`16 gamma=-5 r^2-8 r beta` produces exactly `(4.1)`:

```text
beta = (t - 5 r)/4,
gamma = r (5 r - 2 t)/16,
mu2 = r^2 t / 32.
```

At `p=c=0` write `x=z^2` and `Q=x^2+r`. Substituting `(4.1)` into
`Q^2+beta Q+gamma` gives the loaded polynomial

```text
P = x^4 + ((t+3 r)/4) x^2 + r (r+2 t)/16.
```

The polynomial part of `sqrt(Q) P` is

```text
A = x^5 + ((t+5 r)/4) x^3 + (r (5 r+4 t)/16) x,
```

obtained from the binomial expansion of `(1+r/x^2)^{1/2}` through the
constant term in `x`. Direct multiplication, collecting even powers of
`x`, yields

```text
A^2 - Q P^2
  = -(r^2 t / 16) x^4
    - (r^2 t (t+5 r)/64) x^2
    - r^3 (r+2 t)^2 / 256.
```

The coefficients of `x^{10}`, `x^8`, and `x^6` cancel identically. The
leading remainder `-(r^2 t/16) x^4` divided by the leading
`2 x^5` of `A+sqrt(Q) P` recovers `h2=r^2 t/32`, a consistency check on
`mu2`.

The next negative coefficient of `H` is the `x^{-5}=z^{-10}` term of
`sqrt(Q) P`. From the binomial coefficients
`C(1/2,3)=1/16`, `C(1/2,4)=-5/128`, `C(1/2,5)=7/256` one obtains

```text
h10 = (7/256) r^5 - (5/128) v r^4 + (1/16) w r^3,
```

with `v=(t+3 r)/4` and `w=r(r+2 t)/16`. This simplifies to
`h10=-r^4 (t-r)/512`, which is `(4.2)`. The identity lives on `(4.1)`
and is not imposed by `(2.1)`. The theorem states this. The locus
`t=0` is the Chebyshev slice (`mu2=0`, constant remainder); the locus
`t=r` cancels `h10` and is a successor sentinel only.

---

## Attack 6 — application boundary

**CONFIRMED** as a firewall, not as a total-Rees, correction, terminal,
or JC2 theorem.

The object classified is the affine seven-row Laurent receiver `(2.1)`
for the normalized combined load `H` on the exact-square chart `k10=1`.
Vanishing of tails is homogeneous in a nonzero leading load, so the same
reduced support describes the ratios `beta=k6/k10`, `gamma=k2/k10` on
`D(k10)`. The hyperplane `k10=0` is a different two-load problem and is
not a silently lost affine family.

Unitriangular Laurent-to-Faber transport through seven rows applies to
`H` because it is a property of `z0(w)=w+O(w^{-1})` with even correction
`O(w^{-2})`. That transport does not identify `(2.1)` with a literal
total-Rees pullback. Source weights `Lambda^2 k10`, `Lambda^6 k6`,
`Lambda^{10} k2`, target grades `Lambda^{13}` through `Lambda^{19}`, and
a chosen valuation ray must still be substituted into the literal total
source before specialization. A target tying the same grade is a
separate inhomogeneous row. Correction jets, deck compatibility, the
terminal `[6,2]` passport, both Taylor families, and the other square
and discriminant charts are absent from `(2.1)`. No strict arc is
constructed or excluded. Nothing here closes order two, `(8,12)`,
maximum twelve, or JC2.

The sentinel `h10` is available for successor design on the new
component and is not a Keller, source, or terminal equation of this
theorem.

---

## Scope firewall

This review confirms only the reduced support of the affine seven-row
Laurent receiver `h1=h3=h4=h5=h6=h7=0`, `h2=mu2`, for
`H=sqrt(Q)(Q^2+beta Q+gamma)` over a characteristic-zero field, in the
affine chart `k10=1`, together with primeness of the three displayed
component ideals, the radical equality `(2.3)`, the parametrization
`(4.1)`, the generalized-Pell remainder, and the identity `(4.2)`. It
does not:

- classify the two-load chart `k10=0`;
- pull `(2.2)` through the literal total-Rees rows, the substitutions
  `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^{10} k2`, or a chosen valuation
  ray;
- absorb correction jets, target/deck ties, the terminal `[6,2]`
  condition, either Taylor family, or the other square and discriminant
  charts into `(2.1)`;
- promote `h10` to a source or terminal equation;
- construct or exclude a strict `Lambda!=0` arc;
- close order two, `(8,12)`, maximum twelve, or JC2.

The exact-Q Groebner narrative and the token `PASS_AFFINE_MU2_PROBE` are
not part of the confirmed argument. The mislabelled producer equation
`E2=mu2` is not part of the confirmed statement.

CONFIRMED
