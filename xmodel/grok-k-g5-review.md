# Hostile audit: Conjecture K (sol-conjecture-k.md) and G5 BLOCKED (sol-g5-emission.md)

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-19.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Targets:

- **(A)** `xmodel/sol-conjecture-k.md`. Sol: the Conjecture-K premise is
  FALSE (no constant-linear dependence among \(g_1,g_2,g_3\) in any of
  72 fibers); the \(13\to 11\) cut is a torsion/component mechanism.
  Reconcile against the extraction-agent 8.S6 claim of rank 5 with one
  cross-prime dependency. Who is right, and does 8.S6 need a correction?
- **(B)** `xmodel/sol-g5-emission.md`. Sol: G5 is BLOCKED (FC5 +
  `M=1` depth-closure + NF-M cannot force the Sigray bound) and names a
  missing lemma. A false BLOCKED wastes the prize; check for a usable
  FC5 consequence he missed.

Method: independent `python3` reparse of
`cases/nf_reduced_rows_p{105337,105673,200257}.txt` and both
`cases/d23_atlas_p*.json`; exact \(\mathbf F_p\) rank / left-kernel /
character-template arithmetic; witness evaluation of the displayed
\(q_p\); algebraic replay of the G5 family, \(\Phi_s\), and both
sign-controls. Cited books (`TOWER-TD11.md` FC5, `SHEET6-DEPTH.md`,
`NF-M.md`, `SHEET6-CAMPAIGN.md` Prop 9.3, `SHEET6-AF2.md`,
`SHEET6-H3.md`, `BOOK-OFFAXIS.md` R2.2, `SHEET6-TDUNIFORM.md`,
`TDBOUND.md`, `REDUCTION.md`, `xmodel/sol-tdbound-review.md`,
`SHEET6-DIRECTIONB.md` 8.S5/8.S6/8.S8, `xmodel/sol-round5.md` §2,
`xmodel/grok-det23-review.md`) were read, not trusted. No Singular, no
msolve rerun, no 397-element normal-form division.

---

## Verdicts

### (A) Conjecture K

**CONFIRMED on the premise; GAPS on the replacement mechanism as a
banked theorem. 8.S6 needs a correction entry. Sol is right about
\(g_1,g_2,g_3\); the extraction agent is right about rank-5-of-six and
about \(13\to 11\); they are not talking about the same object.**

- The six compatibility normal forms have rank 5 and left-kernel
  dimension 1 at all three primes. The kernel vectors in (K.9)
  recompute exactly. This is the “four becomes three” syzygy among the
  six rows, already confirmed in `grok-det23-review.md`. It is **not**
  a constant-linear relation among \(g_1,g_2,g_3\).
- \(g_1,g_2,g_3\) are constant-linearly independent in all 72 atlas
  fibers and at \(p=200257\) `a00pp`. Private monomials
  \(x_{57}^2 uW_1^2\), \(x_{57}^2 uW_2^2\), \(x_{70}\) have coefficient
  1 in every fiber. Signature field
  \((\mathrm{cond\_dim},\mathrm{rank}\,w,\mathrm{rank\,NF},\dim\ker\mathrm{NF},\mathrm{rank}\,C,\dim V(I_{21}),\dim V(J_{23}))
  =(3,3,5,1,2,13,11)\) is uniform on both atlases, 0 anomalies.
- 8.S6’s prose “one variety-level dependency among the g’s” is the
  error. The atlas JSON already stores `cond_dim: 3` next to
  `nf_rank: 5`. The agent recorded both facts and then identified the
  dimension drop with a linear relation among the three residuals.
  Nullity of a rank-1 conormal span of three classes is two, not one.
- The torsion/component picture is the right *kind* of replacement,
  and two external consistency checks pass (witness \(q\)-values, D21
  sample on \(q=0\)). The load-bearing identities
  \(\mathrm{NF}(q(g_2-\lambda g_1))=0\) and the saturation table (K.19)
  are **not in the cited payloads or anywhere else in the repo**.
  Treat (K.1)--(K.3) as an unbanked computation, not a promoted
  modular theorem.

### (B) G5 emission BLOCKED

**CONFIRMED. The obstruction is airtight against the extracted
bookkeeping. No usable FC5 consequence was missed. The named missing
lemma is SP (one-pole cap \(ab\le\nu\)); it is exactly one-pole
TD-BOUND, not a reduction. KME-2 is TD-BOUND rewritten. PCC is the
only genuine sufficient lemma on the table, and it is unproved.**

A false BLOCKED would freeze the largest remaining prize. This BLOCKED
is not false. FC5 is a local frame-to-state identity; the natural
pole-mass potential \(\Phi_s\) is nonmonotone on coefficient-solvable
charts; the displayed numerical package (pole laws + N1 + Prop 9.3
IIa + FC5 + AF2-vs-ceiling + case-IV gates + local ODEs) admits an
unbounded type-\((2,3)\) arithmetic-schema family with constant FC5
output. Depth-closure is `M=1` and per-entry; NF-M bounds types of a
fixed schema, not sheets. The bookkeeping cannot force
\(\sum ab/\nu\le 1\), even at fixed type \((2,3)\).

