# Significant-news full-spectrum packet — `20260828T0702Z`

Freeze time: 2026-08-28 07:02Z  
Coordinator: Sol Ultra  
Status: **SEALED SAME-INPUT BLIND ROUND**

## 0. Custody gate

Verify every hash below before reading the corresponding file.  Fail closed
and report only the mismatch if any value differs.  The canonical files will
not be mutated until every blind submission has sealed.

```text
603ab8b7412f4d125b0cb1d7dbdda1b166d86023cc6dbb572d4d67bd65bb6599  APPROACHES.md
f58d39825152615fcb8a92e10ab28f81d594817d19cc12eab4855063b5a5f913  AUDIT.md
fe352eaf1575acf37ac18c68ba8e2ad611872256fe95a5ad3176cc0a2b001dcc  COORDINATION.md
486f165748307d27c44896a7be42faf518d45c96cb905cc0093bc543c377cec5  PROGRESS.md
2e71e3f376069ded18bdb350210b6ca7c3e219c38afb6b968ada2be85de490ad  notes.md
4b1789ee6c0807cb5c1165d91c76ef76781ddaec7dc8f846fd7151ef9564ec30  xmodel/ideation-20260827T2259Z-synthesis-sol.md
ecf83ac7b380a18f939e60671a4e97290f9f68b51536c236b81f71bb6a6c5bb8  xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-sol-ultra-20260828.md
a294cdf70f0496b360855b1b88e6f362e752e0bda33498902eb6fba7785e23a5  xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-hostile-review-grok46-20260828.md
2b134d94e387f8a7fa9715d9efbe3b6b7925a39f1801a842b30ed00e09eefe2e  xmodel/ggv-upper-endpoint-uniform-d18-d22-endpoint-collapse-sol-ultra-20260828.md
cd24f249f7ef93ff44c4fbca41e54951fdc94ecfddfd0f4a12cabf49b5923303  xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-independent-sol-ultra-20260828.md
e2d02b32f5274323c47ca7a981f2dfb51e7035538a8b6b8136dd4e6bed316054  xmodel/ggv-upper-endpoint-uniform-d7-d22-A-dependency-audit-sol-ultra-20260828.md
5b3bd56a1921bb0a4ed7ae9ed7c1eabcf5215533a0aae2a769cdcc81927b5401  xmodel/ggv-upper-endpoint-q1-prefix-d7-d9-divisor-target-sol-ultra-20260828.md
2d2b31e604fdea2d2ef5166085f4db3dc62e318e26dbc2727bb21601aeaff838  xmodel/ggv-upper-endpoint-q1-active-translation-gauge-obstruction-sol-ultra-20260828.md
82a67d207b404676a1ab35d02428a50cf436f3a644f1dcafdefe17ecfb76bbc8  xmodel/vandobben2608-projective-bundle-jc2-boundary-infinity-review-codex-20260828.md
e03a5bec4278362e8941312115b7bb7bdd9a7b6dd3eee6b58d836e5dbeb55701  xmodel/websweep-20260828T0524Z.md
ad2b2f112a5c61b101758cd45f38339a69a7e3ce6343dfa81e87f784298298c6  refs/vandobben2026_projective_bundle_complements_affine_space_arxiv2608.27341v1.pdf
c94bd3131238d85b80bfe4cbeda31c5d186619f09417abf6bee2ab1840fa3258  xmodel/ggv-hens-ct-rank-one-control-r0-sol-ultra-20260828.md
424a556baa36c13889a1aab725a7a8af385aa3cb465849a70b9f75fe806b276f  cases/ggv_8_28_upper_endpoint_tail3_aws_custody_20260828/SUPERSEDED_STOP_REPORT_R6D_R2.md
```

The repository basis is HEAD
`418e413593120d19e15e6546eb50c985f4b1f038` plus the explicitly hashed dirty
artifacts.  Do not infer a clean worktree.  Never enter, list, search, read,
build, status, or modify the nested user-owned `jc2-lean` tree.

For the two newest producers, the frozen machine-readable custody is:

```text
ba900c6eacc7302491105bec49516d2e95dff982959a3904370b7e540216260b  cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/RESULT.json
c41f04a93f509adb1f430e808c69cd2171439c9e19fb001c6ea2bf0f29633a46  cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/TARGET.json
1088e21e31bf3c8c6b6eeeb69571113eca39fb159e32800747ecfa31ca4e625c  cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/SOURCE.sha256
2858056b677c55526cd069ebbfaaeca2f53bea48d16ef8198bc60c77733c8583  cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/EVIDENCE.sha256
47f77fe40ccb33f8820a41cb9552b59e6a657c1435f537c8a42bff18fc47b7c5  cases/ggv_8_28_upper_endpoint_q1_translation_gauge_audit_20260828/RESULT.json
bf414ca09ae911351dbc42fd485a197283b24718781cc33354d32680fbe26097  cases/ggv_8_28_upper_endpoint_q1_translation_gauge_audit_20260828/SOURCE.sha256
70e852a4ccfdba2ae158c36a2416b53e7027b9c3cf382318fd04504386231c26  cases/ggv_8_28_upper_endpoint_q1_translation_gauge_audit_20260828/EVIDENCE.sha256
```

