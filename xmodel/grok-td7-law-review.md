**VERDICT: SOUND — the normal form is the P3 B/C object, both directions of the boxed iff replay, the 56/62 census and all six explicit survivors substitute exactly, and both citation corrections are true.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `xmodel/sol-td7-law.md` (GPT-5.6-Sol, td-7 closed-form Prop. 8.1(iv) kill law).
Method: read the cited BOOK-OFFAXIS / SHEET6 / BASH-R2 / TEMPLATE pins against the claimed object; re-derive (2)–(8) from the η-form of Prop. 8.1(iv); run the stated `px5.py` + perl reproduction and an independent silent raw/dedup recount; substitute the six advertised \(s(t)\) into \(E(t)\) over \(\mathbb{Q}(A)\).
No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: clear — the normal form is the right object

- File: `xmodel/sol-td7-law.md:64-93`, citing `BOOK-OFFAXIS.md` R1.0:209-224, R2.2:317-327, P3:521-549
- Claim: every one of the 62 B/C cells is, up to nonzero pattern scalars,
  \(t=\eta^\nu\), \(A=c^\nu\neq0\), \(p=\eta^\mu(t-A)\), \(q=\eta(t-A)s(t)\) with \(\deg s=\ell\).
- How checked:
  - R1.0 really is the Prop. 8.1(iv) root law claimed: every \(p\)-root is simple in \(q\), every off-\(p\) \(q\)-root is simple, and \(\nu\geq2\Rightarrow\eta\mathbin\Vert q\). It does *not* by itself give the displayed shape.
  - R2.2 is the merge radical: \(p_{\mathrm{red}}=\ominus\eta^\varepsilon\prod_e(\eta^\nu-c_e^\nu)^{\mu_e}\prod_j(\eta^\nu-d_j^\nu)^{m_j}\) with \(\varepsilon=\mu_0\) iff a 0-chain arrives, and \(q=\ominus\eta\cdot(\text{each distinct nonzero \(p\)-orbit once})\cdot(\text{simple extras})\), so \(d_q=(r_0+k+\ell)\nu+1\).
  - P3: single merge \(G\) has \(r=2\); chain 1 is frozen at \((\mu,w,M)=(1,2,1)\) and is the only nonzero arrival; chain 2 arrives at 0 (class B: \(\mu_0=1\); class C: \(\mu_0\geq2\)); \(\sum m_j=0\) (P3:547-548); degree pins \(d_p=1+\nu_G\) (B) and \(d_p=\mu_0+\nu_G\) (C).
  - Those pins force \(\Pi_e\) to run over *nonzero* arrivals only (a 0-edge inside \(\Pi_e\) would contribute \(\eta^{\nu\mu_0}\) and give \(d_p=\mu_0+\nu\mu_0+\nu\), contradicting \(d_p=\mu+\nu\)). Combined with \(k=0\), \(r_0=1\), \(\mu_1=1\), this is exactly (1), with \(\ell:=(d_q-1)/\nu-1\) the R2.2 extra-orbit count. R1.0 already gives \(d_q\equiv1\pmod\nu\), so \(\ell\in\mathbb{Z}\). \(d_q/d_p=\bar\kappa/(\bar\kappa-2)>1\) forces \(\ell\geq1\) on the whole book (an \(\ell=0\) cell would have \(d_q=1+\nu\le d_p\)).
- Classic wrong-object failure that does *not* occur: writing the 0-arrival as \(t^\mu=\eta^{\nu\mu}\) instead of \(\eta^\mu\). The P3 degree pin kills that. Class B is the \(\mu=1\) member, i.e. the off-axis ZCH shape, as claimed.
- Nit, not a break: \(d_q=1+(\ell+1)\nu\) is not a P3 display. P3 writes \(d_q=\bar\kappa\,d_p/(\bar\kappa-2)\) for class C and names the two class-B cells. The orbit form of \(d_q\) is R2.2 plus the P3 arrangement. Content is right; the line-cite is slightly fat.

### 2. Severity: clear — both directions of the iff, including the \(\bar\kappa\in\{3,4\}\) pin

