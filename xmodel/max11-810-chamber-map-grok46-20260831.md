# max11 `(8,10)` chamber map and closure program

**Verdict: PARTIAL**

After the committed Pi chain, the `(8,10)` leaf still has three live
chambers and one unauthored last Keller row. The Jacobian of an octic–decic
pair has \(Y\)-degree at most \(17\); coefficients \(16\) through \(1\) are
first-integral rows, and coefficient \(0\) is the inhomogeneous final row.
The Pi modules consume the degree-\(1\) row. The degree-\(0\) row is not
present as a theorem on `origin/master`. Scale-two still has the aligned
face \(N=0\) unopened, and a two-component linear-root packet at the ninth
face. Scale-zero has both constant faces of \(N\) honest and unclosed.

The analogue of the \(610\) jet-quotient bound \(h\)-degree \(\le 6\) is
**not** a landed \(810\) pole-ceiling lemma. From committed factorizations
the Pi numerator satisfies \(Q=h^{96}(\mathrm{head}+h\cdot\mathrm{tail})\)
and \(Q=C(2^{44}\eta)\,h^{112}\), so the remaining polynomial in \(h\) has
formal degree \(\le 16\). That arithmetic is derived below. It is not a
proof that a holomorphic primitive cannot have derivative \(C(j)/h_0\):
the degree-one primitive is a differential constant, so its source
derivative is \(0\), not \(j/h_0\).

No exit-price is claimed.

---

## 0. Sources and verification status

Work over an algebraically closed field \(k\) of characteristic zero, on
the normalized consecutive leaf
`Normalized810LeadingCoreSource` (\(r=4\): \(\deg_Y p=8\), \(\deg_Y q=10\),
leading \(p_8=h^4\), \(q_{10}=h^5\), `IsPlaneKellerPair`). Clone used for
reading: `https://github.com/dcposch/jc2-lean` at
`a2507ecadde77677cf4832ac3af3b625ca366e21` (`origin/master` as of this
run; commit date `2026-08-31 15:04:01 -0700`). The nested worktree
`jc2-lean/` is sandbox-blocked.

Kernel-green status of scratch modules is frozen input from the lane
prompt. This lane did not elaborate Lean. Treat “green” as
**UNVERIFIED** here.

### 0.1 What was read (committed blobs, used below)

Tracked `LowScale810*` chain, the two Fable scale-zero scratch modules,
the five Pi consumers, the three `derive_810_*.py` / emitter scripts,
`LowScaleCore.lean`, `LowScaleOtherLeaves.lean`, `HANDOFF_2026-08-31.md`,
the \(610\) tower/ceiling/wrapper scratch, and the \(410\) cascade /
aligned-closure scratch.

| File | Frontier theorem (exact name) |
|---|---|
| `LowScale810ScaleZeroSource.lean` | `normalized810ScaleZero_discriminatorFirstFace`, `scaleZero_firstClearedDefect_exists_C_810` |
| `LowScale810ScaleZeroSecondDefect.lean` | `normalized810ScaleZero_exists_secondClearedDefect` |
| `LowScale810ScaleZeroThirdDefect.lean` | `normalized810ScaleZero_exists_thirdClearedDefect` |
| `LowScale810ScaleZeroFourthDefect.lean` | `normalized810ScaleZero_exists_fourthClearedDefect` |
| `LowScale810ScaleZeroFifthDefect.lean` | `normalized810ScaleZero_fifthClearedDefectFirstFace` |
| `Fable810ScaleZeroThirteenthDefectScratch.lean` | `normalized810ScaleZero_thirteenthClearedDefectFirstFace` |
| `Fable810ScaleZeroFourteenthDefectScratch.lean` | `normalized810ScaleZero_fourteenthClearedDefectFirstFace`, `scaleZero_omicronResidual_deriv_zero_810` |
| `LowScale810ScaleTwoSourceFace.lean` | `normalized810ScaleTwo_discriminatorFirstFace`, `normalized810ScaleTwo_nonzeroFace_has_linear_root` |
| `LowScale810ScaleTwoSecondFace.lean` … `NinthFace.lean` | `normalized810ScaleTwo_nonzeroFace_ninthInitialPacket` at the tracked frontier |
| `LowScale810ScaleTwoSeventhPacket.lean` | `nonzeroFace810_linearRoot_seventhInitialPacket` |
| `Sol810PiResidualScratch.lean` | `piResidual810_deriv_zero` |
| `Sol810PiDifferentialBridgeScratch.lean` | `piResidual810_deriv_zero_of_monic_differentialJacobian` |
| `Sol810PiSourceClearingDraftScratch.lean` | `piSourceClearingBridge810` |
| `Sol810PiLeftUnsolvedUniformBridgeScratch.lean` | `localClearedSixteenthDefect810_left_unsolved_factored`, `piLeftUnsolvedHead810_eval_root_of_power` |
| `Sol810PiSourcePowerBridgeScratch.lean` | `piSourcePowerRelation810_of_residual_eq_C`, `piLeftUnsolvedHead810_eval_root_of_source_residual` |

