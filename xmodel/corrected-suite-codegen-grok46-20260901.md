# CORRECTED-SUITE-CODEGEN — faithful characteristic ideals as runnable jobs

Lane: `CORRECTED-SUITE-CODEGEN`. Date: 2026-09-01. Agent: grok-4.6.

Status: SEALED — jobs emitted; three self-checks PASS; no Groebner run.

## 0. Custody, hashes, method

Charged frozen copies were hashed with `shasum -a 256` before they were read. Both match the charge exactly:

```text
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.g8GxQ4/inputs/encoding-faithfulness-audit-r2-sol56-20260901.md
c4ee11caa6e5b37e1c7b3a3089709b98d3e07612eee2913418c183195d756c7f
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.g8GxQ4/inputs/moh-check-863-grok46-20260901.md
```

Workspace copies of the same bytes (identically hashed) are used below for readable paths. This lane transcribes the audit's Section 7.1 incidence systems into msolve GROBNER-mode inputs and Macaulay2 mirrors. It does not run msolve or M2 Groebner bases. Coefficient polynomials and the three required self-checks are exact sympy expansions / substitutions (desk-scale). Canonical ledgers and `jc2-lean` were not inspected. No exit-price claim is made.

msolve input discipline, locked to campaign hazards: first line is the variable list (no in-band comment before it: that parses as one variable); characteristic `0`; expanded monomial sums; no parentheses; one occurrence of each monomial; last generator has no trailing comma; POSIX text with one trailing newline. GROBNER-mode convention, written in every M2 header and restated here because it cannot appear as an in-band `.ms` comment without breaking the parser: **output `basis=[1]` means the unit ideal means EMPTY**.

M2 footguns observed: `diff(var, poly)` argument order; `first degree`; no `pi` as a variable (`Pi` if the double-point scheme is built); name a ring map before applying it; close stdin with `exit 0`.

## 1. File inventory and priority

Five types, ten job files, under `box/`. M2 is authoritative (constructs `G86`/`G96` in the polynomial ring and extracts `[t^j]`). Each `.ms` file is the expanded unique-monomial list of those same coefficients plus the Rabinowitsch open. GROBNER-mode: `basis=[1]` means unit ideal means EMPTY.

| priority | file stem | `Delta` | audit job | closed `g_j` | open | `.ms` gens | archival |
|---|---|---|---|---|---|---:|---|
| P1 | `corrected_863` | `(8,6,3)` | D / corrected `I_29` | `g_22..g_4` | `u g_3-1` | 20 | no |
| P2 | `corrected_869` | `(8,6,9)` | B | `g_22..g_10` | `u g_9-1` | 14 | no |
| P3 | `corrected_964` | `(9,6,4)` | 96A + six-node | `g_16..g_5` | `u g_4-1` | 13 | no |
| P4 | `corrected_8611` | `(8,6,11)` | A | `g_22..g_12` | `u g_11-1` | 12 | **yes** |
| P4 | `corrected_867` | `(8,6,7)` | C | `g_22..g_8` | `u g_7-1` | 16 | **yes** |

`(9,6,2)` is REALIZED (audit §6) and is not a job; it is self-check (ii) only. P4 files carry an `ARCHIVAL / LOWEST PRIORITY` header: rep-level dead, do not consume P1–P3 AWS time.

msolve variable order (grevlex, first listed largest): auxiliaries, then the eleven chart coefficients, then `u`. Cover colon and `Res(p',q')` are M2-side only, as in MSOLVE-PREP: extra slack variables would turn a 0-dimensional coefficient point positive-dimensional.

## 2. Census: `delta_aff=6` for `(9,6,4)`

Audit §3 conversions, recomputed here from the displayed formulae (not from a prior validator):

```text
(8,6): beta_1 = 32-c,  delta_inf = (beta_1-1)/2,  p_a(8)=21,  delta_aff = 21 - delta_inf
(9,6): beta_1 = 27-c,  delta_inf = beta_1-1,      p_a(9)=28,  delta_aff = 28 - delta_inf
```