- File: `xmodel/sol-td7-law.md:95-206`
- Claim: admissible Prop. 8.1(iv) solution with nonzero RHS constant iff \(d_p\nmid d_q\), equivalently \(d_p\mid d_q\iff(\mu+\nu)\mid(\mu(\ell+1)-1)\iff M=d_p\iff\bar\kappa\in\{3,4\}\); \(r=2\) never enters; on-axis ZCH \((\nu+1)\mid\ell\) is the \(\mu=1\) case.
- How checked (independent \(\eta\)-calculus, then a \(\mathbb{Q}\) sweep):
  - Printed ODE is \(\delta p q'-(1-u)p'q=\ominus p\) (`SHEET6-L1.md:73-80`, `cases/l1_ode_check.py:5-15`). Division by \(1-u\) is legal on this book: \(\bar\kappa=\kappa(1-\pi)\ge3\Rightarrow\pi\neq1\). Top cancellation gives \(\rho=d_p/d_q\). Substituting (1) and cancelling \(\eta^\mu(t-A)\) reproduces (3) exactly. No scalar can flip the zero/nonzero verdict of \(\widetilde C\).
  - Coefficient extraction on monic \(s=\sum_{j=0}^\ell s_j t^j\) reproduces (4) after the \(\nu\)-cancellation \(d(1+\nu k)-\mu D=\nu(1+dk-\mu(\ell+1))\). Denominator \(d(k-\ell-1)\) is in \(\{-d\ell,\ldots,-d\}\), never zero on \(k=\ell,\ldots,1\). Constant term is (5). Product (6) is the unique monic iterate.
  - Identity (8) is an equality of polynomials in \((\mu,\ell,\nu)\). Hence a numerator in (6) vanishes iff \(d\mid(\mu(\ell+1)-1)\) iff \(d\mid D\). On positive integers, \(d\mid D\) already forces \(D\ge d\); the corresponding \(k=\ell+1-D/d\) lands in \(\{1,\ldots,\ell\}\) as soon as \(D>d\), which is the pin \(d_q>d_p\) from \(\bar\kappa>2\), not an extra divisibility. Checked on the rectangle \(\mu\in[1,11]\), \(\ell\in[1,11]\), \(\nu\in[2,19]\): no off-by-one.
  - Zero-pivot form \(s=t^k(t-A)^{\ell-k}\) is not needed for the kill (\(\widetilde C=0\) suffices) but is correct: it satisfies (3) with \(\widetilde C=0\) iff (7) holds, and the ladder has a unique monic solution. Confirmed on 38 abstract dead \((\mu,\ell,\nu)\) triples. Because \(D>d\), one has \(k<\ell\), so the residual really does pick up extra multiplicity at both \(0\) and \(t=A\).
  - Converse: if \(d_p\nmid d_q\), no numerator vanishes, so \(s_0\neq0\), so \(\widetilde C=A(\mu-\rho)s_0\neq0\) (\(A\neq0\), \(\mu\ge1>\rho\)). Evaluating (3) at \(t=0\), \(t=A\), and at a root \(b\) of \(s\) gives exactly the three R1.0 conditions they list. Linear triangular, not Gröbner.
  - \(\mu=1\Rightarrow d=\nu+1\) and \(D=(\ell+1)d-\ell\), so \(d\mid D\iff(\nu+1)\mid\ell\). Matches `BOOK-BASH-R2.md:31-37` and the residual shapes at `:80-130`.
  - \(\bar\kappa\) pin from equations, *not* from the census: R2.1 + P3 give \(X=\bar\kappa-2\) (chain 1 has \(\mu_e=1\), \(w_e=2\)) and \(X/\bar\kappa=d_p/d_q\), hence (9). N1 (`SHEET6-III.md:121-129`) puts \(\bar\kappa\in\mathbb{Z}\); \(X>0\) puts \(\bar\kappa>2\). Then \(d_p\mid d_q\) iff \(\bar\kappa/(\bar\kappa-2)\in\mathbb{Z}\) iff \(\bar\kappa-2\mid2\) iff \(\bar\kappa\in\{3,4\}\). This uses only the td=7 chain-1 freeze and the general handshake/integrality, not the 62-tuple list. \(M=\gcd(d_p,d_q)=d_p\) is the definition, also Prop. 8.1(v) / R2.2(D):327-331.
  - \(r=2\) does not appear in (2)–(6). It *does* enter the object: \(r=2\) plus one 0-arrival is why \(p\) has a single nonzero \(t\)-factor. Once (1) is fixed, \(r\) is gone. The boxed test is not a family-I \(r\)-law and is not being applied off this book. Acceptable.