Blob SHA256 on this HEAD (content-address, not git tree SHA):

| File | SHA256 |
|---|---|
| `Fable810ScaleZeroThirteenthDefectScratch.lean` | `121f8cdf7f4c86c6b93d19b137dc0bbf5416d56789ecd2e419d659db8dfe167c` |
| `Fable810ScaleZeroFourteenthDefectScratch.lean` | `2be60d3c685490fe3aea6826d414b96b4538f512600a6041628a5defe866cf95` |
| `Sol810PiDifferentialBridgeScratch.lean` | `1ea441ed7ac20dce3ad65f44535aa8527feceaf7660aa179e8227e53db5b33af` |
| `Sol810PiSourceClearingDraftScratch.lean` | `6dc74756306e667423d0f3291b520c17cc25d85aef3af000a7aaba81ef050123` |
| `Sol810PiResidualScratch.lean` | `130ed2957f7a7d8ab9d1e68bd999fbad6f613773bcb00c73de15effa92f69fd1` |
| `Sol810PiLeftUnsolvedUniformBridgeScratch.lean` | `b3aa64316e246fa20a58bb553d806ac5cd44851778da085698a3686782e0387a` |
| `Sol810PiSourcePowerBridgeScratch.lean` | `400e9540c213403851283f83275a56798a594bb094338bb9f1ba1215d7402c68` |

Thirteenth, Fourteenth, Differential, and SourceClearing match the
`HANDOFF_2026-08-31.md` SHAs. Residual, LeftUnsolved, and SourcePower do
**not**: they were rewritten after that `07:00Z` handoff and before this
HEAD. Use the table above, not the handoff, as the frozen blobs.

### 0.2 What is not a blob on `origin/master`

Thirteenth imports `Fable810ScaleZeroTwelfthDefectScratch` and
`Grok810ScaleTwoFourteenthFaceScratch`. Fourteenth imports
`Fable810ScaleTwoFifteenthFaceScratch`. Those three files are absent from
a clean clone of this HEAD. `derive_810_pi_residual.py` additionally
parses residual definitions from

- `Grok810ScaleZeroEighthDefectScratch.lean` (`thetaResidual810`)
- `Grok810ScaleZeroNinthDefectScratch.lean` (`iotaResidual810`)
- `Grok810ScaleZeroTenthDefectScratch.lean` (`kappaResidual810`)
- `Fable810ScaleZeroEleventhDefectScratch.lean` (`muResidual810`)
- `Fable810ScaleZeroTwelfthDefectScratch.lean` (`nuResidual810`)

None of those five files is on this clone. Committed Pi Residual *uses*
`thetaResidual810` through `nuResidual810`. So the Pi chain is not a
closed git source set: it hydrates those definitions from the scratch
olean cache described in the handoff. Their theorem names and exact
statements are **UNVERIFIED** as origin/master text. Headers of
Thirteenth describe the twelfth-defect packet as already clearing
weights \(h^{14}\) through \(h^{91}\); that is a committed comment, not a
theorem read from a sixth-through-twelfth module.

Handoff excludes `Sol810PiLeftJetBridgeDraftScratch.lean` as
source-invalid. It is not in the proof chain.

Python comments mention `bridgeNuLeftPacket810` as carrying the root-value
laws for \(m_1,\tau_1,g_1,k_1\). That name is not a Lean declaration on
this HEAD. **OPEN.**

---

## 1. Jacobian inventory (both scales)

The bivariate Jacobian of an octic–decic pair is a polynomial in \(Y\) of
degree at most \(17\), equal to \(C(C(j))\). Coefficient \(17\) is the
leading weighted Wronskian (common-core source). Coefficients \(16\)
through \(0\) are the remaining Keller rows.