---

## A. Who is right, and what 8.S6 actually said

### A.1 Two different rank-5 facts were glued into one sentence

8.S6 (`SHEET6-DIRECTIONB.md:1505-1510`) and the witnesses JSON
`dimension_analysis.anomaly`:

> the three residual conditions g1,g2,g3 cut only CODIMENSION 2 on
> the fiber (naive count 3) — one variety-level dependency among the
> g’s, identical at all three primes.

8.S8 (`SHEET6-DIRECTIONB.md:1824-1829`) then identifies that anomaly
with the NF payload:

> NF payload: 150 terms x6 rows, rank 5 (kernel dim 1) … g’s cut
> CODIMENSION 2, not 3 (13 -> 11) … the 8.S6 one-dependency anomaly
> is a FAMILY-WIDE structure.

`notes.md` (~09:15Z, ~10:00Z) repeats “one cross-prime-identical
dependency.” That is the claim Sol contradicts.

These are three true facts and one false identification.

| Object | Rank / drop | Who stated it | This audit |
|---|---|---|---|
| 6 NF rows as coefficient vectors | rank 5, leftker dim 1 | 8.S8, nf-quickshot header, (K.9) | **CONFIRMED**, three primes, vectors exact |
| \(\{g_1,g_2,g_3\}\) as polynomials | rank 3 (`cond_dim`) | atlas JSON, `grok-det23-review.md` claim (3), Sol 2.1 / round-5 §2.1 | **CONFIRMED**, 72 fibers + 200257 `a00pp` |
| \(\dim V(I_{21})\to\dim V(J_{23})\) | \(13\to 11\) | 8.S6 LT-staircase, atlas JSON | recorded uniformly; LT-staircase inherited from 8.S8 / prior atlas review, not re-GBed here |
| “therefore one linear relation among \(g_1,g_2,g_3\)” | — | 8.S6 prose, notes.md | **FALSE** if linear means constant coefficients |

The atlas JSON already refuses the false identification: every fiber
has `"cond_dim": 3` and `"nf_rank": 5` simultaneously. 8.S5’s own
semantics (`directionb_det23_p105337.rows.txt:19-20`) say \(g_s\) are
an RREF basis of a **3-dimensional** \(\{u\cdot b\}\) space. The
promoted det23 review already proved that span is 3-dimensional. 8.S6
was written after that linear algebra and still used “one dependency
among the g’s.”

**Adjudication.** Sol is right on the Conjecture-K premise. The
extraction agent is right that the six NFs have rank 5 and that the
maximum dimension drops by two. “Cross-prime identical” is true of
the *shape* (rank, nullity, supports, \(13\to 11\)) and false of the
integer kernel vector: (K.9) is three different vectors, and they
recompute. Sol’s sentence at the end of §5.2 is the correct
dictionary.

### A.2 Independent recompute of the six-row rank (the 8.S6 “rank 5”)

Each `nf_reduced_rows_p*.txt` has six polynomials, 150 terms each, one
shared 150-monomial support. Occurring extras among
\(\{x_{16},x_{24},x_{69},x_{47},x_{52}\}\): none. Affine of degree 1 in
\((x_{17},x_{25},x_{32},x_{37})\). Each tail column is a single carrier:
\(x_{17},x_{32}\) ride \(uW_1^2\); \(x_{25},x_{37}\) ride \(uW_2^2\).
So \(A=C\mathrm{diag}(uW_1^2,uW_2^2,uW_1^2,uW_2^2)\) as polynomial
matrices.

Exact \(\mathbf F_p\) rank of the \(6\times 150\) coefficient matrix:

| prime | `#`mons | rank | leftker dim | normalized leftker | matches (K.9) | \(a\cdot\mathrm{NF}\equiv 0\) | \(\mathrm{rank}\,C\) | \(C=[c_1\mid c_2\mid -c_1\mid -c_2]\) |
|---:|---:|---:|---:|---|---|---|---:|---|
| 105337 | 150 | 5 | 1 | `[1, 58526, 64401, 35257, 74853, 58238]` | yes | yes | 2 | yes |
| 105673 | 150 | 5 | 1 | `[1, 93937, 29382, 35369, 63348, 105378]` | yes | yes | 2 | yes |
| 200257 | 150 | 5 | 1 | `[1, 44507, 189160, 66897, 97147, 85205]` | yes | yes | 2 | yes |

At \(p=105337\), the extracted \(C\) matches
`directionb_det23_p105337.rows.txt` entrywise. `leftker C` has
dimension 4; the NF-kernel vector \(a\) lies in it; \(a\cdot b\equiv 0\)
as a polynomial (one of the four left-kernel conditions is the zero
polynomial). The three atlas `w_vectors` at `a00pp` lie in `leftker C`
and have rank 3 at every one of the 72 fibers. This is (K.8): six
normal forms \(\to\) four left-kernel conditions \(\to\) three
independent residual rows. It explains why there are three \(g\)’s
rather than four. It does **not** explain \(13\to 11\).

