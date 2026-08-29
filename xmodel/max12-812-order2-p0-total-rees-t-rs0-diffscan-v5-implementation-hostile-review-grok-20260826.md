# Hostile implementation review: derivative-scan `T-rs-0` V5

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_total_rees_t_rs0_diffscan_v5_20260826/` |
| Charged baseline | Reviewed row-streaming V2 `cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/` and its reviewed V0R1 parent |
| Producer status | **Source/software equivalence only.** This review does not consume any engine transcript, `PASS` marker, `DISCOVERY.json`, live AWS job, or ledger claim |
| Overall verdict | derivative-scan equivalent of the reviewed V2 mathematical transcript; see the scoped token at the end |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reread of every charged file. Printed `PASS` tokens are not algebra |
| Method | SHA-256 of every named pin; complete source reading of V5, V2, V0R1, and the transitive compilers/tails; independent reconstruction of the 76+7 names; local V2 emit plus the 581-statement rewrite; independent tail census and per-formula degree bounds; attack of `sigma^13`, characteristic-`p` kernels, denominators, representation, targets, and Singular 4.3.2 `diff`. No live engine, Sage, msolve, Lean, or local heavy algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

V5 does not re-derive the total family, the grade-12 ceiling, or the frozen dictionary. It asks the pinned V2 emitter for the entire unchanged 85-variable, 569-tail, seven-row program and then replaces exactly the 581 registered dependency statements by formal derivatives. The shared sentinels remain value-equivalent. Nothing larger is proved.

---

## 0. Custody and SHA pins

No `AGENTS.md` exists in or above the repository. Every file charged in the assignment was read completely, including every path in V5 `FREEZE.sha256`, the reviewed V2 package that V5 imports, that package's freeze and validator, the reviewed V0R1 compiler that V2 imports, `run_aws.sh` / `launch_host.sh` on V5 and V2, `ops/aws_exact_lane.sh`, the square-load `tail_text` compiler, the owner `source_coefficients`, and the raw-cusp V2 certificate repair map. Inspection was read-only except for writing this report. No V5 job directory exists. No engine transcript was opened.

Independently recomputed SHA-256:

| Artifact | SHA-256 |
|---|---|
| V5 `FREEZE.sha256` | `f1db35c4923cdfe97d4900455fa9743b45b76d2b9b6d4eaa7ae51ca9454e6fba` |
| V5 `compile_t_rs0_diffscan.py` | `d06210a240a37c08439164da9b5fbbd6c15e35a127923405437fca0f844a5dc8` |
| V5 `PREREGISTRATION.md` | `fa5af2578ec8a5e55dfb212d97751aca3b19ff49efa9d5a5a80fa25d8143c2ff` |
| V5 `run_aws.sh` | `d2b90d3b1ce392917dce4d52e5006321b57dca3105945d5ce6e42e55e1a94d93` |
| V5 `launch_host.sh` | `14883225e0c2278c8e72517c82e75464e22b75b8418e0cd30e5f8dac53a0bff6` |
| V2 `FREEZE.sha256` | `b505f3c51ec8a5e10936119826445d9d2b92e47dd936f6f0996ce13e52b18397` |
| V2 `compile_t_rs0_stream.py` | `5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112` |
| V2 `validate_t_rs0_stream.py` | `4ff10d85aeb91f3853a4fd2c89ac2e0fe93bd07fd2c3769241cd8f40afb01949` |
| V2 `PREREGISTRATION.md` | `84361c1e686824d90219b08f46afb6474b75e8416095eb59e39664c0d9ebf3b6` |
| V2 `run_aws.sh` | `c7016857eedc0e4b449cf61b7f21ddffb56ecc6da3f0af230fa615104c775bc6` |
| V2 `launch_host.sh` | `8481a9ffc84ef34b5822bb25b15124b7542fd50561b7ffa18047db9f2ced1911` |
| V2 equivalence review | `5c4ae553ae4e2bc63ff9c15168332daff366b9c33cfd57cfdf89d4fb9bf460b4` |
| V0R1 `FREEZE.sha256` | `1fda3e43d7480ff1497ab5abe918d917b7ae1ed2e43ee1c802616743561b616b` |
| V0R1 `compile_t_rs0_discovery.py` | `3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938` |
| V0R1 `validate_t_rs0_discovery.py` | `d05afb4961c071e7ec89a8eb5f850d91aed88ad54b17b1a9965eef52bc9adf1b` |
| V0R1 `PREREGISTRATION.md` | `300faf2a37b587f5dbe21cb3d315957f20b0482516ac7819df04c5a8f51fda80` |
| V0R1 implementation review | `51c294e0ae3d07ced3dac380814d4767bec1e5cc63bd1159cd76ce698f3f69ea` |
| owner `compile_p0_cusp_g10_g11.py` | `9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4` |
| raw-cusp V2 `compile_raw_cusp_g12_cech_v2.py` | `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` |
| `compile_square_load_ladder.py` | `77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc` |
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical tails JSON | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| Codex `T-rs` implementation audit | `5e91571d84b1bae92306bad0a31924a2b4fe3bf183ee8d75ace558bc2dd52c0d` |
| Gate-T obligation table | `50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4` |

The nine assignment hashes match. All four paths in V5 `FREEZE.sha256` rehash to the printed digest. All five paths in V2 `FREEZE.sha256` rehash to the printed digest. All six paths in V0R1 `FREEZE.sha256` rehash to the printed digest. V5's literal `STREAM_SHA256` is the reviewed V2 compiler. V2's literal `OLD_SHA256` is the reviewed V0R1 compiler. V2's literal `REVIEW_SHA256` is the charged V0R1 implementation review. `old.EXPECTED` still matches the six transitive pins above.

Hash chain at runtime:

```text
V5 FREEZE.sha256
  -> compile_t_rs0_diffscan.py
       -> STREAM_SHA256 -> V2 compiler
            -> OLD_SHA256 -> V0R1 compiler
                 -> EXPECTED -> tails, square ladder, owner, raw-cusp V2, audit, gate
                 -> EXPECTED_CANONICAL_TAILS
            -> REVIEW_SHA256 -> V0R1 implementation review
  -> run_aws.sh also sha256sum -c V2 FREEZE.sha256
       -> V2 validator, V2 compiler, V2 preregistration, V2 wrappers
