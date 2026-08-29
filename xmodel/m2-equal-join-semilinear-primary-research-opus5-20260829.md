# Equal-arrival merge families and the `M>=2` semilinear quotient — primary research (Opus 5, 2026-08-29)

Lane: exact Opus 5, maximum reasoning, primary research.
Target: the one regime the prior round left open — equal-`(mu,w)` nonzero-arrival
merges, where `kbar` is affine and unbounded in the merge-local index `nu_G`.

## 0. Custody, scope, honesty

Read in full: my prior report
`xmodel/m2-budget-quotient-primary-research-opus5-20260829.md`
(`ffb83ec1fcbfbbb18573a030e80e22c20a7d78bb92a5e7a6a5ce4d7b9b96e7af`, body
`b161421ccb04a62307b87be4a60f130ded64fe53228bd600c960f2c502632283` — both
re-verified this session);
`xmodel/m2-budget-quotient-falsifier-grok46-20260829.md`
(`df776b25565fb43c2f45fd8bc64db822d5775822b834fa58fe7f45db2f1a4e54`);
`xmodel/m2-finite-reduced-chain-skeleton-sol56-20260829.md`
(`239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad`, body
`8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb`);
`xmodel/m2-caseiii-two-pole-incoming-index-bound-sol56-20260829.md`
(`406e78d220b62910e6296866db998bd0e7d898b2e6a618fe0aa70ffbeb73fd46`, body
`8a16cad9cc3211f90e86b1cc31a3fe2991f3817138ae9da4f6dbc56ddf7b5c43`);
and the exact current `ladder/BOOK-OFFAXIS.md` (all of §§0–11a),
`ladder/SHEET6-DEPTH.md`, `ladder/SHEET6-MULTIPOLE.md` (MP0–MP9, D1–D9,
OBSTRUCTION O), and `ladder/REDUCTION.md` CRITICAL 4–7 / §§5.1–5.4 / frontier
overlay. Two further cited anchors were opened to fix conventions, not to
import results: `xmodel/sol-td7-law.md` (the generalized zero-chain law and its
equations (1)–(9)) and the header of `cases/l1_ode_check.py` (families A/B/C
normalization) and `ladder/SHEET6-III.md` §3 (the N1 statement).

Not done, as instructed: **no access of any kind to `jc2-lean`**; no
`git status` or other workspace-wide command; no web, AWS, Singular, msolve,
Sage, PARI or heavy CAS; no canonical edit; no commit or push. Writes are
exactly the two licensed paths.

Trust perimeter: unchanged from the prior round — `BOOK-OFFAXIS.md` §10's
perimeter verbatim (corrected St 9.3 (24) with the E6 sign fix, St 9.4
(25)/(26) with H3-psi, St 8.4, MP2, MP5/MP8 on `b=1` chains, R1.0, R1.2/R1.4,
R2.1/R2.2, Prop 9.3 (a)–(m)), plus the promoted §11 T1 zero-chain law and
§11a E5 census as *recorded*, both with their stated conditionality. I add no
hypothesis. Every clause below inherits R4 superset semantics
(**alive != existent**), the P0 honesty rider (`lambda` values are lower
bounds), and the stage-R policy that `n_e in N*` and `i`-sync are never used to
kill.

No landing, ceiling, `G2-BD`, `RPMC(C)`, Keller or JC2 inference is drawn
anywhere in this report.

## 1. Verdict in one paragraph

