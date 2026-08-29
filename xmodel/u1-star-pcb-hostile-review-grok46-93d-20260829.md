# Hostile review — pole-inflated U1 star family and PCB

Lane: Grok 4.6, different-model adversarial referee.
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125` (verified
`git rev-parse HEAD` at session start).
Target: `xmodel/td12-occurrence-coverage-attack-opus5-93d-20260829.md`.

No web, AWS, heavy local CAS, commit, push, canonical edit, or external
message. `jc2-lean` was never read, listed, stat'ed, grepped, built,
modified, or touched. Arithmetic is desk `int`/`Fraction` under `/tmp/u1pcb`.
No new exit price is asserted.

---

## 0. Two verdicts

The claims are independent. Killing one does not promote the other.

**Claim A (`U1*(r)`, interface no-go). CONFIRMED, as a statement about the
recorded configuration interface, not as occurrence or realizability.**

For every odd `r >= 3` the enumerated axiom list `Sigma_cfg` admits an
abstract type-`(2,3)` star of arity `r` with all poles `(a,b,nu)=(1,2,3)`,
`td=4r`, equal U1 arrivals `(mu,w)=(2,3/2)`, and at least the `k=1`
one-step dirty P1 terminal

```text
nu_F = 9r-2,  M_F = 3,  w_F = 2/3,  j = 1,  psi = 2,
lambda_floor = 3r-1,  budget = 4r-3,  slack = r-2.
```

The full one-step P1-fitting dirty terminal family is exactly the stated
divisor law: `k | 3r-1`, `k <= r-1`, with

```text
nu = 3r + 2(3r-1)/k,  M = k+2,  w = (k+1)/(k+2),
psi = k+1,  lambda_floor = 3r-1,  budget = 4r-k-2.
```

Zero extra budget-fitting P1 terminals exist outside that list for odd
`r` in `[3,59]`. Local T1 is independently solvable on every `k=1` cell.
No omitted promoted configuration-level axiom and no illegal quantifier
kills the family. Therefore `Sigma_cfg` does not entail `td=12` and does
not entail any `td` ceiling. The object is formal: no Keller pair, no
`PairRef`, no actual occurrence, no attainment.

**Claim B (`PCB`). FALSE/UNSUPPORTED.**

The fibrewise Riemann-Hurwitz identity

```text
sum_{non-pole infinity places}(e_F-1) = 2g-2+d+s
```

is correct and is not the issue. The proposed pole-cluster Euler
decomposition that would turn it into `d >= s + sum wt` is false as a
reading of promoted Section 7, and is forbidden as a flag/place/series
identification. The constant `1` in repaired Corollary 7.1 is
`chi_c(A^2)=1`. Pole clusters of `g` are not points of the finite-value
quotient lines `U_i` and cannot change that Euler characteristic. RH
ramification is a strictly larger quantity than the flag-weight sum in
the counterexample regime, so it cannot be typed to `sum wt`. PCB is
not a duplicate of Corollary 7.1. It is not promoted. That it would
kill `U1*(r)` is irrelevant.

---

## 1. Custody

Full-file SHA-256 of the target, 51927 bytes:

```
acd21ced9c2569b46b9f2123e9a7e106c552e62983eebb4408e4ddce32581f5c
```

Body = every byte through the unique `<!-- BODY-END -->` line, including
its terminating newline: 51552 bytes, SHA-256

```
19d15346303d23f10fdf3bae0fc153396434e4e8835585d063e98e3d6c95947d
```

matching the target's own seal.

Load-bearing sources, recomputed this session before use:

```
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
8755bd5d3d1cd2721d32e5956c5b139b2cc6e0e805662d5278ededff896135ba
  xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md
f9dd2035bbe5a47561cce263ba1288a9245526dec748c3ef031545e443bf510f
  xmodel/m2-u2-one-p0-source-mass-floor-hostile-review-fable5-c359-20260829.md
