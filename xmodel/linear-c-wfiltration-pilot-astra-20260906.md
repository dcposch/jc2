# W-adapted 190-pivot instrument: method/source validation

Evidence: exact rational construction and symbolic coefficient verification. Lifecycle: **PROVISIONAL**, dependent on the unpromoted transverse-line/source interface; independent Fable review was already pending when this task began. No promotion is asserted.

Post-cutoff coordinator notice: after this instrument was constructed, root reported that GGHV, arXiv:2204.14178v1, Theorem 2.1 excludes actual degree pair (66,99), placed new (99,66) frontier computation on `AUDIT17` hold, and launched a separate applicability review. This report has not independently reviewed that newly reported paper or read the live gate. The result below is retained **only as method/source validation**, not evidence of an open counterexample frontier. No expansion, solve, or stronger descendant is authorized by this packet.

## Result and literal certificate

The actual frozen 192-dimensional C-space admits **190 selected positive-Jacobian rows with a unit lower-triangular coefficient matrix**, universally for every polynomial G satisfying

`G(X,0)=X²+tX+s`, with arbitrary off-line coefficients.

The certificate is `box/linear-c-wfiltration-pilot-20260906/certificate.json`, 477,981 bytes, SHA256 `73913179c76a4c2d75429f4fbb35f233face8a40500342add63928efb77d95bb`. It includes every rational basis vector, its exact source-coordinate expression, all 190 selected row indices, and every nonzero universal entry of the 190-by-192 selected matrix. Omitted matrix entries are exactly zero, checked by an independent differentiation-based reconstruction. `selected_rows.tsv` gives a compact index/normalization census of all 190 identities.

Frozen source: `box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json`, SHA256 `778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea`. Physical coordinates are `X=x`, `W=y-x` (determinant one). An A3 source row `(r,z,e)` contributes `e X^(98-r-z) W^z` to C. All source residual rows are empty; the source map is preserved, not replaced by an unrestricted polynomial C.

The source has 192 independent linear A3 parameters in 201 physical coefficient slots, degree at most 35 and W exponent at most 32. They are disjoint from the h3/C2/C3/B2 parameters. Its W=0 restriction is exactly

`C(X,0)=A3c_97_0 X+A3c_98_0`.

Let `B_X` be the **entire** source column of `A3c_97_0`, not the monomial X: it has seven terms and degree 33. The other free basis vector is exactly 1. All remaining 190 source columns vanish on W=0.

## Exact universal triangular proof

Work over Q, or any commutative Q-algebra of base parameters. Order physical monomials by increasing W exponent and, within a fixed W exponent, decreasing X exponent. Sparse column elimination on the actual source space gives leading pairs `(i_l,r_l)`, with `r_l>=1`. Normalize each selected basis polynomial `B_l` so its leading coefficient is `-1/(2 r_l)`.

In this source the resulting transform has only **192 nonzero rational entries**: no nontrivial combination of source columns was required beyond ordering and scalar normalization. The full transformed basis has 228 physical terms. No source tail has been discarded.

For any `P=W^r p(X)+O(W^(r+1))`, using the convention `J(P,G)=P_X G_W-P_W G_X`,

`[W^(r-1)] J(P,G) = -r(2X+t)p(X)`.

The first product `P_X G_W` has W order at least r. Therefore the selected row for leading monomial `X^i W^r` is `(X_power,W_power)=(i+1,r-1)`. Its diagonal entry after the stated normalization is exactly 1. A later basis column has either higher W order or the same W order and smaller leading X degree, so its entry in this row is identically zero. Thus the active 190-by-190 matrix is lower triangular with determinant 1, not merely generically invertible and not merely invertible at a sampled point.

Every selected row is positive degree (its X exponent is at least one). Their total degrees range from 1 through 35; the active W orders range from 1 through 32. The proof needs no prescribed top homogeneous part of G: **all** off-line G coefficients may vary independently. The selected entries only involve 353 such coordinates, of degrees 1 through 36, together with t and fixed rational constants. Higher G terms cannot reach these low rows because a differentiated nonconstant C monomial has degree at least one.

Literal entry formula, with `B_j=sum c_ij X^i W^j` and target row `(a,b)`, is

`M_(a,b),B = sum_(i,j) c_ij (i*v-j*u) g_(u,v)`, where `u=a+1-i`, `v=b+1-j`.

Discard negative u or v. On v=0 substitute `g_2,0=1`, `g_1,0=t`, `g_0,0=s`, and all `g_u,0=0` for u>2; on v>0 retain the distinct free symbol `g_u_v`. A constant term of G contributes nothing after differentiation. This formula defines every selected coefficient, with no parameter localization.

## Exact quotient/reconstruction contract

Write

`C=sum_(l=0)^189 z_l B_l + beta B_X + gamma`.

Orientation of the recorded transform: each original coefficient `A3c_n` equals the sum of `source_combination[n]*new_coordinate` over all 192 basis vectors. The verifier checks exact physical reconstruction and rank 192 of this rational transform.

For the charged physical source, `G=h²-bh/3+D` and `F=h³+(3D+a)h/2+C`. Thus

`J(F,G)=K+J(C,G)`, with `K=((3D+a+bh)/2)J(h,D)`.

Let k_l be the selected physical coefficient of K. All 190 selected equations are exactly

`z_l + sum_(j<l) M_lj z_j + M_l,190 beta + k_l = 0`.

Consequently `z_l=-k_l-sum_(j<l)M_lj z_j-M_l,190 beta`, evaluated in increasing l, is a polynomial reconstruction DAG over the base ring. If the active matrix is `I+N`, its inverse is the finite polynomial sum `I-N+...+(-N)^189`. There is no generic chart, nonzero parameter assumption, or division by a base polynomial. The only divisions are the fixed nonzero rational scalars `2r_l` in the recorded basis.

