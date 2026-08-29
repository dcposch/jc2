# Hostile review — direct total-family `T-cs` certificate (Fable 5, 20260827)

Reviewed report:
`xmodel/max12-812-order2-p0-total-rees-t-cs-direct-total-certificate-opus5-20260827.md`,
SHA-256 `7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f`
(rehashed this session, matches the tasked pin).
Reviewer: Fable 5, different-model adversarial algebra review.
Date: 2026-08-27

Verdict: **CONFIRMED.**

Conditional on the frozen V9/V17 exact-`Q` bytes (all rehashed, §2), the
claimed containment

```text
cs^447 * k^164  in  ( Tg10_1..Tg12_7, Tg14_5,
                      rs-cs*qrs, c0-cs*qc0, c1-cs*qc1, qrs )   over Q   (*)
```

is **true**, and it is of the requested direct type
`cs^N*k^M*(1+rho*W)` with `W = 0`.  Every load-bearing identity in the
report was re-derived here by **full exact expansion** from the frozen
bytes with a from-scratch `fractions.Fraction` sparse-polynomial engine —
no sampling, no banners, no reuse of any producer script.  The two machine
reductions (5.3)/(5.4) were **independently replayed** from the printed
seven-rule system and reproduce every printed structural invariant
(term counts per row, denominators, support shapes) exactly; the resulting
identities were then verified by full expansion.  Both of the report's own
critical findings — the too-broad interface-theorem converse and the
missing V19 typing test — **check out against the frozen promotion and
compiler bytes**, and I supply an explicit two-line counterexample for the
former (§6).  All defects found are LOW except one MEDIUM custody item
(the report's canonical hashes for `X`, `C`, `D` are unverifiable as
printed because no serialization is specified); none is mathematical.

## 1. Claim-by-claim table

