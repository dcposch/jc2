# Opus 5 hostile review — td=12 U1 first trunk consumer

Lane: Opus 5, independent hostile mathematical review (not primary).

Target, byte-pinned and verified this session:

```
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
```

Report body seal recomputed and confirmed: `sha256` of the first 19082
bytes = `ea43c28125b61710d1af58a90de1928a7c05f93734950c6d89814cd3c99d5be2`,
and byte 19082 is the last byte of the `*Report body ends...*` line, as
claimed.

Packet `cases/m2_td12_u1_trunk_consumer_grok46_20260829/`, all four
principal hashes reproduced:

```
e363b697323e63c4257bf3050b4e0b1bd8aa9af5705918f4aef63eb995eaa0da  polyexact.py
6f214a755e1d589bacf155195e687799b8f793706a5ca2fa7cb508c00a038d7e  trunk_consumer.py
57a948dedd6fdd589a910ae23b836f2b3a1b790a6826a0ffdde15f79a373ff41  test_trunk_consumer.py
d117ef7554e5e0221302944515d7c2cac2f11accb1d00be34be55ed09879c4c6  README.md
```

## 0. Perimeter of this review

Read this session, in the named sections only: `ladder/BOOK-OFFAXIS.md`
§6 (R1.0–R1.5), §10 (P0/P1/P2/P5 + the 2026-08-29 resolvent correction +
§10 trust perimeter), §2(c1)/§3 (MP8 non-extension); `ladder/SHEET6-AF2.md`
§1 (St 9.3 (24) verbatim + E6) and §2 (derived λ-rule);
`ladder/SHEET6-TEMPLATE.md` §0 (π-ladder / depth convention), §1c (edge
table), §2a (St 3.9 recap), §2b (F_s solve), §2c (E3–E5 transports);
`cases/l1_ode_check.py` header (family C); the promotion-safe residue
`xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md`
§4.1 and §7.1–7.3.

Executed: the packet, ordinary and `-O`, plus my own hand re-enumeration
of the entire one-step menu and my own re-derivation of the Prop 8.1(iv)
identity from the printed laws. No web, no AWS, no canonical edit, no
commit, no push, no CAS. No access of any kind to `jc2-lean`. One file
written: this path.

Not re-run here, and disclosed as inherited: the entry census that pins
the unique `td=12, m=3` row (CONFIRMED in the residue §7.1), and
Theorems C/C'/D/E at the merge.

**Landing and source realizability are not inferred anywhere below.**
Every PASS is at formal-cell / reduced-pattern scope.

---

## 1. Verdicts

| # | charge | verdict |
|---|---|---|
| 1 | unique `td=12,m=3,[2,2,2]` entry and U1 merge data | **PASS** |
| 2 | dirty trunk step from `(9/2,2)` | **PASS** |
| 3 | exact Prop 8.1(iv) solution and `B/A = 9/8` | **PASS** |
| 4 | Statement 3.9 / gauge compatibility | **PASS_WITH_REPAIR** |
| 5 | lambda `{8,9}` fitting claim and slack-one reading | **PASS_WITH_REPAIR** |
| 6 | complete cap-free one-step menu | **PASS_WITH_REPAIR** |
| 7 | independence from the merge progression parameter `n` | **PASS** |

Lead verdict `FAMILY_SURVIVES_FIRST_TRUNK` and cell verdict
`TRUNK_T1_SURVIVES` are **sustained**. No repair touches the reduced
T1 solve, the ratio, or the menu counts. The repairs are: one
under-reported sheet-level consequence of St 3.9(i) that is the actual
`n`-consumer (charge 4); one load-bearing zero-price assumption on the
`b=2` pole entries that is source-declared UNKNOWN in both directions and
that the report's §8 wrongly excludes from the slack (charge 5); and one
budget-scope circularity plus three packet/annotation defects, none
numerical (charge 6).

---

## 2. Charge 1 — entry row and U1 merge data: PASS

Recomputed from the U1 closed forms at `(r,mu,eps,w) = (3,2,0,3/2)`,
merge index `n`, without reading the report's arithmetic first:

```
dp   = eps + nu*r*mu = 6n           dq = 1 + nu*r = 3n+1
E    = mu - eps = 2                 kbar = mu*w*dq/E = 3(3n+1)/2
X    = mu*w*dp/E = 9n               M = gcd(mu-eps, r*nu+1) = gcd(2, 3n+1)
w_tr = mu*w*r/E = 2*(3/2)*3/2 = 9/2 lambda_G = 0 (eps=0)
```

All eight displayed quantities reproduce exactly.