| `Delta` | `beta_1` | `delta_inf` | `delta_aff` | audit 7.1 `N` |
|---|---:|---:|---:|---:|
| `(8,6,11)` | 21 | 10 | 11 | 11 |
| `(8,6,9)` | 23 | 11 | 10 | 10 |
| `(8,6,7)` | 25 | 12 | 9 | 9 |
| `(8,6,3)` | 29 | 14 | 7 | 7 |
| `(9,6,4)` | 23 | 22 | **6** | **6** |
| `(9,6,2)` | 25 | 24 | 4 | 4 |

For `(9,6,4)`: `beta_1=27-4=23`, `delta_inf=22`, `delta_aff=28-22=6`. This matches the audit table `N=11,10,9,7,6,4`, the NR gap count of `⟨4,6,9⟩` (six gaps), and the HF-twin `Δ_aff=6`. Encoded as `idpPostcheck(p0,q0,6)` in `corrected_964.m2`.

Moh-check coefficient count (raw `I_29`): after the NR chart, nine coefficients remain and ten odd vanishings `h_23..h_5` are imposed, `h_23` already spent. That is the unfaithful raw job. The corrected D job below is the same FSY/Moh finite system after even pole-order reduction, including gap residuals at degrees 10 and 4.

## 3. Encoding dictionary (audit 7.1, not raw `h_k`/`k_j`)

Shared charts, identical to the audit §2 and MSOLVE-PREP 2.1–2.2 (`gam` for `γ`):

```text
p = t^8 + B t^5 + C t^4 + D t^3 + E t^2 + F t + G
q = t^6 + b t^4 + gam t^3 + d t^2 + e t + f
G86 = p^3-q^4 + a22 p^2 q + a20 p q^2 + a18 q^3 + a16 p^2 + a14 p q + a12 q^2 [+ a8 p] [+ a6 q]

p = t^9 + A t^7 + P6 t^6 + B t^5 + P4 t^4 + C t^3 + P2 t^2 + D t
q = t^6 + a t^4 + Q3 t^3 + b t^2 + Q1 t
G96 = p^2-q^3 + a15 p q + a12 q^2 + a9 p + a6 q
```

Subscripts on `a_w` are leading pole degrees. Retain only terms of weight strictly greater than the target `c`. Closed equations are **every** `[t^j]G = 0` in the stated range, not the raw odd list. The even/semigroup slots are triangular of leading coefficient 1 in their own `a_w` (sympy: `g_22,g_20,g_18,g_16,g_14,g_12,g_8,g_6` and `g_15,g_12,g_9,g_6`). After eliminating those auxiliaries one recovers the audit §3 `bar_h`/`bar_k` list. Independent equation counts in the eleven chart variables: `5,7,8,11,8,10` for A,B,C,D,96A,96B, matching audit 7.1.

No `_a`/`_b` variants: the audit's incidence specification is unambiguous. The one encoding *choice* that is not an equation ambiguity is recorded in §6 (I_DP is a post-check, not extra Groebner generators).

## 4. Coefficient-by-coefficient: `(8,6)` reduced remainders

Exact sympy expansion of `H=p^3-q^4` and of `G86` in the full auxiliary ring. Support of both is `0..22`; `h_23=g_23=0` (chart identity, `h_23=-4 a_5` already spent). Leading coefficients, fully expanded:

```text
h_22 = -4*b
g_22 = a22 - 4*b
h_21 = 3*B - 4*gam
g_21 = 3*B - 4*gam
h_20 = 3*C - 6*b^2 - 4*d
g_20 = a20 + a22*b + 3*C - 6*b^2 - 4*d
h_19 = 3*D - 12*b*gam - 4*e
g_19 = 2*B*a22 + a22*gam + 3*D - 12*b*gam - 4*e
```

These are the encoded generators: `corrected_863.ms` / `8611.ms` / `869.ms` / `867.ms` all begin `a22-4*b` then `3*B-4*gam` then `a22*b+a20+3*C-6*b^2-4*d` then `2*a22*B+a22*gam+3*D-12*b*gam-4*e`. That is `g_22,g_21,g_20,g_19`, not raw `h_21,h_19,...`.

Triangular reduction on `g_22=0` forces `a22=4b`. Substituting:

```text
g_19 | (a22=4b) = 8*B*b + 3*D - 8*b*gam - 4*e
                = h_19 + 4*b*(2*B+gam)
```

This is the audit §3 identity `bar_h_19 = h_19 + 4*b*(2*B+gamma)` on the nose. So `h_19=0` is not an off-by-one of the right equation: it is the unreduced coefficient. The encoded `g_19=0` *is* the reduced remainder.

Generator layout in each `(8,6)` `.ms` file (line 1 = variables, line 2 = `0`):

| file | lines 3.. last-but-one | last line |
|---|---|---|
| `corrected_8611.ms` | `g_22..g_12` (11 closed) | `u*g_11-1` |
| `corrected_869.ms` | `g_22..g_10` (13 closed; includes gap `g_10`, no `a10`) | `u*g_9-1` |
| `corrected_867.ms` | `g_22..g_8` (15 closed; `a8` retained) | `u*g_7-1` |
| `corrected_863.ms` | `g_22..g_4` (19 closed; `a8,a6` retained; gap `g_4`, no `a4`) | `u*g_3-1` |

Auxiliaries retained, matching the 7.1 table: A/B keep `a22..a12`; C adds `a8`; D adds `a6`. Degrees 10 and 4 are gaps of `⟨8,6⟩` and appear as closed residuals without an auxiliary, which is why B's closed range reaches `g_10` with the same auxiliaries as A, and D's range reaches `g_4`.

Lower `g_j` are the fully expanded unique-monomial polynomials in the `.ms` files (hashed in §8). They are not raw `h_j`: each contains the `a_w` monomials of pole degree `w` that reduce that slot. Independent counts after eliminating the eight (resp. six, seven) auxiliaries: 11, 7, 8, 5 for D,B,C,A.

Relation to Moh/FSY `I_29`: the raw odd list `h_23,h_21,...,h_5` is the unfaithful encoding. The corrected job is `g_22=...=g_4=0` with `g_3≠0` in the same NR chart. EMPTY of that open ideal is the curve-level kill the Moh-check lane could not source.

## 5. Coefficient-by-coefficient: `(9,6)` reduced remainders

Exact expansion of `K=p^2-q^3` and `G96`. Support of `K` is `2..16` (`k_17=0`, chart identity). Support of `G96` is `1..16` (`a9 p` contributes degree 9 and below, including odd 1). Leading coefficients:

```text
k_17 = 0                          g_17 = 0
k_16 = 2*A - 3*a                  g_16 = 2*A - 3*a
k_15 = 2*P6 - 3*Q3                g_15 = a15 + 2*P6 - 3*Q3
k_12 = 2*A*B + P6^2 + 2*C - a^3 - 6*a*b - 3*Q3^2
g_12 = k_12 + a12 + a15*(P6+Q3)
k_9  = 2*A*P2 + 2*B*P4 + 2*C*P6 - 3*a^2*Q1 - 6*a*Q3*b - Q3^3 - 6*b*Q1
g_9  = k_9 + a9 + (a15,a12 corrections)
k_6  = 2*B*D + C^2 + 2*P2*P4 - 3*a*Q1^2 - 6*Q3*b*Q1 - b^3
g_6  = k_6 + a6 + (a15,a12,a9 corrections)
k_4  = 2*C*D + P2^2 - 3*b*Q1^2
g_4  = k_4 + a15*(C*Q1+D*Q3+P2*b) + a12*(2*Q1*Q3+b^2) + a9*P4 + a6*a
k_2  = D^2
g_2  = D^2 + a15*D*Q1 + a9*P2 + a12*Q1^2 + a6*b
```

`g_16=k_16`: degree 16 is a gap of `⟨9,6⟩` (16 not divisible by 3), so it is a genuine residual with no auxiliary. `g_15` is the `a15`-slot. The old raw jobs zeroed `k_15,k_12,k_9,k_6`, i.e. forced `a15=a12=a9=a6=0`. The encoded equations solve for those four coefficients instead.

`corrected_964.ms` generators, in order: `g_16,...,g_5` then `u*g_4-1` (13 polynomials, 15 file lines). Constants omitted (audit 7.1: every target degree is positive).