| Jac \(Y\)-coeff | Scale-two face file (tracked) | Scale-zero defect file | Residual | Weight of cleared numerator |
|---|---|---|---|---|
| \(16\) | `SourceFace` (`nextCoefficientJacobianRow_810`) | `Source` (discriminator \(N=5p_7 H-4q_9\)) | — | \(N\sim h^9\) |
| \(15\) | `SecondFace` | first cleared defect in `Source` | \(\alpha\) | \(h^{14}\) |
| \(14\) | `ThirdFace` | `SecondDefect` | \(\beta\) | \(h^{21}\) |
| \(13\) | `FourthFace` | `ThirdDefect` | \(\gamma\) | \(h^{28}\) |
| \(12\) | `FifthFace` | `FourthDefect` | \(\delta\) | \(h^{35}\) |
| \(11\) | `SixthFace` | `FifthDefect` | \(\varepsilon\) | \(h^{42}\) |
| \(10\) | `SeventhFace` | sixth (not a blob) | \(\zeta\) | \(h^{49}\) (header of Thirteenth) |
| \(9\) | `SeventhPacket` / `EighthFace` | seventh (not a blob) | \(\eta\) | \(h^{56}\) |
| \(8\) | `NinthFace` | eighth (not a blob) | \(\theta\) | \(h^{63}\) |
| \(7\) | tenth (not a blob) | ninth (not a blob) | \(\iota\) | \(h^{70}\) |
| \(6\) | eleventh (not a blob) | tenth (not a blob) | \(\kappa\) | \(h^{77}\) |
| \(5\) | twelfth (not a blob) | eleventh (not a blob) | \(\mu\) | \(h^{84}\) |
| \(4\) | thirteenth (not a blob) | twelfth (not a blob) | \(\nu\) | \(h^{91}\) |
| \(3\) | fourteenth (import-only) | `ThirteenthDefectScratch` | \(\xi\) | \(h^{98}\) |
| \(2\) | fifteenth (import-only) | `FourteenthDefectScratch` | \(\omicron\) | \(h^{105}\) |
| \(1\) | no face file | Pi chain (`localClearedSixteenthDefect810`) | \(\pi\) | \(h^{112}\) |
| \(0\) | no file | no file | — | inhomogeneous; does not clear a defect |

The weight column for rows \(10\) through \(4\) is taken from the
Thirteenth header’s list of twelve cleared powers. Those powers are
**UNVERIFIED** as theorems of named sixth–twelfth modules.

There is no Keller coefficient below degree \(0\). That is the row
ceiling. It is the same fact \(610\) records in
`LowScale610ScaleTwoFifteenthFinalRow.lean` and \(410\) records in
`Sol410ScaleTwoAlignedFinalKellerRowScratch.lean`.

Off-by-one in file comments starts at the fourth scale-zero defect
(comment says “fifth cleared”, theorem is
`scaleZero_fourthClearedDefect_exists_C_810`). Theorem names and the
weight sequence \(14,21,\ldots,112\) are the census keys.

---

## 2. Question 1: chamber census after Pi

### 2.1 Case tree that remains

```
Normalized810LeadingCoreSource, H.natDegree ∈ {0, 2}
│
├─ H.natDegree = 0                         [scale-zero]
│   N = C(λ)                               [discriminator is a ground constant]
│   ├─ λ = 0                               [aligned constant; no finite root]
│   └─ λ ≠ 0                               [nonzero constant; no finite root]
│   defects 1–5 tracked; 13–14 + Pi landed
│   remaining Keller row: degree 0 only
│
└─ H.natDegree = 2                         [scale-two]
    N² = C(κ) H⁹
    ├─ N = 0                               [aligned; NOT OPENED]
    └─ N ≠ 0, H = h₀², h₀.natDegree = 1    [linear root a]
        ninth packet, two components:
        ├─ left:  t₀(a) may be ≠ 0; v₀=s₀=u₀=w₀=b₆=0 at a;
        │         32 s₁−40 v₁ = 5 t₀² and 128 w₁−160 u₁−40 t₀ v₁+5 t₀³ = 0
        │         Pi unsolved peel is written on this jet
        └─ right: t₀(a)=0 and the same collapsed vanishing;
                  4 s₁ = 5 v₁ and 4 w₁ = 5 u₁
        remaining source-facing faces: Jac degrees 7..0 (eight rows)
        Pi already consumes degree 1 as an integral
        remaining unauthored row: degree 0
```

The twice-prime large-shear adapter
`normalized810LowScale_largeSourceShear_exactGCD` /
`planeKellerNormalizedConsecutiveLowScaleRoute_of_twicePrimeGCD` is a
conditional classical closure of both scales. It is not a chamber
closure: every \(810\) header refuses total-degree and twice-prime
theorems.

