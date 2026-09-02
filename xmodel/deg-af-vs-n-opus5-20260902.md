# DEG-AF-VS-N — the correct form of the degree question, and the bounds that exist

Lane: `DEG-AF-VS-N`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact desk CAS (sympy 1.14 over `Q`; exact linear algebra over
`GF(2^61-1)`; no Groebner, no AWS, no fetching, no web). Drivers in `/tmp/degaf`,
not installed in `box/`.

## 0. Custody, method, scope

The seven charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all seven match the charge exactly:

```text
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  b3-e-geometry-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  chau-delta-budget-gpt55-20260902.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  companion-curve-alln-opus5-20260902.md
e30c80f34d04ceecf0575541401bb57956464925a894117920006072a7bd3f3e  ideation-20260902T0741Z-grok46.md
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  ideation-20260902T0741Z-opus5.md
```

Abbreviations: **B3E** = the `B3-E-GEOMETRY` flagship, **MI** = MPRIME-ALLN-H2,
**HF** = HORN-FLAGSHIP, **CD** = the Chau delta-budget report, **CO** =
COMPANION-CURVE-ALLN.

Typing discipline, as charged. B3E's theorems are UNREVIEWED proposals; I consume
**only** bookkeeping I re-derive here, and I say where. MI, HF, CO are consumed at
banked typing (`Lemma A`, `[P3]`, `7.B'`, sheet gate, `(K)`, `(C2)`, `(C3)`,
`(M')`, Lemma 4.1, THEOREM PROFILE, the meridian cycle type MI:694-695, HF Prop
3.2, Chau C6-C8 with CD's notation repair). CD is consumed at its own declared
typing (its §5 list self-types "budget-only"). The two ideation files are
PROPOSALS.

Repository files read (not edited), hashed:

```text
31e8d92397106b61d7d4102e6203b168c133799a9ac110af0f4291ee031fd069  dist/jc72108-theory-bundle-v1/AM-CHECK.md
459bfe8e3e8e57cf554c019d8051475e74d1e8f44e23991f87ae4cbe26030a2e  dist/jc72108-theory-bundle-v1/SHEET6-CLASSICAL.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  xmodel/b0-reducible-n5-opus5-20260831.md
7c63614eff87640789d4591c67d8f8ce7d48645310d3146e87c44ddfc0dddf89  xmodel/reducible-all-n-opus5-20260901.md
```

Nothing was fetched: `refs/` contains no Jelonek, no Abhyankar-Moh, no
Lin-Zaidenberg (§6). No canonical ledger edited; `jc2-lean` not inspected.
No `charge_basis` line: **this report asserts no new exit price.**

## 1. Verdict, up front

```text
(1) THE INVARIANT.  n_min is well defined but is NOT the sharpest invariant.  The
    right object is the SEMIGROUP AT INFINITY Gamma = { deg_t f(a(t),b(t)) }: it is
    Aut(C^2)-invariant and its gap count is EXACTLY the affine delta,
    #(N \ Gamma) = sum_{p in Sing A_F} delta_p =: delta_aff -- which is precisely
    what the (B2) beta-bound and the (B3) delta-budget consume.  n and delta_infty
    are gauge quantities; the delta-budget is the IDENTITY computing delta_infty
    from them, not a constraint.  Chau's m is gcd(deg a, deg b) in the given gauge.

(2) THE BOUND.  FLOOR (unconditional): delta_aff <= (n-1)(n-2)/2 in EVERY gauge, so
    a bound n_min <= C(N) delivers delta_aff <= (C-1)(C-2)/2 -- the whole downstream
    payoff, with no delta_infty anywhere.  CEILING (from (AM-SG)): b_1 | b_0, or
    n <= 2 delta_aff + b_1 - 1 <= 3 delta_aff; sharp at (t^2, t^(2d+1)).  So the two
    questions are equivalent up to explicit constants, with one residual,
    OPEN[MIN-EMBED-DEGREE].  NEW, and the first N-monotone statement in this
    direction:  MERIDIAN-FLOOR,  n_min >= ceil((N-1)/(W - sum_l s_l))
    >= ceil((N-1)/(W-1)), W = N-a; at W = 2, n_min >= N-1.  With Chau's cap it
    answers half of OPEN[N-VS-MAPDEG]: max(deg P,deg Q) >= ceil((N-1)/(W-1)).

(3) IS IT BOUNDED ABOVE?  NOT DERIVABLE from the banked ledger, and NOT FALSE.
    Exhibited: (a) a satisfying assignment of EVERY banked constraint at fixed N
    with k -> infinity; (b) an explicit family of rational one-place plane curves
    with ONE ordinary (2,3) cusp and exactly k nodes, verified for k up to 11.  The
    charged "fixed profile, unbounded Aut-minimal degree" family does NOT exist --
    the ceiling forbids it -- but the unbounded-k family does, and it is what blocks
    the gate.  The dicritical-side attack returns exactly Chau: n = lambda_l/s_l
    with lambda_l = l . Phi^*(line), i.e. it IS OPEN[N-VS-MAPDEG], not a 2nd route.

(4) CONSEQUENCES (Sec 6).  (B2), 5 <= N <= 16: beta <= floor(delta_aff/2), so (B2)
    dies iff delta_aff <= 3 (N <= 10) / <= 1 (11..16) -- no n, no delta_infty, so
    CD's OPEN[DELTA-INFTY-NOT-NUMERICAL] is not a blocker here.  (B3), N = 4..8: the
    finite list re-indexed by delta_aff, with an exact realisability sharpening of
    CD Sec 5.  Crossing: a cell (N,W) is EMPTY as soon as one proves n_min <= C with
    C < ceil((N-1)/(W-1)) -- at W = 2, any C < N-1.

(5) LITERATURE (Sec 7).  Jelonek's degree bound: ABSENT from refs/, carried by the
    campaign from memory, and in (deg f, deg g) not N -- an instance of
    OPEN[N-VS-MAPDEG], not an answer.  A theorem bounding a curve's degree by the
    degree of a finite etale map onto its complement: ABSENT, and MERIDIAN-FLOOR
    runs the OTHER way.
```

## 2. Part (1): the invariant, and what it is invariant under

### 2.1 `n_min` is well defined, and the profile is the invariant part

For `psi in Aut(C^2)`, `psi o F` is Keller (`Jac(psi o F) = (Jac psi o F)·Jac F in
C^*`), noninvertible, of the same geometric degree `N`, and
`A_{psi o F} = psi(A_F)`; the source curve is literally unchanged,
`(psi o F)^{-1}(A_{psi o F}) = F^{-1}(A_F) = E`. So

> **DEFINITION.** `n_min(F) := min{ deg closure(psi(A_F)) : psi in Aut(C^2) }`.

A nonempty set of positive integers has a least element: `n_min` is well defined,
and is an invariant of the target-`Aut` class of `F`. This is the campaign's
promoted `d_min` discipline (`D1-DEGREE`, CNA §1.4;
`b0-reducible-n5-opus5-20260831.md:417-419`), and the raw-degree refutation is
already banked as **THEOREM NO-DEG-CAP `[D]`**
(`reducible-all-n-opus5-20260901.md:335-343`, `T(x,y) = (x,y+x^k)`). The grok
ideation item (d) reproduces that argument: **CONFIRMED**, and **not new**. What
is new below is what replaces it.

Everything the downstream gates use is `Aut`-invariant: the singularity types of
`A_F` and their `delta_p`, `r_p`, the branch structure, `k`, `nu`, `beta`; and
`a`, `a_p`, `W`, `s_l`, `mu_l`, `K_p`, which are defined from `F` and the covering
and are untouched by `psi`. Not invariant: `n = deg A_F-bar`, `delta_infty`,
Chau's `(m,d,e)`, `max(deg P, deg Q)`.

### 2.2 THEOREM SG-INV: the semigroup at infinity, and `#gaps = delta_aff`

Under `H2`, `Lemma A` (MI, banked) gives `D~ ≅ A^1`, so `D := A_F` carries a
polynomial parametrisation `t |-> (a(t), b(t))` that is **birational** onto `D`.
Put `S := C[a,b] ⊆ C[t]` and

```text
   Gamma  :=  { deg_t f(a(t),b(t))  :  f in C[u,v], f not in I(D) }  =  { deg_t g : g in S\{0} }.
```

> **THEOREM SG-INV.**
> (i) `C[t]` is a finite `S`-module and `Frac(S) = C(t)`; hence `Gamma` is a
>     numerical semigroup (`gcd = 1`, finitely many gaps).
> (ii) `#(N \ Gamma) = dim_C C[t]/S = sum_{p in Sing D} delta_p =: delta_aff`.
> (iii) For every `psi in Aut(C^2)`, `Gamma(psi(D)) = Gamma(D)`.
> (iv) `n := deg closure(D) = max(deg a, deg b) in Gamma`, and
>      `deg_t f(a,b) = sum_{q in A^2} (f · D)_q` — `Gamma` is exactly
>      Abhyankar-Moh's *semigroup at infinity*.
>
> *Proof.* (i) `a` is nonconstant, so `C[t]` is finite over `C[a] ⊆ S`; `S ⊆ C[t]`
> have the same fraction field by birationality and `C[t]` is integrally closed, so
> `C[t]` is the integral closure of `S` and `S` contains a conductor ideal
> `t^c C[t]`; hence `Gamma ⊇ [c,∞)`. (ii) Filtering by degree, a `C`-basis of
> `C[t]/S` is `{t^m : m a gap}`, so `dim_C C[t]/S = #(N\Gamma)`; and `S = C[D]`,
> `C[t] = C[D~]`, so `C[t]/S = ⊕_{p in Sing D} (O~_p/O_p)`, of local dimensions
> `delta_p`. (iii) The parametrisation of `psi(D)` is `psi∘(a,b)`, so its degree set
> is `{deg_t (f∘psi)(a,b)}`, and `f |-> f∘psi` is a bijection of `C[u,v]` carrying
> `I(psi(D))` onto `I(D)`. (iv) `f(a(t),b(t))` is a polynomial whose roots, with
> multiplicity, are the points of `D~` over the affine intersections; a generic
> linear form gives `max(deg a, deg b) = deg closure(D)`. ∎

**Corollary (the delta-budget is an identity, not a constraint).** For a rational
curve of degree `n`, `delta_aff + delta_infty = p_a(n) = (n-1)(n-2)/2`. The left
side splits into the `Aut`-invariant `delta_aff` and the gauge quantity
`delta_infty`; the right side is a gauge quantity. So the budget
`delta(p,q) + sum_i t_i + delta_infty = p_a(n)` **computes `delta_infty` from
`(n, delta_aff)`**; it constrains nothing invariant. Consequently **CD's
`OPEN[DELTA-INFTY-NOT-NUMERICAL]` is not a blocker** for any consumer that is
rewritten in `delta_aff` (§5 does exactly that).

**Explicit demonstration of the gauge dependence** (driver `/tmp/degaf/family3.py`,
exact over `Q`):

```text
  D  = image( t^3 , t^12 + t^4 + t^2 ) :  n = 12,  delta_aff = 3,  delta_infty = 52
  psi = (u,v) |-> (u, v - u^4)         :  n =  4,  delta_aff = 3,  delta_infty =  0
  both:  one ordinary (2,3) cusp at t=0  and exactly k = 2 nodes.
```

Same curve, same `Gamma`, same `k`; degree and `delta_infty` move by 8 and 52.

### 2.3 Relation to Chau's `(m,d,e)`, with the campaign's own control

Under `H2` the Chau/CD data are `deg a = m d`, `deg b = m e`, `gcd(d,e) = 1`,
`n = m·max(d,e)`, `m <= K = gcd(deg P, deg Q)` (CD §1, CONFIRMED with its notation
repair). In SG-INV language: `md, me in Gamma` and `m = gcd(deg a, deg b)` **in the
given gauge** — not the multiplicity of `Gamma`, and not `Aut`-invariant. The
campaign's realised `(9,6,2)` component (`CO §3.3`) is the control, and it is a
**two-route agreement**:

```text
  (u,v) = ( t^9 + 12 t^5 + 24 t ,  t^6 + 8 t^2 ) ,  (m,d,e) = (3,3,2),  n = 9
  Gamma computed from the parametrisation  =  <2, 9>      [driver sg3.py]
     #gaps = 4   = delta_aff        <-- CO/CD: "the realised affine curve has four nodes"
     p_a(9) - 4 = 24 = delta_infty  <-- CD §2: Puiseux semigroup <3,25>, delta = 24
  and  m(Gamma) = 2  !=  m = 3 :  Chau's m is a gauge gcd, not a semigroup invariant.
```

CD's second curve `(t^9, t^6+t)` is reproduced identically: `delta_infty = 13`
(CD: `<3,14>`, `delta = 13`), `delta_aff = 15`. Both of CD's independent
Puiseux computations are confirmed by a computation that never touches infinity.

## 3. Part (2), first half: the two-sided bound between `n_min` and `delta_aff`

### 3.1 FLOOR — unconditional, and it is the direction the campaign consumes

> **THEOREM DEG-DELTA(a).** In every gauge, `delta_aff <= p_a(n)`; hence
> ```text
>       delta_aff <= (n_min - 1)(n_min - 2)/2 ,     n_min >= ceil( (3 + sqrt(8 delta_aff + 1))/2 ).
> ```
> *Proof.* Genus formula for the rational plane curve `closure(D)`:
> `0 = p_a(n) - sum_all delta_q`, and the affine points are among all points. ∎

This is the whole of what the gates need: **a bound `n_min <= C(N)` yields
`delta_aff <= (C-1)(C-2)/2`, hence `beta` and `k` bounds, with no `delta_infty`
and no Chau data.** It is also why the raw-degree refutation was never fatal: it
kills the statement, not the payoff.

### 3.2 CEILING — from the banked `(AM-SG)`

`(AM-SG)` is banked in the campaign at `AM-CHECK.md:50-63` (Abhyankar-Moh, Crelle
260/261 (1973); Crelle 276 (1975); semigroup paper 1977 — citation inherited
there, and the PDFs are ABSENT from `refs/`, §6). In the indexing used here:
`b_0 = n`, `d_0 = b_0`, `d_i = gcd(d_{i-1}, b_i)`, `n_i = d_{i-1}/d_i >= 2`,
`d_h = 1`, with **(ii)** `n_i b_i > b_{i+1}` and **(iii)**
`n_i b_i in <b_0,...,b_{i-1}>`. Condition (iii) makes `Gamma` free/telescopic,
hence symmetric, so its conductor and gap count are

```text
   c(Gamma) = sum_{i=1}^h (n_i - 1) b_i - b_0 + 1 ,        delta_aff = c/2 .        (F)
```

`(F)` was verified independently on every explicit curve of this lane and on
every AM-admissible pair in the enumeration of §3.3: **0 violations**.

> **THEOREM DEG-DELTA(b).** With `b_1` the second term of the AM sequence of a
> gauge of degree `b_0 = n`: either `b_1 | b_0`, or
> ```text
>        n = b_0  <=  2 delta_aff + b_1 - 1  <=  3 delta_aff .
> ```
> *Proof.* By `(F)`, `2 delta_aff = sum_{i>=1}(n_i-1)b_i - b_0 + 1 >= (n_1-1)b_1 -
> b_0 + 1`. Write `d_1 = gcd(b_0,b_1)`; `b_1 ∤ b_0` gives `d_1 <= b_1/2`, so
> `(n_1-1) b_1 = b_0 (b_1/d_1) - b_1 >= 2 b_0 - b_1`, whence
> `2 delta_aff >= b_0 - b_1 + 1`. In the canonical sequence
> `b_i = min(Gamma \ <b_0..b_{i-1}>)` one has `b_1 = m(Gamma)`, the multiplicity;
> and `1,...,m(Gamma)-1` are gaps, so `b_1 <= delta_aff + 1`. ∎

Sharpness: `Gamma = <2, 2delta+1>`, realised by `(t^2, t^{2delta+1})`, has
`b_1 = 2 ∤ b_0 = 2delta+1` and `n = 2 delta_aff + 1` **exactly**. The campaign's
own `(9,6,2)` curve is the case `delta_aff = 4`, `n = 9 = 2·4+1`: it **saturates
the ceiling**.

The escape clause `b_1 | b_0` is the classical Tschirnhausen-reducible case; the
elementary reduction of §3.3 removes it whenever the minimal linear-form degree
equals `b_1`, but not in general. Residual, typed:

```text
 OPEN[MIN-EMBED-DEGREE].  Is  n_min <= 2 delta_aff + 1  unconditional?  Equivalent
 to: is the minimal embedding degree of a polynomial curve bounded by its affine
 delta?  Evidence: §3.3 computes  max_{Gamma of genus d} n_AM(Gamma) = 2d+1  for
 every d <= 10, attained only at <2,2d+1>; every explicit curve computed in this
 lane attains its n_AM exactly.  NOT needed for any consumer in §5 (they use the
 FLOOR).  Needed only for the delta_aff form of the crossing (§5.3).
```

### 3.3 A sharper floor: exact necessary conditions on a minimal gauge

Let a gauge have coordinate degrees `p <= n` after a linear target change chosen
so that `p := min{ deg_t l(a,b) : l affine-linear }`.

```text
 (R1) n in Gamma.                                          [SG-INV(iv)]
 (R2) (n, Gamma) satisfies (AM-SG).
 (R3) delta_aff <= p_a(n).                                 [THEOREM DEG-DELTA(a)]
 (R4) there is p in Gamma, 0 < p < n, with p ∤ n and
        delta_aff  <=  p_a(n) - (n-p)(n-p-1)/2 .
```

`(R4)` is two facts. *First*, the branch of `closure(D)` at its unique point at
infinity has multiplicity exactly `n - p`: in the chart at `[0:0:1]` the branch is
`(X,Z) = (1/b, a/b) = (tau^n·unit, tau^{n-p}·unit)`, so
`mult = min(n, n-p) = n-p`, and a germ of multiplicity `mu` has
`delta >= mu(mu-1)/2`; combine with `delta_infty = p_a(n) - delta_aff`. *Second*,
if `p | n` the target automorphism `(u,v) |-> (v, v - lambda u^{n/p})` strictly
lowers `max(deg a, deg b)`, so the gauge is not minimal.

Write `n_AM(Gamma) :=` least `n` satisfying (R1)-(R4). Then `n_min >= n_AM(Gamma)`.
Exhaustive computation (driver `/tmp/degaf/am4.py`; the semigroup census
reproduces the known counts `1,1,2,4,7,12,23,39,67,118,204` for genus `0..10`,
which validates the enumerator):

```text
 delta_aff | AM-admissible semigroups at infinity, with least admissible degree
    0      | <1> n>=1
    1      | <2,3> n>=3
    2      | <2,5> n>=5
    3      | <3,4> n>=4 ; <2,7> n>=7
    4      | <3,5> n>=5 ; <4,5,6> n>=6 ; <2,9> n>=9
    5      | <4,6,7> n>=6 ; <2,11> n>=11
    6      | <4,5> n>=5 ; <4,6,9> n>=6 ; <3,7> n>=7 ; <2,13> n>=13
    7      | <4,6,11> n>=6 ; <3,8> n>=8 ; <4,7,10> n>=10 ; <2,15> n>=15
    8      | <4,9,10> n>=10 ; <2,17> n>=17
```

Two readings. (a) **Most numerical semigroups are not semigroups at infinity**
(e.g. at `delta_aff = 8`, 2 of 67 survive), so `delta_aff` is far more rigid than
its gap count suggests. (b) Every explicit curve computed in this lane lands on
its predicted minimum: `<2,3> -> 3` (cuspidal/nodal cubic), `<3,4> -> 4`
(`(t^3,t^4+t^2)`, verified quartic with one cusp and two nodes), `<3,5> -> 5`,
`<4,5> -> 5`, `<4,6,11> -> 6` (`(t^4,t^6+t^5)`), `<3,7> -> 7`, `<2,9> -> 9`
(the `(9,6,2)` curve and `(t^2,t^9)`).

## 4. Part (2), second half: MERIDIAN-FLOOR — an `N`-monotone lower bound

Nothing above involves `N`. Here is the bridge, and it is a floor.

> **THEOREM MERIDIAN-FLOOR (all `N`, `H2`).** Let `F` be a noninvertible plane
> Keller map of geometric degree `N` with `A_F` irreducible, `a` the covering
> degree over `A_F°`, `W = N - a = sum_l s_l mu_l`, `S = sum_l s_l`. Then for
> **every** gauge, `n = deg closure(A_F)` satisfies
> ```text
>       n  >=  (N - 1) / (W - S)   >=  (N - 1)/(W - 1) ,     hence   n_min >= ceil((N-1)/(W-1)).
> ```
>
> *Proof.* (1) `F : A^2 \ E -> A^2 \ A_F` is finite (proper over the complement of
> the non-properness set, and quasi-finite), étale (`Jac F in C^*`), of degree `N`,
> with connected total space (`A^2` minus a curve). [This is B3E's LEMMA E-ETALE;
> it is re-derived here from the definition of `A_F` and is not consumed from
> B3E.] Hence the monodromy `rho : pi_1(A^2 \ A_F) -> S_N` is **transitive**.
> (2) By Zariski's theorem the inclusion of a generic line `L` induces a surjection
> `pi_1(L \ A_F) ↠ pi_1(A^2 \ A_F)`, so `pi_1(A^2\A_F)` is generated by the
> `#(L ∩ A_F) = n` meridians of a generic line. [The campaign uses this step at
> `b0-reducible-n5-opus5-20260831.md:421-426`.]
> (3) `A_F` is irreducible (`H2`), so all meridians are conjugate, and their common
> image has cycle type `1^a · prod_l mu_l^{s_l}` (MI:694-695): support of size
> `W`, consisting of `S` nontrivial cycles.
> (4) Start from the partition of the `N` sheets into `N` singletons and adjoin the
> generators one at a time. A permutation `sigma` merges, per cycle `c`, at most
> `len(c)` blocks into one, so it decreases the block count by at most
> `sum_c (len(c) - 1) = W - S`. Transitivity requires the count to fall from `N`
> to `1`, so `n · (W - S) >= N - 1`. `S >= 1` gives the stated weaker form. ∎

Since the statement holds in every gauge it holds for `n_min`. The `N = 5`,
`W = 2` instance of this table is the record's Gate TG
(`b0-reducible-n5:421-426`, `d_min >= 4`); MERIDIAN-FLOOR is its all-`N`,
all-`W` form, and `7.B'` (`mu_l >= 2`, so `S <= W/2` and `W - S >= W/2`) is the
sharpener when `S` is known.

```text
 MERIDIAN-FLOOR, guaranteed form  n_min >= ceil((N-1)/(W-1)) ; second entry is the
 delta_aff shadow ceil(that/3) via THEOREM DEG-DELTA(b) (conditional, §3.2).

   N |   W=2      W=3      W=4      W=5
   4 |   3/1       --       --       --
   5 |   4/2       --       --       --
   6 |   5/2      3/1       --       --
   7 |   6/2      3/1       --       --
   8 |   7/3      4/2      3/1       --
   9 |   8/3      4/2      3/1       --
  10 |   9/3      5/2      3/1      3/1
  11 |  10/4      5/2      4/2      3/1
  12 |  11/4      6/2      4/2      3/1
  13 |  12/4      6/2      4/2      3/1
  14 |  13/5      7/3      5/2      4/2
  15 |  14/5      7/3      5/2      4/2
  16 |  15/5      8/3      5/2      4/2
  17 |  16/6      8/3      6/2      4/2
  18 |  17/6      9/3      6/2      5/2
  19 |  18/6      9/3      6/2      5/2
  20 |  19/7     10/4      7/3      5/2      (columns W >= 6 read 4/2 or 3/1)
                                        [driver /tmp/degaf/tables.py]
```

> **COROLLARY (half of `OPEN[N-VS-MAPDEG]`, answered).** Chau's cap
> `n <= max(deg P, deg Q)` (CD §1/§4, CONFIRMED) composes with MERIDIAN-FLOOR:
> ```text
>       max(deg P, deg Q)  >=  n  >=  ceil( (N-1)/(W-1) ) ,   and at W = 2:  >= N-1.
> ```
> So the map degree is bounded **below** by the geometric degree. `OPEN[N-VS-MAPDEG]`
> asks for the opposite inequality; this corollary is not evidence for it, and it
> shows the two are not symmetric.

**Consistency checks.** `N = 4`, `W = 2`: floor `n_min >= 3`; CD §5 independently
finds `n >= 4` for `(B3)` (its `n=3` row is case (A)) — consistent, and CD's is the
sharper. `N = 5`, `W = 2`: floor `4`, equal to the record's Gate TG value. The floor
is vacuous (`= 2`) in the largest-`W` cells, exactly where `a` sits at its
sheet-gate minimum.

## 5. Part (3): is there an upper bound? — not derivable, and not false

### 5.1 The banked constraint set does not bound `k`

Fix `N`, take `a = N-2`, `W = 2`, one dicritical with `(s,mu) = (1,2)`, one cusp
carrying `K_c = a-1`, and `k` double points with `K_p = 0`. Then, for **every**
`k >= 1`:

```text
 sheet gate  ceil(N/2) <= a <= N-2                     OK
 [P3] N = a + sum_l s_l mu_l,  W >= 2, 7.B' mu_l >= 2  OK
 (K)  sum_p K_p = a - 1                                OK   (carried entirely by the cusp)
 (C2) K_p <= D_gap at multibranch points               OK   (K_p = 0)
 Lemma 4.1 a_p = a - (r_p-1)W - K_p >= 0               OK   (cusp: a_p = 1; nodes: a_p = a-W)
 (C3) #{p : K_p > 0} = 1 <= R + beta = 0 + 1           OK
 (M') sum_p (a - a_p) = (a-1) + nu W,  nu = k          OK   identically in k
 PROFILE (B3): >= 1 cusp and >= 1 multibranch point    OK
```

Verified mechanically for `N in {5,8,12,16,20}` at `a = N-2` and for
`N in {10,16}` at `a = ceil(N/2)`, with `k` up to `10^4`
(driver `/tmp/degaf/tables.py`, table T-A: all OK). **No combination of the
banked constraints bounds `k`, hence none bounds `delta_aff`, hence none bounds
`n_min`.** This is a satisfying-assignment proof of non-derivability, not a
counterexample: it says no re-derivation from the present ledger can close the
gate. It reproduces, with the constraint list made explicit, B3E's finding that
each double point has `K_p = 0` and is therefore invisible to `(K)`.

### 5.2 The curve side does not bound `k` either

For every `k` in the tested range there is a rational plane curve with **one place
at infinity**, exactly one **ordinary `(2,3)` cusp** and exactly `k` nodes
(driver `/tmp/degaf/family2.py`, `family3.py`; exact over `Q`; the cusp is
certified by the critical point `t=0` with germ semigroup `<2,3>`, the node count
by the distinct roots of `Res_s((a(t)-a(s))/(t-s), (b(t)-b(s))/(t-s))`, and
`delta_aff` independently by the semigroup):

```text
   a(t) = t^3 ,  b(t) = t^q + t^2 + (generic tail)
   q  |  4   5   7   8   10  11  13        n = q,  delta_aff = q-1 = 1 + k
   k  |  2   3   5   6   8   9   11        (one cusp of delta 1, k nodes)
```

All seven are `1 + k = delta_aff` on the nose, i.e. the cusp plus `k` nodes are
**all** of the affine singularities. So the curve theory of rational one-place
plane curves imposes no bound on `k` at fixed cusp type. Both halves of the
necessary conditions are therefore satisfiable with `k -> infinity`.

**What this is, and what it is not.** It is not the family the charge asked for in
item (3): a family with *fixed* profile and *unbounded* `n_min` cannot exist,
because DEG-DELTA(b) forbids it (fixed profile ⟹ fixed `delta_aff` ⟹
`n_min <= 3 delta_aff` outside the Tschirnhausen case). The obstruction to the gate
is the other variable, `k` itself. Typed:

```text
 OPEN[DEG-AF-VS-N]  -->  retyped OPEN[DELTA-AFF-VS-N]:  is delta_aff(A_F) <= C(N)?
   * The raw form (deg A_F <= f(N)) is FALSE and already banked as NO-DEG-CAP [D].
   * The invariant form is equivalent to the delta form: FLOOR gives one direction
     unconditionally, CEILING the other outside OPEN[MIN-EMBED-DEGREE].
   * NOT DERIVABLE from the banked ledger (§5.1) and NOT FALSE (no Keller witness
     exists or can exist without refuting JC2).  It is a genuine open input.
```

### 5.3 The dicritical-side attack, run and returned

As charged: `phi_l = Phi|_{l'} : l' ≅ A^1 -> A_F` is `eta ∘ h_l` with
`deg h_l = s_l`, so as a polynomial map its coordinate degrees are
`s_l·(deg a, deg b)` and

```text
    lambda_l  :=  l · Phi^*(generic line)  =  s_l · n ,        n = lambda_l / s_l .
```

Bounding `n` is therefore exactly bounding `lambda_l`. But `Phi^*(line)` is the
total transform on the source compactification, `Phi^*O(1) = O(D_F H - sum a_i E_i)`
with `D_F = max(deg P, deg Q)`, so `lambda_l` is a linear functional of the map
degree and the resolution multiplicities: **the dicritical side returns
`OPEN[N-VS-MAPDEG]` verbatim.** It is not an independent route, and the two
ideation submissions' split of the question is confirmed here by a second
computation of the same quantity.

The remaining dicritical instruments do not reach `k`:

* `(RH_l)`: `h_l : A^1 -> A^1` totally ramified at `∞` has `sum_t (e_t - 1) = s_l - 1`,
  so at most `s_l - 1` finite critical points. That bounds `R = sum_l (s_l-1)`, the
  input to `(C3)`, and `(C3)` only constrains the points with `K_p > 0`. The `k`
  double points have `K_p = 0` and are invisible to it. (Equivalently, in B3E's
  E-CHARGE(iii) language, they carry `k_t = 0`.)
* The Domrina-Orevkov determinant package is degree-free (B3E §6) but is a
  **boundary** instrument, and the number of `K_p = 0` affine double points is
  exactly the datum it never sees — this lane's independent confirmation of B3E's
  "disjoint halves" reading.
* AMS and Lin-Zaidenberg close only the extremes: `delta_aff = 0` forces `A_F` to be
  a coordinate line (AMS), which is MI's SMOOTH-KILL; a single unibranch singularity
  forces `A_F ~ {x^p = y^q}` (LZ), which is case (A). Neither touches
  `delta_aff >= 2` with a multibranch point, i.e. `(B2)`/`(B3)`.

## 6. Part (4): consequences, written out

### 6.1 `(B2)` at `5 <= N <= 16` — `delta_infty` eliminated

In case `(B2)` every singular point has `r_p >= 2`, and a point counted by `beta`
carries a singular branch, so `delta_p >= delta(branch) + (B_i·B_j) >= 2`; every
other singular point has `delta_p >= 1`. Hence

> **`beta <= floor(delta_aff / 2)`**, and more precisely `delta_aff >= beta + s`.

Re-derivation of MI's thresholds (driver `/tmp/degaf/ledger.py`; minimise `beta`
subject to `a - 1 <= (R_max(W) + beta)(2a - N)`, `R_max(W) = floor(W/2) - 1`,
`W >= 2`, `D_gap >= 0`, `a <= N-2`) — it **reproduces MI:427/434 exactly**:

```text
  N          5..10        11..16        >= 17
  beta_min     2             1             0     (0 = the cell is already empty)
  (B2) dies iff  delta_aff <= 3   |   delta_aff <= 1   |   already empty
  witness cell (a,W,D_gap)  N=5:(3,2,1)  N=10:(6,4,2)  N=11:(7,4,3)  N=16:(10,6,4)
```

This route uses **no `n` and no `delta_infty`**. CD §3's substitution
(`beta <= Delta_aff = p_a(n) - delta_infty`) is the same bound written in a gauge:
`Delta_aff` *is* `delta_aff`, by SG-INV(ii). So CD's blocker
`OPEN[DELTA-INFTY-NOT-NUMERICAL]` is **not on the critical path**; what is needed is
`delta_aff <= 3` (resp. `<= 1`), an `Aut`-invariant statement.

### 6.2 `(B3)` at `N = 4..8` — the finite list, re-indexed and sharpened

With a bound `delta_aff <= C`, the `(B3)` enumeration is finite and needs nothing
else: the cusp contributes `delta_c = (p-1)(q-1)/2` and each double point at
least `1`, so

```text
     delta_c <= C ,      k <= C - delta_c ,      contacts t_i with sum t_i = delta_aff - delta_c .
```

Cusp types admitted by HF Prop 3.2 (`gcd(p,q)=1`, `p,q >= 2`, one divisible by 2
and the other by 3), listed by `delta_c` (driver `/tmp/degaf/tables.py`, T-D):

