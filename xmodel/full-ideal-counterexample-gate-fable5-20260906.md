**Full direct ideal: properness of the complete chart is an existential plane-JC counterexample**

**Verdict: the audited implication is sound. Arrow 1 CONFIRMED, Arrow 2 CONFIRMED-WITH-FIX, Arrow 3 CONFIRMED, Arrow 4 CONFIRMED.** Every field-valued point of the complete direct ideal (either 99 branch or the repaired-mean D108 chart) reconstructs polynomials `F,G` of exact degrees `(99,66)` or `(108,72)` with `J(F,G)` a nonzero constant; a Keller pair with those degrees is not an automorphism; hence an exact-Q proof that the full ideal is proper would prove that the plane Jacobian conjecture is false, with no coordinates, canonical resultant lift, or source condition needed. No properness is asserted or charged here. The reverse implication (Keller pair of this configuration ⇒ chart point) is a typed **GAP** in the charged inputs, which is a hard stop on treating any unit or timeout as an exclusion.

| Arrow | Verdict | What carries it |
|---|---|---|
| 1. `h,D,C` are polynomials; exact total degrees | CONFIRMED | frozen source-map supports, numeric top row of `h` |
| 2. every point ⇒ `J(F,G)∈K×` | CONFIRMED-WITH-FIX | explicit derivative degrees only; Moh propositions are not usable at non-Keller points |
| 3. proper ⇒ point over Qbar | CONFIRMED | weak Nullstellensatz in a polynomial ring with a global order |
| 4. degrees `(3K,2K)` ⇒ not an automorphism | CONFIRMED | Jung–van der Kulk divisibility; Jacobian rescaling is free |

**Custody.** I derived the eight-line manifest mechanically from the indexed `charged_input_i_basename/_sha256` fields of the `.run.v2` receipt and ran `sha256sum -c` in `/tmp/jc2-lane.q5U0M9/inputs`: all eight `OK` ([inputs.sha256](/home/ubuntu/jc2/box/full-ideal-counterexample-gate-20260906/inputs.sha256), [hash-check.txt](/home/ubuntu/jc2/box/full-ideal-counterexample-gate-20260906/hash-check.txt)). The three source maps named in frozen `build_direct.py:35–83` match their embedded hashes `778eda93…`, `3f81dc99…`, `1c927d83…` and were read only. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. No fleet, no ledger/launcher/adapter/`jc2-lean` access, no other lane report, no polynomial expansion beyond symbolic identities with `h,D,C` as free symbols; host writes are this report plus 28 KB of replay notes ([replay_checks.py](/home/ubuntu/jc2/box/full-ideal-counterexample-gate-20260906/replay_checks.py), [replay_checks.json](/home/ubuntu/jc2/box/full-ideal-counterexample-gate-20260906/replay_checks.json)). Nothing below uses a status word of any model as evidence.

**Arrow 1 — physical polynomials and exact degrees (CONFIRMED).** Normalization: `t=1/x`, `z=y/x−1`, `K_P(t,z)=t^N P(1/t,(1+z)/t)`. A table `Σ c_{rz} t^r z^z` denormalizes to `P=x^N K_P(1/x,y/x−1)=Σ c_{rz} x^{N−r−z}(y−x)^z`, a polynomial iff every support point has `r+z≤N`; the `r=0` row is its degree-`N` form `Σ c_{0z}x^{N−z}(y−x)^z`. Independent checks on the frozen maps (replay §C): all coefficient expressions are polynomials in the frozen semantic names with no foreign symbol and no division by a variable; supports satisfy `r+z≤N` with `N=11,22,33,65,98` for `h3,C2,C3,B2,A3` (99, both branches) and `36,71,107` for `h,D,C` (D108); `B2,A3` have `z<k`. Hence `h=h3³+C2·h3+C3`, `D=B2`, `C=A3` are polynomials of degrees `≤33,≤65,≤98` and `≤36,≤71,≤107`. The `r=0` row of `h` is numerically `z^{24}(1+z)^9` and `z^{28}(1+z)^8`, free of every parameter, so `h_top=y^9(y−x)^{24}` or `y^8(y−x)^{28}` at every point. With `F=h³+(3D+a)h/2+C` and `G=h²−bh/3+D` (the `degree_premap` rows `A2c=3·B2c/2`, `A2c_65_0=…+target_a/2`, `B1c_32_0=−target_b/3` encode exactly this), the corrections have degree `≤98<99` and `≤65<66`, so `deg F=99`, `deg G=66`, `F_top=y^{27}(y−x)^{72}`, `G_top=y^{18}(y−x)^{48}`; D108 gives `108,72`, `y^{24}(y−x)^{84}`, `y^{16}(y−x)^{56}`. This holds at every point of the semantic affine space, before any row is imposed.