- Nit, not a break: step 2 asserts \(D>d\) before step 4 invokes the pin that proves it. True on the book, just out of order.

### 3. Severity: clear — census reproduces to the last integer

- File: `xmodel/sol-td7-law.md:208-312, 353-376`
- Claim: 61 class-C tuples, 55 dead, the displayed 30+25 killed lists, six exceptions, 1,636/1,689 routes removed, 53 remaining of which 35 are budget-equality; class B is \((3,9,2,3)\) with 18 routes / 14 equality.
- How checked:
  - Ran the stated block: `python3 cases/scratch_offaxis_pricing/px5.py > /tmp/px5.out` (exit 0, 53s), then the perl unique-sort. Result: **61** lines.
  - Independent arithmetic on those 61: \(\ell=(d_q-1)/\nu-1\), \(\bar\kappa=2d_q/(d_q-d_p)\), \(\mathrm{dead}\iff d_q\equiv0\pmod{d_p}\). Split is **55 dead / 6 alive**. \(\bar\kappa\) histogram is \(\{(3,30),(4,25),(5,4),(6,2)\}\) — so “3 and 4 die, 5 and 6 pass” is the book, not an extra restriction in the law. Every dead cell has \(M=d_p\); every alive cell has \(M<d_p\). All 62 (incl. B) satisfy \(\gcd(\bar\kappa,\nu)=1\), so L6 kills nothing here.
  - The 30 \(\bar\kappa=3\) tuples, 25 \(\bar\kappa=4\) tuples, and 6 exceptions are exactly the generator’s sets (no missing, no extra, no overlap). Class B is the \(\mu=1\) cell \((3,9,2,3)\), \(\ell=3\), \(\bar\kappa=3\), \(3\mid3\).
  - Deduped `lam=… <= budget=…` parse of the same `/tmp/px5.out`:

    | outcome | cells | routes | equality |
    |---|---:|---:|---:|
    | B, killed | 1 | 18 | 14 |
    | C, killed | 55 | 1,618 | 1,341 |
    | C, left | 6 | 53 | 35 |
    | total | 62 | 1,689 | 1,390 |

    Left-cell route split: \((10,15,7,5)\) carries 47 (29 equality); the other five carry \(2+1+1+1+1\). Removed \(18+1618=1636\). Class A/tail: 0, as P4 claims.
  - Silent re-collection of `px5.surv` (same functions, no print): **raw 1,713 / raw equality 1,413**; after the documented `seen` key, **1,689 / 1,390**. `SEEN_BOUNDARY` empty.
- The 62-cell list is the generator’s book, not a Markdown table (`BOOK-OFFAXIS.md` P4:578-590 states the count and the px5 citation). They already say this. `cls_C_cells` uses a \(c_{\max}=40\mu_0\) cap on \(\bar\kappa\le4\); that can only omit *further dead* cells, so it cannot create a false survivor or shrink the exception list.

### 4. Severity: clear — all six advertised solutions are admissible with nonzero \(\widetilde C\)

- File: `xmodel/sol-td7-law.md:264-283`
- Claim: the six non-killed cells have the displayed monic \(s\) and nonzero \(\widetilde C\) in the normalization of (3).
- How checked: built \(E(t)\) from (3) over `fractions.Fraction` and compared both to the recurrence (4)–(5) and to the printed closed forms, at \(A=1\) and at \(A=5\).

  | cell | \(\mu,\ell,\bar\kappa\) | \(s(t)\) | \(\widetilde C\) | \(E(t)-\widetilde C\) |
  |---|---|---|---|---|
  | \((9,15,7,3)\) | 2,1,5 | \(t-\frac23 A\) | \(-\frac{14}{15}A^2\) | 0 |
  | \((10,15,7,5)\) | 3,1,6 | \(t-\frac12 A\) | \(-\frac76 A^2\) | 0 |
  | \((15,25,8,5)\) | 7,2,5 | \(t^2-\frac23 A t-\frac19 A^2\) | \(-\frac{32}{45}A^3\) | 0 |
  | \((15,25,12,5)\) | 3,1,5 | \(t-\frac23 A\) | \(-\frac85 A^2\) | 0 |
  | \((18,27,13,9)\) | 5,1,6 | \(t-\frac12 A\) | \(-\frac{13}{6}A^2\) | 0 |
  | \((39,65,32,13)\) | 7,1,5 | \(t-\frac23 A\) | \(-\frac{64}{15}A^2\) | 0 |

  Linear roots are \(A/2\) or \(2A/3\), neither \(0\) nor \(A\). Quadratic roots are \(A(1\pm\sqrt{2})/3\), discriminant \(8A^2/9\neq0\), \(s(0)=-A^2/9\neq0\), \(s(A)=2A^2/9\neq0\). These are genuine local T1 survivors, not divisibility-test misses.

