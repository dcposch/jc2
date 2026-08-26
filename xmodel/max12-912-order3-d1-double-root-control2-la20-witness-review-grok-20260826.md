# Hostile text-only review — control-2 `la^20` LPDP witness V2

| Field | Value |
|---|---|
| Claim under review | Exact dehomogenized preimage of `la^20` in the frozen nine-generator control-2 Rees ideal, hence the fixed-weight obstruction and the seven strict witness halfspaces, at `a=1,h=q2=k=nu=0,mu=2/3` |
| Overall verdict | **LA20_WITNESS_CONFIRMED**. The V2 compiler reconstructs quarantined V1 source SHA `2d22f986…` and changes only the AWS tag and four reserved `GCD` tokens to `CDSTD`. The r6d LPDP run returns a literal zero-polynomial identity `s^96*la^20-s^97*TAIL=sum FINAL[i]*I[i]`. Substituting `s=1` into `la^20-s*TAIL` is the eight-term `W` in `WITNESS_RESULT.md`. `la^20` is its unique least-weight term at the charged vector, so `la^20∈in_w(J)` on the open witness-obstruction region |
| Smallest failing identity | none in the frozen V2 source, the reconstructed V1 source, or the harvested AWS stream |
| Smallest missing hypothesis for a stronger theorem | moving axis/load, nonzero `q2`, another support, equality-face torus saturations, a full Gröbner cone or Newton fan, a parametric neighbourhood, D1, or JC2 (all firewalled). Independently ordered global-`dp` enumeration and the V3 minimum-exponent race are pending corroboration, not hypotheses of this identity |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; inverse tag/`CDSTD` reconstruction of V1 source; `cmp` of the nine B polynomial bodies; hand arithmetic on `TAIL`, `W`, weights, and halfspaces. No local Python, Singular, Sage, msolve, Lean, Gfan, or other substantive symbolic computation |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V2 compiler, V1 compiler, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute Python (the V1 or V2 compilers included), Singular, Sage, msolve, Lean, Gfan, or any other solver. Hashes were checked with `shasum -a 256 -c` and `shasum -a 256`. File identity of the nine charged polynomial bodies was checked with `cmp`. Inverse reconstruction of the quarantined V1 source was a `LC_ALL=C sed` tag/`CDSTD` inversion piped to `shasum -a 256`. Marker counts used `grep -c`. Git identity was read with `git rev-parse`. Two accidental `python3 -c` print no-ops produced no computational output and were not used for reconstruction or arithmetic. AWS streams were read as already-emitted text. Hand arithmetic is recorded under charges 3 and 4.

Charged freeze SHA-256, recomputed and matched:

```text
04cd09886ed78e1af48a6387ee2c67996856d2b6f59791963450e7e4380e32a3  WITNESS_FREEZE.sha256
```

Every path listed in that freeze recomputed and matched:

```text
c4a2207bd5a67f819963eee1b579413372a1953c21bb24e31b72547d9be51bcd  WITNESS_RESULT.md
0e6538bd40c72f014558a107742ef7f91e19229f2bf0750c232a7f7833a13f20  CONE_PREMISES_PROVISIONAL.md
061ed471b68b32ec53a07943fa5eb93f4224789176e5998aba9379acc39ab47b  SOURCE_CLOSURE.sha256
fcd9e8d642c4aa4e3463674163ac1532d092faa85555a98843eeb957841e74e1  compile_la20_syzygy_v2.py
ed3527acbbcdf854f34cb665ccbd0f21951f3eaaf390b5da83d65d6a71cbfcdb  remote_worker.sh
cd3e5268f11daba274b8cd08c44ba9479b5cc277b638fb78ef7b5ed6e25c8a69  aws_r6d_LPDP/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_LPDP/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_LPDP/compiler.rc
e9b2c1594460cc8a6053654f0fcd810522044c6b1ef89d6e92ec2fb0038fd894  aws_r6d_LPDP/la20_syzygy_v2_lpdp.sing
a0611ede0e667d45f569a954fdaa73818f0ebea328212b8c46d4ccb0aa29fe08  aws_r6d_LPDP/singular.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_LPDP/singular.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_LPDP/singular.stdout.diagnostics
3b88afd5f1bc991c2f6e73e693e12cdf2af0f9f85d7081411cb114fe65aea6ec  aws_r6d_LPDP/singular.time
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_LPDP/singular.rc
1921691a435fd69879b5c4e0a6e856210d7fe331b243e765b90f1317a21d5841  aws_r6d_LPDP/result.sha256
4b630333c12c49d598ee95abe1a77915c1e08b1cf9d3c3a41958298cd0da013a  aws_r6d_LPDP/worker.metadata
```

