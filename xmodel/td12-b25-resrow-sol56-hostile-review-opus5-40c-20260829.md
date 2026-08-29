# Opus 5 hostile different-model review — TD12-B25-RESROW/v1 (Sol 5.6 provisional correction)

Lane: Opus 5, equal-standing adversarial reviewer. Date: 2026-08-29.
Frozen campaign basis, verified at session start and again before sealing:

```text
40c1ab3448209e3d87173feb947a733f6fe54f7f
```

The reviewed Sol correction and the three bridge documents were sealed on the
parent basis `92ebe92ad5986a47f01af9ed901260595dfed869`; `40c1ab34` is its
child ("Promote reviewed carrier, TD12 bridge, and K00 strata") and is the
commit that recorded the Sol correction as *provisional pending independent
review*. This report is that review.

The correction was not taken as a premise. Starting from `J(f^F,Dev)=x^(-u)`
I collected every coefficient independently and re-derived the operator, the
signs, and the outer powers before comparing with any of the three prior
documents.

## 0. Binary disposition

```text
VERDICT: PASS_WITH_REPAIR

SOL_CORE_CONFIRMED_INDEPENDENTLY
  FABLE_C4_III_INTEGRATING_FACTOR_REFUTED   exponent is p^(I-i)=p^m, not p^(I-1)
  FIRST_RESONANCE_IS_A_TOTAL_DERIVATIVE     R_17 = -(d/deta) S_17, identically
  BOTH_ORBIT_RESIDUES_IDENTICALLY_ZERO      unconditionally, at every point of P^1
  RESROW_VACUOUS_ON_CLASS                   confirmed, and on a strictly larger domain
  FABLE_C1_TOP_SCALE_REPAIR_CONFIRMED       alpha = c_g lambda_f^(-3/2)
  NO_ROUTE_KILL                             confirmed
  NO_RESROW_DESCENDANT_LICENSED_AT_j=17     confirmed; stop upgraded from provisional

REPAIRS_REQUIRED_TO_SOL_SECTION_6_FRONTIER_GUIDANCE
  R-A  j=42 consumption list is incomplete: it omits the free resonant gauge C_17
  R-B  "outside B24" rests on an untyped P_a <-> window-depth identification

TYPED_OPEN
  OPEN(J42-NONVACUITY)             not decidable without P-values
  OPEN(NONRESONANT-EXISTENCE-B25)  rational-existence at non-resonant rows untyped
  OPEN(WINDOW-INDEX-B25)           P_a index vs B-gate depth index not typed anywhere
```

Sol's six disposition strings are all correct. The load-bearing sections
(§§0-5) verify in full and I obtained three strengthenings Sol did not claim
(§§5.3, 6.2, 7.3 below). The repairs are confined to §6's explicitly fenced
frontier guidance and to the canonical notes that consumed it.

`charge_basis` is absent: no exit price is asserted anywhere in this report.

## 1. Custody

Recomputed with `shasum -a 256` before reading and again before sealing; body
seals recomputed with the campaign convention (all bytes before the literal
`## Seal` heading). All eight values matched their declared or manifest
values both times.

```text
edfec0a0d9abb8b24db9406bdc1147348114f198a4a9e92a10486bbe9131a720
  xmodel/td12-b25-resrow-v1-provisional-sol56-20260829.md
  body 11988 bytes  9c72c20e02efcb74fd351f7ac820268386a625dbfc60b855dc18a1e212766b4f
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b
  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md
  body 39510 bytes  539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
20684d3e5ea0f070817c08c72d0dd1b45e691787429bd8eb57eaf68296431bf8
  xmodel/td12-global-source-bridge-b-fable5-hostile-review-grok46-92e-20260829.md
  body 41244 bytes  dab4058f598c05dbd5d00448c7e36c56dbbbfa7869ec3df3189f4640876a85b4
c6c1d5fe6df7796cac468fb81db16b3bbce777c305d869b9ad46cbb88a16f339
  xmodel/td12-global-source-bridge-b-coordinator-integration-sol56-20260829.md
  body  6243 bytes  89fc2555eeeb4424a45cde47a16b910b3a34b9ac42a3b91717d89e5442b759d5
```

Read for propagation check only, not charged as mathematical input:
`APPROACHES.md:95-105`, `AUDIT.md:325-340`, `COORDINATION.md:755-770`,
`PROGRESS.md:95-105`, `notes.md:13338-13350`. All five record the Sol
correction correctly as provisional and pending this review; none promotes
it. No canonical file was edited.

**Custody finding (favourable to Sol).** Sol's §1 charge list is Fable
`0175063f`, bchild primary `1a602643`, bchild disposition `876d1717`,
formal-cascade coordinator `97ba497f`, inhomogeneous-row `1272b394`. The
Grok review is **not** on it, and no string matching `grok` or `20684d3e`
occurs in Sol's file. Sol therefore did not read Grok before finding the
`p^(I-1)` error. Grok's §7 and Sol's §3 are two independent rediscoveries of
the same slip. That is genuine corroboration, not an echo — and it is the
correct way to read the agreement.

**Divergence finding.** Grok stopped at the repair and expected the corrected
residues to be live: Grok §7 writes "Two deck-orbit conditions survive after
the repair", and Grok's countermodel list posits "simple pole of `RHS_17` at
an A-root ... correct residues of `RHS_17` need not [vanish]". Sol's §4 goes
one step further and shows they *do* vanish. My §5.3 below shows Grok's
posited countermodel is structurally impossible: the corrected `R_17` can
never have a simple pole anywhere. Sol supersedes Grok here, correctly.

