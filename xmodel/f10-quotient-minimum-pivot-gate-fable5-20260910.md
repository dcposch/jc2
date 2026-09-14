# FIRST hostile gate: minimum-degree pivot proof and three static deltas

Status: FIRST independent gate of charged report e72bc42e (astra) and its
three code deltas. STATIC/DOCUMENTARY ONLY. No Python, CAS, AST, compile,
import, fixture, test, worker, runtime, ledger, corpus, Git or network read.
First action 03:22:27 UTC; controlling stop 03:36:00 UTC (equal to first
action plus 14 minutes, rounded); reserve from 03:34. Basis 0d39df3c is
provenance, not a price.

## 1. Verdict

- A CONFIRMED. The minimum nonzero projected-degree rule (constants
  included, -1 only when all nine projections vanish, first-index ties,
  both split children rescanned) is sound for the accepted UNIT and
  SEPARATOR read-back on all 217 rows and 1638 columns. No field or
  reducedness assumption on the T-quotient is used. All six manual
  controls recompute as stated.
- B CONFIRMED. All three diffs regenerated here with `diff -u` are
  byte-identical to the charged diffs (SHA ca811d65, b4110b12, 511e95f5).
  newsolver 961e22e6 = oldsolver 58cdc472 with one removed line replaced
  by one selection line and two comments (48 bytes out, 219 in, +171 bytes,
  332 to 334 lines). Each caller changes exactly one solver literal.
- C CONFIRMED WITH QUALIFICATION. The stale documentary field
  `source_sha256.solver.py = 58cdc472` in plan ce193898 is not consumed by
  the charged generic caller or by generic_controls.py. It is hash-pinned
  whole (ce193898 unchanged) and so must stay byte-identical. probe.py
  receives the plan path but is not a charged input; its treatment of that
  field is unverifiable here (GAP, see section 6).
- D Smallest actual defect found: none in the mathematics or the three
  hunks. The only changed observable outside the certificate witness is the
  documentary trace fields `degree`/`pivot` per leaf, which now record the
  minimum. No charged consumer reads them (generic_controls.py line 296
  trusts no trace); the unchanged checker is uncharged and unverified here.

Nothing here is an executed result. No actual degree, rank, height, speed,
memory or source claim follows. No rerun, cap raise or JC2 is authorized.

## 2. Custody

All 15 snapshots in the read-only inputs directory hashed BEFORE reading
and matched the task list exactly; pins and the three regenerated-diff
hashes are in box/f10-quotient-minimum-pivot-gate-fable5-20260910/
input-pins.sha256. Own report and box were absent before writing. Read
WHOLE: newsolver.py, the astra report, ROOT-CARD, the plan, all three
diffs. Old solver bytes are covered as newsolver minus the single hunk.
Caller coverage: the exact one-line hunks plus the accepted old snapshots
(54c55be3, a7c0cf17 byte-identical to accepted 17zk/17zm); I read the
binding regions (generic lines 40-62 and 228-300; actual lines 158-215)
and grepped both whole files for plan/solver/source_sha256 use. I did NOT
read every caller line myself; that coverage rests on the accepted
premises plus the regenerated diffs. generic_controls.py was grepped whole
and read at lines 388-421; the 17zg/17m gates were not re-read (accepted).

## 3. A: proof of the selection rule

Setting (accepted interface): B = Q[v]/(p), p monic degree 7 squarefree
(line 20), so B is a product of fields, finite etale of rank 7; C = B[T];
nine f_i and q of T-degree <= 5 (lines 23, 30); b = q^5, deg b <= 25.

1. Leaf structure is rule-independent. project() trims exactly, so
   `if f` is nonzero-ness; min over nonempty with default -1 gives -1 iff
   all nine vanish, the same set as the old max < 0. The chosen pivot has
   degree d >= 0 and nonzero leading coefficient c reduced mod p_a, so
   gcd(c,p_a) is 1 or proper (0 < deg g < e); squarefreeness gives
   g coprime to h = p_a/g. On the h child c is a unit (a common factor of
   c and h would divide g); on the g child the leading term dies and both
   children rescan all nine (lines 92-99). Each split lowers ranks with
   sum 7, so <= 7 leaves, <= 6 splits, <= 13 visits: the requires at
   lines 94, 113, 118, 120, 124 never fire spuriously under either rule.
