# Hostile review — Sigray Prop. 4.2 constant-shift repair (Opus 5, r1)

Reviewer: **Opus 5** (`claude-opus-5`).  This is a **different-model hostile
review**: the frozen producer was written by a different model, and nothing
below reuses its reasoning as evidence.  Every mathematical claim was
re-derived from `refs/sigray_full.pdf` directly.

Date: 2026-08-28.

## Terminal verdict

**REPAIR.**

The mathematical core is correct and I reproduce it independently: the fiber
residual lemma, the complete zero-bracket trichotomy, the uniqueness and
immediate termination of the constant-shift step, the terminal order and
degree formulas, and the `T_a^nearrow` location theorem all survive hostile
re-derivation.  The producer is downgraded because its §6/§7 typing claim is
**not complete**: at least five printed downstream arguments on `T_a^+`
(the p. 20 Remark, Prop. 4.4's "In particular" clause, Prop. 5.2,
Prop. 5.3(ii), and the displayed ratio identities inside Props. 6.2 and 6.3)
silently require `l_j >= 1`, equivalently `d_(h_j,F) != 0`, and two of them
literally divide by `d_(h_j,F)`, which is exactly zero at the newly admitted
corner.  The `T_a^searrow` firewall of §5 does **not** cover them, because
they are stated on `T_a^+` / `T_a^nearrow`.  The smallest exact repair is
given in §9; with it the audit entry may become an erratum.

## 1. Live hashes (recomputed this session)

Producer, re-hashed before reading, matches the charge:

```text
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
```