## 1. Blindness and execution boundary

Read no peer `20260828T0702Z` response before sealing yours.  Do not read any
file whose name begins `xmodel/ideation-20260828T0702Z-` except this packet,
your assigned prompt, and your own assigned output.  Disclose any accidental
contamination and fail closed if it can affect independence.

Do not touch AWS or running jobs.  Do not run Singular, msolve, Sage, Lean, or
heavy/uncertain local algebra.  Short read-only inspection, hashes, and small
standard-library exact checks are allowed.  Do not edit canonical files or
any case.  Your only write is the assigned
`xmodel/ideation-20260828T0702Z-<lane>.md`.  Print its SHA-256 and state the
exact model, files read, checks run, failed attempts, assumptions,
contamination, and scope.

## 2. Authoritative significant news

### 2.1 Reviewed fixed endpoint theorem

The complete fixed upper branch-P fixture
`A=X^4-1, F1=A^2` (`V0=1`), with the full nine characteristic modes and
literal raw coefficient windows, is now different-model-confirmed
characteristic-zero **field-valued empty**.  D18 and D20 kill `c18,c20` at
birth; D18--D21 impose four exact `A^2` relations; complete `g22` has minimum
`A` exponent `-2`; absent raw `G22` gives `D22_raw in (A)`, contradicting the
full target polynomial `1`.  Grok46 passed 289 hostile checks; two independent
Sol packets replay all 513 rows.  This is not a scheme unit, a general-`V0`
theorem, another branch, Keller, or JC2.  Every fixed-slice tail/solver lane is
retired.

The dependency audit says the formal D7--D22 field-point cascade only uses a
nonconstant squarefree quartic `A`, conditional on the same D4--D6 normal
form, mode schedule, and raw windows.  A discriminant-localized parameterized
raw compiler and window/kernel transport remain missing, so do not silently
generalize the theorem.

### 2.2 Genuine q1-compatible D7/D8 escape and provisional D9 repair

For

```text
F0=A^4,
F1=A^2 V0,
F2=(V0^2+A^2 Z)/4,
F3=(V0 Z+A T)/8,
V0=A'R0+2AR0',  deg R0<=4,
```

and on the c2-zero divisor cover

```text
C=gcd(A,V0)=gcd(A,R0),  A=CB,  V0=CV1,  T=BU,
K=64F4-Z^2,
```

the exact producer obtains

```text
D7: C | U(K-2UV1),
D8: A^2 | (K-4UV1)^2-8B^2U^2Z
              +1024A(c6 C^2V1^2+F5BU).
```

A literal q1-compatible raw fixture with `A=X^4-1`, `R0=X-1`, and `T=B`
respects every window and has `D0=...=D8=0` while `A` does not divide `T`.
Thus the fixed-`V0=1` D7 inference genuinely does not transport.

The same producer then gives the **provisional** repair

```text
on the full q1-compatible c2 branch cover,
D1=...=D9=0  ==>  A|T                 (field points, char 0).
```

For proper `C`, the D9 factorization leaves `-8B^4U^3` at a `C` root if
`U!=0`; for active `C=A`, the complete `A^-3` class leaves `-8T^3` after D7
and D8.  This requires hostile review.  q1 is strategically licensed only
when the later D23 theorem is included; D1--D22 do not imply it.

After `T=A U0`, set

```text
Delta4=F4-V0 U0/16-Z^2/64=A W.
```

The remaining c2-zero D9 condition is

```text
A^2 | W[-16V0W+A(64F5-U0Z)].
```

For `V0=CV1`, this forces `B|W` but not yet `C|W`.  The smallest next target
is the missing `C` part of `W`, together with the separate active-c2 lower
poles—not an undifferentiated D22 elimination or a 16/81-chart brute force.

### 2.3 Tempting translation gauge is not licensed

On the deepest active component, q1 gives `R0=lambda*A` and
`V0=3lambda*A*A'`.  The affine source shear `X -> X-(3lambda/4)t` exactly
intertwines the determinant operator, fixes `t^22`, and kills the formal
`F1,G1` pair.  However, exact negative audit proves it does **not** preserve
the frozen lower-X raw windows: allowed `F8=X` creates a forbidden constant
slot in F9, and allowed `G12=X` does the same in G13.  Therefore `C=A` cannot
be gauged to `V0=0` on the full raw space.  It remains open whether the
determinant equations force every forbidden shear tail to vanish on the
solution locus; absent such a theorem, analyze active `C=A` directly.

### 2.4 HENS-CT and external evidence