### 2.2 Scale-zero: defects beyond the Fourteenth

Tracked through the fifth defect. Next missing input in
`LowScale810ScaleZeroFifthDefect.lean` is the degree-\(10\) residual
(sixth cleared defect, weight \(42\) already landed as
`localClearedSixthDefect810`).

Thirteenth’s header states that the twelfth-defect packet has already
cleared the first twelve defects to constants times
\(h^{14},h^{21},\ldots,h^{91}\), and then consumes the degree-\(3\) row
to a weight-\(98\) constant. Fourteenth consumes the degree-\(2\) row to
a weight-\(105\) constant (`localClearedFifteenthDefect810`). Pi consumes
the degree-\(1\) row to a weight-\(112\) numerator.

**Defect ceiling, row sense.** After Pi there is exactly one remaining
Keller coefficient: degree \(0\). There is no further first-integral
defect. That is the analogue of \(610\)’s fifteenth final row, not the
analogue of “jet quotient \(h\)-degree \(\le 6\)”.

**Defect ceiling, \(h\)-adic sense.** Not landed. See §3.

Both faces of \(N\) are kept: every scale-zero defect theorem has an
aligned (`λ=0`) and a nonzero (`λ≠0`) form, and every header says neither
face is closed. Root evaluation from a scale-two packet is unavailable,
because a nonzero constant has no finite root.

Frontier theorems to consume next on this chamber:

- landed: `normalized810ScaleZero_fourteenthClearedDefectFirstFace`,
  `piResidual810_deriv_zero_of_monic_differentialJacobian` (constant-core
  Jacobian is \(C(c)\), so \(\pi\) is a differential constant);
- missing: a degree-\(0\) source row, analogue of
  `alignedFinalCoefficientJacobianRow_410` /
  `LowScale610ScaleTwoFifteenthFinalRow`.

### 2.3 Scale-two: faces beyond the ninth

Tracked through the ninth face and the seventh packet. Ninth consumes
the degree-\(8\) Jacobian row (`ninthCoefficientJacobianRow_810`) and
does **not** clear a first integral: the header says the corresponding
defect is larger than the remaining exact jet. The strongest exact
output is the two-component packet
`normalized810ScaleTwo_nonzeroFace_ninthInitialPacket`.

**How many Keller rows remain to degree \(0\)?** Eight source-facing
rows: degrees \(7,6,5,4,3,2,1,0\). Pi already treats degree \(1\) as an
integral, so a sixteenth *face packet* is optional for the linear-root
chamber. Degree \(0\) is still required.

Untracked imports name at least a fourteenth and a fifteenth scale-two
face. Their packets are **UNVERIFIED**.

The aligned face \(N=0\) is refused in every scale-two \(810\) header.
That is a separate chamber, in the same position \(410\) was before
`Grok410ScaleTwoAlignedFaceClosureScratch`.

### 2.4 Ninth-face jet (the Pi peel’s parent)

On the nonzero face \(H=h_0^2\), \(N=C(\lambda)h_0^9\), \(h_0(a)=0\):

\[
p_7=h_0^6 t_0,\quad
p_6=h_0^3 v_0,\quad
p_5=h_0 u_0,\quad
q_8=h_0^5 s_0,\quad
q_7=h_0^3 w_0,\quad
h_0^8\mid q_9,\quad
h_0^2\mid q_6,
\]
and \(v_0=h_0 v_1\), \(s_0=h_0 s_1\), \(u_0=h_0 u_1\), \(w_0=h_0 w_1\).
Both components then have \(v_0=s_0=u_0=w_0=b_6=0\) at \(a\). Left keeps
\(t_0(a)\) possibly nonzero with
\(32s_1-40v_1=5t_0^2\) and
\(128w_1-160u_1-40 t_0 v_1+5t_0^3=0\). Right forces \(t_0(a)=0\) and
\(4s_1=5v_1\), \(4w_1=5u_1\).

The Pi unsolved peel substitutes the *left* orders
\(p_7=h^6 t_0\), \(p_6=h^4 v_1\), \(p_5=h^2 u_1\),
\(q_8=h^6 s_1\), \(q_7=h^4 w_1\), \(q_6=h^2 b_{62}\), and leaves
\(a_4,a_3,a_2,a_1,a_0,b_5,b_4,b_3,b_2,b_1\) unpeeled. That is the
handoff invariant: do not replace those letters by a scalar solve that
only holds modulo \(h\).