```text
  (p,q)  (2,3) (3,4) (2,9) (2,15) (3,8) (3,10) (2,21) (4,9)
  delta_c   1     3     4     7      7     9     10     12      (all others have delta_c > 12)
```

so `C = 1` admits only `(2,3)` with `k = 0` (case (A), not `(B3)`); `C = 2` admits
`(2,3)` with `k = 1`; `C = 3` admits `(2,3), k <= 2` and `(3,4), k = 0`; and so on.
Note this **replaces** CD §5's `n`-indexed list: no `n`, no `T_n`, no
`max(p,q) <= n` Bezout side-condition (that condition is subsumed —
`delta_c <= delta_aff` bounds `(p,q)` directly).

**Exact realisability, sharpening CD §5 (which self-types as budget-only).** By
the `(R1)-(R4)` table of §3.3:

```text
  delta_aff = 1  =>  Gamma = <2,3>,  n_min = 3.   [k=0: case (A), the cuspidal cubic]
  delta_aff = 2  =>  Gamma = <2,5>,  n_min = 5.   NOT 4.
  delta_aff = 3  =>  Gamma = <3,4> (n_min = 4)  or  <2,7> (n_min = 7).
```

Hence CD §5's row `n = 4, (p,q) = (2,3), k = 1` (which has `delta_aff = 2`) is
**empty**: a degree-4 curve would need `delta_infty = 1`, i.e. a branch at infinity
of multiplicity 2, i.e. `p = n - 2 = 2`, and `2 | 4` makes the gauge reducible to
degree `<= 3`, where `p_a(3) = 1 < 2`. The row `n = 4, k = 2` **is** realised —
witness `(t^3, t^4 + t^2)`, verified: irreducible rational quartic, one place at
infinity, one ordinary `(2,3)` cusp at `t=0`, exactly two nodes, `Gamma = <3,4>`,
`delta_aff = 3 = p_a(4)`, `delta_infty = 0`. And the minimal `(B3)` profile
(one `(2,3)` cusp + one double point, `delta_aff = 2`) is realised at degree 5:

```text
   E_1 :  (a,b) = ( t^2 ,  t^5 + t^3 + t^2 ) .
   Gamma = <2,5>, gaps {1,3}, delta_aff = 2, n = 5, p = 2, 2 ∤ 5 (minimal gauge),
   p_a(5) = 6, delta_infty = 4;  one ordinary (2,3) cusp at t = 0 (germ (t^2,t^3+t^5)
   after v |-> v-u), and exactly one node, from the parameter pair {i,-i}.
   TYPING: REPRESENTATIVE ONLY -- it realises the numerical type; nothing claims it
   is A_F for any Keller map.
```

### 6.3 All degrees: where the crossing is, and how weak the bound may be

B3E's G-ANTI table has no crossing because both of its ingredients move the same
way when `k` grows. The crossing that does exist is between MERIDIAN-FLOOR and any
upper bound:

> **CROSSING (unconditional).** The cell `(N, W)` is EMPTY as soon as one proves
> `n_min <= C` with `C < ceil((N-1)/(W-1))`.
> **CROSSING (delta form, conditional on OPEN[MIN-EMBED-DEGREE]).** The cell is
> EMPTY as soon as one proves `delta_aff <= C` with `C < ceil(ceil((N-1)/(W-1))/3)`
> — the second entry of the §4 table.