```

`run_aws.sh` checks V5 `FREEZE.sha256` and V2 `FREEZE.sha256` before compile. Compile then re-checks the V2 compiler digest, `OLD`, the review file, `old.EXPECTED`, the canonical tails digest, and the derivative-safety census. A swapped V2 compiler, V0R1 compiler, review, tail file, or owner source fails closed before any `.sing` is written. V5 `FREEZE.sha256` does not itself list the V2 compiler; the pin lives as a literal inside the frozen V5 emitter. That is the same one-hop pattern V2 used for V0R1, not a missing pin.

`launch_host.sh` ships the V5 package, the entire V2 package (compiler, validator, freeze, preregistration, wrappers), the V0R1 compiler, the three hashed source compilers, `tails.json`, the audit, the gate table, the V0R1 review, and `ops/aws_exact_lane.sh`. Those are exactly the files the hash chain reads, plus the V2 validator that `run_aws.sh` invokes. V0R1's own validator and preregistration are not shipped; V5 does not import them.

No engine result is inferred from any live job.

---

## 1. Formula identity: V2 emit, then exactly 581 statements

Comparison order is the emission order of the mathematical objects, not print order. No mismatch was found.

### 1.1 V5 does not copy formulae

V5 does not copy `source_block`, `series`, `shifted_series`, `phi_text`, `emit`, or the ring/qring/extraction/Delta text. It `exec_module`s the pinned V2 compiler, calls `stream.load_old()` and `stream.emit(...)`, and reads the resulting file. The owner dictionary, the 569-term tail reconstruction, `Lambda -> sigma^2`, the targets

```text
row 1: 0
row 2: sigma^{28}*mu2
row 3: 0
row 4: sigma^{32}*mu4
row 5: 0
row 6: sigma^{36}*mu6
row 7: sigma^{38}*(J/4)
```

the 85-name `dp` ring, `qring Q=std(sigma^13)`, the twelve-factor pass gate, the six `Keep*` copies, and the `FrozenCert` / `FrozenOmit` / `Delta` identities are therefore the reviewed V2 strings, which are the reviewed V0R1 strings with V2's row-streaming layout.

V5 does **not** call `stream.main()`. That would demand a `..._stream_v2_` AWS tag. V5's own `require_aws` demands `..._diffscan_v5_`. The split is required and correct.

### 1.2 Independent reconstruction of the rewrite

V2 `emit` was executed locally (hash checks only; no AWS, no Singular). It wrote a 1829-line program. Independently reconstructed names from the same list algebra as V2/V0R1 were then substituted with V5's exact strings:

```text
before: if (subst(TPhi,{name},0)-TPhi!=0) { dep_{name}=1; }
after:  if (diff(TPhi,{name})!=0) { dep_{name}=1; }
```

Results:

| Check | Value |
|---|---|
| Names | 76 candidates + 7 inactive = 83 |
| Old statements per name | exactly 7, none other |
| Total old statements | 83 × 7 = 581 |
| Lines after rewrite | 1829 (unchanged) |
| Changed lines | 581 |
| Changed-line class | all 581 are the dependency rewrite; zero `OTHER` |
| Surviving old statements | none |
| `if (diff(TPhi,` count | 581 |
| Non-dependency text | byte-identical |

The only other `subst(TPhi,...)` sites are the seven `TSpec=subst(TPhi,rho,0)` assignments and the seven deck checks `subst(TPhi,rho,-rho)-TPhi`. `rho` is not a tested name. Those fourteen lines, the seven `subst(TSpec,ell1,0)` synthetic-omission checks, every `T_F*` / `T_K*` formula, every extraction identity, and every `Keep*` / `Delta` line are untouched.

Full-statement strings for distinct names are not substrings of one another, including the prefix families `ell1`/`ell10`/`ell11`/`ell12`, `k`/`k1`/`k2`/`k2c`/`k2_1`/`k6`/`k6_1`, `cs`/`cs1`, `a1`/`aa1`/`aaa1`. Sequential `str.replace` in V2 list order therefore cannot corrupt a longer name. V5 further requires seven old copies, seven new copies, total 581, no survivors, and `source_text != text` before writing `t_rs0_diffscan_{label}.sing`.

This is the V4 rewrite pattern with `diff` in place of the illegal `deg`, and with V3's overbroad substring postcondition not restored. V5 contains no `deg(` call.

Earliest mismatch: none.

---

## 2. The 76+7 names, seven occurrences each

Independently reconstructed from the same list algebra as V2/V0R1, then compared to V2 `emit` output and to the validator literals:

```text
candidates (76):
  ell1..ell12
  cs, cs1..cs10
  rs, rs1..rs10
  a1, aa1, aaa1, az3..az7
  a0, aa0, aaa0, ac3..ac7
  c1, e1, ee1, ez3..ez7
  c0, e0, ee0, ec3..ec7
  k, k1, k2c, k10_3..k10_8
  k6

inactive (7): k6_1, k2, k2_1, mu2, mu4, mu6, J
```

The two lists are disjoint, contain no duplicates, and with `{sigma, rho}` exhaust the 85 ring variables (12+11+11+8+8+8+8+9+1 = 76, plus 3 leftover series atoms plus 4 targets = 7). Validator `CANDIDATES` / `INACTIVE` are order-identical to the V2 compiler lists, which V5 copies into `result.json` via `**manifest`. `k` / `k1` / `k2c` / `k10_3` and `k2` / `k2c` remain distinct atoms; both `subst` and `diff` receive a ring variable, not a string prefix.

Seven occurrences per name is the seven-row loop in V2 `emit`, not a V5 invention. 76×7 + 7×7 = 532 + 49 = 581.

---

## 3. Formal-derivative equivalence

Let `Phi` be the unique reduced representative of `TPhi` in `Q = k[x_1,...,x_85]/(sigma^13)`, so every term has `deg_sigma < 13`. For a tested atom `x ≠ sigma`,

```text
subst(Phi, x, 0) - Phi != 0
```

if and only if some term of `Phi` has positive `x`-exponent. The V5 replacement

```text
diff(Phi, x) != 0
```

is the formal partial derivative of that same representative. Write a term `c * sigma^a * x^e * m` with `a < 13` and `x` not dividing `m`. Then

```text
d/dx = c * e * sigma^a * x^{e-1} * m.
```

This vanishes iff `c = 0` in `k`, or `e = 0`, or `char(k)` divides `e`. Hence:

- in characteristic 0, `d/dx Phi = 0` iff `Phi` is independent of `x`;
- in characteristic `p`, the same holds iff every `x`-exponent is strictly less than `p`.

The relation `sigma^13 = 0` does not involve `x`. Differentiating the reduced representative with respect to `x` preserves `deg_sigma < 13`, so the qring does not insert a second kernel. `d/dx` of a sigma-multiple of the relation remains a sigma-multiple of the relation.

It remains to prove every tested-atom exponent on every emitted row is at most 72, hence strictly less than each allowed prime.

### 3.1 Factor/load census, recomputed

Frozen tails, keys `'1'`–`'7'`:

```text
36 + 54 + 58 + 81 + 89 + 120 + 131 = 569
```

Every monomial has length 10. Jet weights all match `12+row`. Load components are in `{0,1}` with total load at most 1 (also rejected by `tail_text` if violated). Independently:

| Quantity | Value |
|---|---|
| max coefficient-factor count `sum(m[:7])` | 9 |
| max load count `sum(m[7:])` | 1 |
| monomials with 9 factors | 2, both load-free: row 6 `F6^9`, row 7 `F5 * F6^8` |
| pairs `(9,1)` | 0 |
| load types among 289 loaded monomials | 190 `k10`, 72 `k6`, 27 `k2` |
| max of `8*factors + loads` | 72 |
| tail-coefficient denominators | powers of two, maximum `2^23`; none of `32003`, `65521`, `1000033` divides any |

The compiler requires `max_factors == 9`, `max_loads == 1`, and `exponent_bound == 72`, then rejects any positive characteristic `<= 72`. Characteristic 0 is falsy and is allowed. The three allowed primes all exceed 72.

### 3.2 Source-coefficient degree bound eight, against every `F0..F6`

V0R1/V2 `source_block` (the formulae actually assigned to `T_F*` / `F_F*`):

```text
p = -2*rho^2 + sum_{i=1}^{12} 2*sigma^i*ell_i
c = sigma^2 * (cs-series)
r = (p^2 + sigma^2*(rs-series))/4
n3 = sigma^3*(az-series)
n2 = sigma^3*(ac-series)
n1 = sigma^3*(p*az + ez)/2
n0 = sigma^3*(p*ac + ec)/2
F6 = 2p
F5 = 2c
F4 = p^2 + 2r
F3 = 2p*c + sigma^2*n3
F2 = c^2 + 2p*r + sigma^2*n2
F1 = 2c*r + sigma^2*n1
F0 = r^2 + sigma^2*n0
K10, K6, K2 = the three series
```

Max exponent of any **single tested atom** in each formula, by the exact sum/product exponent calculus (no cancellation of leading tested-atom powers: the relevant coefficients are `±2`, `1/2`, `1/4`, `1/16`, all nonzero in characteristic 0 and in the three odd primes):

| Poly | tested-atom max exponent | of which | rho exponent (not tested) |
|---|---|---|---|
| `F6` | 1 | `ell` | 2 |
| `F5` | 1 | `cs` | 0 |
| `F4` | 2 | `ell` | 4 |
| `F3` | 1 | `ell`,`cs`,`az` | 2 |
| `F2` | 3 | `ell` from `p*r` | 6 |
| `F1` | 2 | `ell` from `c*r` | 4 |
| `F0` | 4 | `ell` from `r^2` | 8 |
| `K*` | 1 | the corresponding load atom | 0 |

Total degree in tested atoms is the same column (`F0` is 4, `F2` is 3). The constant 8 is the total degree of `F0` **including** `rho` (`r ~ p^2 ~ rho^4`, `r^2 ~ rho^8`) and the jet weight of `F0`. It is a valid, non-sharp upper bound on tested-atom degree: every `F0..F6` satisfies `deg_{tested} <= 4 <= 8`. Loads contribute exponent 1 per factor. Therefore any tail monomial with `f` coefficient factors and `l` loads has tested-atom exponent at most `8f+l`, and the frozen census makes this at most 72.

A sharper bound from the same tails times the table above is 9, attained by `ell` in `F6^9` on row 6. That is still far below 72 and far below every allowed prime. The compiler's equality-to-72 check is a census lock on the *loose* formula, not a claim that some atom actually reaches exponent 72.

### 3.3 Target terms, accounted separately

`phi_text` appends `-sigma^{2(12+row)}*(mu2|mu4|mu6|J/4)` on rows 2, 4, 6, 7. Each target atom has exponent one. They are not included in `8f+l`. In the qring they are identically zero (`28,32,36,38` all exceed 12), so both `subst` and `diff` report independence, which is the inactive-custody requirement.

---

## 4. Attacks

| Attack | What actually happens | Outcome |
|---|---|---|
| `sigma^13` kills high jets, so unreduced `Phi` could depend on `x` while the qring element does not | Both tests run on the assigned, already-reduced `TPhi`. Targets and every `k2`-loaded monomial (`Lambda^{10} -> sigma^{20}`) vanish. `k6_1` sits at `sigma^1` in `K6` and the `k6` load already brings `sigma^{12}`, so `k6_1` vanishes too. `subst` and `diff` agree on the reduced representative | **Holds.** Inactive `k2`,`k2_1`,`k6_1`,`mu2`,`mu4`,`mu6`,`J` remain independent in `Q` |
| Characteristic-`p` kernel `k[x^p]` | Independently, every tested exponent is `<= 9 <= 72`. Allowed primes `32003`, `65521`, `1000033` are prime and `> 72`. V5 rejects any positive characteristic `<= 72` before emit. Characteristic 0 has no `p`-power kernel | **Holds** |
| Coefficient `e` of `d/dx x^e` vanishes in char `p` | Needs `p \| e` with `1 <= e <= 72`. Then `p <= 72`, which the compiler rejects. None of the allowed primes divides any integer in `1..72` | **Holds** |
| Denominators `/2`, `/4` in `r,n0,n1` and `J/4` | Characteristic 0 is `Q`. The three primes are odd, so 2 is invertible. Tail denominators are powers of two, maximum `2^{23}`, and are not divisible by those primes | **Holds** |
| Noncanonical polynomial representation | `poly TPhi=...` in a qring with monomial ideal `(sigma^13)` stores the unique normal form of degree `< 13` in `sigma`. `diff` and `!=0` act on that representative. Product-rule-on-unexpanded-`F`-symbols does not occur: `T_F*` are already assigned polynomials, and `TPhi` is assigned before the dependency loop | **Holds** |
| Target variables confuse `diff` | Exponent one, killed by `sigma^13`, inactive. `J/4` is `(1/4)*J`, a polynomial | **Holds** |
| Singular 4.3.2 `diff` does not accept a ring variable (the V4 `deg` failure) | Manual 4.3.2, §5.1.24: `diff(poly_expression, ring_variable)` is the partial derivative, returning a `poly`. Second argument is a ring variable, which is exactly `ell1`, `cs`, `k`, `J`, … The frozen square-load ladder already emits `diff(e4,k10)!=0` as a dependence test. V4's `deg(TPhi,name)` is a different, unsupported signature and is not present in V5 | **Holds** |
| `diff` in a qring follows Kähler differentials along `sigma^13=0` rather than the representative | Kernel `diff` is termwise on the stored polynomial. The relation does not involve the tested variables, so the two coincide | **Holds** |
| Name-prefix replacement (`k` vs `k1`, `ell1` vs `ell12`) | Full-statement match; independently, no `before`/`after` string is a substring of another name's statement; seven-and-seven census would fail if it were | **Holds** |
| V3-style overbroad postcondition matching the deck check | V5 counts `if (diff(TPhi,`, which the deck line `subst(TPhi,rho,-rho)` does not contain. Independently 581, not 588 | **Holds** |

`T_RS0_SOURCE_HASHES=PASS` remains a hardcoded engine print after Python already hashed. Same V0R1/V2 residual.

---

## 5. Frozen V2 validator versus the V5 compiler contract

V5 has no validator of its own. `run_aws.sh` invokes the freeze-pinned V2 parser. V5 `result.json` still has:

```text
status = PASS-T-RS0-DISCOVERY-COMPILER
implementation = ROW_STREAM_V2          # copied from stream.emit manifest
characteristic = argparse value
input_sha256 = sha256(t_rs0_diffscan_{label}.sing)
candidate_manifest / inactive_custody = V2 lists
candidate_manifest_count = 76
ring_variable_count = 85
```

Extra keys `accelerator`, `dependency_scan`, `dependency_replacement_count`, `max_tail_*`, `tested_atom_exponent_bound`, `streaming_compiler_sha256` are ignored by `dict.get`. The validator still:

- binds `meta.rc=0` and `meta.stdout_sha256 == sha256(stdout)`;
- binds `compiler.input_sha256` to the `.sing` it is handed (the diffscan file, not the temporary V2 file, which is unlinked);
- requires the hard-coded 76+7 tuples and the 76/85 census;
- rejects any `T_RS0_FAIL=` and any line starting `? `;
- requires the twelve source-control sentinels to be `"1"`, including `frozenCert`, `frozenOmit`, `deltaSpecial`, `deltaEven`, `deltaRho2`, `deltaMultiplyBack`, `syntheticOmission`;
- records `DELTA_NONZERO` against `size(DeltaQ)` and does not put `deltaNonzero` in the pass product;
- requires inactive bits `0`, a nonempty discovered set, `commonOrder in 0..12`, grade bits iff term-count sums, and all seven `ROW_*_STREAM_RELEASED=1`.

The engine text still prints `T_RS0_IMPLEMENTATION=ROW_STREAM_V2` because that line is not among the 581. The validator requires that string. Stale as a product name; required for contract reuse; not a math claim.

The parser is still fail-closed *parser*. It does not replay the `.sing`. A pair of forged stdout and matching meta remains a custody hole one layer above this review, inherited from V2.

---

## 6. AWS wrapper and detached launcher

`run_aws.sh` versus reviewed V2, and nothing else: V5 package path; additional `sha256sum -c` of V2 `FREEZE.sha256`; V5 compiler; `t_rs0_diffscan_` input name; V2 validator path; pass token `PASS_T_RS0_DIFFSCAN_V5_NAVIGATION_ONLY`. Characteristic whitelist, `ulimit -v`, compile/engine `timeout`, `124 -> TIMEOUT_NO_VERDICT` without invoking the validator, nonzero engine rc `FAIL_ENGINE`, validator failure `FAIL_STREAM_PARSER`, `JC2_REGISTERED_AWS_LANE`, `label=q` for characteristic 0, `aws_exact_lane.sh`, and `EVIDENCE.sha256` are unchanged.

`launch_host.sh` versus reviewed V2: V5 tag prefix, ships the V2 directory in addition to the V0R1 compiler and the same transitive sources, `setsid -f bash ...` instead of `nohup bash ... & echo $!`. Memory and timeouts remain `134217728` KiB, `900` s compile, `7200` s engine. `setsid -f` detaches a new session; it does not raise those bounds or drop `set -euo pipefail`, the archive SHA check, the characteristic whitelist, or the host allow-list. Inner `aws_exact_lane.sh` still wraps the engine in `timeout 43200 /usr/bin/time -v`, which is strictly looser than 7200 and is the same outer cap V2 used.

V5 `require_aws` rejects any lane tag not starting `max12_812_order2_p0_total_rees_t_rs0_diffscan_v5_`. A reused V2 tag fails closed.

---

## 7. Defect classification

**Math/source defect.** None. The total/frozen dictionary, seven rows, 569 tails, 85-name ring, targets, quotient grades, both negative controls, six retained cusp coefficients, `Delta` identities, and the twelve-factor pass gate are the reviewed V2 program. The 581 dependency predicates are equivalent to V2's substitution test on the reduced representatives in characteristic 0 and in each allowed prime, by the exponent bound independently recomputed above.

**Software/custody defect.** None that break equivalence or reopen a named validator hole. Residuals, not repairs owed before treating V5 as a derivative-scan stand-in for V2:

1. The constant 8 is the rho-inclusive degree of `F0`, not the sharp tested-atom degree (that is 4). The inequality `deg_tested(F_i) <= 8` holds, and the census lock `8f+l == 72` holds. The sharp exponent bound is 9.
2. Compiler JSON and engine text still say `implementation=ROW_STREAM_V2`. Required by the reused validator.
3. V5 freeze does not hash the V2 freeze file; the V2 compiler digest is a literal inside V5, and `run_aws.sh` checks V2 freeze as a bundle. Same one-hop pattern as V2→V0R1.
4. The parser cannot stop an attacker who rewrites both stdout and the lane meta after `aws_exact_lane.sh` returns.
5. `setsid -f` versus `nohup & echo $!` is a detach-style change, not a bound change.

**Scope wording defect.** The preregistration says each source coefficient has total degree at most eight *in the tested atoms*. That sentence is true as an upper bound and false as a sharpness claim; eight is the degree counting `rho`. Engine and JSON scope strings remain discovery-only and do not claim a Rees, chart, or order-two verdict.

Earliest mismatch: none. Smallest repair: none.

---

## Firewall

This review licenses treating the frozen V5 emitter as a derivative-scan evaluation of the reviewed V2 row-streaming transcript, under the same `sigma^13` prefix ring, the same 76+7 ceiling, and the same polynomial identities except for the 581 equivalent dependence tests. It does not prove:

- that any V5, V2, or V0R1 job has already passed, or that any future `PASS` marker is algebra;
- that V5 is faster or uses less memory than V2 on any host;
- agreement of any future V5 transcript with any V2 transcript at a good prime (the preregistration still requires that operationally before using V5 as an accelerator);
- Gate T for `T-rs`, or any other standard chart;
- that `rho=0` is flat, or that saturation commutes with the specialization;
- emptiness of `V(J1+J2)`, the seven residual `A` shards, or the `D(rho)` overlap;
- `k10=0`, another load ray, another square-normal cone;
- order two, `(8,12)`, maximum twelve, moving-`p`, or JC2.

The compiled scope string is `SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT`. This review enforces it.

This is no Rees, moving-`p`, order-two, maximum-twelve, or JC2 theorem.

GO_DIFFSCAN_EQUIVALENT