This gives a scheme-level quotient isomorphism for the selected equations over **any** specified base Q-algebra. To obtain the full-J quotient, every remaining equation must be carried through this same map. This includes **all other positive physical Jacobian rows, the distinct normalization equation `Zj*J0-1`, and all original source/monic definitions**. Gamma can be retained as a genuinely free additive constant; it does not occur in J. Removing it only removes a free affine factor, not a Jacobian gauge.

All 190 selected row labels occur in the charged complete full-J stream. Its 1,468 nonzero positive row labels leave **1,278** residual positive labels, plus the inverse row and 160 h-lift definitions. The safe full-grid contract retains every positive coefficient slot through degree 99 except the selected 190: **4,859 slots**. Previously identically zero physical rows remain zero under a polynomial substitution. No additional row is discarded based on this count.

An actually compiled eliminated h-lift presentation would nominally have 1,439 rows and 410 coordinates with gamma retained, or 409 after removing that free factor. **No such expanded presentation was constructed.** The K rows, semantic G expressions, all residual rows and the inverse row have not been densely substituted. This certificate therefore is a reconstruction interface, not a newly emitted smaller full ideal or an ideal-nonemptiness certificate. The h-lift is admissible because its only W=0 auxiliary is `Hfact_0_0`, so the monic quadratic restriction of G persists before imposing its defining equations; those equations nevertheless remain part of the full contract.

## Measured discriminator and limits

| Measured object | Prior high-degree 189-pivot instrument | This W-adapted 190-pivot instrument |
|---|---:|---:|
| Basis physical terms | 681 | 228 |
| Rational transform entries | 660 | 192 |
| Selected matrix nonzero entries | 15,391 | 15,258 |
| Literal selected-matrix coefficient terms | 42,131 | 16,623 |
| Recorded abstract reconstruction graph terms | 42,320 | 16,623 |
| Nonconstant free C coordinates | 2 | 1 |
| Used variable G coordinates | 188 | 353 |
| Used G-coordinate degrees | 34–65 | 1–36 |

The new graph-term count is explicit: 190 RHS k nodes plus 16,433 literal off-diagonal/free-beta coefficient terms; it has 15,068 nontrivial product edges. The earlier graph count is quoted literally from its sealed summary (its counting convention retains an extra 189 diagonal terms); the matrix-to-matrix comparison uses the same coefficient-term convention. This is a real reduction in this **abstract selected-matrix** size. The greater number of low-degree G coordinates, nonlinear semantic source expressions, and dense recursive residual substitution remain unmeasured costs. It is **not** a construction-time or solver win against the complete 600-variable, 11,299,180-term full-J presentation. The previous 24-pivot residual-prefix experiment still timed out; nothing here reverses that result.

The single local generation took 0.2365 s to build and 0.2210 s for universal verification; total internal work was 1.1013 s, peak self-RSS 45,972 KiB. The capped process completed normally in 1.2973 s. A later read-only semantic replay of the immutable certificate completed in 1.2042 s, peak self-RSS 52,684 KiB, capped-process wall 1.2874 s. Each command was capped at 60 s and 200 MiB aggregate RSS; no worker was used.

## Verification, genuine mutation controls, and custody

The builder uses target-oriented coefficient extraction. The independent verifier differentiates basis polynomials and iterates source G monomials to reconstruct the entire selected universal matrix. It also checks the source pin, exact rational source transform, rank 192, monomial order, all row indices, all normalizations, universal zeros above the diagonal, and the absent constant column.

An exact 26-term test polynomial `G=H^6+X²+3X+5+W+2XW+3W²+X^5W^7`, where `H=(X+W)^3 W^8`, checks all 36,480 selected matrix positions by ordinary polynomial multiplication. A separate exact point reconstruction checks all 190 graph equations with rational RHS values and beta=7. This is a matrix/control point, **not** a full source or Keller point.

Five deliberately damaged packets were passed to the actual semantic verifier: a sign-flipped source transform coefficient, altered selected X row index, diagonal coefficient changed from 1 to 2, deleted off-line G term, and reversed Jacobian convention. Every mutation was rejected for the relevant semantic discrepancy, not merely a changed file hash. The final read-only replay recomputed the independent universal matrix for the coefficient mutations; no cached-matrix shortcut was used there.

Replay from repository root:

```sh
python3 box/linear-c-wfiltration-pilot-20260906/pilot.py --verify-certificate box/linear-c-wfiltration-pilot-20260906/certificate.json
```

The shipped code is SHA256 `324ef050145efded869ee6d326130b16f0c611159e45b08dfe76b6f715f9bd24`. The first generation predates a wrapper refactor adding the read-only replay mode, overwrite refusal, and fully recomputed mutation replays; its builder mathematics and immutable certificate did not change. The final shipped code is the code used for the recorded read-only replay. Only one certificate generation occurred.

`box/linear-c-wfiltration-pilot-20260906/custody.json` records exact file/dependency sizes and hashes, both terminal PGIDs and caps, no live writers, and the coordinator's post-cutoff hold. `run.telemetry.json` and `replay.telemetry.json` both report normal exit and no live group members. The source and all previously charged worker artifacts were untouched. Worker .56 remains under root's existing custody; this task neither used nor changed it. After this report is transactionally sealed, all task writers are finished and the producer yields. No shared ledgers were edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11790`.
- Body SHA-256:
  `8c94c2ef70e5ca0e24895937a4078e74b2c42a5be52ec52439e0ce843b005b6e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
