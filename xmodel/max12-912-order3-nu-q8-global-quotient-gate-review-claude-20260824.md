# Hostile review: max12 `(9,12)` corrected-Q8 global quotient gate

| Field | Value |
|---|---|
| Reviewer | claude (different-model hostile reviewer) |
| Date | 2026-08-24 |
| Report under review | `xmodel/max12-912-order3-nu-q8-global-quotient-gate-20260824.md` |
| Case under review | `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/` |
| Overall verdict | **CONFIRMED** (execution-side caveats in section 2, none charged to the artifact) |

Everything in the case directory, the charged report, and the frozen parents in
the executing chain was read in full byte-for-byte before any verdict: both
producer scripts, all four payloads, `MANIFEST.sha256`, `FREEZE.txt`,
`README.md`, `REGISTRATION.md`, the fibre compiler
`cases/max12_912_order3_fibre_20260824/order3_fibre.py`, the leaf-4 descent
replay and its payload and report, the Q8 normalization-jet replay, the
corrected Q8 formal-branch report, and the verdict lines of the three pinned
different-model reviews (formal branch, critical-value norm, leaf-4 descent:
all `CONFIRMED`).  No repository byte was modified other than the creation of
this file.

## 1. Charged hashes

```text
report          2102e5d730af7d9bd4a434a99ea9b7213cdf08016becd0e49061f5210ec0feaa
manifest        3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4
freeze          c34fff2b838ca4803872b709857ae7becb1751a7e1ce261c9fa8c7e6d8b46c97
replay          f0f52954bed71b65b9219fd497f7ea2bbe6652144c463ca06f03391b87957fdd
replay payload  d05eeb86d8c11b6463f25b18bff1a59b736a924bd3fcf619aaf23404f4e764a5
```

Cross-pin lattice verified by reading: the charged report, replay, and replay
payload hashes appear identically in `MANIFEST.sha256` (lines 1, 9, 10) and in
`FREEZE.txt`; the charged manifest hash equals `FREEZE.txt:manifest_sha256`;
`replay.py`'s `FILES` dict equals `MANIFEST.sha256` lines 4–8; the FREEZE
registration/readme/compiler/payload hashes equal manifest lines 2–8.
`quotient_compiler.py` pins the fibre compiler at `a4fdac5d…` — byte-identical
to the pin recorded independently by the normalization-jet replay — and both
`quotient_compiler.py` and `local_series.py` pin the leaf-4 descent replay at
`5dcb0a67…`.  The import chain is fail-closed: loading `local_series.py`
re-verifies every transitive parent hash before any mathematics runs.

## 2. Execution disclosure (reviewer-side, mandatory)

This review session has no shell: the Bash tool is absent and the Monitor
tool was permission-denied.  Consequently I could **not** byte-execute:

- `shasum -a 256 -c …/MANIFEST.sha256` and the sha256 of `FREEZE.txt`
  against the charged values;
- the end-to-end `replay.py | diff -u replay.json -` (including the two
  Singular `slimgb` runs);
- my independent probe.

The probe is staged at `/tmp/q8gq_probe.py` and performs, with no reliance on
any in-case PASS string: (1) exact random-rational-point verification of
`r_l(chart) = t^(l mod 2) * row_l` for all eight rows including both outputs;
(2) exact verification of the C\*-weights `wt(r_l)=12+l`; (3) the report
table and the 167-versus-230 monomial counts; (4) an independent re-run of
the `w^5` lift with fail-closed solves; (5) the `q0,q1` digest agreement with
the frozen leaf-4 payload; (6) the Padé falsifiers; (7) an exact rank over
`Q` of the full 48×25 `n,q` rectangle (which subsumes every `1<=deg<=4` box
unconditionally) and a third-prime (1000037) rank pass over every tested `Z`
bidegree box.  The maintainer should run the two commands of report §7 plus
`python3 /tmp/q8gq_probe.py`.

The verdict below therefore rests on: complete source reading, hand
re-derivation of every charged identity, the internal consistency of the
frozen cross-pinned attestations, and the three CONFIRMED parent reviews.
Every claim marked "frozen" below is attested by pinned bytes I read; every
claim marked "hand-verified" I re-derived independently in this review.

## 3. Charge 1 — the exact parity quotient