Admissibility is **derived**, not assumed: `kbar in Z` and `M=2` are the
same condition `3n+1 even`, i.e. `n` odd. N1 at the merge is
`gcd(kbar, n) = 1`; since `gcd(3n+1, n) = 1` and `n` odd kills the
2-part, the only residual obstruction is `gcd(3, n)`, so N1 holds iff
`n !== 0 (mod 3)`. Together: `n mod 6 in {1,5}`, and `nu >= 2` with that
AP gives `n >= 5`. The report's admissibility line is exactly right, and
its three-way factorisation into (odd, not-3, `>=5`) is the correct one.

Uniqueness of the `td=12, m=3` row of type `(2,3)`, `Lambda=(4,4,4)`,
poles `(1,2,3)^3`, `M=[2,2,2]`, `w0=3/2` is inherited from the CONFIRMED
residue §7.1 and is not re-derived here; the report does not claim to
re-derive it either. No overreach.

The `n` versus `nu_F` notation split is handled correctly and is not
cosmetic: `25 mod 6 = 1`, so `nu_F = 25` does lie on the merge AP. The
report flags the collision explicitly in §0 and the packet enforces
`nu_F != l` and `nu_F != k` as live checks. I found no place where the
two are conflated.

---

## 3. Charge 2 — the dirty trunk step: PASS

Recomputed from `BOOK-OFFAXIS.md` §10 P0 and §6 R1.3/R1.4 verbatim, at
`(l, eps, k, lex, Sm, nu_F) = (2, 0, 1, 0, 1, 25)` with parent `w_G = 9/2`:

```
dp = eps + nu(l+Sm) = 75          dq = (1+k+lex)nu + 1 = 51
E  = l*dq - dp = 27               C_P0 = l(k+lex) - Sm = 1
T  = Sm + l - eps(1+k+lex) = 3    kbar = l*w_G*dq/E = 9*51/27 = 17
X  = kbar*dp/dq = 17*25/17 = 25   M_F = gcd(75,51) = 3
w_F = l*w_G(dq-1)/(nu*E) = 9*50/675 = 2/3
```

`w_F = 2/3` is reproduced from R1.4's own formula, not from the report.
Filters: (S) `102 > 75`; (NE) `1*51 < 75` strict; (R) `75 != 51`,
`75 != 102`; N1 `gcd(17,25)=1`; R1.0 `gcd(M_F,nu_F) = gcd(3,25) = 1` and
`dq = 2*25+1 ≡ 1 (mod 25)`; MP2 `M_F = 3 >= 2`. Divisor law
`E | l*num(w_G)*T = 54` with `54/27 = 2`. Terminal: `j = M_F(1-w_F) = 1`,
`psi = ceil(3/1) - 1 = 2`, budget `td-1-psi = 9`. Floor
`lambda_F >= max(1, ceil(25/1 - 17)) = 8`.

The `l=1` exclusion is correct and printed (R1.3: at `mu=1` arrivals
`dq > dp` makes every root searrow, so no dirty vertex exists); the
`lex=0` forcing is correct and I re-derived it: NE with `m_j >= 1`
requires `dq < dp`, i.e. `nu*lex + 1 < nu`, which fails for every
`lex >= 1`. The `k=1` multiplicity is forced by `m_j <= l-1 = 1`.

**One precision note, no verdict impact.** The report calls the Fable
resolvent evaluation `27*(36-34) = 54 = l*a*T` an independent check
("independently evaluated ... holds"). It is an algebraic identity, not
a constraint. Writing `K := 1+k+lex`, `a/d := w_G` in lowest terms, and
using `E = nu*C + (l-eps)`, `dq = K*nu + 1`, `kbar*d*E = l*a*dq`:

```
E(l*a*K - kbar*d*C) = l*a*(E*K - dq*C) = l*a*((l-eps)K - C)
                    = l*a*(l + Sm - eps*K) = l*a*T.
```

So it cannot fail once `kbar` is computed correctly; its entire content
is the implication `kbar in Z  ==>  E | l*a*T`, which is the finiteness
law and is separately used. The packet's `resolvent_ok` boolean is
likewise a re-check of `kbar in Z` (it goes through `int(kbar)`), not a
second witness. The arithmetic is right; the epistemic weight is smaller
than the phrasing suggests.

---

## 4. Charge 3 — exact Prop 8.1(iv) and `B/A = 9/8`: PASS

I re-derived the identity from scratch rather than checking the report's.

With `t = eta^nu`, `t' = nu*t/eta`, `Pfull = (t-A)^2(t-B)`,
`W = (t-A)(t-B)`, `q = eta*W`:

```
q' = W + nu*t*W_t,      p' = (nu*t/eta) * Pfull_t,
rho*p*q' - p'*q = rho*Pfull*W + nu*rho*t*Pfull*W_t - nu*t*Pfull_t*W,
```

which is **verbatim family C of `cases/l1_ode_check.py`**
(`E := rho*pt*w + nu*rho*t*pt*w' - nu*t*pt'*w = ctilde*pt`). The report's
§3.1 display is exactly that object.

Since `Pfull = (t-A)*W`, the division is exact and gives, independently:

```
C_iv(t) = rho(t-A)(t-B) + nu*t[ (rho-2)(t-B) + (rho-1)(t-A) ].
```

Top coefficient, with `rho = dp/dq = 3nu/(2nu+1)`:

```
rho + nu(2rho - 3) = [3nu + nu(6nu - 6nu - 3)]/(2nu+1) = 0   identically.
```

I also confirmed this is the same cancellation as the drop of `E` from
degree 5 to degree 3: `Pfull` is monic, so the quotient's `t^2`
coefficient equals `E`'s `t^5` coefficient, which is
`rho + 2*nu*rho - 3*nu`. No degree cap is in play; the report's "exact
degree 5 before cancellation" is correct.

Linear coefficient, cleared:

```
A*[rho + nu(rho-1)] + B*[rho + nu(rho-2)]
   = A*nu(nu+2)/(2nu+1) - B*nu(nu-1)/(2nu+1) = 0
   ==>  B/A = (nu+2)/(nu-1).
```

At `nu = 25`: `27/24 = 9/8`, and the two coefficients are `225/17` and
`-200/17`, both nonzero, so the kernel is exactly one-dimensional.
`C_iv = rho*A*B`; at `(A,B) = (8,9)`, `C_iv = (25/17)*72 = 1800/17 != 0`;
at `(A,B) = u*(8,9)`, `C_iv = 1800*u^2/17 != 0` for `u != 0`. **All of
this reproduces the report exactly.**

**Independent second-cell corroboration.** The report's `nu=7`
cross-check is not a restatement — I verified it against the printed
object. `SHEET6-TEMPLATE.md` §2b's own identity, in its own
i-normalisation, is `3*phi*psi - (9/7)eta*phi'*psi + (6/7)eta*phi*psi'`.
Expanding with `eta*phi' = eta*psi' = 7t`:

```
3(t-A)(t-B) - 9t(t-B) + 6t(t-A) = (6B - 9A)t + 3AB,
```

constant iff `B = (3/2)A`, with constant `3AB = (9/2)A^2` — exactly the
printed `(9/2)A^2`. That polynomial is `(15/7)` times my `E/Pfull` at
`nu=7, rho=7/5`, so the two normalisations agree on the nose, and my
closed form `(7+2)/(7-1) = 3/2` reproduces the printed F_s solve. The
report's closed form is therefore validated on a **second, independently
printed cell**, not only on the charged one.

R1.0 side conditions all check: `A,B != 0` and `A != B` (from
`C_iv != 0` and `9/8 != 1`); `rho = 25/17` lies strictly in `(1,2)` so
`rho != mu*` for both `p`-multiplicities `mu* in {1,2}` — equivalently
`dp != 1*dq` and `dp != 2*dq`, which is filter (R); `Pfull(0) = 64*9*u^3 != 0`
so no `p`-zero-root, consistent with `eps=0`; `W(0) = AB != 0` so
`eta || q` exactly.

Packet mutation set is non-vacuous: `A=B`, `B/A=7/8`, `A=0`, `nu -> -nu`,
and dropping the `Pfull_t` term are all detected, and the eight-`nu`
sweep cross-checks the derived ratio `-c_A/c_B` against the closed form
rather than asserting it. `require()` is a function raising `ValueError`,
not `assert`, which is why `-O` is genuinely equivalent — I confirmed
`checks=134` under both.

---

## 5. Charge 4 — Statement 3.9 and gauges: PASS_WITH_REPAIR

### 5.1 The orientation is correct (I attacked it and it held)

The report's `shallow = dirty vertex F, deep = merge G` looks inverted
against `BOOK-OFFAXIS` P2's "the trunk below the merge" and R1.2's
"`G` parent above, `F` = child". It is not. `SHEET6-TEMPLATE.md` §0 pins
the convention explicitly — "root at the bottom; `°` moves toward the
root, `+ c` away from it" — with the π-ladder

```
P_i (poles)  pi = 37/42   deepest
G_m (merge)  pi = 16/21
F_s          pi = 2/7
(0,y) = R    pi = 0       shallowest
```

