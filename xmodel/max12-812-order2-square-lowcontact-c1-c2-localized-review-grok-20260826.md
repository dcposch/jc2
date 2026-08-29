# Hostile review: localized low-contact `c=1,2` square gate

Date: 2026-08-26
Reviewer: grok-4.6 (read-only except this report; no Singular/Sage/Lean/solver; no live `.run` transcript)
Target: `cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/RESULT.md`

**Verdict: `CONFIRMED`.**

No load-bearing identity failed.  The exact-Q run proves the two scoped implications on the generic-square first-normal open `D(p*k0)`: the `c=1` leading correction vanishes integrally, and the `c=2` leading correction vanishes after saturation by `p*k0`.  This is arcwise/set-theoretic contact-raising of those two finite leading corrections, and no more.

## Firewall (enforced)

Licensed claim is at most the finite `c=1,2` leading corrections on the generic-square first-normal chart `D(p*k0)`.  It does **not** cover positive horizontal contact of `A`, `p=0`, `k0=0`, the exact-square zero section, fan exhaustiveness, the whole square branch, exact order two, maximum twelve, or JC2.  The producer states this and the evidence does not overreach it.

## Hashes actually verified

Advertised hashes, recomputed on disk with SHA-256:

| Object | SHA-256 | Status |
|---|---|---|
| V4 `RESULT.md` | `b8ae74e5ca69b50ee346c2a11acf3282bf68bd42522fa9a10bab537d7ab14e7d` | match |
| V4 `RESULTS.sha256` (result manifest) | `6931164bb265fc94deb4241b280a02a1110c120dc4cfe1664e38e3a3e3af7da1` | match |
| V4 `FREEZE.sha256` | `beea0c90fad4da24b386333917f2fea445ae941ad059e0ec2a4ceb69fe77123e` | match |
| V3 `FREEZE.sha256` | `676f97810cc0c758ba864efe3463c2798f3c5d8f3fd70d57dee8ba0fb7457b57` | match |

Every path inside both freeze files and inside V4 `RESULTS.sha256` was rehashed and matched.  In particular:

- V4 freeze: `REGISTRATION.md` `3979d38e…`, `compile_delta_v4.py` `e78e4473…`, `run_aws.sh` `b5980e8f…`, `launch_host.sh` `a49ab903…`
- V3 freeze: `REGISTRATION.md` `ae310808…`, `compile_rootwise_v3.py` `2fa4cabd…`, `run_aws.sh` `7958cb9b…`, `launch_host.sh` `ad2a5bab…`
- V4 exact-Q compiled input `square_lowcontact_c2_localized_delta_v4_q.sing` `82b422dc…`
- V4 exact-Q stdout `0c44047c…`, validation `c014ece4…`, meta `d32f5f6a…`
- V4 `compiler.stdout` `f1a4d5be…`, `launch_registration.txt` `cbe7eb56…`
- V3 exact-Q stdout `1c5399e0…`, V3 `F_65521` stdout `718d1c4c…`

Parent pins reached by the explicit compiler hash chain also matched on disk:

- V2 freeze-file `d7333dd0…` and V2 compiler `cbeab153…`
- V1 low-contact compiler `85c411a3…` and its freeze-file `a35b0784…`
- CGE compiler `352ad4f2…` and its freeze-file `a5efc70c…`
- pinned `tails.json` `d72f774c…` and load-ladder compiler `77f25216…`

Nested compiled inputs inside the V4 job match the compiler JSON pins: V2 `e8f26213…`, V3 `0f94e059…`, V4 `82b422dc…`.  The V3 exact-Q compiled `.sing` is byte-identical to the V4 nested V3 input (`0f94e059…`).  The V3 `F_65521` compiled `.sing` is `749b3808…`, matching that lane’s `compiled.sha256`.

Engine stderr hashes also match the corresponding `.meta` records: V4 `42a99fff…`, V3 Q `2cde9fb0…`, V3 `F_65521` `2f4f8760…`.  V4 `compiler.stderr` is the empty-file digest `e3b0c442…`.  V4 `compiler.validation` is exactly `compiler_rc=0`.

## 1. Custody, engine exit, validator