| # | Report claim | Independent check | Result |
|---|---|---|---|
| 1 | Report SHA-256 `7af66e58…` | `shasum -a 256` | MATCH |
| 2 | §0: 11 document/prereg/compiler hashes | all rehashed | 11/11 MATCH |
| 3 | §9: V9 manifest + 21 rows + V17 `RESULT.json` + `Tg14_5_q.poly` | all rehashed; "manifest" identified as `aws_q_v9/COEFFICIENTS.json` via the V18 compiler pin | 24/24 MATCH |
| 4 | `Tg10_6.poly`, `Tg11_6.poly` are the two-byte file `0\n` | `xxd` + shared hash `9a271f2a…` | PASS |
| 5 | All `rho` exponents even in all 22 rows | exponent census, raw and substituted | PASS (exps ⊆ {0,2,4,6,8}) |
| 6 | Charted term counts `4,5,5,2,5,0,5 \| 12,14,17,3,18,0,18 \| 27,36,47,12,58,9,60 \| 304` | fresh parse + chart map `rs→cs*qrs, c0→cs*qc0, c1→cs*qc1` (identical to the frozen compiler's `chart_expression`) | 22/22 MATCH (raw counts identical; census also matches the Grok-corrected witness census, `0` not `1` for the zero rows) |
| 7 | Lemma 0 identity for all 22 rows | division-free telescoping (order `rs, c0, c1, qrs`), identity re-expanded per row | 22/22 EXACT |
| 8 | Lemma 0 cofactor count table `(2,1,1,1)…(131,38,45,97)` | counts of my independently constructed `B`'s | 22/22 MATCH — pins their construction; no hidden division by `cs`, `k`, or `rho` is possible in this construction |
| 9 | §3 `gam/del/alp/bet` displays, `Tg10_5` relation, `Tg10_6 = 0` | full expansion from bytes | 6/6 EXACT |
| 10 | Prop 3.1 (no common zero with `cs,k,rho ≠ 0`) | case logic replayed on the certified displays; needs only `2,3,5` invertible | SOUND |
| 11 | §4 nine-line chain | free-symbol expansion in `Q[u,w,p,a0,a1,kap]`; note `- p*w^3` in line 5 denotes the line-3 polynomial itself | 9/9 EXACT |
| 12 | Certificate (a), substituted: `cs^6k^2rho^6 = A1*E10_1+A2*E10_2+A3*E10_3+A4*E10_4` | `A1..A4` parsed from report bytes; full expansion | EXACT |
| 13 | Certificate (a), honest ordered, with printed `B_rs,B_c0,B_c1,B_qrs` | full expansion against the **raw** rows and bilinears | EXACT; printed `B`'s also equal `Σ A_i·B^{(i)}` from my Lemma 0 term-for-term |
| 14 | §5.1 solved forms `B1..B7`, `B2/B3/B4` zero tails | all seven ideal-element identities expanded (`head − tail = Σ rowcof·Ebar`) | 7/7 EXACT |
| 15 | (5.2): free part of `Ebar14_5 + (cs/2)Ebar12_2` w.r.t. `(qc0,qc1,e0,a0,ell1)` is exactly `−(7/256)cs^5k`; `\|g\| = 57` | recomputed from bytes | EXACT, 57 terms; constant agrees with the fibre-promotion display |
| 16 | (5.3): `1 − X = Σ C_i Ebar_i`; `\|X\|=341`; denoms `cs^16k^6`/`cs^18k^6`; 11 monomial shapes; `a0*e0` absent; `C` row counts `32,277,87,200,51,1,38,29,1` (716) | reduction replayed from the printed rules and priority; identity verified by full expansion | EXACT; **every** printed invariant reproduced (my elementary-replacement count is 879, not 1880 — see defect L1) |
| 17 | (5.4): `phi(X)` 13 terms; `phi(X)^3 = Σ D_i phi(Ebar_i)`; `D` counts `10,152,10,156` (328); denoms `cs^36k^9`; `NF(phi(X)^2)` 6 terms | replayed; identity verified by full expansion; `D` verified `qc0/qc1`-free (needed for the verbatim lift) | EXACT, all invariants match |
| 18 | §5.5 denominator table `(146,54),(147,54),(132,45),(120,36),(108,27)` and clearing exponents `(147,54)` | recomputed from the actual denominators of `X`, `C`, `D` plus multiplicativity bounds | MATCH; `cs^147k^54` clears |
| 19 | Certificate (b): `cs^147k^54 ∈ (Ebar_1..Ebar_22)` with polynomial cofactors; lift (5.5) to `cs^147k^54 + rho^2·H ∈ I` | forced by items 14–18 + even-`rho` (item 5) + formal algebra (§3 below) | ESTABLISHED |
| 20 | §6.1 composition and `(N,M) = (447,164)` | `(A+Bq)(A^2−ABq+Bq^2) = A^3+Bq^3`, `Bq^3 = rho^6H^3`; `cs^{6+441} = cs^447`, `k^{2+162} = k^164`; both right-hand terms in `I` | EXACT |
| 21 | §6.4 geometry: outright emptiness `V(I) ∩ D(cs*k) = ∅`, strictly stronger than the promoted fibre statement; interface converse too broad | verified; counterexample supplied (§6) | CONFIRMED, incl. the flag |
| 22 | §7 V19 typing: acceptance predicate lacks the divisibility test; Lemma 0 absent from V18/V18R1/V19; `psi`-clearing algebra | frozen `compile_t_cs_certificate_v19.py`, `compile_t_cs_rho_unit_v18.py`, `v18r1.py`, both preregistrations read | CONFIRMED with one precision defect (L3) |
| 23 | §11 scope firewall | checked against the interface and fibre promotions | ADEQUATE |

## 2. Custody: everything rehashed this session

All 11 hashes in report §0 (four xmodel documents, V18/V18R1/V19
preregistrations, three compilers) and all 24 in §9 (21 V9 `Tg*.poly`,
`aws_q_v9/COEFFICIENTS.json` = the "V9 manifest" `86c535a3…`, V17
`RESULT.json` `25d40556…`, `Tg14_5_q.poly` `91d96924…`) match the on-disk
bytes.  The report's own hash matches its pin.  The report's five `/tmp`
script hashes are session-local to the producer and were **not**
verifiable; they carry no evidential weight here — this review's evidence
is its own replay.

Boundary kept: no Singular/Groebner, no AWS read or mutation, no
`jc2-lean`, no web, no V18R1/V19 engine output read.  Local tools:
`shasum`, file reads, and four fresh Python scripts (sparse exact-`Q`
arithmetic, `fractions` only), staged session-local under `/tmp/jc2rev/`,
not committed:

```text
d92f68741aa4ecad41c332dbbf2ba212785fbcbd19e1ad530a1e9ce892d9162a  polylib.py
4923eae3c7765fcd783732a9b8c2106c0888f3f8c78aa9ceb709b130cd54c719  stage1.py
5639538f0613f263a9e86832d8067476be6c1a2649db1c421d282642c65b7014  stage2.py
79d5263b6fc5e0c7fd9e0ea55734c72739db1152585b546c591890277e092dee  stage3.py
```

## 3. What was proved by expansion, and what is forced algebra

The composite cofactors of (*) are not serialized in the report (§6.2).  I
therefore separated the certificate into its computational facts, each
verified by full exact expansion, and its assembly, which is
characteristic-free polynomial algebra with no further computational
content:

Verified by expansion (this session): Lemma 0 (22 rows), the four
grade-10 displays plus two side facts, the nine chain lines, Certificate
(a) in both presentations with the printed cofactors, `B1..B7`,
(5.2), (5.3), (5.4), the `qc`-freeness of `D`, the even-`rho` census, and
the actual denominators of `X`, `C`, `D`.

Forced by the above with zero additional computation:

1. `1 = (1−X)(1+X+…+X^8) + X^9` — geometric series.
2. `X^9 = (Y + W_J)^3` with `Y := X^3 − W_J` — binomial identity.
3. `phi(Y) = phi(X)^3 − Σ D_i·phi(Ebar_i) = 0` (ring map `phi`, `D`
   `qc`-free, (5.4)), so every monomial of `Y` carries `qc0` or `qc1`;
   hence every monomial of `Y^3` has `qc`-degree ≥ 3 and is divisible by
   `qc0^2`, `qc0*qc1`, or `qc1^3`, each an element of `J[1/(cs*k)]` with a
   **zero-tail** one- or two-term cofactor (B3, B2, B4; worst extra cost
   `cs^3` from B4).
4. Denominators: `denom(X^j) | (cs^16k^6)^j` etc.; the five-row table of
   §5.5 follows and `cs^147*k^54` clears every cofactor into a polynomial.
   Hence `cs^147k^54 = Σ Γ_i·Ebar_i` with `Γ_i` polynomial and `rho`-free.
5. (5.5): `Σ Γ_i·E_i = cs^147k^54 + rho^2·H` with `H` polynomial, because
   `E_i − Ebar_i ∈ (rho^2)` (even-`rho` census).
6. §6.1: `cs^447k^164 = cs^6k^2(A+Bq)(A^2−ABq+Bq^2) − H^3·(cs^6k^2rho^6)`,
   both right-hand terms in `I`; Lemma 0 then maps `I`-membership into the
   honest ordered ideal `K` with the bilinear/`qrs` cofactors it supplies.

So the answer to the serialization question is: **yes, the printed
generating data suffices** to establish existence of the polynomial
cofactors of (*).  Steps 1–6 are constructive and deterministic given
`X`, `C`, `D`, which I rebuilt independently from the printed rule list
and priority and pinned by full-expansion identities — not by trusting
any hash or sample value.

Replay telemetry (mine, for the record): `|X| = 341`, min exponents
`(cs,k) = (−16,−6)`; `C` per-row `Tg10_2:32, Tg10_3:277, Tg10_4:87,
Tg11_1:200, Tg11_2:51, Tg12_2:1, Tg12_3:38, Tg12_4:29, Tg14_5:1` (716),
min exponents `(−18,−6)`; `|phi(X)| = 13`; raw `|phi(X)^3| = 308`,
normal form `0`; `D` per-row `Tg11_1:10, Tg11_2:152, Tg12_3:10,
Tg12_4:156` (328), min exponents `(−36,−9)`; `NF(phi(X)^2)` 6 terms;
`X` monomial shapes exactly the 11 printed; `ell1` and `a0*e0` absent
from `X`; no negative exponent on any variable other than `cs, k`
anywhere.  Substituted-row census: `E` term counts
`3,3,4,2,4,0,4 | 8,8,12,3,13,0,13 | 19,22,32,9,39,4,40 | 207`; `Ebar`
`2,2,1,1,0,0,0 | 6,4,4,2,1,0,0 | 15,13,13,6,7,1,1 | 64`; charted
inventory 40 names (= the V19 ring's "40 chart names"; ring count 42 with
`u,v`, matching the Grok fibre review).

Portable canonical hashes of my replayed objects, serialization =
newline-joined sorted lines `"<Fraction> <name^exp*…, names sorted>"`
(future replays can compare):

```text
X          0dfaeba47364b5db91c6ee524c1e5c921885dc0bc3c42a9951cd8f094fed2af0
C[Tg10_2]  75e4d4fe182ebe36e0dce9ac8bd6caf89f9cdc3181333a233807b1cc050df960
C[Tg10_3]  e84a4d4ad2edf20b2f682580e36cb116cdea2e224ef3558a4f98367dcb7af76f
C[Tg10_4]  9845474209100abb95bfd63fbf8d7dd9a50f0d217e543ce853dae3f8a9db138d
C[Tg11_1]  998a7fe7cfec6c38e53b6de93388414fcbf6c517bcf982c1dd61413c05edb5ef
C[Tg11_2]  5cbd04fc158e2d6f91f95a74762d249162ea8bacba0020828ee0ea92ee2d427e
C[Tg12_2]  5b816d6089715577d37375f641da84c68d75e905f6a1f12682e8f33ec806db31
C[Tg12_3]  b0e460941d4c97c2fa437c11391da9dcf74e9921ce3facf544740ee2be42367f
C[Tg12_4]  f22bc2c67ecb1f9f67463c38facf9e337cdbe7ffaafc21e61c19918672990aff
C[Tg14_5]  fc08afeea246439108e1464d83f355028f4dc94d128390a7a5d0d08331f03986
D[Tg11_1]  fee1b2f485c81ff8c6f8fe8e7cd99bf7aadc5e3bf0785c5fef54875847ad4c18
D[Tg11_2]  b85913c4ffecc446138ac2015388400fa77630b85c3510828564eb4ad870824e
D[Tg12_3]  db79cb3bd5022bc988214cbc9cfe779a7c0b9fd88919cafeb0fd2fd60ce8dfcc
D[Tg12_4]  62b4a9c9fe83fbaa6264ea371e502e7ed26fa1bad830c88e7472b57f1844733d
```

## 4. Generator order and the two presentations, pinned

The literal ordered generator list of (*) is
`Tg10_1,…,Tg10_7, Tg11_1,…,Tg11_7, Tg12_1,…,Tg12_7, Tg14_5,
rs−cs*qrs, c0−cs*qc0, c1−cs*qc1, qrs` — 22 raw rows (raw variables `rs,
c0, c1`, **no** substitution, confirmed by variable census: no
`qrs/qc0/qc1` occurs in any raw row), the three `T-cs` bilinears, and the
ordered equation `qrs`.  This matches the chart registered by the V18
preregistration and fibre promotion (`rs=cs*qrs, c0=cs*qc0, c1=cs*qc1`,
ordered complement `qrs=0`, localizer `k`), with the bilinears restored
as honest generators.  Ideal membership is order-independent; the order
matters only for cofactor bookkeeping, and the report's cofactor indexing
is consistent with this list.

The substituted presentation (`E_i` rows, no `rs/c0/c1/qrs`) is what
V18/V18R1/V19 actually compute in: the frozen V18 compiler substitutes by
regex **before** Singular ever sees the rows, and its ring does not
contain `rs, c0, c1` at all.  Lemma 0 is therefore genuinely the only
bridge from any V18/V19-style output back to the honest ordered
presentation, and the report is the first place that bridge is written
down and certified.  My replay confirms both directions and confirms that
the report's §1 map ("`chart_expression` composed with `qrs = 0`") is
byte-identical to the frozen compiler's map.

## 5. Defects

**HIGH — none.**

**MEDIUM**

- **M1 (custody, not math).**  §5.3/§5.4 print "canonical sha256" values
  for `X`, `C`, `D` and §6.2 offers them as the byte-level audit hook,
  but no serialization is specified, so those hashes are unverifiable in
  principle by any other party.  I could not confirm them and did not try
  to guess the format.  The hook the report offers cannot be exercised as
  printed.  Mitigation here: every printed structural invariant of
  `X, C, D` (counts, per-row distribution, denominators, shapes) was
  reproduced independently and the identities (5.3)/(5.4) verified by
  full expansion, so the mathematics does not rest on those hashes.
  Repair: state the serialization, or print the objects.

**LOW**

- **L1.**  "1880 rewrites" is not reproducible from the printed
  specification: the rule list and priority are printed, but the
  monomial-selection strategy is not.  A faithful replay (batch per
  priority pass, one count per elementary monomial replacement) yields
  **879** replacements with bit-identical structural output.  Telemetry
  only; the normal form and cofactors are what matter and they agree.
- **L2.**  §1's ring `S` is declared as "`cs, k, rho, qc0, qc1`, and the
  30 remaining names"; the correct count is 34 remaining (39 names,
  `S# ∖ {rs,c0,c1,qrs}`), of which 38 total actually occur in the
  substituted rows (`rs4` dies with the `qrs`-terms).  The `S#` list
  itself (43 names) is exactly right.  Harmless: all identities are
  variable-explicit.