### 2.5 Pi frontier (what the five consumers actually prove)

1. `piResidual810` is the grouped exact primitive of the depressed
   degree-one row. Earlier residuals remain literal. Identity:
   \[
   d\pi
   =(2V_0\,dG+W\,dF-F\,dW-2E_0\,dX)
   +(\text{certificates})\cdot d(\alpha,\ldots,\xi,\kappa,\mu,\nu).
   \]
   On the residual-constant locus with vanishing degree-one Jacobian
   coefficient, \(d\pi=0\) (`piResidual810_deriv_zero`).

2. `piResidual810_deriv_zero_of_monic_differentialJacobian`: a constant
   depressed differential Jacobian makes \(\pi\) a differential constant.
   This uses Jacobian coefficients \(15\) through \(1\).

3. `piSourceClearingBridge810`: on the ninth-power face
   \(5a_7 h^2-4b_9=\lambda h^9\),
   \[
   2^{44}\,h^{112}\,\pi
   =\texttt{localClearedSixteenthDefect810},
   \]
   with \(2^{44}=17592186044416\). The \(762\)-term numerator is the
   blocked CommRing literal.

4. `localClearedSixteenthDefect810_left_unsolved_factored`: after the
   left orders of §2.4,
   \[
   Q=h^{96}(\texttt{piLeftUnsolvedHead810}+h\cdot\texttt{piLeftUnsolvedTail810}).
   \]
   The order-\(96\) head is not the zero polynomial (block 1 begins
   \(-5153960755200\,a_4^4\)).

5. `piSourcePowerRelation810_of_residual_eq_C`: if the depressed \(\pi\)
   equals a scalar \(\eta\) in \(\mathrm{RatFunc}\,k\), then
   \(Q=C(2^{44}\eta)\,h^{112}\). Combined with (4),
   `piLeftUnsolvedHead810` vanishes at every root of \(h\)
   (`piLeftUnsolvedHead810_eval_root_of_source_residual`).

There is no source wrapper that instantiates the affine-depression
Jacobian \(C(j/h_0)\) and then *proves* \(\pi=\eta\) from a
`(8,10)` source. DifferentialBridge assumes a constant depressed
Jacobian; SourcePowerBridge *assumes* `sourcePiResidual810 = C(η)`.
That missing wrapper is the first authoring step, in the same slot as
`Grok610DegreeZeroSourceWrapperScratch`.

---

## 3. Question 2: does the \(610\) bounded-tower method transfer?

### 3.1 What \(610\) actually does (committed pattern)

On the \(610\) nonzero linear-root face, after Backwire peel:

1. Source wrapper: affine depression sends the Keller identity to
   \(\mathrm{differentialJacobian}(\hat p,\hat q)=C(j/h_0)\).