## 2. Notation firewall

Held distinct throughout, and checked for conflation at every use:

```text
nu     = 25   deck order / top-pattern lattice modulus / rationality modulus for p^c
kbar   = 17   local state numerator; also the landing offset ord_top(Dev) = kbar - D_F
kappa_F       chart denominator in the Jacobian coefficient equation; unpinned, kappa_F > 17
D = D_F = nu*i = 25 i        f-side top order
D_g = 25 r,  r = 3i/2,  i even and positive
X = 25        state datum kbar*dp/dq; NOT re-used as an index
I = i + m     conjugation exponent at the resonance j = kbar + nu*m
i             the P_0 exponent, P_0 = lambda_f p^i;  m             the resonance ordinal
j             relative row index below the landing;  a, b          graded drop indices
' = d/d eta   throughout (both Sol and Fable declare this explicitly; t-level
              derivatives are written with subscripts, so no prime-label ambiguity)
```

`p = (t-A)^2(t-B)`, `q = eta(t-A)(t-B)`, `t = eta^25`, `A,B` nonzero and
distinct, `B/A = 9/8` (promoted T1). `p(0) = A^2(-B) != 0`, so `eta = 0` is
not a pole; the finite poles of `C[eta][1/p]` are exactly the 50 roots of
`p`, 25 double (A-orbit) and 25 simple (B-orbit).

Two identifications that the algebra below **uses** and that are consumed,
not re-derived: `D_F = nu_F * i` (trunk state plus Prop 8.1(i)) and the
promoted `(E_s)` normalization with right side `kappa_F * 1_(s=s*)`. Sol's §1
firewall is adequate; I found no `D/nu/kbar/kappa` conflation in Sol. See
§6.3 for the one place where the coincidence `D_F/i = nu_F` is load-bearing
and §5.4 for the fact that the vacuity result does not use it at all.

## 3. Independent coefficient collection

With `J(u,v) = u_x v_eta - u_eta v_x`,

```text
f^F = sum_(a>=0) P_a(eta) x^((D-a)/kappa_F),
Dev = sum_(b>=0) T_b(eta) x^((O-b)/kappa_F),        O := ord_top(Dev).
```

The `(a,b)` term of `J(f^F,Dev)` is

```text
(1/kappa_F) [ (D-a) P_a T_b' - (O-b) P_a' T_b ] * x^((D+O-a-b)/kappa_F - 1),
```

so with `j = a+b` and, granting C2's landing `O = kbar - D`, the graded rows
in the promoted `(E_s)` normalization are

```text
sum_(a=0)^j [ (D-a) P_a T_(j-a)' - (kbar-D-j+a) P_a' T_(j-a) ]
    = kappa_F * 1_(j=0).                                        (ROW_j)
```

This is Sol (3.1) and Fable C4's displayed row, coefficient for coefficient
and sign for sign. Grok confirmed the same row (C4.L). Three independent
derivations agree; I add a fourth.

**Sign-convention robustness.** If the campaign's `J` carries the opposite
sign, every row and every `R_j` below flips sign uniformly; if `(E_s)` is
rescaled, only the `j=0` right side changes. Neither touches any conclusion
of §§4-6, because **row `j = 17` is homogeneous**: the single monomial
`x^(-u)` lands in exactly one row, and C2 places it at `j = 0`.

The `a=0` term, using `P_0 = lambda_f p^i`, `P_0' = i lambda_f p^(i-1) p'`:

```text
D P_0 T_j' - (kbar-D-j) P_0' T_j
  = 25 i lambda_f p^i T_j' + (25i+j-17) i lambda_f p^(i-1) p' T_j
  = i lambda_f p^(i-1) * L_j[T_j],
L_j[T] := 25 p T' + (25i+j-17) p' T.                            (FRESH)
```

Setting `R_j := -sum_(a=1)^j (...)`, `(ROW_j)` for `j>=1` is exactly

```text
i lambda_f p^(i-1) L_j[T_j] = R_j.                              (3.3)
```

Note the outer factor `p^(i-1)`. It is present in Fable's own prose ("after
clearing `i lambda_f p^(i-1)`") and is the factor Fable then drops.

## 4. The integrating factor: `p^(I-i)`, not `p^(I-1)`

Resonance: `25i+j-17 = 25I` for an integer `I` iff `25 | (j-17)` iff
`j = 17 + 25m`, and then `I = i+m`. The Leibniz conjugation

```text
L_j[T] = 25 p^(1-I) (p^I T)'
```

is correct as Fable C4(i) states it. Substituting it into **the whole** of
(3.3), outer factor included:

```text
i lambda_f p^(i-1) * 25 p^(1-I) (p^I T_j)' = R_j
  =>  25 i lambda_f p^(i-I) (p^I T_j)' = R_j
  =>  (p^I T_j)' = p^(I-i) R_j / (25 i lambda_f) = p^m R_j / (25 i lambda_f).
```

Fable C4(iii) and §5 assert `p^(I-1)`. **Refuted.** The discrepancy is the
factor `p^(i-1)` of (3.3), which Fable clears from the left and forgets on
the right. Equivalently: `p^(I-1)` is what one gets from the mis-stated row
`i lambda_f L_j[T_j] = R_j`.

