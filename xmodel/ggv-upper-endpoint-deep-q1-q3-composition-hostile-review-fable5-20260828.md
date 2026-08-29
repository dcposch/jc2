# Hostile review: deep upper endpoint licensed q1/q3 composition

Date: 2026-08-28  
Reviewer: Fable 5 (independent different-model audit)  
Verdict: **REPAIR** — every displayed mathematical identity, (1)–(5) and
(8)–(14), is CONFIRMED by full symbolic recomputation; two wording/scope
defects require repair (normalization of the primitive, and an unjustified
localization in (11)), plus one hypothesis-completeness note.  No conclusion
of the target changes under the repairs.

## 1. Target and frozen inputs

Primary target (read in full, byte-frozen):

| file | sha256 |
|---|---|
| `xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md` | `6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715` |

Reviewed upstream atoms consumed (pinned, matching the coordinator's
frozen hashes):

| file | sha256 |
|---|---|
| `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828.md` | `042dbacdd4d7fe6e014ccfb7d82d030e633e4a1291a313b9d022d1b78e4e36a8` |
| its checker | `505cfd93279ffe8189d25a681b8490ba71edbc5567bc5eecea70e0e2bfc52796` |
| `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md` | `9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1` |
| `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md` | `7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29` |
| `xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md` | `46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1` |

The same-model downstream addendum
`ggv-upper-endpoint-deep-q1-composition-addendum-r1-sol-ultra-20260828.md`
was deliberately **not read**; this is an independent check of the frozen
coordinator target only.  Per standing custody policy, `jc2-lean` was not
entered.  All algebra below was redone by hand and re-verified by a
self-contained standard-library checker (no producer checker imported):

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828-check.py
```

Result: `ALL 32 CHECKS PASS` (24 direct confirmations, 6 mutation
detections, squarefree and D12 load-bearing controls).

## 2. Item-by-item audit

### (1) Licensing firewall — CONFIRMED

R7R1 (frozen producer, "for a truncated target `E=t^22+O(t^N)`, the
licensed rows are exactly `q_n` with `n+22<N`") gives, on the exact
successor normalization `D22=1`:

- `q1` needs `1+22<N`, i.e. `N>=24`, i.e. `D23=0`;
- `q3` needs `3+22<N`, i.e. `N>=26`, i.e. `D23=D24=D25=0`.

The target's §1/§2 statements match exactly, and its statement that
nothing is licensed by `D0..D22` alone matches R7R1's "modulo `t^23` only
`q_0` is licensed."  The full hypothesis, stated exactly: **either** the
exact Keller identity `12F_XG-8FG_X-t(F_XG_t-F_tG_X)=t^22` holds
identically (equivalently `[f,g]=1` for the typed pair), which licenses
every row, **or**, at the finite level, the truncated identity holds
through the row one past the gate being used.  D5G-style freezes of
`D0..D22` alone license no q-gate used here.  CONFIRMED as written.

### (2) q1 parametrization — CONFIRMED, with the exact T_A bridge

The reviewed convention (active-c2 review, frozen: `V0=A'R0+2AR0'`,
`deg R0<=4`) plus deep `A|V0`: `A|A'R0`; `gcd(A,A')=1` by squarefreeness;
so `A|R0`; `deg R0<=4=deg A` and `A` monic force `R0=lambda*A` with
`lambda` a base-field scalar.  Then `V0=A'(lambda A)+2A(lambda A)'
=3lambda*A*A'` and `S=V0/A=3lambda*A'` (exact division, checker S8a/S8b).
Kernel check: on `A=X^4-1` the solution space of `A | A'R0` in degree
`<=4` is exactly 1-dimensional, spanned by `A`; on the non-squarefree
control `A=X^4` it is 4-dimensional (S8d) — squarefreeness is
load-bearing, exactly as the target's §2 says.

Bridge to the reviewed `T_A` q1 theorem (`T_A(Q)=2AQ'-3A'Q`,
`F1 in im(T_A)` on `K[X]_(<=12)`): the two conventions are literally
conjugate,

```text
F1 = A^2 V0 = T_A(A^2 R0),
```

verified symbolically (S8c); the window `deg R0<=4` corresponds to the
reviewed `T_A`-domain window `deg(A^2 R0)<=12`.  So the target consumes
precisely the reviewed q1 theorem, in its odd-primitive normal form
(primitive `p*R0/2` for `q1 = p*V0/(4A)`).