so merges are **deeper** than the suffix/trunk vertices, and `F + c` is
deeper. BOOK-OFFAXIS's "parent above / child below" is the direction of
the P0 recursion (poles toward the root), which is deep-to-shallow in π.
The report's assignment is right, and its choice of `c` is right too:
`mult(Pfull_F, A) = 2 = l = mu`, matching St 8.4 and matching the
template's own suffix edge `F_s->G_m | mu 2 | II(a) k=1, l=0` — which is
the *same shape* as the charged cell at `nu=7`. The St 3.9(ii) direction
(lead of the deeper = `mult`-th Taylor coefficient of the shallower at
`c`) also matches the template's E5 usage. No repair here.

The gauge table is correct. The order-2 Taylor coefficient of
`(eta^nu - A)^2(eta^nu - B)` at `eta = c` is `nu^2 c^(2nu-2) (A-B)`, a
unit times `(A-B) = -u`: homogeneous of degree 1 in the scale, hence a
normalisation, not a second ratio invariant. And `A_star` is a symmetric
function of the merge roots while `9/8` is a trunk root ratio in a
different chart (`eta_G^n` vs `eta_F^25`), so the row
"a numerical relation `A_star <-> 9/8` — **not** forced by printed
St 3.9" is **CONFIRMED**.

### 5.2 REPAIR 4a — the sheet-level count law is exact, and it is the `n`-consumer

§4's second bullet says St 3.9(i) "is not applicable to those two
polynomials as written". True for the *reduced* patterns, and the reason
is right (it is a sheet law). But the report stops there, and the
sheet-level instance is not vacuous — it is **exact**, and the template
proves it on the analogue. At `F_s`: `deg p_{F_s} = 126` and reduced
`dp = 21`, so `i_{F_s} = 6`; `mult(p_{F_s}, c_m) = i*2 = 12`; and
`deg p_{G_m} = 12`. Count law exact, `12 = 12`.

Transporting the same reading to the charged edge gives

```
i_F * mult_red(Pfull_F, A) = i_G * dp_red(G)
       i_F * 2             = i_G * 6n        ==>   i_F = 3n * i_G.
```

That is the sharpest available statement about this edge, it is the
**only** place in the entire charge where `n` enters a printed law, and
the report never writes it down. §6.2 correctly *names* the consumer
("it needs a named tower/`i` at `G` as a function of `n`") but by leaving
it unquantified it understates the strength of the `n`-dependence: it is
not a vague growth, it is a linear pin on the tower-index ratio.

This changes no verdict — `i` is an unbounded normalisation index and a
linear pin on a ratio of unbounded indices is not a kill — but it is
the object a cofinality or budget-on-`i` argument would attack, and it
should be recorded rather than left as prose.

---

## 6. Charge 5 — lambda `{8,9}` and slack one: PASS_WITH_REPAIR

### 6.1 What is correct

The floor is right and rests on the corrected (24). AF2 §1's E6-repaired
St 9.3 reads `kappa_H(pi(H)-1) >= D_F/mult(p_F,c*) - kbar_F` for
`c* != 0`; with `X_F = D_F/i` (from `rho_F = X_F/dp_F = D_F/deg p_F`)
this is `gap = X_F/m_j - kbar_F = 25 - 17 = 8`, an exact integer, so
`lambda_F >= max(1, ceil(8)) = 8`. The report's §5 statement that the
**exact** value is `kappa_H(pi(H)-1)` at the cv vertex `H`, and that
this is not a function of the reduced `(p,q)` cell, is exactly the
content of (24) and is correct. The NE/climb premise is also correct:
`gap > 0` puts `F + B in T_a↗` (AF2 R2), and St 7.3 then supplies the
cv flag (R3). The ceiling `9 = td - 1 - psi` with `psi = 2` is correct.

### 6.2 REPAIR 5a — the three `b=2` pole entries are unpriced, and they are in the same budget

`{8,9}` and "slack 1" both require `Sum lambda` over the **other**
pairwise-distinct ↘-vertices to be zero. `lambda_G = 0` at the merge is
derived (Theorem B, `eps = 0`, `k = 0`: no NE orbit, no free 0-root).
`lambda = 0` at the three pole entry vertices is **not** derived, and the
source says so in terms:

- `BOOK-OFFAXIS.md` §2(c1): "For `M >= 2` the printed record does NOT
  exclude segment vertices in `V_{2,a}` ... Hence the MP8 zero-row
  itemization does not extend: off-axis chains can carry `Y(F) != ∅` /
  `lambda > 0` — but a POSITIVE lower bound is not printed either
  (transparency fails in both directions)".
- §3: "budget status of every off-axis cell is UNKNOWN, in both
  directions."
