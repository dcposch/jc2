# Hostile review V2 — `(8,12)` order-four `mu_4 != 0` coefficient-curve freeze repair

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md` |
| Target SHA-256 | `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621` |
| Compiler | `cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve_v2.py` |
| Compiler SHA-256 | `b000ed1557bd307dc37b92fd1ff3fbe1e075cec169721d346a28599374890e1b` |
| Freeze list | `cases/max12_812_order4_mu4_nonzero_curve_20260825/FREEZE_V2.sha256` |
| Freeze-list SHA-256 | `d4a5c584a792d38d74c09b607da4777ba83715d0d092c590b99f15083b35e31b` |
| V1 review (inspection parent) | `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-20260825.md` |
| V1-review SHA-256 | `0877fc072583c3a484ad7740e0abc6a0a981be6ad4b17e4002765f21e97cd57b` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none in the V2 freeze delta |
| Smallest missing hypothesis | none that breaks a numbered V2 claim. Computational geometry remains unrun in this review |
| Reviewer / model | Grok 4.6 (xAI). Independent V1-to-V2 delta review. The V1 overall token is not evidence. Charged parent reviews were opened only to recompute their hashes |
| Method | source reading and hand review of the repair delta; SHA-256 of every `FREEZE_V2.sha256` path, of the freeze list itself, and of the V1 client/compiler; unified diff of V1 against V2; no CAS, solver, substantive exact Python, Sage, Singular, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named V2 producer, compiler, freeze, and V1 inspection parent uncommitted) |
| Date | 2026-08-25 |

Independently recomputed SHA-256 of the V2 client is `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621`, matching the launch pin, `FREEZE_V2.sha256`, and the compiler's `EXPECTED_CLIENT_SHA256`. Independently recomputed SHA-256 of the V2 compiler is `b000ed1557bd307dc37b92fd1ff3fbe1e075cec169721d346a28599374890e1b`, likewise matching. Independently recomputed SHA-256 of `FREEZE_V2.sha256` is `d4a5c584a792d38d74c09b607da4777ba83715d0d092c590b99f15083b35e31b`. Independently recomputed SHA-256 of the V1 review is `0877fc072583c3a484ad7740e0abc6a0a981be6ad4b17e4002765f21e97cd57b`. The V1 overall token, the V2 status sentence that the V1 mathematics was “confirmed”, and every charged `CONFIRMED`/`REPAIR` string were not used as evidence. Live AWS outputs under `aws_compile_*` and `aws_recon/` were not opened and are not evidence. No file other than this review was written.

---

## Verdict

The V1 blocking defect was cryptographic misidentification of three otherwise-named parents. V2 replaces exactly those three 64-character strings by the SHA-256 values of the named source audit, terminal theorem, and terminal review; moves the compiler client pin in the same freeze; and lists those three parents together with the V1 review in `FREEZE_V2.sha256`. Every listed hash recomputes. Numbered mathematics in V2 §§0,2–5 is byte-identical to V1. The V2 compiler retains, unchanged as source, the no-load order-four reconstruction, independent shifted polynomial, mutual ideal-containment checks, lead identity `v5+2*r7`, mandatory `r7` saturation before dimension, AWS gate, and scope firewall. Remaining inherited nits (`deg` in `(4.1)`, JSON canonicalization, usage-string filename) were not introduced by V2 and are not freeze failures.

This review does not rerun the V1 hand derivations and does not consume a live geometry endpoint. It confirms the freeze repair and the retention of the already-written client.

**CONFIRMED**

---

## Hashes

Recomputed SHA-256 of every path listed in `FREEZE_V2.sha256`, and of the freeze list itself:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md` | `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621` | V2 client; matches launch pin, freeze list, and compiler `EXPECTED_CLIENT_SHA256` |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve_v2.py` | `b000ed1557bd307dc37b92fd1ff3fbe1e075cec169721d346a28599374890e1b` | V2 compiler; matches launch pin and freeze list |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/FREEZE_V2.sha256` | `d4a5c584a792d38d74c09b607da4777ba83715d0d092c590b99f15083b35e31b` | freeze list; matches launch pin; internally consistent for every named path |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/run_compile_v2_aws.sh` | `67b55e7a24b2d385c296adb1de05cc386e1bc55c2446db7521533527085f477e` | freeze list; execs `compile_curve_v2.py` |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/launch_remote_v2.sh` | `cb77b335ad78b4a3946fee29592a2fdf72b50363f9a2f23e53a6bd7bb158eb88` | freeze list; compile mode uses the V2 runner |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/run_geometry_aws.sh` | `71dcafdfbf2ec6b07e0bf98cbe7b89179e40c7e4e6c31753c6599c34102094c8` | freeze list; byte-identical to the V1 geometry runner |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` | shared Faber source; matches V2 client §1, compiler `EXPECTED_SHARED_SHA256`, and freeze list |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` | freeze list |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | named source audit; matches V2 client §1 and freeze list |
| `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | named terminal theorem; matches V2 client §1 and freeze list |
| `xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` | named terminal review; matches V2 client §1 and freeze list; unused as a verdict |
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-20260825.md` | `0877fc072583c3a484ad7740e0abc6a0a981be6ad4b17e4002765f21e97cd57b` | V1 review, freeze-listed as the repair warrant; unused as a verdict |

V1 controls, recomputed only to identify the delta:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-20260825.md` | `2a7c5b6e09818d523954f8896a339d5f31407650b1777dd83f7a5bbbe5eda4fa` | V1 client; superseded; not in `FREEZE_V2.sha256` |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve.py` | `5c1add225079ff56454654bcbb893326bc95dc34cf5c3f763aa58a0ef012b8de` | V1 compiler; superseded; not in `FREEZE_V2.sha256` |

No `FREEZE_V2.sha256` line mismatches. No charged parent string in V2 §1 mismatches the named file.

---

## Attack A — three repaired parent strings

**CONFIRMED.** The three 64-character strings printed in V2 §1 are the SHA-256 values of the three named files.

| Named file | V1 §1 printed (false) | V2 §1 printed | Actual SHA-256 of the named path |
|---|---|---|---|
| source audit | `092dfb6dcdbb4fc52438b4027bef994607f61d9f04247ff19c5db2237af2ff9c` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| terminal theorem | `1cd824c9f82601620500187c3a98cdd105769ee12988b2e3b12b7179f99a3fdb` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` |
| terminal review | `db67f16d8e287ba74bb49e26d558b43f81592298446a8685143345089518fc79` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` |

Each V1 string still agrees with the true hash through eight hex characters and then diverges; those three strings are absent from V2. Each V2 string equals both the file hash and the corresponding `FREEZE_V2.sha256` line. The three named paths exist. No other parent string in V2 §1 is charged: the shared Faber pin `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` already matched in V1 and still matches.

The terminal-review file is hashed, freeze-listed, and unused as a theorem. Its header token is not an input to this verdict.

---

## Attack B — every semantic change V1 to V2

**CONFIRMED as a hash-and-pin repair, with no mathematical edit.** Unified diff of the two clients and the two compilers, read against the two freeze lists and the two AWS compile wrappers.

**Client.** The only content changes are:

1. Title suffix `V2`.
2. Status block: the V1 two-line specification banner becomes a V2 banner plus the sentence that V2 changes only three mistranscribed charged-parent hashes.
3. The three parent SHA-256 strings of §1, as in Attack A.

V2 §§0,2,3,4,5, including `(0.1)`–`(0.5)`, `(2.1)`–`(2.3)`, `(3.1)`, compiler contract items 1–7, `(4.1)`, and the §5 firewall, are byte-identical to V1. No numbered identity was rewritten. No generator, weight, saturation, or scope sentence was added or deleted.

**Compiler.** The only content changes are:

1. Docstring suffix `V2`.
2. `CLIENT` path retargeted to the V2 client file.
3. `EXPECTED_CLIENT_SHA256` retargeted to `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621`.
4. Payload status token suffix `-V2`.
5. A trailing newline after `main()`.

`Ring`, Faber loop, `g=faber[12]`, inverse depth `last_q=n+last_tail-1`, tail sign `cscale(-1,…)`, weight `12+ell`, independent `V=g^2-f^3+2f`, high-degree fail, `Itail`/`Icoef`, both `reduce` containments, `reduce(v5+2*r7,Gtail)`, `sat(Itail,ideal(r7))` before `dim`/`size`, `require_registered_aws`, `mkdir(..., exist_ok=False)`, shared-Faber pin, and the `scope` block are textually the V1 compiler. The `scope` keys and values are unchanged, including `order4_mu4_nonzero_closed: False` and `JC2: NOT_CLAIMED`.

**AWS compile wrapper and launcher.** `run_compile_v2_aws.sh` is the V1 compile runner with the usage string, the Python path, and a trailing newline changed: it still refuses non-Linux and non-`Amazon EC2`, still exports `JC2_REGISTERED_AWS_LANE`, still `ulimit -v 134217728`, still `timeout 7200`, and execs through frozen `ops/aws_exact_lane.sh`. `launch_remote_v2.sh` is the V1 launcher with the usage string, the compile-mode runner path, and a trailing newline changed. Geometry mode still points at the unchanged `run_geometry_aws.sh`. That geometry runner takes a Singular input as argv and does not pin a client hash; sharing it across V1 and V2 is correct.

**Freeze list.** V2 drops the V1 client, V1 compiler, V1 compile runner, and V1 launcher, and adds the V2 client, V2 compiler, V2 compile runner, V2 launcher, the three named parents, and the V1 review. Shared Faber, `run_geometry_aws.sh`, and `ops/aws_exact_lane.sh` are retained at the same hashes. That is the freeze coupling the V1 review demanded: parent strings, producer bytes, and `EXPECTED_CLIENT_SHA256` move together.

Attacks that failed: a silent rewrite of `(0.3)`–`(0.5)` or `(2.1)`–`(2.3)` under the hash repair; a V2 compiler that still pins the V1 client; a V2 compile runner that still execs `compile_curve.py`; a freeze list that advertises the new client while omitting the repaired parents.

---

## Attack C — compiler retention, independently of live output

**CONFIRMED as source.** The V2 compiler was read, not run. No emitted `.sing`, JSON, or AWS stdout is evidence.

**Pins the V2 client.** `CLIENT` is the V2 path. `EXPECTED_CLIENT_SHA256` equals the recomputed V2-client hash. `main` refuses a mismatch before `build_order4`. The payload records that same pin.

**No-load order-four reconstruction, unchanged.** Coefficient ring `Ring([a0,…,a6])`. No `k_10`, `k_6`, `k_2`. Faber polynomials `j=0,…,12`, then `g=faber[12]`. Monic/degree check on `g`. Inverse depth `last_q=18`. Tails `ell=1,…,7` scaled by `-1`, each monomial checked to weight `12+ell`.

**Independent shifted polynomial, unchanged.** `vpoly` is `zmul(g,g)-zpower(f,3)+2f`. Any exponent `>11` fails.

**Two presentation checks, lead identity, mandatory `r7` saturation, unchanged.** Emitted Singular still: `Itail=r1,r2,r3,r4-1,r5,r6`; `Icoef=v11,…,v6`; both `reduce` containments; `lead_ok=(reduce(v5+2*r7,Gtail)==0)`; `SOURCE_EQUIVALENCE=FAIL` and `quit` if any of those fail; only then `sat(Itail,ideal(r7))`, `std(SS[1])`, unit/dimension/size/basis. Saturation remains before `dim`. No expected dimension is hardcoded.

**AWS guard, unchanged at the advertised entry points.** `require_registered_aws` still demands Linux, `Amazon EC2`, and a nonempty `JC2_REGISTERED_AWS_LANE`. The V2 compile runner repeats the OS/vendor check and execs the frozen lane wrapper. `build_order4` itself is still not AWS-gated; that is the inherited process nit, not a new leak.

**Inherited compiler/spec nits, none introduced by V2.** `(4.1)` still lists `deg(std(J_4))` and the emitter still does not print `deg`. Lead reduction is still only modulo `Gtail`. On-disk JSON still uses default separators plus newline while recorded SHA-256 uses `separators=(",", ":")` and no newline. The argv fail string still names `compile_curve.py`. These are classified below; they are not V2 freeze failures.

---

## Attack D — freeze closure and firewall

**CONFIRMED.** `FREEZE_V2.sha256` is a closed, internally consistent manifest of the V2 producer, the V2 compiler, the V2 compile entry points, the shared Faber source, the AWS lane wrapper, the three repaired parents, and the V1 review. Every line recomputes. The V1 client and V1 compiler are correctly absent.

V2 §0 and §5, and the compiler `scope` block, still state the same restriction: a point of `C_4` is a 7-tuple of constants with ordinary Faber tails `(0,0,0,1,0,0,r_7)` and `r_7\neq 0`. Emptiness of `I_4` over an algebraically closed field of characteristic zero would eliminate the `mu_4\neq 0` order-four leaf. A nonempty component is not a source, not `8dR_7=j\,dx/u`, not a terminal-power/Belyi profile, not a polynomial Taylor realization, not a Keller pair, and not JC2. Failed containment, missing `r_7` saturation, timeout, OOM, or engine disagreement remain **NO VERDICT**. The `mu_4=0` Davenport–Stothers elimination is still a separate stratum. Order-two loads are still absent.

`REGISTRATION_V2.md` is not freeze-listed. It is an operational ledger, not a parent of the client, and is not used as evidence. In particular its recorded AWS compile and geometry tags are not inputs.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field. Let `f=z^8+a_6 z^6+\cdots+a_0` be the generic monic depressed octic over `L`, and let `g=F_{12}(f)` be its Faber polynomial of degree twelve, with no lower Faber constants. Write

```text
w=f^{1/8}=z+O(z^{-1}),
w^{12}-g(z(w))=sum_{ell>=1} r_ell w^{-ell}=:E.
```

Then, as an identity of Laurent series in `w` with coefficients in `L[a_0,\ldots,a_6]`,

```text
g^2-f^3=-2 w^{12} E+E^2,
```

and `E^2` has strictly negative `w`-order, hence strictly negative `z`-order. Consequently the polynomial `V=g^2-f^3+2f` has degree at most eleven, the two unsaturated ideals

```text
(r_1,r_2,r_3,r_4-1,r_5,r_6)
    =  ([z^{11}]V,[z^{10}]V,[z^9]V,[z^8]V,[z^7]V,[z^6]V)
