# Hostile review — Sigray Proposition 5.4 `q`-half repair

Reviewer model: **Claude Opus 5** (`claude-opus-5`), independent adversarial referee.
Date: 2026-08-28.  Target: `xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md`.

## Verdict

**REPAIR**

Theorem 5.1 (the two-pattern `q`-half) is **true**, and the producer's own new
mathematics — Sections 3 (projectors/transport) and 4 (Lemma 4.1) — is correct
as written; I could not break it.  Section 6.2's `alpha=1` emptiness argument is
also correct.  But the producer's Section 2 typing imports Proposition 5.3(iv)
as a settled input, and the printed proof of 5.3(iv) (p. 25) is **incomplete at
exactly one branch**: with `alpha>=2` a linear `p_F` does *not* force `alpha=1`;
it forces `deg p_{g,F}=0`, which is the degenerate branch that Proposition
4.6(17) explicitly leaves open at `mu_F=0`.  Since (1.2) rests entirely on
5.3(iv), the producer's claim "No extra geometric or later-section premise is
needed" (§1) is false as stated.  The hole is closable inside the printed
apparatus; replacement text is in §10 (Lemma A).  Three further textual repairs
(§10.2–§10.4) and one ledger-phrase replacement (§5.3) are required.  Producer
errors are separated from pre-existing source errors in §11.

## 0. What was run

| artifact | result |
|---|---|
| `verify_qhalf.py` (frozen) | **PASS**, 1788 grouped assertions (28/8/112/1441/128/64/7), 2.6 s |
| checker-primitive audit (mine, `/tmp/qhalf/audit_checker.py`) | 31/31 pass, incl. both-direction controls the checker never runs |
| mutation battery on the frozen checker (mine) | **7/7 caught** — checker is not tautological |
| independent control suite (mine, `/tmp/qhalf/indep.py`) | **PASS**, 1014 assertions, dict-polys + own elimination, own fixtures |

No repo file was edited except this report.  `jc2-lean` untouched.

## 1. Proposition 5.3(iii) from Proposition 4.6(11) at `m_F=0` (charge 1)

**The right side is a nonzero constant — and needs no derivation.**  The blank
glyph in the print is defined by **Notation 1.1, p. 4**: "We use the symbol ⋅
for a non-determined constant in **C\***".  So 5.3(iii) (p. 25) *literally reads*
`k_f p_F p'_{g,F} - k_g p'_F p_{g,F} = C`, `C in C*`.  The producer's route via
4.6(11) is a corroboration, not a necessity, and it costs more than it earns:

- 4.6(11)'s exponent is `mu_F`, not `m_F`.  `mu_F=0` when `m_F=0` is **Prop
  4.2(iv), p. 19** ("`mu := mu_F = 0` if `m = 0`"; same in 4.3(iv), p. 21).  The
  producer's "`m_F=0`, so ... right side `C*p^0`" silently uses this; cite it.
- 4.6 sets **`k = d_F`, `l = d_{h,F,b}`** (p. 23), *not* `k_f,k_g`.  Converting
  (11) into 5.3(iii) therefore needs `d_{g,F}/d_F = k_g/k_f` — i.e. the
  **corrected** 5.3(ii).  So §2's boast that the proof "does not use the
  inverted ratio printed in Proposition 5.3(ii)/(viii)" is only true if 5.3(iii)
  is taken *as printed*.  Both readings are fine; the report must pick one.
  I confirm the inversion independently: Prop 5.3(ii)'s own proof gives
  `(g_G^+)^k=(f_G^+)^l`, `k/l=k_f/k_g`, hence `k d_{g,G}=l d_G`, hence
  `d_{g,G}=(k_g/k_f)d_G=(beta/alpha)d_G`.  **Prop 4.6(16), p. 23** prints
  `deg p/deg q = d_F/d_{h,F}` — the correct direction — which is a second,
  previously unrecorded internal corroboration of the 5.3(ii)/(vii) inversion.
- `d_F>0` (needed to divide (11) by `k=d_F`) holds: 5.3(ii) gives `d_{g,F}>0`,
  St 5.1 (p. 24) gives `d_F>0` iff `d_{g,F}>0`.  Producer omits this; harmless.

