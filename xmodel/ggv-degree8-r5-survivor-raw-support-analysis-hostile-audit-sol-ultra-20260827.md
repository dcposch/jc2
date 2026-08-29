# Hostile audit: degree-eight R5 survivors against D3 raw support

Date: 2026-08-27  
Producer: Grok 4.6  
Reviewer: Sol Ultra (different model from the producer)  
Reviewed object: `xmodel/ggv-degree8-r5-survivor-raw-support-analysis-grok-20260827.md`  
Reviewed SHA-256: `43a949b24a3cdec5de41a8b1bf1bf76ed9f3b863d04d99d1b48ddb6040d9c3a5`  
Verdict: **CORRECTION REQUIRED — core support/high-weight lemmas pass, but the staged search and “first incidence at weight 15” do not**

## 0. Executive verdict

The report contains a useful, independently reproducible exact core:

1. the D3 raw windows and the counts `141+301=442`;
2. `F_n=0` for `n>=15`, `G_n=0` for `n>=22`;
3. the coefficient recurrence for `D_n`;
4. the literal constant-coordinate formula
   `D_22[X^0]=F_11[X^1]G_11[X^0]-F_7[X^0]G_15[X^1]`;
5. injectivity and the stated ranks/cokernel dimensions of `L_15,...,L_21`;
6. the generic `Q` and generic `P` rational-mode schedules and their first
   nonpolynomial modes;
7. the endpoint reduction and the two degree-eight survivor types;
8. the leading-edge/polynomial-mode negative control; and
9. the reported weight-11 bilinear ranks `13` (`P`) and `14` (`Q`).

Those statements may be retained with the qualifications below.

The principal campaign-facing conclusion does **not** pass.  Raw
compatibility incidences occur before weight 15.  In fact, on both generic
survivor strata there is already an exact weight-2 divisibility gate.  The
report's `127`-dimensional “product of linearized kernels” is therefore not
the space of prefixes satisfying `D_1=...=D_14=0`, unless an omitted
conditioning/elimination procedure is supplied.  Consequently the finite-
field trials in section 4.5 and the stop rule in section 8 are not licensed
as statements about valid raw jets.

This is a correction of the proposed successor, not a retraction of the raw
window, `D_22`, `L_n`, rational-mode, or endpoint lemmas.  The report still
does not prove or disprove either survivor branch.

## 1. Custody and replay scope

The four custody hashes printed by the producer were recomputed on live
bytes and match:

```text
fd1640420ac389b1b6c3a0ea21243f5d72488bba5d39e4cc2293ab9e7c494681
  xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-sol-20260827.md
3d8ba26743a5c77bf37694ec0118a221a9c5fa1faff6fffb426659010a51c419
  cases/ggv_keller_face_general_multiplicity_endpoint_r5_20260827/FREEZE.sha256
012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256
5187676bdb9b1ea449dde569e426385ad1453b4f15ebc8906886a7cc33c14557
  xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-hostile-review-grok-20260827.md
```

Both charged freeze manifests replay `OK` against every listed file.  The
Grok report itself has no frozen script or result object for its prime-field
sampling claims.  I therefore rederived the identities and used independent
desk-scale exact rational row reduction only as an audit; the empirical
claims in section 4.5 remain nonreproducible from a charged artifact.

## 2. Claims that pass

### 2.1 D3 windows and `D_22`

The inequalities give exactly

```text
F_n: max(0,ceil((n-8)/3))  <= i <= 16-n,
G_n: max(0,ceil((n-12)/3)) <= i <= 24-n.
```

Direct enumeration of the frozen D3 `RAW_INPUT.json` reproduces every
window in the producer table, with `141` `F` slots and `301` `G` slots.
Thus `F_15=F_16=...=0` and `G_22=G_23=...=0` are exact raw-support facts.

For

```text
E=12F_XG-8FG_X-t(F_XG_t-F_tG_X),
```

coefficient extraction gives

```text
D_n=sum_{i+j=n} ((12-j)F_i'G_j+(i-8)F_iG_j').
```

