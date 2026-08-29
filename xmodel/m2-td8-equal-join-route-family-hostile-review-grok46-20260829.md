# Hostile review — Sol 56 fixed-entry td=8 equal-join affine family

Lane: Grok 4.6, different-model adversarial referee.
Target report: `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`.
Packet: `cases/m2_td8_equal_join_route_family_r1_20260829/`.
Comparison sources only: `cases/book_offaxis.py` `census` / `l6_pole_ok`;
`cases/book_enum.py` `entries` / `tdu_rows` / `w0_of`;
`ladder/BOOK-OFFAXIS.md` §§1, 6 R1.0–R1.4, 7 R2.1–R2.2, 10 P0–P2;
`ladder/SHEET6-DEPTH.md` §§1–2 DS1 and the i-normalized frames;
`ladder/SHEET6-MULTIPOLE.md` MP1–MP2, MP4, MP6(b) as cited;
`ladder/SHEET6-AF2.md` §§1–2 (corrected St 9.3(24) gap rule);
`ladder/SHEET6-H3.md` §3 St 9.4 (25) and §4a H3-psi;
`ladder/REDUCTION.md` T8/T9 notes on St 9.4 and CRITICAL 4–5;
and the prior Grok report
`xmodel/m2-budget-quotient-primary-research-opus5-hostile-review-grok46-20260829.md`
used solely as a named D2-scope crosswalk, never as authority.

The family is tested against those book laws. Agreement with the prior
D2 recipe is not evidence.

No access of any kind to `jc2-lean`. No web, AWS, heavy/local CAS,
canonical edit, git status, commit, or push. Arithmetic is desk
`int`/`Fraction`. Packet and producer report were not modified.
Mutations ran in a throwaway directory.

Nothing here claims landing, a type ceiling, realizability, an exact
lambda cost, Prop. 8.1(iv), T1 on this off-class family, or JC2.

---

## 0. Custody

Full-file SHA-256 of the target, 5,623 bytes:

```
9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a
```

matches the brief.