The `C_e = 0` theorem of my prior round was **stated with the wrong
quantifier and is repaired here to a sharp classification**: a merge admits
infinitely many `nu_G` **iff** *every* arriving edge degenerates simultaneously,
which happens iff all arrival multiplicities are equal, all *effective*
arrival invariants are equal, `k = lex = 0`, and no chain arrives at the
0-direction (Theorem A). One nonbinding edge with `C_e = 0` is never enough —
the two-edge consistency residual is affine in `nu_G` with *two* coefficients,
and the constant one is exactly what forbids unequal `mu`. I then give the
complete equal-arrival calculus in closed form for every free-0-root variant
(Theorem B), prove the admissible `nu_G` set is an explicit finite union of
arithmetic progressions with `nu_G = 1` the only exceptional value (Theorem C),
and prove that the **entire downstream reduced state is constant** and `M` is
periodic even though `kbar` is affine and unbounded (Theorem C'). Consequently
**no numerical `kbar` bound is needed for the combinatorial full-configuration
ledger** (§5): every combinatorial consumer is constant or periodic on the
progression, and the unique consumer that reads the full parameter is a later
case-III zero-edge for which this merge is itself the leaving vertex — bounded
by sol56's two-pole theorem. Attacking the first consumer proper, I derive the
**general merge Prop. 8.1(iv) reduction (T1-GEN)**, which specializes exactly
to `sol-td7-law.md` (3)/(4) and to `l1_ode_check.py` families A/B/C, and show
that on the unbounded family the whole T1 content collapses to the one-line
criterion `r*Rad - t*Rad_t = const`, i.e. `Rad(t) = t^r - A` — **T1 does not
kill the family; it rigidifies its coefficients, uniformly in `nu`**
(Theorem D/E). The honest outcome of charge 4 is therefore the third option:
**an explicit infinite alive family**, exhibited concretely at `td = 12`,
`m = 3`, `M = [2,2,2]`, where the entry data are *forced* arithmetically, the
merge is `lambda = 0`, and a single trunk step reaches a legal terminal at
`Sigma lambda = 8 <= td - 1 - psi = 9` for **every** member of the progression.
Finally I repair the `nu <= mu_0*num(w_0)` statement: sol56 is right that it
binds `nu_G` and not the incoming `nu_H`, and it additionally needs the
*effective* 0-edge invariant, which makes it vacuous under the promoted E5
reading — but the *conclusion* (case III is always `nu_G`-bounded) survives
under both H5a readings by the consistency argument, and under E5 it is
strengthened from "bounded" to "pinned to one value" (§7).

## 2. Setting: one uniform transport law for all three Prop 9.3 cases

At a merge `G` (`r >= 2` arriving edges) the R1.0/R2.2 reduced pattern is

    p = (-) eta^eps * prod_{e=1..r0} (eta^nu - c_e^nu)^{mu_e}
                    * prod_{j=1..k}  (eta^nu - d_j^nu)^{m_j}
    q = (-) eta * (each distinct nonzero p-orbit ONCE) * (lex extra simple orbits)

    P  = sum_e mu_e + sum_j m_j,   s = r0 + k + lex,
    dp = eps + nu*P,   dq = 1 + nu*s,   M = gcd(dp, dq),
    T  = P - s*eps  (!= 0 by the root-mult law (R)).

`eps = mu_0` iff a chain arrives at the 0-direction (Prop 9.3 case III);
otherwise `eps >= 0` is a **free 0-root** priced by P2. Give every arriving
edge an **effective invariant**

    what_e = w_e            (case I/II, nonzero direction; R2.1)
    what_0 = nu_H * w_H     (case III zero-edge, printed DEPTH §5c)
             or  nu_G * w_U (case III zero-edge, promoted E5/(I4) reading)

Then R2.1 and Prop 9.3(b) give one transport law for **every** edge:

    E_e := mu_e*dq - dp = (mu_e - eps) + nu*C_e,   C_e := mu_e*s - P,   (2.1)
    kbar * E_e = mu_e * what_e * dq,   X = kbar*dp/dq = mu_e*(kbar - what_e),
    rho = kbar/dq,   w_child = (kbar - rho)/nu = mu_e*what_e*s/E_e.      (2.2)

(For the zero-edge, `mu_0 = eps` makes (2.1) read `E_0 = nu*C_0`, and (2.2) is
`X = mu_0(kbar - what_0)` — R2.1's case-III line verbatim.) Recorded laws used,
no new hypotheses: (S) `mu_e*dq > dp` on every arriving edge; (NE) `m_j*dq < dp`
and `eps*dq < dp` strictly on every non-arriving orbit; (R) `dp != mu*·dq`;
(I) `kbar in Z` at `nu >= 2` (DS1(c)/Not 3.5), `kbar in Q` at `nu = 1`
(case I); N1 `gcd(kbar, nu) = 1` at every `nu >= 2` vertex
(`SHEET6-III.md` §3); MP2 `M >= 2` at interior vertices `<= G*`; the P0/P2
`lambda` rule.

(NE)+(S) give the load-bearing inequality `m_j <= mu_min - 1` and
`eps <= mu_min - 1`, used throughout.

## 3. Charge 1 — the repaired quantifier

> **Theorem A (unbounded classification).** Fix the discrete merge data
> (`r0`, `{mu_e}`, `k`, `{m_j}`, `lex`, `eps`, the 0-regime, and the effective
> invariants `{what_e}`) and let `nu_G` vary. The set of legal `nu_G` is
> **infinite** if and only if
>
> 1. no chain arrives at the 0-direction (case III absent), **and**
> 2. all arrival multiplicities are equal, `mu_e = mu`, **and**
> 3. all arrival invariants are equal, `w_e = w`, **and**
> 4. `k = 0` and `lex = 0`, equivalently `C_e = 0` for every `e`
>    simultaneously.
>
> In every other regime `nu_G` is bounded, with an explicit bound; in the
> case-III regime it is bounded under **both** H5a readings, and under the
> promoted E5 reading it is *pinned to a single value*.

*Proof.* **(a) Two-edge consistency is affine with two coefficients.** For
edges `e != f`, equality of the two expressions for `kbar` in (2.2) is
`kappa_e*E_f = kappa_f*E_e` with `kappa_x := mu_x*what_x > 0`, i.e. by (2.1)

    kappa_e[(mu_f - eps) + nu*C_f] = kappa_f[(mu_e - eps) + nu*C_e].     (3.1)

(3.1) is affine in `nu`. It holds for infinitely many `nu` iff both

    (i)  kappa_e*C_f = kappa_f*C_e          (slope)
    (ii) kappa_e*(mu_f - eps) = kappa_f*(mu_e - eps)   (constant)

vanish. Multiply (ii) by `s` and subtract (i), using `C_x = mu_x*s - P`:

    kappa_e*(P - s*eps) = kappa_f*(P - s*eps),  i.e.  (kappa_e - kappa_f)*T = 0.

Since `T != 0` (law (R) at the multiplicity `eps`; if `eps = 0` then `T = P > 0`
outright), `kappa_e = kappa_f`. Feeding that back into (ii) and using
`kappa_e > 0` gives `mu_e = mu_f`, hence `what_e = what_f`. This proves 2 and 3
and shows **a single degenerate edge is never sufficient**: the constant half
(ii) is load-bearing, and it is exactly the half my prior Theorem 2.1 dropped.

**(b) With all `mu_e = mu` equal, `C_e = C = mu*(k + lex) - sum_j m_j`,** and
`m_j <= mu - 1` gives `C >= k + mu*lex >= 0` with equality iff `k = lex = 0`.
If `C >= 1` then `kbar = mu*w*(1 + nu*s)/((mu - eps) + nu*C)` is strictly
decreasing in `nu` with limit `mu*w*s/C`, so each integer value of `kbar`
determines `nu` uniquely and only finitely many `nu` are legal. This proves 4.

**(c) Case III is always bounded.** *Printed DEPTH §5c reading* (`what_0`
independent of `nu_G`): the classification of (a),(b) applies verbatim, and
`eps = mu_0 = mu` forces `E_0 = nu*C_0` with `C_0 >= 1` by (S) on the zero
edge; hence `C != 0` and (b) bounds `nu_G`. *Promoted E5 reading*
(`what_0 = nu_G*w_U`): now `kbar = mu_0*w_U*dq/C_0` is affine in `nu_G`, so
consistency with any nonzero edge `e` gives
`E_e = mu_e*w_e*C_0/(mu_0*w_U)`, a constant; hence `C_e = 0` and
`E_e = mu_e - mu_0 > 0` by (S), so `mu_e > mu_0`; but `C_e = 0` means
`P = mu_e*s`, whence `C_0 = (mu_0 - mu_e)*s < 0`, contradicting `C_0 >= 1`.
So `C_e != 0` and `nu_G = [mu_e*w_e*C_0/(mu_0*w_U) - (mu_e - mu_0)]/C_e`
is a **single determined value**. ∎

**Regimes in which some merge-local quantity is unbounded — the complete list.**

| regime | condition | what is unbounded | reduced child state |
|---|---|---|---|
| **U1 EQJOIN** | `nu_G >= 2`, equal `(mu,w)`, `k = lex = 0`, no 0-arrival | `nu_G`, `kbar`, `dp`, `dq`, `X` | **constant** `w_tr`, **periodic** `M` |
| **U2 case-I tail** | `nu_G = 1` (Prop 9.3 case I, `kbar in Q`), equal `(mu,w)`, `lex` free | `lex`, `dq`, `s` | `w_tr` takes **infinitely many** values, `-> w` |
| bounded | everything else, incl. **all** case III, all unequal `mu`, all unequal `w`, all `k >= 1` | — | — |

U2 is a genuine second regime that my prior report wrongly folded into its
family 6a. It is the `td=7` `(2,2t) M2` tail of `BOOK-OFFAXIS.md` P3 class A
(`w_tr = 2 + 1/(t-1)`, the record's own formula), and it is *not*
reduced-state-finite: `num(w_tr) -> infinity`. It exists only at `nu_G = 1`,
because integrality of `kbar` bounds `lex` at every `nu_G >= 2` (each integer
value of `kbar in (w, ...]` determines `lex` uniquely, and `kbar -> w` as
`lex -> infinity`). At `td = 7` the record closes U2 by budget (P4, "first-step
inversion `u | 2dq` / `u | dq`, no caps hit"). **U2 is not otherwise closed and
is the second-ranked open object of §10.**

## 4. Charge 2 — the general equal-arrival calculus

> **Theorem B (closed forms; every free-0-root variant).** Let `r >= 2`
> arrivals have common multiplicity `mu` and common invariant `w = a/b` in
> lowest terms, `k = lex = 0`, and a free 0-root of multiplicity `eps` with
> `0 <= eps <= mu - 1` (`eps = 0` = absent; `eps = mu` is forbidden by (NE),
> `eps > mu` by (S)). Write `E := mu - eps`. Then, for every legal `nu`,
>
>     p = (-) eta^eps * prod_{e=1..r}(eta^nu - c_e^nu)^mu,
>     q = (-) eta     * prod_{e=1..r}(eta^nu - c_e^nu)
>
>     dp = eps + nu*r*mu,        dq = 1 + nu*r,        s = r,  P = r*mu
>     E_e = E = mu - eps         (independent of nu, every edge)
>     kbar = mu*w*(nu*r + 1)/E   (affine, unbounded)
>     rho  = mu*w/E              (constant)
>     X    = mu*(kbar - w) = mu*w*(eps + nu*r*mu)/E
>     M    = gcd(mu - eps, nu*r + 1)          (EXACT, not merely a divisor)
>     T    = r*(mu - eps),  so M | T
>     trunk child: (w_tr, M) with  w_tr = mu*w*r/(mu - eps)   (CONSTANT)
>     lambda_G = 0 if eps = 0, else max(1, ceil(mu*w*r/eps))  (CONSTANT)

*Proof.* `dp, dq, s, P` are the §2 definitions. `E = mu*dq - dp = mu - eps`
by (2.1) with `C = 0`. (2.2) gives `kbar`, `rho`, `X`, `w_tr`. For `M`:
`M | dp` and `M | dq` give `M | mu*dq - dp = mu - eps`; conversely any common
divisor of `mu - eps` and `dq` divides `mu*dq - (mu - eps) = dp`. Hence
`M = gcd(mu - eps, dq)` exactly. The price: `X/eps - kbar = kbar*(dp - eps*dq)/(eps*dq)`
and `dp - eps*dq = nu*r*(mu - eps)`, so `(X/eps - kbar)/nu = mu*w*r/eps`,
which is `w_tr*(mu-eps)/eps`; `k = 0` contributes nothing. ∎

Two immediate consequences the record does not contain.

* **`M` is odd whenever `r` is even.** `dq = nu*r + 1` is then odd. In
  particular at `r = 2` (forced at `m = 2` by MP1) **MP2 forces the odd part of
  `mu - eps` to be `>= 3`, hence `mu >= 3`.** Verified exhaustively for
  `mu <= 40` and for the `eps >= 1` variants in the packet.
* **Every recorded `m = 2` off-axis headline entry is no-jump-dead.** An
  equal-arrival merge needs one common `mu` dividing `M_{H_e}` on *both*
  chains; with no prior `M`-raising step `M_{H_e} | b_i`, so
  `mu | gcd(b_1,b_2)`. The headline `M`-vectors of `BOOK-OFFAXIS.md` §1 are
  `[1,2]`, `[2,2]`, `[2,5]`, `[2,3]`, `[2,1]`, `[1,3]`, `[2,5]`, whose gcds are
  `1,2,1,1,1,1,1`; in every case `mu - eps <= 2` has odd part `1`, so `M = 1`
  and MP2 kills. **Both chains must first execute an `M`-raising dirty step.**
  (Rider: §1 prints headline rows, not the full 23-row table; the argument is
  stated for the rows the record prints.)

> **Theorem C (the admissible `nu` set).** With `w = a/b`, put
> `B' := b*E / gcd(b*E, mu*a)` and
> `R := prod{ prime p : v_p(mu*a) > v_p(b*E) }`. Then for `nu >= 2`
>
>     kbar in Z        <=>  B' | dq = nu*r + 1
>     MP2 (M >= 2)     <=>  some prime p | (mu - eps) has  nu*r == -1 (mod p)
>     N1 gcd(kbar,nu)=1 <=> gcd(nu, R) = 1
>
> Each condition is a congruence condition on `nu`; hence the admissible set is
> a finite union of residue classes modulo `L := lcm(B', mu - eps, R)`,
> intersected with `[2, infinity)`, and it is **infinite whenever it is
> nonempty**. The `kbar`-integrality class is nonempty iff `gcd(r, B') = 1`,
> and it is then the single class `nu == -r^{-1} (mod B')`.

*Proof.* `kbar = mu*a*dq/(b*E)`, so `kbar in Z` iff `b*E | mu*a*dq` iff
`B' | dq`. `M = gcd(mu - eps, dq)` is a function of `nu mod (mu - eps)`.
For N1: `gcd(dq, nu) = 1`, so if a prime `p` divides `nu` then `p ∤ dq` and
`v_p(kbar) = v_p(mu*a) - v_p(b*E)`, which is **independent of `nu`**; hence
`gcd(kbar, nu) > 1` iff `nu` shares a prime with `R`. ∎

**Exceptional values.** Exactly one: `nu_G = 1`. There the merge is a Prop 9.3
case-I lattice meet in `V_{2,a} \ V_{1,a}`, `kbar in Q` is legal, N1 does not
apply, and the regime is U2 rather than U1. It must be stored as an explicit
special value, never as a member of the progression. (My prior §6a listed
`(mu,w,nu) = (3,3,1)` as a family member; that is erratum **E5** below.)
Secondarily, if `n_e in N*` were ever promoted from "never used to kill" to a
kill, it would remove at most a finite initial segment, since
`n_e = nu_e*kbar_G - kbar_e` is affine and increasing in `nu_G` — the family
would stay semilinear.

> **Theorem C' (downstream constancy).** On a U1 family, with the arrivals and
> the discrete data fixed: `w_tr`, `lambda_G`, the whole P0 successor menu of
> the trunk, the P1 terminal data of any descendant, and the T1 verdict at `G`
> are **constant** in `nu_G`; `M_G` and everything downstream of it are
> **periodic** with period dividing `mu - eps`; and `kbar_G, X_G, dp, dq, n_e`
> are affine and unbounded.

*Proof.* `w_tr` and `lambda_G` are constant by Theorem B; `M` is periodic by
Theorem C. The trunk's P0 menu is a function of `(w, M)` and the trunk vertex's
own indices (BOOK-OFFAXIS P0), so it inherits constancy/periodicity. The P1
terminal data are a function of `(w_t, M_t)` (`psi = ceil(M/j) - 1`,
`j = M(1 - w_t)`). The T1 verdict is Theorem E below. ∎

## 5. Charge 3 — the ledger does not need a numerical `kbar` bound

The answer is **no**, with an exact statement of what replaces it.

> **Theorem F (semilinear sufficiency).** For the *combinatorial*
> full-configuration ledger — every kill in the recorded grammar (S), (NE),
> (R), (I), N1, MP2, St 8.4, R2.1/R2.2, P0/P1/P2 pricing, the §11 T1
> zero-chain law, and the §11a E5 matching — a U1 merge may be represented by
> the single normalized family record below, with **no** upper bound on `kbar`.
> The unique consumer that reads the full parameter is a later Prop 9.3
> case-III zero edge **whose leaving vertex is this merge itself**; there the
> parameter is bounded (§7).

Normalized record (schema `EQJOIN-FAMILY/v1`, emitted by the packet):

    kind        = "EQJOIN"
    r, mu, eps                                   (integers, 0 <= eps <= mu-1)
    w           = "a/b"                          (lowest terms)
    E_gap       = mu - eps ;  T = r*(mu - eps)
    lambda      = 0 or max(1, ceil(mu*w*r/eps))
    w_child     = "mu*w*r/(mu-eps)"              (exact fraction, constant)
    kbar_affine = { slope = mu*w*r/(mu-eps), intercept = mu*w/(mu-eps) }
    M_law       = "gcd(mu-eps, r*nu + 1)"
    kbar_integrality_modulus = B'
    n1_radical  = R
    period      = L_min       (the MINIMAL period, computed, not declared)
    residues_mod_period = sorted list
    t1          = "RIGID: prod_e (t - c_e^nu) = t^r - A, A != 0"
    consumes_full_nu = ["case-III-zero-edge-when-this-merge-is-the-leaving-vertex"]

**Equality and hash rules.** Two records are equal iff their canonical JSON
(sorted keys, `,`/`:` separators, no floats, fractions serialized `"a/b"` in
lowest terms) is byte-identical; the family hash is the SHA-256 of that blob.
`period` must be reduced to the *minimal* period before hashing, and `residues`
reduced modulo it; otherwise two presentations of the same family would hash
differently. Members are recorded as `(dp, dq, nu, M, kbar)` **carrying the
family key as provenance** — never keyed on the cell tuple alone.

> **Theorem G (no duplicate families; but cells do collide).**
> (a) A U1 family determines `(r, mu, eps, w)`: `r = (dq - 1)/nu`, the pair
> `(slope, intercept) = (r*mu, eps)` of `dp` as a function of `nu` is
> determined by any two members, and `w = kbar*(mu-eps)/(mu*dq)`. Hence
> **whole-family collisions are impossible**.
> (b) Individual **cells do collide across distinct records**: `(2,10,0,9)`
> and `(2,9,4,5)` both give `(dp, dq, nu, M, kbar, X, w_tr) =
> (40, 5, 2, 5, 45, 360, 18)` at `nu = 2`, differing only in
> `lambda in {0, 23}` and in the family key. Their `dp` slopes `20` and `18`
> differ, so the collision is confined to that one member.

(b) is the exact realization of the "D9-style duplicate family" hazard the
brief names, and it is why the ledger must key on the *labelled* record, not on
`(dp,dq,nu,M)`. It is control **C4** of the packet, replayed under `-O`.

**Consumers that still need the full parameter.** Exactly one, plus two
riders:

1. **Case-III zero edge with this merge as the leaving vertex.** Then
   `what_0 = nu_G*w_tr` (printed §5c reading), and the sol56 two-pole theorem
   bounds `h = nu_H = nu_G` explicitly. Under the promoted E5 reading the
   later merge's own `nu` is used instead and `nu_G` does not enter at all.
2. *(rider)* `n_e in N*` and `i`-sync, if ever promoted to kills — affine,
   hence uniform beyond a finite threshold.
3. *(rider)* the coefficient/gluing tier, which reads the actual arrival
   directions `c_e`; Theorem E below shows the constraint there is uniform in
   `nu` too, but this report makes no realizability claim.

This is the exact repair of Grok's falsifier §1.2 `S3/S5` objection at the
merge layer: the objection is correct that `(w, M, nu mod M)` is too coarse,
and the fix is not a bigger congruence but the **labelled family record plus a
finite exceptional table**, which is what sol56's L3 asked for and what
Theorem C' now supplies for the U1 sector.

## 6. Charge 4 — the first consumer, attacked

### 6.1 The general merge T1 equation

> **Theorem D (T1-GEN).** Let a merge pattern be
> `p = eta^eps * prod_i (t - A_i)^{n_i}`, `q = eta * Rad(t) * S(t)` with
> `t = eta^nu`, `Rad = prod_i (t - A_i)`, `deg S = lex`, `nu >= 2`. Then
> Prop. 8.1(iv) in the normalized form `rho*p*q' - p'*q = C*p`,
> `rho = dp/dq`, is **equivalent** to
>
>     (rho - eps)*W + rho*nu*t*W_t - nu*t*S*sum_i n_i*prod_{i'!=i}(t - A_{i'}) = C
>                                                                   (T1-GEN)
> with `W = Rad*S`. For equal multiplicities `n_i = mu` it becomes
>
>     (rho - eps)*Rad*S + nu*(rho - mu)*t*Rad_t*S + rho*nu*t*Rad*S_t = C.  (T1-EQ)

*Proof.* `p' = eta^{eps-1}[eps*Pfull + nu*t*Pfull_t]` and `q' = W + nu*t*W_t`;
substituting and dividing by `eta^eps*Pfull` gives (T1-GEN), the division being
legitimate because `t*Pfull_t*W = t*Pfull*S*sum_i n_i*prod_{i'!=i}(t-A_{i'})`. ∎

(T1-GEN) is verified as an **exact symbolic polynomial identity in the unknown
pattern coefficients** (not by sampling) for 13 parameter tuples in the
emitter and for a `4 x 3 x 3 x 3 x 3` grid in the test suite, with three
deliberate mutations of the reduced expression all detected.

**Anchoring.** (T1-GEN) specializes to every printed instance:

| specialization | data | recorded form |
|---|---|---|
| class B/C (`sol-td7-law.md` (3)) | one nonzero orbit, `n = 1`, `eps = mu_0` | `(rho-mu)(t-A)s + (rho-1)nu t s + rho nu t(t-A)s' = C̃` |
| `l1_ode_check.py` family A | `eps = 0`, `mu = 1`, `r = 2` | `rho*pt*s + nu*rho*t*pt*s' + (rho-1)*nu*t*pt'*s` |
| `l1_ode_check.py` family C | `n = (2,1)`, `eps = 0`, `S = 1` | `rho*pt*w + nu*rho*t*pt*w' - nu*t*pt'*w` |
| D9 / `nu = 1` (eta absorbed, `q = p*s`) | `r = 2`, `rho = 2/(2+l)` | `2*p*s' - l*p'*s = c'` |

The class-B/C coefficient of `t^k` is `alpha_k*s_{k-1} - beta_k*A*s_k` with
`alpha_k = rho(1 + nu k) - d`, `beta_k = rho(1 + nu k) - mu_0`, `d = dp`, and

    beta_k/alpha_k = (1 + d*k - mu_0*(l+1)) / (d*(k - l - 1)),

which is `sol-td7-law.md` eq. (4) **verbatim**; identity (8),
`mu_0(l+1) - 1 + dq = dp(l+1)`, and the law `T1-dead <=> dp | dq` follow. All
of this is control **C3**, checked on six parameter tuples including the
promoted class-B cell `(3,9,2,3)`, which is re-killed.

### 6.2 T1 on the unbounded family: rigidity, not death

> **Theorem E (T1-EQJOIN).** On a U1 family (`lex = 0`, equal `mu`, free
> 0-root `eps`), (T1-EQ) multiplied by `dq` is **identically**
>
>     nu*(mu - eps) * [ r*Rad(t) - t*Rad_t(t) ] = C*dq.
>
> Hence, for every `nu`, Prop. 8.1(iv) has an admissible solution
> (`C != 0`, `q`-roots simple and off `0` and off each other) **iff**
>
>     Rad(t) = t^r - A   with A != 0,   i.e.  e_1 = ... = e_{r-1} = 0
>     on the arrival bases {c_e^nu},
>
> and then `C = -nu*r*(mu - eps)*A/dq != 0` automatically.

*Proof.* By (2.1) with `C_e = 0`, `dp - eps*dq = nu*r*(mu - eps)` and
`dp - mu*dq = -(mu - eps)`; substituting into `dq*(T1-EQ)` with `S = 1` gives
the display. `r*Rad - t*Rad_t = sum_{j=0}^{r-1}(r - j)*pi_j*t^j` is constant iff
`pi_j = 0` for `1 <= j <= r-1`, i.e. `Rad = t^r + pi_0`; the top coefficient
`j = r` vanishes identically (top-degree cancellation), and `C = r*pi_0*
nu*(mu-eps)/dq`. Admissibility: the `r` roots of `t^r - A` are distinct and
nonzero for `A != 0`, and `q = eta*Rad` has all roots simple with
`eta || q`, matching R1.0. ∎

So **T1 does not kill the family**. It imposes a codimension-`(r-1)`
*coefficient* rigidity — the `r` arriving orbit bases must be the `r`-th roots
of one number, so the full root set of `p^red` is `{0}^eps` together with a
single `(r*nu)`-orbit — and it does so *uniformly in `nu`*. This is a direct
correction of my prior report, which declared family 6a "not T1-dead" by
citing the `dp | dq` law; that law is proved only for the class-B/C shape and
does not apply here (erratum **E3**).

**Positive control (C1).** The same machinery, run on the promoted `td = 6`
residue cell `(r, nu, l) = (2, 3, 1)`, `(dp,dq) = (6,10)`, `M = 2`, returns
`Rad = t^2 - (3/2)B t + (3/8)B^2`, `C = -9B^3/40 != 0`, whose root ratio
satisfies `pi_1^2/pi_0 = 6`, i.e. `A_1/A_2 = 2 +- sqrt(3)` — **exactly
OBSTRUCTION O's rigid coefficients**. An independent reconstruction of a
promoted number from a general theorem.

**Negative control (C2, the td-6 D9 family).** `SHEET6-MULTIPOLE.md` MP9/D9
records the interior survivor set "IIa(`l` odd, `nu >= 3` odd), `M = 2`", an
infinite *pattern-level* family. It is `mu = 1`, `eps = 0`, `r = 2`,
`lex = l >= 1`, hence `C = l >= 1`, hence **bounded** by Theorem A. Concretely
`T = P = 2`, `M | 2`, `E = l*nu + 1 <= M*mu*num(w) = 4` at `w = 2`, so
`l*nu <= 3` and integrality of `kbar` leaves exactly `(l,nu) = (1,3)`: the
single cell `(6,10)`, `M = 2` — precisely `SHEET6-DEPTH.md` §6's `td = 6`
menu. My classification therefore reproduces the correct finiteness where the
record has it, and does not spuriously promote D9's pattern-level family to a
semilinear one. Its `nu = 1` branch reproduces `2*p*s' - l*p'*s = c'` and the
exact even-`l` log residue `(-1)^{n-1} binom(2n-2, n-1) != 0`.

### 6.3 An explicit infinite alive family (`td = 12`, `m = 3`)

The `td = 7` equal-join family (P3 class A) is `mu = 1`, so `M = gcd(1, ·) = 1`
at `lex = 0`, MP2-dead; its live members need `lex >= 1` (the `(6,10)` cell,
`C = 1`, bounded) or `nu_G = 1` (regime U2, the `(2,2t)` tail), and P4 prices
both out. So `td = 7` supplies no U1 witness. The **smallest witness the
printed arithmetic forces** is:

> **Entry (derived, not read from an engine).** `td = 12`, `m = 3`, all
> `b_i = 2`, global type `(2,3)`. Prop 5.7 gives `Lambda_i >= beta = 3` and
> MP4 forces `b = 1` at prime `Lambda`, so all-`b = 2` at `td = sum Lambda_i =
> 12` forces `Lambda_i = 4` for every `i`. Then `Lambda = a*b*alpha*beta/nu =
> 12a/nu = 4` gives `nu = 3a`, and L6 `gcd(a(alpha+beta), nu) = gcd(5a, 3a) =
> a = 1`. **Every pole is `(a,b,nu) = (1,2,3)` with
> `w_0 = a(b(alpha+beta) - 1)/(b*nu) = 9/6 = 3/2`.** MP1
> (`sum (r-1) = m - 1 = 2`) admits a single `r = 3` merge.

All three chains arrive **directly from their pole vertices** at `lambda = 0`
with `mu = 2` (`mu | b_i = 2`, St 8.4; P2's entry clause with `nu_i = 3`,
`gcd(nu_i, mu) = 1`), equal `w = 3/2`. MP6(b) equal-quotient holds with the
common `i = 2` (`deg p_{P_i} = b*alpha = 4 = i*mu`). The merge is the U1 family
`(r, mu, eps, w) = (3, 2, 0, 3/2)`:

    dp = 6*nu,  dq = 3*nu + 1,  E = 2,
    kbar = 3*(3*nu + 1)/2,  X = 9*nu,  M = 2,  w_tr = 9/2,  lambda_G = 0,
    admissible nu:  nu odd and nu !== 0 (mod 3)   [period 6, residues {1,5}]
                  = 5, 7, 11, 13, 17, 19, 23, 25, ...

(`B' = 2` from `kbar in Z`; MP2 gives `2 | 3nu+1`, i.e. `nu` odd; N1 gives
`gcd(nu, 3) = 1`; all three verified against the independent `merge_local`
engine and against a full-period periodicity check.) T1: alive, with the
rigidity `c_1^nu + c_2^nu + c_3^nu = 0` and `e_2(c_e^nu) = 0`.

**Budget.** The trunk starts at `(w, M) = (9/2, 2)`. There is provably **no**
`M`-preserving clean resonant step from `9/2`: resonance needs
`Delta | num(w) = 9`, `Delta = (n-1)nu + 1 >= 3`, while `M >= 2` needs `l = 2`
and `n, nu` both odd, forcing `(n-1)nu in {2, 8}` with `nu` odd — impossible.
One P0 dirty step suffices instead:

    l = 2, eps = 0, k = 1 (one non-chain orbit of multiplicity 1), lex = 0, nu = 25
    dp = 75, dq = 51, E = 2*51 - 75 = 27, kbar = 2*(9/2)*51/27 = 17, X = 25,
    NE 1*51 < 75 ok,  (S) 2*51 > 75 ok,  (R) ok,  N1 gcd(17,25) = 1 ok,
    w -> 2*(9/2)*2/27 = 2/3,  M -> gcd(75,51) = 3,
    lambda >= max(1, ceil(25/1 - 17)) = 8.

Terminal at `(2/3, 3)`: `j = M(1 - w) = 1 in N*`, `psi = ceil(3/1) - 1 = 2`,
budget `td - 1 - psi = 9`, and `Sigma lambda = 0 + 0 + 0 + 8 = 8 <= 9`, slack 1.

> **Result.** For **every** `nu_G` in the infinite progression
> `{nu odd, nu !== 0 mod 3, nu >= 5}` the `td = 12` `m = 3` `[2,2,2]`
> configuration is legal at the pattern tier, passes (S), (NE), (R), N1, MP2,
> St 8.4, R2.1/R2.2, the T1 tier (with the stated coefficient rigidity), and
> **fits the shared St 9.4 budget with slack 1**. This is charge 4's third
> option: an explicit infinite alive family, not a contradiction and not a
> finite exceptional-value theorem.

Honesty riders on this result, all inherited: R4 superset semantics — alive is
not existent, and no `(f,g)` is claimed; `lambda` values are P0 lower bounds,
so a single new printed unit anywhere on the route would eat the slack and
kill it; the trunk step's own Prop. 8.1(iv) solve at the *chain* tier is not
performed here (the §11 law is a merge-cell law); the entry derivation assumes
the global type is `(2,3)` — types `(2,5)`, `(3,4)`, `(3,5)` also admit
`[2,2,2]` at `td = 12` with `w_0 = 13/10`, `13/12`, `1` respectively, and each
yields its own U1 progression by Theorem C, so the conclusion is robust to the
type but the displayed numbers are not; `td = 12` is a composite panel that
`BOOK-OFFAXIS.md` §4 already records as open, so **no panel changes status** —
what changes is that the panel is now known to contain an exact infinite
semilinear family rather than an unenumerated haze.

### 6.4 If the source data are insufficient: the smallest missing row

The one thing I could not settle from the record is whether the `td = 12`
`[2,2,2]` entry's global type is `(2,3)`. That is a single row of
`cases/book_offaxis.py`'s entry census (`entries`/`tdu_rows` output for
`td = 12, m = 3`). **Fail-closed emitter specification for it:**

    INPUT   td, m, and the L6-surviving off-axis entry multisets
    OUTPUT  for each entry: (type (alpha,beta), per-pole (a,b,nu), Lambda_i,
            M_i = b_i, w_0i = a_i(b_i(alpha+beta)-1)/(b_i*nu_i)) as EXACT
            Fractions, plus gcd(a_i(alpha+beta), nu_i) = 1 asserted per row
    GATES   (G-a) sum Lambda_i == td, exactly;
            (G-b) every Lambda_i >= beta and MP4's "prime or beta-minimal
                  Lambda forces b = 1" asserted per row, not assumed;
            (G-c) the type is GLOBAL: assert one (alpha,beta) per entry;
            (G-d) refuse to emit any row whose w_0 is not an exact Fraction;
            (G-e) refuse any cap token; the enumeration bound must be the
                  derived Lambda >= beta / td = sum Lambda relation.
    FAIL-CLOSED  emit `ENTRY_ROW_UNKNOWN` (never a guess) for any (td,m) whose
            gates do not all pass, and make the consumer treat
            `ENTRY_ROW_UNKNOWN` as OPEN, not as absent.

Until that row is read, §6.3 stands as: *for whichever global type the
`[2,2,2]` entry carries, Theorem C produces an infinite progression, and for
type `(2,3)` the displayed route fits the budget.*

## 7. Charge 5 — reconciliation with the two sol56 theorems, and errata

**sol56's finite reduced P0-chain skeleton** (body
`8587625b...`) proves the reachable reduced **chain** states `(w, M)` are
finite at fixed `(td, entry, B)`. Theorems A–C' are compatible and
complementary: they say the reachable reduced **merge child** states are also
finite in regime U1 (`w_tr` constant, `M` periodic), so the U1 sector does not
break sol56's skeleton. They do **not** extend it to regime U2, where
`w_tr = mu*w*s/E` takes infinitely many distinct values as `lex -> infinity`
at `nu_G = 1`. **U2 is the one place where "finite reduced state" is currently
false at merges**, and sol56's theorem does not cover it because it is a chain
theorem. That is a precise, small, named gap, not a refutation.

**sol56's incoming-index bound** (body `8a16cad9...`) bounds `h = nu_H`, the
index of the vertex from which a case-III zero edge leaves. That is a different
quantity from the `nu_G` bounded by my prior Theorem 2.4, and **sol56's
correction is right**. I record the full repair:

* **E1 (quantifier).** My prior Theorem 2.4's `nu <= mu_0*num(w_0)` binds
  `nu_G` in `dp = eps + nu*P`, `dq = 1 + nu*s`. Its prose identified that `nu`
  with the incoming case-III index; that identification is **withdrawn**.
* **E2 (which invariant, and H5a-conditionality).** The `w_0` in that bound
  must be the *effective* zero-edge invariant `what_0`, not the arriving
  chain's `w`. Under the printed `SHEET6-DEPTH.md` §5c reading
  `what_0 = nu_H*w_H`, so the correct statement is
  `nu_G <= mu_0 * num(nu_H*w_H) <= mu_0 * nu_H * num(w_H)` — which is only
  effective *after* sol56's `nu_H` bound. Under the promoted E5/(I4) reading
  `what_0 = nu_G*w_U`, and the bound is **vacuous** (both sides carry `nu_G`);
  there `nu_G` is instead bounded — indeed pinned — by two-edge consistency
  (Theorem A(c)). So the prior Theorem 2.4 as printed is **not unconditional**;
  its conclusion is, by a different proof.
  Numerical check on the promoted `(9,15,7,3)@2` cell: `eps = mu_0 = 2`,
  `P = 1`, `s = 2`, `C_0 = 3 = |T| = M`, `E_0 = nu*C_0 = 21`,
  `what_0 = nu_G*w_U = 7/2`, `kbar = mu_0*what_0*dq/E_0 = 5`, and
  `E_0 = 21 <= M*mu_0*num(what_0) = 3*2*7 = 42` — Theorem 4a holds, and the
  derived `nu_G <= mu_0*num(what_0) = 14` is satisfied but circular under E5.
* The **algebra of the prior Theorems 1, 3 and 4 is preserved** and used here:
  Theorem 1 (`M | T`, `T != 0`) is sharpened to the exact `M = gcd(mu-eps, dq)`
  on U1; Theorem 4a (`E_e <= M*mu_e*num(what_e)`, via `gcd(E_e, dq) | M`) is
  used verbatim with the effective invariant and is what makes E2 quantitative;
  Theorem 3's zero-cost monovariants are untouched.

Further errata to my prior report, all self-reported:

* **E3.** §6a's T1 claim ("no member is T1-dead, since the §11 law kills iff
  `dp | dq`") **misapplied a shape-specific law**: `dp | dq` is proved only for
  the class-B/C shape (one nonzero orbit of multiplicity 1, `eps = mu_0`,
  `lex = l`). Theorem E is the correct replacement, and it gives a different
  kind of answer (rigidity, not divisibility).
* **E4.** Theorem 2.1's "`C_e = 0` for the binding edge" is replaced by the
  simultaneous condition of Theorem A; one edge is provably insufficient, and
  the packet exhibits unequal-`mu` data where the *slope* of the consistency
  residual vanishes while the constant does not (and vice versa).
* **E5.** §6a's member list included `(mu,w,nu) = (3,3,1)`; `nu = 1` is a
  Prop 9.3 case-I lattice meet with `kbar in Q`, an exceptional value outside
  the progression, and it belongs to regime U2.
* **E6.** §6a's `M_G = gcd(mu, 2nu+1)` is correct only at `eps = 0`; the
  general law is `M = gcd(mu - eps, r*nu + 1)`.
* **E7.** §6a conflated the `(2,2t)` `td = 7` tail with the equal-join family;
  they are the distinct regimes U2 and U1 of §3.
* **E8.** §10a's merge clause was made conditional on "an upper bound for
  `kbar`". Theorem F shows that bound is **not required** for the combinatorial
  ledger; the correct requirement is the labelled semilinear record plus the
  case-III consumer bound. §8's "First obstruction" should be re-typed
  accordingly: it is not a missing bound, it is a missing *record schema*, now
  supplied.

Grok's falsifier is confirmed on the two points it makes about this sector:
its Attack A (`(w,M)` and `(w,M,nu mod M)` are too coarse) is correct and is
answered by the labelled record, and its Attack E (the Avenue-1 colon
transplant is ill-typed here) is untouched by anything above. Its §6.1 table
row for the `(2,2t)` tail is exactly regime U2 and is here given a name and a
status.

## 8. Charge 6 — the packet

`cases/m2_equal_join_semilinear_opus5_20260829/` — exact `int`/`Fraction`/
symbolic arithmetic, stdlib only, no floats, no search caps, no engine import,
no network, no CAS. Cap tokens (`NUCAP`, `MAXNU`, `--cap`) are **refused** by
both executables. The T1 work is done with a self-contained exact sparse
multivariate polynomial class over `Q`, so the identities are verified
**symbolically in the unknown pattern coefficients**, not sampled.

```text
a23403a231f0418b0e036248baa6d3846933335a50b3fcc421bf8edb4d626779  polyexact.py
dd826f24ff179c34ca1af6f20fb53615de791a52271378380c654be4ee5f9482  t1_merge_reduction.py
6de8b7974de4a556d6347a36b9e777a4a559ea0e296064f509044e9aa1216ef9  eqjoin_semilinear.py
b72cf02aa897390287926bf7439575b93d14afe7337d488b05f748204fd4eb2e  controls.py
d5bddea6f9590fb2ffa9b4f930fb6965febb859b2ebf8bbfbbdfe041a9f1d475  emit_eqjoin.py
c3cb105ee9f57785d77bbcf191e9c346eb7a3312c98b2058dda771587263dc3e  trunk_probe.py
1f4e4260afce85dd06345c48704af77c74f2243db32e730e69066786ee95bf99  test_eqjoin_semilinear.py
a419002987f29cbd74d390b11aee1d68ff817aab6293c34ea53c0a484d81c09d  README.md
3914fd3c62bdecc59d250292bd98751054fa4a9ffc9b2e9dcae115745b734da6  charged emission (/tmp/eqjoin.json)
5a39a1b14d0820f37ef43e9f96984edc4517d326c6c02bfa13dbf77f07639824  trunk probe output (/tmp/trunk92.json)
```

Charged replay and observed output:

```sh
cd cases/m2_equal_join_semilinear_opus5_20260829
python3    emit_eqjoin.py --output /tmp/eqjoin.json
python3 -O emit_eqjoin.py --output /tmp/eqjoin-O.json && cmp /tmp/eqjoin.json /tmp/eqjoin-O.json
python3    test_eqjoin_semilinear.py
python3 -O test_eqjoin_semilinear.py
python3    trunk_probe.py --w 9/2 --M 2 --budget 10 --depth 3 --output /tmp/trunk92.json
```

```text
emit_sha256 3914fd3c62bdecc59d250292bd98751054fa4a9ffc9b2e9dcae115745b734da6
t1_identities 13
families 8
EQJOIN_EMIT_PASS
EQJOIN_SEMILINEAR_TEST_PASS checks=5810     (identical under -O; emission byte-identical)
one_step_menu 9
terminals_reached 9
states_seen 60 depth 3
  TERMINAL w=2/3 M=3 spent=8 psi=2 ['dirty(l=2,eps=0,k=1,lex=0,nu=25)->w=2/3,M=3']
```

Mutation tests that must and do **fail** when the mathematics is perturbed:
three wrong reduced T1 expressions (sign flip on `t*Rad_t*S`, dropped `nu`,
`mu <-> eps` swap); the wrong forced-zero set `{1..r}` instead of `{1..r-1}`;
the naive `M = gcd(mu, dq)` law once `eps >= 1`; the slope-only and
constant-only halves of the consistency residual; and the `td = 6` control's
ratio invariant. Guards proved live, not decorative: (S), (NE) on non-chain
orbits, (NE) on the free 0-root, (R), R2.1 cross-edge consistency, `r >= 2`.
Controls C1–C6 as listed in §6 and the README; C5 checks 24 416 unequal-`mu`
configurations with zero false families. `trunk_probe.py` re-derives the P0
menu rather than importing `book_offaxis`/`px5`, using the printed P0
finiteness relation `E | l*num(w)*T` as its stop rule; its BFS depth is a
*display* bound and the report does not claim BFS completeness — only the
single exhibited route, which is verified by hand in §6.3.

## 9. What is and is not claimed

**Proved at the recorded tier, no new hypothesis:** Theorem A (unbounded
classification, including case-III boundedness under both H5a readings),
Theorem B (closed forms for every free-0-root variant, incl. the exact
`M = gcd(mu-eps, r*nu+1)`), Theorem C (the admissible `nu` set is an explicit
finite union of APs; `nu_G = 1` the only exceptional value), Theorem C'
(downstream constancy/periodicity), Theorem D (T1-GEN, with the four printed
specializations), Theorem E (T1-EQJOIN: `Rad = t^r - A`, `C != 0` automatic,
uniform in `nu`), Theorem F (semilinear sufficiency for the combinatorial
ledger), Theorem G (no whole-family duplicates; one exhibited cell collision),
the `r`-even parity law and its `m = 2` consequence, and the reproduction of
OBSTRUCTION O's `2 +- sqrt(3)` from a general theorem.

**Exhibited, at superset tier:** the `td = 12`, `m = 3`, `[2,2,2]` infinite
budget-fitting family of §6.3, conditional on the entry's global type being
`(2,3)` and inheriting R4 (alive != existent) and the `lambda`-lower-bound
rider.

**Explicitly not claimed:** JC2; any landing, full-configuration cover, type
ceiling, `G2-BD`, `RPMC(C)`, cofinal `td` bound, or Keller consequence; any
realizability of any state or cell by an absolute `(f,g)`; any change of status
for any `(m, td)` panel; any adjudication of CONJECTURE H5a, of `U_7C`, or of
the P-value reading; any statement about `jc2-lean`, which was not accessed;
completeness of the `trunk_probe.py` BFS.

**Corrections offered to the record.** `BOOK-OFFAXIS.md` §7 R2.2(D)'s
subadditivity rider is discharged on the equal-arrival sector by the exact law
`M = gcd(mu - eps, r*nu + 1)`; §9's survivor-anatomy type (i) ("equal-`mu`
equal-`w` joins, `kbar` underdetermined at stage R") should be re-typed as the
U1 semilinear family with a labelled record rather than as an undetermined
cell; §10 P3's class-A `(2,2t)` tail should be re-typed as regime U2
(`nu_G = 1`, unbounded `lex`, non-constant `w_tr`), which is a *different*
finiteness failure from U1 and is currently closed only at `td = 7` and only by
budget; and the §11 `dp | dq` T1 law should carry an explicit scope note that
it is the class-B/C specialization of (T1-GEN) and must not be applied to
equal-arrival shapes.

## 10. Ranked next action, and the verdict

1. **(highest leverage, desk-scale, ~1 day) Close or characterize regime U2.**
   It is the only place where the reduced state set is *provably* infinite, and
   it sits at `nu_G = 1` where `kbar in Q` removes the integrality lever. The
   exact question: at a Prop 9.3 case-I merge with `r >= 2` equal-`(mu,w)`
   arrivals and free `lex`, is `w_tr = mu*w*(r+lex)/((mu-eps) + mu*lex - Sm)`
   ever compatible with a legal terminal for infinitely many `lex`, given
   MP2 and the P1 `j = M(1-w_t) in N*` law? A negative answer makes the merge
   reduced-state set finite and completes sol56's skeleton to a merge theorem;
   a positive answer is a second, sharper counterfamily.
2. **(next, cheap) Read the one missing entry row** (§6.4) and re-run §6.3 with
   the true global type. This either confirms the displayed `td = 12` witness
   or replaces its numbers, without touching any theorem.
3. **(next) Promote the labelled family record into the ledger schema** of
   `REDUCTION.md` §5.1's object (3)/(4), with Theorem G's equality/hash rules
   and the `consumes_full_nu` flag, and make the case-III consumer call
   sol56's `nu_H` theorem. This is the concrete form of the CRITICAL 5 repair
   for the U1 sector.
4. **(after 1–3) The coefficient/gluing tier on the U1 rigidity.** Theorem E
   reduces the U1 coefficient question to: can `r` arriving chains, each with
   its own pole and Puiseux data, have `c_e^{nu}` equal to the `r` distinct
   `r`-th roots of one number? That is a sharply posed question about deck and
   monodromy data, and it is the first place a U1 kill could come from.
5. **(do not do)** Do not seek a numerical `kbar` bound at equal-`(mu,w)`
   joins. Theorem F says the ledger does not need one, and Theorem A says one
   cannot exist: the family is genuinely infinite.

**Verdict.** Not a theorem that closes the sector, and not a uniform
contradiction. Three things are proved (Theorems A–G: the quantifier repair,
the complete closed-form calculus and AP structure, the general merge T1
reduction with its rigidity consequence, and the semilinear-sufficiency of the
ledger), and one thing is **found**: an explicit infinite family of
budget-fitting, `lambda`-cheap, T1-alive equal-arrival merge configurations at
`td = 12`, which is a counterfamily to any reading of the off-axis endpoint as
a finite set of cells and is exactly consistent with reading it as a finite set
of labelled semilinear families. The named exact gap that remains is
**regime U2** — the `nu_G = 1`, unbounded-`lex` case-I tail, where the reduced
child state `w_tr` is provably not finite and no printed statement closes it
beyond `td = 7`.

---

*Report body ends. The seal below covers everything above this line.*

report_body_sha256 = bacf0d6ba789655ebbfd0b9da7018b8e10303fab149b38ef052587fadc5278d2
(sha256 of the first 43954 bytes of this file, i.e. up to and including the line
"*Report body ends...*")