Nested `SOURCE_CLOSURE.sha256` and harvested `result.sha256` entries all matched from the case root / harvest directory as appropriate. Empty compiler/CAS stderr and the hardened stdout-diagnostic file are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`. Harvested copies of the compiler, worker, preregistration, AWS registration, and source-closure files are byte-identical to the case-root copies.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826/`
except five 163-byte macOS AppleDouble sidecars `aws_r6d_LPDP/._*` (binary resource-fork copies, not in the freeze, not payload); every harvested payload under `aws_r6d_LPDP/`; V1 `compile_la20_syzygy.py`, `base_B.sing`, `V1_SOFTWARE_CONTROL.md`, `PRESOLVE_CUSTODY.md`, `PREREGISTRATION.md`, `AWS_REGISTRATION.md`, and `SOURCE_CLOSURE.sha256`; V1 and V2 global-`dp` `V1_SOFTWARE_CONTROL.md` / preregistration as charged; corrected-A `RESULT.md` and `PROMOTION.md`; and
`xmodel/max12-912-order3-d1-double-root-control2-la20-witness-cone-formulation-20260826.md`.
The still-running `la20_dp_cone_v2` package and `la20_syzygy_minexp_v3` package were inspected only far enough to confirm they have no harvested endpoint and are not evidence for this review.

---

## Promotion

**Accept `FOR THE PINNED NINE-GENERATOR CONTROL-2 REES SYSTEM AT a=1, h=q2=k=nu=0, mu=2/3, THE REGISTERED r6d LPDP V2 RUN PROVES THE LITERAL IDENTITY s^96*la^20 - s^97*TAIL = sum_{i=1}^9 FINAL[i]*I[i] IN Q[s,la,tau,rho,q1,q0,r2,r1,r0]. AFTER s=1 THIS IS MEMBERSHIP OF THE EIGHT-TERM POLYNOMIAL W IN THE DEHOMOGENIZED IDEAL GENERATED BY ALL NINE CHARGED EQUATIONS. AT w=(4,1,1,22,22,30,30,30) THE UNIQUE LEAST-WEIGHT TERM OF W IS la^20, SO la^20 LIES IN in_w(J) AND THE EIGHT-COORDINATE TORUS LOCALIZATION OF THAT INITIAL IDEAL IS EMPTY. THE SAME SUPPORT YIELDS THE SEVEN STRICT WITNESS HALFSPACES IN CONE_PREMISES_PROVISIONAL.md. THIS IS A FINITE WITNESS-OBSTRUCTION REGION, NOT A GRÖBNER CONE AND NOT A NEWTON FAN.`**

Do not promote this to: a moving-axis or moving-load theorem; a nonzero-`q2` theorem; another support; an equality-face or all-face theorem; a complete Gröbner cone or Newton fan; a parametric neighbourhood of the rational source; a whole-double-root, D1, or JC2 theorem; a citation of any V1 saturation exponent; or a claim that `96` is minimal.

---

## Charge 1 — Source custody and repair

**CONFIRMED. The frozen V2 compiler pins and reconstructs exact quarantined V1 source SHA `2d22f9867aceb250d8df6002fc4a541fffd225dfb6f8b18d3bbce2aab0f75737`, then changes only its one tag and the four reserved-identifier tokens `GCD` to `CDSTD`. Emitted V2 source SHA is `e9b2c1594460cc8a6053654f0fcd810522044c6b1ef89d6e92ec2fb0038fd894`. V1 has no mathematical verdict. No V1 printed saturation exponent is cited as evidence.**

