# Blind whole-portfolio scan — Opus 5 — round `20260828T0702Z`

Model: `claude-opus-5` (Opus 5), equal-standing blind whole-portfolio lane.
Packet: `xmodel/ideation-20260828T0702Z-packet.md`,
SHA-256 `b0c9110f85ab19965db086f75dbbb08daa0f9ae8ee2b30ce43ea72ed66d00f1c`
— verified before any other file was opened.

No proof or counterexample of JC2 is claimed here. No model verdict in this
report is mathematical evidence.

---

## 0. Custody, execution boundary, blindness, contamination

### 0.1 Custody gate

All 25 packet hashes (18 canonical/report files plus the 7 machine-readable
custody files for the two newest producers) were checked with
`shasum -a 256 -c` in one batch: **25/25 OK, exit 0**.  `git rev-parse HEAD`
= `418e413593120d19e15e6546eb50c985f4b1f038`, matching the packet basis.  The
worktree is dirty exactly as the packet warns; I did not assume otherwise.

### 0.2 Execution boundary — obeyed

- No AWS contact, no job inspection, no signals.
- No Singular, msolve, Sage, Lean, `ore_algebra`, or any CAS.
- No `jc2-lean` entry, listing, search, read, build, status, or modification.
- No canonical file and no `cases/` file was edited or executed in place.
- All computation was **standard-library Python 3 `fractions.Fraction`**, in
  two throwaway scripts staged under `/tmp` (`/tmp/opus5_local_check.py`,
  `/tmp/opus5_quartic.py`), each running in well under one second.
- My only write is this file.

### 0.3 Blindness and contamination — one real disclosure

I read the packet, my own prompt
(`xmodel/ideation-20260828T0702Z-opus5-prompt.md`, SHA-256
`85af7b93f77c3699fb850361281a9fec6113558c7f4afb45bd4b8ae810f3744c`), and no
peer `0702Z` response.

**Disclosure.**  Late in the session, while checking whether my new mechanism
was already in the repository, I ran a `grep -ril` novelty sweep whose glob
`xmodel/*.md` had by then come to include newly sealed peer files.  The
output listed the *filename* `xmodel/ideation-20260828T0702Z-grok46.md` as
containing the string `root algebra`.  I opened no peer body, and I
immediately excluded `0702Z` from all later searches and re-listed the
directory to bound the exposure (`fable5.md` and `grok46.md` now exist; I
read neither).

**Independence assessment: non-load-bearing.**  (i) One bit was exposed: that
Grok46's response contains the two-word string `root algebra`.  (ii) That
string is already in the charged packet material — §3 of the q1 prefix report
writes "the etale root algebra `Kbar[X]/(A)`" — so a peer using it carries no
information about their conclusions.  (iii) Every mathematical result in §1–§2
below was derived, machine-checked, and written down *before* that grep ran;
the ordering is visible in my transcript.  I therefore do not fail closed, but
I record the exposure as real.

### 0.4 Files read

Complete: the packet; my prompt; the seven new `xmodel` reports
(`fullmodes-sol-ultra`, `fullmodes-hostile-review-grok46`,
`endpoint-collapse`, `fullmodes-independent`, `d7-d22-A-dependency-audit`,
`q1-prefix-d7-d9-divisor-target`, `q1-active-translation-gauge-obstruction`);
`vandobben2608-...-review-codex`; `websweep-20260828T0524Z`;
`ggv-hens-ct-rank-one-control-r0`; the tail-3 superseded stop report; and
`xmodel/ideation-20260827T2259Z-synthesis-sol.md`.
Partial as directed: `APPROACHES.md` (current 06:23Z overlay in full, plus the
complete 46-row master union table and the executive summary);
`AUDIT.md` (top corrections, lines 1–150); `PROGRESS.md` (all of the current
day 2026-08-28); `notes.md` (newest `LIVE STATE` and all later events, plus
the head for orientation and targeted lane greps); `COORDINATION.md`
(protocol through the speculative-parallelism section).  One extra file
outside the packet, for an honest novelty comparison only:
`xmodel/ggv-upper-endpoint-tail2-fullfixture-ideation-hostile-audit-sol-ultra-20260828.md`
(the "Newton scaling" hit).  I did **not** read the PDF at `refs/`; I relied
on the two charged audits of it.

---

## 1. Question 1 — is the provisional D9 repair correct?

**Verdict: `CONFIRMED` on every divisor endpoint I could reach, by an
independent method, with one scope strengthening and one documentation gap.
Label remains `PROVISIONAL` — this is a second desk, not a promotion.**

I did not replay the producer's checker.  I built a different model of the
same object and compared closed forms and literal numbers.

### 1.1 The independent method: root-local Newton rescaling

Fix a root `a` of the squarefree quartic `A` at which `V0` vanishes (a root of
`C=gcd(A,V0)`).  Put `eps = X-a`, `A = eps*al` with `al(a)=A'(a) != 0`, and
`V0 = eps*v`.  On the reduced prefix

```text
F0=A^4,  F1=A^2 V0,  F2=(V0^2+A^2 Z)/4,  F3=(V0 Z+A T)/8
```

the local orders are `ord_a F_i >= max(0, 4-i)` for every `i`.  Rescaling
`t = eps*s` therefore gives a *uniform* leading order:

```text
eps^{-4} F(eps*s) = Phi(s) + eps*Phi_1(s) + eps^2*Phi_2(s) + ...,

Phi(s) = al^4 + al^2 v s + ((v^2+al^2 Z)/4) s^2
                + ((v Z + al T)/8) s^3 + F4 s^4.
```

Two immediate structural facts.

**(LQ-1) Local square form.**  With `Psi(s) = al^2 + (v/2)s + (Z/8)s^2` and
`K = 64F4 - Z^2`,

```text
Phi(s) = Psi(s)^2 + (al T/8) s^3 + (K/64) s^4.
```

So the *only* deviation of the local quartic from a perfect square is the pair
`(T(a), K(a))`.

**(LQ-2) Valuation lemma.**  For any exponent `beta`,
`ord_a( (F^beta)_n ) >= 4*beta - n`, and the coefficient of `eps^{4*beta-n}`
is exactly `[s^n] Phi(s)^beta`.

*Proof.* Each monomial of `(F^beta)_n` is `A^{4beta} * prod_m F_{i_m} / F_0^j`
with `sum i_m = n`, of order `4beta + sum_m ord_a F_{i_m} - 4j >=
4beta + sum_m (4-i_m) - 4j = 4beta - n`. □

**(LQ-3) Uniform mode firewall (new, and uniform in `n`).**  Mode
`c_m t^m F^{(12-m)/8}` contributes to weight `n` with

```text
ord_a >= 6 + m/2 - n,
```

while the principal branch `F^{3/2}` reaches `6-n`.  **Every characteristic
mode is shallower than the principal branch by exactly `m/2`, at every weight,
at every `C`-root.**  Hence at a `C`-root no mode can ever cancel the deepest
pole class.  This replaces, for the deepest class at `C`-roots, the campaign's
per-row causal mode audits (`c6` at D8, `c10` at D11, `c14` at D14, `c16` at
D16, `c18` at D18, `c20` at D20).  It does **not** replace them for subleading
classes, which is where the fixed-fixture kills actually live.

**(LQ-4) The recurrence is the same recurrence, with 5 slots instead of 15.**
Writing `y = Phi^{3/2}` and using `2*Phi*y' = 3*Phi'*y` gives

