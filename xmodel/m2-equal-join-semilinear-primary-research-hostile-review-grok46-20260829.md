# Hostile review — Opus 5 equal-arrival semilinear theorems

Lane: Grok 4.6, different-model adversarial referee.
Target: `xmodel/m2-equal-join-semilinear-primary-research-opus5-20260829.md`
and packet `cases/m2_equal_join_semilinear_opus5_20260829/`.

Comparison sources only, all read in the sections the target cites:
`ladder/BOOK-OFFAXIS.md` §§0–11a (R1.0, R2.1–R2.2, P0–P5, T1, E5);
`ladder/SHEET6-DEPTH.md` §1 and §5c–5d; `ladder/SHEET6-MULTIPOLE.md`
MP0–MP9, D1–D9, OBSTRUCTION O; `ladder/REDUCTION.md` CRITICAL 4–7 and
§§5.1–5.4; `ladder/SHEET6-III.md` §3 (N1); `xmodel/sol-td7-law.md`
(1)–(9); `cases/l1_ode_check.py` header (families A/B/C);
the prior Opus M2 report and this lane's hostile review of it;
Sol56's finite reduced-chain theorem with both R1 reviews and the R2
repair note; Fable5's correction of Sol56's incoming-index theorem.
Entry-row verification used the current `cases/book_offaxis.py` census
(reusing `book_enum.entries` / `tdu_rows`).

No other active post-target model output was read. No access of any
kind to `jc2-lean`. No web, AWS, heavy/local CAS, canonical edit, git
status, commit, or push. Arithmetic below is desk `int`/`Fraction` and
a second exact sparse-polynomial class under `/tmp`.

Nothing here claims landing, a type ceiling, realizability, or JC2.

---

## 0. Custody

Full-file SHA-256 of the target, 44,147 bytes:

```
7ed65bc22f836230dada03776a1b3c6f9110c955a35b52fa28c21d0811a6c99d
```

Body hash of the first 43,954 bytes (through and including the newline
after `*Report body ends. The seal below covers everything above this
line.*`):

```
bacf0d6ba789655ebbfd0b9da7018b8e10303fab149b38ef052587fadc5278d2
```

matches the report's own `report_body_sha256` line.

Packet principal hashes, verified this session, match the target §8
table byte-for-byte:

```
a23403a231f0418b0e036248baa6d3846933335a50b3fcc421bf8edb4d626779  polyexact.py
dd826f24ff179c34ca1af6f20fb53615de791a52271378380c654be4ee5f9482  t1_merge_reduction.py
6de8b7974de4a556d6347a36b9e777a4a559ea0e296064f509044e9aa1216ef9  eqjoin_semilinear.py
b72cf02aa897390287926bf7439575b93d14afe7337d488b05f748204fd4eb2e  controls.py
d5bddea6f9590fb2ffa9b4f930fb6965febb859b2ebf8bbfbbdfe041a9f1d475  emit_eqjoin.py
c3cb105ee9f57785d77bbcf191e9c346eb7a3312c98b2058dda771587263dc3e  trunk_probe.py
1f4e4260afce85dd06345c48704af77c74f2243db32e730e69066786ee95bf99  test_eqjoin_semilinear.py
a419002987f29cbd74d390b11aee1d68ff817aab6293c34ea53c0a484d81c09d  README.md
```

Cited comparison sources, hashes as on disk this session:

```
7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77  ladder/BOOK-OFFAXIS.md
ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d  ladder/SHEET6-DEPTH.md
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936  ladder/REDUCTION.md
59a2fa489f7f999b24aabc4c707254b7e54f8db02d69690226754e3224f9bdda  ladder/SHEET6-III.md
99bd762aa458840bd8e3327fae35c7e23ad388976fb0fcb85c0fd8570ab592f2  xmodel/sol-td7-law.md
ffb83ec1fcbfbbb18573a030e80e22c20a7d78bb92a5e7a6a5ce4d7b9b96e7af  prior Opus M2 report
5192c007536cc2b36e813c23ab16b9badba85d61bec6a56646d561c0f1ff4bfa  this lane's prior M2 review
df776b25565fb43c2f45fd8bc64db822d5775822b834fa58fe7f45db2f1a4e54  prior Grok falsifier
239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad  Sol56 finite-chain R1
bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912  Grok R1 review
3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f  Fable R1 review
406e78d220b62910e6296866db998bd0e7d898b2e6a618fe0aa70ffbeb73fd46  Sol56 incoming-index
350b5190eaae7a285510d62bc687d56fe1b0a92eedab714254d420a7995f5393  Fable incoming-index review
c22e3a1f977fef94022f34378232fcc78148fa506501f71ec6a57313d6042ebc  cases/book_offaxis.py
002bacb152f1ff86a5b99d8d990d2f1b7b55c4bc063d4e3146fa0aa268f8e81e  cases/book_enum.py
e766bfe27ac9a06ef6eab053dbea666f8b3d3e70a48ee8c76b88e45246c3bea9  cases/l1_ode_check.py
```

---

## 1. Verdict

**`REPAIR_REQUIRED`**

The closed-form U1 calculus, the exact `M = gcd(mu-eps, r*nu+1)` law,
the AP description of admissible `nu`, the general merge Prop. 8.1(iv)
identity, and the U1 rigidity `Rad = t^r - A` with automatically
nonzero right-hand side are independently re-derived and hold. The
prior-round quantifier bug (one degenerate edge versus all edges) is
actually repaired: both coefficients of the affine consistency residual
are load-bearing, and unequal `mu` cannot form an unbounded family.
Regime U2 is genuinely distinct and is currently unclosed outside
`td=7`. The `td=12` star is a real **conditional** infinite
pattern-tier family, not a false witness: the current source entry row
is unique of global type `(2,3)`, and the displayed numbers are that
row's numbers.