Off-`a00pp` NF polynomials are not in the repo (8.S8 notes they live
in session scratch). Independent recompute of `nf_rank=5` is only for
the three `a00pp` payloads. The 72-fiber `nf_rank` field is the
agent’s own recording. That gap does **not** touch \(g\)-independence,
which is read from `g_rows`.

### A.3 Independent recompute of \(g_1,g_2,g_3\) independence (Sol’s theorem 2.1)

`a00pp` at \(p=105337\) matches (K.4) coefficient-exactly, including
the square \((x_{57}-x_{65})^2=(1,-2,1)\) with \(-2\equiv 105335\).
The same private-monomial argument as Sol §2: a constant combination
\(ag_1+bg_2+cg_3\) supported on standard monomials has coefficients
\((a,b,c)\) on \(x_{57}^2 uW_1^2\), \(x_{57}^2 uW_2^2\), \(x_{70}\).
Those three coefficients are 1 in every atlas `g_rows` string and in
the 200257 `a00pp` comment lines of
`directionb_det23_p200257.rows.txt`. Hence \(a=b=c=0\) in all 73
tested specializations.

Atlas field census, both primes, 36 fibers each:

- unique structural signature
  `{(3, 2, 5, 1, 13, 11, 'NONEMPTY', 0)}` for
  `(cond_dim, rankC, nf_rank, kernel_dim, dim I21, dim J23, verdict, #anomalies)`;
- `rank w = 3` on all 72 `w_vectors`;
- square \((1,-2,1)\) on both pole rows, all 72;
- 0 private-monomial failures, 0 rank-\(\langle g\rangle\ne 3\) failures.

200257 `a00pp`: \(g_1,g_2,g_3\) as in the det23 rows file, cross term
\(200255\equiv -2\), private coefficients 1, three-term rank 3.

**EXACT MODULAR THEOREM 2.1, as a statement about constant-linear
independence of the three displayed residual rows, is CONFIRMED.**
The parenthetical “and in the third-prime `a00pp` payload” is
confirmed. The 72-fiber claim does not require a characteristic-zero
identity; Sol does not claim one.

### A.4 Character template (K.10)--(K.11): CONFIRMED, 864/864

From `a00pp` fiber data the two extractions of \(r\) agree
(\(A_1^3\equiv 3+r\) and \(A_2^3\equiv 3-r\)), \(r^2\equiv 3\),
\(2h_{32}^2\equiv 3\), and the smaller primitive cube root of 1 is
\(\omega=15094\) at 105337 and \(\omega=13168\) at 105673.

Formula (K.10) as written, evaluated in \(\mathbf F_p\) with the
fiber’s \((A_1,A_2,h_1,h_2)\), matches every atlas `g_rows`
coefficient at every fiber: 0 template failures on 72 fibers. The
72 × 12 term-count is 864. Grading:

- \(g_3\) takes exactly 3 values, constant on \((j-i)\bmod 3\)
  (12 fibers each);
- \(g_2\) takes exactly 6 values, one per \((j,s_2)\), independent of
  \(i\) and \(s_1\) (6 fibers each);
- \(g_1\) takes exactly 18 values, one per \((i,j,s_1)\), independent
  of \(s_2\) (2 fibers each).

Covariance cannot cause a constant relation inside a fixed fiber,
because the rows are independent inside every fixed fiber. Sol §4 is
right: the grading is transport, not redundancy.

### A.5 8.S6 correction entry (required)

Yes. The JSON is already correct; the prose is not. A consumer who
reads 8.S6 / notes.md / 8.S8 “one-dependency anomaly” as a linear
relation among \(g_1,g_2,g_3\) will reopen a closed linear-algebra
question and will mis-count the conormal nullity.

Suggested replacement for the 8.S6 anomaly sentence and the matching
witnesses-JSON `anomaly` field:

> The six reduced compatibility normal forms have rank 5 (one
> constant syzygy, kernel vectors prime-dependent; this is the
> rank-\(C=2\) “four becomes three”). The three residual rows
> \(g_1,g_2,g_3\) are constant-linearly independent (`cond_dim=3`,
> private monomials \(x_{57}^2 uW_1^2\), \(x_{57}^2 uW_2^2\),
> \(x_{70}\)) and cut maximum dimension by two, not three
> (\(13\to 11\)). That dimension defect is not a constant-linear
> relation among the three \(g\)’s. A rank-1 conormal span of three
> classes has nullity two. Cross-prime identity is of the signature
> \((3,3,5,1,2,13,11)\), not of one integer coefficient vector.

8.S8’s “one-dependency anomaly is FAMILY-WIDE” should be rewritten
the same way: family-wide is the signature, not a linear dependence
among the \(g\)’s.

No other 8.S6 factual claims (dim 11, 6 witnesses, reconstruction
tiers, fail-closed experimental \(e\)) are in scope for this
correction. Do not touch 8.S7.