## 6. Encoding choices that are not equation ambiguities

The audit's closed/open lists are unambiguous. No `_a`/`_b` files.

**I_DP vs Groebner generators (P3).** Audit 7.1: on each corrected locus, invert `Res_t(p',q')`, then run the reduced unordered double-point check with `N=6`. That is a post-check on a closed point, not a unit-ideal test of `Iopen` (the corrected `(9,6,4)` locus is already known nonempty). Adjoining one off-diagonal pair `(s,t)` to the Groebner system would encode “at least one node,” which the HF-twin already has four of, and would not encode length 6. Six explicit pairs would change the ring and the meaning. Encoded: characteristic incidence in both engines; `idpPostcheck(p0,q0,6)` (immersive, 0-dimensional, degree 6, radical; variable `Pi` not `pi`) in the M2 file. Distinct-tangents / no-reused-parameter remain the existing `idp_postcheck.m2` clauses on an extracted point.

**In-band `.ms` comments.** Campaign 2026-08-24: a comment before the variable line is parsed as one variable. msolve's input parser does not skip `#` lines. The GROBNER-mode convention is therefore in every `.m2` header and in §0, not inside the `.ms` bytes.

**Cover colon / immersive resultant.** M2 only, rings asserted, named `colonInf`, `diff(t,p)` not `diff(p,t)`. Not in msolve (no slack variables).

## 7. Self-check transcripts (verbatim)

Sandbox: sympy 1.14.0. No msolve, no M2 Groebner. Substitutions into the same expanded `g_j` that were written to the `.ms` files.

### (i) charged A false-positive vs corrected `(8,6,11)` — required FAIL

Point (audit §5), chart order `(B,C,D,E,F,G,b,gam,d,e,f)`, `zeta^2-zeta+18474=0`:

```text
B=1, C=0, D=(294-zeta)/144, E=0, F=(150-zeta)/48, G=0,
b=1, gam=3/4, d=1, e=-(138+zeta)/192, f=(2*zeta-71)/144.
```

```text
check(i) g22 at point (in a22): a22 - 4
check(i) g21 at point: 0
check(i) h19 at point: 0
check(i) g19 residual (a22=4): 11
check(i) raw h11 at point: 59291/18432 - 27671*zeta/110592
SELF-CHECK (i) charged A false-positive vs corrected (8,6,11): PASS — old A holds (g21=0, h19=0, h11=59291/18432 - 27671*zeta/110592 != 0) but corrected residual g19|a22=4b equals 11 != 0, so the point is not on V(g_22,...,g_12)
```

`h_11 = (355746-27671*zeta)/110592` after `59291/18432=355746/110592`, matching the audit. Residual `g_19=11` matches the audit's `[t^19]R=11`. The point satisfies every old A generator/open and fails the encoded corrected A system. FAIL of membership is the required outcome; the self-check harness labels that outcome PASS.

### (ii) `(9,6,2)` curve vs corrected `(9,6,2)` membership — required PASS

`q=t^6+8t^2`, `p=t^9+12t^5+24t`. Auxiliaries `(a15,a12,a9,a6)=(0,0,0,-64)` recover the identity `p^2-q^3-64q=64t^2`.

```text
check(ii) closed g_16..g_3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check(ii) g2: 64
check(ii) g0,g1: 0 0
SELF-CHECK (ii) (9,6,2) curve q=t^6+8t^2, p=t^9+12t^5+24t vs corrected (9,6,2): PASS — aux (a15,a12,a9,a6)=(0,0,0,-64) gives g_j=0 for 3<=j<=16 and g_2=64 != 0
```

No `(9,6,2)` job file was emitted (type REALIZED). The membership check uses the same `G96` as `corrected_964`.

### (iii) HF-twin `(9,6,4)` vs corrected locus (before nodal) — required PASS

Shared constant-zero chart: `A=3`, `B=21/4`, `C=35/8`, `D=63/32`, `a=2`, `b=5/2`, mixed terms zero. Auxiliaries `(a15,a12,a9,a6)=(0,-9/4,0,-27/16)` (constant `-27/64` omitted).

