# B3-E-GEOMETRY — the (B3) horn attacked through the source curve `E = F^{-1}(A_F)`

Lane: `B3-E-GEOMETRY`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact symbolic algebra (sympy 1.14, rationals only). No
Groebner, no AWS, no literature fetched, no web. Drivers in `/tmp/b3e`, not
installed in `box/`.

## 0. Custody, method, scope

The seven charged frozen copies were hashed with `shasum -a 256` **before any
was read**; all seven match the charge exactly:

```text
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
424e2f5ddec7189efa90c4259b19394ccee75e3eec4842ed1879544cb8fd7fd2  horn-flagship-review-grok46-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
e30c80f34d04ceecf0575541401bb57956464925a894117920006072a7bd3f3e  ideation-20260902T0741Z-grok46.md
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  ideation-20260902T0741Z-opus5.md
58020a0e85692a6a92e16db18fe2d540f6073e9de596c1348d3596c3597e8202  ideation-20260902T0741Z-fable51.md
b905417b8b62339af75d4a339f207c65926e53c47f8dbd80005a92479d5a0fa8  ideation-20260902T0741Z-fable51-coordinator.md
```

Below: **HF** = HORN-FLAGSHIP, **HR** = its grok-4.6 hostile review (verdict:
promote B3-DEGREE, B3-CAGE, B3-LOC, B3-PUSHOFF, B3-COMPONENT, Props 3.1-3.2,
B3-N4, HORN-A2 at the printed scope incl. `SCOPE[B3-QH]`), **MI** =
MPRIME-ALLN-H2. The four ideation files are cited as **PROPOSALS** only; no
statement of theirs is consumed as a result. Repository files read for the
fresh-eyes task (§6): `xmodel/do1-mu2-replay-sol56-20260901.md`,
`xmodel/integration7-coordinator-fable5-20260902.md`. No charged file was
edited; no repository file other than this report was written.

Consumed at their CONFIRMED typing: HF B3-N4, Props 3.1/3.2, B3-DEGREE,
B3-CAGE, B3-PUSHOFF, B3-COMPONENT, `SCOPE[B3-QH]`. Consumed at
PROVED-HERE/UNREVIEWED typing (MI, review-CONFIRMED where noted): Lemma A,
Lemma 4.1 (fibre law `N - a_p = r_p W + K_p`), Orevkov Lemma 2.1 as MI states
it, control 2 (`a_p = a` at smooth `p`), 7.B' (`mu_l >= 2`), N4-PIN, THEOREM
PROFILE. **Not consumed:** `Z(G) = 1` (HR types it GAP); any `A2`-cell result
(different object); the unreviewed `CUSP-A-VOID` claim (case (A), different
object).

No `charge_basis` line: this report asserts no new exit price.

## 1. Verdict, up front

```text
NO KILL.  The (B3) object survives all four charged mechanisms.  Three of the
four are closed with a REASON rather than left as NEEDS-DATA, and one of those
reasons is itself an all-N theorem.

(G-KAPPA)  CLOSED, NO-GO, ALL N, WITH PROOF.  F restricts to a FINITE ETALE
   cover A^2\E -> A^2\A_F of degree N (proper exactly off the non-properness
   set, etale by Keller).  Hence kappa-bar(A^2\E) = kappa-bar(A^2\A_F), and
   BOTH log Chern numbers scale by N: c_2-bar by covering multiplicativity and
   c_1-bar^2 by the log ramification formula K+D = pullback of K+D.  So
   c_1-bar^2 <= 3 c_2-bar holds on the SOURCE pair iff on the TARGET pair
   (THEOREM E-BMY-VACUITY): no log-BMY-type instrument on E can ever say
   anything the same instrument on A_F does not, at any N and any profile.
   Row 28's wall is inherited exactly; the arm is not blocked, it is void.
   The Galois-closure variant inherits it too (degree 24 for N).  The one
   genuinely different instrument is the ORBIFOLD pair on the TARGET; it needs
   deg A_F-bar AND the non-cyclic branching at L_infty:
   OPEN[ORBIFOLD-BMY-AT-INFINITY].

(G-SPLICE) CORRECTS THE CHARGE'S PREMISE, THEN STOPS ON DEGREE AS INSTRUCTED.
   NOT all five places of E at infinity sit on the dicritical.  Exactly the
   places converging to AFFINE points do, and (LOC-1, all N) a place of E at
   infinity can converge only to a SINGULAR point of A_F.  At N=4, k=1 the
   split is  2 (over the one place at infinity of A_F) + 1 (over the cusp)
   + 2 (over the node), so THREE of five sit on l', at the three points of
   l' over Sing A_F.  New bridge (THEOREM E-CHARGE): a place of E at infinity
   over a branch b is charged against Orevkov's excess k_t = mu_t - e_t*mu_l
   at t in l' EXACTLY WHEN it lies over the same branch b that l' covers; at a
   unibranch point this is forced and saturates, giving a - a_p = K_p with the
   whole of K_p carried by places of E at infinity.  Consequence: at a cusp
   the link-at-infinity ledger of E IS the (K) ledger, not a new one.  The
   splice/Neumann compatibility test needs the L_infty-multiplicities of the
   five places, i.e. deg E-bar.  Not pinned:  OPEN[E-INFINITY-SPLICE-DEGREE].
   Degree-free lower bounds obtained: deg E-bar >= n_infty(E) = 5 and
   (d-1)(d-2)/2 >= g + sum_p a_p delta_p.

(G-EMBED) ANSWERED, NEGATIVE FOR THE CAMPAIGN: such curves EXIST.  Explicit
   verified witness (quintic, §4): rational, exactly five places at infinity,
   one ordinary (2,3) cusp and nothing else affine, chi_c = -3 -- the exact
   numerical type of the k=1, k_odd=1 cell.  No embedding obstruction to kill.

(G-ANTI)  RUN IN FULL, ALL N.  NO CROSSING, at any N, with a closed form.
   Degree-free covering cap:  2g(E) <= 1 - a + sum_p r_p*max(0,(r_p-1)W+K_p-1),
   sharp at N=4 (it returns g <= k-1, and B3-N4 gives g = k_odd-1 <= k-1).
   On the minimal (B3) profile (one cusp + one double point) the maximum over
   all counting-admissible (a, K_c, K_m) is exactly  2g <= N-3, positive at
   every N >= 4, so the covering window is never empty.  Adding double points
   only raises the cap.  The single unbounded parameter is the number of
   double points -- equivalently deg A_F-bar.  OPEN[DEG-AF-VS-N] is therefore
   not one candidate input among several; it is the ONLY thing between the
   present ledger and a degree-monotone obstruction.

(FRESH EYES)  The N=4 object is Orevkov's one-dicritical profile
   (mu, corr) = (2,1).  The lemma set that excludes it is Domrina-Orevkov I
   §§2-7 (local census Lemmas 8-9 -> six global graphs -> Lemmas 10-15), on the
   determinant apparatus Prop 3 / Lemmas 1-5.  NOT N-uniform: the census is
   finite only because of sum_{a~ in a'} Deg a~ = 4, which is literally N=4.
   And it is entirely a BOUNDARY argument -- it never touches Sing A_F, rho or
   E.  The literature kill and the campaign cage attack disjoint halves of the
   same object, which is why the cage saturates without emptiness.
```

