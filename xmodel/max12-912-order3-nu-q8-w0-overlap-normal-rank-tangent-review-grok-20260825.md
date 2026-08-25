# Hostile review: raw-overlap normal-rank/Fitting and ordinary tangent package

Date: 2026-08-25  
Reviewer: independent hostile algebraic-geometry / source-fidelity referee (Grok; different model from the producer lane).  
Targets: `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-fitting-20260825.md` and `xmodel/max12-912-order3-nu-q8-w0-overlap-horizontal-tangent-20260825.md`.  
Cases: `cases/max12_912_order3_nu_q8_w0_overlap_normal_rank_fitting_aws_20260825/` and `cases/max12_912_order3_nu_q8_w0_overlap_horizontal_tangent_aws_20260825/`.  
Verdict: **CONFIRMED**.

No source-identity, Fitting-formula, rank-drop, tangent-coordinate, residual, or firewall defect requiring repair. Process hardenings in §8 do not disturb the frozen claims.

## 0. Execution-environment disclosure

This review used nThe review is in `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-tangent-review-grok-20260825.md`.

The two reports survive a hostile source-fidelity audit. The imposed source is exactly `(e1,e3,e5,e7,e2,e4)` on the raw overlap `w=x1=x3=x5=0`, with no hidden load or terminal. Hand expansion confirms `L2=(2/9)F2`, `L4=(-4/27)F4`, the reduced two-point scheme `(d2-2 d4, d4(d4-2))`, the boundary-sheet tangent at `(0,0)`, the residual `729 L7=-432` at `(4,2)`, and the doubled rank-drop `(d2-d4-1)^2`. Fitting `K3=(d2,d4)` is actual rank-three incidence, not a saturation ghost of the drop line; `K2=K1=K0=(1)` empties the lower strata. Custody is engine/order/host independence of one mathematical lineage. Ordinary first-order/`delta w=1` facts only.