At weight 22 there is no linear `F_22` or `G_22` handle.  Inspecting the
low ends of the windows and the two zero scalar coefficients at `(i,j)=(8,14)`
and `(10,12)` leaves exactly

```text
D_22[X^0]=F_11[X^1]G_11[X^0]-F_7[X^0]G_15[X^1].
```

No omitted raw pair contributes to the constant coordinate.

### 2.2 The high-weight maps

For `n=15,...,21`, the new coefficient is

```text
L_n(G)=2H((12-n)H'G-4HG').
```

If `G` is a nonzero polynomial of degree `d`, the leading coefficients in
`L_n(G)=0` would force

```text
4d=8(12-n),
```

which is impossible for `n>12` and `d>=0` in characteristic zero.  Hence
`L_n` is injective on every raw `G_n` window, independently of the chosen
degree-eight `H`.  Its ranks are the raw window dimensions

```text
9, 7, 6, 5, 3, 2, 1,
```

and subtracting these from the ambient dimensions `40-n` reproduces the
cokernel dimensions

```text
16, 17, 17, 17, 18, 18, 18.
```

The factor `2H` proves `im(L_n) subset (H)`.  More precisely, at a root of
`H` of multiplicity `m`, every image vanishes to order at least `2m-1`.
This is the clean multiplicity-safe version of the producer's simple/double
root discussion.

### 2.3 Modes and endpoint branches

The identity

```text
E(F,t^nF^gamma)=t^nF^gamma F_X(12-8gamma-n)
```

and the rationality criterion `4 | e_i(12-n)` for every factor multiplicity
are correct.  The generic schedules used for the two displayed fixtures are
also correct:

```text
Q (delta=1): n=0,4,8,12,16,20;
P (delta=2): n=0,2,4,...,20,22.
```

Thus the first scheduled mode whose leading coefficient is nonpolynomial is
`H^-1` at `n=16` on `Q`, and `A^-1` at `n=14` on the generic `P` stratum.
These are lost optional kernel directions, not by themselves obstructions.

The endpoint transformation, the criterion

```text
H=A^2B, B squarefree,
A=Bv'+(3/2)B'v,
```

the degree-eight reduction to `deg B=0` or `2`, and the raw-coordinate
`4 x 3` matrix for the quadratic branch all check exactly.

### 2.4 Negative controls and the weight-11 check

With `F=H^2` fixed, `E` is linear in `G`.  Therefore adding any collection
of exact polynomial homogeneous modes to `G=H^3` preserves `E=0`
identically.  This proves the producer's negative control, including
`D_22=0`, more directly than the discussion of “self-pairings”: there are
no `G-G` self-pairings in `E`.

For the two printed fixtures, independent rational row reduction reproduces
the weight-11 facts.  The kernel is the graph

```text
G_11=(3/2)HF_11,  F_11 in span(X,...,X^5),
```

and the 25 cross-bilinear values have rank `13` for
`H=(X^4+1)^2` and rank `14` for
`H=(5X^3-4X^2+X+1)^2(X^2-1)`.  Their total degrees range from 9 through 17,
but their actual supports range from degree 1 through 17; every value is
divisible by `X`.  Thus the constant polynomial is indeed absent.  The
phrase “min degree 9” should mean *minimum total degree*, not minimum
supported exponent.

The constant 2-jet formula in section 4.4 also checks: one exact generic
choice has rank `23`, the `H(0)=0` specialization has rank `22` with the
`D_22[X^0]=1` target still in the image, and the leading-edge-only map has
rank `16` with that target outside the image.  This remains only a necessary
2-jet check.

## 3. Decisive correction: compatibility already appears at weight 2

The statement “no low-weight obstruction through 14” and the claim that
weight 15 is the first genuine raw compatibility incidence are false as
written.

Work on either generic stratum (`Q`, with `delta=1`, or `P`, with
`delta=2`).  There is no weight-1 rational homogeneous mode.  The complete
polynomial solution of `D_1=0` is therefore

```text
G_1=(3/2)HF_1.                                      (3.1)
```

At weight 2, write