V2 `compile_la20_syzygy_v2.py` hard-pins

```text
V1_COMPILER_SHA = 18af62ed9b9529387a6b13abf685d7001a873935023dc0ef0b33b63c6bd3171c
V1_TAG           = max12_912_order3_d1_double_root_control2_la20_syzygy_20260826T015817Z_r6d_LPDP
V1_SOURCE_SHA    = 2d22f9867aceb250d8df6002fc4a541fffd225dfb6f8b18d3bbce2aab0f75737
```

The on-disk V1 compiler hashes to that digest. The V1 compiler's `emit` body contains exactly four `GCD` tokens, at the declaration `ideal GCD=std(CD);` and the three subsequent uses in the two-way `reduce` loops. The V2 compiler loads that file, calls `extract_polynomials` / `emit(V1_TAG, …)` only (it never calls V1 `main` or V1 `require_aws`), refuses unless the reconstructed text hashes to `V1_SOURCE_SHA`, occurs with the V1 tag exactly once, contains `GCD` exactly four times and `CDSTD` zero times, then does

```text
source = reference.replace(V1_TAG, tag).replace("GCD", "CDSTD")
```

and refuses unless `GCD` is absent and `CDSTD` occurs exactly four times.

The harvested `la20_syzygy_v2_lpdp.sing` (103 lines, 4230 bytes) contains `CDSTD` four times, `GCD` zero times, the registered V2 tag once, and the V1 tag zero times. Inverse reconstruction — replace the V2 tag by the V1 tag, then every `CDSTD` by `GCD` — hashes to exactly `2d22f986…`. Byte accounting is exact: V1 PRESOLVE records 103 lines / 4219 bytes; the V2 tag is three characters longer (`_v2`) and four `GCD`→`CDSTD` replacements add eight bytes; `4219+11=4230`. Collateral substitution is therefore impossible: if a polynomial body had contained `GCD`, the inverse hash would not have recovered the quarantined source.

The nine `poly E1,…,E8,LT` lines in the V2 source are byte-identical to the same nine lines of frozen B

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

which is the same B digest charged by corrected A. The V1 compiler extracts them by the unique-anchor regex `^poly NAME=(.*);$`.

AWS compiler stdout reprints the three pinned hashes and the exact source-diff marker once, then `PASS_CONTROL2_LA20_SYZYGY_V2_COMPILER` once. Compiler rc 0, empty stderr.

V1 `V1_SOFTWARE_CONTROL.md` is `QUARANTINED_NO_VERDICT`. It records that Singular 4.3.2 treated `GCD` as a reserved/outdated identifier, printed parser diagnostics to stdout, continued, and was stopped with rc 1. Quote: “No printed intermediate, including the apparent saturation exponent, is a mathematical endpoint.” The V1 wrapper (unlike V2) did not classify stdout parser diagnostics independently of stderr. This review cites V1 only as a source/deployment negative control. The exponent `96` in `WITNESS_RESULT.md` is the V2 stdout line `S_SATURATION_EXPONENT=96`, not a V1 figure. The global-`dp` V1 control is likewise `QUARANTINED_NO_VERDICT` and is not a witness, cone, or exponent source.

---

## Charge 2 — Saturation and lift semantics

**CONFIRMED. The printed identity is a literal polynomial membership certificate in `I=(E1,…,E8,LT)`. The exponent `N=96` is a working colon exponent used only to lift; it is not claimed minimal, and minimality is irrelevant after `s=1`.**

Toy orientation, in the emitted source:

```text
ideal TOYI=s^2*(q1+1);
list TOYS=sat_with_exp(TOYI,CS);
… TOYN!=2 → FAIL_TOY_SAT_EXPONENT
ideal TOYSC=s^TOYN*TOYC;
matrix TOYL=lift(TOYI,TOYSC);
matrix TOYR=matrix(TOYSC)-matrix(TOYI)*TOYL;
TOYR!=0 → FAIL_TOY_LIFT_ORIENTATION
```