- §10's trust perimeter cites MP5/MP8 as "**`b = 1`** chains free". These
  poles have `b = 2`.

The residue §7.2's `lambda=0` clause is the P2 *arrival* law
(`(nu_i, mu | b)` with `mu=2 | b=2`), which licenses a zero-length pole
chain — i.e. no intermediate chain vertices to charge. It does not price
the pole vertices themselves, which are separate elements of St 9.4's
`F_i` sum.

Taking `lambda_poles = 0` is legitimate for a *non-exclusion* verdict
(you need one budget-fitting assignment, and the superset policy is
"unpriced ⟹ 0, no false kills"). So the lead verdict survives. But it is
an optimistic open assumption in the survival direction, and the report
grades it inconsistently: §5's "with merge and pole chains at floor 0"
is honest (it says *floor*); §2.2's "Merge plus three pole chains
contribute `lambda=0`" is flat; and §8's

> "That is the first missing subtop, and it is the only remaining local
> unknown that can still spend the slack."

is **too strong**. The cv jet is the only remaining *trunk-local*
unknown. There are three further unpriced ↘-vertices in the same shared
budget, each of which can spend the same single unit.

Correct rider: *any one* further unit anywhere in the configuration —
extra-branch cv jet **or** a pole entry — still fits at 9; any two kill.
And because the three pole entries are identical `(1,2,3)` cells with
`M=2`, a positive price at one is a positive price at all three by
symmetry, i.e. `+3` at once: `8 + 3 = 11 > 9` kills the charged route and
`8 + 3 = 11 > 8` kills the `(3/4,4)` sibling too. That asymmetry (one
unit from the jet is survivable; the pole question is all-or-nothing for
the whole family) is not visible in the report and is what makes it the
better next target — see §9.

---

## 7. Charge 6 — the complete cap-free one-step menu: PASS_WITH_REPAIR

### 7.1 Full independent re-enumeration

I enumerated the entire menu by hand from P0 / R1.2 / R1.3, **without**
running or reading the packet's enumerator first, and then compared.

*Clean, `l=1`.* `m_j <= l-1 = 0` and `eps <= l-1 = 0` force `k=Sm=eps=0`.
`lex=0` is neutral (`M'=gcd(1,dq)=1`, `w` fixed). `lex>=1` needs
`Delta = lex*nu+1 | num(w)=9`, so `Delta in {3,9}`, i.e.
`(lex,nu) in {(1,2),(1,8),(2,4),(4,2)}`; all four have `dq` odd
(`5,17,13,11`) so `den(w)=2 | dq` fails and `kbar` is not integral. Zero
survivors.

*Clean, `l=2`, `k=lex=eps=0`.* Neutral: `dp=2nu`, `dq=nu+1`, `E=2`,
`kbar = 9(nu+1)/2 in Z` iff `nu` odd, then `M' = gcd(2,nu+1) = 2` and
`w' = 9/2`. One family.

*Clean-resonant, `l=2`, `k=0`, `lex>=1`.* Same four `Delta|9` candidates,
same parity failure. Zero survivors.

*Pure-epsilon, `l=2`, `eps=1`, `k=lex=Sm=0`.* `w -> l*w/(l-eps) = 9`,
`M' = gcd(1,nu+1) = 1`, `lambda >= ceil(l*w/eps) = 9`. One family.

*Dirty, `eps=0`, `k>=1`, `lex=0` (forced).* `E = k*nu + 2 | 18(k+2)`,
`kbar = 9((k+1)nu+1)/(k*nu+2) in Z`. Scanning `k = 1..9` (`k>=10` costs
`>= 10`):

| k | E-divisor candidates | survivors |
|---:|---|---|
| 1 | `nu+2 \| 54`: nu ∈ {4,7,16,25,52} | **7, 25** |
| 2 | `2nu+2 \| 72`: nu ∈ {2,3,5,8,11,17,35} | **5, 17** |
| 3 | `3nu+2 \| 90` | none |
| 4 | `4nu+2 \| 108`: nu ∈ {4,13} | **13** |
| 5 | `5nu+2 \| 126`: nu ∈ {8} | none |
| 6,7,9 | — | none |
| 8 | `8nu+2 \| 180`: nu ∈ {2,11} | **11** |

Six survivors. *Dirty, `eps=1`, `lex=0` (forced), `k>=1`.*
`E = k*nu + 1 | 18`, `E in {3,6,9,18}` gives
`(k,nu) in {(1,2),(1,5),(1,8),(2,4),(4,2),(1,17)}`; `kbar` integrality
kills `(1,5)` and `(1,17)`. Four survivors.