**Involution derivation (hand-verified).**  With `wt(a_i)=9-i`, `wt(k)=6`,
`wt(p)=2` (the leaf-4 report freezes `wt(a0)=9, wt(p)=2, wt(r8)=20`, matching
my derivation), the slice `p=1` of the `p!=0` cone meets each `C^*` orbit in
exactly the two points `lambda=±1`, and `lambda=-1` is precisely
`f(z)->-f(-z)`: it negates `(a0,a2,a4,a6)`, hence `(q_c,x0,x2,x4)`, and fixes
`k,x1,x3,x5,p`.  The report's involution is the residual deck action of the
geometric `p=1` chart — exact, not chosen.

**Substitution (hand-verified).**  From `K=z^3+z+q_c` and
`f=K^3+sum x_i z^i`: `a0=t(1+wc^3)`, `a1=x1+3wc^2`, `a2=t(3c+d2)`,
`a3=1+x3+3wc^2`, `a4=t(6c+d4)`, `a5=3+x5`, `a6=3tc`, `a7=3`, `k=0`.  These
are exactly the `normal_images`/`invariant_images` of
`approximate_quotient_polynomial`.  Each monomial carries
`t^(normal degree)`; the compiler checks `normal_degree ≡ l (mod 2)` for
every monomial of every row and raises on failure, so the division of odd
rows by `t` is an exact exponent shift with a fail-closed character
certificate, never a floor.  The mod-2 character is itself the `lambda=-1`
shadow of `wt(r_l)=12+l`, and the compiler independently enforces the mod-3
Kummer shadow on the raw tails.

**Reversibility (hand-verified).**  On `w!=0` the two lifts `t=±sqrt(w)`
are exchanged by the involution and satisfy the eight original tail
equations iff the point satisfies (2.2); the quotient map is 2:1 étale over
the punctured chart.  The localization (3.1) inverts `w`, so the charged
punctured branch lies entirely in the chart where the substitution is
reversible.  Correct as stated.

**Outputs (hand-verified).**  `wt(r6)=18=wt(p^9)` and `wt(r8)=20=wt(p^10)`,
so `n=r6/p^9` and `q=r8/p^10` are the unique weight-0 extensions of the
chart functions `r6|_{p=1}`, `r8|_{p=1}` that the code actually evaluates —
the code comments say exactly this.  Source-honest: all eight rows,
including the two outputs, are compiled from the frozen fibre tails of the
hash-pinned parent, with no independent re-derivation to trust.  The report
table (terms/total degree/`w` degree for all eight rows) equals the frozen
`quotient.json` values, and `10+20+35+57+16+29=167` as claimed; the raw-mode
count 230 is frozen in the compiler's `--coordinates raw` path but was not
independently executed here (probe stages it; the report attaches no
inference to it).

## 4. Charge 2 — the selected-component dimension claim

The report's own §3 already rejects every over-claim this charge names: the
two 607-element `slimgb` bases at 32003 and 1000003 are labelled routing
evidence; no lifted basis, flat model, or lucky-prime certificate is claimed;
characteristic-zero upper bound, reducedness, irreducibility, whole-scheme
dimension, and boundary classification are each explicitly disclaimed.  The
frozen `dimension.json` matches the report table including `vdim=-1`.

The characteristic-zero source is the reviewed corrected Q8 formal-branch
theorem (`CONFIRMED` by a different model), which on the fibre
`k=mu=0, nu!=0` proves: rank `J_N=3` with unit minor
`det d(r3,r5,r7)/d(a2,a4,a6)`, rank `J_I=3` with unit minor
`det d(r2,r4,r6)/d(x1,x3,x5)`, and the Schur unit `dPhi/ds(0,0)!=0`, giving
the non-parity branch as the smooth reduced formal curve `s=psi(t^2)` — that
is, literally "a smooth formal curve with `w` a parameter after the parity
quotient".  Transfer from the reviewed `r6=nu` slice to this case's `p=1`
slice is the standard transversal-slice equivalence of the free `C^*`
direction (`wt(p)=2!=0`, `wt(r6)=18`, `nu!=0`), with the residual `mu_2`
being exactly the parity involution absorbed in §3 of the report.