### A.6 Replacement mechanism: structurally the right kind; certificates unbanked

Once constant-linear dependence is dead, three independent equations
on an equidimensional 13-fold would drop dimension by 3. They drop
maximum dimension by 2. The remaining explanations are: the three
rows fail to be a regular sequence on the top components, and/or
\(I_{21}\) is not equidimensional and the top components are killed
or missed by a different mechanism than a third independent equation
on one 13-fold. Sol’s (K.1)--(K.3) is exactly that: two
quotient-torsion syzygies, \(q\) a zerodivisor, residual ideal
principal on a 12-dimensional \(q\)-open stratum.

**What this audit could check without a Gröbner engine.**

1. The `a00pp` ratios \((\lambda,\mu)=(29311,42896)\) at 105337 and
   \((101767,105528)\) at 105673 are the same numbers
   `sol-round5.md` §2.2 measured as conormal ratios
   \([dg_2]/[dg_1]\), \([dg_3]/[dg_1]\) at all six witnesses per
   prime. That is independent corroboration of the *ratios*, not of
   the annihilator \(q\).
2. Sol’s tables (K.15)--(K.16) are internally consistent with the
   atlas \(\omega\): \(\lambda(\delta)=\lambda_{00}\omega^{-\delta}\)
   and \(\mu(j)=\mu_{00}\omega^{j}\) hold at both primes. The tables
   themselves are Sol’s computation; they are not in the atlas JSON.
3. Displayed \(q_p=x_{70}(x_{65}-x_{57})+a_p(x_{54}-x_{63})+b_p(x_{59}-x_{66})\)
   evaluated on the 12 banked D23 witnesses reproduces (K.18)
   entrywise, all 12 values nonzero. Witnesses lie in \(D(q)\).
   Several have \(\Delta=x_{57}-x_{65}=0\) but not the full \(H\)
   slice \((x_{57}=x_{65},\,x_{54}=x_{63},\,x_{59}=x_{66})\), matching
   Sol’s claim that neither coarse \(Q\)/\(L\) label is the source
   and that \(q_0\) vanishes identically only on \(H\).
4. The 12 seed-2026 D21 fiber points in
   `cases/directionb_fiber_points_p105337.txt` all have \(q=0\), and
   all have \((g_1,g_2,g_3)\ne 0\) and \(g_2\ne\lambda g_1\),
   \(g_3\ne\mu g_1\). The D23 witnesses are in \(V(I_{21})\) with
   \(q\ne 0\), so \(q\) is not identically zero on \(V(I_{21})\).
   Together this is consistent with “every 13-dimensional component
   lies in \(q=0\), and \(q\) is a zerodivisor, not a generic
   equation.” It is not a proof: twelve rational points are not a
   primary decomposition. It also makes the syzygy test at those
   twelve points vacuous (\(q\cdot(\cdots)=0\) because \(q=0\)).

**What this audit could not check, and is not in the repo.**

- \(\mathrm{NF}_{G_{21}}(q_p(g_2-\lambda_p g_1))=0\) and the twin for
  \(g_3\). Degree-\(\le 2\) map \(\Phi\): 227 standard monomials,
  681 columns, rank 673, nullity 8, factorization into four \(q_j\)
  times two triples. No matrix, no \(q_1,q_2,q_3\), no kernel basis
  is banked.
- Saturation table (K.19): four LT hashes
  `e50a85c583a44133`, `07480ceeed3f95d4`, `b2f63c3e065506bf`,
  `a14bcb6f3bad67ae` occur **only** in `sol-conjecture-k.md`. No
  GB, no `.out`, no row counts other than the already-banked 397 and
  509. The claim “all 36 fibers at \(p=105337\) have the same
  saturation dimensions, basis sizes, and leading-term hashes as
  `a00pp`” is an unbanked computation. K-FAMILY-SAT (35 fibers at
  105673) is already labelled conjecture; the 36-fiber 105337
  saturation claim is labelled proved and still has no artifact.
- Irreducibility / reducedness / uniqueness of \(K\): Sol withholds
  these. Keep the withhold.

**Implication chain, granting the unbanked identities.** If (K.1)
holds in \(R_p\), then on \(D(q)\) one has \(g_2=\lambda g_1\),
\(g_3=\mu g_1\), hence \((J_{23})_q=(I_{21}+(g_1))_q\). If
\(\dim(I_{21}+(q))=13\) and \(\dim(I_{21}:q^\infty)=12\), then \(q\)
is a zerodivisor and every 13-dimensional component lies in \(q=0\).
If \(\dim(J_{23}+(q))=10\), every 11-dimensional D23 component meets
\(D(q)\). Differentiating (K.1) at a point of \(V(J_{23})\cap D(q)\)
kills the \(dq\) terms and gives conormal rank \(\le 1\) on that
open. That chain is algebraically correct. It is not a theorem in
this repository until the identities and dimensions are banked.