**First exceptional value of `i`.** `p^(I-1) = p^(I-i)` for all `m` iff
`i = 1`, and `i = 1` is the *only* exceptional value. It is excluded twice
over on this route: `r = 3i/2 in Z` forces `i` even, and the reviewed
depth-24 window transparency needs `i >= 16` (`r >= 24`). So on the class the
spurious factor has `t`-degree `3(i-1) >= 45`. Sol's exceptional-value
statement is correct and tight; I confirm there is no second exceptional
value and no gauge reading under which the two forms agree.

At `j = 17` (`m = 0`, `I = i`) the correct equation is

```text
25 i lambda_f (p^i T_17)' = R_17,       i.e.  (p^i T_17)' = R_17/(25 i lambda_f),
```

against Fable's `(p^i T_17)' = p^(i-1) RHS_17/(25 i lambda_f)`. Grok reached
the same corrected first-row form independently.

## 5. The first resonance is a total derivative

### 5.1 The collapse, and why it is structural

In `(ROW_j)` the coefficient of `P_a T_(j-a)'` is `(D-a)` and the coefficient
of `P_a' T_(j-a)` is `-(kbar-D-j+a) = D+j-kbar-a`. These are equal iff

```text
D - a = D + j - kbar - a   <=>   j = kbar.
```

So for every `a`, at `j = kbar` and **only** at `j = kbar`, the summand is a
product-rule derivative:

```text
(D-a) P_a T_(kbar-a)' + (D-a) P_a' T_(kbar-a) = (D-a) (P_a T_(kbar-a))'.
```

Hence, with `S_j := sum_(a=1)^j (D-a) P_a T_(j-a)`,

```text
R_17 = - (d/d eta) sum_(a=1)^17 (25i - a) P_a T_(17-a) = -S_17'.   (CONFIRMED)
```

The displayed identity in the task statement **holds identically.** I verify
the specialization `kbar - D - 17 + a = a - D` directly: `17 - 25i - 17 + a =
a - 25i`. Sol (4.1)-(4.3) confirmed.

This is not a numerical accident of `(17,25)`. Because `gcd(kbar,nu)=1` and
`0 < kbar < nu`, the smallest positive solution of the resonance congruence
`j ≡ kbar (mod nu)` is `j = kbar` itself — which is exactly the collapse
index. **On any such state the first resonance is the total-derivative row.**
Sol did not state this; it is the sharp form of the finding and it explains
why the failure is not repairable by re-choosing constants.

### 5.2 Both residues vanish — on a strictly larger domain than Sol claims

For any `h` in `C(eta)` and any `zeta`, writing `h = sum_n a_n (eta-zeta)^n`,
`h' = sum_n n a_n (eta-zeta)^(n-1)` has `(eta-zeta)^(-1)`-coefficient
`0*a_0 = 0`. Therefore

```text
Res_zeta( R_17 d eta ) = -Res_zeta( dS_17 ) = 0    for every zeta in P^1(C),
```

including the 25 A-orbit points, the 25 B-orbit points, infinity, and any
hypothetical pole outside the roots of `p`. Sol (5.1)-(5.2) confirmed.

**Strengthening.** The identity `R_17 = -S_17'` is a *formal* consequence of
the product rule. It holds for arbitrary rational `P_1..P_17` and
`T_0..T_16`, with no assumption that they solve the preceding rows, satisfy
any child condition, lie in `C[eta][1/p]`, are on-weight, or come from an
actual pair. Sol's §5 states the conclusion "wherever the preceding rational
tail is defined"; the true domain is the entire space of rational tuples.
Since that is a superset, Sol's conclusion is safe, but the caveat is
unnecessary for the residue claim and should not be carried forward as if it
were a live restriction. The caveat *is* needed for the separate solvability
claim (§5.5).

The two proposed deck-orbit functionals of Fable C4(iii)/§5 are therefore the
**zero functional**, not two constraints and not an inconsistency. Fable's
verdict that `s*+17` is "the first genuinely unspent consequence" is
invalidated; the row spends nothing.

### 5.3 Grok's countermodel is structurally impossible

Grok's countermodel list posits `RHS_17` with a simple pole at an A-root.
From `R_17 = -S_17'`, the Laurent expansion of `S_17'` at any point has
coefficients `n a_n` at `(eta-zeta)^(n-1)`, so the `(eta-zeta)^(-1)` slot is
identically empty: **`R_17` has no simple-pole part at any point whatsoever.**
It can have poles of order `>= 2` only. Grok's countermodel reasoned about a
generic function in the right weight class rather than about the actual
`R_17`, and is void. This does not affect Grok's `PASS_WITH_REPAIR`, whose
repair item 6 is correct.

### 5.4 What the vacuity does and does not depend on

The collapse of §5.1 uses only `j = kbar` and the product rule. It uses
**none** of: `nu = 25`, `D_F = nu i`, the rationality modulus, the Theorem D
weight law, the deck action, the fifty-to-two orbit collapse, membership in
`C[eta][1/p]`, the pattern shapes of `p` and `q`, the T1 ratio `B/A = 9/8`,
`kappa_F`, `lambda_f`, `gamma`, `c_g`, or any ledger constant. It does depend
on Theorem C2's landing `ord_top(Dev) = kbar - D_F`: in general the collapse
index is `j = D_F + ord_top(Dev)`, and C2 is exactly what makes it `kbar`.
Sol grants C2/C3 conditionally and that conditionality is correctly placed
and genuinely required.

The identification of `j = kbar` as a *resonance* — as opposed to a
total-derivative row — does use `D_F/i = nu_F` and `nu_F | D_F`. So if that
consumed route datum were wrong, what would break is the claim that `j = 17`
is where a residue condition was ever expected, not the vacuity.