**Suppressed scalar is harmless** ✓ — only `c != 0` and its deck character `0`
are used.  **`(k_f,k_g)=s(alpha,beta)` is licensed** ✓ — Notation 2.4(i), p. 9
*defines* `alpha/beta = k_f/k_g` with `gcd(alpha,beta)=1`, so `alpha | k_f`,
`s=k_f/alpha=k_g/beta in N*`.  This is a definition, not the inverted 5.3(ii).
`alpha>=2` ✓ — St 2.1, p. 9 (`alpha != 1`), forced by Lem 2.1(iv) `k_g/k_f
not in N*` plus `gcd=1`.

## 2. The `p = eta^eps P(eta^nu)` chain — and the one real hole (charge 2)

Correct in the producer: **axes** (5.3(i), p. 25, excludes `(0,x),(0,y)`, so
St 3.16's first half applies); **canonical exponent** (write `p=eta^l p~(eta^nu)`
with `p~(0)!=0`; then `l = ord_0(p)`) ✓; **squarefreeness** (5.3(v) forces
`ord_0(p)<=1`, hence `eps in {0,1}` and `P(0)!=0`) ✓; **character** ✓
(`p(zeta*eta)=zeta^eps p(eta)`); **`nu != 1` means `nu >= 2`** ✓.  Also correct:
5.3(v) makes **both** `p` and `q` squarefree, and 5.3(iii) itself yields
(v)/(vi) by evaluation at a root — I re-derived all three.

**The hole.**  Prop 5.3(iv)'s printed proof (p. 25) is:

> "By Statement 3.16, we have to prove, that `p_F` has more than one root.
> Otherwise, by (iii), `p_F` would be linear, and `k_g/k_f in N`, contradicting
> Statement 2.1."

The step `p_F` linear ⟹ `k_g/k_f in N` runs through `deg p/deg q = alpha/beta`
and needs `deg q >= 1`.  It fails at `deg q = 0`, and that branch is *live*:
with `p = A(eta-a)`, `q = b in C*`, the bracket is `-beta A b in C*` **for every
`(alpha,beta)`** — verified exactly (control C9, four types).  Worse, this is
not an artefact: **Prop 4.6(17) at `mu_F=0`** is precisely `deg p + deg q - 1 =
0`, i.e. `(deg p, deg q) = (1,0)` (`deg p >= 1` since `F` is a child, St 3.9(i)
+ St 3.18), and 4.6 explicitly says that in that branch (16) — the degree ratio
— "is not true".  Conversely, with `alpha>=2` a linear `p` *forces* `deg q = 0`
(`alpha d = beta` is unsolvable), so the printed contradiction is never reached.
The only printed exclusion of `deg q = 0` is 5.3(vii), which `SIGRAY-AUDIT.md:66`
already records as "never actually derived in print".