The HENS rank-one control packet is only a control design.  As of the freeze,
a fresh AWS-only adapter has for the first time serialized a real nonzero
`L,C`, matched the upstream doctest operator, reduced the Ore remainder to
zero, and independently reduced the direct algebraic-field remainder to zero.
The mandatory rank-one campaign control is running.  This is software
`UPSTREAM_PASS`, not yet an evidence-capable control certificate and not a
mathematical result.

The 05:24Z web sweep found no external JC2 proof or counterexample.  The new
van Dobben de Bruyn paper arXiv:2608.27341v1 is preserved and audited.  Its
naive `n=2` symmetric-power descent does not obstruct a JC2 boundary curve:
the nontangent complement has Picard group `Z`, while the tangent complement
is `A1 x Gm`.  Retain only a secondary possible bridge to the campaign's
one-vertex/boundary-at-infinity geometry; do not promote it as an obstruction.

### 2.5 Resources at the cutoff

All seven authorized AWS instances are running and have zero swap.  `box01`
has the long exact D43 builder (one saturated core, about 184.6 GB RSS);
`r6b` has LF40 exact Singular (one saturated core, about 9.3 GB RSS); `r6c`
has the small HENS-CT control.  Box02, Box03, r6a, and r6d are idle and
available after exact target selection.  The six-chart fixed-tail run was
safely stopped before any algebraic marker and is operational non-evidence.
Use AWS aggressively only after compression and target-fidelity checks;
never run heavy campaign computation locally and never revive superseded
brute force.

## 3. Whole-campaign task

Think independently about the **entire** plane Jacobian conjecture campaign,
not just the new GGV endpoint.  Read all of `APPROACHES.md`, the current/top
corrections of `AUDIT.md`, the current day in `PROGRESS.md`, the newest live
state and later events in `notes.md`, the prior synthesis, and the exact new
reports.  Reconsider every proof and counterexample route, every live gap,
and every connection suggested by the new evidence.  Victory may come from a
new avenue or a connection no prior round considered.  Agreement with the
packet is not a goal; try to falsify its framing.

Answer these critical questions inside the whole-portfolio scan:

1. Is the provisional D9 repair actually correct on every divisor endpoint,
   including active c2 and all mode valuations?  Use it only with an explicit
   provisional label.
2. What is the fastest exact way to resolve the post-D9 `W` split and then
   decide whether the fixed endpoint mechanism transports?  Look for a
   root-algebra, valuation, differential-operator, norm/resultant, or
   equivariant compression before chart fanout.
3. Can the failed translation shear be repaired on the solution locus, by a
   compensating target/source automorphism, or by enlarging and then
   descending the raw window space?  State precisely why or why not.
4. Perform a theorem-interface composition pass: can the reviewed fixed
   endpoint theorem, q1/D23 gate, D24/target law, raw-to-global landing maps,
   boundary one-vertex results, or any non-GGV avenue discharge one another's
   hypotheses?  Report a real bridge, exact scope mismatch, or `NO HIT`.
5. How should the four idle AWS nodes be used for maximum expected information
   gain without brute-force explosion?  Include exact stop conditions.
6. Which non-GGV proof or counterexample avenue is now under-resourced or
   incorrectly ranked?  Do not let recent success create tunnel vision.

## 4. Required submission contract

Your report must contain all of the following:

1. A compact disposition vector for **every numbered avenue 1 through 46**:
   `unchanged`, `raise`, `lower`, or `reopen`, with a reason for every change.
   Group unchanged entries compactly, but do not omit any number or silently
   merge the two meanings of G2.
2. A reranking of the three principal proof bottlenecks and two principal
   disproof/counterexample bottlenecks.
3. At least one genuinely new avenue or mechanism, explicitly compared with
   repository history, and at least one new connection between existing
   avenues.
4. The strongest proof attack and strongest counterexample/falsification
   attack you would run next.
5. One software acceleration or decisive experiment.
6. No more than three detailed idea cards.  Each card must name exact
   dependencies and licensed assumptions, the cheapest decisive
   discriminator, all materially different outcomes and their meaning, a
   stop/rollback condition, estimated compute/review cost, and expected
   information gain.
7. A `continue`, `redesign`, or `stop` recommendation for every current major
   lane, including general-q1 GGV, raw-to-global landing, HENS-CT, D43, LF40,
   order-two/TD6, Artin--Schreier, and external intelligence.
8. One likely-missed insight: the claim or connection most likely to have
   escaped earlier rounds, plus the cheapest way to test it.
9. A full epistemic ledger: distinguish proved/promoted facts, provisional
   inputs, conjectures, failed approaches, hidden assumptions, checks run,
   failed checks/attempts, contamination, and exact scope.  No model verdict
   is mathematical evidence.

Do not output a generic brainstorm.  Rank by expected information gain per
wall-clock hour and by probability of resolving JC2, not by ease.  Preserve
independent disagreement.  A result with reasonable producer confidence may
seed reversible descendants while hostile review runs in the background;
review still gates promotion, publication, irreversible action, and expensive
fanout.