Primary source and auxiliary artifacts, all matching the charge:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
8396a44c5f81f011a8a343124bd0de21329d0f1756a99fcf4cc9df718baf3e14  cases/sigray_prop42_constant_shift_repair_20260828/verify_constant_shift.py
c57abd5f0a49dd39fc1b2aa5acf763e3df7948d16034f867fb1aef6b52b0f183  cases/sigray_prop42_constant_shift_repair_20260828/CUSTODY.md
```

Non-authoritative context read for downstream scope only, hashes matching
`CUSTODY.md`:

```text
f4964e2fdfef7b3081a3effb0f54eb2cac0f52d34a7c1118ef329ddefc2090d2  ladder/SIGRAY-AUDIT.md
5751fdacd00351b84c4fc14f7203eeca1265bda78f24099441230ed04056fb5b  xmodel/sol-landing1.md
e88ef03a7edbf6128de1e54be7a029e23e776e12422a205f9493b6a52c1d9447  xmodel/sol-gluing-design.md
```

Producer preserved byte-for-byte; the only write in this session is this
review file.  No `jc2-lean` path was entered, listed, searched, read, built,
statused or modified.  No web, no AWS, no CAS.

## 2. Custody verification and source anchors

The custody map is accurate.  With
`pdftotext -f 18 -l 21 -layout refs/sigray_full.pdf - | nl -ba` I confirm
Prop. 4.2 at lines 51--151, its statement at 51--71, (9) at 94--97, (10) at
101--109, the invalid inference at 120--126, the `delta_j` descent at
131--147, the **Remark** at 150--151, Prop. 4.3 at 153, Prop. 4.4 at 204.
The PDF page number equals the printed page number.

Anchors used below (printed pages):

- p. 10, Statement 3.1: at `P in bar(R_a)\R_a` either `x(P)=inf, y(P) in C`
  with `y = sum c_j x^(-j/kappa)`, or the transposed form.  Two charts.
- p. 11--12, Definition 3.3 / Notations 3.1, 3.6: `T_a = T_a^* ∩ pi^(-1)(Q)`,
  so **every** `F in T_a` is `I_P(u)` for some branch `P`.  `(0,y):=(P,0)~`.
- p. 13, Notation 3.9: `eta_F := x^pi(F)(y - sum_(j<pi(F)) c_j x^(-j))`;
  Statement 3.7: `h^F = sum_j x^(j/kappa) p_j(eta)`, finitely many `p_j != 0`;
  Notation 3.10: `h_F^+ := xi^(j/kappa)p_j`, `j` the **largest** index with
  `p_j !≡ 0`, `d_(h,F):=j/kappa`, `p_(h,F):=p_j`.
- p. 15--16, Statement 3.9 (i)(ii)(iii); Notation 3.13 `p_F:=p_(f,F)`;
  Notation 3.14 `T_a^+ := {F in T_a : pi(F) in Q_+, d_F > 0}`.
- pp. 19--20, Prop. 4.2 (i)--(iv), (9), (10), the disputed sentence, the
  `delta_j` descent, and the Remark.
- p. 21, Notation 4.1 and Prop. 4.4; p. 22, Prop. 4.5.
- p. 23, Prop. 4.6 and (11)--(17).
- p. 24--25, Prop. 5.2, Notation 5.2, Prop. 5.3 (i)--(ix).
- p. 29, Notation 6.1, Statements 6.1--6.2, Prop. 6.2.
- p. 30--31, Prop. 6.3, Prop. 6.4; p. 32, Corollary 6.1, Prop. 6.5.
- pp. 39--40, Notation 8.1, Statement 8.1, Prop. 8.1.
- p. 48, Notation 9.1 `Q(F)`; pp. 49--50, Statements 9.4--9.5, Prop. 9.2,
  Prop. 9.3.

**Glyph pin (needed for §7).**  `pdftotext` renders the two arrow classes of
Notation 6.1 as the raw bytes `%` (0x25) and `&` (0x26) while genuine Unicode
(`∈` = `E2 88 88`) is emitted properly; the page-29 font is `CMSY10`, whose
slots 0x25/0x26 are `\nearrow`/`\searrow`.  Hence

```text
T_a^nearrow  = {F in T_a^+ : d_F > (1-pi(F)) deg p_F}
T_a^searrow  = {F in T_a^+ : d_F < (1-pi(F)) deg p_F}
```

Cross-checked semantically: Statement 9.4's proof asserts
`(0,x) in T_a^nearrow`, and Prop. 6.5's proof derives exactly
`(0,x) not in T_a^searrow` from Prop. 6.4.  The producer's identification is
correct.

## 3. The printed gap, restated from the source

Printed p. 20, lines 120--122, verbatim from the extraction:

> Then it can be easily proved, that there exist `k_j , l_j in N*` and
> `s_j in C` with (i) and (iii).  Moreover, since `h_j` is a non-constant
> polynomial, `s_j != 0` and `l_j != 0` and `k_j , l_j` are uniquely defined.

`h_j` non-constant is a statement about the *global* polynomial; `l_j != 0`
is a statement about its *leading Laurent part* `h_(j,F)^+`.  The inference
is invalid, exactly as `SIGRAY-AUDIT.md:54` files it.  Note also the printed
arity slip already on record there: `(k_0,...,k_(m-1))` has `m` entries but
is typed `in N*^(m-1)`.

## 4. Charge 1 — fiber residual `p_F` is nonconstant.  **CONFIRMED.**

Claim: for every `F in T_a^+`, `deg p_F >= 1`.

*f versus f-a.*  `Notation 3.13` defines `p_F := p_(f,F)`, **not**
`p_(f-a,F)`.  This matters, and it is harmless **exactly on `T_a^+`**:
`(f-a)^F = f^F - a` differs only in the `j=0` coefficient, and on `T_a^+` the
leading index is `kappa d_F > 0 > ` nothing, i.e. strictly positive, so
`p_(f-a,F) = p_(f,F)` and `d_(f-a,F) = d_(f,F)`.  (On `T_a^0` they differ,
which is precisely why Statement 3.14 on p. 16 splits `T_a^+` from `T_a^0`
with the `-(b-a)` correction, and why the audit's `p_(f-a,F)` slip family is
inert here.)  The producer's phrasing "`f=a` is finite while `d>0`" captures
this; I confirm it is sound on `T_a^+` and would be unsound on `T_a^0`.

*Proof, both charts.*  By Notation 3.6 every `F in T_a` is `I_P(u)`.  In the
`y`-chart, `eta_F = x^u(y - sum_(j<u)c_j x^(-j)) -> c_u =: gamma in C` along
the branch, since the Puiseux series (3) has only exponents `<= 0` in `x`.
Along `P`, `f = a`, so `sum_j x^(j/kappa)p_j(eta_F) = a` with top index
`n = kappa d_F > 0`.  Each `p_j(eta_F) -> p_j(gamma)` is finite, so the
subleading part is `O(x^((n-1)/kappa)) = o(x^(n/kappa))`.  If
`p_F(gamma) != 0` the sum is asymptotic to `x^(d_F)p_F(gamma) -> inf != a`.
Hence `p_F(gamma) = 0`, and since `p_F !≡ 0` by Notation 3.10, `deg p_F >= 1`.
The `x`-chart (`T_(x,a)`, form (4), `y -> inf`) is the literal transpose. ∎

*Traps checked.*
- **Zero next coefficient.**  `gamma = 0` is allowed; `p_F(0)=0` still gives
  `deg p_F >= 1`.
- **Axes.**  `F=(0,y)` has `pi(F)=0`, empty subtraction sum, `eta_(0,y)=y`,
  so `d_(h,(0,y)) = deg_x h` and `p_(h,(0,y)) =` leading `x`-coefficient.
  If `(0,y) in T_a^+` then `deg_x f > 0` and the argument applies verbatim
  with `gamma = c_0`.  Prop. 5.3(i)'s proof asserts the `x`- and `y`-degrees
  of `f` and `g` are positive, so `(0,x),(0,y) in T_a^+`.  No axis exception.
- **Finite truncations.**  `F` *is* a finite truncation `I_P(u)`; and
  Statement 3.7's expansion is finite, so "largest index" in Notation 3.10 is
  well defined.  Nothing degenerates.
- The lemma is sharp: it fails on `T_a^0`, so the producer's warning against
  exporting the repair to arbitrary Laurent charts is correct and necessary.

## 5. Charge 2 — negative order is impossible.  **CONFIRMED.**

*Transformed Jacobian.*  With `xi = x`, `eta = eta_F`, `det D(phi) = x^u`, so
`J_(x,y)(A,B) = xi^u J_(xi,eta)(A^F,B^F)`; this reproduces Prop. 4.1's
`J(f^F,(g-b)^F) = xi^(-u)` from `J(f,g)=1`.  Directly,

```text
J_(xi,eta)(xi^d p, xi^e q) = xi^(d+e-1)(d p q' - e p' q),
```

which is where the `d_F + d_(h,F) - 1` of Prop. 4.1 and (10) comes from.  So
`J(f_F^+,H_F^+) = 0  <=>  d p q' - e p' q ≡ 0`.  The producer's (2.2) is
correct.  (Its sentence about the "nonzero monomial factor" is loose — the
displayed Jacobian is already the `(xi,eta)` one — but nothing rests on it.)

*e < 0 impossible.*  `d, e in (1/kappa)Z`.  Put `A := kappa d in N*`,
`B := -kappa e in N*`.  Then `A p q' + B p' q = 0`, and

```text
(q^A p^B)' = q^(A-1) p^(B-1) (A p q' + B p' q) = 0,
```

so `q^A p^B` is constant in characteristic zero.  But `p, q != 0` (Notation
3.10) and `deg(q^A p^B) = A deg q + B deg p >= B * 1 >= 1` by Lemma 1.
Contradiction. ∎  Denominator clearing is legitimate (one `kappa` clears both
orders); the derivative computation is exactly as written.

*Countermodel hunt.*  I actively searched the failure modes named in the
charge:
- **Inverse/Laurent.**  `A = xi`, `B = xi^(-1)`: `d=1,e=-1,p=q=1` gives
  `dpq'-ep'q = 0`.  A genuine countermodel to the unrestricted claim, killed
  by `deg p >= 1` only.  The producer flags this correctly.
- **Monomials.**  `p = eta^a`, `q = eta^b` gives `(Ab+Ba)eta^(a+b-1)`, zero
  iff `a=b=0`, i.e. iff `p` is constant.  Same firewall.
- **Zero polynomials.**  Excluded by Notation 3.10's "largest index with
  `p_j !≡ 0`"; and `h_j != 0` because `h -> h^F` is the substitution
  `y |-> x^(-u)eta + sum c_j x^(-j)`, invertible over the Laurent extension.
- **Cancellations / roots at infinity.**  The obstruction is a pure degree
  count, `A deg q + B deg p >= 1`; no leading-coefficient cancellation can
  occur because both `A,B > 0` and both degrees are `>= 0`.
- **Machine probe (audit of the checker, no new artifact).**  Removing the
  `deg(p)>=1` filter from the frozen checker's own enumeration yields **36**
  counterexamples at `deg p = 0` — all with `q` constant, matching the hand
  proof.  Widening the alphabet to `{-2..2}`, degrees `<= 2`, orders
  `d in {1/3,1,5/2}`, `e in {-1/3,-1,-5/2}` gives **133920** checks and
  **0** violations.  The firewall is load-bearing and the theorem holds
  outside the producer's sampled alphabet.

## 6. Charges 3 and 4 — zero order, legality, immediate termination.  **CONFIRMED.**

*`e=0` forces `q in C*`.*  (2.2) becomes `d p q' = 0`; `d > 0` and `p != 0`
give `q' = 0`, so `q` is constant, and nonzero by Notation 3.10.  So the
stuck case is exactly `d_(h_j,F) = 0`, `h_(j,F)^+ = c in C*`.

