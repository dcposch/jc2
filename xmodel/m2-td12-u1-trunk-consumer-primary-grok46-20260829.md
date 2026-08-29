# Grok 4.6 primary research — td=12 U1 family's first trunk consumer

Lane: Grok 4.6, primary mathematics (not review).
Target: the displayed dirty trunk cell of the source-pinned `td=12`,
`m=3`, `[2,2,2]`, type `(2,3)` U1 family.

Writes: this path, and packet
`cases/m2_td12_u1_trunk_consumer_grok46_20260829/`. Scratch under `/tmp`
only.

## 0. Custody and perimeter

Promotion-safe residue, used as law:
`xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md`
§8 (U1 closed forms, exact `M = gcd(mu-eps, r*n+1)`, AP of admissible merge
index `n`, T1-GEN, U1 rigidity `Rad = t^r - A_star` with `A_star != 0`).
Opus clauses are used only where that review marks them CONFIRMED: Theorem B
closed forms, Theorem C AP, Theorem C' constancy/periodicity of `(w_tr, M)`,
Theorem D (T1-GEN) and its family-C specialization, Theorem E at the merge,
the unique source row of type `(2,3)`, and the displayed dirty-step
arithmetic / P1 budget (slack 1, lambda a lower bound).

Current source, read in the named sections only:

- `ladder/BOOK-OFFAXIS.md` R1.0, R1.3–R1.4, P0, P1, and the 2026-08-29
  resolvent correction `E(l*a*(1+k+lex) - kbar*d*C_P0) = l*a*T`;