2. The degree-**zero** primitive satisfies \(d(\mathrm{prim})=WE'-DX'\),
   which *is* the Jacobian, hence \(\rho'=C(j)/h_0\).
3. Clearing by \(h^{75}\) produces a polynomial \(Q\). Post-collapse,
   \(Q=h_0^{69}\cdot(\text{jet quotient})\), so \(h_0^6\rho\) is
   polynomial. Pole order \(6\); ceiling at order \(75\); at most seven
   frozen heads (orders \(69\) through \(75\)).
4. Head split \(p_{32}(a)=0\vee q_{41}(a)=0\), then a bounded tower.
   At the ceiling a polynomial cannot have derivative \(C(j)/h_0\) with
   \(j\neq 0\).
5. `Grok610DegreeZeroOrder75CeilingScratch` records arms \((a)(b)(c)\)
   closed and mixed arm \((d)\) not advanced. The method is committed;
   the chamber is not fully closed.

### 3.2 What transfers to the \(810\) degree-one row

| Quantity | \(610\) degree-zero | \(810\) degree-one (Pi) | Status |
|---|---|---|---|
| Clearing power | \(75\) | \(112=2^{44}\) displayed as \(C(2^{44}\eta)h^{112}\) | committed, `piSourcePowerRelation810_of_residual_eq_C` |
| Extracted vanishing order | \(69\) | \(96\) | committed, `localClearedSixteenthDefect810_left_unsolved_factored` |
| Formal \(h\)-degree of jet quotient | \(\le 6\) | \(\le 16\) | **derived**: \(112-96=16\), from the two displayed identities |
| Inclusive head count | \(69\ldots 75\) (seven) | \(96\ldots 112\) (seventeen) | derived, same arithmetic |
| Pole lemma | `localLinearPoleSix_…` | none | **OPEN** |
| Endgame derivative | \(\rho'=C(j)/h_0\) | \(d\pi=0\) on the residual-constant locus | committed; **not** \(j/h_0\) |
| Source wrapper | drafted in `Grok610DegreeZeroSourceWrapperScratch` | missing | **OPEN** |
| Honest jet letters | Backwire quotients | keep \(m_1,\tau_1,g_1,k_1\); do not scalar-solve the \(h^{97}\) jet | frozen invariant; the four letters are **UNVERIFIED** as Lean names |

The transfer of *shape* is: source wrapper \(\to\) head vanishing at the
linear root \(\to\) bounded \(h\)-adic tower whose ceiling is the
clearing power \(\to\) cancel-and-expose a polynomial in the remaining
\(h\)-degree. The transfer of the *endgame identity* is not.

### 3.3 Expected endgame identity (degree-one row)

From committed algebra, writing \(A_0:=\texttt{head}+h\cdot\texttt{tail}\):

\[
A_0 = C(2^{44}\eta)\,h^{16},
\qquad
\texttt{piLeftUnsolvedHead810}(a)=0.
\]

If one sets \(\rho:=A_0/(2^{44}h^{16})\), the power relation says
\(\rho=\eta\) as a rational function, hence \(\rho'=0\). That is the
honest degree-one identity:

\[
\rho\text{ is a polynomial (in fact a scalar)},\qquad \rho'=0.
\]

It is **not** \(\rho'=C(j)/h_0\). Using a simple-pole equation on this
primitive would be a pole identity without the matching Jacobian
coefficient. Typed **OPEN** for any claim that the Pi tower alone
contradicts \(j\neq 0\).

A ceiling at order \(112\) for \(\pi\) produces a finite list of scalar
equations on the unsolved jet, not a holomorphic-versus-simple-pole
kill. The last identity is of the form “order-\(112\) coefficient
equals \(2^{44}\eta\)”, which constrains the jet rather than emptying
the chamber.

### 3.4 Expected endgame identity (degree-zero row, unauthored)

Once \(\pi\) is a constant, the only surviving Jacobian coefficient is
degree \(0\). A primitive of that row — the object analogous to
`degreeZeroPrimitive610` — would have derivative equal to the full
depressed Jacobian.

- Scale-two linear root: affine depression of a `(8,10)` source is not
  a landed theorem. The \(68/610\) bridge
  `differentialJacobian_affineDepress_sourceToRatFunc68` gives
  \(C(j/h_0)\) for a sextic–decic pair. Whether the octic–decic
  depression has the same simple pole is **OPEN** (do not fill by
  analogy). If it does, the expected identity is
  \(\rho'=C(j)/h_0\) versus \(\rho\) polynomial after a (yet uncomputed)
  clearing power.
- Scale-zero: \(H\) is a nonzero constant, so there is no linear local
  parameter and no simple pole. The degree-\(0\) row is
  inhomogeneous in \(j\) as a polynomial identity. Closing that chamber
  is a constant-scale evaluation, not a pole tower.

### 3.5 Pole order

For the degree-one numerator, the unconstrained Laurent order before the
power relation is \(112\); after the unsolved \(h^{96}\) factorization
the remaining pole order of \(A_0/h^{16}\) is \(0\) once the relation
holds. The number \(16\) is the correct *ceiling* for the Pi jet, not a
landed pole-six-style lemma.

Python’s docstring calls \(\pi\) a “weight-\(16\) first integral”.
\(16\cdot 7=112\). That ratio is a generator comment, not a Lean
theorem. **UNVERIFIED** as geometry.

---

## 4. Question 3: ordered lane plan

Each step is one Grok Lean lane: one new `*Scratch.lean` (or one
commit of an already-green cache blob), one consumer, no bulk-add of
the historical scratch tree. Do not restart live AWS gates.

Prerequisite (coordinator, not a math lane): land the cache-hydrated
sixth–twelfth scale-zero defects and the residual definitions
\(\theta,\iota,\kappa,\mu,\nu\) as exact blobs, so a clean clone can
elaborate Pi Residual. Until that happens the Pi chain is
receipt-green and git-open.

### 4.1 Primary: scale-two linear-root, left component (610-style)

The handoff route. Consumes the ninth-face left jet and the five Pi
modules. Does not scalar-solve \(h^{97}\).

| # | Module to author | Consumes | Proves |
|---|---|---|---|
| P0 | `Sol810PiSourceWrapperScratch` | `piResidual810_deriv_zero_of_monic_differentialJacobian`, `piSourcePowerRelation810_of_residual_eq_C`, ninth packet, an octic–decic affine-depression Jacobian bridge (**OPEN** if the \(68\) sextic bridge does not apply) | \(\pi=\eta\) as a `RatFunc` identity on the residual-constant locus of a literal `(8,10)` source; discharges the assumed `hpi` of SourcePowerBridge |
| P1 | `Sol810PiHeadSplitScratch` | `piLeftUnsolvedHead810_eval_root_of_source_residual`, `piLeftUnsolvedHead810` as a polynomial in \((t_0,v_1,u_1,a_4,\ldots)\) | factorization of the order-\(96\) head at \(a\); keep \(m_1,\tau_1,g_1,k_1\) as first \(h\)-adic witnesses. Do not import the discarded LeftJetBridge draft |
| P2 | `Sol810PiOrder97Scratch` | P1, LeftUnsolved tail, retained witnesses | next frozen head after substituting \(\mathrm{coord}=\mathrm{value}(a)+h\cdot(\text{next})\) |
| P3–P16 | `Sol810PiOrder{k}Scratch` for \(k=98,\ldots,111\) | previous order | one frozen head per lane, same size as `Grok610DegreeZeroOrder72Scratch`–`Order74Scratch` |
| P17 | `Sol810PiOrder112CeilingScratch` | P16, the \(A_0=C(2^{44}\eta)h^{16}\) identity | last head of the degree-one tower; records remaining scalar equations; does **not** claim \(j\neq 0\) dies here |

If P1 splits into several arms, duplicate P2–P17 per arm rather than
enlarging a lane. Right-component specialization \(t_0(a)=0\) is a
separate thin consumer after P1, not a rewrite of the unsolved
factorization.

### 4.2 Degree-zero primitive (the actual \(610\) endgame object)

Only after \(\pi\) is a scalar. This is the row whose derivative can
meet \(C(j)\) or \(C(j)/h_0\).

| # | Module | Consumes | Proves |
|---|---|---|---|
| Z0 | `Sol810DegreeZeroRowScratch` | Jac coeff \(0\) of a monic octic–decic; analogue of `alignedFinalCoefficientJacobianRow_410` | the inhomogeneous identity, source-facing and depressed |
| Z1 | `Sol810DegreeZeroPrimitiveScratch` | Z0, residual-constant locus of \(\alpha\) through \(\pi\) | grouped primitive \(\rho\) with \(d\rho=(\text{degree-0 row})\) |
| Z2 | `Sol810DegreeZeroDifferentialBridgeScratch` | Z1 | \(d\rho=0\) iff the degree-0 coefficient vanishes; on a constant Jacobian, \(\rho'=c\) |
| Z3 | `Sol810DegreeZeroSourceWrapperScratch` | Z2, octic depression, scale-two linear root | \(\rho'=C(j)/h_0\) **or** a typed **OPEN** if the depression Jacobian is not a simple pole |
| Z4 | `Sol810DegreeZeroLocalPoleScratch` | Z3 | pole lemma with the *computed* pole order, not \(16\) copied from Pi |
| Z5 | `Sol810DegreeZeroClearingScratch` | Z1, CAS generator | integer numerator and clearing power (**OPEN** until computed; do not cap at \(112\)) |
| Z6+ | bounded tower, one frozen head per lane, ceiling at the Z5 power | Z4, Z5, ninth (or post-Pi) jet | cancel-and-expose \(\rho\) polynomial versus the Z3 derivative equation |

Z5’s clearing power is a new calculation. Filling it by \(112\) or by
the \(610\) value \(75\) is forbidden.

### 4.3 Parallel: scale-two face cascade (410-style)

Use this if the Pi tower’s remaining scalar equations do not empty the
linear-root chamber, or to refine the jet for a valuation kill.

\(410\) closed the nonzero face by: face cascade to the degree-\(0\)
row \(\to\) polar collapse (\(p_1(a)=0\) from an order-\(-3\) block)
\(\to\) valuation exhaustion \(h^4\mid(h^4)'\). Eight \(810\) faces
remain; \(410\) had five after its eighth face. Size each face as one
lane, matching `LowScale810ScaleTwoNinthFace.lean`.

| # | Module | Consumes | Proves |
|---|---|---|---|
| F10 | `LowScale810ScaleTwoTenthFace` (or Fable/Grok scratch) | Ninth packet | degree-\(7\) row and the strongest exact jet refinement |
| F11–F15 | Eleventh through Fifteenth | previous | degrees \(6\) through \(2\); Fifteenth already named as an import |
| F16 | optional; Pi already owns degree \(1\) | F15 | only if a source-facing packet is still needed |
| F17 | `LowScale810ScaleTwoFinalRow` | F15/Pi | degree-\(0\) row on the cascade jet |
| F18 | `Grok810ScaleTwoCascadeEndgameScratch` | F17 | polar collapse of a named first integral, then a valuation kill on the supplied source and the supplied root |

Do not claim F18’s valuation identity in advance. \(410\)’s
\(h^4\mid(h^4)'\) is that leaf’s jet, not this one.

### 4.4 Scale-zero remainder

No linear root. The Pi tower’s root peel does not run.

| # | Module | Consumes | Proves |
|---|---|---|---|
| S6–S12 | commit the already-green sixth–twelfth defects | Fifth, then each predecessor | weights \(h^{49}\) through \(h^{91}\) as ground constants on both faces of \(N\) |
| S0 | `LowScale810ScaleZeroFinalRow` | Fourteenth + Pi + Z0 | degree-\(0\) row at constant \(H=C(t)^2\); both \(\lambda=0\) and \(\lambda\neq 0\) |
| S1 | constant-scale evaluation / degree kill | S0 | either a polynomial-degree contradiction in \(k[X]\) or a typed **OPEN** |

S6–S12 are custody if the cache already has receipts; do not re-author
literals.

### 4.5 Aligned scale-two face \(N=0\)

Separate chamber. \(410\) closed it by an aligned first-integral ladder
through degree \(0\), then square/nonsquare valuation kills, then the
scale-zero adapter. Nothing in the \(810\) tracked chain opens \(N=0\).
First lane: `LowScale810ScaleTwoAlignedFace`, consuming only
`normalized810ScaleTwo_discriminatorFirstFace`’s left disjunct. Do not
import linear-root packets.

### 4.6 What not to author

- A scalar-solved \(h^{97}\) jet that eliminates \(m_1,\tau_1,g_1,k_1\).
- `Sol810PiLeftJetBridgeDraftScratch`.
- A pole-sixteen lemma with derivative \(j/h_0\) attached to \(\pi\).
- A twice-prime or total-degree closure of this leaf.
- Copying \(610\)’s clearing power \(75\) or pole order \(6\), or
  \(410\)’s \(h^4\mid(h^4)'\), onto \(810\).

### 4.7 Suggested start order

P0 (source wrapper) is the unique blocker for every later Pi-tower
lane: without it, SourcePowerBridge’s `hpi` remains an assumption.
In parallel, Z0 (degree-zero row) is the unique blocker for the actual
simple-pole endgame, and the custody commit of sixth–twelfth makes the
Pi import chain source-honest. F10 is optional until P1 shows that the
ninth jet is insufficient.

---

## 5. FALLACY-v2 controls

- No flag / place / series identification. No exit-price, so no
  `charge_basis` line.
- Pole identities are used only where the vertex class is the scale-two
  nonzero square core \(H=h_0^2\), \(\lambda\neq 0\), \(h_0(a)=0\), and
  every source hypothesis of the cited theorem is present. The Pi
  derivative is *not* treated as a simple pole.
- \(112-96=16\) is an equality of displayed polynomial identities, not
  a floor promoted to attainment.
- Prime marks on compact coordinates mean the next Taylor coefficient
  at \(a\), except where a source defines `Polynomial.derivative`.
- `REPRESENTATIVE` ninth-face letters \((t_0,v_1,\ldots)\) are packet
  coordinates, not `FULL_ACTUAL_EXIT`.
- Missing octic–decic depression Jacobian, missing degree-zero
  primitive, missing aligned-face packets, missing sixth–twelfth blobs:
  typed **OPEN**, not filled by the \(410\) or \(610\) numbers.

---

## 6. What this map is not

It is not a closure of `(8,10)`. It is not a kernel check of the Pi
scratch. It is not a CAS recomputation of the \(762\)-term numerator or
of the unsolved head. It does not read untracked sixth–twelfth or
scale-two fourteenth/fifteenth files. Claims that those modules exist
in an AWS cache are handoff text, **UNVERIFIED** from this clone.