Frozen-source → compiled-input → AWS-output chain:

1. V4 `run_aws.sh` refuses non-Linux/non-EC2, `sha256sum -c` the V4 freeze (recorded `freeze_check.stdout` all OK), then runs `compile_delta_v4.py`.
2. That compiler re-pins V3 compiler `2fa4cabd…` and V3 freeze `676f9781…`, recursively compiles V3 (which re-pins V2, which re-pins V1 and CGE and `tails.json`), then performs a unique textual replacement of the unlocalized `c2root` test by the saturation/delta printer.
3. `compiled.sha256` records the compiled input `82b422dc…` (AWS path, same digest as the vendored `.sing`).
4. Lane `max12_812_order2_square_lowcontact_c2_delta_v4_q_20260826T094000Z_box03` on Box03.  `.meta` has `rc=0`, stdout/stderr digests as above.  `/usr/bin/time` stderr has `Exit status: 0`.  `.validation` is
   ```
   engine_rc=0
   validator=PASS_LOCALIZED_MEMBERSHIP
   ```
   not a free-floating PASS token.

The validator is the frozen `run_aws.sh`: it writes `engine_rc`, rejects timeout/`FAIL_ENGINE`, requires unique copies of the c1 endpoint, raw non-membership, localized properness, and the four delta fences, rejects `^\? ` diagnostics, and writes `PASS_LOCALIZED_MEMBERSHIP` only if `SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED=1` is present.  That last flag is `c2root=(c2DeltaLocal==0)` in the compiled input.  Stdout also prints the localized polynomial `0` between the localized-delta fences.  Both the integer flag and the displayed remainder were inspected.

V3 controls: both lanes have `compiler_rc=0`, freeze checks OK, `engine_rc=0` / time `Exit status: 0`, and validator
`FAIL_MISSING_OR_NONUNIQUE:SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED=1`.
That is the intended negative-control failure, not an engine crash.

## 2. Seven source/Faber rows, chart, normalization

Compiled V4 input contains `c1Phi1`–`c1Phi7` and `c2Phi1`–`c2Phi7`.  Each is the load-ladder `tail_text` of the pinned `tails.json` row, with `Lambda=sigma^2`, moving square coefficients, loads `k10=k0+sigma*k1`, `k6`, `k2`, radial `R=(pp^2+sigma^3 br+…)/4`, and the even-row targets `mu2`, `mu4`, `mu6`, `J/4` subtracted at `sigma^{2(12+row)}`.  No row is omitted.  Exact division identities and the forbidden-variable sentinels all printed `=1`; the script would `quit` on a dropped term at the relevant grades.

Normalization on the generic-square first-normal chart:

- `p` is the leading square modulus: `L0=z^2+p/2`, `sp=p/2+sigma*ell1(+sigma^2*ell2)`, `pp=2*sp`.
- `ell1` (and `ell2` at `c=2`) are the moving-`p` corrections.
- `k0` is the leading `k10` load: `kk=k0+sigma*k1`.
- `A` is the linear form `A0z=a1*z+a0` (`AA` is the `t=1/z` version).
- `E` / leading `C` is `E1z=(e11*z+e10)/2` at `c=1` and `E2z=(e21*z+e20)/2` at `c=2`.
- `B` / radial odd-even pair is `Bz=sigma*(bs1*z+br1/4)+…`; `R` is the even square load above.
- `L` is the moving square polynomial `Ls=z^2+sp`.

`c=1` forbids `k0,k1,k6,k2,mu*,J,bs1,br1` in the extracted grade-11/12 source coefficients.  `c=2` forbids only `k6,k2,mu*,J`, so `B` and `k0` remain.  That is the correct low-contact truncation, not a silent drop of a load that still contributes at those grades.

The affine analytic model `Hshift` and the `z`-numerator `Num` represent the same rational section: `Hshift = t * Num / Ls^2`.  Every displayed `c=1` and `c=2` summand matches under `t=1/z`, `AA=Az/z`, `EE=Ez/z`, `BB=Bz/z`, `Inv1=z^2/Ls`, `Inv2=z^4/Ls^2`.  Inverse series are the binomial expansions of `(1+sp t^2)^{-1,-2}` through `t^{10}`, which covers the extracted Taylor rows `t^2` through `t^8`.