### (3) q3 coefficient — CONFIRMED (independent extraction)

Independently of the producer, `Q=P^2`, `P=F^(1/8)`, `s=t/P` is a
Lagrange-inversion setup: `t=sP(t)` with `phi=P`, so for `n>=1`

```text
[s^n]Q = (1/n)[t^(n-1)] (F^(1/4))' F^(n/8) = 2/(n+2) [t^n] F^((n+2)/8),
```

which is the target's (10).  I verified this by direct exact series
inversion for `n=1,2,3` with symbolic `F1,F2,F3` (checker S1a/S1b),
matching R7R1's frozen `q1,q2` closed forms on the way.  Binomial
extraction of `2/5 [t^3] F^(5/8)` with `F=F0(1+u)`, `F0=H^2=p^8`:

```text
(2/5)(5/8) = 1/4,   (2/5)*2*binom(5/8,2) = -3/32,
(2/5)*binom(5/8,3) = 11/512,
```

confirming every coefficient of the displayed (8); mutations `11/512 ->
12/512` and `-3/32 -> -1/8` are both detected (S2b/S2c).  Substituting the
reviewed reduced prefix (6) gives the exact polynomial identity

```text
128 F3 A^8 - 48 F1 F2 A^4 + 11 F1^3 = A^9 (16AU + 4SZ - S^3)
```

(S3a), i.e. `q3 = p(16AU+4SZ-S^3)/(512A)`, and `2Z=S^2-AQ` turns the
numerator into `N=S^3+A(16U-2SQ)` (S3b), so `q3=N/(512p)`.  (9) CONFIRMED.

**Sheet twist, sharpened.**  On either sheet `p^2=eps*A` (`eps=+-1`),
`p^5=p(p^2)^2=p*A^2` and `p'=eps*A'/(2p)=(A'/(2A))p`; hence
`q3=(N/(512A))*p` — the *same* expression in the odd basis element `p` on
both sheets, and the odd-primitive criterion reduces to the *identical*
rational ODE (11) on both sheets (S4).  So the target's claim that the
other sheet changes "only an irrelevant nonzero scalar/sign" is correct
and in fact conservative: written as an element of `K(X)(p)`, `q3` flips
sign as `N/(512p) -> -N/(512p)`, but the reduced polynomial criterion and
all downstream formulas are literally sheet-independent.  Harmless.

### (4) Exactness ODE — CONFIRMED as an equation; normalization REPAIR (D1)

General primitive `W=w0+w1*p in K(X)(p)`: since `d/dX` preserves the
even/odd decomposition (`(w1 p)' = (w1' + w1 A'/(2A))p`), the odd element
`q3` is exact iff it has an odd primitive `w1*p`, `w1 in K(X)`.  Writing
`w1=C/256` gives exactly

```text
(pC/256)' = (2AC'+A'C)/(512p),
```

so `q3=N/(512p)` is exact iff a rational `C` solves `2AC'+A'C=N` — the
displayed (11) is the correct equation (S5a).

**Defect D1 (normalization wording; REPAIR).**  The target's wording
"Writing that primitive as `p*c/512` and rescaling `C=256c`" is
inconsistent with (11): a primitive `p*c/512` satisfies `2Ac'+A'c=2N`, and
`C=256c` then satisfies `2AC'+A'C=512N`, off by a factor of exactly 512
(mutation S5b).  Clean corrected statement: *the primitive is `pC/256`*
(equivalently: write the primitive as `p*c/512` and rescale `C=c/2`).
Impact: none on (3)–(5) or any downstream formula — all displayed
equations (11)–(14) are internally consistent with each other and with
`q3=N/(512p)`; only the connecting sentence misnames the scaling, and
scaling `C` by any fixed nonzero constant rescales `N`-side data
uniformly without affecting existence, pole, or degree arguments.
Classification: normalization repair, presentation-only.

### (5) Polynomiality and degrees — CONFIRMED, with localization gap (D2)

