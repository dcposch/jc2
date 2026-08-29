# Hostile Review of `sigray-section9-source-audit-sol-ultra-20260828.md`

Date: 2026-08-28
Reviewer: GPT-5.5 / Codex hostile pass
Working tree: `/Users/dc/code/math/jc2`

## 0. Custody

Audited producer report:

```text
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
```

The expected SHA-256 matches.

The task names `refs/sigray1977.pdf`, but that file is absent in this
workspace. I used the available Sigray thesis file already used by the
campaign:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

`pdfinfo` reports 66 pages. The printed page numbers equal the physical PDF
page numbers for the audited range. I checked printed/PDF pp. 45--60 for
Section 9, and pp. 10--18, 23--28, 28--39, and 39--45 for the cited Section
3--8 dependencies. Relevant canonical campaign files inspected were
`SHEET6-CAMPAIGN.md`, `SHEET6-REVIEW.md`, `SHEET6-AF2.md`,
`SHEET6-AF3.md`, `SHEET6-H3.md`, `SHEET6-HIII-REVIEW.md`,
`SHEET6-A2P-REVIEW.md`, `SHEET6-A3L1-REVIEW.md`, the Section 7 hostile
review/resolved-direction file, and the Section 8 hostile review. I did not
enter, list, search, read, build, modify, status, or control `jc2-lean`.

## 1. Overall Verdict

**CONDITIONAL PASS.** The producer's source diagnosis and repaired `td < 6`
assembly survive hostile audit, provided the already-promoted repairs to
Sections 3--8 are part of the trust base, especially:

1. repaired Corollary 7.1 for distinct critical-value vertices, plus the
   resolved-direction/no-duplication lemma;
2. corrected nonroot Proposition 8.4 only;
3. repaired Section 8 divisibility/polynomiality package;
4. the H3-psi budget use of Statement 9.4(25).

The printed thesis proof is not valid as written. The repaired result is:

```text
No normalized counterexample has td(f,g) <= 5.
Equivalently, any normalized counterexample has td(f,g) >= 6.
```

Section 9 does **not** exclude `td = 6`. The producer is right to separate
`td < 6` from `td = 6`, and right that the repaired `td < 6` proof does not
use the quarantined root clause of Proposition 8.4.

I found one non-load-bearing defect in the producer report itself:
Section 5.1 says, too broadly, that in IIa `k > 0` forces `l = 0`, and that
the distinguished factor occurs to exponent `mu-1` in `q`. The statement is
safe only in the `mu = 2` uses where the producer actually solves equations;
the reduced ODE pattern used later in the report has exponent one at roots
of `p`, and the `mu = 3,4` zero/nonzero branches are handled by charge, not
by a general `l = 0` theorem. Minimal repair: replace that sentence by
"In the `mu = 2` IIa branches solved below, regularity/Statement 8.2 forces
`l = 0`; in general the reduced `q` has a simple factor at each root of
`p`, and `k > 0` gives a positive exit charge rather than a universal
`l = 0` conclusion."

This overstatement does not affect the producer's row-4 proof, because the
subsequent statement-by-statement arithmetic uses the correct equations.

## 2. Claim Ledger