**Total 2 + 1 + 0 + 10 = 13.** I then diffed against the emitted payload:
every one of the 10 dirty edges agrees field-for-field on
`(nu_F, k, Sm, E, C_P0, T, kbar, X, lambda, w, M)`. The four P1-shaped
children `(2/3,3)@25`, `(3/4,4)@17`, `(5/6,6)@13`, `(9/10,10)@11` all
carry `lambda = 8`, with `psi = 2,3,5,9` and own budgets `9,8,6,2`, so
exactly the first two fit. The `k=1, eps=0` divisor-of-54 scan recovers
exactly `{7,25}`.

The `lambda = 8` coincidence across all four is not a coincidence and I
record the law: with `eps=0`, `X - kbar = 9(nu-1)/(k*nu+2)`, so
`k(X-kbar) = 8` iff `nu = 9 + 16/k`, giving `k in {1,2,4,8}` ->
`nu in {25,17,13,11}` — precisely the four P1-shaped children.
`k = 16 -> nu = 10` is killed by `kbar = 19/2`.

Replay, both modes, reproduced byte-for-byte:

```
TD12_U1_TRUNK_CONSUMER_TEST_PASS checks=134      (python3 and python3 -O)
payload_sha256  995f67e9b4e6bc69414ec2454ed532639f09d06ee924669600ebffe1cf4b81fc
json file sha   b047c364d4af796eae6fea2b54ffe45074863206e8a60425e1f77555bdfa626e
```

### 7.2 REPAIR 6a — the completeness budget is the one the report's own answer produces

The menu is enumerated at "remaining budget 9", which is `td-1-psi` for
the terminal being advertised. The **maximal** St 9.4 budget at `td=12`
is `10`: `psi >= 1` always, because `w > 0` forces `j = M(1-w) <= M-1`
and hence `ceil(M/j) >= 2`. Claiming a *complete* one-step menu at
budget 9 is therefore mildly circular.

I closed the gap rather than only flagging it. No one-step edge from
`(9/2,2)` costs 10:

- `eps=0` dirty: `lambda = k*ceil(9(nu-1)/(k*nu+2))` with `k*gap < 9`, so
  `lambda = 10` needs `(k, ceil(gap)) in {(1,10),(2,5),(5,2),(10,1)}`.
  `(1,10)` is empty since `gap < 9`. `(2,5)` needs `gap in (4,4.5)`, i.e.
  `nu > 17`, and `2nu+2 | 72` then forces `nu = 35`, where
  `kbar = 954/72` is not integral. `(5,2)` forces `nu = 8`,
  `kbar = 441/42` not integral. `(10,1)` forces `nu = 7`,
  `kbar = 702/72` not integral.
- `eps=1` dirty: `E = k*nu+1 | 18` bounds the family; all four legal
  cells cost exactly 9.
- pure-epsilon: `ceil(l*w/eps) = 9` is the only value. Clean: 0.

**So the menu is complete at budget 10 as well, and the completeness
claim survives.** The report should state the bound it needs (10), not
the one its terminal produces (9).

### 7.3 REPAIR 6b — filters recorded but not enforced

`one_step_menu` writes `N1: gcd(kbar,nu)==1` into each dirty witness but
never filters on it, and never applies R1.0's `gcd(M_F, nu_F) = 1`. All
10 emitted edges satisfy both (I checked each: `gcd(kbar,nu)` and
`gcd(M,nu)` are 1 throughout), so the count of 13 and the "exactly two
fitting terminals" claim are unaffected **here**. But the routine is a
general-state enumerator taking `(w, M_parent, budget)`; at another state
it can over-emit. Over-emission is safe for a completeness claim and
unsafe for an "exactly two fit" claim, so this should be closed before
the routine is reused — e.g. for the `(3/4,4)` sibling's own successors.

Related, smaller: the clean-neutral family is *asserted* (its witness is
only `{M_parent, M_child}`; no `nu` is constructed). I verified
achievability by hand — `M'=2` needs `l=2` with `nu` odd, `M'=1` needs
`l=1` or `nu` even — so the count 2 is right, but the packet does not
exhibit a witness.

### 7.4 REPAIR 6c — the clean-resonant row states the wrong reason

The table note reads "no `Delta | 9` edge keeps `M >= 2` (the claimed
emptiness)". That is not the filter that fires. The filter is R1.2
integrality, `den(w) = 2 | dq_F`; all four `Delta|9` candidates have odd
`dq`, so `kbar` is not an integer. For `l=2` the two conditions are
coextensive (`dq` even iff `M=gcd(2,dq)=2`), and for `l=1` `M=1`
unconditionally, so the stated reason does also fire and the count 0
stands either way. The defect is one of convention consistency: the
document counts MP2-dead edges elsewhere (the clean-neutral `M'=1` row
and the pure-epsilon `M'=1` row are both listed), so "dropped because
`M<2`" is not the rule in force.