## 2. (G-KAPPA): the arm is void, at every `N`, and that is a theorem

### 2.1 The one structural fact the arm forgot

> **LEMMA E-ETALE.** Let `F` be a plane Keller map of geometric degree `N`,
> `A_F` its non-properness set, `E := F^{-1}(A_F)`. Then
> ```text
>      F : A^2 \ E  -->  A^2 \ A_F
> ```
> is a **connected finite étale covering of degree `N`**.
>
> *Proof.* `F` is proper over `A^2 \ A_F` by the definition of the
> non-properness set, and `F^{-1}(A^2\A_F) = A^2 \ E`; proper + quasi-finite
> is finite. `Jac F ∈ C^*` makes `F` étale everywhere. `A^2\E` is the
> complement of a curve in `A^2`, hence connected. ∎

MI uses this fact throughout ("`F` proper and étale over `A^2 \ D`"), and HF
§3.3 already noticed one of its consequences —
`chi(C^2\E) = 4 chi(C^2\A_F)`, correctly dismissed there as "the degree-4
identity, vacuous". What was not noticed is that the **same scaling holds for
the other log Chern number**, and that is the number log-BMY needs.

### 2.2 THEOREM E-BMY-VACUITY

> **THEOREM E-BMY-VACUITY (all `N`, all profiles).** Write `V := A^2\A_F`,
> `V' := A^2\E`, `mu := F|_{V'} : V' -> V` finite étale of degree `N`. Then
> ```text
>  (a)  kappa-bar(V') = kappa-bar(V) ;
>  (b)  c_2-bar(V') := e(V') = N e(V) =: N c_2-bar(V) ;
>  (c)  if (X,D) is any log compactification of V with D reduced and X normal,
>       and (X',D') is the normalisation of X in C(V') with D' := (mu-bar)^{-1}(D)_red,
>       then  K_{X'} + D' = mu-bar^*(K_X + D)  and hence  (K_{X'}+D')^2 = N (K_X+D)^2 .
>  (d)  consequently, for the log-minimal models, c_1-bar^2(V') = N c_1-bar^2(V),
>       and the log-BMY inequality  c_1-bar^2 <= 3 c_2-bar  holds on V' if and
>       only if it holds on V.  The same is true of any inequality that is
>       homogeneous of the same weight in (c_1-bar^2, c_2-bar).
> ```
>
> *Proof.* (b) is multiplicativity of the topological Euler characteristic in
> a finite covering. (c): `mu-bar : X' -> X` is finite and étale over `X\D`,
> so all ramification is along `D'`; with `e_i` the ramification index along
> the component `D'_i`, Riemann-Hurwitz gives
> `K_{X'} = mu-bar^*K_X + sum_i (e_i-1)D'_i`, while `mu-bar^*D = sum_i e_i D'_i`.
> Adding, `K_{X'}+D' = mu-bar^*K_X + sum_i e_i D'_i = mu-bar^*(K_X+D)`;
> squaring and using `(mu-bar^*Z)^2 = N Z^2` gives the second clause.
> (a): with `L := O_X(m(K_X+D))`, (c) gives `mu-bar^*L = O_{X'}(m(K_{X'}+D'))`,
> and `mu-bar` finite flat gives
> `H^0(X', mu-bar^*L) = H^0(X, L ⊗ mu-bar_*O_{X'})` with `mu-bar_*O_{X'}` of
> rank `N`; so `P-bar_m(V) <= P-bar_m(V')` and `P-bar_m(V')` is bounded by a
> fixed rank-`N` twist of `P-bar_m(V)`, which does not change the growth order
> in `m`. Hence the two log-Kodaira dimensions agree. (This is Iitaka's étale invariance of
> `kappa-bar`; the sketch is included because no source was fetched.) (d)
> follows from (b)+(c) once both sides are evaluated on log-minimal models;
> `X'` may acquire quotient singularities along `D'`, which is exactly the
> category in which `(K+D)^2` is the right invariant. ∎

**What this closes.** The charge's step 0 was "compute `kappa-bar(A^2\E)`; if
it is `-infinity`, say so — that is row 28's known wall". The answer is
sharper and does not require computing anything:

```text
 kappa-bar(A^2 \ E) = kappa-bar(A^2 \ A_F)  identically, for every N and every
 profile.  Whatever row 28's wall is on the target, the source inherits it
 EXACTLY.  There is no sense in which E is "a better object for BMY" than
 A_F: the two log Chern vectors are proportional with ratio N, so every
 scale-invariant inequality is literally the same inequality.
```

I therefore do **not** report a value for `kappa-bar`. Determining it is a
target-side problem identical to the one row 28 already carries, and the
lane's charge was to test whether the source curve gives a new handle. It
does not. `NO-GO`, with a proof rather than a stall.

### 2.3 The Galois-closure variant, honestly typed

Let `X-hat` be the normalisation of the target `A^2` in the Galois closure of
`C(x,y)/C(P,Q)`, `G-hat = rho(G) = S_4` at `N=4` (HF Prop 3.1). Over
`A^2\A_F` the covering `A^2\E -> A^2\A_F` is étale, hence so is its Galois
closure: `X-hat \ (preimage of A_F) -> A^2\A_F` is finite étale of degree
`|S_4| = 24`. THEOREM E-BMY-VACUITY applies verbatim with `N` replaced by
`24`. So the **log**-BMY inequality on `X-hat` is again the target inequality.

The genuinely different instrument is the **orbifold** pair — `K_{X-hat}`
without removing the branch divisor, i.e. `(P^2, (1-1/e)·A_F-bar + L_infty)`
with `e = ord rho(m) = 2` (meridian a transposition, HF Prop 3.1). That is a
target-side numerical inequality in `(n, p, q, k, t_i, rho)` with
`n = deg A_F-bar`, and it is not covered by the theorem above. Two inputs it
needs and does not have:

```text
 OPEN[ORBIFOLD-BMY-AT-INFINITY].  The S_4-cover does NOT extend over L_infty
 as a branched cover with a well-defined orbifold index: the boundary
 behaviour is the dicritical (s,mu) = (1,2), i.e. the covering degenerates
 along a curve that maps ONTO A_F-bar, not onto L_infty.  Until the
 compactification of X-hat over L_infty is written, the orbifold Chern numbers
 of the pair are not defined.  This is a different obstruction from the degree.
 The charge's sentence "orbifold BMY there needs only (p,q,k,t_i,rho), all
 pinned at N=4" is FALSE as written: it also needs n and the boundary model.
```

Cross-branch note (a PROPOSAL, not consumed): `ideation-...-opus5` retypes
`OPEN[DEG-AF-VS-N]` into an answered half `n = M max(d,e)` (Chau) and an open
half `OPEN[N-VS-MAPDEG]`. If the answered half is promoted, the first input
above is supplied and only the boundary model remains.

## 3. (G-SPLICE): where the five places actually are, and what charges them

### 3.1 The exact bookkeeping (all `N`)

`F` étale + MI control 2 give the covering `E° -> A_F°` of degree `a` used in
HF (2.5.1). Compactifying both sides:

```text
 A_F~ ≅ A^1  (MI Lemma A),  A_F~-bar = P^1 ;  punctures of A_F° upstairs:
 one per branch of A_F at each singular point (R := sum_{p in Sing} r_p of
 them), plus the ONE place at infinity of A_F.
 E~-bar -> P^1  is finite of degree a, unramified over A_F°, hence ramified
 only over those 1+R punctures.
```

> **PROPOSITION 3.1 (fibre split).** Over the puncture `P_b` attached to a
> branch `b` of `A_F` at `p ∈ Sing A_F`, the fibre of `E~-bar -> P^1` contains
> **exactly `a_p` points with ramification index 1**, namely one for each of
> the `a_p` affine preimages `y ∈ F^{-1}(p) ∩ A^2` (for each such `y`,
> `F : (E,y) -> (A_F,p)` is an isomorphism of germs because `F` is étale, so
> `y` has one branch over each `b`, unramified). The remaining points of that
> fibre have total degree
> ```text
>          a - a_p  =  (r_p - 1) W + K_p            [MI Lemma 4.1]
> ```
> and are **places of `E` at infinity**. Over the puncture at infinity of
> `A_F` the whole degree `a` is carried by places of `E` at infinity.
>
> **COROLLARY (LOC-1).** A place of `E` at infinity converges to an affine
> point of `A_F` only if that point is **singular**: at a smooth `p`,
> `a_p = a` (MI control 2), so the fibre is entirely affine.

> **COROLLARY 3.2 (degree-free identities).** With `s := #Sing A_F`,
> ```text
>   n_infty(E)  =  (R-1)a + 2 - 2g(E) - sum_p a_p r_p ,
>   chi_c(E)    =  a(1-R) + sum_p a_p .
> ```
> *Control.* At `N=4` (`a=2`, `W=2`, cusp `r=1,K=1,a_p=1`, `k` double points
> `r=2,K=0,a_p=0`, so `R = 1+2k`) the second reads `chi_c(E) = 2(1-1-2k)+1 =
> 1-4k`, reproducing N4-PIN. The first, with the Riemann-Hurwitz genus, was
> checked against THEOREM B3-N4 for every `(k,k_odd)` with `k <= 8`: all
> `n_infty` and `chi_c` agree exactly, and `g` agrees for `k_odd >= 1`
> (`k_odd = 0` returns the arithmetic genus `-1` of the disconnected `j=2`
> curve, as it must). Driver `/tmp/b3e/struct.py`.

**The charge's premise, corrected.** At `N = 4`, `k = 1`, ordinary node, the
five places of `E` at infinity split as