This pins two library contracts on a principal example whose saturation exponent is visibly 2: `sat_with_exp` returns that exponent in slot `[2]`, and `lift(A,B)` is oriented as `B=A*lift(A,B)`. The AWS stream prints `PASS_TOY_SATURATION_AND_LIFT` once.

Main construction: `I=(E1,…,E8,LT)`, `CS=<s>`, `list SW=sat_with_exp(I,CS)`, `C=SW[1]`, `N=SW[2]`. Direct `CD=sat(I,CS)` and `CDSTD=std(CD)` are then compared both ways by `reduce`:

- `reduce(C[i], CDSTD)==0` for all `i` tests `C ⊆ sat` against a Gröbner basis (sound).
- `reduce(CDSTD[i], C)==0` for all `i` tests membership of the Gröbner generators of `sat` in the ideal `(C)`. Reduce-to-zero is a membership certificate even if `C` is not a Gröbner basis; a false nonzero would abort (`FAIL_SAT_REVERSE`), so the test is fail-closed. PASS therefore gives equality of ideals `C=sat(I,<s>)`.

What `N` licenses: the `sat_with_exp` contract is `I:<s>^N = I:<s>^∞`, equivalently `s^N*C ⊆ I`. The script does **not** trust that contract alone for the certificate. It builds `H=(C,s)`, `TARGET=la^20`, checks `RH=matrix(TARGET)-matrix(H)*LH==0` (`PASS_H_LIFT`), then takes only those `C[i]` with `LH[i,1]!=0` as `USED` / `HCOEFF`, forms `SUN=s^N*USED`, and checks `RU=matrix(SUN)-matrix(I)*LU==0` (`PASS_USED_C_LIFT`). The stream reports one used generator, `USED_C_INDEX=387`, `USED_C_GENERATORS=1`, `S_SATURATION_GENERATORS=403`. The last H-coefficient `LH[size(C)+1,1]` is `TAIL`, i.e. the coefficient of the extra generator `s`. Unused `C[i]` do not enter the combination.

Composition:

```text
FINAL[i] = sum_j LU[i,j]*HCOEFF[j]
CHECK    = s^N*la^20 - s^(N+1)*TAIL - sum_i I[i]*FINAL[i]
```

Algebra, given the two checked lifts: `la^20 = sum_i C[i]*LH[i,1] + s*TAIL`, multiply by `s^N`, substitute `s^N*USED[j] = sum_i I[i]*LU[i,j]`, and obtain exactly `CHECK=0`. The source aborts and prints `CHECK` on any nonzero. The AWS stream prints `PASS_FINAL_REES_IDENTITY` once, then prints `FINAL` and `TAIL` from the same variables. Therefore the printed identity

```text
s^96*la^20 - s^97*TAIL = sum_{i=1}^9 FINAL[i]*I[i]
```

is a literal zero-polynomial identity in the nine original generators. `FINAL[3]=FINAL[9]=0` is permitted: those generators are simply unused. No denominator is inverted. The only scalars outside `Z` are elements of `Q`, which is the coefficient field of `ring R=0,…`.

Minimality of `96` is not claimed and is not needed. Any working `N` with a checked lift of `s^N*USED` yields, after the ring homomorphism `s↦1`, the same dehomogenized membership `la^20-TAIL|_{s=1} ∈ I|_{s=1}`. A smaller individual exponent is the V3 race, which this review does not use.

This review did not re-multiply the 403-generator saturation or the lift matrices. The algebraic source of `CHECK` is the identity claimed, and the fail-closed AWS wrapper accepted `CHECK==0` with empty diagnostics.

---

## Charge 3 — Exact dehomogenization

**CONFIRMED. Hand substitution of `s=1` into `la^20-s*TAIL` recovers the printed eight-term `W` with every sign and coefficient. Clearing by `972` is the primitive integral representative. `W` lies in the dehomogenized nine-generator ideal, not in a saturation or a localization with an uncharged denominator.**

Printed `TAIL`:

```text
-1/243*s^7*q1*q0^3
-1/54*s*q1*r2*r1
-7/108*s*q1*r1^2
-1/54*s*q1*r2*r0
+1/54*s*q0*r1*r0
-1/108*s*q1*r0^2
-la^20*tau
```

Then `la^20-s*TAIL` expands to

```text
la^20
+ (1/243)*s^8*q1*q0^3
+ (1/54)*s^2*q1*r2*r1
+ (7/108)*s^2*q1*r1^2
+ (1/54)*s^2*q1*r2*r0
- (1/54)*s^2*q0*r1*r0
+ (1/108)*s^2*q1*r0^2
+ s*la^20*tau.
```

At `s=1` this is

```text
la^20*tau + la^20
  + (1/243)*q1*q0^3
  + (1/54)*q1*r2*r1
  + (7/108)*q1*r1^2
  + (1/54)*q1*r2*r0
  - (1/54)*q0*r1*r0
  + (1/108)*q1*r0^2,
```

which is the AWS `DEHOMOGENIZED_WITNESS` line and the displayed `W` in `WITNESS_RESULT.md` (spacing only). The `q0*r1*r0` sign is negative on both sides; every other displayed coefficient is positive.

Denominators `{1,243,54,108}`. Factorizations `243=3^5`, `54=2·3^3`, `108=2^2·3^3`, so `lcm=2^2·3^5=972`. Multipliers: `972/243=4`, `972/54=18`, `972/108=9`, and `7·9=63`. Hence

```text
W_Z = 972*la^20*tau + 972*la^20
    + 4*q1*q0^3
    + 18*q1*r2*r1
    + 63*q1*r1^2
    + 18*q1*r2*r0
    - 18*q0*r1*r0
    + 9*q1*r0^2.
```

`gcd(972,4,18,63,9)=1` because `gcd(4,63)=1`, so this is a primitive integral representative of `W` over `Z`.

Why this is not a saturation leftover or an uncharged localization: the identity of charge 2 is polynomial in `s` with no inversion of `s`. The homomorphism `s↦1` therefore sends a combination of `I[1],…,I[9]` to a combination of the nine dehomogenized generators. `s^N` and `s^{N+1}` both become `1`, so `W` equals that dehomogenized combination. Rational coefficients live in the declared field `Q`. There is no hidden `s`-denominator and no appeal to `C=I:<s>^∞` after dehomogenization.

---

## Charge 4 — Weight and cone arithmetic

**CONFIRMED. Term weights at `(4,1,1,22,22,30,30,30)` are `81,80,88,82,82,82,82,82`. The seven strict halfspaces, the absence of `rho`, and the margins `1,8,2,2,2,2,2` all recompute.**

Variable order `(la,tau,rho,q1,q0,r2,r1,r0)`, weight `w=(L,T,H,Q1,Q0,R2,R1,R0)=(4,1,1,22,22,30,30,30)`.

| term | weight |
|---|---:|
| `la^20*tau` | `20·4+1=81` |
| `la^20` | `20·4=80` |
| `q1*q0^3` | `22+3·22=88` |
| `q1*r2*r1` | `22+30+30=82` |
| `q1*r1^2` | `22+2·30=82` |
| `q1*r2*r0` | `22+30+30=82` |
| `q0*r1*r0` | `22+30+30=82` |
| `q1*r0^2` | `22+2·30=82` |

No displayed term contains `rho`, so `H` is unrestricted by this witness.

Unique least-weight term `la^20` if and only if every other exponent strictly exceeds `20L`:

```text
T                         > 0,          # from la^20*tau
Q1 + 3*Q0                 > 20*L,       # q1*q0^3
Q1 + R2 + R1              > 20*L,       # q1*r2*r1
Q1 + 2*R1                 > 20*L,       # q1*r1^2
Q1 + R2 + R0              > 20*L,       # q1*r2*r0
Q0 + R1 + R0              > 20*L,       # q0*r1*r0
Q1 + 2*R0                 > 20*L.       # q1*r0^2
```

