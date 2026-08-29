# Fable 5 hostile review — td12 U1 sibling exact two-direction charge and twin depth-16 gates

Lane: Fable 5, independent adversarial review, not primary. Date: 2026-08-29.

Target:

```text
xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
full  52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69   (verified)
body  306d69f61eb4b9345bcc2bb09dde41411c8762be5203be905eecb108415bba02   (verified;
      exactly the first 6907 bytes, ending before the final separator, as claimed)
```

Worked only in `/Users/dc/code/math/jc2`. No access of any kind to
`jc2-lean`; no web, no AWS, no commit/push, no canonical or target edit, no
heavy computation (desk `python3` `int`/`Fraction` polynomial arithmetic
only, scratch under `/tmp`). One file written: this path.

The target pins no dependency hashes (finding W1). The chain it names was
re-read in full and re-hashed this session; every file matches the value
pinned inside the previously reviewed td12 chain:

```text
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f  m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829  m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
3f214db8c12d022c2852dfadbbc268d105484343a8f6d4664765a08d3efcea03  m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md
8fd4d1d01bcb082b6f7dfd0ccb91cee072a1e7e2fdb6a319c099075b0b39a9de  m2-td12-pole-entry-price-r1-sol56-20260829.md
48525c6fbc9416cbeef7a12764173e0abf484c411b773767c6a6e593adcd53e6  m2-td12-pole-entry-price-r1-hostile-review-fable5-20260829.md
ae3b561ef8e70f527391291bece8b5df308ed2acd4bb0e714f0f32f014510f3a  flag-place-series-consumer-audit-sol56-20260829.md
570f4f18d46178d8b86fe2276dbb2e35cb91e845842530b8c56df80bc16461f0  ladder/SHEET6-AF2.md
```

The corrected St 9.3 (24) with the E6 sign repair, the R1–R4 pricing
mechanism, and the actual-weight Corollary 7.1 budget were reconstructed
from `ladder/SHEET6-AF2.md` §§1–2 directly, and the flag/place/series
dictionary from the sealed consumer audit, not from the target's prose.

## 0. Verdict

**`PASS`.**

All six charged attack surfaces hold. The sibling cell arithmetic is exact;
there are exactly two nonzero northeast direction-orbits, each of reduced
multiplicity one; every parting branch (conjugate shedding, distinct-place
split, shared endpoint, mixed `q`) was attacked and dies; saturation of the
shared budget eight forces one `q=1` flag of exact weight four per
direction with `tau_0 = 17`; the twin depth-16 pure-power gates, the
endpoint qualification, `i = 6n`, and the gcd degree `6n-1` are correct
with the inherited riders correctly quarantined; the execution order is
right; and the scope firewall has no overread. The producer follows the
R1-repaired proof order of the reviewed `nu_F = 25` record (unconditional
`tau_0` bound first, budget kills second, `N == i` third, area identity
last), so the circularity repaired there does not recur here. Three
findings (W1–W3, §9) are documentation-grade and touch no mathematical
claim, so they do not rise to `PASS_WITH_REPAIR`.

**Decisive review finding (N1, §5):** the target's execution-order step 1 —
the "still-open" reduced Proposition 8.1(iv) / T1 system on the sibling
cell `(nu, dp, dq) = (17, 68, 52)` — is solvable in closed form at desk. I
attempted to refute it (my primary counterexample attempt: make the
conditional theorem vacuous) and failed: the system has a solution, unique
up to gauge and root swap, with the two extra roots automatically distinct,
nonzero, and distinct from the chain root:

```text
B1 + B2 = (9/4) A,   B1 B2 = (45/32) A^2,   B1, B2 = (9 ± 3i) A / 8,
C_iv = -(765/416) A^3 != 0.
```