Read off the table: at `W = 2` a bound `n_min <= C` with `C < N-1` kills the whole
column, at every `N`; in `delta_aff` form, `C < 4` kills `W = 2` at `N = 11..13`,
`C < 5` at `N = 14..16`, `C < 7` at `N = 20`. Compare with the `(B2)` route of
§6.1, which demands `delta_aff <= 1` at `11 <= N <= 16`: **at `W = 2` the crossing
route needs a strictly weaker bound than the `beta` route** (`C <= 3` vs `C <= 1`
at `N = 11`), and it applies to `(B3)` as well, where the `beta` route does not.
This is the concrete payoff of MERIDIAN-FLOOR: it lowers the price of the still-open
input.

**Why the covering cap cannot supply the other half.** B3E's `2g(E) <= 1 - a +
sum_p r_p max(0,(r_p-1)W + K_p - 1)` is an upper bound on `g(E)`; on the `(B3)`
profile with `k` double points it reads `2g(E) <= 2k(W-1) + K_c - 1 - a + 1`,
which **increases** with `k`. It is also equivalent to a lower bound on the number
of places of `E` at infinity, because Theorem (E) pins `g(E)` exactly: from
`chi_c(E) = 1 - N nu` and `chi_c(E) = 2 - 2g(E) - n_infty(E)` for irreducible `E`,

```text
      2 g(E)  =  1 + N nu - n_infty(E) .