| Claim | Verdict | Hostile finding / minimum repair |
|---|---|---|
| Producer hash | PASS | Matches expected SHA-256. |
| Primary source path | CONDITIONAL | `refs/sigray1977.pdf` is absent; audit used `refs/sigray_full.pdf` SHA above. |
| Table (23), eleven numerical rows | PASS | Re-enumeration from Statement 5.2 and `Lambda <= 6` gives exactly 11 rows. |
| Row labels in table (23) | PASS as erratum | The first row printed as `6` in the `(3,4)` block is row 5; source labels rows 5 and 6 both `6`. |
| Pole `M` values | PASS | At a pole, Proposition 5.1 gives `m_F=0`; Proposition 4.2 has `h_0=g`; Notation 8.1 gives `M_F=gcd(deg p_F,deg p_{g,F})`. Thus the producer's `M` column is pinned. |
| Notation 9.1 domain | PASS | `Q(F)` is ill-typed on nonvertex points of `T_a^+`; restrict to `F in V_a`. |
| Statement 9.1 | PASS with typo | Source has one extra parenthesis; formula follows from Proposition 4.1. |
| Notation 9.2 regularity wording | PASS | Source's "regular over" orientation is later mistyped in Statements 9.7--9.10; the intended lower-over-upper reading is correct. |
| Singleton-pole regularity lemma | CONDITIONAL PASS | The sibling-pole exclusion is valid using Propositions 6.7--6.8 plus singleton-pole uniqueness. It belongs in the repair, not in the printed text. |
| Statement 9.2 root data | PASS with convention | `V_1` must use actual characteristic exponents `j >= 1`; otherwise Notation 3.4 asks for `e_{-1}/e_0`. Root `V_2` remains possible from distinct constant terms. |
| Statement 9.3 sign | PASS as source error | The printed RHS is `D/mult + kappa_F(1-pi(F))`; the proof and all numerical uses require `D/mult - kappa_F(1-pi(F))`. |
| `Y(F)`/lambda defect | PASS as source gap | Literal `Y(F)` is nested along a chain and double-counts. Replace by first-separation exit sets. |
| H2 first-separation exit-set repair | CONDITIONAL PASS | The difference-set construction is clean for a singleton-pole characteristic path once the Section 7 distinct-cv/resolved-direction repair is accepted. |
| Proposition 9.2 finiteness | PASS | Finite vertex set and strictly rootward `o` iteration give a finite characteristic sequence ending at `(0,y)`. |
| Proposition 9.3 I--II arithmetic | PASS | With `i=P/mu`, formulas match the printed proof. |
| Proposition 9.3 III denominators | PASS as source error | Child `D,K` denominators must be `nu_G`; the printed `nu_F` denominators are not correctly typed unless one adds an unproved equality. |
| Proposition 9.3 IV | CONDITIONAL PASS | The formulas need `nu=nu_G` and the Section 8 Bezout/divisibility repair. They give integrality, not a blanket root contradiction. |
| Producer's general IIa/q-pattern sentence | FAIL, non-load-bearing | Too broad, as noted in Section 1. Later calculations use the right equations. |
| Statement 9.6 | PASS with repairs | Phantom `(k,n,nu)=(1,13,25)` is false; raw solution is `(1,12,25)` and violates `n == 1 mod 3`. Correct charged children and zero family check. Fix the `q` exponent. |
| Statement 9.7 | PASS with repairs | `regular over F` -> over `G`; `M_G=1` -> `M_F=1`; case-IV proof line `7j` should be `j`. Zero family checks. |
| Statement 9.8 / E2 | PASS as source incompleteness | The `mu=2,l=0` family exists with `M_F=2`; source wrongly says `M_F=1`. The `mu=4` branch has the same numeric family with `M_F=4`. |
| Statement 9.9 / E3 | PASS as source incompleteness | Both printed "no solution" claims are false; `l=0, nu=4t+3, m=3t+2` gives zero-charge self-families with `M_F=2,4`. Root alternative needs `s >= 1`. |
| Statement 9.10 / E4 | PASS as source incompleteness | `l=0, nu=3t+2, m=2t+1` gives the omitted `M_F=3` self-family. Printed alternative (iv) is a copy intrusion. Root alternative needs `s >= 1`. |
| Statement 9.11 | PASS with repairs | Nonzero charged solutions and zero self-family check; fix the same `q` exponent issue as in 9.6. |
| E2--E4 recurrence | PASS | The omitted zero-charge branches are genuine self-families after rescaling. They cannot be infinite survivors because Proposition 9.2 makes the characteristic sequence finite. |
| Repaired row-4 closure | CONDITIONAL PASS | Valid using corrected transition lists, local exit budget, H3-psi, finite termination, and nonroot `M=1`. Not valid as printed. |
| `td <= 5` assembly | PASS after repair | `td <= 5` forces one pole and rows `{1,4,5,7,10}`. Rows 1,5,7,10 die by pinned pole `M=1`; row 4 dies by repaired Statement 9.12. |
| `td = 6` distinction | PASS | Section 9 leaves single-pole rows 8,9 and the two-pole `3+3` case; it proves no degree-six exclusion. |
| Independence from root Proposition 8.4 | PASS | All `M=1` kills used in repaired `td < 6` are at pole or nonroot transition vertices. Root terminals are handled by case-IV `(m)` or H3-psi. |
| Use of Section 7 | CONDITIONAL PASS | No illegal use found after replacing literal `Y(F)` by disjoint exit sets. This remains conditional on the repaired Corollary 7.1/distinct-cv trust base. |
| Circularity / Section 9 used too early | PASS with warning | The row-4 proof may use Section 7 and repaired Sections 8/9 local transition results, but must not be advertised as the printed proof. No dependence on later `td=6` campaign results is needed. |