**Rating of the replacement.** As an explanation of \(13\to 11\), it
is the only remaining modular source once constant-linear dependence
and “rank \(C=2\) by itself” and “mod-3 grading by itself” are
separated (Sol §7 is sharp on those three). As a proved mechanism:
**GAPS**. Do not promote “EXACT MODULAR” for (K.14) or (K.19). The
honest payload-level theorem is 2.1 plus (K.8)--(K.11). Section 0
item 1 (“Proved modular source: zero-divisor torsion … already in
\(S/I_{21}\)”) overclaims relative to what is in the repo.

D25/all-depth: Sol withholds an unconditional bound and splits two
conditional recurrences (K-DEPTH-P vs K-DEPTH-S). That withhold is
correct; `cases/d25_reduce.py` is still a recovery stub. Do not let
anyone read (K.24) or (K.25) as a theorem.

### A.7 Target-(A) ledger

| claim | verdict |
|---|---|
| no constant-linear dependence among \(g_1,g_2,g_3\), 72 fibers + 200257 `a00pp` | **CONFIRMED** |
| 6 NF rows rank 5, (K.9) kernels, rank \(C=2\), “four becomes three” | **CONFIRMED** |
| (K.5) signature uniform on both atlases | **CONFIRMED** as JSON+`g_rows`+`w_vectors`; `nf_rank` off-`a00pp` not re-derived from polynomials |
| (K.10) template, 18/6/3 classes, 864 coefficients | **CONFIRMED** |
| grading does not cause the dim drop | **CONFIRMED** |
| rank \(C=2\) does not cause the dim drop | **CONFIRMED** (it produces three independent rows) |
| 8.S6 “one dependency among the g’s” as constant-linear relation | **REFUTED**; correction required |
| (K.1) torsion syzygies as identities in \(R_p\) | **GAPS** (ratios and \(q(P)\) checks pass; NF identities unbanked) |
| (K.19) saturation \(13\rightsquigarrow 12\to 11\) | **GAPS** (hashes unbanked; 36-fiber 105337 run unbanked) |
| K-SOURCE / K-DEPTH-P / K-DEPTH-S / D25 forecast | already **CONJECTURE**; leave them |

---

## B. G5 BLOCKED

### B.1 What would make BLOCKED false

A usable consequence of FC5, or of FC5 plus the already-proved
`M=1` depth theorem, or of NF-M, that forces a finite bound on
\(\sum_P a_P b_P/\nu_P\) at fixed Sigray type, even a nonsharp one.
Candidates hunted:

1. FC5 is secretly a conservation law for pole mass.
2. \(\Phi_s(w,M)=wM^2/(sM-1)\) is a one-step monotone potential.
3. Some other memoryless \(V(w,M)\) that equals pole mass on pole-law
   states is monotone on coefficient-solvable charts.
4. Depth-closure supplies a cross-rung bound on entries.
5. NF-M supplies a bound on schema parameters, hence on sheets.
6. FC5 plus the handshake inverts, recovering a bound on incoming
   mass from the emitted pair.
7. The full emitted frame \((\bar\kappa,d_p,d_q,\nu)\), not just
   \((w,M)\), is bounded by present theorems, and Prop 3’s scale
   sits in that frame.

All seven fail. Details below. BLOCKED stands.

### B.2 FC5 is a local frame identity. CONFIRMED.

Reconstructed (1.1) matches the discharged lemma FC5-D at
`TOWER-TD11.md:707` and `cases/td11_census.py:1064-1120`:

\[
w_G=\frac{\bar\kappa_G(d_q-1)}{\nu_G d_q},\qquad M_G=\gcd(d_p,d_q).
\]

The census already checks the cylinder identity
`emitted_w(6*nu+3, nu, 2*nu+1)==6` for \(\nu=2..59\). That is the
same BB2 family Sol uses in §4.2. FC5 contains no incoming leaf
count, no incoming \((a,b,\nu)\)-mass, no charge, no proximity, and
no cross-chart relation. \(M_G\mid\sum\mu_e\) is scoped to
\(\varepsilon=0=k\) at `BOOK-OFFAXIS.md:328-331`; Prop 3 has \(k=1\),
so that divisibility is correctly *not* applied (and would have
falsely killed the family: \(M_1=3\nmid\mu=2\)).

Sol’s “PROVED: FC5 has no incoming-mass term” is exactly the content
of (1.1). There is no hidden mass term in the certified identity.

### B.3 \(\Phi_s\) is the exact pole-mass interface, and it is not a telescope. CONFIRMED.

From `SHEET6-TDUNIFORM.md:44-71` and `SHEET6-MULTIPOLE.md` AF3:
\((D,D_g)=a(\alpha,\beta)\), \((P,P_g)=b(\alpha,\beta)\), \(M=b\),
\(\bar\kappa=as\), \(\rho=a/b\). Then
\(w=a(sb-1)/(b\nu)\) and
\(\Phi_s(w,M):=wM^2/(sM-1)=ab/\nu\). Combined with Prop 5.8 this is
(2.2). Exact at poles. At an internal chart it is only a candidate.