### 5. Severity: clear — both citation corrections are true

- File: `xmodel/sol-td7-law.md:304-323`
- Claim A: L6 lives in `SHEET6-III.md:121-129`, not in `SHEET6-LROOT.md`; synthesis is `TEMPLATE-ATTACK.md:58-70`.
  - How checked: `SHEET6-LROOT.md` has **zero** hits for `L6` or for \(\gcd(\bar\kappa,\nu)=1\). What it actually proves is \(\lambda_{\mathrm{root}}=0\) at every case-IV terminal (`:100-126`) and the one-cv-vertex \(x\)-side quantum (`:136-160`), exactly as they retarget it. `SHEET6-III.md:121-129` is N1: \(\bar\kappa_G\in\mathbb{Z}\) and \(\gcd(\bar\kappa_G,\nu_G)=1\) at every \(\nu\ge2\) vertex. `TEMPLATE-ATTACK.md:58-60` names that statement **L6**. The prompt’s LROOT attribution is the error; the note is right.
- Claim B: two route-count conventions, 1713/1689 and 1413/1390.
  - How checked: `BOOK-OFFAXIS.md:587-590` already prints “1689 budget-fitting routes (1713 raw; engine adjudicate_td7 = 1713…)”; `:602-606` prints “1390 of the 1689” equality. Reproduction note `:650-667` reports the raw engine figures “1713 routes … exact-fit 1413” and “px5: 1689 routes”. `cases/book_offaxis.py:881-893` computes `exact` on the *raw* `adjudicate_td7()` list. Independent px5 recount above: raw 1713 / raw equality 1413, deduped 1689 / 1390. Both conventions exist and the numbers match.
  - Nit: P4 is not “deduplicated-only”; it prints 1713 raw in the same bullet as 1689. The discrepancy-explanation is still correct.

### 6. Severity: nit — surrounding citations are accurate and unused ingredients stay unused

- DEPTH \(w=(\bar\kappa-\rho)/\nu\) is `:67-77`; \(\mu=1\) handshake is §5a `:218-233`; case-III 0-edge prototype is §5c `:253-277`; §9 `:416-419` really does leave the Prop. 8.1(iv) coefficient layer out of scope. TEMPLATE §2b `:156-165` and the E5 \(w_i^4\) formula `:226-244` are the td=6 pole-to-merge calculation they decline to import. No CONJECTURE is used. The remaining six cells are claimed as local T1 survivors only.

---

## Attack-list scorecard

| # | Target | Result |
|---|---|---|
| 1 | Normal form (1) from R1.0 / R2.2 / P3 | Holds. Wrong-object (0-arrival as \(t^\mu\)) does not occur. |
| 2 | Iff (2)–(6), \(\mu(\ell+1)-1\), \(r=2\), \(\bar\kappa\in\{3,4\}\) | Holds in both directions, from the pins, not the census. |
| 3 | Census 61 / 55 / 6 / 1636/1689 / 53 / 35 | All reproduced. Raw companion 1713 / 1413 also reproduced. |
| 4 | Six explicit \(s,\widetilde C\) | All six satisfy \(E\equiv\widetilde C\neq0\) exactly. |
| 5 | L6 retarget; 1713/1689 and 1413/1390 | Both true. |

The local law is a full decision on the 62-cell book. The panel remains open on the six class-C cells, which is what the note claims.