## 3. Independent Arithmetic Checks

### 3.1 Table (23)

From Statement 5.2, write

```text
(D_F,D_g,F) = a(alpha,beta)
(deg p_F,deg p_g,F) = b(alpha,beta)
Lambda = a*b*alpha*beta/nu
```

with `1 < alpha < beta`, `gcd(alpha,beta)=1`, `beta <= Lambda <= 6`, and
one of

```text
nu | alpha and nu | (b beta - 1),
nu | beta  and nu | (b alpha - 1).
```

Exact enumeration gives only:

```text
row 1  (2,3), a=1,b=1,nu=2, Lambda=3, M=1
row 2  (2,3), a=1,b=1,nu=1, Lambda=6, M=1
row 3  (2,3), a=2,b=1,nu=2, Lambda=6, M=1
row 4  (2,3), a=1,b=2,nu=3, Lambda=4, M=2
row 5  (3,4), a=1,b=1,nu=3, Lambda=4, M=1
row 6  (3,4), a=1,b=1,nu=2, Lambda=6, M=1
row 7  (2,5), a=1,b=1,nu=2, Lambda=5, M=1
row 8  (2,5), a=1,b=3,nu=5, Lambda=6, M=3
row 9  (3,5), a=1,b=2,nu=5, Lambda=6, M=2
row 10 (4,5), a=1,b=1,nu=4, Lambda=5, M=1
row 11 (5,6), a=1,b=1,nu=5, Lambda=6, M=1
```

This matches the producer, modulo row ordering and the source's row-label
misprint.

### 3.2 Transition Families

I re-solved the small Diophantine equations with exact integer arithmetic.
The checks agree with the producer:

```text
9.6, k>0:     (k,n,nu) = (1,10,7), (2,7,5)
9.6, k=0:     l=0, n=9s+4,  nu=2s+1, s>=1
9.7, k=0:     l=0, n=14s+9, nu=3s+2, s>=0
9.8, mu=2:    l=0, n=15s+11, nu=4s+3, M=2
9.8, mu=4:    l=0, n=15s+11, nu=4s+3, M=4
9.9, mu=2,4:  l=0, m=3t+2, nu=4t+3, M=2 or 4
9.10, mu=3:   l=0, m=2t+1, nu=3t+2, M=3
9.11, k>0:    (k,m,nu) = (1,3,7), (2,2,5)
9.11, k=0:    l=0, m=3phi+1, nu=2phi+1, phi>=1
```

The root case-IV restrictions `s >= 1` in Statements 9.9 and 9.10 are also
real: at `s=0`, `K_G = nu_G`, violating Proposition 9.3(j).

## 4. Row-4 Closure

The producer's repaired row-4 proof is sound at the campaign trust perimeter.
The clean version is:

1. Row 4 gives the pole entry `Q=(2,4,3,2,5)` and budget `td-2=2`.
2. Statement 9.6 either gives a nonroot `M=1` kill, a charge at least 3, a
   charge-2 entry into the 9.7/9.8 sides, or a zero-charge 9.11 self-family.
3. The 9.7/9.10 side has terminal ratio `R=3`; H3-psi gives allowed budget
   `td-1-(ceil(R)-1)=1`, so an accumulated charge 2 is fatal.
4. The 9.8/9.9 side has terminal ratio `R=4`; H3-psi gives allowed budget
   `0`, so an accumulated charge 2 is fatal.
5. E2--E4 add zero-charge self-families, not survivors. Finiteness of the
   characteristic sequence forces eventual exit; exits are `M=1`, positively
   charged, root-impossible by `(m)` in the E2 `M=2` family, or root-killed
   by H3-psi in the `M=3,4` families.

The E2 `M=2` closure deserves to be part of the published repair. With
`r=4s+3` and

```text
Q(G)=(3rj,4rj,r,2,3(r+1)/4),
```

case IV gives `d_root=rj`, hence

```text
d_root*M_G/deg(p_G) = rj*2/(4rj) = 1/2,
```