- printed Statement 3.9 as recapped on-page in `ladder/SHEET6-TEMPLATE.md`
  §2a (and the same file's F_s ratio `B = (3/2)A` at `nu=7`);
- `ladder/SHEET6-AF2.md` extra-branch climb;
- `ladder/SHEET6-III.md` §3 N1: `gcd(kbar, nu)=1` at every `nu>=2` vertex;
- `cases/l1_ode_check.py` header, family C (the `(2,1)` suffix shape);
- the passed finite-chain R1 theorem and R2 implementation repair
  (`PASS_IMPLEMENTATION_R2`), used only for the exact divisor law
  `E | l*num(w)*T` and the lex/k bounds.

Not read, as instructed: active td=8 transport, exact-lambda, U2-review,
ideation, or other post-target model output. No access of any kind to
`jc2-lean`. No web, AWS, commit, push, canonical edit, heavy CAS, or
workspace-wide search. Arithmetic is desk `int`/`Fraction` and one sparse
polynomial class in the packet.

Nothing here proves landing, existence of a Keller pair, a panel exclusion,
a `td` ceiling, gluing of `t^3 - A_star`, or JC2.

Notation split, used throughout: the merge AP parameter is `n`
(`n >= 5`, `n mod 6 in {1,5}`). The trunk vertex index is `nu_F`. The
displayed cell has `nu_F = 25`. That `25` is not `n`, and it is not a local
polynomial exponent (`l=2`, chain-orbit power `2`, extra-orbit power `1`,
`t = eta^{25}`). The integer `n=25` happens to lie on the merge AP; it is a
different object.

---

## 1. Verdict

**`FAMILY_SURVIVES_FIRST_TRUNK`**

Cell-level: **`TRUNK_T1_SURVIVES`**.

The displayed dirty chain cell is a legal P0 edge from the constant reduced
trunk state `(w,M)=(9/2,2)`, and Proposition 8.1(iv) on that cell is an
exact two-coefficient identity in the two `t`-roots. After the top degree
cancels identically, one linear condition remains. Its kernel is one
dimensional: unique ratio `B/A = 9/8`, nonzero right-hand side
`C_iv = (25/17)AB`, no `p`-zero-root, `eta || q`, R1.0 simple `q`-roots.
No source coefficient is missing for this reduced solve. Local survival is
not gluing and not realizability.

Exact lambda of the unique northeast orbit is not pinned by the reduced
cell: P0/AF2 give floor `8`, the P1 ceiling for this terminal is `9`, and
the first missing object is the extra-branch cv jet. Slack one is
genuinely available as a lower-bound remainder; T1 does not consume it and
does not force it to zero.

The complete cap-free one-step menu from `(9/2,2)` at remaining budget 9
has 13 edges (0 clean-resonant, 2 clean-neutral, 1 pure-epsilon, 10 dirty)
and contains exactly two P1-fitting one-step terminals: the charged
`(2/3,3)` cell and a sibling `(3/4,4)` cell at `nu_F=17`, `k=2`, cost 8,
own-budget equality. Both are functions of the constant pair `(w_tr, M)`,
not of the merge index `n`.

---

## 2. Attack 1 — row, merge progression, dirty arithmetic

### 2.1 Source-pinned entry and U1 merge

Confirmed unique L6-surviving off-axis entry at `td=12`, `m=3`: type
`(2,3)`, `Lambda=(4,4,4)`, poles `(a,b,nu)=(1,2,3)^3`, `M=[2,2,2]`,
incoming `(mu,w)=(2,3/2)^3`. Star merge `r=3`, equal arrivals, `k=lex=0`,
no 0-arrival: the U1 family `(r,mu,eps,w)=(3,2,0,3/2)`.

Theorem B (confirmed) at merge index `n`:

```
dp = 6n,   dq = 3n+1,   E = 2,
kbar = 3(3n+1)/2,   X = 9n,
M = gcd(2, 3n+1) = 2,   w_tr = 9/2,   lambda_G = 0,
```

admissible iff `n >= 5`, `n` odd and `n not≡ 0 (mod 3)`, i.e. `n mod 6 in
{1,5}`. Packet check on `{5,7,11,13,17,19,23,25}`: (S), N1, integer `kbar`,
`M=2` all hold. Merge T1 (Theorem E, confirmed, not re-solved here):
`Rad_G(t_G) = t_G^3 - A_star` with `A_star != 0`, `t_G = eta_G^n`.

### 2.2 Dirty trunk step from `(9/2, 2)`

P0 chain vertex, arrival `l | M_parent`, `l=2 | 2`. Shape R1.3 with
`eps=0`, `k=1` (one non-chain orbit, multiplicity 1 forced by `m_j < dp/dq
< 2`), `lex=0` (R1.3: extras `lex>0` would violate `dq < dp` at `l=2`).
Trunk index `nu_F=25`:

```
P = 3,  s = 2,
dp = 75,  dq = 51,  E = 2*51 - 75 = 27,
C_P0 = l(k+lex) - Sm = 1,   T = Sm + l = 3,
kbar = 2*(9/2)*51/27 = 17,   X = 17*75/51 = 25,
w -> 2/3,   M -> gcd(75,51) = 3.
```

Filters: (S) `2*51 > 75`; (NE) `1*51 < 75`; (R) `75 != 2*51` and
`75 != 51`; N1 `gcd(17,25)=1`; R1.0 `gcd(M, nu_F)=gcd(3,25)=1`; MP2
`M=3>=2`. P0 divisor law: `E | l*num(w)*T = 54`, and `27 | 54`. Fable
resolvent (the 2026-08-29 correction, independently evaluated)

```
E * (l*a*(1+k+lex) - kbar*d*C_P0) = 27*(36 - 34) = 54 = l*a*T
```

holds. Successor is a P1 terminal: `j = M(1-w) = 1 in N*`,
`psi = ceil(3/1)-1 = 2`, shared ceiling `td-1-psi = 9`. Lambda floor
`max(1, ceil(X/1 - kbar)) = 8`, so `8 <= 9`, slack 1 as a lower-bound
remainder. Merge plus three pole chains contribute `lambda=0`.

This is an exact P0 edge, not a legacy phantom. The merge parameter `n`
does not enter the cell.

---

## 3. Attack 2 — exact Proposition 8.1(iv) on the dirty cell

### 3.1 Pattern and normalized equation

R1.0 + R1.3 at this cell, `nu_F >= 2`:

```
p = Pfull(t) = (t - A)^2 (t - B),     t = eta^{25},
q = eta * W(t),   W = (t - A)(t - B),
```

one non-chain orbit `B` (simple in `p` and in `q`), no `p`-zero-root
(`eps=0`, `Pfull(0) = (-A)^2(-B)`), `eta || q`. Gauge: overall scaling of
`(A,B)` by a unit in `t` (eta/deck). Distinct from every exponent: the
only polynomial exponents in `t` are `2` (chain) and `1` (extra).

Normalized Prop. 8.1(iv) (`l1_ode_check.py` / R1.0, `rho = dp/dq`):

```
rho * p * q' - p' * q = C_iv * p,    rho = 75/51 = 25/17,    C_iv != 0.
```

Derivatives are in `eta`. With `t' = 25 t / eta` the `eta` in `q` cancels,
and the equation is equivalent to the family-C identity (confirmed
specialization of T1-GEN)

```
E(t) := rho * Pfull * W + nu_F * rho * t * Pfull * W_t
                     - nu_F * t * Pfull_t * W  =  C_iv * Pfull.
```

No degree cap is imposed: `deg_t Pfull = 3` and `deg_t W = 2` are the
exact pattern degrees of this cell, so `E` has exact degree 5 before
cancellation.

### 3.2 Partial-fraction / coefficient form, solved

Dividing by `Pfull` (polynomial identity: `E - C_iv Pfull = 0`) gives the
explicit quadratic

```
C_iv(t) = rho (t-A)(t-B)
        + nu_F t [ (rho-2)(t-B) + (rho-1)(t-A) ].
```

Coefficient of `t^2`:

```
rho + nu_F (2 rho - 3) = 25/17 + 25(50/17 - 51/17) = 0
```

identically, because `rho = 3 nu_F / (2 nu_F + 1)` is the top-cancellation
law `rho = dp/dq` for this shape. The same vanishing holds for every
`nu_F >= 2` of the shape, independently of `(A,B)`.

Coefficient of `t^1`, the only remaining condition:

```
A ( rho + nu_F (rho-1) ) + B ( rho + nu_F (rho-2) ) = 0.
```

At `nu_F=25`, `rho=25/17`:

```
(225/17) A + (-200/17) B = 0,    hence  B/A = 225/200 = 9/8.
```

Closed form for the whole shape, recorded because it is the same linear
algebra and specialises to the printed suffix: `B/A = (nu_F+2)/(nu_F-1)`.
At `nu_F=7` this is `B = (3/2)A`, matching `SHEET6-TEMPLATE.md` §2b
(`F_s: B = (3/2)A unique`) and family C of `l1_ode_check.py`. Both linear
coefficients are nonzero, so the kernel is exactly one dimensional: unique
ratio, overall scale a gauge.

Constant term: `C_iv = rho A B`. At the integral gauge `A=8`, `B=9`,
`C_iv = 1800/17 != 0`. Generally `A=8u`, `B=9u`,
`C_iv = 1800 u^2 / 17 != 0` for `u != 0`.

Packet identity, second sparse `Poly` class: `E - C_iv Pfull = 0`
identically in `t` at `(A,B)=(8,9)`. Degree of the residual is `-1`.
Mutations detected: sign flip on `nu_F`; dropping the `Pfull_t` term;
wrong ratio `B/A=7/8`; coincident roots `A=B`; `A=0`. The identity was
also checked at eight other `nu_F` of the same shape against the closed
ratio, all exact.

### 3.3 R1.0 side conditions

- `A != 0`, `B != 0` from `C_iv != 0`.
- `A != B` because `9/8 != 1`, so `q`-roots simple and distinct.
- `rho != 2` and `rho != 1` (`25/17` lies strictly between), so the
  order-`mu` coefficient of 8.1(iv) at each `p`-root is nonzero.
- No zero-root factor in `p`. The only zero of `q` at `eta=0` is simple.

Cell verdict: **`TRUNK_T1_SURVIVES`**. No named source coefficient of this
reduced pattern is missing.

---

## 4. Attack 3 — solution shape, Statement 3.9, gauges

Complete reduced solution:

```
Pfull(t) = (t - 8u)^2 (t - 9u),    W(t) = (t - 8u)(t - 9u),
q = eta W,    C_iv = 1800 u^2 / 17 != 0,
```

`u` a unit in the `t`-coordinate. Unique invariant `B/A = 9/8`.

Printed Statement 3.9 (TEMPLATE §2a, on-page p. 15) applies per edge
`(shallow F, deep G = F+c)` to every sheet polynomial `p_h`:

1. `mult(p_{h,F}, c) = deg(p_{h, F*c})` when the count is exact
   (St 3.11(i) is the monotone weakening);
2. the leading coefficient of the deeper pattern equals the `mult`-th
   Taylor coefficient of the shallower one at `c`;
3. `d` drops by `mult/kappa` per elementary step.

Explicitly not printed, and not used: anything pinning sub-leading pattern
coefficients across edges.

The unique edge relating the merge to this trunk cell has shallow = dirty
vertex `F`, deep = merge `G`, and `c` = the chain-orbit root `A` of `p_F`.
Consequences:

- St 3.9 sees the chain root `A`, not an identification of
  `Rad_G = t_G^3 - A_star` with `(t_F - A)^2(t_F - B)`. The two
  `t`-coordinates are different (`eta_G^n` versus `eta_F^{25}`).
- Reduced degrees are not count-exact: `deg Pfull_G = 6n` versus
  `mult(Pfull_F, A) = 2`. St 3.9(i) is a sheet law, not a reduced-pattern
  law, and is not applicable to those two polynomials as written.
- St 3.9(ii) at this edge, on a named sheet, would relate the lead of
  `p_{h,G}` to the order-2 Taylor coefficient of `p_{h,F}` at `A`. For the
  reduced pattern that Taylor coefficient is a unit times `(A-B)`. That is
  a scale, i.e. the gauge `u`, together with monic/unit normalisation of
  `p_h`. It is not a second invariant besides `B/A`.
- The extra root `B` is a climbing northeast direction: gap `X/m - kbar = 8
  > 0`, so `F+B in T_a↗` (AF2). St 3.9 along that extra branch would relate
  `F` to an extra-branch child that the reduced cell does not construct.
  That is the first missing extra-branch jet, not a merge-`Rad` consumer.

Gauges versus a genuine shared coefficient:

| quantity | status |
|---|---|
| `B/A = 9/8` | genuine trunk-local T1 invariant |
| scale `u` of `(A,B)`, units of `p,q`, value of `C_iv` up to units | gauges |
| `A_star` in merge `Rad_G = t_G^3 - A_star` | genuine merge-local T1 invariant (Theorem E) |
| a numerical relation `A_star ↔ 9/8` | **not** forced by printed St 3.9 |

Local survival is not promoted to gluing, to a shared coefficient, or to
realizability of `{c_e^n}` as cube roots of one number.

---

## 5. Attack 4 — lambda floor/ceiling and slack one

P0/AF2 price of the unique northeast orbit: `gap = 25 - 17 = 8` exactly
an integer, so `lambda_F >= max(1, ceil(8)) = 8`. The exact value is
`kappa_H(pi(H)-1)` at the cv vertex `H` on the extra branch, which is not
a function of the reduced `(p,q)` cell. First missing object: that
extra-branch cv jet (subtop of the `B`-direction).

P1 on this terminal forces `Sigma lambda <= 9`. With merge and pole chains
at floor 0, a budget-fitting realisation of the displayed step has
`lambda_F in {8,9}`. Slack one is:

- **available** as a lower-bound remainder against the shared St 9.4
  ceiling;
- **not forced to zero** by T1 (no extra priced orbit, `eps=0`, `C_iv != 0`,
  no new printed unit);
- **not consumed** by the reduced solve.

A later extra-branch price of exactly one further unit still fits; a second
further unit kills the route. That is the inherited P0 honesty rider, not a
T1 kill.

---

## 6. Attack 5 — one-step menu, and consumers of the merge AP

The displayed cell survives, so a hunt for an alternative trunk path is
not required to decide the lead verdict. Completeness of the finite menu
actually used is still proved, and the prompt's residual question
(does another consumer vary with `n`?) is answered.

### 6.1 Complete cap-free one-step menu from `(9/2, 2)` at budget 9

R2 (passed at chain scope): extras-present dirty data are finite by
`E | l*num(w)*T`, `nu_F = (E-(l-eps))/C_P0 >= 2`, `k` bounded by remaining
budget, `lex` bounded by the printed `T>=1` / `E <= l a T` inequalities;
clean resonance is a finite divisor scan of `Delta | 9`; pure-epsilon is
an exact residue family. Restricting to one step from one state is that
finite scan. No numerical cap occurs. Legacy phantom divisors are not
emitted.

Result, packet-enumerated, 13 edges:

| family | count | notes |
|---|---:|---|
| clean-resonant | 0 | no `Delta \| 9` edge keeps `M>=2` (the claimed emptiness) |
| clean-neutral | 2 | `M' in {1,2}`, `w` fixed; `M'=1` is MP2-dead as interior trunk |
| pure-epsilon | 1 | `l=2, eps=1`, `w -> 9`, `M' = 1`, `lambda >= 9`, MP2-dead |
| dirty | 10 | exact `E`-divisor children |

Dirty P1-shaped children (`w<1`, `M>=2`, `j in N*`):

| `nu_F` | `k` | `(w,M)` | `lambda` | `psi` | own budget `12-1-psi` | fits? |
|---:|---:|---|---:|---:|---:|---|
| 25 | 1 | `(2/3, 3)` | 8 | 2 | 9 | **yes, slack 1** (charged) |
| 17 | 2 | `(3/4, 4)` | 8 | 3 | 8 | **yes, slack 0** (sibling, T1 not solved here) |
| 13 | 4 | `(5/6, 6)` | 8 | 5 | 6 | no |
| 11 | 8 | `(9/10, 10)` | 8 | 9 | 2 | no |

The charged cell is present. An independent hand scan of divisors of 54
for the charged discrete data `(l,k,Sm,lex,eps)=(2,1,1,0,0)` recovers
exactly `nu_F in {7,25}` (the `w=2`, `M=3`, cost-6 non-terminal, and the
charged terminal). Completeness of that pair is the divisor list of 54
together with `kbar in Z` and N1.

The sibling `(3/4,4)` is recorded as a second one-step P1-fitting reduced
edge. Its Prop. 8.1(iv) solve is not this charge (`k=2`, two extra orbits).
It is not used as a substitute trunk.

### 6.2 Dependence on the merge AP parameter `n`

`(w_tr, M) = (9/2, 2)` is constant on the whole admissible AP (Theorem B/C',
confirmed; packet: `n=5` and `n=13` give the same pair). The charged trunk
cell uses a **fixed** `nu_F=25`, independent of `n`. The ratio
`(nu_F+2)/(nu_F-1)=9/8` is therefore independent of `n`. The one-step P0
menu is a function of `(w,M,budget)` only.

A later consumer that *would* see `n` is St 3.9 sheet-count / lead
transport along the trunk edge, because `deg p_{h,G}` grows with `n`. That
consumer is not instantiated: it needs a named tower/`i` at `G` as a
function of `n`, it is not a reduced-pattern law, and printed St 3.9 does
not apply count-exactly to `Pfull_G` versus `Pfull_F`. It is not a kill at
this tier. Gluing of `{c_e^n}` to the three cube roots of one `A_star`,
for infinitely many admissible `n`, remains the coefficient/monodromy
rider, excluded from the combinatorial claim.

No full-`n` combinatorial kill of this first trunk consumer was found.

---

## 7. Narrowest maximum consequence

At recorded pattern / superset scope, the unique `td=12`, `m=3`, `[2,2,2]`
U1 family's displayed first trunk cell is Proposition 8.1(iv)-alive, with
unique reduced ratio `B/A = 9/8` and automatically nonzero right-hand
side. This particular downstream consumer does not kill the family, and it
does not vary with the merge AP parameter. Exact extra-branch lambda lies
in `{8,9}` if the route is to remain St 9.4-fitting; slack 1 is a
lower-bound remainder, not a theorem of equality. The sibling one-step
terminal `(3/4,4)` is a second reduced option, unused here.

This does not prove the cell is realized by an `(f,g)`, does not glue
`t^3 - A_star` to `B/A = 9/8`, does not close the `td=12` panel, does not
bound `td`, and does not touch JC2. Alive is not existent (R4).

---

## 8. Single best next lemma

Pin the extra-branch cv jet of the unique northeast orbit at this cell
(the `B`-direction, gap 8): either `lambda_F = 8` exactly, or a printed
unit forces `lambda_F >= 9` (still fitting) or `>= 10` (kills the route).
That is the first missing subtop, and it is the only remaining local
unknown that can still spend the slack.

Do not spend a desk day re-solving the reduced T1 identity on this cell.
Do not identify `9/8` with `A_star` from printed St 3.9. A parallel
object, not this charge, is T1 on the sibling `k=2` cell
`(nu_F, dp, dq)=(17, 68, 52)`.

---

## 9. Scope firewall

This report does not assert: a landing theorem; completeness at any `td`;
restoration of a prime-`td` exclusion; realizability of any cell or family;
gluing / monodromy of `t^3 - A_star`; an extra-branch tower; a cofinal
bound on `td`; `G2-BD`; `G2-PSC`; or any JC2 consequence. It does not
access `jc2-lean`. It does not change panel status: `BOOK-OFFAXIS.md` §4
already records `td=12` composite as open.

---

## 10. Replay

Commands, ordinary and `-O`:

```sh
cd cases/m2_td12_u1_trunk_consumer_grok46_20260829
python3    test_trunk_consumer.py
python3 -O test_trunk_consumer.py
python3    trunk_consumer.py --emit /tmp/td12_u1_trunk.json
python3 -O trunk_consumer.py --emit /tmp/td12_u1_trunk-O.json
cmp /tmp/td12_u1_trunk.json /tmp/td12_u1_trunk-O.json
python3    trunk_consumer.py --cap 10
python3    trunk_consumer.py --max_nu 40
```

Observed:

```
TD12_U1_TRUNK_CONSUMER_TEST_PASS checks=134
TD12_U1_TRUNK_CONSUMER_TEST_PASS checks=134
lead_verdict FAMILY_SURVIVES_FIRST_TRUNK
cell_verdict TRUNK_T1_SURVIVES
ratio_B_over_A 9/8
C_iv 1800/17
step_count 13
dirty_count 10
fitting_P1 [(2/3,3, nu_F=25, k=1), (3/4,4, nu_F=17, k=2)]
payload_sha256 995f67e9b4e6bc69414ec2454ed532639f09d06ee924669600ebffe1cf4b81fc
CMP_OK
CAP_TOKEN_REJECTED:cap
CAP_TOKEN_REJECTED:max_nu
```

Packet principal hashes, this session:

```
e363b697323e63c4257bf3050b4e0b1bd8aa9af5705918f4aef63eb995eaa0da  polyexact.py
6f214a755e1d589bacf155195e687799b8f793706a5ca2fa7cb508c00a038d7e  trunk_consumer.py
57a948dedd6fdd589a910ae23b836f2b3a1b790a6826a0ffdde15f79a373ff41  test_trunk_consumer.py
d117ef7554e5e0221302944515d7c2cac2f11accb1d00be34be55ed09879c4c6  README.md
b047c364d4af796eae6fea2b54ffe45074863206e8a60425e1f77555bdfa626e  /tmp/td12_u1_trunk.json
```

Cap tokens were not accepted. Files written: this path and the uniquely
named packet. Scratch under `/tmp` only.

**Verdict: `FAMILY_SURVIVES_FIRST_TRUNK`.**

---

*Report body ends. The seal below covers everything above this line.*

report_body_sha256 = ea43c28125b61710d1af58a90de1928a7c05f93734950c6d89814cd3c99d5be2
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 19082 bytes)