CONFIRMED
56`, `generator.stderr`), and `aws_box02_replay/`.
- Tangent case: `PREREGISTRATION.md`, `README.md`, `generate.py`, `generate_v2.py`, `generate_v3.py`, `replay.py`, `run_remote.sh`, `run_v2_remote.sh`, `run_v3_remote.sh`, `MANIFEST.sha256`, `FREEZE.sha256`, both preregistration hash files, `V2.manifest.sha256`, `V3.manifest.sha256`, both AWS `v3` endpoint trees, and `aws_box02_replay/`.
- Pinned quotient compiler `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py` (through `compile_quotient`, including `imposed = (1, 3, 5, 7, 2, 4)` and `APPROX_NAMES`).

## 2. Attack 1 — imposed source and raw overlap

Both generators call `Q.compile_quotient("approx")` and refuse to emit if `tuple(imposed) != (1, 3, 5, 7, 2, 4)`. The compiler hard-codes that tuple and `APPROX_NAMES = ["w", "c", "d2", "d4", "x1", "x3", "x5"]`. Frozen `input.sing` on all four accepted endpoints writes the eight approximate-cubic tails and then imposes exactly

```text
I = (e1, e3, e5, e7, e2, e4)
```

The unused rows `e6,e8` are compiled into the ring and then ignored: they do not enter `I`, `M`, `N`, or any `L_i`. That is the Q8 six-row source, not a hidden terminal. Chart `k=0` is already inside the pinned converter (monomials with `ek` are skipped); it is not an extra equation.

The raw overlap is exactly the ideal `(w, x1, x3, x5)`:

- Fitting: `ideal A3=w,x1,x3,x5;` then `reduce(I[ir], GA3)` and Jacobian entries reduced by `GA3`.
- Tangent: `ideal E=w,x1,x3,x5;` then each `L_i` reduced by `GE`.

No generator, runner, or frozen input saturates at `w`, at `x5*(x3-2*x5)`, or at any other load. The selected load appears only as future work in the Fitting remaining-gate paragraph. Both packages print `a3_source_rows_zero=1` (Fitting) or work entirely after reduction to `E` (tangent). Hand inspection of `e1..e8` on `w=x1=x3=x5=0` confirms every monomial carries a positive power of `w` or of an `x`-variable, so the six imposed rows vanish on `A3`.

Source identity holds.

## 3. Attack 2 — `M`, `N`, Fitting formulas, and saturation artifacts

Fitting constructs a `6 x 3` matrix `M` whose rows are the imposed source in order `(e1,e3,e5,e7,e2,e4)` and whose columns are `reduce(diff(row, x1|x3|x5), GA3)`, and `N=[M|F_w]` with fourth column `reduce(diff(row, w), GA3)`. Tangent-coordinate columns in `(c,d2,d4)` are separately required to vanish on `A3`; both accepted stdout files print `a3_tangent_columns_zero=1`. Hand differentiation of `e1,e2,e4` on `A3` confirms those three columns are zero; the remaining rows are of the same shape (every `c,d2,d4` derivative still carries `w` or an `x`).

Consequently the ordinary `delta w=1` equation on `A3` is

```text
M (dx1, dx3, dx5)^T + F_w = 0,
```

i.e. `rank(N)=rank(M)`. The four printed ideals are the standard Fitting closures of that incidence on the exact-rank strata of `M`:

```text
K3 = I4(N) : I3(M)^infinity
K2 = (I3(M)+I3(N)) : I2(M)^infinity
K1 = (I2(M)+I2(N)) : I1(M)^infinity
K0 = I1(M) + (entries of F_w)   = I1(N)
```

Frozen `input.sing` emits *all* minors (`20` of size `3` on `M`, `45` of size `2` on `M`, `18` of size `1` on `M`, `15` of size `4` on `N`, `80` of size `3` on `N`, `90` of size `2` on `N`, last generator `N2m90`) and then

```text
list LS3=sat(IN4,IM3); ideal K3=LS3[1];
ideal P2=IM3,IN3; list LS2=sat(P2,IM2); ideal K2=LS2[1];
ideal P1=IM2,IN2; list LS1=sat(P1,IM1); ideal K1=LS1[1];
ideal K0=IM1, N[1,4], ..., N[6,4];
```

Singular `elim.lib` `sat(I,J)` is saturation at the ideal `J`, which is the correct operation for removing `V(I_r(M))`. `K0` is not saturated: the rank-`0` locus is already closed.

**What saturation licenses, and what it does not.** `K_r` is the *Zariski closure* of exact-rank-`r` incidence. A rank-drop point can appear in `K3` as a limit even if it is not itself rank `3`. That artifact is absent from the computed output:

- both engines print `GK3 = (d4, d2)` with `K3_unit=0` and `K3_Dd2_empty=K3_Dd4_empty=1`;
- so as a subset of `A3 ≅ A^3_{c,d2,d4}` one has `V(K3) = {d2=d4=0}` (the `c`-line);
- the rank-drop support is `{d2-d4=1}`;
- `(d2,d4) + ((d2-d4-1)^2) = (1)` even scheme-theoretically, so `V(K3)` does not meet the rank-drop, reduced or fat.

Therefore `K3=(d2,d4)` licenses actual exact-rank-three ordinary `delta w=1` incidence along `d2=d4=0`, not a closure ghost of the drop line. `K2=K1=K0=(1)` licenses that the closures of exact-rank `2,1,0` incidence are empty, hence those strata contain no ordinary `delta w=1` tangent. Because `sat(I,(t^2))=sat(I,(t))`, the doubled scheme structure of `I3(M)` does not change `K3`.

The ideals live in the ambient ring `(w,c,d2,d4,x1,x3,x5,id2,id4)` because the Jacobian was reduced onto `A3` rather than the ring being quotiented by `A3`. Variables `w,x1,x3,x5` do not appear in the printed bases; the licensed object is the subset of `A3` with those `(c,d2,d4)` coordinates. That is the correct convention for an `A3`-restricted Jacobian.

Hand check of rows `5,6` of `M`: every `x`-derivative of `e2` and of `e4` vanishes on `A3`, so those two rows are identically zero. Rank of `M` is the rank of the `4 x 3` block `(e1,e3,e5,e7)`. On the drop line `d2=d4+1` one has `row(e5)=row(e1)` and `row(e7)=2·row(e1)`, so rank `≤ 2` everywhere on the line. At `(d2,d4)=(2,1)` the surviving row is `(1,0,0)` (up to units), so rank drops further to `1`. Rank never hits `0`. `K1=(1)` therefore also excludes a tangent at this rank-one point of the drop line, which the reports do not name but which their Fitting output covers.

## 4. Attack 3 — rank-drop polynomial and the strict first-order Fitting conclusion

Both engines print

```text
GM3[1] = d2^2 - 2*d2*d4 + d4^2 - 2*d2 + 2*d4 + 1
```

and the algebraic identity

```text
(d2 - d4 - 1)^2 = d2^2 - 2*d2*d4 + d4^2 - 2*d2 + 2*d4 + 1
```

is immediate. The printed reduced basis is the square, not the linear form `d2-d4-1`, so the scheme structure is doubled: `I3(M)=(t^2)` with `t=d2-d4-1`, not `(t)`.

Hand expansion of the `3 x 3` minor on rows `(e1,e3,e5)` of the cleared integer matrix equals `-27 t^2` at the origin, along `d4=0`, along `d2=0`, and at `(3,1)`. Combined with the printed GB being `t^2` rather than `t`, this licenses `I3(M)=(d2-d4-1)^2` as a principal ideal over `Q`, not merely set-theoretic rank drop.

Together with §3:

- exact rank three ordinary `delta w=1` incidence is the reduced line `d2=d4=0` in `A3` (`c` free);
- that line is disjoint from the drop line, so it really is rank three (at the origin the `e1` row is `(0,0,4/9)`);
- exact ranks `2,1,0` contribute no ordinary `delta w=1` tangent.

That is all the Fitting package licenses. It does not license a tangent through the drop line, a ramified/weighted arc, or uniqueness of the `c`-line among non-ordinary deformations.

## 5. Attack 4 — `L2`, `L4`, two-point scheme, branch zero, and `(4,2)` residual

Frozen polynomials (identical on Box02 `std/dp` and Box03 `slimgb/block`):

```text
L2 = 2/9 d2^2 - 8/9 d2 d4 + 2/3 d4^2 + 4/9 d4
L4 = -8/27 d2^2 + 20/27 d2 d4 - 4/9 d4^2 + 4/9 d2 - 16/27 d4
```

These match the producer display (same rationals, opposite monomial-print convention). They are not an artifact of row order: tangent `L_i` is named by the original index `i`, while Fitting `M` uses imposed order `(e1,e3,e5,e7,e2,e4)`. No mismatch.

**Derivation from the source, by hand.** On `A3`, every `c,d2,d4,x`-derivative of `e2` and of `e4` vanishes, so `L2=∂e2/∂w|_{A3}` and `L4=∂e4/∂w|_{A3}`. Direct restriction of those two `w`-derivatives reproduces the displayed polynomials exactly.

**Equivalence to the preregistered pair.** With `u=d2-d4`,

```text
F2 = u^2 + 2 d4 (1-u) = d2^2 - 4 d2 d4 + 3 d4^2 + 2 d4
F4 = 2 u^2 - 3 u + d4 (1-u) = 2 d2^2 - 5 d2 d4 + 3 d4^2 - 3 d2 + 4 d4
```

and `L2 = (2/9) F2`, `L4 = (-4/27) F4`. Units in `Q`, so `(L2,L4)=(F2,F4)`.

**Two-point ideal, scheme-theoretically.** Let `t1=d2-2 d4` and `t2=d4(d4-2)`. Then `F2 = t1^2 - t2` and `(F4-2 F2)/3 = d2(d4-1)-d4^2`. From these:

- `t2 ∈ (F2,F4)` because `F2(d4-1)^2 + t2` lies in the linear generator;
- `t1(d4-1) ∈ (F2,F4)` and `t1^2 ∈ (F2,F4)`;
- `L + 1 = (d4-1)(d2-d4-1)` for `L=d2(d4-1)-d4^2`, hence `t1 = t1·((d4-1)(d2-d4-1) - L) ∈ (F2,F4)`.

The reverse inclusion is the two expansions above. Thus

```text
(L2, L4) = (F2, F4) = (d2 - 2 d4, d4^2 - 2 d4)
```

as ideals over `Q`, not merely as radical supports. The two reduced points are `(d2,d4)=(0,0)` and `(4,2)`. Both engines print `GF24[1]=d2-2*d4`, `GF24[2]=d4^2-2*d4`, and the four mutual-containment flags equal to `1`.

**Branch zero, by hand.** At `(0,0)` the `A3`-restricted `(x1,x3,x5)`-rows are

```text
e1: (0, 0, 4/9)
e3: (0, 4/9, -20/27)
e5: (4/9, -4/9, 40/81)
```

with vanishing `F_w`. These force `dx5=dx3=dx1=0`. The `e7` row is then irrelevant to the value of `L7` once `dx=0` and `F_w(e7)|_{(0,0)}=0`, so `L7=0`. The printed `J0` basis is `(tx5, tx3, tx1, d4, d2)`, matching `T0`. Tangent coordinates are `tx*`, not `tc,td2,td4`: those three columns already vanished, so they do not appear in the reduced `L_i`. No `c`/`tc` swap.

**Branch `(4,2)`, by hand.** The displayed linear forms

```text
dx1 = 8 c + 8/3,   dx3 = 20 c + 88/9,   dx5 = 12 c + 16/3
```

are identical to the printed `J42` basis

```text
9 tx3 - 15 tx5 - 8,
9 tx1 -  6 tx5 + 8,
d4 - 2,  d2 - 4,
36 c - 3 tx5 + 16
```

by solving the last generator for `tx5` and substituting. Direct substitution of these `dx` into the `A3`-restricted `e1,e3,e5` jets cancels both the `c`-coefficients and the constant terms (each identity checked). The `e7` jet is

```text
F_w(e7)|_{(4,2)} = -32/729 c - 240/729
∂x1 = 124/729,  ∂x3 = -108/729,  ∂x5 = 100/729
```

and

```text
L7 = F_w + (∂x) · (dx) = -3888/6561 = -16/27.
```

Then `729 · L7 = 27 · (-16) = -432`. Both engines print `branch42_L7=-16/27`, `branch42_scaled_L7=-432`, `branch42_residual_identity=1`. No ordinary horizontal tangent exists at `(4,2)`.

Note that `(4,2)` lies off the rank-drop line (`4-2=2 ≠ 1`), so it is a rank-three point at which `F_w` is not in the column space of `M`. Fitting `K3=(d2,d4)` therefore excludes it independently of the explicit `L7` residual. The two packages agree; they are not the same calculation.

## 6. Attack 5 — engines, hashes, replay, firewall, V1/V2

Accepted lanes, as frozen:

| package | host | engine/order | input SHA-256 prefix | stdout SHA-256 prefix |
|---|---|---|---|---|
| Fitting Box02 | `ip-172-30-0-186` | `std` / `dp` | `680aae8c…e2ac94` | `2e5bf843…e0d485` |
| Fitting Box03 | `ip-172-30-0-249` | `slimgb` / `block` | `2355ec4a…d21efb` | `90a0b257…7a7e0c` |
| Tangent V3 Box02 | `ip-172-30-0-186` | `std` / `dp` | `b31d05c1…fb2dff` | `68959c2f…3e6e63` |
| Tangent V3 Box03 | `ip-172-30-0-249` | `slimgb` / `block` | `83732e0d…5b320f` | `d58fcf95…541235` |

Every prefix matches the corresponding producer report, `run.meta`, `MANIFEST.sha256`, and `replay.py` lane table. `runner.rc=0`, `rc=0` in `run.meta`, empty `generator.stderr` (`e3b0c442…`, SHA of the empty file). Fitting wall/RSS from `/usr/bin/time -v` on stderr is `0:00.05` / `12700` KiB and `0:00.03` / `13548` KiB, matching the Fitting report. Block orders are `(dp(7),dp(2))` for Fitting and `(dp(7),dp(6))` for tangent, as generated.

Transitive source pins `quotient_compiler.py = 22b0cdc4…` and `order3_fibre.py = a4fdac5d…` appear in both generators, both `run_*.sh` `sha256sum` lists, both `source.sha256` files, and both replay `SOURCE_PINS` tuples. Those are the same pins used by the CONFIRMED 2026-08-24 global-quotient review.

Replay is fail-closed hash-and-marker checking, not a Singular re-run. Both AWS `aws_box02_replay/stdout` files equal the advertised tokens

```text
Q8_W0_OVERLAP_NORMAL_RANK_FITTING_REPLAY_PASS
Q8_W0_OVERLAP_HORIZONTAL_TANGENT_V3_REPLAY_PASS
```

with stdout SHA `c80c5c62…d598c54a` and `009937d2…04b2a65c` matching the reports and the manifests. Banned diagnostic lists cover `redefining`, `not defined`, `error occurred`, `segmentation fault`, `killed`, `timed out` on both stdout and stderr; AWS runners additionally reject `no standard basis` and `// **`. The four accepted stderr files are pure `time -v` records and contain none of those tokens.