b7f07776e30f912fc6cce4b490f9936c139d1b73eaa7f69c73e1f23153d3a71e
  xmodel/td12-u1-first-nonneutral-quartet-detour-analysis-sol56-93d-20260829.md
```

Also read, in the sections cited below: `ladder/BOOK-OFFAXIS.md` R1.3–R1.4
and P0–P1; `ladder/SHEET6-MULTIPOLE.md` MP0–MP8 and D6; `ladder/SHEET6-H3.md`
§4a; `ladder/SHEET6-2POLE.md` header verdict; `cases/l1_ode_check.py` family C;
FALLACY-v2; Proposition 5.1 sidedness as recorded in the every-fibre
Proposition 5.8 audit. Producer hashes of `ladder/REDUCTION.md` /
`ladder/TRANSPORT.md` were not re-opened: Claim A is an interface soundness
statement about `Sigma_cfg` as written in the target, not a re-audit of
those two files.

---

## 2. Claim A — independent recomputation

Notation split, used throughout: merge index `n` is `nu_G`; trunk index
is `nu_F`; pole index is `nu_P=3`. These are three different objects.
FALLACY-v2's target/arrival-index rule is respected. Every `lambda` below
is the consumed AF2/`P0` floor (`REPRESENTATIVE`). No
`FULL_ACTUAL_EXIT` / `FULL_ACTUAL_FIRST_SEPARATION` attainment is claimed
or used.

### 2.1 Entry

Type `(alpha,beta)=(2,3)`, `gcd=1`. Pole `(a,b,nu)=(1,2,3)`:

```text
Lambda = a b alpha beta / nu = 6/3*1*2 = 4,
M_P = b = 2,
w_0 = a(b(alpha+beta)-1)/(b nu) = (2*5-1)/6 = 3/2.
```

Case (B): `nu | beta` and `nu | b*alpha-1`, i.e. `3|3` and `3|3`.
`Lambda >= beta`. L6: `gcd(a(alpha+beta),nu)=gcd(5,3)=1`. Mass `td=4r`.
Bound `s=r <= td/beta = 4r/3` holds for every `r>=1`.

The only other `Lambda=4` row at type `(2,3)` is on-axis `(a,b,nu)=(2,1,3)`,
`M_P=1`, `w_0=8/3`. Off-axis uniqueness of `(1,2,3)` is confirmed. The
target's displayed second equality for `w_0` drops the explicit factor
`a=1`; the value is correct.

`(A1)--(A4)` hold for every odd `r>=3`.

### 2.2 Tree and merge

Star: one merge `G` of arity `R=r`, all `r` pole paths of length zero (or
clean-neutral interpolations of price zero; see 2.8), arrivals
`mu=2 | M_P=2`, `eps=k=lex=0`, equal `w_e=3/2`. MP0/MP1: one merge,
`sum(R-1)=r-1=s-1`. St 8.4 holds.

Theorem B, independently substituted at `(r,mu,eps,w)=(r,2,0,3/2)` with
merge index `n`:

```text
dp = 2 r n,     dq = 1 + r n,     E = 2,
kbar = 3(1+r n)/2,   X = 3 r n,
w_tr = 3r/2,    M = gcd(2, r n + 1),
T = 2r,         lambda_G = 0.
```

Handshake `X_G = mu_e(kbar_G - w_e)` is the identity `3 r n = 2*(3 r n / 2)`.

MP2 forces `M>=2`, i.e. `r n` odd. For integer `n`, this is possible if and
only if `r` is odd. Even `r in {2,4,6,8}` is MP2-dead for every tested `n`,
reproducing the campaign `m=2` no-jump-dead arithmetic. For odd `r`,
`n` odd gives `M=2` and integer `kbar`. N1 at the merge:

```text
gcd(kbar, n) = gcd(3(1+r n)/2, n) = gcd(3, n),
```

because `1+r n ≡ 1 (mod n)` and `n` odd makes `2` invertible. So N1 is
`3 doesn't divide n`. R1.0: `gcd(M,n)=gcd(2,n)=1` automatically. Admissible
merge indices are `n >= 2` with `n mod 6 in {1,5}`, independently of `r`.
Checked on `n=2..39` for every odd `r` in `[3,59]`: the legal set is
exactly that AP. Trunk reduced state `(w_tr,M)=(3r/2, 2)` is constant on
the AP (Theorem C').

`n=1` is the U2 regime (N1 off) and is not used. Any `n in {5,7,11,...}`
supplies merge data; the trunk does not read `n`.

### 2.3 Trunk, divisor, terminal

One dirty P0 step from `(w_G,M_G)=(3r/2,2)`, arrival `l=2 | 2`. R1.3 at
`l=2`: every non-chain orbit is northeast, `m_j < dp/dq < 2` forces
`m_j=1`, and `dq<dp` forces `lex=0`. Shape:

```text
dp = nu(2+k),   dq = nu(1+k)+1,   E = nu k + 2,   k >= 1,
kbar = 3 r dq / E,   X = 3 r dp / E,
w_F = 3 r (1+k) / E,   M_F = gcd(dp, dq).
```

`w_G=3r/2` is already in lowest terms (`r` odd), so `num(w_G)=3r`.
`C = l(k+lex)-Sm = k >= 1`, hence the extras-present divisor law applies:
`E | l*num(w)*T` with `T=Sm+l=k+2`, i.e. `E | 6 r (k+2)`. The Fable
resolvent `E(l a (1+k+lex) - kbar d C_P0) = l a T` is an identity on this
shape, not an extra constraint. `(S),(NE),(R)` hold for `nu>=2`. Euclidean
algorithm:

```text
M_F = gcd(k+2, nu-1).
```

P1 terminal: `w_F<1`, `M_F>=2`, `j=M_F(1-w_F) in N^*`, plus N1 and R1.0.

Enumeration, for every odd `r` in `[3,59]`, of all `(k,E)` with `k=1..79`,
`E | 6r(k+2)`, `E=nu k+2`, `nu>=2`, integer `kbar`, `(S)/(NE)/(R)`, N1,
R1.0, and P1 with slack `>=0`: the budget-fitting terminals are **exactly**
the claimed divisor family, with **zero extras**. In particular the `j>1`
locus is empty on this menu. Closed forms hold with zero failures:

```text
E = 3 r (k+2),
nu = 3 r + 2(3 r-1)/k,          (so k | 3r-1, automatically k | 2(3r-1))
M_F = k+2,   w_F = (k+1)/(k+2),   j = 1,
psi = ceil(M_F/j)-1 = ceil(1/(1-w_F))-1 = k+1,
X - kbar = (3r-1)/k,
lambda_floor = k * (3r-1)/k = 3r-1,
budget = td - 1 - psi = 4r - k - 2,
slack = r - k - 1.
```

The `k<=r-1` cut is exactly `slack>=0`. At `k=1`, which always divides
`3r-1` and always satisfies `1<=r-1`,

```text
nu_F = 9r-2,  kbar_F = 6r-1,  X_F = 9r-2,  w_F = 2/3,  M_F = 3,
psi = 2,  lambda_floor = 3r-1,  budget = 4r-3,  slack = r-2.
```

The `r=3` row is the reviewed charged trunk: `(nu,kbar,X,w,M)=(25,17,25,2/3,3)`,
floor 8, budget 9, slack 1. The `k=2` row is the sibling
`(17,13,17,3/4,4)`, floor 8, budget 8, slack 0. Both were obtained from
the general law, not by copying those records.

Negative controls, matching the target: `k=16` at `r=3` and `k=4,28` at
`r=5` fail R1.0 (`gcd(M,nu)=2`). That is why the live divisors are of
`3r-1` and not of `2(3r-1)`.

The complete `eps=0` dirty **menu** is larger than the terminal slice.
At `r=3` it is exactly six cells

```text
(k,nu,w,M,lambda) =
  (1,7, 2,   3, 6),   (1,25, 2/3, 3, 8),
  (2,5, 9/4, 4, 6),   (2,17, 3/4, 4, 8),
  (4,13, 5/6, 6, 8),  (8,11, 9/10,10, 8).
```

The last two are P1-shaped and fail their own terminal budgets. The first
four are the A7/C5/B25/S17 quartet (Section 5). The target's trunk law
claims only the P1-fitting terminals and is correct on that scope.

### 2.4 T1

On the `k=1` cell the R1.3 shape is family C of `cases/l1_ode_check.py`:

```text
p = (t-A)^2 (t-B),   q = eta (t-A)(t-B),   t = eta^{nu_F},
rho = dp/dq = 3 nu_F / (2 nu_F + 1).
```

The normalized identity, after dividing by `p`, is the quadratic

```text
C_iv(t) = rho (t-A)(t-B) + nu t[(rho-2)(t-B)+(rho-1)(t-A)].
```

Its `t^2` coefficient is `rho + nu(2 rho - 3)`, which vanishes identically
on `rho = 3 nu/(2 nu+1)`. The remaining linear condition is
one-dimensional:

```text
B/A = (nu+2)/(nu-1) = 3r/(3r-1),   C_iv = rho A B != 0.
```

Independent evaluation: at `r=3`, `nu=25`, `B/A=9/8`, `C_iv=(25/17)AB`;
at `r=5`, `nu=43`, `B/A=15/14`; at `r=7`, `nu=61`, `B/A=21/20`. Mutations
`B/A=7/8` and `A=B` make the linear coefficient nonzero, matching the
target's negative controls. Root law: `rho != 2` at the double root and
`rho != 1` at the simple root, both automatic for `nu=9r-2>=25`.
`A != 0`, `B != 0`, `A != B`.

This is vertex-local solvability of Proposition 8.1(iv). It is not gluing
of `t_G^r - A_star` to the trunk ratio, and it is not a source coefficient.

T1 at `k>1` is **not** supplied by the target (the displayed solve is the
`(t-A)^2(t-B)` pattern) and is not independently closed here. The sibling
record at `r=3`, `k=2` still lists the `(17,68,52)` solve as prior work.
This does not touch the no-go: `k=1` is legal for every odd `r>=3` and
is T1-solved.

Merge T1 is Theorem E of the reviewed U1 package (`Rad_G = t_G^r - A_star`,
`A_star != 0`), consumed as a promoted closed form, not re-solved.

### 2.5 Source-mass

Fable's promoted `ASM'` (review §6, not the refuted strong ASM at `mu>=3`):
an arrival of multiplicity `mu>=2` carries pole mass
`>= max(beta, 2 alpha)`; a `mu=1` arrival carries `>= beta`. All `r`
arrivals here have `mu=2`, so `ASM` is the verbatim `mu<=2` case. Incoming
pole-leaf sets are disjoint (Fable A5, tree geometry). Hence

```text
td >= r * max(3, 4) = 4r,
```

saturated by `td=4r`. Minimising `max(beta, 2 alpha)` over coprime
`2<=alpha<beta` gives unique minimum `4` at `(2,3)` (`(2,4)` is not
coprime). Equality forces each incoming subtree to be a single pole of
mass `4`, hence `s=R=r` and each pole `(1,2,3)`. This is the target's
`R`-uniform reading of clause 5, confirmed. The factor `3` in the
reviewed `td>=12` floor is a hypothesised arity, not a premise.

### 2.6 Budget

Poles and the `eps=0` merge price zero. The trunk terminal prices the AF2
floor `3r-1`. Statement 9.4 / P1 shares one ceiling `td-1-psi` over the
whole configuration. Fitting is `3r-1 <= 4r-k-2`, i.e. `k<=r-1`. Slack at
the always-present `k=1` cell is `r-2`, strictly increasing in `r` for
`r>=3`. A budget whose kill power decays in `td` cannot cap `td`.

FALLACY-v2 floor/attainment: the comparison uses a lower bound on `lambda`
against an upper bound on the sum. Formal decoration of the cell by the
floor value satisfies `(A12)`. Exact-charge upgrades are not in `Sigma_cfg`
and are not used. The target's unreviewed `r`-general sibling replay in
§4.3(ii) is likewise not used, and no `charge_basis` line is declared.

### 2.7 Quantifiers

Theorem NG is a soundness statement: `Sigma_cfg` has a model of topological
degree `4r` for every odd `r>=3`. The existentials are: choice of merge
index `n` on the AP (any one), and choice of a fitting trunk `k` (`k=1`
suffices). The fibre label `a` is the usual `!E2`. None of these is
silently universalised. The family is not asserted for actual maps, for
every fibre of one map, or as a `PairRef`.

The no-go is exactly as strong as that: any proof of `td=12` from a
counterexample must consume a premise outside `Sigma_cfg`. It does not
show that a hidden realizability axiom is impossible, and it does not
show that `U1*(r)` occurs.

### 2.8 Omitted-axiom search

Checked and **not a kill**:

- MP6 is scoped to merges with some `mu_e=1`. All-`mu>=2` mixed merges
  are recorded as open at printed tier (`SHEET6-MULTIPOLE.md` after D6),
  and the campaign's own reviewed `r=3` U1 star is the same shape. The
  parenthetical "k=0 needs some `mu_e=1`" is MP6(a)'s hypothesis, not a
  prohibition of U1. Equal-quotient MP6(b) at a literal length-zero pole
  arrival would pin merge index `n=2` via `deg p_P = b alpha = 4 = i mu`
  and then MP2-kill; that reading is an i-sync/chart identification, is
  not in `Sigma_cfg`, and would equally kill the reviewed `td=12` U1
  object. Zero-price clean-neutral interpolations on the pole arms, if
  anyone wants them, preserve `(w,M)=(3/2,2)` and MP1. Not a refutation
  at interface scope.
- St 8.5 / merge-free M-descent is not used on the pole arms. The dirty
  trunk step is a regular `V_{2,a}` step and legally changes `M` without
  an MP0 merge (FALLACY-v2). `M: 2 -> k+2` is the reviewed `r=3` pattern
  `2 -> 3` or `2 -> 4`.
- Contact-zero root window `0<w_e<1` applies to root meets. The U1 merge
  has `w_tr=3r/2>1` and is not a root; the P1 terminal has `w_F<1`.
- Case III / 0-arrival is absent. Target/arrival indices are not mixed.
- i-sync, Statement 3.9, coefficient maps, `H5a`, `RPMC`/`KJN`, BOOK
  marking, and G2-PSC are realizability or unpromoted. They are correctly
  excluded from `Sigma_cfg`. BOOK marking is undefined off-axis besides.
- Proposition 8.4 is single-pole. Vacuous at `s=r>=3`.
- Neutral prefixes from `(3r/2,2)` are optional, price zero, and preserve
  the reduced trunk state. They enlarge the model set.

No omitted promoted configuration-level axiom was found that empties
`U1*(r)` at any odd `r>=3`. No illegal quantifier was found in Theorem NG.

---

## 3. Claim B — Section 7 audit

### 3.1 Where the constant `1` comes from

Repaired Corollary 7.1 is the inequality

```text
d >= 1 + sum_{F in T_{a,cv}} kappa_F (pi(F)-1)
```

proved in the weighted-Euler repair §§4–5 and passed by the Terra
different-model review on the amended hash `c253bd12...`. The global step
is repair (5.1)–(5.3) / Terra §7:

```text
d - N(a,b) = sum_{P at infinity on f=a, g(P)=b} Lambda(P)     (5.1)
d - N     = sum_i (phi_i)_! w_i                               (5.2)
d - 1     = integral_{A^2} (d-N) d chi_c
          = sum_i integral_{U_i} w_i d chi_c
          >= sum_i b_i^+  >=  sum wt.                         (5.3)
```

The `1` is `chi_c(A^2)=1`, from Keller quasi-finiteness and
`integral N d chi_c = chi_c(A^2)`. A second `1` appears inside each line
integral, namely `chi_c(U_i)=chi_c(A^1)=1`, and is used only to get
`integral_{U_i} w_i >= b_i^+` from a constant generic value with upward
jumps. The displayed constant in `d >= 1 + sum wt` is the global
`chi_c(A^2)`, not "the Euler characteristic of that one target line"
(target §5.3 step 2). That misidentification is load-bearing for the
proposed repair of the constant.

Statement 9.4's ceiling `td-1-psi` consumes this same `1` (H3-psi: Cor 7.1
gives `sum lambda + psi <= td-1`). Replacing it by `s` is not a
re-indexing of an existing term.

### 3.2 Pole clusters cannot alter `chi_c(A^2)`

The passed quotient bijection (repair §1, Terra §7) is from
`coprod_i U_i(C)` onto **finite-value** direction clusters in all fibres.
Identity (5.1) sums `Lambda(P)` over infinity places of `f=a` with
**finite** `g(P)=b`. Poles of `g` have `g=infty` and do not appear in
`d-N(a,b)` for finite `b`.

Proposition 5.1's promoted sidedness theorem puts every pole threshold in
`T_a^+` and every finite threshold in `T_a^-`, with no threshold in
`T_a^0`. Pole clusters and finite-value clusters are disjoint by that
repair; they are not `s` extra compactly-supported components of the same
`U_i` Euler integral.

Compactly supported Euler characteristic of `A^2` is `1`, independently of
how many poles `g` has on a fibre. Including the line at infinity would
change the space, break `N = Phi_! 1` on `A^2`, and is not the promoted
argument. There is no missing `s-1` term in (5.3). The identity is an
equality

```text
d - 1 = sum_i integral_{U_i} w_i d chi_c,
```

with no remainder indexed by `T_{a,pole}`.

### 3.3 RH ramification cannot be typed to flag weights

The fibrewise identity is elementary and is confirmed. Because `J in C^*`,
the affine fibre `{f=a}` is smooth and `g` is unramified on it (a critical
point of `g|_{R_a}` would force `J=0`). All ramification of
`g: R~_a -> P^1` of degree `d` lives at infinity. Poles of `g` contribute
`sum (Lambda-1) = d-s`. Riemann-Hurwitz therefore gives

```text
2g-2 = -2d + (d-s) + sum_{non-pole inf}(e_F-1),
```

i.e. the displayed `(*)`. As a corollary, the left side `>=0` and
`g>=0` do **not** give a new lower bound on `d`; they do give that a
generic fibre of a counterexample (`d>=6`) cannot have every place at
infinity a pole of `g`. That corollary is cheap and correct, and it is
not PCB.

FALLACY-v2 forbids identifying a cv flag, a physical place, and a cover
series. Independently of that prohibition, the two numerical quantities
cannot be equal in the regime the lemma needs. Corollary 7.1 gives
`sum wt <= d-1`. The RH left side is `>= d+s-2`. For `s>=2`, `d>=6`,
`g>=0`:

```text
sum (e_F-1)  >=  d+s-2  >= d  >  d-1  >=  sum wt.
```

At the `U1*(r)` numbers: `s=r`, `d=4r` yields RH `>= 5r-2` against
C7.1 `sum wt <= 4r-1`, a gap of `r-1 >= 2`. Transferring `(*)` onto
`sum wt` would contradict the promoted Corollary 7.1, not strengthen it.
The extra `s-1` the target wants for the **budget** is a tightening of
the ceiling; the RH identity supplies a large ramification sum on the
wrong space, in the wrong direction, of the wrong size.

### 3.4 Structural obstruction, not a Keller countermodel

PCB as a statement about actual maps is untestable inside the Keller
class (`s>=2` already forces `d>=6`, hence a counterexample). Automorphism
checks at `d=1`, `s=1` compare two identical statements. The `SHEET6-2POLE`
cell (`td=6`, `s=2`, `sum lambda=2`, `psi=2`) survives both ceilings and
is not a test. None of this is evidence for PCB.

The smallest exact source audit is repair (5.1)–(5.3) with Terra §7. That
package implies: if the inequalities `integral w_i >= b_i^+ >= wt_i`
saturate, then `d = 1 + sum wt`, **independently of `s`**. Saturation is
compatible with Lemmas 3.1–3.2 (Terra's local chart realises `w(0)=b^+`).
A saturating fibre with `s>=2` would refute PCB, and the Section 7 proof
does not forbid saturation at `s>=2`. Therefore PCB is **not a
consequence of the promoted Section 7 package**. Getting PCB would
require a new reason that saturation is incompatible with `s>=2`, which
is circular.

Label at the strongest justified level:

- proposed RH / pole-cluster proof of PCB: **FALSE**;
- PCB as a corollary of promoted Corollary 7.1: **FALSE**;
- PCB as a bare inequality on actual Keller maps: **UNSUPPORTED**;
- combined campaign token: **`FALSE/UNSUPPORTED`**.

Not `DUPLICATE` (strictly stronger than C7.1 at `s>=2`, different
constant). Not `PLAUSIBLE_OPEN`: the proposed mechanism is not a near-miss.
Do not promote PCB because it kills `U1*(r)`. Under present axioms it
does not.

### 3.5 What a genuine extra-`s` lemma would have to be

Any replacement would have to live outside (5.3), name a different space
or a different constructible function, and prove a surplus of at least
`s-1` in the finite-value weight integrals without identifying flags with
places. No such argument is in the target, and none is supplied here.
Typed `OPEN` as a possible future lemma is allowed by FALLACY-v2; that is
strictly weaker than the target's proposal and is **not** PCB.

---

## 4. A7/C5 reconciliation

The separate detour report
`xmodel/td12-u1-first-nonneutral-quartet-detour-analysis-sol56-93d-20260829.md`
is the `r=3` first-nonneutral menu, not a restriction of Claim A.

Independently recovered from `(w,M)=(9/2,2)` at remaining budget 10, the
`eps=0` dirty survivors are the six cells of §2.3. Dropping the two
budget-failing P1 shapes leaves A7, C5, B25, S17, which is the detour
report's quartet. B25 and S17 **are** `U1*(3)`'s two fitting terminals.
A7 and C5 are the `w>1` nonterminal first steps, with formal tails

```text
(9/2,2) -> A7 (2,3) -> (6/7,7) -> (6/13,13),
(9/2,2) -> C5 (9/4,4) -> (6/7,7) -> (6/13,13).
```

They are additional abstract models at `td=12`, not a hole in `U1*(r)`.
Local T1 solvability on those tails is not gluing (detour report's own
firewall). General `r` has analogous `w>1` dirty children; they only
enlarge the formal model set. They do not select `r=3`, and they do not
rescue PCB.

Conditional on an actual `td=12` U1 record, the quartet is still the
right first-nonneutral alternative. That conditional does not supply the
missing occurrence arrow, which is Claim A's point.

---

## 5. Firewall

This review does not assert, and nothing in it may be read as asserting:
an occurrence, attainment, `PairRef`, source value, Keller pair, degree
ceiling, type ceiling, landing, coverage certificate, panel closure,
route kill, JC2 conclusion, or a new exit price. `U1*(r)` is an abstract
admissible configuration. PCB is not proved and is not promoted. The
`r`-general sibling exact-charge observation remains unreviewed and
unused.

What it does assert: the Claim A closed forms and the interface no-go
relative to the target's `Sigma_cfg`; local T1 at every `k=1` cell;
absence of extra one-step P1 terminals on the enumerated menu; the
quantity audit of Claim B, including the RH identity and the
non-identification with `sum wt`; the two tokens of §0.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22849`.
- Body SHA-256:
  `36986889dd6f80ed5ed167b8e0ecdaa457fb0a580252f1edad4846c0e74d77a8`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
- Exit-price declaration: absent.