Three numbered statements, as written, are not theorems of the legality
predicate the report itself lists in §2.

1. **Theorem A's iff** classifies when two-edge consistency and the
   sign of `C` fail to pin `nu_G`. It does **not** classify when the
   set of legal `nu_G` is infinite. Interior MP2 and DS1(c) integrality
   can empty a 1–4 family; the report's own `mu=1` equal-join (the
   `td=7` class-A `lex=0` shape) is a recorded counterexample to
   sufficiency. Necessity of 1–4 for unbounded `nu_G` at `nu>=2` stands.
2. **Theorem A(b)** says `kbar` is strictly decreasing when `C>=1`. The
   derivative has the sign of `T`, so the map is strictly monotone with
   a finite limit; it increases whenever `T>0` (the generic `eps=0`
   extra-orbit case). Finiteness survives; the adverb does not.
3. **Theorem C'** calls the trunk P0 menu constant in `nu_G`. The menu
   is a function of `(w_tr, M)`; `M` is in general periodic with more
   than one interior value (desk example: `r=2`, `mu=15`, `M in {3,5,15}`).
   Constancy holds on families such as the `td=12` witness where `M`
   is identically 2. The correct word is periodic, specializing to
   constant when `M` is.

The other-types honesty rider on the `td=12` entry is false, in the
direction that **strengthens** the witness: types `(2,5)`, `(3,4)`,
`(3,5)` do not admit `[2,2,2]` at `td=12` under Prop. 5.7 / MP4. The
unique L6-surviving source row is type `(2,3)`. Theorem F's unique
full-`nu` consumer, cited as Sol56's incoming-index bound, inherits
Fable's `REPAIR_REQUIRED` handshake; at the promoted E5 pin that
consumer vanishes rather than being bounded. That does not break
combinatorial semilinear sufficiency.

Repair is local. The promotion-safe residue is stated in §8. A PASS is
denied because Theorem A is advertised as an iff classification of all
unbounded merge regimes and is not one. FAIL is withheld because no
U1 identity used downstream is false, and the `td=12` family is not
fictional.

---

## 2. Reconstructed laws used as the referee's baseline

Notation as in the target §2, matching P0 / R1.0 / R2.2:

```
P  := sum_e mu_e + sum_j m_j
s  := r0 + k + lex
dp  = eps + nu*P
dq  = 1 + nu*s
M   = gcd(dp, dq)
E_e = mu_e*dq - dp = (mu_e - eps) + nu*C_e
C_e := mu_e*s - P
T   := P - s*eps
```

`T != 0` by (R) at multiplicity `eps` when `eps>=1`, and by `T=P>=1`
when `eps=0` (prior-review typing repair, which the target now uses).

Transport is **not** uniform in the arriving edge type.

- Case I/II (R2.1, P0, R1.2/R1.4): `what_e = w_e`,
  `X = mu_e*(kbar - w_e)`, `kbar = mu_e*w_e*dq/E_e`.
- Case III, printed DEPTH §5c / R2.1: `what_0 = nu_H*w_H`,
  `X = mu_0*(kbar - nu_H*w_H)`.
- Case III, promoted E5 / §11a (I4): `what_0 = nu_G*w_U`,
  `X = mu_0*(kbar - nu_G*w_U)`. Fable's incoming-index review is
  treated as the live correction of Sol56 on this fork: the mixed
  printed handshake is the non-promoted side, and under E5 the
  incoming index is not the handshake variable.

(S): `mu_e*dq > dp` on every arriving edge. (NE): `m_j*dq < dp` and
`eps*dq < dp` on non-arrivals and on a free 0-root. (I): `kbar in Z`
at `nu>=2`; `kbar in Q` at `nu=1`. N1: `gcd(kbar, nu)=1` at every
`nu>=2` vertex. MP2: interior `M>=2`. P0/P2 price arriving edges and
`lex` at 0; a free 0-root and every NE orbit cost at least 1; a 0-arrival
is not a free 0-root.

A 0-root is a **free** 0-root only when no chain arrives at 0.
`eps = mu_0` on a 0-arrival is case III and prices 0 (P2/P3).

Prop. 8.1(iv) in the normalized form of `l1_ode_check.py` / R1.0:

```
rho*p*q' - p'*q = C*p,    rho = dp/dq,    C != 0.
```

---

## 3. Attack 1 — Theorem A (unbounded classification)

> The set of legal `nu_G` is infinite iff (1) no 0-arrival, (2) all
> `mu_e` equal, (3) all `w_e` equal, (4) `k=lex=0`.

### 3.1 Two-coefficient residual: CONFIRMED

For edges `e != f`, R2.1 equality of the two `kbar` expressions is
affine in `nu` with coefficients

```
const = kappa_e*(mu_f - eps) - kappa_f*(mu_e - eps)
slope = kappa_e*C_f - kappa_f*C_e
```

with `kappa_x = mu_x*what_x > 0`. The identity

```
s*const - slope = (kappa_e - kappa_f)*T
```

holds on a desk box `mu <= 7`, `s <= 7`, `P <= 19`, four sample
`(w_e,w_f)` pairs, zero failures. Since `T != 0`, both coefficients
vanish iff `kappa_e = kappa_f`, hence (from the constant half, and
`kappa>0`) `mu_e = mu_f` and `what_e = what_f`.