**Independence is engine/order/host, not independently authored mathematics.** Both packages share one compiler, one imposed tuple, one generator lineage, and the same two boxes. Fitting and tangent are different Singular scripts (minors/`sat` versus 1-jet ideal containments) and therefore give a real cross-check of the `(0,0)` versus `(4,2)` split, but they are not two independently written proofs.

**V1/V2 negative controls, tangent package.** V1 `generate.py` emits `std(L2,L4)` and the other multi-argument `std`/`slimgb` calls: invalid Singular ideal syntax. V2 wraps those as `ideal IL24=L2,L4; ideal GL24=engine(IL24)` (mathematics of the identities already present) but `run_v2_remote.sh` still demands `F24_vdim=2` in a ring with free `(w,c,x*,t*)`, which is the wrong dimension test. V3 replaces that print by `F24_two_point_scheme=string(f_to_t*t_to_f)` and `run_v3_remote.sh` greps that flag. V1/V2 generators, runners, and manifests are retained; they are not acceptance endpoints. That matches the producer statement. Failed V1/V2 AWS trees are not in the case directory; they are not needed once V3 is the only accepted lane.

Fitting has no V2: a single generator, two engine/order lanes, both accepted.

## 7. Attack 6 — firewall

Licensed, and only licensed:

- on the raw unloaded overlap `w=x1=x3=x5=0` of the pinned six-row approximate-cubic source, ordinary first-order deformations with `delta w=1` exist precisely along `d2=d4=0`, and there they are the boundary-sheet tangent `dx1=dx3=dx5=0`;
- the candidate `(d2,d4)=(4,2)` is a rank-three point with no ordinary horizontal tangent, residual `729 L7 = -432`;
- the normal rank of `M` drops on the doubled line `(d2-d4-1)^2`;
- exact ranks `2,1,0` have no ordinary `delta w=1` tangent.