```text
R_2=G_2-(3/2)HF_2.
```

The self-pairing of weight 1 is

```text
mixed_2=6H F_1F_1'-(21/2)H'F_1^2,
```

and direct substitution gives

```text
L_2((3/8)F_1^2/H)=-mixed_2.                         (3.2)
```

The homogeneous equation for `L_2` is generated rationally by `H^(5/2)`.
It is not rational on `Q`; on generic `P`, where `H=A^2`, it is the
polynomial mode `A^5`.  Adding that polynomial cannot cancel a pole of the
particular solution.  Consequently a polynomial raw extension through
weight 2 requires, and in these windows is equivalent to,

```text
H divides F_1^2.                                    (3.3)
```

Since `H=A^2B` with `B` squarefree, (3.3) is exactly

```text
AB divides F_1.                                     (3.4)
```

This is already a nontrivial compatibility incidence on the previous
weight.  In the factorized form (3.4) it becomes a linear divisibility
condition for fixed `A,B`, but it is not removed by the presence of the raw
`F_2` handle.

An explicit counterfixture to the producer's extension claim is

```text
F_1=1,  G_1=(3/2)H.
```

Both coefficients lie in the D3 weight-1 windows and satisfy `D_1=0`.
For each of the producer's fixtures, however, no raw `(F_2,G_2)` solves
`D_2=0`:

```text
P: H=(X^4+1)^2
   rank(weight-2 new-slot map)=22,
   rank(augmented by -mixed_2)=23;

Q: H=(5X^3-4X^2+X+1)^2(X^2-1)
   rank(weight-2 new-slot map)=23,
   rank(augmented by -mixed_2)=24.
```

Equations (3.2)-(3.4), rather than these fixture ranks, are the general
certificate.

It remains true that weight 15 is the first weight with no `F_n` slot and
that `L_15` is the first map in the producer's seven-map high-weight block.
It is not the first compatibility gate of the raw recurrence.

## 4. Consequences for sections 4.5 and 8

The number `127` is the sum of the dimensions of the *homogeneous
linearized* kernels at weights 1 through 14 on the displayed `Q` fixture.
It is not the dimension of a Cartesian product of independently choosable
coefficients in an exact solution prefix.  Already (3.4) constrains the
weight-1 choice before weight 2 can be solved, and later weights introduce
further conditions.

Therefore:

1. Randomly sampling the product of those linearized kernels does not sample
   valid prefixes satisfying `D_1=...=D_14=0`.
2. “Fix weights 1 through 7 arbitrarily” is not legitimate unless those
   weights have first survived every intervening compatibility equation.
3. The reported `200/200` and `30/30` finite-field observations have no
   charged script and do not specify such conditioning.  They are not
   promotable evidence about the jet variety.
4. The proposed stop rule must include inconsistency at *every* weight,
   beginning at weight 2, with backtracking/elimination over earlier free
   parameters.  Failure of one chosen prefix kills only that prefix.
5. A cokernel form nonzero at one assignment does not exclude a whole
   branch.  Branch exclusion needs a symbolic universal/elimination
   certificate (or an exhaustive stratification), not a pointwise witness.
6. Although every new-weight equation is linear in the new slots, the
   existential problem in the accumulated earlier parameters is nonlinear.
   It is therefore incorrect to describe the complete decision object as
   “each step is one Gaussian elimination” while also retaining the
   quadratic weight-16 gate.

The all-zero positive-weight fixture is a valid regression/negative control,
but a single point with `D_22=0` is not negative evidence for existence of a
different point with `D_22=1`.

## 5. Other local corrections

These do not affect the passing core but should be fixed before reuse.

1. **Stratify `P`.**  `H=A^2` does not imply `delta=2`.  In degree eight,
   the perfect-square branch has `delta=2,4`, or `8`.  If `4|delta`, modes
   occur at every weight and the first nonpolynomial scheduled mode is
   already `n=13`, not `n=14`.  The `n=14` statement is for the generic
   `delta=2` stratum only.