```

(Control: at `N=4`, `nu = k`, HF's B3-N4 gives `g = k_odd - 1` and
`n_infty = 3 + 4k - 2k_odd`, and `1 + 4k - (3+4k-2k_odd) = 2k_odd - 2` ✓.) So the
covering cap carries no independent upper bound on anything that grows with `k`;
the only monotone-in-`N` instrument on this side is MERIDIAN-FLOOR.

## 7. Part (5): literature custody

```text
 (L1) Jelonek, degree of the non-properness set.
      ABSENT from refs/ (refs/ has no Jelonek item; verified by listing).  The
      campaign carries the statement from memory, already flagged as such, at
      SHEET6-CLASSICAL.md:267-272 (hash above):
          deg A(F)  <=  ( deg f · deg g  -  mu(F) ) / min(deg f, deg g)
      with mu(F) the geometric degree.  TYPE: quoted-from-memory, flagged there
      and here; NOT used as an input to any statement of this report.
      Substance: it is a bound in (deg f, deg g), i.e. an instance of
      OPEN[N-VS-MAPDEG], not an answer to it.  Its mu-dependence has the sign the
      campaign wants (larger N, smaller bound) but the deg f·deg g term is
      unbounded in N, and the bound is gauge-dependent in exactly the way
      NO-DEG-CAP [D] describes: applying (u,v)|->(u,v+u^k) raises deg A(F) without
      changing N, and raises deg(psi∘F) correspondingly.  It therefore cannot, in
      any form, yield n_min <= C(N).
 (L2) Jelonek, structure of A(F) (Ann. Polon. Math. 58 (1993)): every component of
      A(F) is the image of a polynomial map C -> C^2.  Banked as (J-1),
      SHEET6-CLASSICAL.md:267-272.  MI's Lemma A re-proves it under H2; this lane
      uses Lemma A, not (J-1).
 (L3) "A result bounding the degree of a curve by the degree of a finite etale map
      onto its complement":  ABSENT.  I know of none, and Sec 4 shows the known
      implication runs the other way -- the etale degree N bounds the curve degree
      from BELOW.  What would be needed is an upper bound on the number of
      generators of pi_1(C^2 \ D) in terms of a subgroup index, false in general.
 (L4) Abhyankar-Moh (Crelle 260/261 (1973); Crelle 276 (1975); semigroup paper
      1977):  ABSENT from refs/.  Used as (AM-SG) at the campaign's own banked
      statement AM-CHECK.md:50-63 (hash above), itself typed there as inherited
      from SHEET6-CLASSICAL.md:150-155.  Everything derived from it -- (F),
      DEG-DELTA(b), the n_AM table -- is marked as such, and (F) is verified
      independently on every explicit curve.
 (L5) Abhyankar-Moh-Suzuki and Lin-Zaidenberg: ABSENT from refs/; used at
      statement level only, for the sharpness family of Sec 3.2 and as a cross-check
      of MI's SMOOTH-KILL, which has its own proof.
 (L6) Nothing was fetched this session; no new file entered refs/.