Explicitly **not** licensed, and not claimed by either producer report once the remaining-gate paragraphs are read as charged work rather than theorems:

- ramified or weighted arcs, including through the rank-drop line and through the rank-one point `(d2,d4)=(2,1)`;
- ordinary tangents with `delta w=0` (special-fibre directions);
- jets with `ord(w)>1` or a first nonzero normal term of order `>1`;
- global horizontal closure `I : (w x5 (x3-2 x5))^infinity`;
- coefficient projective infinity;
- Taylor or terminal realization;
- trajectories, actual-arc landing, or selected-open `D(x5)` opening;
- `(9,12)` in general, maximum twelve, Keller, or JC2.

The Fitting sentence “the ordinary first-order overlap is exhausted” is true for ordinary `delta w=1` and false if read as a statement about all arcs. The remaining-gate paragraph correctly leaves ramified/weighted reconstruction and the global selected saturation charged. The tangent “honest consequence” paragraph is strictly narrower and is the safer language. Neither report smuggles a `(9,12)` or max-twelve conclusion.

## 8. Defects and smallest repairs

No defect requires a change to the frozen mathematics, the accepted endpoints, or the two producer reports.

Non-blocking hardenings, if a later lane is re-run:

1. Fitting `run_remote.sh` currently greps only `a3_source_rows_zero=1`, `a3_tangent_columns_zero=1`, and `PASS`. Smallest repair: grep the same basis/unit markers that `replay.py` already demands (`GK3[1]=d4`, `GK3[2]=d2`, `K{2,1,0}_unit=1`, `GM3[1]=…+1`). The frozen stdout already contains them.
2. Fitting preregistration asked for “original minors reducing into the printed bases”. That check is implied by a Groebner basis of a saturation and would not detect closure artifacts anyway. Smallest repair: replace the sentence by the test actually used, `V(K3) ∩ V(I3(M)) = empty`, which holds scheme-theoretically.
3. Replay banned-token lists omit `no standard basis` and `// **`, which the AWS runners reject. Smallest repair: add those two strings to both `replay.py` `BANNED` tuples.
4. Fitting prose says “the origin” for `V(K3)`. Smallest repair: say “the line `d2=d4=0` (`c` free) in `A3`”. The bases already say this.

None of these is a source, Fitting, residual, or firewall error.

## 9. Verdict

The imposed source is `(e1,e3,e5,e7,e2,e4)` on the raw overlap `w=x1=x3=x5=0` with no hidden load or terminal. The Fitting ideals are the ordinary `delta w=1` incidence closures on exact-rank strata; saturation does not add the rank-drop line to `K3`, and `K2=K1=K0=(1)` empties the lower strata. The rank-drop scheme is exactly `(d2-d4-1)^2`. The tangent package’s `L2,L4`, two-point ideal, branch-zero solution, and `(4,2)` residual `729 L7=-432` all hold by hand, with no tangent-coordinate or row-order mismatch. Custody is two-host engine/order independence of a single mathematical lineage, with V1/V2 retained as software controls. The firewall is intact.

CONFIRMED