2. **A shared root does not imply `B|A`.**  At a simple root of `B`,
   `N_B(v)` vanishes exactly when `v` vanishes there.  Thus
   `gcd(A,B)|v`; it does not follow that all of `B` divides `v` or `A`
   unless all roots/factors of `B` are shared.  For example, with
   `B=X(X-1)` and `v=X`,

   ```text
   N_B(v)=4X^2-(5/2)X,
   ```

   which shares only the root `0` with `B`.

3. **Scaling preserves the raw degree windows.**  Translation mixes lower
   `X`-degrees and generally violates the D3 lower bounds.  A nonzero
   scaling of `X` does not mix degrees or move exponent support.  The
   conclusion that a general completion-of-the-square normalization is not
   a raw-chart operation remains correct because translation is generally
   required.

4. **The `P` weight-22 scalar cannot repair a polynomial part.**  The
   homogeneous term `cA^-5` is proper at infinity and changes the
   `X^-20` coefficient.  It cannot alter, much less determine, the
   polynomial part of the lower-mode coefficient.  That polynomial part
   must vanish independently.  The scalar may then be fixed by matching
   finite principal parts or the full rational identity.

5. **Modes do not self-pair.**  For fixed `F`, `E` is linear in `G`.
   Statements about `2+20`, `6+16`, and `10+12` should be phrased through
   the tails of the exact modes and their pairing with positive `F_i`, not
   as mode-mode or `G-G` quadratic interactions.

## 6. Cleanest executable successor

Replace the proposed weight-15-first sampler by an exact, rollback-tagged
**prefix compiler beginning at weight 1**.

For the generic `Q` (`delta=1`) and generic `P` (`delta=2`) strata, its first
two certified rows should be hard-coded as identities, not rediscovered by
random linear algebra:

```text
G_1=(3/2)HF_1,
F_1=AB U_1,
G_2=(3/2)HF_2+(3/8)B U_1^2
     + c_2 A^5       on P,
G_2=(3/2)HF_2+(3/8)B U_1^2
                    on Q.
```

Here the `c_2` term is present only on the generic `P` stratum.  The
`4|delta` specialisation of `P` must be a separate lane because it already
has a weight-1 homogeneous mode.

Then, for every `n=3,...,22`, the compiler should:

1. construct the exact mixed term from a prefix already certified through
   `n-1`;
2. row-reduce the new-slot map on the literal D3 windows;
3. emit both the particular solution and every cokernel equation on the
   accumulated parameters;
4. retain those equations symbolically rather than sampling an unconstrained
   product of kernels;
5. stop only on an exact inconsistency certificate, or replay a complete
   `D_0=...=D_21=0, D_22=1` rational point; and
6. run modular search on AWS, followed by exact characteristic-zero replay.

The smallest useful first artifact is through weight 3 with the weight-2
divisibility mutation above.  After that passes, extend the same compiler to
weight 16 and compare the *conditioned* residual system with the claimed
`17`-equation quadratic gate.  This is both smaller and safer than launching
the producer's unconditioned `127`-parameter atlas.

## 7. Promotion boundary

Promotable from the Grok report, subject to the local qualifications in
section 5:

```text
D3 support windows and counts;
D_22 mixed/constant formulas;
L_15,...,L_21 injectivity, ranks, and cokernel dimensions;
generic P/Q mode-fit tables;
endpoint branch formulas and infinity estimates;
the leading-edge/polynomial-mode negative control;
the exact weight-11 two-weight negative.
```

Not promotable:

```text
“no low-weight obstruction through 14”;
“first genuine incidence at 15” except in the literal no-F-slot sense;
the unconditioned 127-dimensional kernel-product sampling;
the 200/200 and 30/30 claims as jet evidence;
the advertised Gaussian-elimination-only stop rule;
any whole-P or whole-Q exclusion inferred from a pointwise failure.
```

Maximum surviving claim: the report supplies exact raw-support and
high-weight linear ingredients for a corrected prefix compiler.  It does
not yet supply that compiler, a valid branch-wide decision procedure, a
positive raw fixture, a branch exclusion, GGV landing, or progress to JC2
beyond this necessary-filter layer.