- **L3.**  §7's "Exact condition" first form is correct (`psi(L_24)` must
  have no negative power of `cs` or `k`), but the glossed componentwise
  form ("one needs `cs^alpha k^beta | L_24^{(alpha,beta)}` for every
  `(alpha,beta)`") is **sufficient, not equivalent**: negative powers can
  also cancel between different `u^alpha v^beta` components.  Any future
  preregistered test should check `psi(L_24)` after combining, not
  componentwise.
- **L4.**  §3–§5 write `Tg10_1` etc. for the **substituted** rows `E_f`
  while §1 defines `Tg*` as the raw literal rows; e.g. the §3 displays
  are false for the raw rows (each carries an extra `rs`-term).  Context
  disambiguates, but the overload invites misquotation.
- **L5.**  §9 says "Exact-`Q` V9 manifest `86c535a3…`" without naming the
  file; it is `aws_q_v9/COEFFICIENTS.json` (identified via the V18
  compiler's pin).  `EVIDENCE.sha256` and `FREEZE.sha256` hash
  differently; a reviewer matching by filename alone would miss.
- **L6.**  The verdict-section sentence "the only localization used is at
  `k`" is justified only under the interface theorem's typing (the
  `cs`-power is absorbed freely by the saturated chart presentation); as
  a statement about the polynomial identity itself, `cs^447` and `k^164`
  enter symmetrically.  §6.4 and §11 state the geometry correctly, so
  this is wording, not substance.

## 6. The two criticisms the report itself raises — both verified

**Interface-theorem converse (§6.4).**  The promotion document
(`total-rees-localized-rho-unit-staged-calculus-promotion-sol-20260827.md`,
hash matched) states: *"Conversely, chart-fibre emptiness has a
homogeneous power-containment form after clearing a finite saturation
exponent."*  Read as producing the theorem's own certificate type (2) —
`f^N*s*(1+rho*W)` with **polynomial** `W` — this is false, and the
report's diagnosis of the gap (`(cs*k)^m | G`) is exactly right.
Counterexample: `I = (cs − rho) ⊂ Q[cs, rho]`, `f = cs`, `s = 1`.  The
`rho = 0` fibre on `D(cs)` is empty (`cs ∈ I + (rho)`, exponent 1), yet
no `cs^N(1 + rho*W) ∈ I` exists for any polynomial `W`: substituting
`cs = rho` gives `rho^N(1 + rho*W(rho,…)) = 0` in `Q[rho]`, impossible.
What fibre emptiness does give is the **localized** unit statement
(`rho` a unit in the chart ring localized at `cs*k`, with
denominator-carrying `h` — the sense in which the V18 preregistration's
"hence rho is a unit" sentence is true); the polynomial type (2) is
equivalent to the strictly stronger
`1 ∈ (I : (cs*k)^∞) + (rho)`, i.e. emptiness of `V(rho)` on the
**closure** of the localized stratum, exactly as the report's two-bullet
comparison states.  The report's flag — repair or restrict the converse
clause — is endorsed; it does not affect the promoted forward direction
or this certificate, which meets type (2) outright with `W = 0`.

**V19 typing (§7).**  From the frozen compilers and preregistrations
(hashes matched; no engine output read): the V19 acceptance predicate is
precisely `LiftResidual == 0`, `LiftScalar` a nonzero constant, and three
artifact writes; the generator order is `E1..E22, qrs, rho, 1−u*cs,
1−v*k` (so `L_24` is the `rho` cofactor, as the report indexes); the ring
is `(u, v, 40 chart names)` with block order `(dp(2), dp(40))`.  **No
divisibility test on `L_24` exists anywhere in the predicate**, and no
honest-chart translation exists anywhere in V18/V18R1/V19 — the raw
variables are regex-substituted away before Singular runs, so Lemma 0 is
a genuinely new obligation, discharged for the first time (and verified
here) by this report.  The `psi`-clearing algebra of §7 is sound:
`psi` kills `L_25, L_26`, and `cs^a*k^b` clears every cofactor, yielding
the V18R1-positive form (branch (b)), which becomes the total-family type
only if `cs^a*k^b | Lam_24` (modulo L3's precision note).  The three-step
repair path, including composing a failed-divisibility V19 output with
Certificate (a) at cost `(3a+6, 3b+2)`, is arithmetically correct.
Whether V19 still runs is a protocol decision; nothing here converts
V18R1 or V19 into a recorded result.

## 7. Narrowest accepted theorem

> Conditional on the frozen V9/V17 exact-`Q` bytes pinned in §2, over `Q`:
> `cs^447 * k^164` lies in the ordered ideal
> `(Tg10_1..Tg12_7, Tg14_5, rs−cs*qrs, c0−cs*qc0, c1−cs*qc1, qrs)` of
> `S#`, by a polynomial identity inverting nothing — equivalently
> `cs^447*k^164*(1+rho*W)` with `W = 0`, the strongest instance of the
> requested unit-plus-`rho` type.  Consequently `V(K) ∩ D(cs*k) = ∅`
> outright (all `rho`), the `rho ≠ 0` half already from
> `cs^6k^2rho^6 ∈ (E(Tg10_1),…,E(Tg10_4))` (grade 10 only), and, in the
> `cs`-saturated honest chart, the registered ordered `T-cs` stratum lies
> over `V(k)`.  Exponents `(447, 164)` are certified, **not** minimal.

Under the memory-registered `T-cs` typing gate ("certificate types iff
the `rho`-cofactor is divisible by the cleared power"): `W = 0` makes the
divisibility trivial; the certificate types.

## 8. Firewall of nonclaims

Not established, and not to be cited to this review:

- anything about the unfrozen upstream: the V9/V17 rows were **not**
  re-extracted from the Faber emitter; the literal-source provenance debt
  is inherited in full, exactly as the report says;
- the `k = 0` residual stratum (now carrying weight `k^164`) — live and
  registered, untouched here;
- the full `T-cs` chart, `T-c0`, `T-c1`, either second-stage `A` chart,
  chart overlaps, the terminal all-zero receiver, the deck/square bridge,
  the generic comparison, any effective decisive-grade bound, Gate `T`,
  order two, the `(8,12)` frontier, maximum twelve, TD6, the prime-ray
  lane, AS109, any Lean statement, or JC2;
- minimality of `(447, 164)`; the §6.3 shrink analysis (including the
  claimed grade-10 obstruction `a0^n w^n` and the reported divergence of
  the unified rewriting system) was **not** audited — the report marks it
  open/informational and nothing rests on it;
- the `F65521` lane (the report does not assert it; neither do I);
- any validator PASS: no V18R1/V19 engine output was read by producer or
  reviewer; this review harvests nothing and converts no protocol state;
- the producer's `/tmp` script hashes and the report's canonical `X/C/D`
  hashes (M1): unverified and carrying no weight — the confirmations above
  rest exclusively on this session's own expansions;
- the interface theorem's converse clause remains flagged as needing
  repair or restriction (my counterexample in §6 is offered for that
  erratum), independently of this chart.

The only repository file written by this review is this one.