This is the exact repair of prior Theorem 2.1 / E4. A single
`C_e=0` edge is never sufficient. Packet mutations exhibit both
one-sided vanishings at unequal `mu`; C5, charged at box 6, checks
24,416 constant-solved unequal-`mu` configurations with zero double
degeneracies (the report's 24,416 is this charged box, not box 8).

### 3.2 Unequal multiplicities, unequal invariants, free 0-roots, non-chain orbits, `lex`

- Unequal `mu` or unequal `what`: residual pins `nu` to at most one
  root of a nontrivial affine equation. CONFIRMED.
- Free 0-root `0 <= eps <= mu-1` does **not** destroy `C=0`: with
  equal `mu` one has `C = mu*(k+lex) - Sm` independent of `eps`.
  (S) and (NE) on the free 0-root both reduce to `eps < mu`, already
  assumed. U1 includes these variants. CONFIRMED, and Theorem B
  carries them.
- Non-chain orbits: `m_j <= mu-1` gives `C >= k + mu*lex >= 1` unless
  `k=lex=0`. Desk enumeration at `r0 in {2,3}`, `mu_e <= 4`,
  `k,lex <= 2` finds `C_e=0` for every `e` only at equal `mu` and
  `k=lex=0`, and finds the some-but-not-all zeros the prior review
  used to kill the old iff (samples still legal as degree
  inequalities). CONFIRMED.
- `lex` at `nu>=2`: `C = mu*lex >= 1` when `k=0` and `lex>=1`, so
  `kbar` is strictly monotone in `nu` with finite limit `mu*w*s/C`.
  Integrality of `kbar` then yields finitely many `nu`. CONFIRMED
  as a finiteness argument. At `nu=1`, integrality is off and `lex`
  is unpriced: that is U2, listed.

No omitted merge-local unbounded-`nu_G` regime was found. Neutral
chain rays are not merges. Unpriced `lex` at `nu=1` is U2, not a
third U1-like family.

Integrality is **not** used circularly. On U1 it is a congruence
filter (Theorem C). On `C != 0` it is a finiteness lever. The defect
in the iff is that integrality and MP2 are **underused**: they can
empty a 1–4 family, so they belong in the sufficiency half.

### 3.3 Case III, both readings: CONFIRMED as boundedness of `nu_G`

Printed DEPTH §5c (`what_0` independent of `nu_G`): `eps = mu_0`
makes `E_0 = nu*C_0` with `C_0 >= 1` by (S), so the configuration
is never U1, and (b) bounds `nu_G`. CONFIRMED.

Promoted E5 (`what_0 = nu_G*w_U`): `kbar = mu_0*w_U*dq/C_0` is
affine, so consistency with a nonzero edge forces `E_e` constant,
hence either `C_e=0` or a single `nu`. `C_e=0` plus (S) on the
nonzero edge needs `mu_e > mu_0`, which makes `C_0 = (mu_0-mu_e)*s < 0`,
contradicting `C_0 >= 1`. Desk sweep with (S) enforced: 0 legal
`(C_e=0, C_0>=1)` cells; without (S), 48 spurious hits, all with
`E_e < 0`. So `nu_G` is a single determined value. CONFIRMED.

The packet function `classify_unbounded` implements only the printed
reading (constant `whats`). The E5 pin lives in the prose proof, not
in the classifier. That is a packet gap, not a hole in (c).

### 3.4 The iff, as a statement about legal `nu_G`: REFUTED

§2 includes (I), N1, and MP2 in the recorded legality predicate.
Theorem A's sufficiency ignores them.

Counterexample 1, recorded by the target itself in §6.3: `r=2`,
`mu=1`, `eps=0`, `k=lex=0`, no 0-arrival, equal `w`. Conditions 1–4
hold, `C=0`, consistency holds for every `nu`, but
`M = gcd(1, 2*nu+1) = 1` for every `nu`, so every interior vertex is
MP2-dead. The legal interior set is empty, not infinite. This is
exactly the `td=7` class-A `lex=0` shape the report uses to say
`td=7` supplies no U1 witness.

Counterexample 2, integrality: `r=2`, `mu=1`, `w=1/2`, same discrete
data. `B' = 2` and `gcd(r, B') = 2 != 1`, so `kbar = (2*nu+1)/2`
is never an integer. The `nu>=2` legal set is empty even before MP2.

Necessity of 1–4 for an infinite `nu>=2` legal set is not in doubt:
if any of 1–4 fails, either consistency pins `nu` or `C != 0` makes
`kbar` strictly monotone with a finite limit, hence only finitely
many integer `kbar`. Repair: A's iff is the classification of when
consistency plus the sign of `C` fail to bound `nu`; infinitude of
the **legal** set is Theorem C's nonempty AP, i.e. 1–4 plus
`gcd(r, B')=1` plus MP2 satisfiable plus N1 not emptying the class.

### 3.5 Theorem A(b) adverb: REFUTED, finiteness CONFIRMED

`d(kbar)/d nu` has the sign of `T`. Samples:

| data | `C` | `T` | trend | limit |
|---|---:|---:|---|---|
| `r=2, mu=3, eps=0, lex=1` | 3 | 6 | increasing | `9/2` |
| `r=2, mu=4, eps=3, lex=1` | 4 | −1 | decreasing | `9/2` |

Each integer `kbar` still determines `nu` at most once, and the
finite limit bounds the integer window. The word "decreasing" is
wrong whenever `T>0`. Replace by "strictly monotone with finite
limit `mu*w*s/C`".

---

## 4. Attack 2 — Theorems B / C / C'

### 4.1 Theorem B closed forms: CONFIRMED, including the exact `M` law

On U1 (`k=lex=0`, equal `(mu, w)`, `0 <= eps <= mu-1`):

```
dp = eps + nu*r*mu,     dq = 1 + nu*r,     E = mu - eps,
kbar = mu*w*dq/E,       X = mu*w*dp/E,     rho = mu*w/E,
w_tr = mu*w*r/E         (constant),
M = gcd(mu-eps, r*nu+1) (exact),
T = r*(mu-eps),
lambda = 0  if eps=0, else max(1, ceil(mu*w*r/eps))  (constant).
```

`M | dp` and `M | dq` imply `M | (mu*dq - dp) = mu-eps`; conversely
any common divisor of `mu-eps` and `dq` divides `dp`. Desk identity
on `r<=5`, `mu in {1,2,3,5,7}`, all legal `eps`, five `w`, nine
`nu` including 1 and 30: zero failures. The naive `M = gcd(mu, dq)`
differs as soon as `eps >= 1` (packet mutation live).

Lambda density: `(X/eps - kbar)/nu = mu*w*r/eps`, matching P2's free
0-root price. Successor weight `w_tr` is the P0/R1.4 formula
`mu*w*s/E` at `s=r`. Floor/ceil of a positive rational is unambiguous.

`r` even implies `dq` odd, hence `M` odd. At `r=2`, MP2 therefore
needs the odd part of `mu-eps` at least 3. Exhaustive for `mu<=40`
and the listed `eps>=1` variants: CONFIRMED. The `m=2` no-jump-dead
headline argument is correctly scoped to printed §1 rows: those gcds
are `1` or `2`, so `mu-eps <= 2` has odd part 1 and MP2 kills. Both
chains must first raise `M`. Rider accepted.

### 4.2 Theorem C: CONFIRMED

`kbar = mu*a*dq/(b*E)` is an integer iff `B' | dq`, with
`B' = b*E / gcd(b*E, mu*a)`. The integrality class is nonempty iff
`gcd(r, B')=1`, and is then the single class `nu ≡ -r^{-1} (mod B')`.

MP2 is the condition that some prime `p | (mu-eps)` divides `dq`.
N1: `gcd(dq, nu)=1`, so if `p | nu` then `v_p(kbar) = v_p(mu*a) - v_p(b*E)`
independent of `nu`; hence `gcd(kbar, nu)>1` iff `nu` shares a prime
with the stated radical `R`. Independent scan on seven families
including the `td=12` witness and the C4 pair, `nu=2..119`: every
integrality and N1 predicate matched the closed form.

`nu=1` is correctly excluded: case I, `kbar in Q` legal, N1 off,
regime U2. Prior §6a's `(mu,w,nu)=(3,3,1)` is rightly erratum E5.
If `n_e in N*` were promoted to a kill it would cut a finite initial
segment; the family would stay semilinear. CONFIRMED as a rider.

The period `lcm(B', E, R)` is a period; the packet reduces it to the
minimal period before hashing, as Theorem F's equality rule requires.

### 4.3 Theorem C': CONFIRMED after a wording repair

`w_tr` and `lambda_G` are constant by B. `M` is periodic of period
dividing `mu-eps`. T1 at `G` is constant by E. P1 terminal data of a
descendant are a function of `(w_t, M_t)`, hence inherit periodicity
of the reduced trunk state. Sol56's chain theorem (both reviews
`PASS` at chain scope, R2 an implementation repair only) then makes
the reduced descendant set finite at fixed remaining budget.