**Arrow 2 — Keller at every field point (CONFIRMED-WITH-FIX).** Let `K⊇Q` be a field and `P` a `K`-point of the full ideal `I`. Write `j=J(F,G)`.

*Exact T2 identity.* With `h,D,C` as free symbols, `H=h−b/6`, `v=D+a/3+b²/18`, `V=C−bD/4+ab/12+b³/54−c/2`, `U=8V/3`, `R_raw=v²−UH`, `p=d+bc/2−(a+b²/4)²/3`, sympy confirms (replay §A)

\[
G^3-F^2+aG^2+bFG+cF+dG+e_0=\tfrac34R_{raw}H^2-\tfrac18 vUH+vR_{raw}-\tfrac9{64}U^2+pH^2+pv+q,
\]

with `q=e0+2a³/27+a²b²/18+ab⁴/72−abc/6−ad/3+b⁶/864−b³c/24−b²d/12+c²/4`, a pure scalar; the `h⁶,h⁵,h⁴` coefficients vanish identically. Homogenized with normalizer `6k−2` this is exactly the six-summand table of `build_direct.py:531–584` with `R_low` in place of `R_raw`, so `Q_true=Q_*+(R_raw−R_low)(3H²/4+tv)+q·t^{6k−2}`. Every coefficient of `R_raw` with `z≥k` is a `T2_upper` row (`549–553`); `q` sits at depth `196/214>qcap 161/176` and never enters a row. So on `V(I)`: `Q_true=Q_*+q`.

*Degrees of Q.* `T2_strict` rows are all coefficients at depth `<lead=141/151`, over a support superset (`558–587`), so `deg Q≤55/63`. `T2_face_55/63` with `Z·λ₂−1` gives `[y^{55}]Q=λ₂≠0`, so `deg Q=55/63` exactly. The full face block also fixes `Q_top=λ₂y^{15}(y−x)^{40}` / `λ₂y^{14}(y−x)^{49}`, but only `deg Q` and `Q_top≠0` are used below.

*Degree of W.* The builder forms `W=Q³+t3eq·FG+t3_fq·FQ` (D108: `Q⁴+t3eq·FG²+t3_fgq·FGQ+t3_fq2·FQ²`) from `Q` at relative depths `0..20/25` and from `h³,h²` at depths `≤20/25` (`605–636`). This equals the true `W` there: the `q` term enters at relative depth `55/63`, and the `F/G` corrections start at depths `32/35` (replay: `1+min_r(D)=32/35`, `1+min_r(C)=64/70`, `2k=66/72`, `k=33/36`), all beyond the defect `20/25`. `T3_strict` rows are every coefficient at relative depth `<20/25`, so `deg W≤145/227`. The `7/13` omitted monomials of the recursion have degree `≤132/216<D₃` and are simply not part of this `W`; nothing is "set to zero" (replay §B).

*Nonzero j is constant.* With `P₂(X,Y)=Y³−X²+aY²+bXY+cX+dY+e0` and `P₃=P₂³+t3eq·XY+t3_fq·XP₂`, the chain rule gives `J(F,Q)=B₂j`, `J(F,W)=B₃j` where `B₂=3G²+2aG+bF+d`, `B₃=3Q²B₂+t3eq·F+t3_fq·FB₂`. Since `G_top,Q_top≠0`: `deg B₂=132/144` and `deg B₃=2·55+132=242` / `3·63+144=333`, the other terms having degree `≤231/324`. If `j≠0`, additivity in the domain `K[x,y]` and `deg J(F,W)≤deg F+deg W−2=242/333` force `deg j=0`. (The T2 step `deg j≤20/25` is subsumed and not needed.)