So the sibling cell is T1-alive at reduced-pattern tier, the target's
escape hatch ("if that system has no solution, no source-jet work is
needed") does not fire, and the twin gates are the live object. Alive is
not existent (R4): this is formal-pattern survival, not realization.

Perimeter: nothing here or in the target is a landing theorem, a source
realization, a full-book or degree-ceiling statement, `G2-PSC`, `G2-BD`,
or any JC2 consequence.

## 1. Attack 1 — sibling fields and the two direction-orbits: PASS

Recomputed from P0/R1.3 at `(l,eps,k,lex,Sm,nu_F) = (2,0,2,0,2,17)` with
parent `(w_G, M_G) = (9/2, 2)`, independently of the target:

```text
s = 1+k+lex = 3
dp = eps + nu(l+Sm) = 68        dq = s*nu + 1 = 52
E  = l*dq - dp = 36             C_P0 = l(k+lex) - Sm = 2
T  = Sm + l - eps*s = 4         E = nu*C_P0 + (l-eps) = 36  (consistent)
kbar = l*w_G*dq/E = 13          X = kbar*dp/dq = 17
w_F = l*w_G*(dq-1)/(nu*E) = l*w_G*s/E = 3/4     M_F = gcd(68,52) = 4
```

Filters: (S) `104 > 68`; (NE) `1*52 < 68` strict; (R) `68 not in {52,104}`;
N1 `gcd(13,17)=1`; R1.0 `gcd(4,17)=1`, `52 ≡ 1 (mod 17)`; MP2 `4 >= 2`;
divisor law `36 | 2*9*4 = 72`. Terminal: `j = M(1-w) = 1 in N*`,
`psi = ceil(4/1)-1 = 3`, shared ceiling `td-1-psi = 8`. All eight displayed
reduced fields, the discrete tuple, and `psi = 3` reproduce exactly. The
cell is edge-for-edge the `k=2` row of the Opus-reenumerated one-step menu:
my own scan of `E = 2nu+2 | 72` with `kbar = 9(3nu+1)/(2nu+2) in Z`
recovers exactly `nu in {5, 17}`, and only `nu = 17` is P1-shaped
(`nu = 5` has `w = 9/4 > 1`). So this sibling is the unique second
P1-fitting first-trunk child, as the reviewed primary records.

Directions: `eps = 0` gives no zero root (`Pfull(0) != 0`), so the pattern
roots are the chain orbit `A` (reduced multiplicity `l = 2`) and the two
extras (each `m_j = 1`, forced by `m_j <= l-1 = 1`). The chain root is the
searrow continuation (`l*dq = 104 > 68`); both extras are northeast
(`52 < 68`); St 3.18 / Prop 8.1(i) exclude hidden sheet-level directions
(true multiplicities are the reduced pattern's times `i`). Hence **exactly
two distinct nonzero NE direction-orbits, each reduced multiplicity one,
full multiplicity `i`**, with `D_F/i = X_F = 17` and per-direction gap
`17 - 13 = 4`. The AF2 floor `k*max(1, ceil(gap)) = 8` matches. Verified.
(Distinctness `B1 != B2` is definitional for `k = 2` and is additionally
*forced* by the T1 solve, §5: the discriminant is `-9A^2/16 != 0`.)

## 2. Attack 2 — a cv flag per actual direction, inserted simultaneously: PASS

Existence, per direction: gap `4 > 0` puts each extra child in
`T_a^nearrow` (AF2 R2, regularity-free for positive gap). Proposition 6.6
(nearrow persistence) with repaired St 7.3 in its audited universal form —
"a ray containing any nearrow flag is finite", quantified over **every**
ray, not one selected continuation — plus repaired 7.2 gives every physical
place through each extra child a same-ray critical-value flag, `pi(H) > 1`
(St 7.1), integral weight (INT). Corrected St 9.3 (E6-repaired (24)) is
per-ray with denominator `mult(p_F, c*) = i` **at `F`**, so every actual
flag below either direction — majority or departed sub-cluster alike —
has

```text
wt(H) = kappa_H(pi(H)-1) >= D_F/i - kbar_F = 17 - 13 = 4.
```

The target's disclaimer is honest and load-bearing: it prices the full
actual flag set and never assumes an MFE-selected subset exhausts places
or series, and it never identifies a flag with a conjugate Puiseux series
— exactly the dictionary discipline of the sealed consumer audit.

Distinctness and simultaneous insertion: places through the two different
extras have contact exactly `pi(F)`, strictly below any flag height, so by
Definition 3.3 / AF2 R4 their flags are distinct orbit-level Corollary 7.1
summands (the numerical complex-conjugacy of `B1, B2` found in §5 is not
deck conjugacy; two distinct `t`-roots are two distinct `nu_F`-orbits).
Simultaneous insertion is consistent under both ledger forms: refined
`4 + 4 = 8 <= 8 = td-1-psi`, and coarse Cor 7.1 with the distinct terminal
witness `1 + 3 + 8 = 12 <= 12`, exactly saturated. Verified.

## 3. Attack 3 — all parting branches, and what saturation forces: PASS

The unconditional inputs, in the R1-repaired order: for every flag `H`
below either direction, `tau_0(H) = kappa_F(pi(H) - pi(F)) >= D_F/i = 17`
(reviewed exact-descent integral `D_F = int_0^{tau_0} N dtau` with
`N <= i`, valid with or without partings), `wt(H) = q_H(tau_0 - 13)` with
`q_H = kappa_H/kappa_F in N*` (divisor-chain law). Branches tried:

1. **Conjugate shedding in one direction** (`q >= 2`, before or at the
   endpoint): that flag alone costs `>= 2(17-13) = 8`; the other
   direction's mandatory flag adds `>= 4`; total `>= 12 > 8`
   (coarse form: `1 + 12 = 13 > 12`). Dead.
2. **Distinct-place split strictly below the cv level in one direction**:
   two distinct orbit-level flags below that direction, each `>= 4`
   (the (24) denominator is the multiplicity at `F`, not the sub-cluster
   size — no cheap departed flag); plus the other direction `>= 4`;
   total `>= 12 > 8`. Dead.
3. **Mixed/different `q` across the two directions** (`q_1 = 1`,
   `q_2 >= 2`, or both `>= 2`): any direction carrying `q >= 2` reduces to
   branch 1 by symmetry. Dead.
4. **Shared endpoint**: a distinct-place split at exactly level 17 shares
   the endpoint flag (Definition 3.3 endpoint identification), keeps
   `N = i` on `(0, 17)`, and leaves the charge at 4 — allowed, exactly as
   the target qualifies. Endpoint **conjugate** shedding raises
   `kappa_H` under the post-characteristic Notation 3.5 convention and is
   branch 1. Dead.
5. **Zero flags in one direction**: impossible (repaired 7.3 universal
   quantifier, §2).
6. **Charge drift without parting** (`q = 1`, single flag, `tau_0 = 18`):
   the descent integral would need shed area `i`, i.e. a parting; both
   parting modes are dead. Unconstructible.
7. **Cross-direction flag identification**: contact `pi(F)` is strictly
   below flag height; pole flags cannot be cv flags (POLE-EXIT-ZERO
   package); the terminal x-side witness is in the other tree component.
   No identification escape.

Surviving profile, per direction: exactly one flag, no parting, hence
`q = E_+/E_0 = 1` directly, `N == i` on `(0, tau_0)`, and the exact
integral `17i = D_F = i*tau_0` pins `tau_0 = 17` and
`wt = 1*(17-13) = 4` exactly. Total two-direction charge exactly
`4 + 4 = 8`, saturating the shared budget `8` — with merge charge zero
(derived at the reviewed trunk tier) and the three actual pole-entry
vertices at zero by the PASSed universal POLE-EXIT-ZERO lemma (its review
file now exists in the workspace and hashes to the exact value the
`nu=25` review's F2 finding recorded from the run log; that provenance
gap is closed). Every kill above survives under coarse Corollary 7.1
alone, so the conclusion is robust to the psi-refinement's witness clause.
The target's claim set — one `q=1` flag of exact weight four per
direction, `tau_0 = 17`, no characteristic-denominator jump, total exactly
eight — is **verified on every branch**.

## 4. Attack 4 — twin depth-16 gates, endpoint, `i = 6n`, gcd degree: PASS

- With no parting and no denominator jump before level 17, all `i` series
  of a direction share their truncations through every admissible level;
  the denominator stays `kappa_F`, so the admissible levels are exactly the
  integers `1..16` strictly below `tau_0 = 17` (a fractional-level split is
  a denominator jump, dead by branch 1). Hence each level's normalized
  child polynomial is a pure `i`-th power with nonzero lead (St 3.9(ii)
  supplies `a_0 != 0`; an all-zero subdiagonal gives a legal pure power, so
  the gate never stalls). Two directions, 16 levels: **32 tests**. Correct.
- Pure power `<=>` `deg gcd(C, dC/dz) = i-1` for a degree-`i` polynomial
  with nonzero lead: desk-verified in both outcomes (`(z-2)^6` gives 5;
  `(z-2)^5(z-3)` gives 4 and the gate fires). The target's "either the
  binomial identities hold or the gcd degree" is an equivalence offered as
  alternative tests (W3, wording only).
- Endpoint qualification: purity is demanded at `1..16` only; a
  distinct-place split first allowed at 17 at the shared endpoint flag.
  Correct, and consistent with §3 branch 4.
- `i = 6n`: the trunk-edge count law at this edge reads
  `i * mult_red(Pfull_F, A) = i_G * dp_red(G)`, i.e. `2i = 6n * i_G`, with
  the same arrival multiplicity `l = 2` as the reviewed `nu = 25` child,
  and `i_G = 2` on displayed direct entries (pole top degree 4, merge
  arrival reduced multiplicity 2). So `i = 3n * i_G = 6n`. This inherits
  exactly the two riders of the reviewed `nu = 25` record: count-exactness
  of St 3.9(i) at the trunk edge (Opus REPAIR 4a transport) and the
  direct-entry / zero-length-pole-chain hypothesis (licensed by the P2
  arrival law, not forced). The target quarantines both correctly: the
  exact-charge theorem uses only `i > 0` (`D_F/i = 17` is `i`-free), and
  `i = 6n` enters only the displayed gcd degree `6n - 1`. Verified; no new
  gap beyond the inherited-conditional status, which is disclosed.

## 5. Attack 5 — execution order, and the T1 system decided: PASS + finding N1

Order: source extraction needs the pattern roots (recentering at `c_j`
with `c_j^17 = B_j`), so the reduced T1 solve at `(17, 68, 52)` must
precede it — the target's order 1→2→3→4 is forced, not stylistic. Nothing
previously known kills or solves that system: the trunk primary and its
Opus review decline it in terms, and the promotions pairing ledger records
`B -> sibling nu_F=17` as `NO_HIT`.

**N1 — the system solved (vacuity attack failed).** With
`p = (t-A)^2(t-B1)(t-B2)`, `q = eta(t-A)(t-B1)(t-B2)`, `t = eta^17`,
`rho = dp/dq = 68/52 = 17/13`, Prop 8.1(iv) divides exactly by `Pfull`
(`Pfull = (t-A) W`), and the quotient

```text
C_iv(t) = rho(t-A)(t-B1)(t-B2)
        + nu t [ (rho-2)(t-B1)(t-B2) + (rho-1)(t-A)(t-B2) + (rho-1)(t-A)(t-B1) ]
```

must be constant: three coefficient conditions on the two ratios. With
`e1 = B1+B2`, `e2 = B1 B2`:

```text
t^3:  rho + nu(3 rho - 4) = 0   identically (rho = 4nu/(3nu+1) top law);
t^2:  A[rho + 2nu(rho-1)] + e1[rho + nu(2rho-3)] = (153 A - 68 e1)/13 = 0
      ==> e1 = (9/4) A;
t^1:  e2[rho + nu(rho-2)] + A e1[rho + nu(rho-1)] = (-136 e2 + 85 A e1)/13 = 0
      ==> e2 = (45/32) A^2.
```

All four bracketed coefficients are nonzero, so the solution is **unique
up to gauge and root swap** — one orbit, the `k=2` analogue of the
reviewed `k=1` kernel. Side conditions all hold: discriminant
`e1^2 - 4 e2 = -9A^2/16 != 0` (so `B1 != B2` is *forced*, the `k=2`
pattern is self-consistent), `e2 != 0` and `Pfull(0) = A^2 e2 != 0`
(`eps = 0` consistent, `eta || q` exact), `z = A` is not a root
(`A^2 - e1 A + e2 = (5/32)A^2 != 0`), `rho = 17/13 in (1,2)` strictly
(filter (R): order-`mu` coefficients nonzero at both `p`-multiplicities),
`C_iv = -rho A e2 = -(765/416) A^3 != 0`. The polynomial identity
`E(t) - C_iv Pfull = 0` was verified exactly in `Q[t]` at
`(e1, e2) = (9/4, 45/32)`, `A = 1`; four mutation controls (perturbed
`e2`, wrong `e1`, wrong `rho`, swapped multiplicity pattern) all fail, so
the checker is not vacuous. General-`nu` closed form for the whole `k=2`
shape, recorded because it is the same linear algebra:

```text
e1 = 2A(nu+1)/(nu-1),   e2 = A^2(nu+1)(nu+3)/(nu-1)^2,
disc = -8A^2(nu+1)/(nu-1)^2 != 0  always,
```

verified identically also at the only other legal `k=2` cell `nu = 5`.

Consequence for the target: its conditional theorem is **not vacuous** at
reduced-pattern tier; step 1 of its execution order is decided in the
survival direction (`SIBLING_T1_SURVIVES` at formal-cell scope), and steps
2–4 (source extraction and the 32 gates) are the live objects. This
review-tier solve should be re-sealed as its own producer artifact on any
promotion; it changes nothing in the target's text, which correctly left
T1 open.

Also checked here: the semi-invariance residues do not pre-kill the gates.
`N_1 ≡ -kbar_F ≡ 4 (mod 17)`, `4^{-1} ≡ 13 (mod 17)`, and with
`D_F = 17i ≡ 0 (mod 17)` the graded residues are `e_k ≡ 13k ≡ k e_1` —
exactly the pure-power progression, the `nu = 25` §5 phenomenon
transported. So no cheap desk kill exists; genuine source data are
required, confirming the gates as the correct next gate.

## 6. Attack 6 — scope audit: PASS

The body claims conditional exact-charge and necessary-gate statements
only. Explicitly absent, verified line-by-line: realization or landing;
existence of a Keller pair; full-book or panel change; degree ceiling;
`G2-PSC`; `G2-BD`; JC2; any identification of the sibling ratios with
merge data. "Kills this sibling" is correctly scoped to this route, not
the row. The knife-edge framing ("does **not** kill the sibling") is
exactly right: `8 = 8` fits with zero slack, so any single further priced
unit anywhere in the configuration kills the route — but none is proved.
The lifecycle line correctly marks the note provisional pending this
review. No overread found.

## 7. Counterexample attempts (all fail)

1. **Vacuity via T1 refutation**: solved instead — unique surviving gauge
   orbit (§5 N1). Failed.
2. **Charge 7** (one direction under four): every flag `>= 4` per-ray, and
   every direction owns at least one flag. Unconstructible.
3. **Charge 9+ via `q = 2` at minimal level**: `2(17-13) = 8` plus the
   other direction's 4 gives `12 > 8` (`13 > 12` coarse). Dead.
4. **Cheap departed flag** (one-sheet sub-cluster splitting at level 16):
   (24)'s denominator is `mult(p_F, c*) = i` at `F`; the departed flag
   still costs `>= 4`; totals `>= 12`. Dead.
5. **Fractional-level split at 33/2**: denominator jump, i.e. `q >= 2`.
   Dead.
6. **Endpoint abuse**: place split at exactly 17 shares the flag; charge
   unchanged at 4; conjugate shed at 17 costs `>= 8` and dies. No drift.
7. **Flag sharing across the two directions**: contact `pi(F)` strictly
   below flag height forces distinct orbit-level flags; numerical complex
   conjugacy of `B1, B2` is not deck conjugacy. No merge in the ledger.

## 8. Negative controls

1. **`nu = 5` sibling-shape cell**: T1 equally solvable
   (`e1 = 3A, e2 = 3A^2`, distinct extras), but `w = 9/4 > 1` is not a P1
   terminal, no psi-budget exists, and the machinery correctly emits **no**
   exact-charge theorem there. The knife-edge is budget-driven, not an
   artifact of the pricing formulas.
2. **`nu = 25` charged cell**: one NE direction only; the same schema
   yields `8 <= 9` with slack one and no saturation — the two-direction
   structure, not the schema, pins the sibling. No overfiring.
3. **Checker mutations**: four independent corruptions of the T1 identity
   all detected (§5).
4. **The target's own §5 control, checked**: at the td8 reference cell the
   defect `3/2` is not priced by its numerator; the floor 3 there comes
   from the `q`-dichotomy, and integrality attaches to
   `q(tau_0 - kbar) in N`, not to the lower-bound gap. The sibling's
   integral defect 4 avoids the fractional regime entirely, and the
   producer's use is confined to it. Control sound. Consistency note: the
   conjectural arity law evaluates to `min(4, 2*4) = 4` per direction
   here, matching the proved exact value — two further consistent
   instances for that conjecture, not a proof of it.

## 9. Findings (all non-blocking)

- **W1 (provenance).** The target pins no dependency hashes, unlike the
  `nu = 25` discriminator it parallels. All named inputs verify against
  the previously sealed chain (header block above), so nothing drifted,
  but pins should be added on any promotion.
- **W2 (attribution).** §1's "Corollary 7.1 gives the shared ceiling
  eight" is the coarse actual-weight inequality *plus* the `>= psi`
  terminal witness in the other tree component — the reviewed
  St 9.4/9.5 + Cor 7.1 route, same as the `nu = 25` record. Since every §3
  kill survives under coarse Cor 7.1 alone (`13 > 12`), nothing
  mathematical rides on the refinement; a promotion should cite the
  witness clause explicitly.
- **W3 (wording).** §4's "either the binomial identities hold or
  `deg gcd = i-1`" offers two equivalent tests as if disjunctive
  alternatives; read "equivalently".

## 10. Maximum safe consequence and cheapest next discriminator

> Conditional on the reviewed td=12, `m=3`, `[2,2,2]` U1 row and on its
> sibling reduced cell `(nu_F, dp, dq) = (17, 68, 52)`,
> `(l,k,Sm,eps,lex) = (2,2,2,0,0)`, `(w_F, M_F) = (3/4, 4)`, `psi = 3`
> occurring as the P1 terminal of an actual td=12-surviving configuration,
> under the pinned repaired source package: the cell has exactly two
> nonzero northeast direction-orbits, each of full multiplicity `i`; each
> owns exactly one orbit-level critical-value flag with
> `kappa_H = kappa_F`, normalized cv level `tau_0 = 17`, and exact charge
> 4; the two-direction charge is exactly `4 + 4 = 8`, saturating the
> shared budget `td-1-psi = 8` (and the coarse ledger `1+3+8 = 12` at
> equality); consequently both direction clusters are unchanged-denominator
> pure `i`-th powers at every normalized level `1..16` — 32 necessary
> direction-level tests, a distinct-place split first allowed at level 17
> at the shared endpoint flag. On displayed direct entries `i = 6n` and
> the level-one test degree is `6n - 1`, inheriting the count-exactness
> and direct-entry riders of the reviewed `nu = 25` record. The reduced
> T1 system at `(17, 68, 52)` is solvable, uniquely up to gauge and swap
> (`e1 = 9A/4`, `e2 = 45A^2/32`, extras forced distinct), so the theorem
> is non-vacuous at reduced-pattern tier. A single further priced unit
> anywhere in the configuration kills the route; none is currently proved.

Explicitly not established: realizability by any `(f, g)`; the coupled
Keller recurrences; landing; full-book td=12 exclusion; any td ceiling;
`G2-PSC`; `G2-BD`; any JC2 consequence.

**Cheapest next discriminator.** Step 1 of the target's order is done
(N1). The residue progression closes the last desk-only avenue, so the
discriminator is now the twin level-one gates themselves: extract both
first-child coefficient vectors `([(eta-c_j)^{i-k}] P_k)_{k=1..i}`,
`c_j^17 = B_j`, from the exact source/Keller identities — the same
`BChildJet`-style extractor already specified for the `nu = 25` lane, here
in a two-direction, 16-level variant fed by the one shared `P_k` family —
and run the two `deg gcd = 6n-1` / binomial tests; kill on the first
failure. A cheaper intermediate desk step, if wanted before source work:
the `nu = 25` §5 analogue (three-point `R_k` interpolation at
`A, B1, B2`, now `deg R_k <= 2`) to certify formal freedom for the twin
gates; it was not needed for this verdict and is producer work.

## Seal

Body SHA-256 (all bytes before this `## Seal` heading): `9b53f3ce94859f4854480f3e49decd91da319f782f87a2bf7a5f7116e836c7e3`