**Defect D2 (unjustified localization; REPAIR).**  (11) asserts
`C in K[X,1/A]` a priori.  The correct starting point is `C in K(X)` (a
rational primitive's odd part need not lie in the localization), and the
target's pole argument, as written, only treats roots of `A`.  The missing
half-line: at `beta` with `A(beta)!=0`, a pole of order `m>=1` in `C`
makes `2AC'` have a pole of order `m+1` with leading coefficient
`-2m*A(beta)*c_(-m) != 0`, unmatched by anything (`A'C` has order `<=m`),
contradicting polynomial `N`.  Verified exactly for `m=1,2,3` (S6a).  So
there are no poles away from `A`, *then* the target's argument applies.
Impact: none after the one-line repair.

At a simple root `alpha` of `A` (all roots simple by squarefreeness),
`2AC'+A'C` applied to `C=(X-alpha)^(-m)` equals
`[-2mA+A'(X-alpha)](X-alpha)^(-m-1)`; the bracket vanishes at `alpha` to
first order with derivative `(1-2m)A'(alpha)`, so the pole order is
exactly `m` with leading coefficient `(1-2m)A'(alpha) != 0` for every
integer `m>=1` — integral orders are the only ones a rational `C` can
have.  Verified for `m=1,2,3` on `A=X^4-1` (S6a).  Load-bearing control:
for non-squarefree `A=X^4`, `C=1/X` solves the ODE with polynomial right
side `2X^2` (S6b) — genuinely rational solutions exist, so squarefreeness
cannot be dropped.  Hence `C` is a polynomial.

Degrees.  Raw windows (frozen in the active-c2 review: `deg F_n<=16-n`,
`deg F0=16`): `deg F1<=15 => deg V0<=7 => deg S<=3` (also direct from
`S=3lambda*A'`); `deg F2<=14 => deg Z<=6`; `deg F3<=13 => deg T<=9 =>
deg U<=5`; `S^2-2Z=AQ => deg Q<=2`.  Then `deg S^3<=9`,
`deg A*16U<=9`, `deg 2ASQ<=9`, so `deg N<=9` (S7a).  For `deg C=d`, the
leading coefficient of `2AC'+A'C` is `(2d+4)lc(C)` on `X^(d+3)`
(verified for `d=0..6`, S7b), nonzero in characteristic zero since
`2d+4>0`; so `d+3<=9` gives `deg C<=6`.  All CONFIRMED.  Note the target
states `deg N<=9` bare; the window provenance above should be cited, but
this is documentation, not a defect.

### (6) C-structure and (13) — CONFIRMED symbolically

With `S=3lambda*A'`: `N = S^3 mod A`, so (11) mod `A` gives
`A'C = 27lambda^3(A')^3 mod A`; `A'` is a unit mod squarefree `A`, so
`C = 27lambda^3(A')^2 mod A`; both sides have degree `<=6` and the
difference is `A*r` with `deg r<=2` — (12) CONFIRMED (S9, exact division).
Substituting (12) into (11) and cancelling `S^3`, the identity

```text
2AC'+A'C = S^3 + A(16U-2SQ)   with   16U = 2SQ+108lambda^3 A'A''+3A'r+2Ar'
```

holds *identically* in all eleven free parameters
(`a0..a3, lambda, q0..q2, r0..r2`) — (13) CONFIRMED coefficientwise (S10).

### (7) D12 composition — CONFIRMED

Consumed input, pinned to the reviewed active-c2 atom only: on exact
`D=0`, `c2!=0`: `A | L`, `L=QS+4U` (that review's §5, "on exact `D=0`:
`A|E`, `A|L`"; constants used there: 3, 5, `c2`).  Reducing (13) mod `A`
with `4U=-QS mod A`: the checker finds the *exact* polynomial
factorization (stronger than a mod-`A` congruence)

```text
-4QS-(2SQ+108lambda^3 A'A''+3A'r) = -3A'(r+6lambda*Q+36lambda^3 A''),
```

(S11a), so `A | A'(r+6lambda*Q+36lambda^3 A'')`; `gcd(A,A')=1` gives
`A | (r+6lambda*Q+36lambda^3 A'')`; and `deg(r+6lambda*Q+36lambda^3 A'')
<= 2 < 4 = deg A` (S11b) forces the polynomial identity (14),
`r=-6lambda*Q-36lambda^3 A''`.  Back-substitution gives exactly

```text
U = -(3lambda/4)(A'Q+AQ') - (9lambda^3/2) A A''',
L = -3lambda A (Q'+6lambda^2 A'''),
```

verified symbolically, including exact divisibility `A|L` with quotient
`-3lambda(Q'+6lambda^2 A''')` (S11c–e).  (3), (4) CONFIRMED.

### (8) lambda=0 and the U-controls — CONFIRMED

`lambda=0` gives `S=3*0*A'=0` and (3) gives `U=0` (S12a); (5) CONFIRMED.
Alternate double-divisibility route, audited and verified (S12b): at
`lambda=0`, `N=16AU`; D12 gives `A|4U`, so `U=A*u`, `deg u<=1`; the ODE
mod `A` gives `A|A'C`, hence `C=A*rt`, `deg rt<=2`; substituting and
cancelling one `A`: `3A'rt+2A*rt' = 16A*u`, so `A|3A'rt`, so `A|rt`, so
`rt=0`, so `u=0`, so `U=0`.  Function spaces: `rt` in degree `<=2` (from
`deg C<=6`), `u` in degree `<=1` (from `deg U<=5`); only the constants 3
and 16 are inverted (characteristic zero).  The 5-unknown linear system
has full rank on two squarefree samples.

**Control (q3 alone does not force `U=0`).**  At `lambda=0` take
`U=48A'`, `C=256A` (primitive `pA` in the corrected normalization, i.e.
`c=512A` in target `c`-units): `2AC'+A'C = 768AA' = 16A*U = N` holds
identically (S13a), so the q3 gate passes with `U != 0`; but the D12
residue `(QS+4U) mod A = 192A'` is nonzero mod squarefree `A` (S13b).  So
the D12 input `A|(QS+4U)` is genuinely load-bearing, and its omission is
a detected mutation (S13c: with `r` unresolved, (3) fails).

### (9) Scope — CONFIRMED as stated

The target's firewall is accurate and complete on its own terms:
characteristic-zero field, stable under base-field extension; the sheet
choice `p^2=+-A` is a harmless radical extension (and by §2(3) above the
reduced criterion is even sheet-independent); everything is asserted only
on the exact-`D=0`, `c2!=0` successor, with the other `D`-valuation
branches and the `c2=0` companion explicitly excluded (matching the
reviewed refutation that mere `A|D` leaves a `D*B11/A^2` pole); the
result is field/radical algebra, not nonreduced scheme membership.  No
promotion to scheme membership, branch emptiness, endpoint exclusion,
q5–q13 compatibility, Keller theorem, or JC2 occurs anywhere in the
target, and §6's roadmap is explicitly non-claiming.  (Spot-check: on
`lambda=0`, `F1=A^3S=0` and `F3=A(SZ+AU)/8=0`, and then `(10)` gives
`q5=(2/7)(7/8)p^7F5/H^2=F5/(4p)` since `F1=F3=0` kills all `t^5`
cross-terms — the §6 formula is consistent; its `A|P1, A|F7, F5=A^2r5/256`
inputs cite an external Newton theorem not audited here and are consumed
by nothing in §1–§5.)

## 3. Defect register

| id | defect | classification | impact |
|---|---|---|---|
| D1 | "primitive `p*c/512`, rescaling `C=256c`" is inconsistent with ODE (11) by a factor of exactly 512; correct: primitive `pC/256` (equivalently `C=c/2`) | normalization REPAIR | none — (11)–(14), (3)–(5) mutually consistent; wording only |
| D2 | (11) asserts `C in K[X,1/A]` without excluding poles away from `A`; needs the `-2m*A(beta)` half-line before the `(1-2m)A'(alpha)` step | localization gap, REPAIR | none after one-line repair |
| D3 | §1 names only `A|V0` as the deep condition, but the displayed prefix (6) (and the consumed D12 atom) also uses `A|T` (`T=AU`, `F3=A(SZ+AU)/8`) | hypothesis-completeness note | none — hypothesis is embedded in the displayed prefix; should be named |

No mathematical identity in the target failed.  Verdict: **REPAIR**
(CONFIRMED with the above repairs).

## 4. Execution and artifacts

Checker rerun (exact command and full output frozen in the case
directory):

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828-check.py
```

Output tail: `OVERALL: ALL 32 CHECKS PASS (6 mutations detected;
squarefree and D12 load-bearing controls held)`.

Case directory:
`cases/ggv_8_28_upper_endpoint_deep_q1_q3_composition_hostile_review_fable5_20260828/`
(README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256; manifests are
repo-root-relative and non-self-referential; every frozen input byte
preserved).