The P0 **menu** is a function of `(w, M)`, not of `w` alone. When `M`
takes several interior values the menu is periodic, not constant.
Desk: `r=2`, `mu=15`, `eps=0`, admissible `M in {3,5,15}`. On the
`td=12` witness `M ≡ 2`, so the menu is in fact constant. Repair:
"constant in `nu_G` when `M` is; otherwise periodic with `M`".

Family/cell collisions: Theorem G(a) CONFIRMED — two members determine
the `dp`-slope `r*mu` and intercept `eps`, and `r = (dq-1)/nu`, hence
the whole family. G(b) CONFIRMED: `(2,10,0,9)` and `(2,9,4,5)` collide
at `nu=2` on `(dp,dq,M,kbar,X,w_tr)=(40,5,5,45,360,18)` and separate
by `lambda in {0,23}` and by family key. Keying the ledger on the
labelled record is mandatory; keying on the cell tuple is not.

---

## 5. Attack 3 — Theorems D / E

### 5.1 T1-GEN from the printed equation: CONFIRMED

Start from `rho*p*q' - p'*q = C*p` with
`p = eta^eps * Pfull(t)`, `q = eta*W`, `W = Rad*S`, `t = eta^nu`.
Then `t' = nu t / eta`,

```
p' = eta^{eps-1}(eps*Pfull + nu t Pfull_t),
q' = W + nu t W_t.
```

Substituting and dividing by `eta^eps * Pfull` (justified as a
polynomial identity: an independent second `Poly` class verified
`lhs - eta^eps Pfull * reduced = 0` identically in `eta` and the
symbolic pattern coefficients) yields exactly (T1-GEN). Equal
multiplicities collapse to (T1-EQ) by `dlog = mu Rad_t`.

Independent identities: T1-EQ on a 3×3×(eps<mu)×2×2 grid plus the
packet's 216-cell grid; T1-GEN on `([1],3,2,3)`, `([2,1],0,0,7)`,
`([2,2],1,0,3)`, `([1,1,1],0,1,2)` and the packet's eight mixed
tuples; three deliberate mutations (sign on `t Rad_t S`, dropped
`nu`, `mu <-> eps`) all detected. Packet tests 5810/5810 under
`python3` and `python3 -O`. No sampling.

### 5.2 Specializations: CONFIRMED, no gluing inferred

- Class B/C, one nonzero orbit of multiplicity 1, `eps = mu_0`:
  (T1-GEN) is `sol-td7-law.md` (3) verbatim. Coefficient ratio
  `beta_k/alpha_k` is equation (4) verbatim, including identity (8)
  `mu_0(l+1)-1+dq = dp(l+1)`, on all six charged tuples plus
  `(4,7,2)`. The promoted class-B cell `(3,9,2,3)` is T1-dead iff
  `dp | dq`. Scope note demanded by E3: this `dp|dq` law is
  shape-specific and must not be applied to equal-arrival U1.