*Uniqueness of `(k,l,s) = (1,0,c)`.*  With `gcd(k,0) = k` (the standard
convention, which the erratum must state in (i)), `gcd(k_j,0)=1` forces
`k_j = 1`, and then (iii) reads `h_(j,F)^+ = s_j`, i.e. `s_j = c`.  No
competing positive-`l` representation exists: `s(f_F^+)^l` has order
`l d_F > 0` for `l >= 1` because `d_F > 0`, while `(h_(j,F)^+)^k = c^k` has
order `0`.  So uniqueness holds across the **enlarged** parameter set, not
merely within it.

*`f^0` legality and non-constancy.*  (ii) becomes `h_(j+1) = h_j - c`, a
genuine polynomial identity (`f^0 = 1`).  `h_j` non-constant gives `h_(j+1)`
non-constant, which is required by the statement of Prop. 4.2 on p. 19 line
56.  The printed product formula
`J(f,h_(j+1)) = h_0^(k_0-1)...h_j^(k_j-1)` is preserved because `k_j = 1`
makes the new factor `h_j^0 = 1`, so `J(f,h_(j+1)) = J(f,h_j) != 0` and the
printed "cannot be a constant polynomial" line survives unchanged.

*Strictly negative successor order.*  `h_(j+1)^F = h_j^F - c` cancels
**exactly** the `xi^0` coefficient, which is the constant `c`; every
remaining coefficient has index `< 0`, and not all vanish (else
`h_j^F ≡ c`, hence `h_j ≡ c` by injectivity, contradiction).  So
`e := d_(h_(j+1),F) < 0` strictly.  Producer (3.5) correct.