*Zero j is excluded.* If `j=0`, characteristic zero gives `F=f(H)`, `G=g(H)` for some `H∈K[x,y]` (Nowicki–Nagata 1988, ring of constants of a nonzero derivation of `K[x,y]` is `K[H]`; equivalently the Arzhantsev–Petravchuk lemma cited by the gate). Then `deg H` divides `gcd(99,66,55)=11` resp. `gcd(108,72,63)=9`; `deg H=1` (or `3` at D108) contradicts unique factorization of `F_top`; so `deg H=11`, `deg f=9` (resp. `9,12`). On the cover `(t,z)=(s³,πs⁴)` resp. `(s⁴,πs⁵)`, `F=s^{−9}((π³−1)^{24}+O(s))` resp. `s^{−12}((π⁴−1)^{21}+O(s))`: the weight-`96/140` face of `h` is `(π³−1)^8/(π⁴−1)^7` with all free parameters cancelling, and every correction has weight `≥291/424>288/420` (replay §C reproduces `major_face_audit.py:100–118`). Negative valuation forces `val H<0`, the top power of `f` dominates, and `(π³−1)^{24}` would be a ninth power (or `(π⁴−1)^{21}` a twelfth), which fails on multiplicities. So `j≠0`, hence `j∈K×`.

*Fix.* The gate's paragraph leans on "the preceding proofs", which cite Moh Prop. 2.2/3.2/4.5 (pp. 152–172): those carry a Keller hypothesis and cannot be invoked at an arbitrary chart point. The field-point argument must be stated as above, from the explicit polynomials only; the gate's own recurrence check (`3Q²B₂` of degree 242 vs `≤231`) is that argument. Second precision: only the rows `T2_upper ∪ T2_strict ∪ {T2_face_55, Z·λ₂−1} ∪ T3_strict` (2,689 of 2,754 at 99 δ=2; 3,105 of 3,196 at D108) are used. The `T3_face` block, `T3_equality`, `Z3·λ₃−1`, the separation localizer, the other face rows, and the residual/source rows are not needed for this direction; call this sub-ideal `J_core⊆I`.