So the producer's §2 bullet — "its proof uses Statement 2.1 when it excludes a
linear `p`" — describes the printed text accurately but treats an unfinished
argument as an input.  **Lemma A (§10.1) closes it** in four lines from Prop
5.1(ii) + Prop 4.2(iii) + St 3.9(i), and yields the printed conclusion verbatim
(`deg p_F = 1 ⟹ alpha = 1 ⟹ k_g/k_f in N*`, contra St 2.1).  Lemma A is a
bonus elsewhere: it proves St 5.2(i)'s degree half `deg p_F/deg p_{g,F} =
alpha/beta` **without** 5.3(ii)/(vii), and supplies Prop 5.7's unproved
"`nu_F < deg(p_F)`" step (`deg p_F >= alpha >= 2` and `deg p_F ≡ 1 mod nu`
give `deg p_F >= nu+1`).

**Does the chain already consume `alpha>=2`?**  Yes, twice, and the producer's
§6.1 is right about it: once inside 5.3(iv) (as repaired: `alpha | deg p_F`
with `deg p_F >= 1` gives `deg p_F >= alpha >= 2`), and again in Lemma 4.1.
These are two uses of one gate, not circularity.

## 3. Projectors and the differentiation law (charge 3)

Recomputed and **confirmed**.  `q_r = (1/nu) sum_j zeta^{-rj} q(zeta^j eta)` is
the isotypic projector; `q = sum_r q_r`; `q_r(zeta eta)=zeta^r q_r(eta)`.
Differentiating that identity gives `zeta q_r'(zeta eta) = zeta^r q_r'(eta)`, so
`q_r'` has character `r-1` — sign correct.  With `p` of character `eps`, both
`alpha p q_r'` and `beta p' q_r` have character `eps+r-1`, so `L(q_r)` lies in
`V_{eps+r-1}`.  `r |-> eps+r-1` is a bijection of `Z/nu`, the right side `c` has
character `0`, and `C[eta] = ⊕_r V_r` is a direct sum (`nu` invertible in `C`),
so `L(q_{1-eps})=c` and `L(q_r)=0` otherwise — **exactly `r = 1-eps`**.
`nu=2` is included with no special case (`eps=0 -> r=1`, `eps=1 -> r=0`).
**Zero components are harmless**: `0 in V_s` for every `s`, and the checker
correctly skips them (`if not is_zero(got)`).  432 independent transport checks
at `nu in {2,3,4,6}`, `eps in {0,1}`, three types, all degrees `j <= 4nu+2`:
`res(L(eta^j)) = {(eps+j-1) mod nu}` with no exception (control C8).

## 4. The local kernel (charge 4)

**Lemma 4.1 is correct.**  I re-derived the local expansion: with `t=eta-a`,
`p=At+O(t^2)` (`A=p'(a)!=0` by squarefreeness), `R=Bt^m+O(t^{m+1})`, the
`t^m`-coefficient of `alpha p R' - beta p' R` is exactly `AB(alpha m - beta)`
— `p` has no constant term, so `pR'` starts at `t^m`, and `p'R` starts at `t^m`;
no `O(t^{m+1})` term contaminates it.  Initial evaluation `R(a)=0` is forced
because `alpha p(a)R'(a) = 0` and `beta p'(a) != 0`.  `alpha m = beta` with
`gcd=1` forces `alpha=1`.

Exception hunt, all negative:

- **constant `R`**: then `R(a)=0` gives `R=0`; equivalently `-beta p' R = 0`
  needs `p` constant, excluded.
- **rootless `p`**: impossible over `C` for nonconstant `p`.  (Over `R` the
  local step fails but the statement is about `C[eta]`, and `p_{g,F}, p_F` are
  genuinely complex polynomials, Not 3.10 p. 13.)
- **Laurent/rational**: the general solution is `C p^{beta/alpha}`, polynomial
  iff `alpha | beta`, excluded by `gcd=1, alpha>=2`.  The theorem claims only
  polynomial `R`, and `p_{g,F}` *is* a polynomial — no scope creep.
- **characteristic**: `alpha m - beta` can vanish only in char `p | (alpha m -
  beta)`; irrelevant over `C`, and the producer states `C`.
- **`p` not squarefree**: genuinely load-bearing — `L(2,3,eta^2,eta^3)=0`
  (control C4 sharpness).  Supplied by 5.3(v).
- **`alpha | beta`**: `L(2,4,p,p^2)=0`, `L(1,3,p,p^3)=0` (control C5).

60 randomized exact null-space computations (`nu in {2,3,4,5,7}`, 1–3 deck
factors, nine coprime types with `alpha>=2`, windows `floor(beta n/alpha)+4`):
kernel dimension **0** every time.

## 5. `alpha = 1` (charge 5)

### 5.1 The mixer is exact

`(nu,alpha,beta,p,q)=(3,1,2,eta,1+eta^2)`: bracket `1*eta*2eta - 2*1*(1+eta^2)
= -2` ✓ nonzero constant; `p` squarefree ✓; `q=(eta-i)(eta+i)` squarefree ✓;
`gcd(p,q)=1` (`q(0)=1`) ✓; `deg p/deg q = 1/2 = alpha/beta` ✓; `p` has character
`1 mod 3` while `q` mixes `{0,2}` ✓ — so (5.2) fails.  Structurally the wrong
piece is *the kernel element*: `eta^2 = p^beta`, and `L(1,2,eta,eta^2)=0`
(control C7).  The producer's §6.1 is exactly right.