2. d = -1 leaf. b = 0: zero cofactors. b != 0: the functional
   x -> coeff_l((pi_a(x)_k) mod p_a)/beta (lines 153-162) is Q-linear on all
   217 coordinates, kills every column T^j v^l f_i because pi_a(f_i) = 0,
   and takes value beta/beta = 1 on q^5. Independent of the rule.
3. d = 0 leaf (new reach). The pivot is a nonzero constant with unit c;
   h_p = c^{-1} b, others 0, gives sum h_i f_i = b with len <= 26 (line
   280). Other generators may now be nonconstant; the identity ignores
   them. Correct.
4. 1 <= d <= 5 leaf. R_a = B_a[T]/(fhat) is free over B_a with basis
   1..T^{d-1}, Q-dimension e*d. Multiplication by T satisfies
   fhat(T) = 0 on R_a (Cayley-Hamilton on the regular representation), so
   the B_a[T]-span of the images of f_i (i != p) equals the B_a-span of
   T^j f_i for j < d, which is the Q-span of the 8*e*d columns (lines
   189-198). No bound on deg f_i relative to d is used. R_a need not be
   reduced; nothing above uses reducedness.
5. UNIT read-back. If b_bar lies in the column span, the RREF particular
   solution (free variables 0, lines 240-243) gives h_i of degree <= d-1,
   deg(h_i f_i) <= d+4 <= 9 <= 25, so N = b - sum h_i f_i has degree
   <= max(25, d+4) = 25, monic division is exact (line 260), deg(N/fhat)
   <= 25-d, and h_p = c^{-1}(N/fhat) satisfies h_p f_p = N for the RAW
   generator; len <= 26-d (line 262) holds. The old 2d-1 estimate is not
   needed. CRT idempotents (lines 267-279) act only in v, so the nine
   global cofactors have T-degree <= 25; witness 9*26*7 = 1638 in the
   declared column order. Converse: any degree-25 certificate projects and
   reduces to a small solution on every leaf, so UNIT is complete.
6. SEPARATOR read-back. If b's column is a pivot, row k of the identity
   block is mu with mu*A = 0 and mu*b = 1 on the COMPLETE direct sum (all
   coordinates, including any outside the multiplier image). lambda(k,l) =
   sum over active leaves of mu_a(v^l T^k mod fhat_a) (lines 231-236, power
   iteration to k = 30) is Q-linear on 217 coordinates. Every column
   v^l T^j f_i, j <= 25: on leaf a either i = p_a (image c*fhat = 0) or the
   image lies in the ideal image = column span by item 4, for ALL j, so
   mu_a kills it. lambda(q^5) = sum_a mu_a(b_bar_a) = mu*b = 1. Non-active
   leaves are irrelevant to a separator. Complete: q^5 not in I forces
   either a d = -1 leaf with b != 0 or an active leaf with b_bar outside
   the span; d = 0 leaves have unit ideal.
7. Envelope. rows = sum e_a d_a <= 35, columns <= 280 (line 173) since
   d_a <= 5 under either rule.

Six manual controls, recomputed by hand (over Q; control 5 over Q x Q):
1. f1=T^5, f2=T, q=T: min picks index 1, d=1, fhat=T, target 0 mod T,
   all columns 0, solution 0, N=T^5, h2=T^4, len 5 <= 25. Correct.
2. f1=T^5, f2=1, q=T^5: min picks index 1 (non-first), d=0, h2=T^25,
   len 26 = 26-0 bound attained. Correct; old max rule would take d=5.