```text
check(iii) closed g_16..g_5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check(iii) g4: -27/128
check(iii) g3,g2,g1,g0: 0 -351/1024 0 0
SELF-CHECK (iii) HF-twin (9,6,4) vs corrected (9,6,4) locus: PASS — aux (a15,a12,a9,a6)=(0,-9/4,0,-27/16) gives g_j=0 for 5<=j<=16 and g_4=-27/128 != 0 (constant term 0 omitted as in audit 7.1)
```

Leading `g_4=-27/128` is `(-27/1024)*8`, matching the displayed identity. The point lies on `V(g_16,...,g_5)` with `g_4≠0`, hence on the encoded corrected 96A locus, before any nodal test. `g_2≠0` is allowed: the type is `c=4`, not `c=2`.

## 8. Per-file SHA-256 (emitted jobs)

Independent `shasum -a 256` of the bytes on disk after the last write. POSIX text, LF only, one trailing newline. `.ms` files contain no parentheses.

```text
cd13e1c25bcfcc43d30c238420ab8383580b8c078b16c0b0ff967ff43761d75b  box/corrected_863.ms
a6c7e647316f6546145a855b4f8ee972a188f5a2db1171304f5f032c7beff937  box/corrected_863.m2
d0d5e5d40ce74adda6f84df2e01959fe7f628625cd76537df24febd74471adb8  box/corrected_869.ms
a86a9782f516431723ede80555d5b41f7630a970d79e3afcc939cd3d5ed562ce  box/corrected_869.m2
f2c46839b56a766230eebd7e279a88f449fe0df0ecf8f1dc09cbaf0f39cc6434  box/corrected_964.ms
71065d4986dbadf08bf91b29e34f7c8f828ed1dfdd42272419439e799461fd74  box/corrected_964.m2
9feb22915f92f92eb80aedff29829c0e2846dcc8d3147aed895c503f343b5766  box/corrected_8611.ms
67314c378279c7016b582cbc876d3593a820fdb48afba28312fddbe777ededc0  box/corrected_8611.m2
2f6cb64e1a44cd9176c8b424a3bc4323090fa9fe2570a9593d365308d9d61ea5  box/corrected_867.ms
658ddd2472b1731b86f50de9b3db6e10dd7f2db9c8c6c8023c5ede1edafd6f0b  box/corrected_867.m2
```

Suggested AWS invocation (not run here): `msolve -v 2 -g 2 -f box/corrected_863.ms`. Output `[1]:` (length-of-basis 1, the constant 1) is EMPTY.

## 9. Guardrails, limitations, status

- **Flag/place/series:** not in play. The charged A point remains one place with conjugate series; this lane only tests coefficient-ideal membership.
- **Raw remainder degree:** encoded generators are `[t^j]G86` / `[t^j]G96` after the 7.1 auxiliaries, not raw `h_j`/`k_j`. Zero, vanished leaders, and gap degrees 10/4 and 16 are explicit.
- **Variable/ring map:** charts and auxiliary names are declared; M2 names `killt` before applying it; matching names are not used as a map proof.
- **`sat()` wrapping:** no `saturate()`. Opens are Rabinowitsch. Cover colon is a named loop with a ring assert each pass.
- **Floor/attainment:** HF-twin NONEMPTY of the corrected `(9,6,4)` locus is not a six-node witness. `(9,6,2)` is not re-promoted; the membership check is a regression control.
- **Carrier:** `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. Emitting a job is not a realization or a kill.
- **Scope:** no msolve/M2 Groebner, no ledger edit, no `jc2-lean`, no exit-price claim.

**Final status: jobs emitted, self-checks PASS, types still OPEN at their stated scopes.** P1 `(8,6,3)` is the live curve-level kill path (Moh-check died). P3 is the six-node question on a known-nonempty locus. P2 is corrected type B. P4 is archival.

No `charge_basis` line: this report does not assert a new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16110`.
- Body SHA-256:
  `3a5b451c004d400a0e1f9f2f9a44fca97751b3a00d3457f93c64c18676cf9a2c`.
- Frozen basis: `7a35f2d99c72179080a504484cfc1cf790abb642`.