```

## 8. FALLACY-v2 audit

* **Flag/place/series.** Four semigroups are kept apart and never identified:
  `Gamma` (semigroup at infinity, degrees of `f(a,b)`, `Aut`-invariant,
  `#gaps = delta_aff`); `Gamma_infty^loc` (local semigroup of the *branch* at
  infinity, gap count `delta_infty`); the affine germ semigroups (gap counts
  `delta_p`); and the AM `delta`-sequence `(b_0,...,b_h)`, a generating datum for
  `Gamma` *together with* a choice of `b_0 = n`, not a semigroup. §2.3 records that
  Chau's `m` is a gauge gcd, not `m(Gamma)`: on `(9,6,2)`, `m = 3`, `m(Gamma) = 2`.
  `N`, `n`, `n_min`, `a`, `s_l`, `mu_l`, `max(deg P,deg Q)` are never substituted.
* **Carrier/attainment.** `E_1` (§6.2) and the `cusp + k nodes` family (§5.2) are
  typed REPRESENTATIVE: numerical types only, no Keller realisation claimed.
  `n_AM(Gamma)` is an attained *lower* bound; the observed equality `n_min = n_AM`
  on every computed curve is evidence, not a promotion.
* **Floor/attainment.** DEG-DELTA(a) and MERIDIAN-FLOOR are floors and used only as
  floors; §6.3, the one place a floor becomes a kill, names the missing ingredient
  (an upper bound `C`) and does not assert it. DEG-DELTA(b) is a ceiling with a
  named escape (`b_1 | b_0`), typed `OPEN[MIN-EMBED-DEGREE]` rather than closed by
  analogy; every §6 consumer is routed through the floor so none depends on it.
* **Per-ray/exit-set charge.** No exit price asserted; no `charge_basis` line. In
  MERIDIAN-FLOOR each generator is charged once, to the block-count reduction
  `W - S`, and each cycle once (`sum_c (len(c)-1) = W - S`, not `W`); fixed points
  contribute nothing and are excluded explicitly.
* **Pole/interior.** `mult_O = n - p` is derived in the chart at `[0:0:1]`,
  legitimate only because there is exactly one place at infinity (Lemma A) and
  `deg b > deg a` there; `deg a = deg b` is removed first by a linear change and
  `p = 0` (a line) is excluded separately.
* **Variable/ring map.** The semigroup driver declares its map: monomials `a^i b^j`
  over `GF(2^61-1)`, elimination with pivot = leading degree, truncation `M >= 3pq`,
  reporting window `[0, min(3n+10, M/3)]` with the conductor detected inside it. A
  first run at an unsafe window produced visible artefacts (spurious gaps near the
  truncation) and was discarded and re-run — which is what the window discipline
  exists to catch. Positive controls: `(9,6,2)` reproduces CO's four nodes
  (`delta_aff = 4`) and CD's `<3,25>` (`delta_infty = 24`); CD's variant reproduces
  `delta_infty = 13`. Negative control: `(t^2,t^4+t)` returns `Gamma = N`,
  `delta_aff = 0`, a line, as AMS requires.
* **Prime label/derivative.** `l'` is a label; the only derivatives are `a'(t),
  b'(t)` in the cusp certification, and the two never share a display.
* **`sat()` / raw remainder.** Not in play: no saturation, no Groebner basis, no
  quotient-ring normal form. The single resultant (node counting) is reported by its
  *distinct*-root count `deg R - deg gcd(R,R')`, so repeated roots are not
  double-charged.