### 5.2 No mixer survives `deg p >= 2` — §6.2 confirmed and strengthened

The producer's argument is sound; I simplified it and it needs neither
squarefreeness nor a kernel classification.  For `alpha=1`, `deg p = n`,
`deg q = m`, the leading coefficient of `L(q)` is `(m-beta n)·lead(p)lead(q)` at
degree `n+m-1`.  If `m != beta n`, `deg L(q) = n+m-1 >= n-1 >= 1`, never a
nonzero constant.  If `m = beta n`, subtract `lambda p^beta` (`L(p^beta)=0`
identically); the remainder `S != 0` has `deg S < beta n` and still solves
`L(S)=c`, contradiction by the first case.  Both cases need only `n >= 2`.
Verified on 129 configurations, with windows `beta n + 3` (wider than the
checker's `beta n + 1`), including three **non-deck** squarefree `p` — the
checker only tests deck-shaped `p` here (control C6).

The `n=1` boundary is sharp and I classified it completely: for
`p = A(eta-a)`, the full solution set of `pq'-beta p'q = c` is
`q = -c/(beta A) + lambda p^beta`, `lambda in C` — a genuine 1-parameter family,
mixing characters exactly when `nu ∤ beta` (54 members verified, control C7).

### 5.3 Required replacement of the audit phrase

`ladder/SIGRAY-AUDIT.md:67`'s "**for α = 1 genuine counterexample solutions
exist**" **needs qualification; as an unqualified statement about Proposition
5.4's hypothesis set it is false.**  Replacement text:

> load-bears on α ≥ 2 (St 2.1).  Deleting α ≥ 2 from the *abstract* lemma
> (constant bracket, squarefree p, gcd(p,q)=1, deg p/deg q = α/β) admits
> character-mixing solutions **iff deg p = 1**, where the complete solution set
> is q = −c/(β·lead p) + λ·p^β (witness (ν,α,β,p,q) = (3,1,2,η,1+η²)).  For
> deg p ≥ 2 the α = 1 system has **no** polynomial solution at all, so the
> ablated hypothesis set is empty, not counterexample-rich; and deg p = 1 is
> excluded at every pole vertex (Prop 5.3(iv), completed by the deg-pin lemma).

## 6. The `kappa` / Statement 3.9 rider (charge 6)

The producer's §7 conclusion is right but its first bullet is imprecise.

- **The `q`-half proper is St-3.9-free** ✓: producer §§3–5 use only `C[eta]`,
  `eta -> zeta eta`, and the bracket.  No parent/`F*c` comparison, no derived
  `h_j`, no `kappa`.  Statement 3.9's `h`-dependent `kappa` defect
  (`SIGRAY-AUDIT.md:44`) cannot reach them.
- **But the typing in §2 is not St-3.9-free.**  Prop 5.3's printed proof already
  invokes St 3.9 ("By Statement 3.9, `deg(p_G) > 0`", p. 25), and Lemma A
  (§10.1) invokes St 3.9(i) twice.  In both places the auxiliary polynomial is
  an **original** one (`f-a` and `g`), never a derived `h_j`.  So the producer's
  own prescription — one `K` divisible by a fibre-suitable denominator, the
  denominator of `pi(F)`, and the Prop 3.1 pole orders of `{f-a, g}` (or their
  squarefree factors) — **is sufficient here**, and it is a genuine finite lcm.
  Enlarging `kappa` is safe: `d_{h,F}, p_{h,F}, h_F^+` are invariant under
  change of suitable `kappa` (Not 3.10 rider), and `kappa u in N` survives
  passage to multiples.  Replace "They never invoke Statement 3.9" with "The
  argument of §§3–5 never invokes Statement 3.9; its inputs do, but only for
  `h in {f-a, g}`."
- **No silent tower repair** ✓.  The producer explicitly refuses to license
  omitting the rider for downstream `h_j` families.  I endorse that and add
  nothing: this report repairs no tower consumer.

## 7. Statement 5.2(ii) and the promoted consumers (charge 7)

**Menu re-derivation, every gcd step checked.**  From (5.1): `nu | deg p` and
`deg q ≡ 1 (nu)`.  From (5.2): `deg q ≡ 0 (nu)` and `deg p ≡ 1 (nu)`.  Degree
ratio `beta·deg p = alpha·deg q` (from 5.3(iii)'s leading-coefficient
cancellation, valid because `deg p + deg q - 1 >= 1` once `deg p >= 2`; also
Lemma A directly).  Case (5.1): `nu | deg p ⟹ nu | beta·deg p = alpha·deg q`;
`deg q ≡ 1 (nu)` ⟹ `gcd(nu, deg q) = 1` ⟹ `nu | alpha` ✓.  Case (5.2)
symmetrically `nu | beta` ✓.  This is producer (8.2) and printed St 5.2(ii).

**Promoted direct consumers.**  Four, not two:

| consumer | what it uses | supplied? |
|---|---|---|
| `SHEET6-TDUNIFORM.md:47` **(R2)** | `(A) nu\|alpha & nu\|Pg-1` or `(B) nu\|beta & nu\|P-1`; then `nu<=beta`, `gcd(nu,b)=1` | **yes, exactly** (the derived gcds follow from `nu \| b·(other)-1`) |
| `SHEET6-AF3.md:142-146` parity pin | `(e,e_g)=(1,0)` at `(alpha,beta,nu)=(3,5,5)`, `p=eta(eta^5-A)`, `p_g=B(eta^10-(5/3)Aeta^5+(5/9)A^2)` | **yes** — I recomputed the pair from scratch (solve, don't trust): unique solution in a degree-14 window, character `0 mod 5`, bracket `(25/9)A^3B` ✓ |
| `SHEET6-MULTIPOLE.md:87` β-minimal / prime-Λ | `nu\|alpha` or `nu\|beta` + Prop 5.6(19) + 5.7 + St 2.1 | **yes** (arithmetic re-checked line by line) |
| Prop 5.7, p. 27 (source) | St 5.2(ii) menu, plus `nu_F < deg(p_F)` | menu **yes**; `nu_F < deg p_F` needs `deg p_F >= 2`, i.e. **Lemma A** |

**Another unproved assertion does remain in the surrounding stack, but it is not
the `q`-half**: Prop 5.8 (20) is still `GAP` (`SIGRAY-AUDIT.md:73`), and
TDUNIFORM (R3), MULTIPOLE and LROOT all consume it.  Nothing here changes that.

**Pre-existing source erratum found, not previously on the St 5.2 row.**
St 5.2(i) prints `deg(p_F)/deg(p_{g,F}) = D_{g,F}/D_F = alpha/beta`.  The middle
term is **inverted**: `D_{g,F}/D_F = d_{g,F}/d_F = beta/alpha`; the correct term
is `D_F/D_{g,F}`.  The campaign already computes with the corrected direction
(`TDUNIFORM:45` "D/Dg = P/Pg = alpha/beta"; `SHEET6-PILOT.md:40`
"`D_F/D_g,F = α/β`").  This is the same inversion family as the filed 5.3(ii)/
(viii) erratum, and the `St 5.2 | VERIFIED_WITH_NIT` row should name it.
It does **not** affect the producer: §8 uses only the degree half, which is
correct as printed.

## 8. Separation / firewalls (charge 8)

- **Prop 4.2 constant-shift repair.**  Producer §8 bullet 2 ("the repaired
  Proposition 4.2 recursion and its constant-corner terminal never enter") is
  **too strong once the 5.3(iv) hole is patched**: Lemma A uses Prop 4.2(iii)
  at `j=0` at the parent `G` (where `m_G > 0`) and needs `l_0 in N*`, i.e. no
  constant corner on the pole spine.  That is supplied twice — by Prop 4.2's own
  printed proof ("since `h_j` is a non-constant polynomial, `s_j != 0` and
  `l_j != 0`"), and by the promoted repair's clause that a corner lies in
  `T_a^↗`, never on a pole characteristic path.  The dependency is real and must
  be recorded; it is **not** a use of the terminal-corner degree formula.
- **Prop 5.1 finite-puncture repair.**  Correctly firewalled ✓: `T_{a,pole}`
  members are genuine `g`-poles where `b_P = 0`, so the printed 5.1(i)–(iii)
  hold verbatim.  Lemma A uses 5.1(ii) only at a pole, inside the repair's
  validated régime.
- **Prop 5.8, decorated-tree propagation, landing, JC2.**  Untouched ✓.  Nothing
  here bounds topological degree, proves (20), realizes a multiplicity datum,
  or advances JC2.  The producer's scope paragraph is accurate.
- **Prop 5.3(ii)/(viii) inverted ratio.**  Correctly quarantined ✓ — but see §1:
  the 4.6(11) route does use the corrected ratio, so the "no ratio used" claim
  must be attached to the *as-printed* reading of 5.3(iii).

## 9. Checker audit (charge 9)

**Orientation** ✓: `operator_matrix` columns are `L(eta^j)`, rows are
coefficient indices; `nrows = max(len(col))` covers every column;
`rref_rank(rows) == cap+1` is full **column** rank = injectivity on the window.
**Augmented-rank consistency** ✓: `rhs_consistent` compares `rank(A)` with
`rank([A|b])` on equal-length rows; `rhs = [1,0,...]` is the constant polynomial
`1`, correct for the row convention.  **Cap sufficiency** ✓: the unique degree
at which the leading term can cancel is `m = beta n/alpha`; both caps
(`floor(beta n/alpha)+3`, `beta n + 1`) strictly contain it.  **squarefree /
gcd_poly** ✓: Euclid over `Fraction` with exact leading-coefficient
cancellation; `divmod_poly` indices are in range; constants are (correctly)
squarefree.  **Positive fixtures** ✓: all four recomputed with independent
arithmetic — brackets are exactly `1`, characters `eps` and `(1-eps) mod nu`,
degree ratios `beta·deg p = alpha·deg q`, both alternatives represented.

**One-sided predicates — checked in the direction the checker never runs.**
`constant_nonzero` is only ever asserted *False*, `squarefree` only *True*, and
`rhs_consistent` only *False*.  A vacuously-constant implementation of any of
the three would leave `PASS` intact.  I ran the missing controls:
`constant_nonzero(1)=True`, `squarefree(eta^2)=False`, `squarefree((eta-1)^2)=
False`, `rhs_consistent` True on a solvable system, and — the sharp one —
`rhs_consistent` **True** for `(alpha,beta,p)=(1,2,eta)`, the mixer regime.  All
behave correctly; **not defects, but the controls should be added.**

**Mutation battery (mine), 7/7 caught**: perturb a fixture by a *right*-character
`eta^3`; swap `(alpha,beta)`; flip the bracket sign; off-by-one `deriv`; shift
`residues` by `+1`; force `alpha=1` into the `alpha>=2` grid; drop the
`eta^eps` prefactor in `pattern_p`.  The checker is not tautological.

**Genuine coverage gaps (no `PASS` retraction):**

1. **Every positive fixture has a single deck orbit** — `p = eta^eps(eta^nu-a)`.
   Restricted to the two live character classes, `#slots - #unknowns` for
   `L(q) = c` equals exactly **`(#deck orbits of p) - 1`** (`= (deg p - eps)/nu
   - 1`; verified over `nu in {2,3,4,5}`, `eps in {0,1}`, 1–3 orbits).  So
   single-orbit `p` is the *square*, always-solvable case, while `>= 2` orbits
   is a genuine codimension condition on `p`.  The checker therefore never
   exhibits a solvable pair whose `p` carries two `nu`-orbits.
2. Mutations add only the *lowest* wrong-character monomial.
3. No end-to-end control: "solve `L(q)=c` on a window, then check the unique
   solution has the predicted character".

**My independent nonconstant control (hand-derived, not a copy of any fixture).**
Take `(nu,eps,alpha,beta) = (2,0,4,5)` and `p = eta^4 + A eta^2 + B`,
`q = c_1 eta + c_3 eta^3 + c_5 eta^5`.  By hand, `4pq' - 5p'q` has zero
`eta^8` coefficient automatically, and the remaining conditions are
`c_3 = (5A/4)c_5`, `c_1 = (5A^2+40B)c_5/32`, `A c_1 = 2B c_3`, whose resultant
is **`B = A^2/8`**.  Normalizing `c_5 = 1`:

> `p = eta^4 + A eta^2 + A^2/8`,  `q = eta^5 + (5A/4) eta^3 + (5A^2/16) eta`,
> `4 p q' - 5 p' q = 5A^4/32`.

At `A = 8`: `p = eta^4+8eta^2+8`, `q = eta^5+10eta^3+20eta`, bracket `640`.
Here `p` has **two distinct nonzero deck orbits** (`disc = A^2/2 != 0`,
`B != 0`), `p,q` are squarefree and coprime, `5 deg p = 4 deg q`, `alpha=4>=2`,
`gcd(4,5)=1`, menu case (A) `nu|alpha`, `nu|deg q - 1`; and solving the
inhomogeneous system over a degree-14 window returns this `q` **uniquely**
(nullity 0) with residues exactly `{1} = {1-eps}`.  Verified for five values of
`A` (including `1/2` and `7/5`).  This closes gaps 1 and 3 above, and confirms
the theorem is not an artefact of single-orbit `p`.  I also rebuilt AF3's
`(3,5,nu=5)` pair by solving rather than checking, and it reproduces AF3's
printed closed form and its `(25/9)A^3B` bracket exactly.

Incidental finding: `p = eta(eta^2-1)(eta^2-4)` at `(nu,alpha,beta)=(2,5,6)`
satisfies the entire divisibility menu yet admits **no** `q` — by the count
above, solvability is a codimension-`(#orbits - 1)` condition on `p` *beyond*
the menu.  Worth knowing before any realizability claim is read off St 5.2(ii):
the menu is necessary, never sufficient.

## 10. Replacement text

### 10.1 New lemma to insert before producer §2's `F in V_a` bullet

> **Lemma A (degree pin at a pole vertex).**  Let `F = I_P(u) in T_{a,pole}`.
> By 5.3(i) and Not 3.2, `F != I_P(0)`, so `u > 0`.  Choose `kappa in N*`
> suitable with `kappa u in N` and with the Proposition 3.1 property for both
> `f-a` and `g`, and set `G := I_P(u - 1/kappa)`, so that `F = G * c` for the
> unique `c` of Prop 3.2; by St 3.18, `c` is a root of `p_G`.
> (i) By St 3.9(i) applied to `h = f-a` and to `h = g`:
> `deg p_F = mult(p_G, c) >= 1` and `deg p_{g,F} = mult(p_{g,G}, c)`.
> (ii) `0 <= u - 1/kappa < u`, so `m_G > 0` by Prop 5.1(ii); hence Prop 4.2
> (`h_0 = g`) at `j = 0` gives `(g_G^+)^{k_0} = s_0 (f_G^+)^{l_0}` with
> `gcd(k_0,l_0)=1`, `s_0 != 0`, `l_0 in N*` (Prop 4.2's proof; equivalently the
> promoted 4.2 repair, which puts every constant corner in `T_a^↗`, never on a
> pole characteristic path).  By Prop 4.4 and Not 2.4, `(k_0,l_0) = (alpha,
> beta)`.  Comparing `eta`-parts, `p_{g,G}^alpha = s_0 p_G^beta`, so
> `alpha·mult(p_{g,G},c) = beta·mult(p_G,c)` for every `c`.
> (iii) Therefore `alpha·deg p_{g,F} = beta·deg p_F`.  With `gcd(alpha,beta)=1`
> this gives `alpha | deg p_F`, hence `deg p_F >= alpha >= 2` and
> `deg p_{g,F} = (beta/alpha) deg p_F >= beta >= 3`.  ∎
>
> Lemma A completes the printed proof of Prop 5.3(iv): `deg p_F = 1` would give
> `alpha = 1`, i.e. `k_g/k_f = beta in N*`, contradicting St 2.1 — which is
> exactly the printed inference, now with its missing support.  It also proves
> St 5.2(i)'s degree half without 5.3(ii)/(vii), and supplies Prop 5.7's
> unproved `nu_F < deg(p_F)`.

### 10.2 Producer §1, last paragraph

Replace "No extra geometric or later-section premise is needed." with:
"Beyond Proposition 5.3(iii),(iv),(v) and Statement 3.16, the only extra input
is Lemma A, which completes the printed proof of 5.3(iv) at its one open
branch `deg p_{g,F} = 0`.  No later-section premise is needed."

### 10.3 Producer §2, fourth bullet

Replace with: "The right side of Proposition 5.3(iii) is the symbol of Notation
1.1 (p. 4), i.e. a non-determined constant in `C*`; nothing needs to be derived.
As a consistency check, at a pole vertex `m_F = 0`, so `mu_F = 0` by Prop
4.2(iv), and 4.6(11) reads `d_F p q' - d_{g,F} p' q = C`; converting that into
the `(k_f,k_g)`-normalization of 5.3(iii) requires the *corrected* 5.3(ii)
`d_{g,F} = (k_g/k_f) d_F`, which 4.6(16) independently corroborates.  The proof
below uses 5.3(iii) as printed and therefore needs neither direction."

### 10.4 Producer §7 bullet 1 and §8 bullet 2

§7: "…the argument of Sections 3–5 never invokes Statement 3.9; its inputs do
(Prop 5.3's printed proof, and Lemma A), but only for `h in {f-a, g}`, so the
single common lcm below suffices."
§8: "…Proposition 5.3(iii) is used only at `m_F = 0`; Lemma A additionally uses
Proposition 4.2(iii) at the parent vertex, where `l_0 in N*`, so the repaired
recursion's terminal constant corner never enters."

## 11. Producer errors vs pre-existing source errors

**Producer (must fix):** §1 "no extra premise" overclaim (§10.2); §2's
4.6(11)/`m_F` bullet, which both skips the `mu_F=0` citation and is in tension
with the "no inverted ratio" claim (§10.3); §7/§8 scope sentences (§10.4);
inheriting 5.3(iv) without noting or closing its `deg q = 0` branch (§10.1).
Everything the producer *proves* — (1.2)→(1.4), §3, Lemma 4.1, Theorem 5.1,
§6.1, §6.2, the (8.1)/(8.2) menu — is correct.

**Pre-existing source (already filed or newly found):** Prop 5.3(iv)'s printed
proof is incomplete at `deg p_{g,F} = 0` — **new**, adjacent to the filed "(vii)
never actually derived" nit on `SIGRAY-AUDIT.md:66`; St 5.2(i)'s middle term
`D_{g,F}/D_F` is inverted — **new** on the St 5.2 row, same family as the filed
5.3(ii)/(viii) erratum; Prop 4.6(16) is a second internal corroboration of that
inversion — **new**; Prop 4.6's "Set `F = T_a^+ ∪ T_a^-`" misprints `∈`
(already filed).

## 12. Hashes

**All four frozen input hashes still match**, re-verified at the end of review:

```text
f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75  xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md      MATCH
4c6164b9cf01a797ca6d1029e038f44d7e9f32b34e405c38ec53b2c2f2256bea  cases/sigray_prop54_qhalf_20260828/verify_qhalf.py    MATCH
21cd5407791da8a8426d2792548b177183fae73d732e4ff11c33657360f7430f  cases/sigray_prop54_qhalf_20260828/CUSTODY.md         MATCH
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf                                 MATCH
```

SHA256 of this report.  A file cannot contain its own digest, so the seal is
taken over the report body, defined as this file with its final line removed;
the recomputation recipe is exact:

```
sed '$d' xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md | shasum -a 256
```

Report-body SHA256: `e024d4117309ec7482e0b9ad74ba7ddee0622d497fbf9307cde592810ca6f102`