*Immediate termination and the exact terminal equation.*  `alpha_(j+1) =
alpha_j + (k_j-1)l_j/k_j = alpha_j` since `k_j = 1`.  By (10) the next test
is either `0` or exactly `(f_F^+)^(alpha_(j+1)) xi^(-u)` — the dichotomy is
driven by the order equation, so "nonzero" and "equal to the terminal value"
are the same statement here.  §5's `e<0` result excludes `0`.  Hence
`m = j+1`, `mu = alpha_m = alpha_(m-1)`, and (iv) holds with its suppressed
nonzero scalar (the paper makes that scalar explicit as `c` in Prop. 6.4's
proof, `d_F p q' - d_(h,F) p' q = c p^mu`; the producer's blanket "up to the
fixed nonzero scalar" is the honest reading).

*`delta` bookkeeping, both routes, agreeing.*  Terminal order equality gives
`e = (mu-1)d_F + 1 - u`, hence

```text
delta_j     = kappa(d_F + 0 - alpha_j d_F - 1 + u) = -kappa e > 0,
delta_(j+1) = kappa(d_F + e - alpha_(j+1)d_F - 1 + u) = 0.
```

Independently, the printed descent identity, which I re-derived from p. 20
lines 142--147 using `k_j d_(h_j,F) = l_j d_F`, is
`delta_(j+1)-delta_j = kappa(d_(h_(j+1),F) - k_j d_(h_j,F))`; at the corner
`k_j = 1`, `d_(h_j,F)=0`, so it is `kappa e < 0`.  The two routes agree
(`-kappa e + kappa e = 0`), which is a real consistency check, not a
restatement.  So `delta_next = 0`, strictly stronger than `< delta`.
All index/off-by-one formulas check: the corner sits at `j = m-1`, produces
`h_m`, and contributes `0` to `mu`.

## 7. Charge 5 — degrees and typing.  **Formulas CONFIRMED; typing INCOMPLETE.**

### 7.1 The degree formula (4.3).  **CONFIRMED, and it is the paper's own (17).**

From `J(f_F^+,h_(m,F)^+) ≐ (f_F^+)^mu xi^(-u)` with `f_F^+=xi^d p`,
`h_(m,F)^+=xi^e q`: orders give `e = (mu-1)d_F + 1 - u` (this is literally
the paper's own line on p. 40, `l = d_(h,F) - k delta = (mu_F-1)d_F+1-u-k delta`),
and residuals give `d_F p q' - e p' q ≐ p^mu`.

*No cancellation.*  The `eta^(a+b-1)` coefficient is
`c_a c_b (d_F b - e a)`; with `d_F > 0`, `b >= 0`, `e < 0`, `a >= 1` we get
`d_F b - e a >= -e a > 0`.  This is correct **including `b = 0`**, where
`q' = 0` and the bracket degenerates to `-e p' q` of degree `a-1 = a+b-1`
with the same coefficient formula.

*Rational `mu`.*  `mu = alpha_m` is rational in general, so `p^mu` is formal.
The honest reading, which I verified, is that the residual of the leading
term of `J(f^F,h_m^F)` is `prod_i (p_(h_i,F))^(k_i-1)` of degree
`sum_i (k_i-1) l_i a / k_i = mu a`, an integer.  So `a + b - 1 = mu a`, i.e.

```text
b = (mu - 1) a + 1.
```

This is **exactly** the paper's (17) on p. 23 (Prop. 4.6), in the branch where
(16) `deg p / deg q = d_F/d_(h,F)` fails — and (16) *must* fail at a constant
corner, since it says `d_F b = e a`, impossible for `e<0<=b*d_F`.  Good
independent corroboration.  Note the producer derives (4.2) from its own
(3.4) rather than citing Prop. 4.6 — which is the **safe** route, because
Prop. 4.6 carries the hypothesis (7) that may itself fail at a `j=0` corner
(see §7.4).

### 7.2 `M_F` and `Q(F)`.  **CONFIRMED.**

Notation 8.1, p. 39, verbatim: `M_F := gcd(deg p_F, deg p_(h_0,F), ...,
deg p_(h_m,F))` and `M_F^*` the same without the last entry.  The corner
member contributes `deg p_(h_(m-1),F) = 0`, inert under `gcd(n,0)=n`, and the
terminal member contributes `b=(mu-1)a+1`.  So

```text
M_F = gcd(M_F^*, (mu-1) deg p_F + 1),
```

by associativity of `gcd`.  Producer (4.4) is right, and its operational
warning is right and non-obvious: **a compiler must not stop at the constant
member and set `M_F = M_F^*`**, because `h_m` still carries a degree slot.
`M_F >= 1` always since `a >= 1`.  Notation 9.1, p. 48, verbatim:
`Q(F) := (D_F, deg(p_F), nu_F, M_F, kappa_F(1-pi(F)))`; the other four slots
depend only on `F` and `f`, never on the `h`-tower, so they are untouched.
Producer (4.5) matches the source character for character.

Prop. 8.1 (p. 39) is stated on `T_a^searrow`, where §7.5 shows no corner
occurs; `i := deg p_F / M_F^*` stays in `N*`; and its internal step
`deg p_(h_j,F) = (l_j/k_j) deg p_F` is `0=0`-consistent at `l_j=0` anyway.
**Prop. 8.1 needs no patch.**

Notations 8.1 and 9.1 are **definitional labels**: they need only the
`gcd(n,0)=n` convention and the instruction to emit `h_m`.  Prop. 8.1 is a
proposition but is domain-firewalled.  The propositions that genuinely need
separate patches are listed next.

### 7.3 Divisions by the newly allowed `l = 0`.  **FOUND — five, unaddressed.**

`l_j = 0` is equivalent to `d_(h_j,F) = 0` and `deg p_(h_j,F) = 0`.  I
searched the printed downstream text for that quantity in a denominator or in
a positivity step.

1. **p. 20, the Remark** (lines 150--151): *"From the above proposition we
   also obtain that the condition (7) automatically holds in the case
   `d_F > 0`."*  Its only possible derivation is `k_0 d_(g,F) = l_0 d_F > 0`,
   which needs `l_0 != 0`.  Under the erratum the Remark becomes **precisely
   the assertion that no constant corner occurs at `j=0`** — i.e. it restates
   the gap instead of closing it.  `SIGRAY-AUDIT.md:54` already files this
   Remark as circular, so a "complete replacement" for that entry must
   dispose of it.  The producer never mentions it.
2. **p. 21, Prop. 4.4**, proof, the displayed chain
   `deg(p_F)/(kappa d_F) = deg(p_(h,F))/(kappa d_(h,F)) <= ...`.  Prop. 4.4
   *as stated* is safe (its hypothesis is `l,l* in N*`, and then
   `d_(h,F) = l d_F/k > 0`).  What breaks is its **"In particular"** clause,
   *"for any `F in T_a^+`, either `F ⪯ F^0` or `F^0 ⪯ F`"*, which is the
   tower-prefix typing the whole campaign consumes.
3. **p. 24, Prop. 5.2.**  "by Propositions 4.2, 4.4 and 4.5, there exist
   `k,l in N*` with `(g_F^+)^k = (f_F^+)^l` for each `F in T_a^+`.
   Consequently `k d_(g,F) = l d_F`.  ... this gives `d_F>0` iff
   `d_(g,F)>0`."  At `l=0` this reads `d_(g,F)=0` and the equivalence dies.
4. **p. 25, Prop. 5.3(ii)** proof: "hence `k/l = k_f/k_g`" — undefined at
   `l=0`.  This is on the pole side, so it is the one that matters most for
   the campaign.
5. **pp. 29--30, Props. 6.2 and 6.3**, both of which display
   `deg(p_G)/d_G = deg(p_(h_j,G))/d_(h_j,G)` resp.
   `mult(p_F,c)/d_F = mult(p_(h_j,F),c)/d_(h_j,F)` for indices `j < m`, i.e.
   including the corner index `m-1`.  Prop. 6.3's `G in T_a^nearrow` branch
   is exactly the sector where §5 puts the corner.

The producer's §5 firewall does **not** reach any of these: it excludes the
corner from `T_a^searrow`, whereas 1--5 are stated on `T_a^+` or
`T_a^nearrow`.  §6 of the producer lists six firewalls, none of which is this
one, and §7 nevertheless proposes "ERRATUM WITH COMPLETE REPAIR".  That is
the reason for the downgrade.

### 7.4 The good news: all five are repairable, cheaply.

I verified that no conclusion is lost.  Two facts do the work.

**Fact A (corner descent).**  Let `h` be any polynomial with
`deg p_(h,F) = 0` and `F = F^0 * c_n`.  Statement 3.9(i) (p. 15) gives
`mult(p_(h,F^0), c_n) = deg p_(h,F) = 0`, and then Statement 3.9(iii) gives
`d_(h,F) = d_(h,F^0) - 0/kappa`, i.e. **`d_(h,F^0) = d_(h,F) = 0`**.  If the
`F^0`-tower also has a vanishing leading Jacobian at that index, Lemma 2.2(2)
applied at `F^0 in T_a^+` forces `p_(h,F^0)` constant, and Statement 3.9(ii)
with `l = deg p_(h,F) = 0` forces `a_0 = b_0`, i.e. **the same constant `c`**.
Otherwise the `F^0`-tower has already stopped and `F^0 ≺ F`.  Either way
comparability holds — item 2 above is repaired, and items 5 are repaired by
replacing the ratio identity by its **cross-multiplied** form
`d_(h_j,F) mult(p_F,c) = d_F mult(p_(h_j,F),c)`, which is what the following
lines actually consume and which reads `0 = 0` at the corner (Prop. 6.3's
subsequent estimate then degenerates to the true `d_(h_j,G) >= 0`).

**Fact B (no corner on the axes).**  For `F=(0,y)`, `eta_F = y`, so
`h_((0,y))^+ = xi^(deg_x h) * (leading x-coefficient of h)`.  That is a
nonzero constant **iff `h` is constant**.  Since every tower member is
non-constant, *the constant corner can never occur at `(0,y)`*, and by
transposition never at `(0,x)`.  Since Props. 4.4/4.5 propagate the uniform
first-step `(k,l,s)` to `(0,y) in T_a^+` (Prop. 5.3(i)'s proof records that
all four partial degrees of `f,g` are positive), the uniform `l` is `>= 1`,
and **items 3 and 4 go through unchanged**.  Fact B also protects Prop. 4.5
and Prop. 6.5, whose proofs assume `k,l,k*,l* in N*` at the axes.

Item 1 (the Remark) is **not** repaired by anything here.  It must be deleted
and (7) carried as a hypothesis where used (Props. 4.1, 4.3, 4.6, 6.2), or
proved separately.  Under the erratum it is logically equivalent to "no
constant corner at `j=0` for `h_0 = g-b`", which this repair explicitly
permits.

### 7.5 Charge 6 — pole-path scope.  **CONFIRMED**, with the missing chain supplied.

*The location theorem.*  I re-derived (5.1): from `b = (mu-1)a+1` and
`e = (mu-1)d_F+1-u`,

```text
b - (e/d_F) a = 1 - (1-u) a / d_F,
```

and the left side is `>= 0 - (e/d_F)a > 0`.  Hence `d_F > (1-u) deg p_F`,
which by Notation 6.1 (glyph-pinned in §2) and Statement 6.1's dichotomy
(itself Prop. 6.1, p. 27) is exactly `F in T_a^nearrow`.  **Independently
corroborated by the paper's own Prop. 6.4** (p. 31): `F in T_a^searrow` iff
`deg p_(h,F) <= (d_(h,F)/d_F) deg p_F`; at a corner the right side is
negative and the left is `>= 0`.  I re-derived Prop. 6.4's `(*)`/`(**)`
equivalences and they are correct, including the tie case (16).  So the
producer's §5 is right, is not circular, and is the safer derivation because
it avoids Prop. 4.6's hypothesis (7).

*Are the consumed pole paths really `T_a^searrow`?*  Statement 9.4 (p. 49) is
**stated** on `F_1,...,F_n in V_a ∩ T_a^searrow`, Notation 9.3 defines
`lambda_F` only there, and Prop. 9.3 (p. 50) is stated on
`F,G in V_a ∩ T_a^searrow`.  So the typing claim is true by inspection of the
statements.  The producer asserts, without proof, that the *characteristic
sequence* of a pole vertex lies there.  I verified this is provable from the
source:
- `T_(a,pole) ⊆ T_a^searrow`: at `F in T_(a,pole)`, `m_F = 0` so `h_F = g`,
  and Prop. 5.3(vii) says `deg p_F/deg p_(g,F) = d_F/d_(g,F)`, i.e. equality
  in Prop. 6.4's criterion, hence `F in T_a^searrow`.  (I used (vii), not the
  (ii)/(viii) pair that `SIGRAY-AUDIT.md` files as ratio-inverted.)
- Descent: if `F in V_a ∩ T_a^searrow` and `F = G + c` with `G = F^o`, then
  `d_F > 0` and `(1-pi(F))deg p_F > d_F > 0` force `pi(F) < 1`; Statement 6.2
  gives `d_G < (1-pi(G)) mult(p_G,c) <= (1-pi(G)) deg p_G`, so
  `G in T_a^searrow`.  Monotonicity of `omega` (Statement 3.10) keeps
  `d_G >= d_F > 0`.
So the whole path from a pole vertex down to `(0,y)` is `T_a^searrow`, and by
§7.5 no corner sits on it.

*Exceptions checked.*  Endpoint `(0,y)`: doubly safe — Fact B kills the
corner there outright, whichever arrow class it lands in.  Chart exception:
`(0,x) in T_a^nearrow` (Statement 9.4's proof), which is the corner-permitted
sector — again neutralized by Fact B.  Root/equality exceptions: Prop. 6.1
(p. 27) rules out `d_F = (1-u)deg p_F`, so the dichotomy is exhaustive and
the strict inequality in (5.2) is not on a boundary.  Corollary 6.1 (p. 32)
independently forces the *equality* branch `deg p_(h,F) = (d_(h,F)/d_F)deg
p_F` on `V_a ∩ T_a^searrow \ {(0,y)}`, which a corner violates — a third,
independent confirmation of §5.

## 8. Charge 7 — what this actually repairs

**It repairs Prop. 4.2 itself, globally on `T_a^+`**: existence, the exact
uniqueness of the data, non-constancy of every member, finiteness of the
recursion, the unchanged `alpha`/`delta` formulas, and the terminal identity
(iv).  That is more than a pole-path repair, and the producer is right to say
so.

**It does not repair, and must not be read as repairing:**
- the p. 20 Remark, hence not the claim that (7) is automatic on `T_a^+`;
- the printed proofs of Prop. 4.4's "In particular" clause, Prop. 5.2,
  Prop. 5.3(ii), Props. 6.2/6.3 (all need §7.4's Facts A/B added);
- **Prop. 4.3 / `T_a^-` / condition (7)**: untouched.  Prop. 4.3 keeps `g-b`,
  `(f-a)`, and (7); (7) is exactly the hypothesis that excludes this corner
  on the negative side, and nothing here removes that gate.  I did not merge
  the two towers.
- **Prop. 5.1's finite-nonzero-puncture threshold**: untouched.  Giving
  Prop. 4.2 a finite tower says nothing about the `b=0` threshold argument.
- landing, coverage, the two-chart/all-root constructor, gluing, bounded
  delay, a cofinal degree ceiling, or JC2.  All remain open obligations.

The producer's own §6 firewalls 4, 5 and 6 state these correctly; the defect
is the *missing* seventh firewall (the `T_a^+` downstream-typing obligation)
and the word "COMPLETE" in §7.

Downstream campaign scope, read for orientation only:
`xmodel/sol-gluing-design.md:704` requires a route meeting a constant leading
part to stop as `UNRESOLVED-PROP4.2` and forbids inventing `l_j>0`.  The
producer's §6.1 normalization `(1,0,c)`-as-final-step is compatible with that
hook.  `xmodel/sol-landing1.md:210` avoids the gap by restricting to pole
segments, which §7.5 now shows is provably corner-free rather than empirical
— the producer's genuine contribution to the campaign.

## 9. Smallest exact repair

Replace the producer's §7 five-item list by the following seven items.  Items
(a)--(e) are the producer's, with (a) sharpened; (f)--(g) are new and
mandatory.

- (a) In Prop. 4.2 type `L_F := (l_0,...,l_(m-1)) in N^m` (correcting the
  printed arity slip `N*^(m-1)` at the same time), and state in (i) the
  convention `gcd(k,0) = k`.
- (b) Permit `l_j = 0` only in the unique terminal form
  `(k_(m-1),l_(m-1),s_(m-1)) = (1,0,c)` with `h_(m-1,F)^+ = c in C*`,
  `h_m = h_(m-1) - c`, `d_(h_m,F) < 0`.
- (c) Keep the printed recursion, `alpha_j` (9), (10) and the `delta_j`
  descent verbatim; add the one line that the corner forces `delta_(m) = 0`.
- (d) Record `deg p_(h_m,F) = (mu_F - 1) deg p_F + 1` and
  `M_F = gcd(M_F^*, (mu_F-1) deg p_F + 1)`; note that the corner member
  contributes `0` and that `h_m` must still be emitted.
- (e) Record the location theorem `d_F > (1-pi(F)) deg p_F`, i.e.
  `F in T_a^nearrow`, noting it also follows from the printed Prop. 6.4.
- **(f) Delete the p. 20 Remark** and carry (7) as an explicit hypothesis in
  Props. 4.1, 4.3, 4.6 and 6.2, or prove it separately.  Under (a)--(b) the
  Remark is equivalent to "no corner at `j=0`", which is not established.
- **(g) Add the two lemmas of §7.4** — Fact A (`d_(h,F^0) = d_(h,F) = 0` and
  the same constant, via Statement 3.9(i)(ii)(iii)) to restore Prop. 4.4's
  "In particular" clause and to license the cross-multiplied forms in
  Props. 6.2/6.3; Fact B (`h_((0,x))^+`, `h_((0,y))^+` are never nonzero
  constants for non-constant `h`) to restore Props. 4.5, 5.2, 5.3(ii), 6.5.

With (a)--(g), and only with (a)--(g), **`SIGRAY-AUDIT.md`'s Prop. 4.2 entry
may move from `GAP` to `ERRATUM WITH COMPLETE REPAIR`** — because that entry
names both the `l_j != 0` inference *and* the circular Remark, and (f)
disposes of the second.  Without (f) the correct new status is
`ERRATUM (partial) + residual GAP on the Remark`.  I have not edited
`SIGRAY-AUDIT.md`.

## 10. Charge 8 — checker quality

**Replay (this session, macOS, CPython 3.9.6, ~10 s):**

```text
$ python3 cases/sigray_prop42_constant_shift_repair_20260828/verify_constant_shift.py
Sigray Prop. 4.2 constant-shift checker: PASS
negative-order nonvanishing checks: 99840
zero-order classification checks:   24960
positive dependence/mutations:       12/12
(k,0) legality checks:               24
terminal delta/degree/scope checks:  938
inverse-firewall controls:           2
total exact assertions grouped:      125788
exit=0
```

Grouped total **125788** as charged.  The banner is *not* producer-authored
in the dangerous sense: every check is an `assert`, so a failure raises before
`main` prints.  Arithmetic is exact `Fraction`, standard library only.  I
reconstructed the counts independently: `polynomials(3)` yields
`2+6+18+54 = 80` polynomials, `78` of degree `>= 1`, so
`78*80*4*4 = 99840` and `78*80*4 = 24960`; `3*4 = 12` positive controls and
12 mutations; `24 + 938 + 2` for the rest; sum `125788`.  Confirmed.

**Genuine controls.**  `check_inverse_firewall_control` is a real
discriminator: `p=q=1, d=1, e=-1` gives a vanishing bracket, and mutating to
`p = 1+eta` destroys it.  `check_positive_controls` builds true dependences
`p=r^k, q=r^l, e/d=l/k` and shows a `+1` coefficient mutation breaks each of
the 12.  `check_negative_and_zero_order`'s `got_zero == (degree(q)==0)` is a
faithful two-sided encoding of Lemma 2.2(2).  My own probe (§5) confirms the
`deg(p)>=1` filter is load-bearing: 36 counterexamples appear the moment it is
dropped.

**Holes, and they are real.**
1. **Sampling, not proof.**  The alphabet is `{-1,0,1}`, degrees `<= 3`, and
   eight fixed orders.  This cannot establish Lemma 2.2 for all `p,q,d,e`.
   The docstring says so explicitly ("not a substitute for the fiber-origin
   lemma"), which is honest, but the *decisive* step of the whole repair —
   Lemma 2.1, `deg p_F >= 1` — is **not tested at all**; it is assumed as a
   filter.  The theorem rests on §4's proof, not on this file.
2. **The terminal block is tautological.**  In
   `check_constant_step_arithmetic`, `e` is *defined* as `(mu-1)d+1-u`, so
   `delta_before == -kappa*e` and `delta_after == 0` are identities of the
   producer's own definitions and can never fail.  The only non-vacuous
   assertions there are the two sign facts `d*b - e*a > 0` and
   `d > (1-u)*a`, which follow from `e<0, b>=0, a>=1, d>0` by inspection.
   938 "checks" is therefore a consistency count, not evidence.
3. **No downstream coverage whatsoever.**  Nothing in the checker touches
   Props. 4.4, 4.5, 5.2, 5.3, 6.2, 6.3, 8.1, the `M_F` recomputation, or the
   `Q(F)` slots — i.e. it is silent on the exact place where I found the
   defect.
4. **No field-theoretic coverage.**  The `e>0` uniqueness argument needs `C`
   algebraically closed (a rational function with constant `t`-th power is
   constant); the checker works over `Q` and never exercises it.  I verified
   that step by hand instead.

Net: the checker is an honest, correctly-guarded control harness for the
easy directions, and it is not the basis of any verdict here.  A theorem must
rest on proof; §§4--7 above are that proof, re-derived from the PDF.

## 11. Downstream impact table

| Source item | Printed p. | Status under the erratum | Action |
|---|---|---|---|
| Prop. 4.2 (i)--(iv), (9), (10), `delta` descent | 19--20 | **Repaired**, globally on `T_a^+` | erratum (a)--(e) |
| Remark "(7) automatic when `d_F>0`" | 20 | **Invalidated** — becomes the open statement "no corner at `j=0`" | delete; carry (7) as hypothesis — item (f) |
| Prop. 4.3, condition (7), `T_a^-` tower | 20--21 | Untouched; (7) still needed | none; firewall holds |
| Notation 4.1 (`⪯`) | 21 | Well-posed via repaired uniqueness | none |
| Prop. 4.4, statement | 21 | True as printed (`l in N*` hypothesis) | none |
| Prop. 4.4, "In particular" clause | 21 | **Proof breaks** (`0/0`) | Fact A — item (g) |
| Prop. 4.5, (0,x)/(0,y) join | 22 | Safe once corner excluded at axes | Fact B — item (g) |
| Prop. 4.6, (11)--(17) | 23 | Needs (7); producer avoids it by deriving (4.2) from (3.4) | none for the repair |
| Prop. 5.1 threshold at finite punctures | 23--24 | **Not repaired** | out of scope |
| Prop. 5.2 | 24 | **Proof breaks** at uniform `l=0` | Fact B — item (g) |
| Prop. 5.3(ii)/(viii) | 25 | **Proof breaks** (`k/l` undefined) | Fact B — item (g) |
| Prop. 5.3(vii), `T_(a,pole) ⊆ T_a^searrow` | 25 | Confirmed, used in §7.5 | none |
| Notation 6.1, Statement 6.1, Prop. 6.1 | 27, 29 | Dichotomy exhaustive; hosts (5.2) | none |
| Statement 6.2 | 29 | Used for `T_a^searrow` descent | none |
| Props. 6.2, 6.3 (displayed ratios) | 29--30 | **Proof breaks** (`/d_(h_j,F)`) | cross-multiply — item (g) |
| Prop. 6.4, Corollary 6.1 | 31--32 | Corroborate (5.2) | none |
| Notation 8.1 (`M_F`, `M_F^*`) | 39 | Definitional; needs `gcd(n,0)=n` and emission of `h_m` | item (d) |
| Statement 8.1, Prop. 8.1 | 39--40 | Safe: `T_a^searrow` domain, corner-free | none |
| Notation 9.1 `Q(F)` | 48 | Four slots untouched; `M_F` per (4.4) | item (d) |
| Statements 9.4--9.5, Prop. 9.2--9.3 | 49--50 | Safe: stated on `V_a ∩ T_a^searrow`, and §7.5 shows the pole characteristic path lies there | none |
| `sol-gluing-design.md` (T2), `UNRESOLVED-PROP4.2` hook | n/a | Compatible; `(1,0,c)`-final-step normalization | campaign follow-up |
| `sol-landing1.md` pole-segment restriction | n/a | Upgraded from empirical guard to theorem | campaign follow-up |
| Landing, coverage, bounded delay, degree ceiling, JC2 | n/a | **Not repaired** | out of scope |

## 12. Charge-by-charge summary

| # | Charge | Verdict |
|---|---|---|
| 1 | Fiber residual `p_F` nonconstant, both charts, `f` vs `f-a`, axes, truncations | **CONFIRMED** |
| 2 | `e<0` impossible; transformed Jacobian, denominator clearing, `(q^A p^B)'`; countermodel hunt | **CONFIRMED** |
| 3 | `e=0 => q in C*`; `(1,0,c)` unique; `f^0` legal; `h-c` non-constant | **CONFIRMED** |
| 4 | Immediate termination; exact terminal equation; `delta_next = 0`; indices | **CONFIRMED** |
| 5 | `deg p_(h_m,F)=(mu-1)deg p_F+1`, `M_F`, `Q(F)` slots | **CONFIRMED** |
| 5' | Downstream `l=0` divisions (4.4 clause, 5.2, 5.3(ii), 6.2, 6.3, Remark) | **REPAIR REQUIRED** — five sites, none addressed |
| 6 | Constant corner forces `T_a^nearrow`; pole paths are `T_a^searrow` | **CONFIRMED**, supporting chain supplied |
| 7 | Firewalls: 4.3/(7), 5.1, landing, coverage, delay, ceiling, JC2 | **CONFIRMED**; one firewall missing (`T_a^+` typing) |
| 8 | Checker quality | **Honest but weak**: real mutation controls, tautological terminal block, sampling only, zero downstream coverage |

**Terminal verdict: REPAIR.**