One point a hostile reader must check (I did, by hand): at `w=0` the 6×6
Jacobian of (2.2) in `(c,d2,d4,x1,x3,x5)` is block-triangular with blocks
`A=d(odd/t)/d(c,d2,d4)` (rank 3 from the reviewed `J_N` minor via the
invertible change `T=[[3,1,0],[6,0,1],[3,0,0]]`), `D=d(r2,r4)/d(x1,x3,x5)`
(rank 2 as a submatrix of the reviewed unit `J_I` minor), and a mandatory
one-dimensional transversality `B(ker D) not in Im A`.  That last unit is
exactly the reviewed Schur condition (3.3) of the formal-branch theorem, and
it is additionally certified fail-closed inside this case's frozen replay:
the degree-1 `J.solve` raises `("singular system", …)` on any rank drop, and
the frozen `six_rows: PASS` plus thirty per-step unit digests attest it
succeeded.  So the dimension-one input is reviewed and doubly certified.

**Algebraization (hand-verified).**  Completion smooth of dimension one
means `Ô ≅ E[[w]]`, a domain; `O -> Ô` is faithfully flat hence injective,
so `O` is a one-dimensional domain: exactly one algebraic component passes
through each Q8 contact, of dimension one, and computing over
`E=Q[v]/(Q8)` treats all eight conjugate contacts at once.  Its punctured
closure in (3.1) is one-dimensional because `w` is not identically zero on
the branch (the branch surjects to `Spf E[[w]]`) and `x5`, `x3-2x5=x5*v` are
units at the contact (`Q8` coprime to `v`, `A2`, `D`: frozen gcd
certificates in the reviewed parent).  No inference beyond this is made or
needed.  Charge discharged.

## 5. Charge 3 — the exact `w^5` Hensel calculation

- **Coefficient field.**  `Q8` (as frozen in the normalization jet:
  `24+296v+…-999v^8`) is irreducible over `Q` by the frozen mod-7 Frobenius
  certificate; I re-verified by hand the monic mod-7 reduction
  `[5,1,4,2,6,1,2,4,1]` from the integer coefficients and the certificate
  logic (all factor degrees divide 8; gcd with `x^{7^4}-x` trivial kills
  degrees dividing 4).  So `E` is a field: **no zero divisors exist**, and
  every inverse is either Euclidean-certified (`gcd_Q8=1` plus recorded
  inverse) or fail-closed (`ZeroDivisionError`/`RuntimeError` aborts the
  replay).  The computation never selects one root of `Q8`: it works in the
  full degree-eight algebra throughout, which is what makes the result
  uniform over all eight contacts.
- **Invertibility at every step.**  The perturbation trick
  (`image - origin` with a unit inserted at degree `d`) yields exactly the
  constant Jacobian at `(w=0, base)` — cross terms land in degree `> d` —
  so each step solves the same 6×6 unit matrix; `J.solve` raises on any
  singular system, and uniqueness of each coefficient is forced.  The
  claimed "unique coefficient at every step" is honest.
- **Substitution residuals.**  After the lift the replay re-evaluates all
  six rows on the solved series and asserts every coefficient through `w^5`
  vanishes (`ORDER=6`), then asserts `n0, q0` nonzero.  Frozen `PASS`.
- **Terminal jet agreement.**  The three digests hardcoded in
  `local_series.py` are: `q0=96515608…` = the leaf-4 frozen
  `etale_at_every_Q8_contact.q.constant`; `q1=87b80678…` = the leaf-4 frozen
  `Q1 = dq/dtheta` unit (also displayed in the leaf-4 report §4); both
  byte-identical in the pinned leaf-4 `replay.json`.  The identification
  `w`-coefficient = `theta`-derivative is exact because
  `theta = a0^2/p^9 = w(1+wc^3)^2` on the `p=1` chart, so `theta = w + O(w^2)`
  — hand-verified.  The third digest, `n0=06823a51…`, occurs **nowhere else
  in the repository**: it is a new intra-case pin, not an external
  agreement.  The report's sentence claims agreement only for "the constant
  and first `q` coefficients" — precisely the two externally frozen ones —
  so the report is source-honest; see §9 for the recommended clarification.

## 6. Charge 4 — every bounded nonrelation claim