These are exactly the seven halfspaces in `CONE_PREMISES_PROVISIONAL.md`. At the charged point, `20L=80` and the strict margins are `1-0=1`, `88-80=8`, and five copies of `82-80=2`, i.e. `1,8,2,2,2,2,2`.

The AWS firewall string still reads `CONE_INEQUALITIES_NOT_YET_AUDITED` because the LPDP job does not enumerate terms. The halfspaces above are a hand consequence of the printed support, not an output of the still-running global-`dp` job.

---

## Charge 5 — Initial-ideal theorem

**CONFIRMED for the campaign’s least-weight convention, as a finite witness-obstruction region, not as a Gröbner cone or Newton fan.**

The formulation’s one-polynomial lemma is the correct one: if `W=A*la^20+sum_{e∈S} B_e x^e ∈ J` with `A≠0` (here `A=1`) and `e·w>20 w_la` for every nonzero non-target term, then the least-weight initial form of `W` is `A*la^20`, hence `la^20∈in_w(J)`. Other elements of `J` may contribute other initial generators, including terms of weight below 80; that does not remove `in_w(W)` from `in_w(J)`. The argument does not require `in_w(J)` to be constant on the region.

On the torus where all eight coordinates `(la,tau,rho,q1,q0,r2,r1,r0)` are nonzero, `la` is a unit, so `la^20` is a unit and the torus saturation of `in_w(J)` is `(1)`. The localization is empty: there is no torus-valued leading coefficient for this fixed source and any weight in the open region.

This is strictly weaker than a Gröbner cone (the rest of a reduced initial basis may jump) and strictly weaker than a complete Newton fan (other source/support/cancellation walls are not represented). `CONE_PREMISES_PROVISIONAL.md` and the formulation both say so; this review adopts that name: **witness obstruction region**.

---

## Charge 6 — Exceptional faces and coefficients

**CONFIRMED. Equality faces are not settled by this certificate. The parametric warning is correct. This run is a single rational source.**

On a wall `e·w=20 w_la` the initial form of `W` is `la^20` plus at least one other term of `W`. A nonmonomial initial form generally has torus zeros, so emptiness of the torus localization of `in_w(J)` does not follow from this witness. Each inclusion-minimal face requires a separate full face-initial-ideal torus saturation (or another explicit monomial/preimage certificate). Face results do not propagate to adjacent cancellation walls. No face is excluded here; `CONE_PREMISES_PROVISIONAL.md` states that.

Parametric form in the formulation: a moving source must charge every denominator into a polynomial `D(θ)` and the target coefficient into `A(θ)`, and persist only on `D(θ)A(θ)≠0` together with the strict inequalities for currently nonzero support. Vanishing of a non-target `B_e` only drops an inequality. Vanishing of `A`, a pole, or a change of the charged ideal is exceptional and must be recomputed. The V2 jobs (and this certificate) are only over the pinned point `a=1,h=q2=k=nu=0,mu=2/3`. They do not supply a parametric neighbourhood.

---

## Charge 7 — AWS endpoint

**CONFIRMED for the registered r6d LPDP V2 run. The global-`dp` cone job and the V3 minimum-exponent race are pending corroboration, not evidence, and not prerequisites of the identity.**