Body hash of the first 5,491 bytes (through and including the newline
before the separator `---` above the report's own body-hash line):

```
bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7
```

matches the brief and the report's own `Report-body SHA-256` line.

Packet hashes, independently recomputed:

```
48d1288e9235fa9a079b7a9b29d9c10b3800454d6bdb4c557165fae89dea4a94  td8_equal_join_route_family_r1.py
dccd335edebc9bb2d329df9c95da8e27265e5a7e6f705f6cadbe3d3b257b72c4  test_td8_equal_join_route_family_r1.py
69e3d1ea1f4951f963f48354dc8d0f7eb811eebb3969798ab4375b092cdaeae4  README.md
2cb4eddcda8feeb89d766dcfcfa6c712adce5b81939c3d8d1237e4c15cb483e2  charged JSON stdout
```

match the report. Prior Grok review full-file
`5192c007536cc2b36e813c23ab16b9badba85d61bec6a56646d561c0f1ff4bfa`
and body `7af0e75fb1b62dd9394fd60f63de1bbbb6e5b76526f025eb4b4e393aa27506ed`
match the brief.

Licensed comparison sources were read in the sections named above.

---

## 1. Verdict

**`PASS_AT_RECORDED_BOOK_SCOPE`**

The unique off-axis `td=8,m=2` entry, both `(4,1,2,3)` poles, the printed
P0 `(A)` step `(21,15)` with recorded lambda lower bound two, the affine
equal-`(mu,w)=(3,2/3)` merge family indexed by `t>=0`, the parent-dependent
trunk label `22+17t`, the full case-II proportion/frame equations, MP2, and
the terminal `j=3, psi=1` law all reproduce from the current book grammar.
The recorded lower-bound sum is six and meets `td-1-psi` at equality; that
is a filter survival, not an exact-cost theorem. Affine identities, not the
10,001-point scan, prove infinitude of full cells with one reduced successor
`(w,M)=(4/3,3)`.

No omitted zero-slot, `nu_G>=2`, E5/H5a, or i-normalization premise makes
the family ill-typed. MULTIPOLE §4 remains open as a mixed-merge
*completeness* statement; it is not a typing ban on this R2.1/R2.2 cell.

---

## 2. Referee baseline

Frames as in DEPTH §1 / R1 / P0: `w=(kbar-rho)/nu`, `rho=D/deg(p)`
i-normalized, `M=gcd(dp,dq)`, `E=l*dq-dp` on a chain edge of arrival
mult `l`. Pattern degrees `dp=eps+nu*(l+Sm)`, `dq=1+nu*(1+k+lex)`.

- Census: off-axis iff some `b_i>=2`; L6 `gcd(a(alpha+beta),nu)=1`; MP4
  `M_i=b_i`. Engine: `book_offaxis.census`.
- P0 transport: `kbar=l*w_parent*dq/E in Z` at `nu>=2`,
  `w_child=l*w_parent*(dq-1)/(nu*E)`, `M_child=gcd(dp,dq)`, `l | M_parent`.
- P0/AF2 price (lower bound): for each extra orbit of reduced multiplicity
  `m_j`, `lambda >= max(1, ceil(X/m_j - kbar))`, with
  `X=kbar*dp/dq` and gap `X/m_j-kbar` the corrected St 9.3(24) quantity
  `D/(i*mult)-kbar`. A free 0-root adds the `nu`-discounted term. Clean
  `eps=k=0` costs 0. The simple-orbit specialisation `k*ceil(X-kbar)` is
  *not* the general rule.
- P1 / H3-psi / St 9.4(25): one shared budget over pairwise-distinct
  searrow vertices; `psi=ceil(1/(1-w))-1=ceil(M/j)-1` at the last searrow
  vertex above `(0,y)`, with `j=M(1-w) in N*` and `w<1`;
  `sum lambda <= td-1-psi`.
- P2: merge extras/free 0-roots price as P0; arriving edges and `lex`
  q-extras price 0. Arrival `mu | M_H`. Explicit licence: `mu=3` may leave
  the `(21,15)` cell at `nu_H=7`.
- R1.0 / R2.2: `dq ≡ 1 (mod nu)`, `gcd(M,nu)=1`, searrow `mu_e*dq>dp`,
  root-mult `dp != mu*dq`. T-law `M | P-s*eps`. At `eps=k=0`,
  `T=sum mu_e` and `M | sum mu_e`.
- R1.4 / R2.1 case I/II: `n_e=nu_parent*kbar_child-kbar_parent in N*`,
  `X=mu*(kbar-w)` on a nonzero arrival,
  `(rho_parent+n):(kbar_parent+n)=dp:(l*dq)` across a dirty child.
- DS1(a)–(d): at `nu>=2`, vertex in `V_{1,a}`, `kbar in Z`, chain edges
  case II. `nu=1` is not this typing.
- MP1: `sum(r-1)=m-1`. MP2: interior trunk and `G*` have `M!=1`.
- T1 of BOOK-OFFAXIS §11 is a closed form for Prop. 8.1(iv) on the `td=7`
  class-B/C book. It is not a vertex-local law of this off-class family.

---

## 3. Charge 1 — unique header, both poles, `(21,15)`, lower bound two

`book_offaxis.census(tdmax=8)` returns a single off-axis L6 survivor at
`(m,td)=(2,8)`:

```
type (alpha,beta)=(2,3), poles = ((4,1,2,3),(4,1,2,3)).
```

`m` ranges only to `floor(td/3)=2`, so there is no `m=3` row. Raw count
1, L6 count 1. `book_enum.entries(8,2)` also contains the on-axis twin
`(3,4)` with both `b=1`; the off-axis filter drops it. Headline in
BOOK-OFFAXIS.md §1 (`td8 m2: [2,2]`) matches.

Independent pole arithmetic, type `(2,3)`:

- `Lambda = a b alpha beta / nu = 1*2*2*3/3 = 4`.
- `tdu_rows(4)` supplies the `(2,3)` row `(D,deg p,nu)=(2,4,3)`, hence
  `(a,b,nu)=(1,2,3)`.
- L6: `gcd(a(alpha+beta),nu)=gcd(5,3)=1`.
- Entry frame: `kbar_0=a(alpha+beta)=5`, `rho_0=a/b=1/2`,
  `w_0=(5-1/2)/3=3/2`, `M_0=b=2`. Same from `w0_of`.

Both poles are identical, so both chains start at `(w,M)=(3/2,2)`.

P0 `(A)` step, independently expanded:

```
l=2 | M_parent, nu=7, eps=0, k=1, Sm=1, lex=0,
dp=0+7*(2+1)=21, dq=1+7*(1+1+0)=15, E=2*15-21=9,
kbar=2*(3/2)*15/9=5, X=5*21/15=7, rho=5/15=1/3,
w=2*(3/2)*14/(7*9)=2/3, M=gcd(21,15)=3.
```

`(kbar-rho)/nu=(5-1/3)/7=2/3` recovers `w`. Unique extra: `k=1` forces
one extra orbit, `Sm=1` forces multiplicity one. Pattern uniqueness at
`nu=7`: `k+lex=1` and `eps+7 Sm=7` give only `(eps,Sm)=(0,1)` or `(7,0)`;
the second violates either `k<=Sm` or 0-root northeast (`7*15>21`). One
legal pattern. AF2/P0 price `max(1, ceil(7/1-5))=2`. This is the printed
St 9.6(iii) `(A)` badge (`lambda >= 2 = X-kbar` on `(X,kbar)=(7,5)`),
already named in P0's one-step menu from `(3/2,2)`.

Among that printed four-escape menu, only `(A)` yields odd `den(w)` and
`M>=2`. `(C)=(20,16)` has `w=3/4`; pure-`(b)` and `eps=(7,5)` land `M=1`
(MP2-dead on any interior trunk) or even `den(w)`. Neutrals at the entry
preserve `w=3/2` (`den=2`), so they cannot instantiate an equal-`(mu,w)`
join at `nu>=2`. The `(A)` step is therefore the unique printed one-step
producer of a legal host `w` for this family; that is a book fact, not a
discriminator-recipe fact.

---

## 4. Charge 2 — the affine merge family, every `t>=0`

Set `mu=3`, arrival `w=2/3` (so `mu | M_H=3`), `eps=k=lex=0`, two nonzero
arrivals, `r0=2`. Then

```
nu_G=4+3t, dp=2*mu*nu_G=24+18t, dq=2*nu_G+1=9+6t,
E_e=mu*dq-dp=3, kbar=w*dq=6+4t, X=mu*(kbar-w)=16+12t,
rho=X/dp=2/3, M=gcd(dp,dq)=3, w_tr=(kbar-rho)/nu_G=4/3.
```

Closed identities, checked symbolically and on `t=0..49,100,1000,10^6`:

| law | identity |
|---|---|
| degrees | `dp=24+18t`, `dq=9+6t` |
| ratio | `X/kbar=dp/dq` |
| reduced successor | `(w_tr,M)=(4/3,3)` constant |
| T-law | `P=6`, `s=2`, `eps=0`, `T=6`, `M=3 \| 6` |
| `gcd(M,nu_G)` | `gcd(3,4+3t)=1` |
| R1.0 | `dq=2 nu_G+1 ≡ 1 (mod nu_G)` |
| (S) | `3 dq - dp = 3 > 0` |
| (R) | `dp != 3 dq` |
| MP2 | `M_G=3 != 1` |
| `M=gcd(6 nu, 2nu+1)` | `2nu+1=9+6t`, so `gcd=3` identically |

Integrality `kbar in Z` at `nu>=2` is `3 | 2 nu+1`, i.e. `nu ≡ 1 (mod 3)`.
The residue class is `1`, not `4`; the report's phrase "`nu_G=4 mod 3`" is
the arithmetic progression starting at 4, which is exactly the `nu>=2`
slice of that class. Neighboring classes `nu ≢ 1 (mod 3)` never have
integral `kbar` (checked `nu=2..79`). The point `nu=1` (`t=-1`) is
integral (`kbar=2`) but is excluded by DS1(a)/Not 3.4 (`nu=1` is not
`V_{1,a}`, so case II is not licensed). The claimed family `t>=0` is the
correct slice, not an omitted-member hole.

Incoming case-II labels, both edges, parent the `(21,15)` frame
`(nu,kbar,rho)_H=(7,5,1/3)`:

```
n_e = 7*(6+4t)-5 = 37+28t >= 1    (t>=0),
(kbar_H+n_e)/nu_H = (5+37+28t)/7 = 6+4t = kbar_G,
3*(rho_H+n_e)/nu_H = 3*(1/3+37+28t)/7 = 16+12t = X_G.
```

Equal `(mu,w)` makes R2.1(i) consistent: both edges write the same `X`.
R2.1(ii) does not fire. Both labels are the same affine function because
both incoming frames are the same; that is required, not an omitted
asymmetry. P2's written example is this arrival: `mu=3` at `nu_H=7`
directly from the `(A)`-cell.

Typing audit, as charged:

- **Zero-slot.** `eps=0`, no 0-arrival. MP1 for `m=2` is one 2-ary merge;
  a 0-edge is a different arrangement, not a missing slot in this one.
  E5/H5a pin a 0-edge and do not apply.
- **`nu_G>=2`.** `4+3t >= 4`. DS1 and case II are in force.
- **Nonchain / q-extra.** `k=lex=0`. `(S)` on extras is vacuous. `dp>dq`
  is the family-6a slope (`6 nu > 2 nu+1`) and does not violate arrival
  searrow.
- **i-normalization.** R2.1 uses `deg(p_H)=i_G mu_e`. Two arrivals of
  `mu=3` give reduced `dp=6 nu`, matching `eps=k=0`. DEPTH's all-`mu=1`
  MP6(b) sentence is not the licence; R2.1 plus P2's `(21,15)` arrival
  law is. No extra i-premise is missing.
- **Omitted arrangement.** The family is an existence statement, not a
  census of all `td=8` merges. Neutrals after `(A)`, the `(C)` jump, a
  0-arrival, or unequal `mu` are other objects. None of them is required
  to type *this* cell.
- **MULTIPOLE §4.** Mixed all-`mu>=2` completeness remains open. R2.1–R2.2
  still type the equal-`(mu,w)`, `eps=k=0` cell (R2.3(ii) `l=0` arithmetic
  with the odd-denominator constraint). Open completeness is not
  ill-typedness.

The family is well-typed in the recorded book grammar.

---

## 5. Charge 3 — trunk `(85,35)` and parent-dependent `22+17t`

Interior merge `w_tr=4/3>=1` cannot be a P1 terminal (`w<1`). Trunk
arrival `l | M_G=3`, and `l=3` is the only `l>=2` option. Fixed P0 step
from `(w,M)=(4/3,3)`:

```
l=3, nu=17, eps=0, k=1, Sm=2, lex=0,
dp=17*(3+2)=85, dq=1+17*(2)=35, E=3*35-85=20,
kbar=3*(4/3)*35/20=7, X=7*85/35=17, rho=7/35=1/5,
w=(7-1/5)/17=2/5, M=gcd(85,35)=5.
```

Pattern uniqueness at `nu=17`: `k+lex=1` and `eps+17 Sm=34` give
`(eps,Sm)=(0,2)`, `(17,1)`, `(34,0)`; only `(0,2)` has a northeast 0-root
test that does not fail, and `k=1<=Sm=2<=k*(l-1)=2`. One extra orbit of
multiplicity two. Northeast `2*35=70<85`. Own-edge searrow `E=20>0`.
Root-mult `85 != 3*35` and `85 != 2*35`. P0 divisor `E | l num(w) T` with
`T=Sm+l=5` is `20 | 60`.

Parent-dependent label, merge as parent:

```
n_F = nu_G * 7 - kbar_G = (4+3t)*7 - (6+4t) = 22+17t >= 1.
```

Full frame, not merely the reduced successor, for every `t>=0`:

```
(kbar_G+n_F)/nu_G = (6+4t+22+17t)/(4+3t) = 7 = kbar_F,
(rho_G+n_F)/(kbar_G+n_F) = (2/3+22+17t)/(28+21t) = 17/21
                         = dp_F/(l*dq_F) = 85/(3*35).
```

Companion R2.1 X-handshake, not displayed in the report and checked here:

```
X_F = l*(rho_G+n_F)/nu_G = 3*(17/3) = 17.
```

AF2 *general* gap on the multiplicity-two extra is `17/2-7=3/2`,
`ceil=2`. The simple-orbit template `ceil(X-kbar)=10` is the wrong rule
and would kill the budget; the packet uses the general gap. Recorded
trunk lower bound two is therefore the P0/AF2 number, not an underprice
relative to the printed simple-orbit slogan.

Terminal P1/9.3(m):

```
j = M(1-w) = 5*(3/5) = 3 in N*,
psi = ceil(M/j)-1 = ceil(5/3)-1 = 1
    = ceil(1/(1-w))-1.
```

`w=2/5<=1/2`, so `psi=1` and the ceiling is `td-2=6`, matching P1's
near-half-window clause. MP2: trunk `M_F=5 != 1`, merge `M_G=3 != 1`.
The last searrow vertex above `(0,y)` is the trunk vertex, not the merge;
evaluating `psi` at `w_tr=4/3` would be illicit and is not done.

---

## 6. Charge 4 — budget semantics

Recorded lower bounds:

```
two incoming (A)-steps  2+2
merge (no extras, no free 0-root; P2 arriving edges price 0)  0
trunk (A)-style extra of multiplicity 2  2
sum  6
psi=1,  td-1-psi = 8-1-1 = 6.
```

The merge 0 is exact under P2 (nothing to underprice). The three 2's are
AF2 ceilings, hence lower bounds. Charge 4's only allowed statement:

> the recorded lambda lower bounds total six, and therefore every family
> member survives the printed budget filter at equality

is **CONFIRMED**. St 9.4(25)/P1 compares a *sum of lambdas* to
`td-1-psi`. The printed off-axis filter uses the P0/P2 recorded floors
(BOOK-OFFAXIS §10: the direct list is a superset along in-budget paths).
`sum LB = ceiling` means the filter does not kill the route. It means
each actual lambda must *equal* its floor for the configuration to remain
budget-legal. If any actual climb strictly exceeds its ceiling, the true
sum exceeds 6 and St 9.4 kills the route.

The report does not upgrade that. Explicit non-upgrades:

- Result: "terminal lambda-budget **lower-bound filter** at equality";
- "recorded lambda values are lower bounds, not proved exact costs";
- "not a proof that the true lambda cost equals its recorded lower bound";
- packet keys `lambda_lower_bound*`, verdict
  `RECORDED_LOWER_BOUND_BUDGET_FITTING_SUPERSET_ALIVE`;
- firewall `configuration_realizable: false`.

Diction that can be *misread*, but does not change the claim: "priced
chain steps", "budget-fitting **superset-formal** routes", "is reached
by". In context those are grammar-reachability and the recorded filter,
not exact costs or polynomial realizations. No repair is required.

---

## 7. Charge 5 — tests, mutations, infinitude

Ordinary and `-O` suites each print
`TD8_EQUAL_JOIN_ROUTE_FAMILY_R1_TEST_PASS checks=80097`. Check census:
3 (fixed step) + `10001*8` (family box) + 78+2 (integrality / distinctness)
+ 5 (certificate/`-O` identity) + 1 (invalid `t`) = 80,097. Charged JSON
stdout hash matches. Certificate firewall flags are all `false`.

Independent `/tmp` mutations of the producer, packet untouched:

| mutation | result |
|---|---|
| `nu_G=5+3t` (wrong residue) | `merge kbar is not integral` |
| incoming label `+1` | `incoming kbar handshake mismatch` |
| trunk label `+1` | `trunk edge-label progression mismatch` |
| terminal `(w,M)` forced to `(3/5,5)` | `trunk terminal mismatch` |
| `kbar_G=w*dq+1` | `merge ratio mismatch` |

Infinitude is the affine identities, not the scan. For every integer
`t>=0`,

```
2 nu_G+1 = 9+6t = 3(3+2t),
kbar = (2/3)*3(3+2t) = 6+4t,
n_e = 37+28t,  n_F = 22+17t,
(dp,dq,kbar) = (24+18t, 9+6t, 6+4t)
```

are strictly increasing, hence infinitely many distinct full cells, while
`(w_tr,M)=(4/3,3)` is constant. The 10,001-point loop is a regression
battery, as the report already states. A finite scan cannot prove, and
is not being asked to prove, the `t` theorem.

---

## 8. Charge 6 — exact consequence for M2

A PASS at this scope establishes:

1. an infinite family of full formal merge cells at the unique off-axis
   `td=8,m=2` entry, inside the recorded P0/P1/P2 + R1/R2 + DS1 + MP2
   grammar;
2. one reduced merge successor `(4/3,3)`;
3. that a numerical `kbar` cap cannot be the completeness mechanism for
   the *cell* book at this entry;
4. that a semilinear (arithmetic-progression) record is necessary if the
   cell book is to be compiled.

It does **not** establish: Prop. 8.1(iv) or a T1-style closed form on this
off-class family; exact lambda costs; source landing; geometric
realizability of any member; a degree ceiling; completeness of all `td=8`
merges; or JC2.

The reduced-state quotient at this entry may still be finite (`M | T=6`
already bounds `M_G`, and `w_tr` is constant). Cell-infinitude with
reduced-finiteness is exactly why quotienting is necessary and why a
finite reduced menu does not give a finite cell list. That is a
book-scope combinatorial fact, independent of who first named D2.

Next exact obligation, not discharged: the parametric Prop. 8.1(iv) / log
equation in `t` on this family, then a uniform obstruction, a finite
exceptional set, or an explicit formal survivor. Keep lambda-exactness,
landing, and realizability as separate gates.

---

## 9. Findings, severity order

No CRITICAL, HIGH, or MEDIUM refutation of the stated theorem at recorded
book scope.

**LOW (diction only, not a math error).** "The progression `nu_G=4 mod 3`"
names an arithmetic progression whose residue is `1 mod 3`. The formulae
are the correct progression.

**LOW (diction only).** "Reached by" / "priced chain steps" can be read as
exact cost or geometric reachability. The surrounding lower-bound and
firewall sentences prevent that reading. Not an upgrade of the claim.

**NOTE, not a defect.** `nu=1` (`t=-1`) continues the same identities
arithmetically and is correctly excluded by DS1(a). Zero-slot, E5/H5a,
and extra i-normalization premises are not required. T1 is not cited.

---

## 10. Clause-by-clause ledger

| item | verdict |
|---|---|
| Hash pair of the Sol report | CONFIRMED |
| Packet four-hash list, including charged JSON | CONFIRMED |
| Unique `td=8,m=2` off-axis header, type `(2,3)` | CONFIRMED |
| Both poles `(Lambda,a,b,nu)=(4,1,2,3)`, `w_0=3/2`, `M=2` | CONFIRMED |
| P0 `(A)=(21,15)`, frame `(kbar,X,rho,w,M)=(5,7,1/3,2/3,3)` | CONFIRMED |
| Unique extra of multiplicity one; recorded LB `=2` | CONFIRMED |
| Affine merge family as displayed, all `t>=0` | CONFIRMED |
| Degrees, `M=3`, T-law, `gcd(M,nu)=1`, (S)/(R), R1.0 | CONFIRMED |
| Integrality `nu ≡ 1 (mod 3)`; AP starts at 4 for `nu>=2` | CONFIRMED |
| Both incoming labels `37+28t`; both handshakes | CONFIRMED |
| Zero-slot / E5 / H5a omitted-premise ill-typedness | ABSENT |
| i-normalization / case-II typing | CONFIRMED |
| MULTIPOLE §4 completeness used as a typing ban | NOT DONE (correct) |
| T1 applied off-class | NOT DONE (correct) |
| Trunk `(85,35)`, frame `(7,17,1/5,2/5,5)`, LB `=2` | CONFIRMED |
| Parent-dependent `n_F=22+17t` and full proportion | CONFIRMED |
| Companion trunk X-handshake `X=l(rho_G+n)/nu_G` | CONFIRMED (extra) |
| MP2 at merge and trunk | CONFIRMED |
| Terminal `j=3`, `psi=1`, ceiling 6 | CONFIRMED |
| Recorded LB total 6; filter survival at equality | CONFIRMED |
| Upgrade of LB to exact cost or actual configuration | ABSENT |
| Ordinary/`-O` 80,097 checks | CONFIRMED |
| Affine identities prove infinitude; scan is regression | CONFIRMED |
| One reduced successor `(4/3,3)` | CONFIRMED |
| Prop. 8.1(iv) / landing / realizability / JC2 claimed | ABSENT (firewall held) |

---

## 11. Scope firewall and replay

This review does not assert: a landing theorem; completeness at `td=8`;
exact lambda; realizability of any cell; a solution of Prop. 8.1(iv) on
the family; restoration of a prime-`td` exclusion; a cofinal bound on
`td`; or any JC2 consequence. It does not access `jc2-lean`. It does not
promote the family off the recorded superset tier.

- Files read: the four paths named in the brief, plus the ladder/engine
  sections named in the header.
- Files written: this path only. Packet and producer report untouched.
- Compute: `book_offaxis.census(tdmax=8)` and `book_enum.entries/tdu_rows`;
  desk `int`/`Fraction` reconstruction of header, P0 menus, affine
  identities, trunk frame/proportion/X-handshake, P1/psi; ordinary and
  `-O` packet tests; charged JSON hash; `/tmp` mutations of progression,
  both edge labels, and terminal. No engine beyond those imports, no CAS,
  no `jc2-lean`.
- Blindness: no ideation bodies; prior Grok D2 text used only as a
  named crosswalk.

**Verdict: `PASS_AT_RECORDED_BOOK_SCOPE`.**

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = a53a78dbabaaa6f1c2a30247ad016b99bf2d2011132736a2e8b7c5f098552c49
(sha256 of this file up to and including the line "*Report body ends. Self-hash below covers everything above this line.*", i.e. of the first 20342 bytes)

Full-report SHA-256 is the hash of the complete file bytes, including this appendix. Compute with:

```
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md').read_bytes()).hexdigest())"
```