- **Padé boxes.**  For each of `n, q, Z` and each `[m/d]` in
  `{[1/1],[2/1],[3/1],[1/2],[2/2],[1/3]}` the frozen payload records
  `fit: SOLVED` with `3,2,1,2,1,1` unused residuals respectively, every one
  nonzero and a unit.  Hand-verified logic: with `D(0)=1` the `d` Toeplitz
  equations are forced by compatibility through `w^{m+d}`; a nonsingular fit
  determines `D` uniquely, and any nonzero unused residual at degree `<=5`
  falsifies compatibility through `w^5`.  The `D(0)=0` degenerate cases
  reduce to strictly smaller boxes or to polynomials, which the recorded
  unit coefficients of `n,q,Z` through `w^5` exclude.  The claim is exactly
  "no compatibility through `w^5`", nothing more.
- **Rank logic (hand-verified).**  A nonzero rational nullvector, scaled to
  a primitive integer vector, reduces to a nonzero nullvector modulo any
  prime; `fraction_mod` raises if a denominator is divisible by the prime,
  so the frozen full-rank results at 1000003 and 1000033 are fail-closed
  reductions of the exact rational matrix.  Full column rank at one good
  prime therefore excludes the rational relation exactly.  48 equations =
  6 `w`-degrees × 8 `v`-components, as stated.
- **Box inventory.**  `Z`: all `1<=deg_Z<=10, 0<=deg_w<=4` rectangles with
  `(deg_w+1)(deg_Z+1)<=48`; exactly the two rectangles `(deg_Z,deg_w) in
  {(9,4),(10,4)}` are skipped, and the report says "at most 48 monomials in
  the tested rectangle".  `n,q`: all sixteen boxes `1<=deg<=4` (at most 25
  columns) are tested.  Both frozen `nonzero_nullities` lists are empty.
  §4 closes with "No conclusion is made outside the displayed degree boxes",
  and no other file claims otherwise.  Charge discharged.

## 7. Charge 5 — scale reconstruction and terminal descent

All hand-verified, exponent by exponent:

- `pi=p^9=nu/n` is the definition of `n` rearranged along a trajectory with
  fixed load `r6=nu` (the fibre constant of the reviewed parent); it is
  well-defined near the contact because `n0` is a frozen unit.  This is the
  corrected reconstruction: the `p=1` chart is a coefficient quotient, and
  the trajectory's scale is recovered from the full off-parity `n`, not by
  rescaling the source along the trajectory.
- `S=r8^9=(p^9)^10*(r8/p^10)^9=pi^10*q^9=nu^10*q^9/n^10=nu^10*Z` — algebraic
  identities, no root extracted anywhere (`90=9*10`); leaf-4 additionally
  froze the series-level assert `S=(pi^10 q^9)`.
- The predecessor identity: from `9*r8'=j/u`, `r8=u^2R`, `u^3=h`:
  `S'=9r8^8r8'=j*r8^8/u=j*u^15R^8=j*h^5R^8` (16-1=15=5·3), so
  `h^3(S')^9=j^9h^48R^72=j^9(u^144R^72)=j^9S^8` (144=48·3, 72=9·8).  These
  are the leaf-4 integer guards, re-derived here.
- Descent: `nu` constant in `x` gives `S'=nu^10*Z'` — **no missing
  derivative factor** — and dividing `nu^90 h^3(Z')^9=j^9 nu^80 Z^8` by
  `nu^80!=0` gives (5.2) exactly.  Both primes of attack named in the
  charge fail: there is no chosen ninth root (the identity is root-free and
  `S` is a polynomial in `r8`), and no hidden vanishing denominator (`nu` in
  `C^*` by the reviewed fibre; `n0`, `q0` frozen units).
- The parity-only identity `r6=p^9R6(v)` is not used at any point in the
  case source; the leaf-4 parent freezes the negative control
  `p^9R6(v)-nu = c*t^2+O(t^4)` with a Euclidean unit certificate for `c`,
  exactly as the report states.  Charge discharged.

## 8. Charge 6 — scope and boundary accounting