## 3. Lower-unitriangular Laurent bridge

`transform_series(i,j)` is the coefficient list through `sigma^2` of `T_{ij}(p+2 sigma ell1+2 sigma^2 ell2)`: zero for `i<j` or odd `i-j`, unit diagonal, and the Pochhammer/binomial values on even subdiagonals.  Compiled checks match those coefficients by hand, including the `sigma^2` block (e.g. `c2Check14_7` contains `(5/128)p^3`, `(15/64)ell1 p^2`, and `(15/64)ell2 p^2+(15/32)ell1^2 p`).  V3’s `c1h* → c1ah*` / `c2h* → c2ah*` rename makes the bridge read the actual Laurent Taylor names; the unrepaired `c1h11_1` family is absent.

Unitriangularity over `Z[p,ell1,ell2]` inverts on the finite `7×7` block.  Source rows `g` vanish if and only if Laurent rows `h` vanish.  That is equivalence of the full seven-dimensional square-chart section to the analytic model, not a proper projection.  All fourteen `c=1` checks and all twenty-one `c=2` checks printed no remainder; `SQUARE_ROOTWISE_C1_ROW_IDENTITIES=1` and `SQUARE_ROOTWISE_C2_ROW_IDENTITIES=1`.  Division recurrences `L0^2 P = H-R` printed `=1`, and remainder `z`-degree `<4` printed `=1`.

## 4. Integral `c=1`

Grade 11 of `Num` is `(3/4) A0z E1z L0`.  `R11=reduce(H11,L0^2)` therefore vanishes as a polynomial in `z` iff `L0` divides `A E`.  The ideal `c1G=(L0,` four Taylor coefficients of `R11)` is that divisibility together with `L0=0`.  The moving correction is `C12=H12-2 L0 ell1 P11`, which is the `sigma^1` transport of the double pole of `L_sigma^{-2}`.  The engine reports `reduce(C12-(3/8)E1z^2,c1G)==0` as a polynomial identity in the ambient ring (characteristic 0, no saturation, no radical).

On `D(p)`, `L0=z^2+p/2` is squarefree of degree 2.  `A E` has degree 2, so `L|AE` as polynomials is equivalent to vanishing at both roots, with no extra reducedness hypothesis: the membership is in `Q[z,parameters]`, and the identity does not pass through `radical()`.  At a root with `A≠0`, `E=0` already from grade 11.  At a root with `A=0`, grade 12 gives `(3/8)E^2` as the polar remainder; the source/Laurent vanishing sets that remainder to 0, so `E^2=0` there.  Restricting the integral identity to the smaller open `D(p*k0)` is valid.  `k0` is absent from the `c=1` analytic model and forbidden in the `c=1` source coefficients.

## 5. V3 negative controls

Both V3 exact-Q and `F_65521` print

```
SQUARE_LOW_C1_DIVISIBLE=1
SQUARE_LOW_C1_IDENTITIES=1
SQUARE_LOW_C1_FORBIDDEN=1
SQUARE_ROOTWISE_C1_ANALYTIC_DIVISIBLE=1
SQUARE_ROOTWISE_C1_ROW_IDENTITIES=1
SQUARE_ROOTWISE_C1_DIVISION_RECURRENCE=1
SQUARE_ROOTWISE_C1_REMAINDER_DEGREE=1
SQUARE_ROOTWISE_C1_G12_MOD_LOWER_EQUALS_THREE_EIGHTHS_C1_SQUARED=1
SQUARE_ROOTWISE_C1_ENDPOINT=PASS_LEADING_C1_KILLED
SQUARE_LOW_C2_DIVISIBLE=1
SQUARE_LOW_C2_IDENTITIES=1
SQUARE_LOW_C2_FORBIDDEN=1
SQUARE_ROOTWISE_C2_ANALYTIC_DIVISIBLE=1
SQUARE_ROOTWISE_C2_ROW_IDENTITIES=1
SQUARE_ROOTWISE_C2_DIVISION_RECURRENCE=1
SQUARE_ROOTWISE_C2_REMAINDER_DEGREE=1
SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED=0
SQUARE_ROOTWISE_C2_FAIL=BRIDGE_OR_ROOT
```