```text
   2  over the place at infinity of A_F  (unramified: t_1 odd is a NODE
                                          puncture, not the infinity puncture)
   1  over the cusp puncture P_0         (a - a_{p_0} = 1, index 1)
   2  over the two node punctures P_1^±  (a - a_{q_1} = 2 each, ramified,
                                          one place of index 2 each)
```

so the charge's "the places of `E` at infinity sit on the unique affine-image
dicritical" is true of **three** of the five, not all five. The other two are
genuine ends over `L_infty`.

### 3.2 THEOREM E-CHARGE: which places are paid for by Orevkov's `k_t`

Let `Phi : X -> P^2` be Orevkov's compactified model, `l` a dicritical,
`l' = l ∩ Phi^{-1}(A^2) ≅ A^1`, `mu_l = ord_l Phi^*(A_F-bar)`,
`phi_l = eta ∘ h_l : l' -> A_F` with `deg h_l = s_l`, and for `t ∈ l'`,
`mu_t := deg_t Phi` and `k_t := mu_t - e_t mu_l >= 0` (MI Lemma 4.1, `e_t` the
local degree of `h_l` at `t`). Let `E-bar_X ⊂ X` be the closure of `E`. MI's
reading of Orevkov Lemma 2.1 — the boundary is a disjoint union of linear
chains, each with a single dicritical endpoint and a contracted tail attached
at one point of `l` — gives that no boundary component other than `l` meets
`l'`, so at `t ∈ l'` the only curve germs inside `Phi^{-1}(A_F-bar)` are `l'`
itself and the branches of `E-bar_X`.

> **THEOREM E-CHARGE.** Let `t ∈ l'`, `p := Phi(t) ∈ A_F`, and let `b` be the
> branch of `A_F` at `p` that `phi_l` covers near `t`. Then
> ```text
>     k_t  >=  sum over branches Gamma of E-bar_X at t with Phi(Gamma) = b
>                 of  deg( Phi|_Gamma ).
> ```
> In particular:
> * (i) if `p` is a **smooth** point of `A_F`, `b` is the only branch, so every
>   branch of `E-bar_X` at `t` is charged; since `K_p = a - a_p = 0` at a
>   smooth point, `E-bar_X` misses `l'` over the smooth locus — an independent
>   proof of LOC-1, purely intersection-theoretic;
> * (ii) if `p` is **unibranch singular** (a cusp), again `b` is the only
>   branch, so `sum_{places xi of E at infinity over p} deg(Phi|_xi) <= K_p`;
>   the covering count of Prop 3.1 gives that sum `= a - a_p = K_p` exactly
>   (`r_p = 1` in MI Lemma 4.1). **The inequality is an equality: at a cusp,
>   Orevkov's excess `K_p` is precisely the total degree of the places of `E`
>   at infinity lying over it.**
> * (iii) at a **multibranch** point, the branches of `E-bar_X` at `t` mapping
>   to branches other than `b` are **not** charged to `k_t`; they are paid for
>   by the `(r_p - 1)W` term. At `N=4` they are the only ones present: at
>   `t ∈ l'` over the node, `mu_t = 2 = mu_l`, `e_t = 1`, so `k_t = 0` and no
>   branch of `E-bar_X` at `t` may map to `b`.
>
> *Proof.* Let `L` be a generic line through `p`. For a curve germ `C` at `t`,
> the projection formula gives `(C · Phi^*L)_t = deg(Phi|_C)·(Phi(C)·L)_p`, and
> for germs `C, C'` at `p` without common component the local degree formula
> gives `(Phi^*C · Phi^*C')_t = mu_t (C·C')_p`. Now `ord_{l'} Phi^*(b) = mu_l`
> (the multiplicity of `l` in `Phi^*(A_F-bar)` is `mu_l`, and locally only the
> branch `b` carries it), `ord_Gamma Phi^*(b) = 1` for each branch `Gamma` of
> `E-bar_X` mapping onto `b` (`E = F^*A_F` is reduced because `F` is étale).
> Hence
> `mu_t (b·L)_p = (Phi^*b · Phi^*L)_t >= mu_l (l'·Phi^*L)_t + sum_Gamma (Gamma·Phi^*L)_t
>  = [ mu_l e_t + sum_Gamma deg(Phi|_Gamma) ] (b·L)_p`,
> and `(b·L)_p > 0` cancels. For (iii) at `N=4`: `k_t = 0` forces the sum to be
> empty. ∎

**Consequence for the arm.** By (ii), at a cusp the link-at-infinity data of
`E` and the `(K)` ledger are the *same* numbers, so a splice computation over
the cusp cannot produce information independent of `(K)` — a second, weaker
N-blindness in the same direction as §2. The only genuinely new boundary data
live at multibranch points, clause (iii), where the places of `E` at infinity
are *branch-exchanged*: at `N=4` the place of `E` over the node branch `b_+`
sits at the point of `l'` lying over `b_-`, and vice versa (`E` reduced forces
`ord_Gamma Phi^*b_+ + ord_Gamma Phi^*b_- = 1`, `l'` already carries `mu_l = 2`
on its own branch, and `k_t = 0` forbids `Gamma` from sharing it). A splice
diagram read off `l'` naively therefore mislabels the components.

### 3.3 The degree, and the stop

Neumann/Eisenbud-Neumann compatibility for the link at infinity of a plane
curve is a statement about the *multiplicities* `d_i = (E-bar · L_infty)` at
each of the five places, and `sum_i d_i = deg E-bar`. Those are not pinned:

```text
 OPEN[E-INFINITY-SPLICE-DEGREE].  deg E-bar is not determined by the (B3)
 numerical type.  What IS determined, degree-free:
    deg E-bar  >=  n_infty(E)  ( = 5 at the k=1 ordinary-node cell ),
    (d-1)(d-2)/2  >=  g(E) + sum_p a_p delta_p          [ delta_p the delta of
                      the germ of A_F at p; a_p copies appear on E because F
                      is etale, so delta_aff(E) = sum_p a_p delta_p ]
    which at k=1, k_odd=1, (p,q)=(2,3) reads (d-1)(d-2)/2 >= 0 + 1, i.e. d>=3,
    and is therefore weaker than the first bound.
 Per the charge, this arm STOPS here.  I did not invent a degree formula; in
 particular deg E-bar = N * deg A_F-bar is NOT used anywhere and is not
 implied by anything above (a = 2 is deg(E -> A_F), not deg F).
```

§4 shows independently that nothing in the numerical type forces a large
degree: the type is realised by an honest plane quintic.

## 4. (G-EMBED): the curve exists — explicit, verified witness

**Question, as charged.** Is there a rational plane curve with exactly five
places at infinity, one ordinary `(2,3)` cusp, and no other affine
singularity?

**Answer: YES.** Here is one, found by a five-condition parametrisation
construction and then verified independently from its implicit equation.

```text
 WITNESS E_0.   Parametrisation (birational, t ∈ P^1):

    x(t) = (149 t^2 - 785 t + 1100) / ( t (t-1)(t-2) ) ,
    y(t) = (3 t - 13) / ( (t-3)(t-4) ) .

 Implicit equation (irreducible over Q, total degree 5):

   72 X^2Y^3 + 450 X^2Y^2 + 823 X^2Y + 455 X^2
   - 2064 XY^3 - 10461 XY^2 - 34776 XY - 6699 X
   + 14792 Y^3 + 57491 Y^2 + 332717 Y  =  0 .
```

Verified facts (sympy 1.14 over `Q`, drivers `/tmp/b3e/embed*.py`):

```text
 (1) Irreducible over Q; total degree 5; leading form  X^2 Y^3.
 (2) Poles of the parametrisation: t = 0,1,2,3,4 -- exactly FIVE places at
     infinity, all transverse to L_infty (each pole simple), and
     0+1+2+3+4 multiplicities sum to 5 = deg.
 (3) Points at infinity: [0:1:0] carries the three branches t=0,1,2 with
     pairwise-distinct tangents (slopes y(0),y(1),y(2) = -13/12, -5/3, -7/2)
     -- an ORDINARY TRIPLE POINT, delta = 3.
     [0:0:1] carries the two branches t=3,4 with equal slopes
     x(3) = x(4) = 43/3 and contact exactly 2 (computed: the difference of the
     two Puiseux branches z = phi_i(v) is  -2233 v^2/72 + O(v^3) )
     -- a TACNODE, delta = 2.
 (4) Affine singular locus, computed from the implicit equation as the full
     solution set of (f, f_X, f_Y): the single point (X,Y) = (15,1).
     Its 2-jet is 2(30X-31Y)^2 (a double tangent line) and its 3-jet
     Y(1939X^2+3327XY+32Y^2) is not divisible by (30X-31Y), so the germ is
     A_2.  Confirmed on the parametrisation: at t = 5 one has x-15 and y-1
     both of order 2 in (t-5), and the tangent-killed combination has order
     exactly 3 -- branch semigroup <2,3>, an ORDINARY (2,3) CUSP, delta = 1.
 (5) Injectivity: x(t1)=x(t2), y(t1)=y(t2) with t1 != t2 has ONLY the
     solutions (3,4) and (4,3) -- i.e. only the tacnode at infinity.  So the
     parametrisation is injective on P^1 minus the five poles, and birational.
 (6) delta-budget:  3 + 2 + 1 = 6 = (5-1)(5-2)/2 = p_a.  Hence geometric
     genus 0 and NO further singularity anywhere.  chi_c(E_0) = 2 - 0 - 5 = -3.
```

`chi_c(E_0) = -3` is exactly N4-PIN's `chi_c(F^{-1}(A_F)) = 1-4k` at `k = 1`,
and the whole tuple `(g, n_infty, #affine sings, type) = (0, 5, 1, (2,3))` is
exactly THEOREM B3-N4's `k = 1`, `k_odd = 1` cell.

```text
 TYPING.  E_0 is REPRESENTATIVE ONLY.  It is a plane curve with the required
 numerical type; NOTHING here claims it is F^{-1}(A_F) for a Keller map, nor
 that any Keller map exists, nor that E_0 admits a degree-2 map onto a
 one-place-at-infinity rational cuspidal curve.  Its only role is to answer
 the charged question, and the answer kills the arm:  (G-EMBED) can produce
 no obstruction, because the object it was asked to obstruct exists.
```

Two notes. The construction is uniform, not lucky: three poles over one point
of `L_infty` and two over another force `delta_infty >= 4`; the tangency
`x(3) = x(4)` raises it to `5`; `x'(t_0) = y'(t_0) = 0` supplies the cusp; and
the genus formula forces `delta_aff = 1` with nothing else. Both conditions are
*linear* in the numerator coefficients once `t_0` is chosen, so a one-parameter
family of witnesses exists for every `t_0 ∉ {0,1,2,3,4,7/2}`. And
`deg E_0 = 5` while `N·deg A_F-bar >= 12`: the type does not force a large
degree, one more reason the degree ansatz the charge forbids is false.

## 5. (G-ANTI): counting versus covering, all `N` — no crossing, with the reason

### 5.1 The covering-admissible side, degree-free

From Prop 3.1: over a branch puncture at `p`, the fibre of `E~-bar -> P^1` has
`a_p` unramified points plus places of total degree `a - a_p`, hence at least
`a_p + 1` points when `a_p < a`; over the puncture at infinity it has at least
one point. Riemann-Hurwitz `2g-2 = -2a + sum_P (a - n_P)` then gives:

> **THEOREM B3-E-GENUS (all `N`, `H2`, any profile).**
> ```text
>   2 g(E)  <=  1 - a  +  sum_{p in Sing A_F}  r_p · max( 0 , (r_p-1)W + K_p - 1 )
> ```
> with `sum_p K_p = a - 1` and `a_p = N - r_p W - K_p >= 0` (MI `(K)`, Lemma 4.1).

*Sharpness control.* At `N=4` (`a=W=2`, cusp `(r,K)=(1,1)`, `k` double points
`(r,K)=(2,0)`) the bound reads `2g <= -1 + 2k`, i.e. `g <= k-1`; THEOREM B3-N4
gives `g = k_odd - 1 <= k - 1`, attained at `k_odd = k` (all contacts odd, in
particular ordinary nodes). **The bound is attained.**

### 5.2 The counting-admissible side and the tabulation

Counting-admissible (THEOREM PROFILE, case (B3)): `N >= 4`,
`ceil(N/2) <= a <= N-2`, `W = N - a >= 2` (7.B'), at least one cusp
(`r_p = 1`) and at least one multibranch point (`r_p >= 2`), `sum_p K_p = a-1`,
`K_p <= D_gap = 2a - N` at multibranch points `(C2)`, `a_p >= 0`.

Driver `/tmp/b3e/anti.py` enumerates, for `N = 4..20` and every admissible `a`,
the **minimal** (B3) profile (one cusp + one double point) and maximises the
covering cap over the admissible split `K_c + K_m = a-1`, `K_m <= D_gap`:

```text
  N   a   W  Dgap    covering cap                N   a   W  Dgap    covering cap
  4   2   2     0    2g <= 1                    12   6   6     0    2g <= 9
  5   3   2     1    2g <= 2                    13   7   6     1    2g <= 10
  6   3   3     0    2g <= 3                    14   8   6     2    2g <= 11
  6   4   2     2    2g <= 3                    ...
  7   4   3     1    2g <= 4                    17   9   8     1    2g <= 14
  8   4   4     0    2g <= 5                    ...
  9   5   4     1    2g <= 6                    20  11   9     2    2g <= 17
 10   5   5     0    2g <= 7                    20  18   2    16    2g <= 17

  Cells with an EMPTY covering window: NONE.
```

The table is generated by a closed form, which I then verified by hand: with
`K_m = min(a-2, D_gap) = 2a-N` (admissible since `a <= N-2`) and
`K_c = a-1-K_m`, the cap is `2W + K_m - 3 = 2(N-a) + (2a-N) - 3 = N - 3`,
**independent of `a`**. So

```text
 THEOREM B3-E-NOCROSS.  On the minimal (B3) profile the covering-admissible
 genus window is  0 <= g(E) <= (N-3)/2 ,  nonempty at every N >= 4.  Adding
 double points strictly enlarges it (each contributes +2 max(0,W-1) >= +2).
 There is NO crossing between the counting-admissible and covering-admissible
 ranges at any N, and none can appear from these two ingredients alone.
```

### 5.3 What a crossing would need — named exactly

The genus cap that the charge wanted from "a plane curve of bounded degree"
runs the wrong way without a degree bound: the plane-curve identity is

```text
   g(E) = (d-1)(d-2)/2  -  sum_p a_p delta_p  -  delta_infty(E),   d := deg E-bar,
```

which for fixed `g` bounds `d` from **below**, not above. So the crossing test
is blocked on an *upper* bound for `d`, and the same computation identifies
the one unbounded parameter on the counting side: the number of double points
of `A_F` (each has `K_p = 0`, so `(K)` never limits how many there are). Both
blockages are the same blockage:

```text
 The degree of A_F-bar bounds the number of double points through the
 delta-budget  delta(p,q) + sum_i t_i + delta_infty = (n-1)(n-2)/2 ;  a bound
 on the number of double points bounds R, hence caps THEOREM B3-E-GENUS, hence
 caps g(E), hence -- with the plane-curve identity -- caps d = deg E-bar.
 OPEN[DEG-AF-VS-N] is therefore not one of several candidate inputs; it is the
 unique gate.  This lane's independent confirmation of MI §9's ranking.
 OPEN[B3-INFINITY-RANK] (HF) is NOT needed for G-ANTI: the covering cap above
 is derived without pinning r_O at the infinity orbits.
```

## 6. Fresh eyes: which lemma kills this object at `N = 4`, and is it uniform?

**Locating the object in the literature's own coordinates.** N4-PIN gives one
dicritical with `(s_1, mu_1) = (1,2)`. Orevkov's budget for one dicritical at
`N = 4` is `mu + corr = N - 1 = 3`, so the (B3) `N=4` object sits in the
profile `(mu, corr) = (2,1)`. In Domrina-Orevkov I's own notation
(`do1-mu2-replay-sol56-20260901.md:53-60`) this is
`n(g~) = 2, m(g~) = 1, Deg g~ = 2` — **the `mu = 2` track**.

**The lemma set.** Per that replay's assembly table
(`do1-mu2-replay-sol56-20260901.md:711-719`), the three one-dicritical profiles
close as `(1,2)` by campaign Prop 4.1, `(3,0)` by campaign Cor 3.8, and
`(2,1)` — ours — by **§§2-7 of Domrina-Orevkov I**: the complete local
neighbourhood census (published Lemmas 8-9, a 35-row enumeration), its assembly
into six global boundary graphs (§6), and the elimination of all six (published
Lemmas 10-15), resting on the determinant apparatus of Proposition 3
(`det R_a = 1`, `det D_a > 1`, `det L_a > 1`, `det L = -1`, pairwise-coprime
branch determinants) and Lemmas 1-5, with the campaign's own repairs to
Proposition 4, Lemma 7, Corollary 5, the `delta(ab)>0` step of Lemma 10, three
omitted companion cases, and the Lemma 13 citation, all binding.

**Is the mechanism `N`-uniform? NO.** The finiteness of the argument is
literally `N = 4`. The generic-sheet identity used to bound the local data is

```text
   sum_{a~ over a}  Deg a~  =  4               (formula (9), p. 854)
```

which yields the four-element fork list `(D;m,n) = (2;2,1),(3;3,1),(4;4,1),(4;2,2)`,
and it is that four-element list that makes the 35-row census and the six-graph
assembly finite. At general `N` the identity reads `sum Deg a~ = N`, the fork
list is every `(D;m,n)` with `mn = D <= N`, and both the census and the graph
assembly grow without any stated uniformity. The genuinely degree-free
ingredients are the determinant/transfer package (Lemmas 1-5, Prop 3, the edge
formula) and Riemann-Hurwitz on `F|_{a~} : P^1 -> P^1` — those transport, but
they are the *tools*, not the *kill*.

**The structural point this lane wants on the record.** The Domrina-Orevkov
mechanism is a **boundary** argument: it works entirely inside the dual/splice
graph of `X \ A^2` and its determinants. It never uses `Sing A_F`, never uses
`rho`, and never mentions `E = F^{-1}(A_F)`. The campaign's `(B3)` cage
(B3-DEGREE, B3-CAGE, Props 3.1-3.2, B3-N4) is entirely **affine and
representation-theoretic**: it uses `Sing A_F`, `rho`, and `E`, and says
nothing about the boundary graph. The two instruments attack disjoint halves of
the same object. That is a complete explanation of HF's finding that the cage
is "rigid but not empty": the cage was never going to close `(B3)`, because the
half of the object that the literature's `N=4` kill actually uses is the half
the cage does not touch. THEOREM E-CHARGE (§3.2) is the first bridge between
the two halves — it identifies Orevkov's boundary excess `k_t` with the
degrees of `E`'s places at infinity over a cusp — and, read as a
recommendation, it says the successor should be a boundary instrument fed by
the affine data, not a further affine instrument.

## 7. FALLACY-v2 audit

* **Flag/place/series.** Five objects kept strictly apart throughout:
  `A_F ⊂ target A^2`; its normalisation `A_F~ ≅ A^1`; `E = F^{-1}(A_F) ⊂ source
  A^2`; its normalisation/smooth model `E~`, `E~-bar`; and the dicritical
  `l ⊂ X\A^2` with `l' ≅ A^1`. Places of `E` at infinity (points of
  `E~-bar \ E~`) are never identified with points of `E-bar_X ∩ L~` without the
  branch-by-branch dictionary of §3.1-§3.2, and §3.2(iii) records that the two
  labellings differ by a branch exchange at `N=4`. `a = deg(E -> A_F)` is kept
  apart from `N = deg F` and from `deg E-bar`.
* **Carrier/attainment.** `E_0` (§4) is typed `REPRESENTATIVE`: it realises the
  numerical type and nothing more; no realisation of any Keller map is claimed.
  THEOREM B3-E-GENUS is an upper bound and is stated as one; its attainment at
  `N=4` is exhibited against B3-N4, not assumed.
* **Floor/attainment.** §3.3's `deg E-bar >= n_infty(E)` and the delta-budget
  inequality are floors and are labelled as floors; no exact degree is asserted.
  §5's "no crossing" is a statement that the window is nonempty, not that any
  point in it is realised.
* **Per-ray / exit-set charge.** THEOREM E-CHARGE charges each branch of
  `E-bar_X` at `t` **once**, to `k_t`, and only when `Phi(Gamma) = b(t)`; the
  branches over other branches of `A_F` are explicitly declared uncharged and
  attributed to the separate `(r_p-1)W` term of MI Lemma 4.1. The two
  contributions to `a - a_p` are never added twice: §5.1 uses
  `a - a_p = (r_p-1)W + K_p` as MI's single identity.
* **Pole/interior.** The local degree and projection formulas are applied only
  where `Phi` is a finite map germ, i.e. at `t ∈ l'` with `Phi(t) ∈ A^2`; that
  no other boundary component meets `l'` is quoted from MI's statement of
  Orevkov Lemma 2.1, not assumed.
* **Variable/ring map.** §4's parametrisation-to-implicit passage is by
  resultant and was checked in both directions (the affine singular locus
  computed from the implicit equation matches the parametrisation's critical
  point, and the branch data match the Puiseux expansions).
* **Prime label/derivative.** In §3 primes are labels (`l'`, `P_1^±`, `b_±`); in
  §4-§5 the only derivatives are `x'(t), y'(t)` and are written as such. The two
  never occur in the same display.
* **`sat()` / raw remainder.** Not in play: no ideal saturation, no Groebner
  basis, no normal form in a quotient ring. `sympy.solve` on `(f, f_X, f_Y)` was
  used and its output is a complete finite solution set, printed in full.
* **Not filled by cap or analogy.** Where `deg E-bar` is needed I stop and type
  `OPEN[E-INFINITY-SPLICE-DEGREE]`; where the orbifold cover's boundary model is
  needed I type `OPEN[ORBIFOLD-BMY-AT-INFINITY]`; where Iitaka's étale
  invariance of `kappa-bar` is used I give a proof sketch rather than cite a
  source I did not fetch; where the arms do not kill, I say so.

## 8. Typed verdict block

```text
LANE              B3-E-GEOMETRY
SCOPE             Keller, noninvertible, H2, case (B3); the source curve
                  E = F^{-1}(A_F).  Cusp quasi-homogeneous only where HF's
                  local theory is invoked (SCOPE[B3-QH], charged, not banked).
                  §§2,3.1,5 use no quasi-homogeneity at all.

PROVED HERE       LEMMA E-ETALE      F : A^2\E -> A^2\A_F is connected finite
                                     etale of degree N.
                  E-BMY-VACUITY      kappa-bar and BOTH log Chern numbers of
                                     A^2\E are the target's, scaled by N;
                                     log-BMY upstairs <=> log-BMY downstairs.
                                     ALL N, ALL PROFILES.
                  PROP 3.1 / LOC-1   fibre split of E~-bar -> P^1; no place of
                                     E at infinity over a smooth point of A_F.
                  COR 3.2            n_infty(E) and chi_c(E) = a(1-R)+sum a_p,
                                     degree-free; controls B3-N4 for k<=8.
                  E-CHARGE           k_t >= sum deg(Phi|_Gamma) over the
                                     same-branch branches of E-bar_X at t;
                                     equality at every unibranch point, so
                                     a - a_p = K_p is carried entirely by
                                     places of E at infinity.
                  B3-E-GENUS         2g(E) <= 1-a+sum_p r_p max(0,(r_p-1)W+K_p-1),
                                     attained at N=4 (g <= k-1).
                  B3-E-NOCROSS       minimal (B3) profile: 2g(E) <= N-3
                                     independently of a; covering window
                                     nonempty at every N; no crossing.
                  WITNESS E_0        explicit rational plane quintic, five
                                     places at infinity, one ordinary (2,3)
                                     cusp, no other affine singularity,
                                     chi_c = -3.
                  All PROVED-HERE, UNREVIEWED.

CORRECTED HERE    the charge's "the places of E at infinity sit on the unique
                  affine-image dicritical" -- only those converging to affine
                  points do (3 of 5 at N=4, k=1).
                  the charge's "orbifold BMY needs only (p,q,k,t_i,rho), all
                  pinned at N=4" -- it also needs deg A_F-bar and a boundary
                  model for the S_4-cover over L_infty, which does not exist
                  as a cyclic branched cover (the dicritical maps ONTO A_F-bar).

CONSUMED          HF: B3-N4, Prop 3.1, Prop 3.2, B3-PUSHOFF, B3-COMPONENT,
                  B3-DEGREE, B3-CAGE, SCOPE[B3-QH] -- at HR's CONFIRMED typing.
                  MI: Lemma A, Lemma 4.1, control 2, 7.B', N4-PIN, THEOREM
                  PROFILE, MI's statement of Orevkov Lemma 2.1.
                  Repo (fresh-eyes only): do1-mu2-replay assembly table;
                  integration #7's N=4-CHECKED-CLOSED chain.

MEASURED          E_0: irreducibility, degree, leading form, the two
                  singularities at infinity with their exact deltas (3 and 2),
                  the unique affine singular point (15,1) and its A_2 type via
                  both the implicit 2-/3-jets and the branch semigroup,
                  injectivity off the poles (complete solution set {(3,4),(4,3)}).
                  B3-N4 control: n_infty and chi_c for every (k,k_odd), k<=8.
                  G-ANTI table: N = 4..20, every admissible a, zero empty cells.

NOT CLAIMED       any kill of (B3) at any N; any EMPTY window in N; that E_0 is
                  F^{-1}(A_F) for any map; a value for kappa-bar(A^2\A_F);
                  deg E-bar; realisability of any (p,q) or k; anything about
                  case (A), the A2 cells, or Z(G).

OPENS RAISED      OPEN[E-INFINITY-SPLICE-DEGREE]   deg E-bar unpinned; blocks
                                                   every Neumann/EN splice test.
                  OPEN[ORBIFOLD-BMY-AT-INFINITY]   the S_4-cover has no cyclic
                                                   branched model over L_infty;
                                                   orbifold Chern numbers of
                                                   (P^2, (1/2)A_F-bar + L_infty)
                                                   are undefined until it does.

OPENS RE-RANKED   OPEN[DEG-AF-VS-N] is the UNIQUE gate for G-ANTI, confirmed by
                  the closed form of §5 rather than asserted.
                  OPEN[B3-INFINITY-RANK] is NOT needed for anything in this lane.
                  OPEN[B3-J1-KILL] (HF's successor #2, "a route through the
                  ends"): this lane closes the BMY end of it (§2) and shows the
                  cusp end is the (K) ledger (§3.2); what remains is exactly the
                  multibranch clause E-CHARGE(iii), which is where the only
                  uncharged boundary data of E live.

SUCCESSOR         A BOUNDARY instrument fed by affine data, not another affine
                  instrument.  Concretely: extend E-CHARGE(iii) to a global
                  count on l' -- E-bar_X . l with the three (at N=4) contact
                  multiplicities computed in §3.2 -- against Orevkov's
                  determinant package on the same chain.  That is the one place
                  where the campaign's ledger and Domrina-Orevkov's ledger meet.

DEVIATIONS        (1) The charge said "stop at the first kill".  No arm killed,
                      so all four were run to completion; G-KAPPA was closed by
                      a theorem rather than by computing kappa-bar, which the
                      charge did not anticipate and which is strictly stronger
                      than the anticipated "kappa-bar = -infinity" outcome.
                  (2) G-EMBED was answered by construction rather than by an
                      obstruction search, within the charged desk budget
                      (< 1 min, < 100 MB).
                  (3) Drivers left in /tmp/b3e, not installed in box/.
```

<!-- BODY-END -->


## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `40006`.
- Body SHA-256:
  `87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2`.
- Frozen basis: `ca191fe1dd43f936e6c06f714a167bc55cab731a`.