```

of `L[a_0,\ldots,a_6]` are equal, the change of generators is triangular with diagonal `-2`, and

```text
[z^5]V+2 r_7  lies in  (r_1,r_2,r_3,r_4-1,r_5,r_6).
```

On the exact-order-four leaf `(r_1,\ldots,r_7)=(0,0,0,mu_4,0,0,R_7)` with `mu_4\in L^*` one has

```text
g^2-f^3+2 mu_4 f=-2 R_7 z^5+O(z^4),     [z^5]=-2 R_7.
```

The weighted `G_m`-action `a_i\mapsto\lambda^{8-i}a_i` sends `r_ell\mapsto\lambda^{12+ell}r_ell`. Over an algebraic closure, every geometric point of this leaf is represented, after a finite constant-field extension, on the affine chart `r_4=1`, `r_7\neq 0`; the residual `mu_{16}` is finite, fixes `r_4`, and acts on `r_7` by a primitive character. Emptiness of the saturation

```text
I_4=(r_1,r_2,r_3,r_4-1,r_5,r_6):r_7^{infinity}
```

would therefore eliminate the entire `mu_4\neq 0` order-four terminal leaf. Nonemptiness is only a coefficient-infinity necessary condition.

The V2 compiler, as read in source, reconstructs both presentations from the frozen shared Faber primitives, demands the two containments and the lead relation before saturating, pins the V2 client by SHA-256, and refuses to run off a registered AWS lane. Its geometry gate is emitted, not executed, in this review.

This is the V1 client theorem with uniquely hashed parents. It is not a new mathematical claim.

---

## Scope firewall

Accepted, not enlarged:

- coefficient-infinity necessary condition on the normalized chart `r_4=1`, `r_7\neq 0`, with no lower Faber loads;
- exact equality of the two unsaturated six-generator ideals, and the congruence `[z^5]V+2r_7\equiv 0` modulo that ideal;
- weighted normalization `lambda^{16} mu_4=1` over an algebraic closure, without arithmetic descent;
- AWS-only reconstruction of those presentations from frozen shared Faber source.

Refused:

- source exactness `8dR_7=j\,dx/u` as a coefficient-fibre statement;
- polynomial Taylor realizations at finite branch points;
- terminal-power/Belyi divisor constraints;
- a Keller pair;
- order-four closure of the `(8,12)` cell;
- JC2;
- any live AWS emptiness, dimension, or basis statement;
- the V1 overall token, and the V2 status sentence that treats that token as a mathematical certificate.

---

## Findings, classified

**Fatal.** None. The three V1 parent pins that failed now recompute. No numbered identity in V2 §§0,2–5 was edited. The V2 compiler pins the V2 client and retains the reviewed reconstruction, checks, saturation, AWS gate, and firewall.

**Repairable, non-blocking, inherited, not introduced by V2.**

1. Target `(4.1)` still lists `deg(std(J_4))`; the emitted Singular program still does not print it. The ideal remains inhomogeneous (`r_4-1`). Recording `dim`, reduced-basis `size`, and the basis is still the honest affine gate. Align `(4.1)` with the compiler, or drop `deg`.

**Cosmetic, inherited or labelling.**

2. V2 status says the V1 mathematics was “confirmed by hostile review”. The V1 overall token was not a confirmation of the freeze. The numbered identities in §§0,2–5 were not rewritten; the sentence is documentary overclaim, not a parent-hash defect.
3. V2 §1 still says the hostile-review/erratum chain is recorded in the source audit. The erratum remains a separate file. The client still does not consume repaired `(7.2)`.
4. Lead-relation reduction is still only modulo `Gtail`. After both containments this is equivalent to “either ideal”.
5. On-disk JSON bytes are still not the hashed canonical dumps.
6. Calling `C_4` a curve before dimension is known. No expected dimension is a verdict token.
7. `build_order4` can still be imported off AWS; `main` cannot.
8. The argv fail string still names `compile_curve.py`.
9. `REGISTRATION_V2.md` is present in the case directory and is not freeze-listed. It is not a parent of the client.

**Fatal freeze failures.** None. Every `FREEZE_V2.sha256` line matches the named file. The three repaired parent strings match the named source audit, terminal theorem, and terminal review.

---

## Smallest failing identity

None in the V2 freeze delta. The V1 identities

```text
SHA-256(source audit)   = 092dfb6dcdbb4fc52438b4027bef994607f61d9f04247ff19c5db2237af2ff9c
SHA-256(terminal theorem) = 1cd824c9f82601620500187c3a98cdd105769ee12988b2e3b12b7179f99a3fdb
SHA-256(terminal review)  = db67f16d8e287ba74bb49e26d558b43f81592298446a8685143345089518fc79
```

are absent from V2. Their replacements are the actual SHA-256 values of those three files. No identity in V2 `(0.1)`–`(0.5)`, `(2.1)`–`(2.3)`, `(3.1)`, or the compiler contract of §4 was changed, and none of those displayed identities is failed by the freeze repair.

Live AWS outputs were not used as evidence. The V1 overall token was not inherited.

CONFIRMED