They fail only the unlocalized `c=2` membership.  V3 does not print the remainder polynomial.  V4’s unlocalized `reduce(C14-(3/8)E2z^2,c2G)` is the same polynomial on the same `c2G` as V3 exact-Q (nested V3 `.sing` digest identical), and V4 prints

```
3/8*ell1*a0*a1*bs1+3/32*ell1*a1^2*br1
```

which is the advertised `(3/8)*ell1*a0*a1*bs1+(3/32)*ell1*a1^2*br1` up to Singular syntax.  `F_65521` confirms the same non-membership; it does not re-print the `Q`-normal form, and is not required to.  This is a negative control, not a theorem failure.

## 6. `sat(c2G,ideal(p*k0))`

`elim.lib` / `primdec.lib` `sat` returns the saturation `I:J^∞` as list `[saturated ideal, exponent]`.  The compiled line is `ideal c2Gpk=std(sat(c2G,ideal(p*k0)))`.  That is localization to `D(p*k0)`: `f` lies in the extension of `c2G` to `Q[x][1/(p k0)]` iff some `(p k0)^N f` lies in `c2G` iff `f` lies in the saturation.

Two engine facts kill the standard list/ideal coercion false-positives:

- `SQUARE_ROOTWISE_C2_LOCALIZED_IDEAL_PROPER=1` means `reduce(1,c2Gpk)!=0`.  If the saturation exponent had been coerced in as a nonzero constant, characteristic 0 would have produced the unit ideal and this flag would be `0`.
- Localized remainder `0` means the tested polynomial lies in `(c2Gpk)`.  Dropping saturation generators would shrink the ideal and make membership *harder*; it cannot manufacture a false `reduce==0`.  Adding the exponent as a unit *would* manufacture one, and is already ruled out by properness.

No `^\? ` diagnostic appears.  `c2G` is already `std(...)`; the outer `std` is a Groebner basis of the saturated ideal in the ring ordering `dp`, with no extra `std` flags.  Displayed obstruction reduces to `0` there.  The localized ideal is proper, so the open `D(p*k0)` still meets the locus.

## 7. Pointwise/rootwise implication

Lower rows:

- Grade 12: `H12=(3/4)A0z E2z L0` plus higher-contact terms that start later, so `R12=0` is `L|A E`.
- Grade 13: moving transport `C13=H13-2 L0 ell1 P12`; its remainder is the intermediate polar part, included in `c2G`.
- Grade 14: `C14=H14-2 L0 ell1 P13-(2 L0 ell2+ell1^2)P12` is the full double-pole correction through `sigma^2`.  This is the expansion of `L_sigma^{-2}` and was checked by hand.

`c2G` contains `L0` and `A0z`, so the grade-14 sentinel is the identity at an `A`-root of `L`.  After localization, `C14=(3/8)E^2` there.  Source/Laurent vanishing kills the polar part, hence kills `E^2` at that root.

At a root with `A≠0`, grade 12 already gives `A E=0` hence `E=0` (A is a unit in the local ring at that point; no reducedness needed).

Why `p≠0` makes `L` squarefree and why two roots exhaust the linear correction: `L0=z^2+p/2` has discriminant proportional to `p`.  On `D(p)` there are two distinct roots.  `E2z` is linear in `z`.  A linear polynomial vanishing at two distinct points is identically zero, equivalently `L|E` with `deg L=2>deg E=1`.  This is a polynomial statement and does not allocate roots in an algebraic closure.

Why `k0≠0`: the raw remainder is a `B`-obstruction with no explicit `k0`, but `c2G` knows `k0` through the `kk B^3`, `kk B E`, and `kk A^2` numerator terms.  Saturating by `k0` (together with `p`) is exactly what cancels that remainder.  On `k0=0` those relations drop and the displayed `B`-obstruction is allowed to survive; that stratum is out of scope.

## 8. Localized membership vs reduced scheme vs arcs