3. f1=2T, f2=T^5, q=T: d=1, c=2, h1=T^4/2; without the inverse 2T^5 != T^5.
4. f1=T^2, f2=1+T+T^3, q=1: d=2, C=Q[T]/T^2, span{1+T, T} = all, h2=1-T,
   N=T^2-T^3+T^4=T^2(1-T+T^2), identity (1-T+T^2)T^2+(1-T)(1+T+T^3)=1
   checked termwise. Mod-T shortcut gives 1-f2=-T-T^3, not divisible by
   T^2. Correct.
5. Q x Q, f1=(T,T^2), f2=(T^3,1): root min degree 2 at f1 with lc (0,1)
   = v mod v(v-1); g=v, h=v-1. g child: f1=T (not zero), f2=T^3, rescan
   d=1. h child: f1=T^2, f2=1, rescan d=0 at f2. Correct as stated.
6. all zero, q=0: zero UNIT. q=1: beta=1 at (k,l)=(0,0), lambda = that
   coordinate, value 1 on 1, kills all zero columns. An unfiltered min
   would return -1 whenever any single f_i vanished and emit a separator
   that does not kill the nonzero columns; the `if f` filter is essential.

## 4. B: literal deltas

Regenerated with `diff -u --label` from the charged old/new snapshots;
cmp against each charged diff: identical. Solver hunk at old line 97: one
`max(...)` line out; two comment lines and
`degree = min((len(f) - 1 for f in local if f), default=-1)` in. Line 103
tie-break unchanged. Generic caller: only `known['solver.py']` at line 238;
actual caller: only `known['solver.py']` at line 166. No transplant, CLI,
cap, env, authority barrier, source acceptance, checker, control or schema
line changed (diff exhaustively lists all differing lines).

## 5. C: targeted plan/harness compatibility

- generic_dispatch_batch.py reads the plan at line 264 and consumes only
  `plan['positive_cases']` (lines 56, 304) and `plan['negative_cases']`
  (lines 58, 316): output path inventory and expected branch/reason
  zipping. The string `source_sha256` occurs nowhere in either caller or
  in generic_controls.py. The runtime solver pin comes from the
  registration `file_sha256` vector checked against `known` (lines
  256-257) and, inside generic_controls.py, from `spec['file_sha256']`
  (lines 397-399) plus its own digest of the sibling solver.py (line 371),
  which the caller compares to `known['solver.py']` = 961e22e6 (line 290).
  So the stale plan field is documentary-only in the charged caller and
  harness; it neither refuses nor misbinds.
- The plan hash ce193898 stays in `known` (line 239) and in the receipt
  (line 326), so the plan body with the stale field must remain unchanged.
- Expected branches: UNIT/SEPARATOR is the membership q^5 in I, proved
  rule-independent in section 3, and no require can newly fire (item 1, 5,
  7). Receipt schema (8 positives, 4 negatives, fields at lines 280-281),
  the 217/1638 certificate schema (solver lines 132-140), the FROZEN import
  `from solver import generic_candidate` (controls line 420) with unchanged
  signature (solver line 12), and the receipt `solver_sha256` contract
  (controls 371, caller 290) are unaffected.
- actual_dispatch_batch.py does not read the plan; it hands probe.py
  frontier.json and runs solver.py unchanged (line 211).

## 6. GAPs and qualifications

- GAP[PROBE-PLAN-FIELD]: probe.py (pin 02913a1c, uncharged) receives the
  plan path (generic lines 269-270). Whether it reads
  `source_sha256.solver.py` cannot be decided from the charged inputs.
- GAP[CHECKER-TRACE]: the unchanged checker (122842e5, uncharged) is
  presumed by the 17zg premise to verify witnesses, not the trace; not
  re-verified here.
- Caller WHOLE coverage rests on accepted old snapshots plus exact diffs,
  not on a fresh full read of the two callers.
- Everything is static. The new solver has never been parsed or run;
  the accepted generic harness and actual runtime are not proved by this
  gate, and the astra report's own status line says the same.

<!-- BODY-END -->