* **Not filled by cap or analogy.** Tschirnhausen -> `OPEN[MIN-EMBED-DEGREE]`; the
  wanted bound -> `OPEN[DELTA-AFF-VS-N]`; Jelonek marked ABSENT and used for
  nothing; `(AM-SG)` named at its banked typing with its consequence `(F)` verified
  independently.

## 9. Typed verdict block

```text
LANE              DEG-AF-VS-N
SCOPE             Keller, noninvertible, H2 (A_F irreducible).  §§2-4 use no
                  case split; §6 is cases (B2)/(B3) at the charged ranges.
                  Quasi-homogeneity is never used.

PROVED HERE       (all PROVED-HERE, UNREVIEWED; DEG-DELTA(b) consumes (AM-SG) at
                  the campaign's banked literature typing)
                  SG-INV        Gamma := {deg_t f(a,b)} is a numerical semigroup,
                                Aut(C^2)-invariant, #(N\Gamma) = sum_p delta_p =
                                delta_aff, and n = max(deg a,deg b) in Gamma.
                  BUDGET=IDENT  delta_c + sum t_i + delta_infty = p_a(n) computes
                                delta_infty; constrains no invariant datum.
                  DEG-DELTA(a)  delta_aff <= p_a(n) in every gauge; hence
                                n_min <= C(N) ==> delta_aff <= (C-1)(C-2)/2.
                  DEG-DELTA(b)  b_1 | b_0, or n <= 2 delta_aff + b_1 - 1
                                <= 3 delta_aff.  Sharp at (t^2, t^{2d+1}).
                  (R1)-(R4)     exact necessary conditions on a minimal gauge,
                                incl. mult_O = n - p; n_min >= n_AM(Gamma),
                                tabulated for delta_aff <= 8.
                  MERIDIAN-FLOOR  n_min >= ceil((N-1)/(W - sum_l s_l))
                                >= ceil((N-1)/(W-1)); at W = 2, >= N-1.
                  N-VS-MAPDEG(half)  max(deg P,deg Q) >= ceil((N-1)/(W-1)).
                  beta <= floor(delta_aff/2) in (B2); k <= delta_aff - delta_c in
                                (B3) -- both delta_infty-free.
                  2 g(E) = 1 + N nu - n_infty(E)   (exact form of B3E's cap).

CORRECTED /       * delta_aff, not n_min, is the invariant the consumers eat.
SHARPENED         * CD's OPEN[DELTA-INFTY-NOT-NUMERICAL] is off the critical path
                    for the (B2) beta-bound and the (B3) budget.
                  * CD Sec 5 (self-typed budget-only): row n=4, (2,3), k=1 is EMPTY
                    (delta_aff = 2 forces n_min = 5); row k=2 is realised.  The
                    minimal (B3) profile is realised at n = 5.
                  * The charge's item (3) family cannot exist (DEG-DELTA(b)); the
                    family that does block the gate has unbounded k, and is given.
                  * grok item (d) CONFIRMED but not new: NO-DEG-CAP [D],
                    reducible-all-n-opus5-20260901.md:335-343.

MEASURED          Gamma, delta_aff, conductor, symmetry and minimal generators for
                  30+ explicit parametrisations, incl. CO's realised (9,6,2) curve
                  (delta_aff = 4, delta_infty = 24) and CD's variant
                  (delta_infty = 13) -- both matching the charged inputs exactly.
                  Numerical-semigroup census to genus 10 (counts 1,1,2,4,7,12,23,
                  39,67,118,204 -- the known sequence).  AM admissibility: 0
                  violations of (F) and 0 of DEG-DELTA(b) over the census;
                  max_Gamma n_AM = 2 delta + 1 for every delta <= 10.  Ledger
                  satisfiability at k <= 10^4 for 7 (N,a) cells.  Cusp+k-node
                  family verified for k = 2,3,5,6,8,9,11.

NOT CLAIMED       any kill of (B2)/(B3) at any N; any upper bound on delta_aff or
                  n_min in N; that any exhibited curve is A_F for a Keller map;
                  realisability of any profile as a Keller non-properness set;
                  anything about case (A), the A2 cells, Z(G), or the reducible
                  branch beyond citing NO-DEG-CAP.

OPENS RAISED      OPEN[MIN-EMBED-DEGREE]  is n_min <= 2 delta_aff + 1
                    unconditional (does the Tschirnhausen step always apply when
                    b_1 | b_0)?  Blocks only the delta-form of the Sec 6.3 crossing.
OPENS RETYPED     OPEN[DEG-AF-VS-N] -> OPEN[DELTA-AFF-VS-N] (invariant form); its
                  raw form stays FALSE (NO-DEG-CAP [D]).  OPEN[N-VS-MAPDEG] keeps
                  its upper half only; the lower half is answered here.
                  OPEN[DELTA-INFTY-NOT-NUMERICAL] demoted: real, off the critical
                  path for the (B2)/(B3) consumers.

SUCCESSOR         Two, both aimed at delta_aff, not at n.
                  (1) UPPER BOUND ON delta_aff.  Sec 6.3 prices it: at W = 2 a
                      bound n_min <= C with C < N-1 kills the column at every N.
                      The only instrument in the record producing upper bounds of
                      this shape is Chau's cap, so this is exactly
                      OPEN[N-VS-MAPDEG] and should be staffed as such.
                  (2) SHARPEN MERIDIAN-FLOOR with the group.  Its proof uses only
                      the meridian cycle type and transitivity; feeding in the
                      CUSP-CAGE relations and the point-stabiliser conditions
                      should raise (N-1)/(W-S), and every unit of increase lowers
                      the price in (1) in proportion.

DEVIATIONS        (1) The charge's item (3) asked for a witness family if no bound
                      exists; DEG-DELTA(b) shows that family cannot exist, so
                      non-derivability was certified instead by a satisfying
                      assignment of the whole banked constraint set (Sec 5.1) plus a
                      realised curve family (Sec 5.2).
                  (2) MERIDIAN-FLOOR was not on the charged instrument list; it is
                      the only N-monotone statement this lane found and it prices
                      the successor, so it is reported in full.
                  (3) Desk CAS: total wall time under 12 minutes, peak memory well
                      under 200 MB.  Drivers left in /tmp/degaf (sg3.py, am2.py,
                      am3.py, am4.py, family2.py, family3.py, delta2.py, ledger.py,
                      tables.py), not installed in box/.
```

<!-- BODY-END -->