The report distinguishes a formal coefficient-fibre branch from a global
trajectory in §1 ("not an equation, normalization, irreducibility statement,
genus computation, or rational trajectory"), §5 (necessity only), and §6.
Charged and left open, verbatim in §6 and in the FREEZE scope: `w=0`,
`x5=0`, `x3-2*x5=0`, `p=0`, the projective endpoints of the punctured
non-parity curve, both full Taylor families at `r=A/9`, and the missing
global quotient equation/normalization/genus analysis.  The localized
Singular evidence is correctly noted not to classify components on the
removed boundary.  No punctured-trajectory, all-`(9,12)`, maximum-twelve,
counterexample, or JC2 conclusion appears in any charged file.  The
successor gates named are the honest smallest next steps.  One implicit
hypothesis is worth surfacing (not a defect): the chart also fixes `k=0`
and imposes `r3=0` (`mu=0`); both are inherited verbatim from the reviewed
fibre `(1.1)` `k=mu=0, nu!=0` of the formal-branch theorem and are disclosed
in the frozen chart payload (`"k": 0`) and by the imposed row list, though
the report prose never writes `k=0`.

## 9. Smallest false identity or missing hypothesis

**None found at the stated scope.**  The closest items, none of which is a
false identity or a load-bearing missing hypothesis:

1. The `n0` digest `06823a51…` is pinned only inside this case; the report's
   external-agreement sentence covers only `q0,q1` (which are frozen in
   leaf-4), so it is honest, but a successor should either freeze `nu`'s
   digest in a parent or say "the `n` constant is pinned here for the first
   time".
2. `k=0` and `mu=0` are implicit in the report prose (explicit in the frozen
   chart payload, the imposed rows, and the reviewed parent fibre).  A one
   line "on the `k=mu=0` leaf" in §2 would close the wording gap.
3. The 6×6 invariant-chart invertibility needs, beyond the two reviewed unit
   minors, the one-dimensional Schur transversality; this is exactly the
   reviewed `dPhi/ds(0,0)!=0` and is independently certified fail-closed by
   the frozen replay, but the report's attribution sentence could name (3.3)
   explicitly.
4. The raw-quotient count "230" is frozen but was not re-executed by this
   reviewer (no inference rests on it).

## 10. Promotable sentence and strict scope

Promotable:

> On the `k=mu=0`, `nu!=0` leaf, the punctured non-parity branch through
> every corrected Q8 contact is exactly modelled, after the parity-involution
> quotient of the geometric `p=1` chart, by the six equations
> `r1/t=r3/t=r5/t=r7/t=r2=r4=0` in `(w,c,d2,d4,x1,x3,x5)` with outputs
> `n=r6/p^9`, `q=r8/p^10`; the unique algebraic component through each
> contact is one-dimensional; the lift of the branch through `w^5` over
> `Q[v]/(Q8)` exists uniquely with all displayed coefficients units and with
> `q0,q1` agreeing with the frozen leaf-4 terminal jet; no rational relation
> of Padé type `[1/1],[2/1],[3/1],[1/2],[2/2],[1/3]`, no `H(w,Z)` with
> `1<=deg_Z<=10`, `0<=deg_w<=4`, at most 48 monomials, and no `H(n,q)` with
> `1<=deg_n,deg_q<=4` is compatible with the branch through `w^5`; and along
> any actual fixed-load trajectory the necessary terminal equation
> `nu^10*h^3*(Z')^9=j^9*Z^8` holds with `pi=p^9=nu/n`, `S=r8^9=nu^10*Z`.

Strict scope: formal/algebraic statements about the selected branch and its
component only.  Not promotable: any whole-scheme characteristic-zero
dimension, reducedness, or irreducibility for the localized open scheme (the
two-prime bases remain routing evidence); any classification on
`w*x5*(x3-2*x5)=0` or `p=0`; the projective endpoints; the Taylor families;
any global quotient equation, normalization, or genus; any relation outside
the displayed finite boxes; and any punctured-trajectory, all-`(9,12)`,
maximum-twelve, counterexample, or JC2 conclusion.

## 11. Residual conditions

This confirmation is conditional on the staged byte checks passing on a
shell-bearing session: the two §7 replay commands, sha256 of `FREEZE.txt`
against `c34fff2b…` and of `MANIFEST.sha256` against `3d60b567…`, and
`python3 /tmp/q8gq_probe.py`.  Every hash relation that can be checked by
reading is consistent; a failure of any of these commands would reopen this
review.

CONFIRMED