Cosmetic, same family: §6.1 says completeness of `{7,25}` follows from
"the divisor list of 54 together with `kbar in Z` and N1". N1 does no
work — all six `k=1` candidates that survive the divisor list and
`kbar in Z` also satisfy N1.

### 7.5 REPAIR 6d — the sealed payload carries a wrong `C_iv` annotation

```
"C_iv_general": "225 u^2 / 136  (A=8u, B=9u)"
```

This is wrong. `C_iv = rho*A*B = (25/17)(8u)(9u) = 1800 u^2 / 17`, which
is what the report prints in §3.2 and §4 and what I derived
independently. `225/136 = (25/17)*(9/8) = rho*(B/A)` — a different
object, carrying a spurious `u^2`.

The field is free text, is not read by any `require`/`check` (the test
asserts only `t1["C_iv"] == "1800/17"`), and no mathematics depends on
it. But it sits inside the hashed payload `995f67e9...`, so the sealed
certificate contains a false statement, and the report and its own packet
disagree on the general `C_iv`. **The report's value is the correct one.**

---

## 8. Charge 7 — independence from the merge AP parameter: PASS

Three separate legs, all verified:

1. `w_tr = mu*w*r/E = 2*(3/2)*3/2 = 9/2` contains no `n`, and
   `M = gcd(2, 3n+1) = 2` for every admissible (odd) `n`. So
   `(w_tr, M) = (9/2, 2)` on the whole AP. Confirmed by re-deriving the
   closed forms, not by trusting Theorem C'.
2. The one-step menu is a function of `(w, M_parent, budget)` only. This
   is not merely asserted: `one_step_menu(w, m_parent, budget)` has no
   other input, and I read the body — `n` appears nowhere in it. My hand
   enumeration in §7.1 likewise never used `n`.
3. `nu_F = 25` is a fixed cell index, and `B/A = (nu_F+2)/(nu_F-1) = 9/8`
   is a function of `nu_F` alone.

The `25 in AP` coincidence is flagged by the report and does no work
anywhere.

The report's identification of the residual `n`-consumer (St 3.9
sheet-count / lead transport along the trunk edge) is **correct in
kind**, and REPAIR 4a makes it quantitative: `i_F = 3n * i_G`. That
sharpening does not disturb this PASS. An `i`-ratio growing linearly in
`n` is not a kill, since `i` is an unbounded normalisation index; it is
simply the first named object that sees `n`.

---

## 9. Best next subtop / jet discriminator

The report nominates the extra-branch cv jet at the `B`-direction
(gap 8): either `lambda_F = 8` exactly, or a printed unit forces
`>= 9` (still fits) or `>= 10` (kills). That is a correct and worthwhile
target, and I agree it is the first missing *trunk-local* object.

**But it is not the best next discriminator.** I recommend instead:

> **Price the `b=2` pole entry vertex `(a,b,nu) = (1,2,3)`, `M=2`,
> `w0 = 3/2`: is its St 9.4 exit set empty?**

Reasons it dominates the cv jet:

- **Leverage.** The three pole entries are identical, so by symmetry the
  answer is `0` or `>= 3`. `>= 3` gives `8 + 3 = 11 > 9` and kills the
  charged route outright, *and* `11 > 8` kills the `(3/4,4)` sibling, and
  it removes the only two one-step P1-fitting terminals in the entire
  menu at one stroke. The cv jet can at best move `lambda_F` from 8 to 9
  (still fitting) or to `>= 10`, which kills only this cell and leaves
  the sibling and every longer route alive.
- **Scope.** It is `n`-free and `(w,M)`-free, so one computation settles
  the whole admissible AP, and it transfers to every other off-axis
  `b >= 2` entry in the `td <= 14` book.
- **Standing.** `BOOK-OFFAXIS.md` §2(c1)/§3 declare it UNKNOWN *in both
  directions* at printed tier — it is a named, live, printed-tier gap,
  not a speculative one. MP5/MP8 cover `b=1` only.
- **Cost.** It is a single-vertex exit-set question at an entry cell
  whose full data are already pinned (`Lambda=4`, `deg p = b*alpha = 4`,
  `i=2`, `mu=2`), not a jet construction on a branch the reduced cell
  does not build.