| Check | Result |
|---|---|
| Host / tag | r6d `100.26.198.153`; `max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826T021500Z_r6d_LPDP`. Harvested hostname `ip-172-30-0-45`, uname Linux AWS, matches the V1 r6d box |
| Worker PID / caps | `pid=206223`; compiler `2097152` KiB / 300 s; solver `201326592` KiB (192 GiB) / 21600 s; `nice -n 10`; tag case-match `…_v2_20260826T*` |
| Source closure | Harvested `source.check` and `source.prelaunch.check` both `OK` on compiler, worker, preregistration, AWS registration, V1 compiler, and `base_B.sing`. Verified locally from the case root |
| Compile | rc `0`, empty stderr, `source_diff=…` once, `PASS_CONTROL2_LA20_SYZYGY_V2_COMPILER` once, compiled SHA `e9b2c159…` |
| Solve-source pin | `solve_source.sha256` / `compiled.sha256` both pin that same digest; `solve_source.check` `OK` |
| Solve | rc `0`, empty stderr, empty `singular.stdout.diagnostics` (worker greps `^// **`, `?`, `halt`, `error occurred`, `wrong type`, `skipping text`, `outdated identifier` — the V1 hole) |
| PASS markers, each exactly once | `PASS_TOY_SATURATION_AND_LIFT`, `PASS_SAT_WITH_EXP_DIRECT_EQUALITY`, `PASS_H_LIFT`, `PASS_USED_C_LIFT`, `PASS_FINAL_REES_IDENTITY`, `PASS_CONTROL2_LA20_SYZYGY_LPDP` |
| `FAIL_` / parser diagnostics | none in stdout; diagnostics file empty |
| Timing / RSS / swap | wall `13:21.79`, max RSS `13115180` KiB, `Swaps: 0`, `Exit status: 0`. UTC `02:18:57Z`–`02:32:19Z` agrees. Pre/post `free -h` both show `Swap: 0B` |
| Worker close | `PASS_REMOTE_WORKER`; `COMPILE_DONE` / `SOLVE_DONE` present; no `COMPILE_FAILED`, `SOLVE_FAILED`, or `REFUSED` |
| Singular | 4.3.2 (`4330`), same family that rejected V1 `GCD` |

The extra child PID `206404` appears only in `WITNESS_RESULT.md`, not in `worker.metadata`. That is an unauditable operational annotation. It is not used as evidence; the payload is bound by the stdout/time/rc hashes.

Still-running, **not** cited:

- `cases/max12_912_order3_d1_double_root_control2_la20_dp_cone_v2_20260826/` is registered on Box03 and has no harvest.
- `cases/max12_912_order3_d1_double_root_control2_la20_syzygy_minexp_v3_20260826/` is a minimum-individual-exponent race and has no harvest. Its own preregistration says it is neither evidence against V2 nor a cone claim.

Quarantined V1 LPDP and V1 global-`dp` are negative software controls only.

---

## Charge 8 — Scope firewall

**CONFIRMED. The strongest theorem this package may state is the one in the Promotion section.**

Admissible:

- the explicit dehomogenized membership `W ∈ J` for the frozen nine generators;
- the fixed-weight obstruction `la^20 ∈ in_w(J)` at `(4,1,1,22,22,30,30,30)`;
- emptiness of the eight-coordinate torus localization at that weight;
- the seven strict witness halfspaces as the open set on which this same `W` has unique least-weight term `la^20`;
- all of the above only for exact `a=1,h=q2=k=nu=0,mu=2/3` and this support.

Not admissible, and not claimed by the frozen firewall strings:

- moving axis or loads;
- nonzero `q2`;
- another support mask;
- equality faces, all faces, or a full Gröbner cone;
- a complete Newton fan or whole-double-root theorem;
- D1 globally, or JC2;
- a moving-parameter neighbourhood of the rational source;
- any V1 exponent or V1 stdout line;
- minimality of `96`.

Corrected A already gave `la^20` in the special fibre of this same finite ideal, in two orders, by contraction rather than by an explicit preimage. Promotion of corrected A remains valid and independent. This V2 run supplies the missing preimage; it does not re-derive the eight charged equations, which remain byte-extracted from reviewed B.

---

## Nits, not defects

1. Harvest contains five macOS AppleDouble `._*` sidecars, 163 bytes each, not in the freeze. Ignored.
2. Harvested `SOURCE_CLOSURE.sha256` uses paths relative to the case root, so `sha256sum -c` from inside `aws_r6d_LPDP/` cannot see V1. The worker ran `cd "$run"` at the case root; local verification from the case root passes.
3. `WITNESS_RESULT.md` records Singular child PID `206404` with no harvest file that contains it.
4. Producer status lines still say “hostile review pending” / “cone inequalities not yet audited.” Those are timestamped producer flags, not contradictions of the identity.

No source or certificate repair is required.

LA20_WITNESS_CONFIRMED