Residue-A decrease, \(s=5\): two poles \((w,M)=(2,1)\) total mass 1;
IIa \((r,\nu,l)=(2,3,1)\) emits \((3/2,2)\) of mass \(2/3\). Decrease
\(1/3\). Recomputed.

BB2 increase: two B-inputs mass \(4/3\); for every \(N\ge 2\),
\((\bar\kappa,d_p,d_q)=(6N+3,4N+1,2N+1)\), \(M'=1\), FC5 gives
\(w'=6\), \(\Phi_5(6,1)=3/2\). Increase \(1/6\). Recomputed for
\(N=2..19\). Type `b=-a` is the NF-M cylinder at `NF-M.md:175-178`.
The later CAP-DEN death of the chart does not restore monotonicity of
FC5.

Both endpoint states are type-\((2,3)\) pole-law states:
\((2,1)\leftarrow(a,b,\nu)=(1,1,2)\),
\((3/2,2)\leftarrow(1,2,3)\),
\((6,1)\leftarrow(3,1,2)\). Any memoryless \(V(w,M)\) that equals
pole mass on pole-law states takes these three values, and so obeys
neither one-step inequality uniformly. The no-telescope statement is
proved as an identity of this relaxation, not as a claim about
globally glued trees.

Proposition 2 (nonsaturated all-\(\mu=1\) IIa dissipates \(\Phi_s\)):
the coefficient \(A_R=D(sg-1)-g(s-1)\) is positive for \(g=1,D\ge 2\)
and for \(g\ge 2,D\ge 2\), and the \(R=1\) lower bound
\(gs(D-2)+D(g-2)+2g+s-1\) (resp. \((s-1)(D-1)\) at \(g=1\)) is
positive on the lattice checked. Dissipation is the wrong direction
for an *upper* bound on leaf mass.

### B.4 Proposition 3 family: arithmetic CONFIRMED; realization correctly withheld

For \(A=30t+5\), \(N=9A-2\), \(n=13A-3\), type \((2,3)\),
\((a,b,\nu_0)=(A,2,3)\):

- pole laws, \(\Lambda=td=4A\), \(M_0=2\), N1
  \(\gcd(5A,3)=1\) because \(A\equiv 2\pmod 3\);
- Sigray entry \(\nu_0\mid\beta\) and \(\nu_0\mid(b\alpha-1)\);
- IIa with \(\mu=2\mid M_0\), \(k=1\Rightarrow l=0\), child \(\nu_1=N\);
- ratio \(d_p/d_q=2(\rho_0+n)/(\bar\kappa_0+n)\) holds identically;
- transport \(D_1=2N\), \(P_1=6N\), \(\bar\kappa_1=6A-1\),
  \(M_1=3\), child N1 via \(2N-3(6A-1)=-1\);
- FC5 \(\Rightarrow (w_1,M_1)=(2/3,3)\) **constant in \(A\)**;
- pole mass \(2A/3\to\infty\);
- characteristic gcds for \(A=30t+5\): \(\gcd(3N,22A-6)=1\),
  \(\gcd(3N,9A-3)=3\), checked \(t=0..20\);
- AF2 gap \(=3A-1\le 4A-3=td-1-\psi\) with \(\psi=2\), \(R=3\);
- case-IV numerical gates (k),(l),(m) hold, \(M_{\mathrm{root}}=3\)
  satisfies the single-pole Prop 8.4 veto \(M\ne 1\) and the
  divisibility \(M_{\mathrm{root}}\mid M_1\);
- pole Wronskian \(2p_0 q_0'-3p_0'q_0=\frac98 U_0^3\) by direct
  expansion; \(p_0,q_0\) squarefree and coprime for \(U_0\ne 0\);
- child NF-M reduction becomes constant at \(V_1/U_1=(N+2)/(N-1)\),
  \((\widehat Q-1)!=1\) for every \(A\).

The family lives on \(M=2\to 3\), outside `SHEET6-DEPTH.md:416-422`.
It uses H1-tier Prop 9.3 arithmetic (`SHEET6-CAMPAIGN.md:69-75`,
foundations audit pending). That does not rescue BLOCKED: the
obstruction is to the *displayed numerical package the campaign
actually runs*, which includes that H1-tier arithmetic. If Prop 9.3
were later refuted, the campaign’s local gates would change and the
family would have to be rebuilt; it would not create a proof of
TD-BOUND from FC5+depth+NF-M as presently stated.

Sol withholds global Eggers--Wall gluing, coefficient transport,
algebraization, and the Keller condition. Keep the withhold. The
family is not a counterexample. It is a scale-loss witness for the
scalar relaxation after assigning \(\lambda\) its permitted AF2
lower bound. That is the right quantifier for “these bookkeeping
consequences do not force a bound.”

Section 6 two-pole IIa schema: for odd \(A\ge 3\), two poles mass
\(A/2\) each, \(td=6A\), merge \((r,l,\nu_G)=(2,1,2A-1)\) emits
\((w,M)=(3,2)\) independent of \(A\). Ratio and integrality hold.
The local coefficient formula (6.4) is the L1-IIa rigid solve at
`SHEET6-L1.md:268-272`. Same moral: a coefficient-solvable
multi-arrival merge can send unbounded incoming pole mass to one
constant emitted pair. Single-pole Prop 3 is already fatal to an
emission-only proof; section 6 is completeness, not load-bearing.

### B.5 The reconstruction that is *not* a bound (the FC5 miss that was checked)

Prop 3’s child frame is not constant: \(\bar\kappa_1=6A-1\),
\(\nu_1=N=9A-2\), \(d_p=3N\), \(d_q=2N+1\) all scale with \(A\).
In particular \(A=(\bar\kappa_1+1)/6\) is a rational function of the
child frame. If a later theorem bounded that frame, it would bound
pole mass. **FC5 does not emit the frame; it consumes the frame and
emits \((w,M)\).** Depth-closure does not bound \(\kappa_i\)
(`SHEET6-DEPTH.md:128-138`). NF-M’s locality theorem requires the
same type *and the same emitted frame* (`NF-M.md:108-116`); the BB2
cylinder is the exact quantifier witness: one type `b=-a` for every
\(N\), infinitely many tagged \((N,\mathrm{type},\mathrm{frame})\)
triples, constant FC5 pair \((6,1)\). Sol §8 is the right answer to
“use the frame, not just \((w,M)\).” There is no present theorem
that bounds the frame parameters at \(M\ge 2\).

Depth-closure cannot restore coercivity for four independent reasons,
all printed in `SHEET6-DEPTH.md` and `SHEET6-DEPTH-REVIEW.md`: scope
is the `M=1` axis; \(W(w_0)\) is per fixed entry; \(\kappa_i\) is
uncontrolled; the representative bound is on the cumulative jump-cell
menu, not on endpoint frames. Prop 3 lives on \(M=2\to 3\).

NF-M cannot restore coercivity: \((\widehat Q-1)!\) counts decorations
of a *fixed* zero-dimensional schema. Prop 3 has \(\widehat Q=2\)
and one type for every \(A\). The unbounded parameter is the schema
itself.

### B.6 21-of-22 census, mismatch energy, iteration, cofinality

The 21-of-22 off-axis violation frequency is a construction effect
(\(q>\alpha\) or off-axis \(q=\alpha\)), as already computed in
`sol-tdbound-review.md:211-257`. It is not evidence of a conservation
law. Sol is right to demote it.

Mismatch-energy identity (10.1): from \(C^2=D^2=0\) and \(C\cdot D=td\)
on a common resolution of the two pencils,
\(\sum(R_p/\alpha-S_p/\beta)^2=2\,td/(\alpha\beta)\). Algebraically
correct; no Keller hypothesis beyond generic finiteness. Combined
with Prop 5.8 this is (10.2). KME-2 is exactly TD-BOUND in those
coordinates, not a strictly weaker lemma. Calling KME-2 “the missing
lemma” would be a false reduction: it restates the prize. Sol says
this (“not an independent mechanism lemma”). Keep it diagnostic.

PCC: \(h_p=\min(\lfloor R_p/\alpha\rfloor,\lfloor S_p/\beta\rfloor)\)
satisfies \(R_p S_p\ge\alpha\beta h_p^2\) because
\(R_p\ge h_p\alpha\) and \(S_p\ge h_p\beta\). Summing and using
\(I_\infty=\sum RS=B^2\alpha\beta-td\) gives \(td\le\alpha\beta\) once
\(\sum h_p^2\ge B^2-1\). So PCC is a genuine *sufficient* lemma. It
is unproved. The needed weighted/Laurent-to-projective transport,
proximity accounting, distinct-center coverage, and no-double-counting
theorem are correctly listed as absent. Hardness 8.5/10 is a
judgment; the statement is precise.

Iteration (Prop 4): \(td(F^k)=d^k\) for a nonautomorphic Keller map
with \(td(F)=d>1\) is the tower formula for
\([K:(F^k)^*K]\). A universal absolute bound \(td\le N\) for *every*
plane Keller counterexample is therefore equivalent to JC2, not an
intermediate rung. The published \(td\ge 6\) (`REDUCTION.md:340-351`)
makes the premise \(d>1\) automatic here. This does **not** obstruct
a bound on a selected globally minimal counterexample. Sol’s
quantifier correction is mandatory. G5 as actually posed is
type-relative TD-BOUND \(td\le\alpha\beta\), which is compatible with
iteration (the type of \(F^k\) may grow). The iteration paragraph is
a correction of principle for a *universal* bound, not a proof that
TD-BOUND is equivalent to JC2.

Cofinality: `TDBOUND.md:97-103` claims that TD-BOUND plus “finiteness
of the GGV \((m,n)\)-list” makes the sheet ladder finite.
`REDUCTION.md:225-267` already records that GGV Algorithm 8 is finite
only after an explicit input bound, and that an exhaustive finite GGV
catalog is **NOT ESTABLISHED**. Sol’s CONJECTURE SC is the missing
type cap for a *selected* pair. The cofinality sentence in TDBOUND.md
is not a theorem. Correction accepted.

### B.7 The missing lemma, stated precisely

Sol names four statements. They are not interchangeable.

**SP (single-pole cap).** If a one-pole Sigray configuration is
globally realizable by a polynomial Keller pair, then \(ab\le\nu\).

This is exactly TD-BOUND restricted to one pole, because
\(td=\alpha\beta\,ab/\nu\) there. It is necessary for any
merge/emission proof: a theorem for every configuration cannot omit
the sector with no multi-leaf merge. Prop 3 satisfies the current
local rules and violates SP by an unbounded factor. FC5 cannot prove
SP: after the first chart it has already forgotten the scale
(\((w,M)=(2/3,3)\) constant). Hardness “8/10” is optimistic if read
as “a lemma.” SP is one-pole JC2 in Sigray coordinates. Isolate it
as the smallest *necessary sector test*, not as an available tool.

**KME-2.** \(\sum_p(R_p/\alpha-S_p/\beta)^2\le 2\) on a common
resolution. Equivalent to TD-BOUND, \(\sum ab/\nu\le 1\), and
\(\Delta^2\ge -2\). Diagnostic coordinate change, not a reduction.
The exceptional lattice does not imply it: multiples of a root have
arbitrarily negative square. Correct.

**PCC.** \(\sum_p h_p^2\ge B^2-1\) with
\(h_p=\min(\lfloor R_p/\alpha\rfloor,\lfloor S_p/\beta\rfloor)\).
Sufficient for TD-BOUND, strictly stronger, concrete. Unproved.
This is the only statement on the list that could actually *be* a
lemma implying the prize rather than renaming it.

**KME-finite.** A type-wise bound with some
\(C_{\alpha,\beta}<\infty\). Still new global geometry; Prop 3 shows
it is not in the local laws even for type \((2,3)\). A universal
absolute \(C\) independent of type would hit the iteration
obstruction; Sol’s statement is per type, which is the right
quantifier.

**What an emission proof must import.** At least SP, because the
one-pole sector has no merge to compare. SP does not follow from
refining FC5. A proof of the full bound must control normalized
mismatch energy at divergence centers (KME-2 / PCC or something that
implies them). That information is not in \((w,M)\).

No present FC5 consequence was missed that would prove SP, KME-2,
KME-finite, or even a type-\((2,3)\) bound on \(A\) in Prop 3.

### B.8 Target-(B) ledger

| claim | verdict |
|---|---|
| FC5 = (1.1), no incoming mass | **CONFIRMED** |
| \(\Phi_s=wM^2/(sM-1)=ab/\nu\) at poles; (2.2) | **CONFIRMED** |
| \(\Phi_s\) nonmonotone on coefficient-solvable charts | **CONFIRMED** (both signs) |
| Prop 2 dissipation, wrong direction for an upper bound | **CONFIRMED** as IIa-nonsaturated arithmetic |
| Prop 3 unbounded arithmetic-schema family, constant FC5 output | **CONFIRMED** as arithmetic; realization withheld (correct) |
| depth-closure not coercive in `td` | **CONFIRMED** (printed scope) |
| NF-M not coercive in `td` | **CONFIRMED** (quantifiers in NF-M.md + BB2) |
| BLOCKED as a verdict on FC5+depth+NF-M (plus displayed numerical gates) | **CONFIRMED** |
| a usable FC5 consequence forcing any finite type-wise bound | **not found** |
| SP as stated | precise; necessary for emission proofs; equivalent to one-pole TD-BOUND; unproved |
| KME-2 as stated | precise; equivalent to TD-BOUND; not a lemma |
| PCC as stated | precise sufficient lemma; unproved |
| universal absolute `td<=N` ≡ JC2 | **CONFIRMED** |
| TD-BOUND does not make the book ladder cofinal | **CONFIRMED** (GGV catalog not absolute) |
| Prop 3 as a Jacobian counterexample | Sol does not claim this; do not promote |

---

## Corrections this audit requires (no edits made)

1. **8.S6 / 8.S8 / witnesses JSON `anomaly` / notes.md “one
   dependency among the g’s.”** Replace with the disambiguation in
   A.5. Sol is the surviving interpretation of the linear algebra.
   The agent’s rank-5 and \(13\to 11\) numbers stay.
2. **`sol-conjecture-k.md` §0 item 1 and §6 “the full K mechanism is
   proved on the complete first-prime atlas.”** Demote until
   \(q_j\), \(\Phi\), and the (K.19) GBs/hashes are banked artifacts.
   Payload-level theorem = 2.1 + (K.8)--(K.11) + witness \(q(P)\ne 0\).
3. **`TDBOUND.md:97-103` cofinality sentence.** Already flagged by
   Sol; it is not a theorem.
4. Do not open a G5 proof lane from FC5, depth-closure, or NF-M as
   presently stated. The missing import is global
   Keller/proximity/mismatch information (PCC, or anything that
   implies KME-2), with SP as the mandatory one-pole sector test for
   any emission-based attempt.

No other file was changed. No git.