```text
2 n phi_0 y_n = sum_{i=1}^{4} phi_i (5i - 2n) y_{n-i},
```

which is *literally* the campaign's `n A^4 y_n = sum ((alpha+1)i-n) F_i y_{n-i}`
at `alpha=3/2` with `(F_0,...,F_14)` replaced by the local 5-tuple
`(phi_0,...,phi_4) = (al^4, al^2 v, (v^2+al^2 Z)/4, (vZ+alT)/8, F4)`.
All of `F5..F14` are pushed into the `eps`-corrections.

### 1.2 What the independent model reproduces

Running (LQ-4) symbolically and then numerically (`/tmp/opus5_quartic.py`,
`fractions` only, random rational `al,v,Z,T,K`):

| weight | my closed form for the deepest class | charged producer form | agreement |
|---|---|---|---|
| 7 | `3T(al K - 2Tv)/(2048 al^2)` | (11)/(12): `A^2 \| T(AK-2TV0)`; active `A \| T(K-2TS)` | **exact** |
| 8 | `3[(al K-4Tv)^2 - 8 al^2 T^2 Z]/(32768 al^4)` | (13): `N8=(AK-4TV0)^2-8A^2T^2Z+O(A^3)`, `g8^-=3N8/(32768A^4)` | **exact** |
| 9 (under D7,D8, `T!=0`) | `-T^3/(8192 al^3)` | (19) `P9 = -8B^4U^3`; (20) `-8T^3/65536` | **exact** |

The weight-9 match was checked in both stratum shapes.  For proper `C`, with
`al = C'(a)B(a)` and `T=BU`, my `-T^3/(8192 al^3)` equals the producer's
`-8B^4U^3/(65536 C^3 B^4)` near `a`.  For the active component (`C=A`, `B=1`,
`V0=AS`, so `v=al S`), it equals the producer's complete `A^{-3}` coefficient
`(-8T^3)/65536`.

I also re-derived the two facts the producer states without display:

- The active-`c2` D8 leading equation.  Substituting `V0=AS` in (13) gives
  `g8^- = 3[(K-4TS)^2 - 8T^2Z + 1024A(c6 A^2 S^2 + F5 T)]/(32768 A^2)`, so
  modulo `A` at a root with `T!=0` and `K=2TS`, `4T^2(S^2-2Z)=0`, i.e.
  `S^2 = 2Z`.  This is the missing step behind "the leading D8 equation then
  gives `S^2=2Z`".  It is correct.
- The claim "every `c2`, `F5`, `F6` contribution begins only at `A^{-2}`".
  By (LQ-3), `c2` reaches at most `n-6-1 = 2` at `n=9`; `c6` at most `0`;
  `F5` enters `Phi_1` hence at most `2`; `F6` enters `Phi_2` hence at most `1`.
  Verified, and now *proved uniformly* rather than asserted at one weight.

### 1.3 Literal fixture replay (independent arithmetic)