- Family A (`eps=0`, `mu=1`, `r=2`): (T1-EQ) is the `l1_ode_check.py`
  family-A expression termwise.
- Family C (`n=(2,1)`, `eps=0`, `S=1`): (T1-GEN) with those
  multiplicities; the packet identity holds on `([2,1],0,0,7)`.
- D9 / `nu=1`: `rho=2/(2+l)` times the divided identity is
  `2 p s' - l p' s = (2+l)C`. Even-`l=2n-2` residue
  `(-1)^{n-1} binom(2n-2, n-1) != 0` for `n>=2`. `l=2` residue `= -2`.

C1: the `td=6` cell `(r,nu,l)=(2,3,1)`, `(dp,dq)=(6,10)` returns
`pi_1^2/pi_0 = 6`, i.e. root ratio `2 ± sqrt(3)`, matching
OBSTRUCTION O. Independent reconstruction, not a lookup.

C2 as a negative control of Theorem A: D9 is `mu=1`, `eps=0`,
`r=2`, `lex=l>=1`, hence `C=l>=1`, hence bounded. With `T=2` and
`E = l nu+1 <= 4` at `w=2`, the only `nu>=2` pair in range is
`(l,nu)=(1,3)` with integer `kbar` (the pair `(1,2)` has
non-integral `kbar`). This is SHEET6-DEPTH §6's `td=6` menu cell,
not a semilinear family. CONFIRMED.

No gluing, landing, or coefficient-tier existence is read out of D/E.

### 5.3 Theorem E: CONFIRMED, including nonzero RHS and side conditions

On U1, `S=1`, `dq*(T1-EQ)` is identically

```
nu*(mu-eps)*[ r*Rad - t*Rad_t ] = C*dq.
```

Independent check: `dq * coeff_j = nu*(mu-eps)*(r-j)` for
`j=0..r`. Top `j=r` vanishes; `j=1..r-1` never vanish on the U1
range; `j=0` gives `C = -nu r (mu-eps) A / dq` with `A = -pi_0`.
Hence `Rad = t^r - A`, and `C != 0` iff `A != 0`. The `r` roots of
`t^r - A` are distinct and nonzero for `A != 0` in characteristic 0;
`q = eta*Rad` then has simple roots, `eta || q`, matching R1.0.
`A=0` is the excluded `C=0` and also puts a 0-root in `Rad`.

The rigidity is uniform in `nu` at pattern tier: the same
codimension-`(r-1)` condition on the `t`-roots, for every `nu`.
Whether arriving pole bases `c_e` can realize `c_e^{nu}` as the
`r`-th roots of one number, for infinitely many `nu`, is gluing /
monodromy and is not claimed. Correct.

---

## 6. Attack 4 — Theorem F (semilinear sufficiency)

### 6.1 Listed combinatorial grammar: no missed kill-consumer of full `nu`

The listed grammar is (S), (NE), (R), (I), N1, MP2, St 8.4, R2.1/R2.2,
P0/P1/P2, the §11 T1 law, and §11a E5 matching.

| consumer | depends on full `nu_G` / `kbar_G` / labels? | status |
|---|---|---|
| (S), (NE), (R) | no (U1: `mu>eps` constant) | constant |
| (I), N1, MP2 | congruence in `nu` | periodic, stored |
| `w_tr`, `lambda_G` | no | constant |
| trunk P0 menu, P1 `psi` | through `(w,M)` | periodic |
| T1 at `G` (pattern) | no (E is uniform) | constant |
| `gcd(M, nu)=1` (R2.2) | automatic on U1 | not a filter |
| St 8.4 `mu \| M_H` | arriving chain | not `nu_G` |
| `n_e in N*`, `i`-sync | affine in `kbar_G` | rider; stage-R never-kill; finite threshold |
| later case-III 0-edge leaving this vertex | yes, printed 5c | the named consumer |
| `{c_e^{nu}}` / gluing | yes, if that tier is in scope | rider 3; excluded from combinatorial claim |

A missed **combinatorial kill-consumer** of full `nu` was not found.
Edge labels and source coefficients are read by T1 only through the
`t`-roots, and E makes that constraint uniform. If the coefficient /
gluing tier is promoted into the ledger, `{c_e^{nu}}` **is** a
full-`nu` consumer and semilinear sufficiency at that tier is not
proved. The report does not promote that tier. Theorem F, at the
grammar it lists, stands.