### 5.5 Explicit solution, gauge, and on-weight admissibility

From `25 i lambda_f (p^i T_17)' = -S_17'`,

```text
p^i T_17 = -S_17/(25 i lambda_f) + C_17,
T_17     = -S_17/(25 i lambda_f p^i) + C_17 p^(-i),     C_17 in C.
```

The homogeneous freedom is exactly `ker L_17 = C p^(-I) = C p^(-i)`,
one-dimensional, matching Fable C4(i) and C4(iii)'s "one new gauge constant
per resonant row". Sol (4.4)-(4.5) confirmed.

Ring membership: `P_a` are polynomials and `T_0 = gamma q p^(-i)`, so if
`T_1..T_16` lie in `C[eta][1/p]` then `S_17` does, hence `p^i T_17` does,
hence `T_17` does. Row 17 is unconditionally solvable in the on-weight ring
given a prior tail in that ring. **No obstruction of any kind.**

**Weight check Sol omits, and which passes.** Under Theorem D
(`e_k ≡ 22k mod 25`), `P_a` has weight `≡ 22a`, and `T_b` at drop `s*+b` has
weight `≡ 22(s*+b) ≡ 1 + 22b` (using `s* ≡ 8`, `22*8 ≡ 1`). Then every
product `P_a T_(17-a)` has weight `≡ 22a + 1 + 22(17-a) = 1 + 22*17 ≡ 0`
(mod 25) — I checked all `a = 0..17` and the set of values is `{0}`. So
`S_17` is on-weight `0`, `R_17 = -S_17'` is on-weight `-1` (matching Fable's
and Grok's `≡ 22j ≡ -1` bookkeeping), `p` is on-weight `0`, and the required
weight of `T_17` is `1 + 22*17 ≡ 0`. Both `S_17/p^i` and `C_17 p^(-i)` sit at
weight `0`. **The explicit solution and the full one-dimensional gauge are
on-lattice.** The vacuity therefore survives the on-weight constraint, not
merely the `C(eta)` constraint. Sol did not check this; it closes the last
place a hidden condition could have hidden.

## 6. General resonances, and `j = 42`

### 6.1 The general row

At `j = 17 + 25m`, `kbar - D - j + a = a - D - 25m`, so

```text
R_j = -S_j' - 25 m U_j,
S_j := sum_(a=1)^j (D-a) P_a T_(j-a),    U_j := sum_(a=1)^j P_a' T_(j-a).
```

Sol (6.1) confirmed. The total-derivative collapse is exactly the `m = 0`
case, as Sol says.

### 6.2 Closed form for every resonance obstruction (new)

Using `p^m S_j' = (p^m S_j)' - m p^(m-1) p' S_j` and `Res(d(anything)) = 0`,
the corrected primitive equation `(p^I T_j)' = p^m R_j/(25 i lambda_f)` gives,
for every `m >= 0` and every point `zeta`,

```text
Res_zeta( p^m R_j d eta )
   = m * [ Res_zeta( p^(m-1) p' S_j d eta ) - 25 Res_zeta( p^m U_j d eta ) ].
```

The overall factor `m` exhibits §5.2 as the `m = 0` specialization and gives
every higher resonance obstruction in closed form. This was verified exactly
at `m = 0,1,2` (control C6, §9). It also shows there is no analogue of the
`m = 0` collapse at any `m >= 1`: with generic rational inputs both residues
are nonzero (control C6 returns nonzero values at `m = 1,2`).

### 6.3 Is `j = 42` the first possibly nonvacuous row?

Resonances are `j ≡ 17 (mod 25)`, `j >= 1`: `17, 42, 67, 92, ...`. Given
§5.2, `j = 42` is the first resonance whose two orbit residues are not
identically zero as functionals. **Within the resonance/residue lane, yes.**

But the unqualified phrase "first possibly nonvacuous row" is not
established, and must not be promoted:

- **OPEN(NONRESONANT-EXISTENCE-B25).** Grok's C4(ii) note is right and
  unresolved: at a non-resonant `j`, uniqueness in `C(eta)` follows from the
  irrational kernel, but *existence in `C[eta][1/p]` is an extra condition*
  for a formal `(V)/(W)` jet, free only for an actual pair. Neither Fable,
  Grok, nor Sol types that condition anywhere. So non-resonant rows
  `1..16` and `18..41` are not known to be vacuous on a formal class; they
  are merely un-analyzed. The safe statement is "first possibly nonvacuous
  **resonant** row". The coordinator integration §2 already uses the word
  "resonance" and is correctly scoped; `APPROACHES.md`, `PROGRESS.md`,
  `COORDINATION.md`, and `notes.md` say "next possible resonance" or "next
  algebraically possible resonance" and are also correctly scoped. No
  canonical repair is needed on this point; it is recorded so the qualifier
  is not dropped later.

### 6.4 What `j = 42` would need, and whether anything licenses it

Consumption at `j = 42` (`m = 1`, `I = i+1`):

```text
P_1, ..., P_42;   T_0, ..., T_41;   kappa_F, lambda_f, i, A, B  (through T_0 = gamma q p^(-i));
and -- omitted by Sol -- the free resonant gauge C_17.
```

**R-A, the omitted gauge (new blocker).** `T_17` is determined only up to
`C_17 p^(-i)`. Rows `18..41` are linear in the prior `T`'s with a linear
solution operator, so `T_18, ..., T_41` are *affine in `C_17`*, hence so are
`S_42`, `U_42`, hence so are both `j = 42` residues. The `j = 42` conditions
are therefore **not functionals of window data alone**: they are two affine
conditions in one unpinned constant. Nothing on the frozen basis pins
`C_17` — it is a Theorem-A functional of the actual pair with no serialized
instance, exactly like `lambda_f` and `kappa_F`. Generic elimination of
`C_17` would leave at most one net condition, not two. Sol's §6 says `j = 42`
"would consume data through `P_42`" and stops; the list is incomplete in a
way that understates the blocker. Repair required.

**R-B, the "outside B24" wording.** `P_a` is indexed by drop from the top of
`f^F`; the depth-24 B gate / window is indexed by `s`, the ledger drop from
the top of `g^F` (the coordinator's "binomial response licensed through
`s <= r`", `r >= 24` iff `i >= 16`). Fable §5 silently identifies the two
("the window pieces `P_1..P_17` ... of the depth-24 B gate"); Grok did not
challenge it; Sol inherits it in "`P_42`, not the B24 window". No document in
the charged set types that identification. Logged as
**OPEN(WINDOW-INDEX-B25)** under the FALLACY-v2 variable/ring-map and
target/arrival-index clauses. Repair the wording to the index-free form:
"consumes `P_42`, which is two indices deeper than any window depth reached
by any promoted result, and whose value no packet supplies."

**Licensing decision: NO packet licenses `j = 42`.** This is robust to both
R-A and R-B, on four independent grounds:

1. No packet supplies any value of `P_k` for `k >= 1`. Fable §9 nonclaims it
   explicitly; the coordinator §3 firewall repeats it; the promoted bchild
   underdetermination is the positive statement that the window pieces carry
   genuine freedom.
2. `C_17` is unpinned (R-A), so even complete window values would not
   determine the two residues.
3. `CAP-B25` and `OCCURRENCE-B25` are unchanged by anything in this review.
4. The expansion cost is not desk-sized: producing `T_1..T_41` means solving
   41 first-order ODEs over `C(eta)` with `lambda_f, kappa_F, i, A, B` and 42
   unpinned `P_a` all symbolic. Fable's own §10 sized the descendant for
   `j = 17`; `j = 42` is a different object.

## 7. Audit of the rest of Sol's report

### 7.1 The C1 leading-scale repair — confirmed, and already bound

With Fable's own convention `(f^F)^rho := lambda_f^rho x^(rho d_F) p^(i rho)
(1+V)^rho`, the leading piece of `(f^F)^(3/2)` is `lambda_f^(3/2) p^r`, and
`G_0 = c_g p^r`. So `g^F - c_g (f^F)^(3/2)` cancels at top iff
`lambda_f^(3/2) = 1`. The correct constant is `alpha = c_g lambda_f^(-3/2)`.
Sol (2.1) confirmed.

Scope: this is a display slip inside C1's setup, not a theorem-level failure
— C1 quantifies the `C_k` existentially, so only the *possibility* of top
cancellation is used. It is also **not new**: the coordinator integration §2
already binds it in the equivalent tower form `s_0 = c_g^2/lambda_f^3`
(and indeed `alpha^2 = c_g^2 lambda_f^(-3) = s_0`, consistent). Sol did not
charge Grok or re-check the integration for this, so §2 is an honest
independent re-derivation of an already-bound repair, not a new finding.

### 7.2 Sol (2.2): the ledger constants really do drop out — confirmed

`J(f^F,(f^F)^rho) = rho (f^F)^(rho-1) J(f^F,f^F) = 0` (Fable §4.1, valid for
formal powers with `i rho in Z`, which holds since `i` is even). `H` is a
finite sum (C1 item 3 bounds `m <= 5i/2 - 1`), so `J(f^F,H(f^F)) = 0` and
`J(f^F,Dev) = J(f^F,g^F) = x^(-u)` exactly. Hence `c_g`, `C_ell`, `rho_ell`
carry **no explicit dependence** into the tail recurrence. This independently
settles the Fable/Grok disagreement on C4's consumption list in Grok's favour
(Grok C4.cons): in `Dev^red` language the consumed constants are
`kappa_F, lambda_f, i, A, B, p, q`, and `c_g`/`C_k` appear only on conversion
back to original `G`-pieces. Triply confirmed now.

### 7.3 Sol (2.3): the landing scale — independently reconfirmed

Substituting `T = gamma q p^(-i)` into `25 p T' + (25i-17) p' T`:

```text
25 p T' = 25 gamma p^(-i) (p q' - i q p'),
(25i-17) p' T = (25i-17) gamma q p' p^(-i),
sum = gamma p^(-i) [25 p q' - 17 p' q] = 25 A B gamma p^(1-i),
```

using the promoted cell identity `25 p q' - 17 p' q = 25 A B p`. Setting this
equal to `(kappa_F/(i lambda_f)) p^(1-i)` gives
`gamma = kappa_F/(25 i lambda_f A B)`. Fable C3's `gamma`, the coordinator's
`gamma`, and Sol (2.3) all confirmed by a fourth independent substitution.

### 7.4 Sol's controls (§7) — all four re-run and correct

The top-scale control, the integrating-factor control, the `i=2, m=0`
mutation, the `j = kbar` coefficient control, and the general-resonance
mutation are each one-line identities in a differential field, and each is
correct as displayed. Sol's claim "no checker was needed" is defensible; I
nevertheless ran an independent exact checker (§9) and it agrees.

### 7.5 What Sol got right that is easy to get wrong

- Did not invent any `P_k`, child value, occurrence witness, or transport map.
- Did not assert a route kill from a vacuous row.
- Fenced §6 as frontier guidance and refused a `j = 42` nonvacuity claim —
  the correct side of the FALLACY-v2 floor/attainment clause.
- Kept `nu`, `kbar`, `kappa_F` explicitly unidentified (§4 last bullet).
- Emitted `charge_basis` nowhere; no exit price is asserted (verified: zero
  occurrences of the string in the file).
- Reported the C1 slip as repairable and *not* the cause, rather than
  inflating it.

## 8. Attacks run and their outcomes

```text
leading-scale normalization      C1 literal display FALSE unless lambda_f=1;
                                 alpha = c_g lambda_f^(-3/2). Non-propagating (§7.1).
D/nu/kbar/kappa conflation       none found in Sol. The one real coincidence,
                                 D_F/i = nu_F, is consumed route data and is NOT
                                 used by the vacuity argument (§5.4).
coefficient signs                4 independent derivations agree (Fable, Grok, Sol,
                                 mine). Conclusion is sign- and normalization-robust
                                 because row 17 is homogeneous (§3).
outer powers                     THE error. p^(i-1) dropped from the right side.
                                 p^(I-i), not p^(I-1) (§4).
first exceptional value of i     i = 1, uniquely; excluded by i even and by i >= 16
                                 (§4). No second exceptional value exists.
omitted poles                    none. p(0) != 0; residue argument covers every point
                                 of P^1 including infinity and any pole outside
                                 roots(p), so the C[eta][1/p] membership question
                                 cannot leak into the residue claim (§5.2).
dependence on prior tail         residue vanishing: independent of it entirely.
                                 row solvability: genuinely needs T_0..T_16 in
                                 C[eta][1/p]. Sol bundles the two; separated in §5.5.
                                 Direction of Sol's caveat is conservative.
source-honest child conditions   cannot rescue the row: the identity holds before any
                                 specialization, so intersecting with any subvariety of
                                 admissible (P_a) leaves the zero functional (§5.2).
                                 No child value was read or used by me.
on-weight / on-lattice leak      checked and closed: solution and gauge both sit at
                                 weight 0 mod 25 (§5.5). Sol omitted this.
Grok's surviving countermodel    void: R_17 has no simple-pole part anywhere (§5.3).
j=42 consumption list            incomplete in Sol: omits C_17 (§6.4, R-A).
"outside B24"                    untyped index identification, inherited from Fable §5
                                 (§6.4, R-B; OPEN(WINDOW-INDEX-B25)).
non-resonant rows                un-analyzed lane; "first possibly nonvacuous row" must
                                 read "resonant row" (§6.3).
```

## 9. Controls

Exact, stdlib-only, `Fraction` arithmetic, no CAS, scratch
`/tmp/b25resrow/resrow.py`
(sha256 `229160243f0edc0710d66f22c43614fe69d22793068e96c4bcb381c9b4697753`).
Normal form `N(eta)/p^e`; residues by exact power-series inversion at a root.
The desk proofs of §§3-6 are universal in `(nu, kbar, i)` with `0 < kbar < nu`
and `D = nu i`; the checker instantiates the structural toy
`nu = 5, kbar = 3, i = 2, D = 10, p = (eta-1)^2(eta-2)`, which exercises both
a double-root (A-orbit) and a simple-root (B-orbit) pole type with rational
roots. It does **not** model the deck action or the weight lattice, which
§5.4 shows the result does not use.

```text
C1  a=0 term == i*lambda_f*p^(i-1)*L_j[T_j]            True at j=1,2,3,4,8,13
C2  L_j == nu p^(1-I) (p^I .)' at j = kbar+nu*m        True at m=0,1,2
C3  (p^I T_j)' == p^(I-i) R_j/(nu i lam)               True  at m=0,1,2
    (p^I T_j)' == p^(I-1) R_j/(nu i lam)               False at m=0,1,2   <- Fable
C4  R_kbar == -S_kbar'                                  True
    Res R_kbar at both root types                       0 and 0
C5  mutation j -> 2, 4, kbar+nu breaks the collapse     False, False, False (detected)
C6  Res[p^m R_j] == m*(Res[p^(m-1)p'S_j] - nu Res[p^m U_j])
                                                        match at m=0,1,2, both roots;
                                                        values 0,0 at m=0 and nonzero
                                                        (-4458, 7132, 3288, 704) at m=1,2
C7  Fable's p^(I-1) form at j=kbar                      SPURIOUS residues 4035, 1207
ALL_CONTROLS_CONSISTENT
```

C7 is the decisive control: the dropped `p^(i-1)` is *exactly* what
manufactures nonzero residues out of an exact derivative. C5 confirms the
collapse is pinned to `j = kbar` and is not an artefact of the toy. C6
confirms both the new closed form and that `m >= 1` is generically live.

Disclosure: my first run of C2/C3 reported `False` because of a sign slip in
my own helper (`p^(-I)` where `p^(I)` was meant); the helper was fixed and
re-run. C1, C4, C5, C6, C7 were unaffected and passed on both runs. The
producer's error is in the producer's document, not in a checker artefact:
C3's `False` for the `p^(I-1)` form persists after the fix, and the desk
derivation of §4 is independent of any checker.

## 10. Maximum safe theorem

Let `0 < kbar < nu` with `gcd(kbar,nu) = 1`, `D = nu i`, `i >= 1`,
`P_0 = lambda_f p^i` with `lambda_f` a nonzero constant, and let the graded
rows `(ROW_j)` of §3 hold with `ord_top(Dev) = kbar - D` (Theorem C2, granted
conditionally). Write `R_j := -sum_(a=1)^j (...)`,
`S_j := sum_(a=1)^j (D-a) P_a T_(j-a)`, `U_j := sum_(a=1)^j P_a' T_(j-a)`.
Then, for arbitrary `P_a, T_b in C(eta)`:

```text
MST-1  Row j>=1 is  i lambda_f p^(i-1) L_j[T_j] = R_j,
       L_j[T] = nu p T' + (D+j-kbar) p' T.
MST-2  ker L_j != 0 in C(eta)  iff  j = kbar + nu m;  then I := i+m and
       L_j = nu p^(1-I) o (d/d eta) o p^I,  ker L_j = C p^(-I).
MST-3  At j = kbar + nu m the row is exactly
           (p^I T_j)' = p^(I-i) R_j/(nu i lambda_f) = p^m R_j/(nu i lambda_f).
       The exponent is I-i, not I-1; the two coincide for all m iff i = 1.
MST-4  The two row coefficients coincide iff j = kbar. Since 0 < kbar < nu,
       j = kbar is simultaneously the FIRST resonance and the UNIQUE
       total-derivative row, and there R_kbar = -S_kbar' identically.
       For the B state: R_17 = -(d/d eta) sum_(a=1..17) (25i-a) P_a T_(17-a).
MST-5  Hence Res_zeta(R_kbar d eta) = 0 at EVERY zeta in P^1(C), with no
       hypothesis on the P_a, T_b beyond rationality. R_kbar has no
       simple-pole part anywhere. Both proposed deck-orbit residue
       functionals at j = 17 are the zero functional.
MST-6  If additionally T_0..T_(kbar-1) lie in C[eta][1/p], row kbar is
       solvable there, with
           T_kbar = -S_kbar/(nu i lambda_f p^i) + C_kbar p^(-i),  C_kbar in C,
       a one-dimensional resonant gauge. On the B state both terms are
       on-weight (class 0 mod 25), so solvability holds in the on-weight ring.
MST-7  For every m >= 0 and every zeta,
           Res_zeta(p^m R_j d eta)
             = m * [ Res_zeta(p^(m-1) p' S_j d eta) - nu Res_zeta(p^m U_j d eta) ].
       MST-5 is the m = 0 case; no analogue holds for m >= 1.
```

Corollaries at the reviewed scope: Fable Theorem C4(iii) is false as written
and true after MST-3; Fable §5's "two nontrivial residue conditions" at
`j = 17` do not exist; Fable's verdict that `s*+17` is the first genuinely
unspent consequence is invalidated; the proposed `TD12-B25-RESROW/v1`
kill/emission descendant at `j = 17` has no target. Fable C4(i), C4(ii), the
`L_j` form, the kernel, and the fifty-to-two orbit collapse all survive.

**Not covered by MST**, and unchanged by this review: Theorems A and B; C1
items 1-4 and C2 (granted conditionally, as Sol does); C3 beyond the `gamma`
recheck of §7.3; the promoted `(E_s)`; Theorem D; Prop 8.1(i),(iv); the T1
ratio; the bchild underdetermination; `CAP-B25`; `SUBTOP-TRANSPORT-B25`;
`OCCURRENCE-B25`.

## 11. Repairs required

```text
To Fable's report (erratum, both sites):
  F-1  C4(iii): (p^I T_j)' = p^(I-i) RHS_j/(25 i lambda_f) = p^m RHS_j/(...).
  F-2  Section 5: (p^i T_17)' = RHS_17/(25 i lambda_f); and DELETE the
       "first genuinely unspent consequence" verdict and the "solvability is
       exactly two residue conditions" sentence at j = 17. The row is
       unconditionally solvable and spends nothing.
  F-3  C1: alpha = c_g lambda_f^(-3/2), or state and propagate lambda_f = 1.
       (Already bound by the coordinator integration §2 as s_0 = c_g^2/lambda_f^3.)
  F-4  Section 10: the TD12-B25-RESROW/v1 descendant is answered, not open;
       its emitted state is RESROW_VACUOUS_ON_CLASS, in Fable's own vocabulary.

To Grok's review (minor, does not change PASS_WITH_REPAIR):
  G-1  Repair item 6's general form "p^(I-1) RHS_j/(25 i lambda_f p^(i-1))" is
       correct but should be reduced to p^(I-i) = p^m to avoid re-introducing
       the same slip downstream.
  G-2  The "simple pole of RHS_17 at an A-root" countermodel is void (§5.3).
  G-3  "Two deck-orbit conditions survive after the repair" is refuted at
       j = 17: zero conditions survive.

To Sol's report (both in §6 frontier guidance only):
  R-A  Add C_17 to the j = 42 consumption list, with the affine-dependence
       observation and the "two conditions in one unpinned constant" count.
  R-B  Replace "not the B24 window" with an index-free formulation, pending
       OPEN(WINDOW-INDEX-B25).

To canonical notes (wording only; all currently correct as provisional):
  N-1  APPROACHES.md:100-105 and notes.md:13343-13350: apply R-A and R-B.
  N-2  Upgrade "provisionally" to "reviewed" for the j = 17 stop once this
       report is integrated; the j = 42 marker stays provisional.
```

## 12. Typed OPEN

```text
OPEN(J42-NONVACUITY)
  Are the two j = 42 orbit residues nonzero and independent on the admissible
  class? Undecidable on the frozen basis: needs P_1..P_42 values (none exist)
  and C_17 (unpinned). Do not assume nonvacuity; do not assume vacuity either
  -- MST-7 shows the m >= 1 obstruction is generically live.

OPEN(NONRESONANT-EXISTENCE-B25)
  Is existence of T_j in C[eta][1/p] at non-resonant j a real condition on a
  formal (V)/(W) jet, and if so what is it? Raised by Grok, acknowledged by
  Sol, typed by no one. Until closed, "first possibly nonvacuous row" must be
  read as "first possibly nonvacuous RESONANT row".

OPEN(WINDOW-INDEX-B25)
  Is P_a (drop a from the top of f^F) the same index as the depth-a datum of
  the B gate / the ledger index s (drop from the top of g^F)? Fable §5 asserts
  the identification, Grok and Sol inherit it, no charged document types it.
  No conclusion in this report depends on it.
```

## 13. Stop and launch decisions

```text
STOP   TD12-B25-RESROW/v1 at j = 17.  CONFIRMED and upgraded from provisional
       to independently reviewed. The row carries no obstruction; there is
       nothing at j = 17 to expand, emit, or kill with. Fable §10's descendant
       and Grok §10's corrected-recursion descendant are both ANSWERED and
       CLOSED, not merely deferred.

DO NOT LAUNCH  any j = 42 lane. Four independent blockers (§6.4): no P_k value
       for k >= 1 in any packet; C_17 unpinned; CAP-B25/OCCURRENCE-B25; and the
       41-row symbolic cost. Requires a source-bearing client that supplies
       P-values AND pins or eliminates C_17 -- neither exists on this basis.

LAUNCH (cheap, optional)  a Fable C3/C4 erratum installing F-1..F-4. It is a
       document repair, not research, and needs no new mathematics: MST-1..3
       and MST-5 are complete and checked.

DO NOT REOPEN  the window-cascade lane; nothing here touches it. Route
       separation from the sibling nu = 17 route is preserved: no object in
       this report may be reused there.

NO CHANGE  to Theorems A, B, C1, C2, C3, or to any promoted result. The
       coordinator integration's "PROMOTE C4 OPERATOR/KERNEL STRUCTURE WITH
       CORRECT FIRST-RESONANCE FORM" stands and is now reviewed; its rider
       "does not prove that the two orbit residue functionals are nonzero"
       is upgraded to "they are identically zero".
```

## 14. Nonclaims

Not claimed here: any value of `P_k` or `v_(B,k)` for `k >= 1`; any occurrence,
realizability, gluing, landing, or coverage result; any serialized `PairRef`;
any degree or `kappa_F` cap; any kill, exclusion, or survival of the B route;
any gate verdict or level advance; any exit price (`charge_basis` absent by
design and by task); any `td` bound, panel closure, book, counterexample, or
JC2 consequence. Theorems A and B are not reviewed. C1 items 1-4, C2 and C3
are granted conditionally exactly as Sol grants them and are not
independently established here, except for the `gamma` recheck (§7.3) and the
C1 scale (§7.1). `j = 42` is neither shown nonvacuous nor shown vacuous. The
absence of an obstruction at `j = 17` is **not** evidence for or against the
existence of a counterexample on this route; a vacuous row is silence, not a
survival theorem. The structural toy of §9 is a control, not a model of the
B state; the deck action and weight lattice are handled by desk argument
(§5.5) and not by the checker.

Execution disclosure: worked only in `/Users/dc/code/math/jc2`. No access of
any kind to `jc2-lean` (not read, listed, stat-ed, grepped, built, or
modified). No web, AWS, remote shell, CAS, or heavy local computation. No
commit, no push, no external message. Exactly one repository file written:
this report. Scratch confined to `/tmp/b25resrow/`. Five canonical files were
read for propagation checking and none was edited.

## Seal

Git basis `40c1ab3448209e3d87173feb947a733f6fe54f7f`, re-verified unchanged
immediately before sealing. Body = all bytes of this file before the literal
`## Seal` heading.

Charged inputs (file sha256 / body sha256), all recomputed at seal time:

```text
edfec0a0d9abb8b24db9406bdc1147348114f198a4a9e92a10486bbe9131a720 / 9c72c20e02efcb74fd351f7ac820268386a625dbfc60b855dc18a1e212766b4f
  xmodel/td12-b25-resrow-v1-provisional-sol56-20260829.md                                 (11988 B)
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b / 539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md                                (39510 B)
20684d3e5ea0f070817c08c72d0dd1b45e691787429bd8eb57eaf68296431bf8 / dab4058f598c05dbd5d00448c7e36c56dbbbfa7869ec3df3189f4640876a85b4
  xmodel/td12-global-source-bridge-b-fable5-hostile-review-grok46-92e-20260829.md          (41244 B)
c6c1d5fe6df7796cac468fb81db16b3bbce777c305d869b9ad46cbb88a16f339 / 89fc2555eeeb4424a45cde47a16b910b3a34b9ac42a3b91717d89e5442b759d5
  xmodel/td12-global-source-bridge-b-coordinator-integration-sol56-20260829.md              (6243 B)
```

Control script (scratch, not a repository file):

```text
229160243f0edc0710d66f22c43614fe69d22793068e96c4bcb381c9b4697753  /tmp/b25resrow/resrow.py
```

```text
report_body_bytes = 37413
report_body_sha256 = 2e5a062fc0dc2e49c3fa5596d41c165aaead03ac91736d0ead040bd48a31d59c
```