From `A=X^4-1`, `R0=X-1` I recomputed
`V0=6X^4-4X^3-2`, `C=X-1`, `B=X^3+X^2+X+1`, `V1=6X^3+2X^2+2X+2`,
`K=64F4-Z^2=18X^3+2X^2+2X+2` (from the report's `F4`, `Z=9/2`), `T=B`, `U=1`,
and then, with my own dense polynomial arithmetic:

```text
D7 :  T(AK-2TV0) mod A^2 = 0 ,  quotient = 2 + 4X + 6X^2      <- matches the report exactly
D8 :  (K-4UV1)^2 - 8B^2U^2Z mod A^2 = 0 ,  K-4UV1 = -6B       <- matches the report exactly
D9 :  P9 = B^2*(-8X^6-16X^5-24X^4-356X^3+84X^2+92X+100),
      P9/(4B^2) = 25+23X+21X^2-89X^3-6X^4-4X^5-2X^6           <- matches the quoted
                                                                 characteristic fraction
                                                                 numerator over 16384 C^3 B^2
      P9 mod C = -2048 = -8*B(1)^4 != 0                        <- matches (19)
```

Every printed literal in the charged report that I could recompute matched.
I did not attempt the 513-generator raw-window reconstruction.

### 1.4 Coverage of the divisor endpoints

- **`C=1` (generic).**  Not an assumption: `B | T` is *derived*.  At a root `b`
  of `B` with `T(b)!=0`, `ord_b(AK-2TV0)=0` because `gcd(B,V0)=1`
  (from `gcd(CB,CV1)=C*gcd(B,V1)=C`), contradicting `B^2 | T(AK-2TV0)`.  Hence
  `T=BU`, and with `C=1` this already gives `A|T` at D7.  ✅
- **Proper `C` (so `deg B >= 1`).**  Chain verified above; the cancellation
  `-12U^2V1^3 + 24B^2U^2ZV1 = 0` under `V1^2=2B^2Z` is exact, leaving
  `-8B^4U^3`, and `gcd(B,C)=1` (A squarefree) makes `B(c)!=0`.  ✅
- **Higher-order `V0` vanishing at a simple `A`-root** (`C` still simple there
  but `ord_a V0 >= 2`, so `V1(a)=0`).  Not separately discussed by the
  producer.  I checked it: D7 gives `K(a)=0`, D8 gives `Z(a)=0`, and my local
  model still yields `[s^9]Phi^{3/2} = -T^3/(8192 al^3)`.  ✅ **no gap.**
- **Active `c2` (`C=A`, `B=1`, `c2` and `c6` live).**  Verified in §1.2.  ✅
- **Mode valuations.**  Now covered uniformly by (LQ-3), not row-by-row.  ✅

### 1.5 One scope strengthening the producer did not claim

**The D9 repair does not use `q1`.**  The implication
`D1=...=D9=0 => A|T` uses only: the reduced prefix (1); the `D1..D6` branch
condition `c2=0 or A|V0`; and the divisor split `C=gcd(A,V0)`, `A=CB`,
`V0=CV1`, `T=BU`.  The `q1` convention `V0=A'R0+2AR0'` enters the report only
to (a) rewrite `gcd(A,V0)` as `gcd(A,R0)`, (b) identify the active component
as the one-parameter family `R0=lambda A`, and (c) bound `deg R0 <= 4`.  None
of these is used in the implication; and my derivation never mentions `R0`.

This matters a lot, because `q1` is licensed *only* by D23, so the packet
correctly flags the whole general-`V0` lane as downstream of an unproved gate.
It is not: `q1` cuts the `V0` space from 8 dimensions (`deg V0 <= 7`, forced by
`deg F1 <= 15`) to 5 (`R0 |-> A'R0+2AR0'` is injective on `deg R0 <= 4`).
Dropping it makes the theorem **strictly stronger and no longer D23-conditional.**

### 1.6 The one real defect I found

**Documentation `GAP`, not a mathematical error.**  The active-`c2` argument
in §5 of the charged report invokes "the leading D8 equation" without ever
displaying an active-`c2` D8 formula, while its only displayed D8, equation
(13), is explicitly labelled *"the c2-zero negative part"* and carries a `c6`
term but no `c2` term.  A reader cannot check the active step from the report
alone.  I supplied the missing derivation in §1.2 and it is correct — but a
hostile reviewer working only from the bytes should record this as a `GAP`
until the active D8 polar and its `c2` pole-order bound are serialized.

---

## 2. Question 2 — fastest exact route through the post-D9 `W` split

The packet asks for "a root-algebra, valuation, differential-operator,
norm/resultant, or equivariant compression before chart fanout."  The local
model above is all five at once.  Here is the route.

### 2.1 Grade the whole cascade in `eps`, not in `A`

Because `Lambda(s,eps) := (eps^{-4}F(eps s))^{3/2} = sum_k eps^k Lambda_k(s)`
and `y_n` is polynomial iff `ord_eps >= n-6`:

> **Master local condition.**  At each root `a` of `A` with `V0(a)=0`:
> `[s^n] Lambda_k = 0` for all `k <= n-7`.

This is a *triangular* ladder, and each `Lambda_k` is an explicit finite object:

| `k` | `Lambda_k` | degree in `s` | first weight it constrains |
|---|---|---|---|
| 0 | `Phi^{3/2}` | infinite unless `Phi` is a square | `n=7` |
| 1 | `(3/2) Psi Phi_1` | `7` (`Phi_1` has degree 5, the `F5(a)s^5` slot) | `n=8` (vacuous) |
| 2 | `(3/2) Psi Phi_2 + (3/8) Phi_1^2 / Psi` | infinite unless `Psi \| Phi_1^2` | `n=9` |

### 2.2 The `k=0` rung is exactly the D7–D9 repair, and it closes at D10

`2 n phi_0 != 0` in characteristic zero, so four consecutive zeros propagate
forever in (LQ-4).  Hence `y_7=y_8=y_9=y_10=0` forces `Phi^{3/2}` to be a
polynomial of degree `<= 6`, so `Phi^3` is a square, so `Phi = Q^2`, so by
(LQ-1)

```text
T(a) = 0   and   K(a) = 0   at every root a of C.
```

Machine-checked: `T=K=0` gives `y_7..y_13 = 0`; each of `(T,K) = (1,0),
(0,1), (1,2)` fails.  This recovers `A|T` (the producer gets it one row
earlier, at D9, by exploiting the specific `-8B^4U^3` shape — sharper, and I
confirm it).  Note `K(a)=0` is automatic after the repair, since
`K = 64AW + 4V0U0`.

### 2.3 The `k=2` rung *is* the post-D9 `W` split — and it is a resultant

After the repair, `Lambda_0 = Psi^3` (degree 6) and `Lambda_1 = (3/2)Psi Phi_1`
(degree 7) are automatically harmless for `n >= 8`.  The first live rung is

```text
[s^n] ( Phi_1^2 / Psi ) = 0   for  n >= 9.
```

`Phi_1^2/Psi` is a rational function with denominator of degree 2, so its tail
coefficients obey an order-2 linear recurrence with invertible leading
coefficient `Psi_0 = al^2`.  Two consecutive zeros therefore propagate:

> **Post-repair local successor (`LQ-W`).**  `D9 = D10 = 0` at a root `a` of
> `C` is equivalent to `Psi_a | Phi_{1,a}^2`; for squarefree `Psi_a` this is
> `Psi_a | Phi_{1,a}`, i.e.
> ```
> Res_s( Psi_a , Phi_{1,a} ) = 0.
> ```

One scalar equation per `C`-root, replacing the polynomial divisibility
`A^2 | W[-16V0W + A(64F5-U0Z)]`.  This is consistent with the charged
statement: at a `B`-root `V0 != 0` and the `-16V0W` term dominates, forcing
`B|W`; at a `C`-root both terms vanish to first order and the true condition
is second-order — exactly the "missing `C` part of `W`" the report names as the
smallest successor.  `Phi_1` is elementary to serialize: it is
`sum_{i<=4} phi_i^{(1)} s^i + F5(a) s^5`, where `phi_i^{(1)}` is the `eps^1`
coefficient of `eps^{i-4}F_i`, i.e. one derivative of already-frozen data.

**Cost.** Desk arithmetic plus a ~200-line standard-library script.  No chart
fanout, no Groebner basis, no AWS.  This is my answer to "the fastest exact
way."

### 2.4 Does the fixed endpoint mechanism transport? — the honest answer

The local model tells us *why* the two regimes differ, which no charged report
states:

> **Cascade depth is controlled by `ord_a(V0)`.**  At a root with `V0(a)=0`
> the correct Newton rescaling is `t ~ eps`, the local model is a genuine
> quartic, its square-defect is 2 numbers, and the cascade dies by D9/D10.
> At a root with `V0(a) != 0` the correct rescaling is `t ~ eps^2`, and the
> leading local data is `(al^2 + (V0/2)s)^2` — **already a perfect square, for
> free**.  All obstruction moves to higher `eps`-order.  That is exactly why
> the fixed `V0=1` fixture (where `C=1`, so there are *no* `C`-roots) survives
> all the way to D22.

**Consequence for transport: the fixed endpoint mechanism transports to the
`C=1` stratum of general `V0` and to nothing else, unmodified.**  The
`C != 1` strata die far earlier and by a different mechanism.  So the correct
general-`V0` programme is *two* compressions, not one, and the expensive one
(the `eps^2` scaling, where D10–D22 lives) has not been built.  I regard this
as the single most useful reframing available from this round's evidence.

---

## 3. Question 3 — can the failed translation shear be repaired?

**No, and I can sharpen why.  I also identify the only repair that is not
already refuted, and it is not a gauge.**

The gauge audit is correct and its counterexample is decisive: `tau_a` is an
exact symmetry of `E(F,G)` and of `t^22`, but `(tau_a P)_n = sum_k (-a)^k
P_{n-k}^{(k)}/k!` moves mass *down* in `X`-degree, and the frozen windows are
not down-closed (`F8` has `X^0..X^8`, `F9` only `X^1..X^7`; `G12` has `X^0`,
`G13` starts at `X^1`).  So the shear is a symmetry of the equation and not of
the Newton support.

Three repair routes, all assessed:

1. **Compensating target/source automorphism — refuted in shape.**  Any
   automorphism that restores the missing constants must act on the same
   `t`-graded raw space; but `t^22` and `F0=A^4` are already fixed by `tau_a`,
   so the compensator would have to be `t`-degree-preserving and `X`-degree
   raising, i.e. multiplication by a unit, which cannot create an `X^0` slot
   that the window forbids.  `NO HIT`.
2. **Enlarge the window space, then descend — this is a category change, not a
   repair.**  Enlarging to the down-closed hull is legitimate (the enlarged
   system has *more* solutions, so emptiness of the enlarged system still
   proves emptiness of the original).  But it destroys the very ranks the
   endpoint theorem uses: the charged `G18..G21` ranks `5,3,2,1` with nullity
   `0` are properties of the *narrow* windows, and `G19` explicitly "rejects
   degree 2".  A down-closed hull would give those maps kernels, and the
   `c18`/`c20` birth kills — which are literally "the window cannot store
   `A^{-3}`" — would evaporate.  So the enlargement is sound as a
   *necessary-condition relaxation* and useless as a *proof of emptiness*.
   Worth stating explicitly, since it is a tempting mistake.
3. **Prove the forbidden shear tails vanish on the solution locus — the only
   live route, and my local model makes it cheap to test.**  On the active
   component the shear parameter is `a = 3*lambda/4`.  The forbidden tails are
   specific low-`X` jets of `F9, G13, ...`.  In the `eps`-graded local model
   these jets are exactly `phi_i^{(1)}`-type data at the roots of `A`, and the
   determinant rows constrain them through `LQ-W` and its successors.  So the
   question "do the determinant equations kill every forbidden shear tail?"
   becomes a finite, root-local linear question at each rung, not a global
   raw-space theorem.  **Recommendation: test rung `k=2` first.**  If
   `Res(Psi_a, Phi_{1,a}) = 0` already forces `F9[X^0] = 0` at every root,
   the gauge is recoverable on the locus; if not, `lambda` is a genuine
   modulus and the active branch must be analysed directly, as the packet says.

Absent that theorem, I agree with the packet: **do not gauge `C=A` to
`V0=0`.**  Treat `lambda` as a real parameter.

---

## 4. Question 4 — theorem-interface composition pass

I checked each pair for an actual hypothesis-discharge, not a shared noun.

| Composition attempted | Verdict |
|---|---|
| Fixed endpoint theorem ⟶ general-`V0` endpoint | **Exact scope mismatch, now explained.**  §2.4: the fixed fixture is the `C=1` stratum; its mechanism is the `eps^2` scaling.  It says nothing about `C != 1`, which dies at D9 by a different mechanism.  The dependency audit's "conditional on the same normal form/modes/windows" is necessary but not sufficient: the *stratum* also has to match. |
| D9 repair ⟶ `q1` / D23 gate | **Real bridge, in the unexpected direction.**  §1.5: the repair does not consume `q1`, so it does not need D23.  The dependency edge that the packet draws (`q1` licensed only by D23 ⟹ general-`V0` lane is conditional) is **not** load-bearing for D7–D9 and should be cut. |
| Fixed endpoint theorem ⟶ D24/target law, raw-to-global landing | **`NO HIT`.**  Endpoint emptiness is a statement about one fibre of one branch; landing needs full-configuration coverage (`G2-PSC`).  Nothing in this round moves it. |
| van Dobben `KEF` ⟶ boundary one-vertex / TD6 | **Real bridge, blocked on data, not on ideas.**  The codex audit is right that `KEF-ONE-VERTEX` is the only licensed continuation and that `ladder/SHEET6-CLASSICAL.md` §3b already predicts a `NOT-TYPED` stop because the `B`- and `x`-side resolution tails are unpinned.  So the bridge exists and the missing hypothesis is *one completed weighted graph*, which is a bounded TD6 task, not a research problem. |
| van Dobben `KEF` ⟶ avenue 7 (`A(F)`) | **Real bridge, and the strongest non-GGV composition I found.**  §5.4 of the codex audit ("target meridians and source-end meridians are different objects") is *exactly* the statement that a completed `A(F)` would discharge: `A(F)` is the target-side asymptotic curve, and its one-place component data is precisely the meridian custody `KEF` cannot supply.  Neither report makes this link. |
| HENS-CT recurrence theorem ⟶ raw GGV cascade | **Real bridge (new).**  See §6.2: `[s^n]Phi_a^{3/2}` is an order-4 P-recursive sequence, the same species the HENS-CT/fixed-receiver theorem decides.  The just-passed backend has, for the first time, a client small enough to certify. |
| Fixed endpoint theorem ⟶ Keller / JC2 | **`NO HIT`.**  Correctly firewalled by all four charged reports; I found no leak. |
| Cutoff-2 closed form (`A^5*Phi22 = X^5/40 - X/8 + gamma`) ⟶ endpoint sign | Already used as the independent sign diagnostic (`8N'=A`, synthetic `g22=N/A^5`).  **Consistent, no new bridge.** |

---

## 5. Question 5 — the four idle AWS nodes

The honest recommendation is uncomfortable: **do not fill all four.**

The current-day log records six consecutive heavy launches
(`466-prefix std/dp`, `466-prefix slimgb`, `row-RREF dp/slimgb`, `homogeneous
saturation`, `authoritative raw lp`, `LF40 std/dp`) that each returned
`RESOURCE_CAP_NO_VERDICT` after emitting only a census banner, plus a K00
`P6R4` cap and two operational aborts/stops.  Expected information gain from
another same-shape launch is approximately zero, and the packet explicitly
warns against brute-force explosion.  Meanwhile the two highest-value targets
this round are desk-scale.

Allocation, with exact stop conditions:

- **`r6a` — parameterized raw-window compiler (the real bottleneck).**  Build
  the discriminant-localized system over `K[a0,a1,a2,a3,Disc(A)^{-1}]` and
  emit *only* items 3 and 4 of the dependency audit's list: the exact
  `F4..F14`/`G4..G21` degree windows and the same-row map ranks/kernels for
  symbolic `A`, plus the absence of `G22`.  This is linear algebra over a
  localized polynomial ring, not a Groebner basis.
  **Stop:** on the first symbolic rank that differs from the frozen
  `A=X^4-1` value (that is the answer — report it), or at 6 h wall, or on any
  swap.  Do **not** attempt items 1, 2, 5 in the same job.
- **`r6d` — window-realizability search for the `LQ` constructor** (see idea
  card B).  Given local data solving the `k=0` and `k=2` rungs at every root,
  solve the *linear* raw-window system for in-window `F/G` coefficients.
  **Stop:** on the first in-window survivor past `D12` (escalate to hostile
  review immediately, do not fan out), or on a proof of linear infeasibility,
  or at 4 h.
- **`box02`, `box03` — leave idle.**  Explicit non-launch, recorded as a
  decision.  Reserve them for whatever the `r6a` window compiler proves is
  actually needed.  If the coordinator wants one job, the only one I would
  sanction is a *different-target* LF40 attempt (see §10), never a repeat
  engine/order.
- `box01` (D43) and `r6b` (LF40) already hold one saturated core each; leave
  them, with the stop conditions in §10.

---

## 6. Questions requiring novelty — new mechanism and new connection

### 6.1 New mechanism: `LQ` — the root-local Newton model

Stated in §1.1–§1.2 and §2.1–§2.3.  Summary of what is new:

1. `ord_a((F^beta)_n) >= 4*beta - n` at any root of `A` where `V0` vanishes.
2. A **uniform-in-`n` mode firewall**: mode `c_m` is shallower than the
   principal branch by exactly `m/2`.
3. The deepest-pole cascade is governed by an explicit **local quartic**
   `Phi_a = Psi_a^2 + (al T/8)s^3 + (K/64)s^4`, i.e. 5 numbers instead of 15
   polynomial slots, obeying the *same* recurrence.
4. `D7..D10 <=> Phi_a` is a perfect square `<=> T(a)=K(a)=0`.
5. The `eps`-graded successor `LQ-W`: `Res_s(Psi_a, Phi_{1,a}) = 0`.
6. **`ord_a(V0)` controls cascade depth**, which explains the `C=1` vs
   `C != 1` split and bounds what "transport" can mean.

**Comparison with repository history** (novelty check run, `0702Z` excluded):
no occurrence of "local quartic"; the one "Newton scaling" hit
(`...tail2-fullfixture-ideation-hostile-audit...`) is a `lambda^(24-3k-2n)`
grading of `W^k` *modes*, an entirely different object.  Closest prior art,
and how `LQ` differs:

- The charged report's own étale root algebra `Kbar[X]/(A)` is used to *state*
  the divisor split `C|U(K-2UV1)`; it is not used to *model the cascade*.
- The campaign's field-radical steps (`A*A'*Delta^2 = 0 mod A^2` then
  `A|Delta`) are the `k=0` rung of `LQ` at a single weight; `LQ` grades all
  weights and all `eps`-orders at once.
- Avenue 4's D-series prolongation is Puiseux depth in the *source*; `LQ` is
  `eps`-adic depth at *roots of `A` in the target row*.
- The memory-recorded "two-fibre"/`K[X]/(A)` techniques and the `V_j`
  nondegeneracy ladder are class-side; `LQ` is raw-side.

### 6.2 New connection: avenue 1 ⟷ avenue 3 (and thence 1/16)

`Phi^{3/2}` satisfies the **rigid first-order ODE** `2*Phi*y' = 3*Phi'*y`.
Avenue 3 is described in the master table as "*face valuation orders bracket
equations; strip block collapses to a rigid ODE*", scoped to "strips, `d1=1`,
depth two, `k>=2` only", with named next step "*depth-three Ore/resultant
extension*".  `LQ` is that same machine — valuation orders bracketing the
equations, collapse to a rigid ODE — applied for the first time to the **GGV
raw determinant cascade**, and its post-repair successor is *literally a
resultant* (`LQ-W`).  This is a nontrivial coupling: avenue 3 is "the
campaign's actual theorem" but has been scope-locked for weeks; avenue 1 has
been doing the same valuation bookkeeping by hand, row by row, with hundreds
of hostile checks per row.

Second-order consequence, which is the practically important one: since
`[s^n]Phi_a^{3/2}` is order-4 P-recursive in `n` with the explicit recurrence
`2n phi_0 y_n = sum_{i=1}^{4} phi_i(5i-2n) y_{n-i}`, deciding "does this
sequence vanish on a window" is precisely the finite-prefix decision the
reviewed HENS-CT/fixed-receiver recurrence theorem provides (avenues 1/16).
**The backend that just passed `UPSTREAM_PASS` now has a mathematical client
two orders of magnitude smaller than the branch-P class tower.**

### 6.3 Second new connection: avenue 7 ⟷ avenues 2/26/27 via `KEF`

Recorded in §4.  `A(F)` is the missing target-meridian object; building it
from a completed boundary book simultaneously feeds `KEF-ONE-VERTEX`
(avenue 27 / avenue 2), supplies the monodromy input for avenue 26, and
reopens avenue 6 in its repaired form.  The historical `JUMP-ONLY / TYPE-FAIL`
verdict was against `A(F)` *as a finite effective divisor on the resolved
source*; the correct object is the **image of the dicritical components in the
target**, which is a curve, not a source divisor.  That type error, not the
difficulty, is what stalled the lane.

---

## 7. Disposition vector, avenues 1–46

Convention: `unchanged` / `raise` / `lower` / `reopen`.  `G2-PSC` (global
packet/sheet transport and fidelity) and `G2-BD` (post-residue-A bounded
delay) are kept strictly distinct throughout and **neither is repriced by me**.

| # | Disposition | Reason (only for changes) |
|--:|---|---|
| **1** | **raise** | `LQ` makes the raw endpoint cascade root-local, `A`-uniform, and mode-firewalled without per-row audits; the D9 repair is `q1`-free (§1.5), removing a D23 dependency; §2.4 gives the first structural account of which strata the fixed theorem can reach. |
| **2** | **raise** (bounded) | Not for van Dobben as an obstruction — for the `KEF-ONE-VERTEX` client coupled to a built `A(F)` (§6.3).  **`G2-PSC` and `G2-BD` ranks unchanged**; the raise is on the one-vertex discriminator only, and is blocked on completing one weighted graph, which is a TD6 data task. |
| **3** | **raise** | Its own rigid-ODE / face-valuation machinery, and its own named "Ore/resultant" extension, are exactly `LQ` and `LQ-W` (§6.2).  This is the first client for avenue 3 outside strips. |
| 4 | unchanged | |
| 5 | unchanged | |
| **6** | **reopen** (conditional) | Only in the repaired form the master table itself names: "correct one-place objects are `A(F)` components".  Reopen is contingent on avenue 7 producing pinned place data; the original fibre-based version stays a closed category error. |
| **7** | **raise** | The prior `JUMP-ONLY / TYPE-FAIL` was against the wrong type (a source divisor).  The right object — the image of the dicriticals in the target — is buildable from a completed boundary book and discharges `KEF` §5.4 meridian custody (§6.3). |
| 8 | unchanged | |
| 9 | unchanged | |
| 10 | unchanged | `NO LEVERAGE` stands. |
| 11 | unchanged | Refuted; nothing this round revives it. |
| 12 | unchanged | |
| 13 | unchanged | |
| 14 | unchanged | |
| 15 | unchanged | |
| **16** | **raise** | HENS-CT `UPSTREAM_PASS` makes a real Ore/holonomic certificate emittable for the first time, and `LQ` supplies a second, far smaller holonomic client (§6.2).  Still software, not mathematics. |
| 17 | unchanged | |
| 18 | unchanged | The `Sym^2` analogue is a negative control; graded plane Keller maps remain closed by Shaska. |
| 19 | unchanged | Correctly ranked; **under-resourced** — see §8.2. |
| 20 | unchanged | |
| 21 | unchanged | |
| 22 | unchanged | |
| 23 | unchanged | |
| 24 | unchanged | |
| 25 | unchanged | Explicitly not reopened; `GATE-INV` stays rejected. |
| **26** | **raise** | Grok's best cheap untried lane finally acquires a concrete client: the branch groups in Ramanujam's Lemma 4 under `KEF` are monodromy data, so avenue 26 stops being a free-floating group-theory wish. |
| **27** | **raise** | `KEF-ONE-VERTEX` is a precise, bounded plumbing client, and van Dobben's `D_{k+2}` computation plus the tangent-`Sym^2` model (`A^1 x G_m`, determinant zero) give two calibration fixtures the lane previously lacked. |
| 28 | unchanged | BMY still `NEEDS-DATA`; the same unpinned `B`/`x` tails block it. |
| 29 | unchanged | |
| 30 | unchanged | |
| 31 | unchanged | |
| 32 | unchanged | Exact three-generator accelerator retained; still equivalent to injectivity. |
| 33 | unchanged | Not reopened; `COSTUME` stands. |
| 34 | unchanged | |
| **35** | **lower** | One more descent mechanism is now closed with a structural reason, not just a failed attempt: the `n=2` symmetric-power analogue has equal Picard classes (non-tangent) or is `A^1 x G_m` (tangent).  Both charged audits agree; the lane's remaining content shrinks. |
| 36 | unchanged | The `LQ` constructor (card B) is a *structured raw-window* search inside avenue 1, not a return to generic sparse search. |
| 37 | unchanged | |
| 38 | unchanged | |
| 39 | unchanged | Still no 10-line class. |
| 40 | unchanged | |
| 41 | unchanged | Falsified; stays so. |
| 42 | unchanged | |
| 43 | unchanged | |
| 44 | unchanged | `REFUTED-AS-PROOF`; only the repaired membership theorem retained. |
| 45 | unchanged | Not reopened. |
| 46 | unchanged | Leaf/identity layer only. |

Compact grouping of unchanged rows:
`4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28,
29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46`.
Changes: raise `1, 2, 3, 7, 16, 26, 27`; reopen `6`; lower `35`.

---

## 8. Bottleneck reranking

### 8.1 Three principal proof bottlenecks (reranked)

1. **Raw-window universality — the parameterized raw compiler.**  *Promoted
   from third to first.*  Rationale: `LQ` shows the characteristic algebra is
   already local, `A`-uniform, and cheap.  What is *not* uniform is the literal
   Newton-window data — the degree windows, the same-row ranks `5,3,2,1` with
   nullity `0`, the absence of `G22`, and the endpoint target's unit.  Every
   endpoint theorem the campaign owns is window-conditional, and the windows
   are the only thing left that is compiled at `A=X^4-1`.  This is now the
   binding constraint *and* it is attackable this week (§5, `r6a`).
2. **Cofinal total-degree / sheet ceiling, plus full-configuration landing and
   coverage (`G2-PSC`).**  *Was first, now second — not because it weakened,
   but because nothing this round touched it and nothing this round can.*  It
   remains the global wall: "always a next pair."
3. **The non-`C`-root deep cascade (`V0` a unit at the root).**  *New entry.*
   All of D10–D22's content lives here, the `eps^2` rescaling makes the leading
   local data an automatic perfect square, and there is currently **no**
   compression for it.  Whether the endpoint mechanism transports is decided
   here and nowhere else.

Demoted from the standing list: `RPMC(C)` and `L3/L5` — still required
interfaces, but no new evidence bears on them and they are not currently
rate-limiting.

### 8.2 Two principal disproof / counterexample bottlenecks

1. **There is no raw-window *constructor*.**  Every campaign "survivor" to date
   is class-level (rows 30–34 over `Q[u,v]/(uv,u^4,v^2)`), fixed-slice, or a
   single engineered point.  There is no machine that takes a survivor
   specification and emits in-window raw `F/G` coefficients.  Until there is,
   the counterexample side can only ever *fail to find* things.  `LQ` gives the
   first cheap constructor (card B) because the local conditions are low-degree
   and the window map is linear.
2. **`A(F)` has never been built.**  Avenue 7, avenue 27's realizability gap,
   avenue 28's BMY data gap, and `KEF` §5.4's meridian custody are all the same
   missing object.  This is the single highest-leverage unbuilt artifact on the
   counterexample side, and — per §6.3 — it stalled on a type error, not on
   difficulty.

---

## 9. Strongest attacks I would run next

### 9.1 Strongest proof attack — build the second scaling

Develop the `eps^2` local model at roots where `V0(a) != 0`, i.e. the analogue
of `LQ` for the fixed-fixture regime.  Concretely: with `t = eps^2 s`,
`eps^{-4}F(eps^2 s) = (al^2 + (V0/2)s)^2 + eps*(...) + ...`, and the whole
D7–D22 ladder becomes an `eps`-graded condition on the corrections to an
automatic square.  If this closes, then:

- the entire D7–D22 cascade is a **two-scale, root-local** computation,
  independent of `A`, of `V0`, and of the 513 raw rows;
- the only remaining input is the window data — collapsing bottleneck 3 into
  bottleneck 1 and making the whole endpoint programme `A`-uniform in one step;
- the general-`V0` theorem follows from the `C=1` and `C != 1` analyses
  together, without a D22 elimination.

This is the highest expected-information-per-hour item in the whole portfolio
right now, and it is a desk task.

### 9.2 Strongest falsification attack — `LQ` in reverse

Use the local conditions as a *constructor*.  At each root of `A`, the rung
conditions are: `k=0` — `T(a)=K(a)=0` (linear in the local data); `k=2` —
`Res_s(Psi_a, Phi_{1,a}) = 0` (one scalar, and *linear in `F5(a)`* since
`Phi_1` contains the free slot `F5(a)s^5`).  Choose a proper `C` (say
`deg C = 2`), solve the rungs at the `C`-roots and the corresponding `eps^2`
conditions at the `B`-roots, then solve the **linear** raw-window system for
in-window `F/G` coefficients.

Materially different outcomes:

- A survivor past `D12` in-window ⟹ the fixed endpoint mechanism does **not**
  transport, the general-`V0` lane needs redesign, and the campaign has its
  first genuine raw-window survivor object.
- Provable linear infeasibility at some rung ⟹ a general-`V0` endpoint theorem
  by pure local algebra, with no D22 elimination and no chart fanout.
- Feasible locally but window-infeasible ⟹ the windows, not the algebra, are
  doing all the work — which directly promotes bottleneck 1 and tells `r6a`
  exactly what to compile.

Every outcome is informative.  That is the property I rank on.

---

## 10. Software acceleration / decisive experiment

**Build the two-scale local root compiler.**  One standard-library Python
module (~200–300 lines, no CAS, no AWS, exact `Fraction`):

- input: `A`, `V0`, `Z`, `T`, `F4..F14` as coefficient vectors (or symbols);
- for each root of `A` (in the étale algebra `K[X]/(A)`, no splitting needed —
  work modulo the irreducible factors), choose the scaling by `ord(V0)`, emit
  `Phi`, `Psi`, `Phi_1`, `Phi_2`, ... and the rung conditions;
- output: the exact list of local conditions per weight per root, plus the
  resultants.

Why this is the right accelerator: it replaces the campaign's dominant cost
(literal 513-generator replays plus per-row nine-mode causality audits, which
have consumed 189 / 289 / 334 / 361 / 499 hostile checks per row-pair) with a
5-number-per-root model that I have already shown reproduces `g7`, `g8`, `g9`
exactly.  It is also the natural input format for the HENS-CT backend (§6.2),
giving that lane its first tractable mathematical client.

**Mandatory controls before it is trusted:** reproduce the charged `g7`, `g8`,
`N9` closed forms; reproduce the literal fixture numbers I verified in §1.3;
reproduce the fixed-fixture `D7 => A|T` and `D8 => A|(F4-V/16-Z^2/64)` on the
`eps^2` branch; and carry a wrong-sign and a dropped-mode mutation.

---

## 11. Idea cards (three)

### Card A — `LQ-LADDER`: resolve the post-D9 `W` split by resultant

- **Dependencies.**  Reduced prefix (1) [reviewed]; `D1–D6` branch condition
  `c2=0 or A|V0` [reviewed]; the D9 repair `A|T` [`PROVISIONAL`, and confirmed
  by my independent desk in §1].  **Not** dependent on `q1`, hence **not** on
  D23 (§1.5).
- **Licensed assumptions.**  Characteristic zero; `A` squarefree; field points
  only; polynomiality of `G_n` (weaker than the literal windows, so the
  conclusion covers all window solutions).
- **Cheapest decisive discriminator.**  Serialize `Phi_{1,a}` (one derivative
  of frozen data plus the free slot `F5(a)`) and evaluate
  `Res_s(Psi_a, Phi_{1,a})` at every root of `C`.  Cross-check against the
  charged condition `A^2 | W[-16V0W + A(64F5-U0Z)]` on the frozen fixture.
- **Materially different outcomes.**  (i) The resultant is identically zero on
  the stratum ⟹ the `C`-part of `W` is unobstructed and the next rung is `k=3`;
  (ii) it is a nonzero polynomial ⟹ a new exact cut, one scalar per root, and
  the `C != 1` strata shrink further; (iii) it disagrees with the charged (23)
  ⟹ one of the two is wrong and the D9 repair's promotion must wait.
- **Stop / rollback.**  Stop if my `Lambda_2` bookkeeping fails to reproduce
  (23)'s `B|W` consequence at `B`-roots; that would refute the grading, not
  the producer.  Roll back to the charged (23) and re-derive.
- **Cost.**  Desk plus ~1 h of scripting.  No AWS.  Review: one different-model
  desk, ~2 h.
- **Expected information gain.**  High.  It either supplies the smallest
  successor the packet asks for, or falsifies my compression cheaply.

### Card B — `LQ-CONSTRUCTOR`: falsify endpoint transport

- **Dependencies.**  Card A's rung conditions; the frozen raw windows
  (`deg F_n <= 16-n`, `deg G_n <= 24-n` and the literal low-degree windows);
  the linear same-row maps.
- **Licensed assumptions.**  Field points, characteristic zero, `q1` **not**
  assumed (that is the point — the constructor may leave the `q1` locus, which
  is legitimate since `q1` is a strategic restriction, not a consequence).
- **Cheapest decisive discriminator.**  Fix `A = X^4-1` and a proper
  `C` of degree 2.  Solve `T(a)=K(a)=0` at the `C`-roots, the `eps^2`
  conditions at the `B`-roots, and `Res(Psi_a, Phi_{1,a})=0`; then solve the
  linear window system for `F/G`.  Push to the first infeasible weight.
- **Materially different outcomes.**  As in §9.2 — survivor past `D12`
  (transport refuted), local infeasibility (general-`V0` theorem by local
  algebra), or window infeasibility (windows are load-bearing ⟹ promote
  bottleneck 1).
- **Stop / rollback.**  Stop immediately on the first in-window survivor past
  `D12` and enqueue hostile review before any descendant.  Stop on 4 h wall.
  Never widen the windows to force a survivor (§3, route 2).
- **Cost.**  `r6d`, ≤ 4 h, low memory (rational linear algebra).  Review: one
  different-model replay of the survivor against all 513 generators.
- **Expected information gain.**  Highest on the counterexample side, because
  every outcome discriminates.

### Card C — `AF-BUILD`: construct `A(F)` for one completed boundary book

- **Dependencies.**  One completed TD6 weighted boundary graph, including the
  currently unpinned `B`- and `x`-side resolution tails
  (`ladder/SHEET6-CLASSICAL.md` §3b); Orevkov's regularized model.
- **Licensed assumptions.**  Complex/characteristic-zero topology; **no**
  injectivity of `pi_1(M_T) -> pi_1(M_D)` (the codex audit §5.2 forbids it);
  **no** claim that `Ram union Phi^{-1}(infinity)` is the whole boundary
  (§5.3).
- **Cheapest decisive discriminator.**  Compute the images of the dicritical
  components in the target — a curve, not a source divisor.  This is the type
  repair that unblocks the old `JUMP-ONLY / TYPE-FAIL` verdict.  Then run
  exactly one `KEF-ONE-VERTEX` test on the completed graph and calibrate the
  conventions on the tangent `Sym^2` control (`A^1 x G_m`, determinant zero).
- **Materially different outcomes.**  (i) Three nonspherical branches at a
  surviving vertex ⟹ that completed book is killed by Ramanujam Lemma 4;
  (ii) the fork vanishes under ordinary minimalization ⟹ stop the lane as the
  codex audit prescribes; (iii) `A(F)` builds but the meridian map is still
  missing ⟹ record precisely which arrow is absent, which is itself the
  deliverable.
- **Stop / rollback.**  Fail closed as `NOT-TYPED` if any tail or weight is
  missing — do not infer anything from the pinned skeleton.  One graph, one
  vertex, one working day, no CAS/AWS.
- **Cost.**  Low compute; the real cost is completing the TD6 tails.
- **Expected information gain.**  Moderate but *diversifying*: it is the only
  card that does not depend on the GGV cascade being the right route.

---

## 12. Lane recommendations

| Lane | Recommendation | Basis and stop condition |
|---|---|---|
| **General-`q1` GGV** | **`REDESIGN`** | The mathematics continues; the *framing* is wrong.  Drop `q1` from the D7–D9 statement (§1.5) — it is not used and it imports a false D23 dependency.  Re-scope as "general-`V0` branch-P, two-scale local model", with `q1` retained only as a stratification convenience.  **Stop:** if the `eps^2` scaling fails to reproduce the fixed-fixture `D7 => A|T`, the whole `LQ` frame is wrong; revert to the charged row-by-row method. |
| **Raw-to-global landing** | **`CONTINUE`** | Unchanged; it is bottleneck 2 and nothing this round bears on it.  Do not divert resources to it on the strength of endpoint progress. |
| **HENS-CT** | **`CONTINUE`, with a client redesign** | `UPSTREAM_PASS` is software, correctly not evidence.  Finish the rank-one control certificate and mutation replay as charged.  **Then** point the same backend at `[s^n]Phi_a^{3/2}` (§6.2), which is order-4, one-variable, and certifiable.  **Stop:** if the control certificate cannot be independently reduced to zero in `E` by a second reducer, stop and report the adapter as non-evidence-capable. |
| **D43** | **`CONTINUE` with a hard cap** | One saturated core, 184.6 GB, long-running, and it is a genuinely different target from the capped Groebner lanes.  **Stop:** at the next telemetry checkpoint showing no new completed tail row, or on any swap, or if `MemAvailable` approaches the recorded floor.  Do not extend its budget on the strength of unrelated endpoint news. |
| **LF40** | **`REDESIGN`** | The `std/dp` cross-check capped at row zero with `completed_rows=[]`, and the printed `1` was a syntax display, not a verdict.  Repeating any engine/order is already banned.  The live `r6b` char-0 lane is cheap (9.3 GB, one core) so it may run to its cap, but a *new* LF40 attempt must change the target — a row-wise certificate or an `LQ`-style compression, not another full basis.  **Stop:** classify any further cap as `RESOURCE_CAP_NO_VERDICT` and do not relaunch the same shape a third time. |
| **Order-two / TD6** | **`REDESIGN`** | Refocus from the eight terminal classes onto *one* deliverable: complete the `B`- and `x`-side resolution tails so a full weighted boundary graph exists.  That single artifact unblocks `KEF-ONE-VERTEX` (card C), avenue 27, avenue 28's BMY data gap, and avenue 26.  **Stop:** if the tails cannot be pinned, record `NOT-TYPED` and stop the `KEF` lane rather than testing a skeleton. |
| **Artin–Schreier / char-`p` / Witt (AS109)** | **`CONTINUE` at low resource** | The bounded partial-degree frontier at maximum twelve is a real, finite target and the lane is the campaign's only live counterexample-side mechanism.  It is under-resourced (see §8.2 discussion) but should not displace the desk work above.  **Stop:** on any claim of an all-Witt-to-polynomial inference — that inference is not available. |
| **External intelligence** | **`CONTINUE` at current cadence** | The 05:24Z sweep is sound: no external JC2 resolution; Matysiak `REFUTED-ON-AUDIT`; van Dobben correctly demoted to a secondary filter with the plane analogue closed negatively.  No cadence change warranted. |

---

## 13. One likely-missed insight

> **The D9 repair is `q1`-free, and therefore is not downstream of D23.**

Every charged artifact this round — the producer report, the `PROGRESS` digest,
the `notes.md` live state, and the `APPROACHES` overlay — frames the general-`V0`
work as living on "the q1-compatible locus", and the packet repeats twice that
"q1 is strategically licensed only when the later D23 theorem is included;
D1--D22 do not imply it."  That framing quietly makes the campaign's newest
result conditional on an unproved gate.

It is not.  The implication `D1=...=D9=0 => A|T` consumes only the reduced
prefix, the `D1–D6` branch condition, and the divisor split `C=gcd(A,V0)`.
`q1` appears only in the *stratification bookkeeping*: `gcd(A,V0)=gcd(A,R0)`,
the identification of the active component as `R0=lambda A`, and `deg R0<=4`.
My independent derivation (§1.1–§1.2) never mentions `R0` and reproduces all
three leading classes exactly.  Since `q1` cuts the admissible `V0` space from
dimension 8 to dimension 5, dropping it is a strict strengthening — a
**60%-larger** theorem, obtained by deleting a hypothesis rather than proving
anything new.

**Cheapest test (minutes, desk).**  Take the frozen checker's fixture and
replace `V0` by a polynomial of degree ≤ 7 that is *not* in the image of
`R0 |-> A'R0 + 2AR0'` — for instance `V0 = X^5` with `A=X^4-1` — recompute
`Z, T, F4` to satisfy `D0..D6`, and verify that the D7, D8, D9 closed forms
(4), (5), (17)/(18) still hold verbatim.  If they do, cut the `q1`/D23
dependency edge in `notes.md` and `APPROACHES.md`.  If any of them silently
uses `R0`, that is itself an important custody finding.

---

## 14. Epistemic ledger

### 14.1 Proved / promoted facts I relied on

- Characteristic-zero field-valued emptiness of the complete fixed
  `A=X^4-1, V0=1` upper branch-P endpoint fixture (Grok46 289/289; two
  independent Sol replays).  Consumed as **promoted**, used only for context
  and the §2.4 reframing, never as an input to my own derivations.
- The reviewed `D1–D6` branch-P parametrization and its branch condition
  `c2=0 or A|V0`.  Consumed as **promoted**; load-bearing for my §1.4 coverage.
- The reduced prefix normal form (1).  Consumed as **promoted**; load-bearing
  for everything in §1–§2.
- The `A`-dependency audit's conclusion that the formal D7–D22 cascade needs
  only a nonconstant squarefree quartic `A`.  Consumed as **promoted**;
  independently corroborated by `LQ`, which is manifestly `A`-free.

### 14.2 Provisional inputs

- The D9 repair `D1..D9 => A|T` (`PROVISIONAL`, awaiting different-model
  hostile replay).  I did not assume it; I re-derived it.  My §1 verdict is a
  second desk, **not** a promotion, and does not substitute for the mandated
  hostile review.
- The exact D7/D8 formulas (4)/(5) and the D9 numerator (17)/(18).  I verified
  the two highest-index terms of (17) by hand from the binomial expansion
  (`F6`: `+6144 A^5 F6 T`; `F5`: `+768 A^3 F5(AK-4TV0)`), verified that the
  naive `F7` pole cancels identically, and verified (18) numerically on the
  fixture.  I did **not** verify all twelve terms of (17).
- `HENS-CT UPSTREAM_PASS` (packet §2.4).  Consumed as *software* status only;
  the R0 report I read predates it and says `TOOL-INTERFACE FAILURE`.

### 14.3 My own claims, by tier

| Claim | Tier | Status |
|---|---|---|
| (LQ-1) `Phi = Psi^2 + (alT/8)s^3 + (K/64)s^4` | `EXACT` | proved by direct expansion; machine-consistent |
| (LQ-2) `ord_a((F^beta)_n) >= 4 beta - n` at `V0`-vanishing roots | `EXACT` | proved (3 lines, §1.1) |
| (LQ-3) mode `c_m` shallower by `m/2`, uniformly in `n` | `EXACT` | corollary of (LQ-2) |
| (LQ-4) local order-4 recurrence = campaign recurrence with 5 slots | `EXACT` | proved from `2 Phi y' = 3 Phi' y` |
| `g7, g8, g9` leading classes reproduce the charged forms | `EXACT` | machine-checked, `/tmp/opus5_quartic.py` |
| Fixture literals (`2+4X+6X^2`; `-6B`; `25+23X+...-2X^6`; `-2048`) | `EXACT` | machine-checked, `/tmp/opus5_local_check.py` |
| `D7..D10 <=> Phi_a` a perfect square `<=> T(a)=K(a)=0` | `EXACT` | proved + machine-checked |
| The D9 repair is `q1`-free | `EXACT` (argument), **unverified against the frozen checker source** | I inspected only the report's prose; I did not read the checker |
| `LQ-W`: `Res_s(Psi_a, Phi_{1,a})=0` is the `k=2` rung | `PROVISIONAL` | derivation sketched; `Phi_1` not serialized; **not** cross-checked against (23) |
| §2.4 "`ord_a(V0)` controls cascade depth" | `PROVISIONAL` | the `eps^2` branch is asserted from the rescaling, not computed |

### 14.4 Conjectures (labelled, not used)

- That the `eps^2` scaling closes the non-`C`-root cascade (§9.1).
- That `KEF` holds for hypothetical nonproper Keller maps (the codex audit's
  own framing; I add nothing to its truth).
- That a `q1`-free general-`V0` endpoint theorem exists.

### 14.5 Failed attempts and dead ends of my own

- I initially expected an `F7`-dependent pole in `g9` and thought (17) was
  missing a term.  It is not: the `u^2` and `u^3` contributions cancel exactly
  (`+3/16` and `-3/16` times `F7 V0^2/A^2`).  This was my own error, corrected
  before it entered any conclusion; it is recorded because it is a good
  regression test for any successor compiler.
- I first stated "`Lambda_0` polynomial of degree ≤ 6" as if a single row
  forced it.  It does not — it needs four consecutive rows (D7–D10).  Corrected
  in §2.2.
- I attempted to extend (LQ-2) to roots where `V0(a) != 0` and it fails there
  (the bound degrades to `4beta - 2n`, which is useless).  That failure is
  informative and became §2.4 and bottleneck 3.

### 14.6 Hidden assumptions I am making explicit

- I work at *field points* only; nothing here is scheme-theoretic.
- I use polynomiality of `G_n`, which is weaker than the literal windows.  My
  conclusions therefore cover every window solution, but they cannot reproduce
  the fixed fixture's `c18`/`c20` kills, which are genuinely window facts.
- `A` squarefree is load-bearing in (LQ-2) via `ord_a(A)=1`.
- Characteristic zero is load-bearing twice: `2 n phi_0 != 0` in the recurrence,
  and the binomial series for `F^beta`.
- I assume the charged reports' transcription of the raw determinant convention
  `D_n = sum_{i+j=n}((12-j)F_i'G_j + (i-8)F_i G_j')`; I did not re-derive it
  from the source JSON.

### 14.7 Checks run

25/25 custody hashes; `git rev-parse HEAD`; two `/tmp` `Fraction`-only scripts
(exact polynomial division and remainder for D7/D8, exact `P9` factorization
and root evaluation, the local recurrence at four random rational parameter
sets plus three constrained sets plus four `(T,K)` corner cases); hand
expansion of the `F5`, `F6`, `F7` and `T^3` contributions to `y_9`; a
repository novelty sweep (with the disclosed contamination).

### 14.8 Failed checks

None failed.  Not attempted, and therefore not claimed: the 513-generator raw
reconstruction; the `G18..G21` window ranks; the endpoint sign convention; any
verification of the frozen checker *source* as opposed to the report prose;
`Phi_1` serialization; any cross-check of `LQ-W` against equation (23).

### 14.9 Exact scope

Nothing here proves or disproves JC2, a Keller-pair theorem, any GGV family
exclusion, scheme-theoretic emptiness, a landing or coverage theorem, a
degree ceiling, or a counterexample.  My §1 verdict `CONFIRMED` applies to the
charged D9-repair *implication at characteristic-zero field points*, on the
divisor endpoints enumerated in §1.4, with the documentation `GAP` of §1.6
outstanding.  My `LQ` mechanism is `EXACT` where §14.3 says `EXACT` and
`PROVISIONAL` where it says `PROVISIONAL`.  This report is one blind lane's
opinion; it is not review, and it promotes nothing.