The unique-consumer bound "sol56 bounds `h = nu_H = nu_G`" is the
printed mixed handshake. Fable's review of that theorem is
`REPAIR_REQUIRED`: at the promoted E5 pin the handshake variable is
`nu_G w_U` of the *later* merge, the incoming index is free, and
Sol56's headline object is the superseded side. Under E5 the named
consumer **vanishes** (the report's own C6 / E2 already says this).
Under printed 5c the consumer exists and would bound the U1 parameter
when this merge is a 0-leaving vertex, but that handshake is not the
promoted one. Repair: drop the Sol56 citation as a bound; at promoted
scope there is no combinatorial full-`nu` consumer at all. That
strengthens F, it does not break it.

Riders 2–3 ( `n_e`, gluing) are correctly typed as non-kills at the
recorded policy. Hash/equality rules (minimal period, labelled
record, no floats) are the right answer to the prior falsifier's
Attack A (`(w,M)` and `(w,M, nu mod M)` too coarse) and to Sol56 L3's
request for a labelled semilinear record.

---

## 7. Attack 5 — the `td=12` witness, and U2

### 7.1 Actual source entry row: unique type `(2,3)`, not unknown

Current `book_offaxis.census` (L6-surviving off-axis entries,
`tdmax=14`):

```
td=12, m=3: raw=1, l6=1
  type (2,3), Lambda=(4,4,4),
  poles (a,b,nu)=(1,2,3) three times,
  M=[2,2,2], w0=3/2, 3/2, 3/2.
```

Across `td=6..14` the M-vector `[2,2,2]` occurs once. Types `(2,5)`
and `(3,5)` cannot appear at `m=3`, `td=12` because `m*beta = 15 > 12`
(Prop. 5.7). Type `(3,4)` would need `Lambda=(4,4,4)=beta`, hence MP4
forces `b=1`, contradicting `[2,2,2]`. The report's rider that those
three types "also admit `[2,2,2]` at `td=12`" with
`w_0 in {13/10, 13/12, 1}` is obtained by illegally keeping
`Lambda_i=4` off the type that licenses it. **False rider, unique
source row, displayed numbers are the source numbers.**

The fail-closed emitter spec in §6.4 is therefore idle for this row:
the gates (G-a)–(G-e) pass on the unique entry. `entry_is_forced: True`
in the charged JSON is correct; the body's "until that row is read"
hedge is not.

### 7.2 Merge-local data, MP conditions, T1, trunk, terminal, budget

U1 family `(r,mu,eps,w)=(3,2,0,3/2)`:

```
dp=6 nu, dq=3 nu+1, E=2, kbar=3(3 nu+1)/2, X=9 nu,
M=2, w_tr=9/2, lambda_G=0,
admissible: nu odd and nu !== 0 (mod 3), nu>=5
           period 6, residues {1,5}.
```

Independent check on `{5,7,11,13,17,19,23,25}`: (S), N1, integer
`kbar`, `M=2` all hold. `B'=2`, `R=3` match Theorem C. MP1 admits the
star `r=3` (also admits a binary hierarchy, which is a different
configuration and is not needed). St 8.4: `mu=2 | b_i=2`. Arrival
from the pole vertices at `lambda=0` is the P2 entry clause
`(nu_i, mu|b)` with `nu_i=3`. MP6(b): `deg p_{P_i} = b alpha = 4 = i mu`
with common `i=2`. MP6(a) is **not** applicable (all `mu_e=2`); `k=0`
is a U1 choice, not an MP6(a) forcing. MP2: interior `M=2`. T1: alive
with `c_1^{nu}+c_2^{nu}+c_3^{nu}=0` and `e_2=0`, uniformly; no
realizability of those `c_e` is claimed.

No M-preserving clean resonant step from `w=9/2`, `M=2`: `l | 2`,
`l=1` emits `M=1` (MP2-dead on the trunk); `l=2` resonance needs
`Delta | 9`, `Delta>=3`, and `n, nu` both odd, hence
`(n-1)nu in {2,8}`, which has no odd `nu>=3`. CONFIRMED.

Exhibited dirty step
`l=2, eps=0, k=1, m=(1), lex=0, nu=25`:

```
dp=75, dq=51, E=27, kbar=17, X=25, w -> 2/3, M -> 3, lambda=8.
```

(S), (NE), (R), N1 all hold. Terminal `(2/3, 3)`: `j=M(1-w)=1 in N*`,
`psi=2`, budget `td-1-psi=9`, `Sigma lambda = 8 <= 9`, slack 1.
Charged `trunk_probe.py --w 9/2 --M 2 --budget 10 --depth 3` reproduces
this terminal as the first hit, and the JSON hash
`5a39a1b14d0820f37ef43e9f96984edc4517d326c6c02bfa13dbf77f07639824`
matches the target. Because `(w_tr, M)` is constant on the family, the
same trunk route is available at every admissible `nu_G`.

Honest budget: `lambda` values are P0 lower bounds; slack 1 means one
new printed unit kills the route. Trunk-chain Prop. 8.1(iv) is not
solved (the §11 law is a merge-cell law). R4: alive is not existent.
No panel status changes (`BOOK-OFFAXIS.md` §4 already records `td=12`
composite as open). All of that is correctly disclosed.

### 7.3 Status of the witness

This is a **real conditional counterfamily** at recorded
pattern / superset scope, not a false family and not a formal
`(f,g)` existence. It is a counterfamily to any reading of the
off-axis endpoint as a finite set of cells, and it is consistent
with reading that endpoint as a finite set of labelled semilinear
families. Conditionality is the inherited P0/R4/`lambda`-lower-bound
perimeter plus unsolved trunk-chain T1 plus unsolved gluing of
`t^3 - A`, **not** an unknown global type. The type is known.

### 7.4 U2: CONFIRMED distinct and unclosed outside `td=7`

U2 is `nu_G=1` (case I, `kbar in Q`), equal `(mu,w)`, unpriced `lex`.
`w_tr = mu*w*(r+lex)/((mu-eps)+mu*lex)` (at `k=0`) is strictly
monotone in `lex` and takes infinitely many values, with limit `w`.
The `td=7` class-A tail is the specialisation `mu=1`, `w=2`, `r=2`:
`dq=2t`, `lex=2t-3`, `w_tr = 2 + 1/(t-1)`, matching P3's printed
formula. It is not U1 (`mu=1` is MP2-dead at `lex=0`; live class-A
cells need `lex>=1`, which is bounded, or `nu=1`). P4 prices the
tail out at `td=7` by first-step inversion, no caps. P5 states that
at `td>=8` the budget `td-2 >= 6` exceeds the `<=5`-unit cost of the
`td=7`-style escapes, so budget does not close those panels. U2 is
therefore a genuine second unbounded reduced-state regime, a chain
theorem does not cover it, and it is currently closed only at `td=7`
and only by budget. CONFIRMED.

Sol56's finite reduced P0-chain theorem remains compatible with U1
(`w_tr` constant, `M` periodic ⇒ finite reduced merge-child states)
and does not cover U2. That reconciliation is correctly drawn.

---

## 8. Strongest promotion-safe residue

After the local repairs of §1, the following may be promoted at
**explicit recorded formal / superset scope**, no AWS, no JC2, no
landing, no panel-status change, no gluing.

> **Theorem (U1 semilinear quotient, repaired).**
> At a merge with `r>=2` nonzero arrivals, no 0-arrival, and the
> P0/R2.1/R2.2/N1/MP2 legality predicate of `BOOK-OFFAXIS.md` §10
> and `SHEET6-III.md` §3:
>
> 1. Two-edge consistency is affine with two coefficients. Both
>    vanish for infinitely many `nu` iff all `mu_e` are equal, all
>    `what_e` are equal, and `T != 0`. A single `C_e=0` edge never
>    suffices. Case III is `nu_G`-bounded under both H5a readings
>    and is pinned to one value under promoted E5.
> 2. With equal `mu`, `C = mu*(k+lex)-Sm >= k+mu*lex`, with equality
>    iff `k=lex=0`. If `C != 0` then `kbar` is strictly monotone in
>    `nu` with finite limit `mu*w*s/C` (increasing if `T>0`,
>    decreasing if `T<0`), so only finitely many `nu>=2` are legal.
> 3. The remaining family (U1) has the closed forms of Theorem B,
>    including the exact law `M = gcd(mu-eps, r*nu+1)`, constant
>    `w_tr` and `lambda`, and affine unbounded `kbar, X, dp, dq`.
> 4. Admissible `nu>=2` form an explicit finite union of arithmetic
>    progressions, infinite iff nonempty. Nonemptiness requires
>    `gcd(r, B')=1` and an interior MP2 class not emptied by N1.
>    `nu=1` is exceptional (regime U2), never a member of the AP.
> 5. Downstream reduced state: `w_tr`, `lambda_G`, and the merge T1
>    verdict are constant; `M` and the trunk P0 menu are periodic
>    (constant on families with constant `M`). No numerical `kbar`
>    cap is required for the combinatorial pattern-tier ledger. The
>    unique normalized record is `EQJOIN-FAMILY/v1` with minimal
>    period, labelled members, and the stated hash rule.
> 6. Prop. 8.1(iv) at a general merge is (T1-GEN). On U1 it is
>    `Rad = t^r - A` with `A != 0` and
>    `C = -nu r (mu-eps) A / dq != 0`, uniformly in `nu`. T1 does
>    not kill U1; it rigidifies coefficients at pattern tier.
>
> **Not in this theorem.** Regime U2; coefficient/gluing realizability
> of `t^r - A`; trunk-chain T1; any later case-III handshake (printed
> or E5); existence of an absolute `(f,g)`.

> **Witness (conditional, source-pinned).** The unique L6-surviving
> off-axis entry at `td=12`, `m=3` is type `(2,3)`,
> `Lambda=(4,4,4)`, poles `(1,2,3)^3`, `M=[2,2,2]`, `w_0=3/2`. The
> star merge is the U1 family `(3,2,0,3/2)` with the AP of §7.2, and
> the dirty trunk step `l=2, k=1, nu=25` reaches a P1 terminal
> `(2/3, 3)` at `Sigma lambda = 8 <= 9`. R4 and the `lambda`-lower-
> bound rider are inherited. This is an infinite pattern-tier
> budget-fitting family, not a cell-finite book and not a
> realizability theorem.

---

## 9. Clause-level scorecard

| clause | verdict | note |
|---|---|---|
| A, necessity of 1–4 for unbounded `nu>=2` | CONFIRMED | two-coefficient residual |
| A, sufficiency / iff as legality | **REPAIR_REQUIRED** | MP2 and (I) can empty a 1–4 family |
| A, unequal `mu` / unequal `w` | CONFIRMED | C5 24,416 charged |
| A, free 0-roots in U1 | CONFIRMED | `C` independent of `eps` |
| A, non-chain orbits | CONFIRMED | `C >= k + mu*lex` |
| A, `lex` at `nu>=2` | CONFIRMED | monotone `kbar`, finite window |
| A(b) "decreasing" | **REPAIR_REQUIRED** | sign of `T`; finiteness stands |
| A, printed case III | CONFIRMED | `C_0 >= 1` |
| A, promoted E5 pin | CONFIRMED | with (S); packet classifier does not run E5 |
| A, omitted unbounded-`nu` regime | none found | U2 is listed, not omitted |
| A, circular integrality | none | underused in the iff, not circular |
| B, `M = gcd(mu-eps, r*nu+1)` | CONFIRMED | exact, two-sided |
| B, `kbar, X, w_tr, lambda` | CONFIRMED | lambda density `mu w r / eps` |
| B, `r` even ⇒ `M` odd | CONFIRMED | `m=2` headline scoped to §1 |
| C, `B'`, AP, `gcd(r,B')=1` | CONFIRMED | |
| C, N1 radical `R` | CONFIRMED | |
| C, exceptional `nu=1` | CONFIRMED | |
| C', `w_tr` / `lambda` / T1 constant | CONFIRMED | |
| C', P0 menu "constant" | **REPAIR_REQUIRED** | periodic in general |
| D, T1-GEN identity | CONFIRMED | independent Poly, mutations live |
| D, four printed specializations | CONFIRMED | no gluing inferred |
| E, `Rad = t^r - A`, `C != 0` | CONFIRMED | `dq*coeff_j = nu(mu-eps)(r-j)` |
| E, local R1.0 side conditions | CONFIRMED | |
| F, combinatorial sufficiency | CONFIRMED | at the listed grammar |
| F, Sol56 as unique-consumer bound | **REPAIR_REQUIRED** | Fable handshake; E5 consumer vanishes |
| F, missed combinatorial consumer | none found | gluing excluded by rider 3 |
| G, family uniqueness / cell collision | CONFIRMED | C4 |
| `td=12` source type | CONFIRMED unique `(2,3)` | other-types rider **false** |
| `td=12` merge / MP / trunk / budget | CONFIRMED | slack 1, lambda lower bounds |
| `td=12` as formal `(f,g)` | not claimed | correctly |
| `td=12` as conditional counterfamily | CONFIRMED | pattern / superset, type now pinned |
| U2 distinct, unclosed off `td=7` | CONFIRMED | P3/P4/P5 |
| reconciliation with Sol56 chain theorem | CONFIRMED | U1 compatible, U2 out of scope |
| errata E1–E8 to the prior Opus report | CONFIRMED as repairs | E3 especially |
| packet replay, hashes, `-O`, caps | CONFIRMED | 5810/5810, emit byte-identical |
| JC2 / landing / panel change | none claimed | firewall held |

---

## 10. Narrowest maximum consequence

At recorded pattern / superset scope, equal-`(mu,w)` nonzero-arrival
merges with `k=lex=0` are a semilinear family with finite reduced
child states, not a numerically `kbar`-bounded cell list and not an
undetermined stage-R haze. The unique `td=12`, `m=3`, `[2,2,2]` source
entry carries one such family that fits the shared St 9.4 budget with
slack 1, for every admissible `nu`. This does not close any `(m,td)`
panel, does not produce an `(f,g)`, does not bound `td`, and does not
touch JC2. Regime U2 remains the one place where the reduced merge-child
state set is proved infinite. Canonical promotion is authorized only
for the repaired residue of §8, at that explicit scope, with no AWS.

---

## 11. Exact next research target

The target's item 2 (read the missing `td=12` entry row) is discharged
by the current census: the row is unique of type `(2,3)`. Do not spend
a further desk day on alternative types.

The highest-leverage remaining object is still **regime U2**: a
Prop. 9.3 case-I merge with equal `(mu,w)` arrivals, `nu_G=1`,
`kbar in Q`, unpriced `lex`, and `w_tr` taking infinitely many values.
Question, as the target ranks it: is `w_tr` compatible with a legal
P1 terminal for infinitely many `lex`, given MP2 and `j = M(1-w_t) in N*`?
A negative answer completes Sol56's skeleton to a merge theorem. A
positive answer is a second, sharper counterfamily.

Second, after U2 or in parallel at the U1 coefficient tier: can `r`
arriving chains, each with its own pole Puiseux data, have `c_e^{nu}`
equal to the `r` distinct `r`-th roots of one number, for infinitely
many admissible `nu`? That is the first place a U1 kill can still come
from. It is gluing / monodromy, not a `kbar` bound.

Do not seek a numerical `kbar` cap at equal-`(mu,w)` joins. After the
A-repair, the family is genuinely infinite at pattern tier whenever
the AP is nonempty.

---

## 12. Scope firewall

This review does not assert: a landing theorem; completeness at any
`td`; restoration of a prime-`td` exclusion; realizability of any
cell or family; an adjudication of CONJECTURE H5a or `U_7C` beyond
Fable's already-stated handshake correction; `G2-BD`; `G2-PSC`; a
cofinal bound on `td`; or any JC2 consequence. It does not access
`jc2-lean`. It does not promote Theorem A as written, the other-types
rider, or Sol56's incoming-index bound as a U1 consumer.

P5's generic `0 DEAD / 0 ALIVE / 2691 OPEN` remains the honest
grid-level statement. What changes is that one named open panel now
contains an exact infinite labelled family rather than an unenumerated
haze, at pattern / superset scope only.

---

## 13. Replay

Commands run this session, ordinary and `-O` where charged:

```sh
cd cases/m2_equal_join_semilinear_opus5_20260829
python3    emit_eqjoin.py --output /tmp/eqjoin_review.json
python3 -O emit_eqjoin.py --output /tmp/eqjoin_review-O.json
cmp /tmp/eqjoin_review.json /tmp/eqjoin_review-O.json
python3    test_eqjoin_semilinear.py
python3 -O test_eqjoin_semilinear.py
python3    trunk_probe.py --w 9/2 --M 2 --budget 10 --depth 3 --output /tmp/trunk92_review.json
```

Observed:

```
emit_sha256 3914fd3c62bdecc59d250292bd98751054fa4a9ffc9b2e9dcae115745b734da6
t1_identities 13
families 8
EQJOIN_EMIT_PASS
CMP_OK
EQJOIN_SEMILINEAR_TEST_PASS checks=5810
EQJOIN_SEMILINEAR_TEST_PASS checks=5810
one_step_menu 9
terminals_reached 9
states_seen 60 depth 3
  TERMINAL w=2/3 M=3 spent=8 psi=2 ['dirty(l=2,eps=0,k=1,lex=0,nu=25)->w=2/3,M=3']
trunk json 5a39a1b14d0820f37ef43e9f96984edc4517d326c6c02bfa13dbf77f07639824
```

Independent `/tmp` work, not imported from the packet: a second
sparse-polynomial T1 identity checker (83/83, three mutations
detected); closed-form / AP / consistency / td-12 / C4 / C5-clean
desk identities; `book_offaxis.census` of the `td=12` row; kbar
monotonicity against the sign of `T`; E5 contradiction with (S)
enforced (0 legal double degeneracies). Cap tokens were not accepted
by either charged executable.

Files written: this path only. Scratch under `/tmp` only.

**Verdict: `REPAIR_REQUIRED`.**

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = cf935fe9674aa36cf7f73eaaee841c7b38307707a6e39416d1a0afe02a0c6d39
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 37608 bytes)