Ranked follow-ups: **(2)** the cv jet as the report proposes; **(3)** the
sheet-level St 3.9(i) instance `i_F = 3n*i_G` of REPAIR 4a, which is the
only place `n` enters and is the natural target for any cofinality
argument; **(4)** T1 on the `(3/4,4)` sibling at
`(nu_F, dp, dq) = (17, 68, 52)`, `k=2` — the report correctly declines to
substitute it for the charge, and I confirm its cell data
(`E=36, kbar=13, X=17, lambda=8, j=1, psi=3, budget 8, slack 0`).

**One cheap cross-check worth running before any of these.** The printed
St 9.6 p.53 possibility list contains `(9j, 75j, 25, 3, 6)` with
`lambda_F >= 3 = 9 - 6` (AF2 §1, example (B)) — the same
`(nu, M, reduced dp) = (25, 3, 75)` as the charged cell, but with
`kbar = 6, X = 9` against the charged `kbar = 17, X = 25`. These are
different frames, so there is no conflict, and the report never cites the
entry. But I could not reconcile the printed tuple with the reduced laws
at all: `rho = D/deg p = 3/25` and `rho = kbar/dq` force `dq = 50`, which
violates `dq ≡ 1 (mod nu)` and gives `gcd(dp,dq) = 25 != 3`. AF2 already
documents slips in that same p.53 block (E5, E6). Anyone who later wants
to lean on that list as a classification must reconcile it first; as it
stands it can be used neither as a pin nor as a counter-cell.

---

## 10. Maximum safe consequence

At recorded reduced-pattern / superset scope, and conditional on the open
items named in REPAIR 5a:

> The displayed first trunk cell of the source-pinned `td=12`, `m=3`,
> `[2,2,2]`, type `(2,3)` U1 family is a legal P0 edge from the constant
> reduced trunk state `(w_tr, M) = (9/2, 2)`, and reduced Proposition
> 8.1(iv) on that cell has a solution set that is exactly one gauge orbit:
> `Pfull = (t-8u)^2(t-9u)`, `W = (t-8u)(t-9u)`, unique invariant
> `B/A = 9/8 = (nu_F+2)/(nu_F-1)` at `nu_F = 25`, with automatically
> nonzero `C_iv = rho*A*B`. This consumer therefore does not kill the
> family, and it does not vary with the merge AP parameter `n`.
> Among the complete 13-edge one-step menu from `(9/2,2)` — complete at
> the maximal `td=12` budget 10, not merely at 9 — exactly two edges are
> P1-fitting terminals: the charged `(2/3,3)` at `nu_F=25` with slack 1,
> and the sibling `(3/4,4)` at `nu_F=17` with slack 0. The `lambda_F`
> window `{8,9}` holds **given** that the merge and all three `b=2` pole
> entry vertices price 0; `lambda_merge = 0` is derived, the pole prices
> are source-declared UNKNOWN in both directions.

That is the whole of it. Explicitly **not** established, by this review
or by the report: landing; realizability of the cell or the family by any
`(f,g)`; existence of a Keller pair; gluing or monodromy of
`t^3 - A_star`, or any numerical relation between `A_star` and `9/8`; an
extra-branch tower; completeness at any `td`; a `td` ceiling or cofinal
bound; restoration of a prime-`td` exclusion; `G2-BD`; `G2-PSC`; any JC2
consequence. Alive is not existent (R4). The panel status is unchanged:
`BOOK-OFFAXIS.md` §4 already records `td=12` composite as open.

I confirm the report's own §7/§9 firewall is accurate and that it does
not overreach from the formal cell to landing or to source realizability
anywhere in the body. Its `slack 1` is correctly presented as a
lower-bound remainder rather than an equality theorem; my only complaint
in that direction is §8's "only remaining local unknown", handled in
REPAIR 5a.

---

## 11. Scope firewall for this review

This review asserts no landing theorem, no completeness at any `td`, no
realizability, no gluing, no `td` bound, and no JC2 consequence. It
changes no panel status and no canonical file. It did not access
`jc2-lean` in any way. It performed no web or AWS work, no commit, no
push, and no canonical edit. Files written: this path only.

**Verdicts: charges 1, 2, 3, 7 `PASS`; charges 4, 5, 6
`PASS_WITH_REPAIR`. Lead verdict `FAMILY_SURVIVES_FIRST_TRUNK` and cell
verdict `TRUNK_T1_SURVIVES` SUSTAINED.**

---

*Review body ends. The seal below covers everything above this line.*


report_body_sha256 = 86ccd2f1f36a37fce7f038ce3a162468f61aea4974dfd778a370ab3e04fa7e3e
(sha256 of this file up to and including the line "*Review body ends...*", i.e. of the first 30274 bytes)