What is proved is exact ideal membership of `C14-(3/8)E^2` in `sat(c2G,(p k0))`, plus the integral `c=1` membership of `C12-(3/8)E^2` in `c1G`.  Neither test uses `radical()`.  Saturation commutes with taking points of `D(p k0)`: a point with `p k0≠0` lies on `V(c2G)` iff it lies on `V(sat(c2G,(p k0)))`.  It does not radicalize, and it does not assert that the quotient is reduced.

Geometric reading over a field: `E=0` at both roots of squarefree `L`, hence `E≡0` as a linear form.  That is set-theoretic contact-raising of the leading correction on `D(p*k0)`.  Reduced arcs (`k[[t]]`, or any reduced DVR with `p k0` a unit on the generic point) are therefore killed.

Nilpotent arcs through an `A`-root see only `E^2=0` from grade 14.  The producer does not claim `E∈sat(c2G,(p k0))` and explicitly refuses a reduced-scheme assertion.  That is the correct ceiling: arcwise/set-theoretic vanishing of the leading corrections, including reduced arcs and the support of nilpotent arcs, and no scheme-theoretic reducedness.

No algebraic-closure gadget is used in the engine.  The case split “`A`-root vs `A`-nonzero root” is interpretive over the two geometric points of `V(L)` on `D(p)`; computationally `A0z` is simply a generator of `c2G`.

## 9. Firewall, again

The compiled `result.json` scope is `DIAGNOSTIC_D_P_K0_ONLY_NO_SQUARE_OR_ORDER2_VERDICT`.  Registration, `RESULT.md`, and this review all stop at the finite `c=1,2` leading corrections on `D(p*k0)`.  Positive horizontal contact of `A`, `p=0`, `k0=0`, the exact-square zero section, fan exhaustiveness, the whole square branch, exact order two, maximum twelve, and JC2 remain untouched.

## Short lemma chain

1. Frozen V1 source + load ladder emit all seven square-chart rows at the advertised grades, with moving `p`, `k10`, `R`, and the fresh `A,E,B` corrections; extracted low-grade pieces omit only the loads that the forbidden sentinels prove are absent.
2. The moving Laurent transformation `T_{ij}` is lower-unitriangular through `sigma^2`, so those seven source rows vanish iff the analytic Laurent Taylor rows vanish.  Affine `Hshift` and `z`-numerator `Num` are the same section.
3. Grade 11/12 polar calculus on `Num` yields the integral identity `C12-(3/8)E1z^2 ∈ (L0,R11)`.  On `D(p)`, squarefree quadratic `L` and linear `E` force the `c=1` leading correction to vanish set-theoretically, with no hidden reducedness.
4. The same calculus at `c=2` produces a proper ideal `c2G=(L0,A0z,R12,R13)` in which `C14-(3/8)E2z^2` is *not* a member; the explicit remainder is `(3/8)ell1 a0 a1 bs1+(3/32)ell1 a1^2 br1`.  V3 exact-Q and `F_65521` retain that as a negative control.
5. `sat(c2G,(p k0))` is localization to `D(p*k0)`.  The saturated ideal stays proper and the remainder becomes 0.  List/ideal coercion cannot fake this pair of facts.
6. Grade 12 gives `L|A E`.  At an `A`-nonzero root this kills `E`.  At an `A`-root the localized grade-14 identity kills `E^2`.  Two distinct roots of squarefree `L` exhaust linear `E`.  `k0≠0` is required for the `B`-obstruction to be torsion.

## Residual non-failing remarks

- `c1ndiv`/`c2ndiv` (numerator `sigma`-divisibility) are computed and then ignored in the product of sentinels.  The missing check is structural: `Ez` starts at `sigma^{c}` so `Num` starts at `sigma^{10+c}`.  Not a false identity.
- V4’s validator is thinner than V3’s (it does not re-list every source/Laurent token).  The compiled script still `quit`s on those failures, and the tokens are present in stdout.
- `F_65521` does not reprint the `Q` remainder polynomial.  The producer does not claim that reprint.

No smaller identity failed.

`ORDER2_SQUARE_LOWCONTACT_LOCALIZED_CONFIRMED`