**Arrow 3 — Nullstellensatz (CONFIRMED).** `I` lives in the polynomial ring `Q[s₁,…,s₄₄₉]` (447 / 507); the three inverse rows are ordinary generators, so no localization is involved. If `I≠(1)`, a maximal ideal `m⊇I` has residue field finite over `Q` (Zariski's lemma), embedding in Qbar: a Qbar-point of `V(I)`. Properness over `Q` and over Qbar coincide (faithful flatness). Primitive-integer rescaling of the images and the 1,716 / 3,826 identically-zero images change nothing. The declared Singular order is global: every first-row entry of the site matrix is positive (`build_direct.py:180,416`) and the tail block is `dp(3)`, so `std`+`reduce(1,G)≠0` in that ring, or an exactly verified char-0 msolve basis without `[1]`, certifies polynomial-ring properness. Arrow 2 then applies to the point with `K=Qbar`.

**Arrow 4 — degree divisibility (CONFIRMED).** Theorem (Jung 1942; van der Kulk 1953; Nagata, *On the automorphism group of k[X,Y]*, 1972, Moh's `[N.1]`; Abhyankar–Moh, *Embeddings of the line in the plane*, 1975, Moh's `[A-M.2]`, both on the charged p. 212; elementary proof McKay–Wang, JPAA 52 (1988)): for any field `K`, if `K[F,G]=K[x,y]` then `deg F | deg G` or `deg G | deg F`. Neither `66|99` nor `99|66`, neither `72|108` nor `108|72`. Rescaling: `J(F,G)=j∈K×` gives `J(F,G/j)=1`, `K[F,G/j]=K[F,G]`, same degrees, so "Keller" may be taken as `J∈K×`. A Qbar-pair with `C[F,G]=C[x,y]` already satisfies `Qbar[F,G]=Qbar[x,y]` (the equations `x=P(F,G)`, `y=P'(F,G)` are linear in the coefficients of `P,P'` over Qbar), so the pair is a counterexample to the plane Jacobian conjecture over `C`. The references outside the charged PDF are cited from the standard literature and were not re-read in this lane.

**What does and does not certify existence.**

| Outcome | Existence force |
|---|---|
| exact-Q properness of the complete verified row set (`I` or any `J_core⊆S⊆I`) | **yes** — Arrows 2–4 |
| exact-Q properness of an exact specialization `I+(s_i−c_i)` | **yes** (`V(I')⊆V(I)`); inconsistency of `I'` proves nothing about `I` |
| nonunit result for a subset `S⊉J_core` (e.g. the 466-generator `J₅₅`) | none — lacks the degree bounds on `Q` or `W` |
| finite truncation dropping any `T2_strict`/`T3_strict` row | none |
| point or nonunit basis mod `p` | none — no lifting theorem; it is a signal only |
| timeout, memory stop, incomplete stream | none |

The frozen builder's `finish` assertion (`655–661`) fails after all rows are emitted but before the Singular footer is written, so its stream is not a runnable Singular script and its row set must be re-bound to the 2,754 / 3,196 nonzero labels before any properness reading; this audit validates the mathematics of the ideal, not any production artifact.

**Reverse implication and hard stop.** "Keller pair with degrees `(99,66)` ⇒ point of this chart" is not established by the charged inputs: it needs necessity of the stage-8 source parametrization (two-point/split branch `δ=2` vs `5/2`, D1/D2 face rows, `ρ≠0`), the gauge slices `beta=1` and `jet0=0`, the Prop. 4.6 `T3` face with a free scalar, and compatibility of the existential `T2` family with the canonical resultant. The compressor gate itself defers this to "source classification and allowed normalization/translation". Typed **GAP**. Consequences: a unit result or timeout on `I`, on `J₅₅`, or on any specialization excludes nothing about the `(99,66)` configuration; and per the brief this is a hard stop on running the nonemptiness computation as a decision instrument. It remains a legitimate bounded disproof attempt, because Arrows 1–4 need no necessity.

**Cheapest precise nonemptiness certificate.** The precise object is a witness point: a rational univariate representation over `Q` (squarefree `w(α)`, coordinates `s_i=q_i(α)/w'(α)`) such that every generator of `J_core` reduces to zero modulo `w`, then an independent exact recomputation of `F,G∈Q(α)[x,y]` and of `J(F,G)` from the maps, which certifies the counterexample with no appeal to the compressor or to Theorem B. Cheapest route to it: (i) restrict to `J_core` (drops `λ₃,Z3,t3eq,Zρ,target_e`, which occur in no remaining row, and 65/91 generators); (ii) one modular msolve run (`-P 1`, one prime) as a dimension/degree signal only, adding random rational slices if the dimension is positive; (iii) exact lift by char-0 msolve or Hensel plus rational reconstruction; (iv) exact verification by substitution, which is linear in the stream size. Reject any promotion at stage (ii). If the coordinator's reading of the brief makes the reverse GAP a stop on (i)–(iv) altogether, the correct next task is instead the necessity route, not more solving.

**FALLACY-v2.** Attainment is not inferred from floors: exact degrees come from a verified identity and explicit rows; `deg W≤145` is used only as an upper bound. Major face and cover valuation were recomputed from the maps, with parameters cancelling. Zero Jacobian is handled by its own theorem. Ring, variable order, coefficient field, and the exact row subset are declared; no `sat()`, raw remainder, or vanished-leader division appears. No new exit price is asserted, so no `charge_basis=` line applies.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13543`.
- Body SHA-256:
  `edf4e5d83b4c4299bb84192eb2b1dc3e0225bba565596b08f2e82801529772d2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