contradicting Proposition 9.3(m). Root case I is also impossible: the root
ratio is `mu/4 <= 1/2`, while the case-I reduced pattern ratio is at least
one. The only zero-charge nonroot continuation is again the same E2 family,
with new scale.

This is a repaired proof, not the source proof. The printed Statement 9.12
uses only the dichotomy "some `M=1` or (26) fails", and that dichotomy misses
its own case-IV terminals.

## 5. Root and `td=6` Boundaries

The producer's root bookkeeping checks.

Root membership must be treated carefully:

```text
(0,y) notin V_1     after the necessary j>=1 convention;
(0,y) may be in V_2 from distinct constant terms.
```

Thus a terminal root may be Proposition 9.3 case I (SF1) in general, and no
global "roots are only case IV" convention is legal.

For the repaired row-4 graph, however, SF1 does not occur:

```text
9.6 and 9.11: K_G >= nu_G, so root K=1 would require n<=0.
9.7: root case I forces ratio mu/3; mu=3 gives 1 while case-I pattern >1,
     and mu=1 gives 1/3 while the root pattern has ratio 1.
9.8 and 9.9: root ratio mu/4; mu<4 is <1, mu=4 is 1, while case-I pattern
     is >=1 or >1 as appropriate.
9.10: same check with mu/3.
```

Therefore every `M=1` used in row-4 closure is nonroot. Rows 1,5,7,10 also
die at nonroot pole entries, since Proposition 5.3(i) says a pole vertex is
not `(0,x)` or `(0,y)`.

For `td=6`, the producer is right:

```text
single pole: rows 2,3,6,8,9,11;
two poles: row 1 + row 1.
```

Pole pin plus nonroot Proposition 8.4 kill rows 2,3,6,11, but rows 8 and 9
remain source-level live, and Proposition 8.4 is unavailable in the two-pole
case. Section 9 proves no exclusion of `td=6`.

## 6. Minimal Clean Repair Stack

The minimum source repair I would promote is:

1. Replace `refs/sigray1977.pdf` references in local audit metadata by the
   actual source file `refs/sigray_full.pdf`, or add the missing alias with
   the same SHA.
2. Correct table (23)'s row label and add the pole pin
   `M_F=gcd(deg p_F,deg p_g,F)`.
3. Restrict `Q(F)` to vertices and define `V_1` using actual characteristic
   exponents `j>=1`; keep root `V_2`/SF1 possible.
4. Replace Statement 9.3 by the minus-`K` inequality:

```text
c* != 0:  kappa_H(pi(H)-1) >= D_F/mult(p_F,c*) - K_F
c* = 0:   kappa_H(pi(H)-1) >= (D_F/mult(p_F,c*) - K_F)/nu_F
```

5. Replace literal chain sums of `Y(F)` by pairwise disjoint first-separation
   exit sets and apply repaired Corollary 7.1 to their union plus the
   x-side `psi` vertex.
6. State Proposition 9.3 with orientation fixed, `i=P/mu`, case-III child
   denominators `nu_G`, and case-IV `(m)` as integrality only.
7. Correct Statements 9.6--9.11 as in the ledger above, especially E2--E4.
8. Prove the E2 `M=2` self-family closure and the finite-exit argument.
9. Use H3-psi for root case-IV terminals; do not use root Proposition 8.4.
10. Assemble `td<=5`: rows 1,5,7,10 die by nonroot pole `M=1`; row 4 dies
    by repaired Statement 9.12. State explicitly that `td=6` is outside the
    conclusion.

## 7. Final Classification

```text
Producer report as a hostile-audited repair:       CONDITIONAL PASS
Printed Section 9 proof:                           FAIL
Table (23) numerical enumeration:                  PASS
Pole M pin and entry kills:                        PASS
Statement 9.3 sign repair:                         PASS
Y(F) first-separation repair:                      CONDITIONAL PASS
Statements 9.6--9.11 corrected arithmetic:         PASS
E2--E4 zero-charge families:                       PASS
Repaired row-4 exclusion:                          CONDITIONAL PASS
Repaired theorem td(f,g) >= 6:                     PASS
Any Section 9 proof of td(f,g) != 6:               FAIL / NOT CLAIMED
Use of root Proposition 8.4:                       NOT NEEDED
```

No counterexample to the producer's repaired `td < 6` conclusion was found.
The only producer-side correction needed is the IIa/q-pattern overstatement
called out in Sections 1 and 2.
