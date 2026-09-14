# Static implementation gate: F10 r=1 complete builder/checker/execution gate (Fable 5.1)

tag=f10-r1-complete-builder-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1); different-model STATIC source review of Astra's unexecuted packet
launch=root actual invitation; actual start 12:23:38 UTC (recorded, not reset); hard stop = earlier of 12:43:38 and 12:45:00 UTC, i.e. 12:43:38 UTC
subprocesses=ZERO mathematical subprocesses of any size. Nothing was imported, compiled, syntax-checked or run. Only date, ls, mkdir, sha256sum, cat, printf, grep, wc ran. Every claim below is hand inspection of source text against the accepted 16q/16r algebra.

## 0. Custody, read scope and classification

All ELEVEN charged objects under /tmp/jc2-lane.rnkxYL/inputs were hashed BEFORE their WHOLE reads; the eleven digests match the invitation's list exactly (pins: box/f10-r1-complete-builder-gate-fable5-20260909/input-pins.sha256). The producer artifact (befb566b) carries body_bytes 8133 and body_sha256 f0e0c4f9, closed 12:17:42Z, consistent with the report's own seal. The CAPRUN object (1b908c1f, 5212 bytes) was used only as the literal lines 1-180 interface excerpt: option names, types and REMAINDER shape. No whole CAPRUN re-audit, no other live body, log, receipt, provenance file or corpus read. The accepted 16q contract and 16r Euler presentation interiors were not re-audited; they are applied as the specification the code must realise.

Classification. Everything below is STATIC. No runtime, emitted row, count, degree, precision, lifecycle or control result exists; each control stays DESIGNED. Verdicts are on the source text as written.

## A. Builder. CONFIRMED (static), one cosmetic note.

Variable order. `names` is exactly `u, ell, d0, d1, v0, v1, v2, k1, k2, k3, k4, omega` (builder.py:16), width 13 with S last; `var(i)` unpacks in that order (line 63). All arithmetic is `fractions.Fraction` over sparse exponent-tuple dicts; `add`, `mul`, `scale`, `ds`, `scalar` delete or filter every zero coefficient, so a stored monomial is always nonzero. Division is only by the fixed integer `j-3*i` (line 85), never by a parameter; no localisation by u.

Module and target. `f=S*d-u`, `h=1-u*d+S*v`, `k=k1 S+...+k4 S^4`, `A=[k,h,f,S]` (lines 65-70) are the 16r cubic-test coefficients A_0..A_3. The delta array (lines 71-73) is 1, u, -ell, ell*u-1, 2u-ell*S, -(u^2+2S), 2uS, -S^2, term for term the 16r section B expansion, including the delta_3, delta_4, delta_5 signs.

Forcing. For j=4..0 the builder forms delta_(j+2) - (j+1)f'B_(j+1) + 2fB'_(j+1) - (j+2)h'B_(j+2) + hB'_(j+2) - (j+3)k'B_(j+3) (lines 78-81), which I re-derived from the operator identity (lA_k'B_l - kA_kB_l')t^(k+l-1) at k+l=j+3: this is exactly 16r (5). B is seeded with B_5=S^2 and zero B_6, B_7, so at j=4 the h and k terms vanish correctly. Inversion divides the S^i slot by j-3i; a NONZERO coefficient at a resonant slot (j=3,i=1 or j=0,i=0) raises (line 87), never drops. Because sparse dicts hold only nonzero entries, an absent resonant slot is exactly the accepted identity, and B_3, B_0 then contain no S^1 / S^0 term: beta=gamma=0 and k0=0 are realised by construction, not by deletion. Envelope: forcing S-degree above 7-j raises (line 88); E1 above S^8 or E0 above S^9 raises (line 103).

Residuals. E1 = 2k'B_2 + h'B_1 - hB_1' - 2fB_0' - u and E0 = k'B_1 - hB_0' - 1 (lines 94-96) are the t^1, t^0 rows re-derived from the same operator at k+l=2 and 1. Rows: E1/S0..S8 and E0/S0..S9 all emitted including empty wires (lines 101-105), then GUARD (line 106); 20 ordered slots. a=k4 (the variable), b=[S^7]B_0 re-keyed with S-exponent 0 (line 98), guard=omega*a*b-1 (line 99). Wires are sorted reduced numerator/positive-denominator strings (line 61); JSON is written with `open(...,"x")`, `allow_nan=False`, integer exponents only. Slot lists use `range(5-j)` for A and `range(8-j)` for B (lines 112-113), the exact envelopes 4-j and 7-j; the Jacobian slot map `range(10-h)` matches the contract's 9-h bound. I found no stale index, width or list error and no coefficient loss.

Cosmetic. The `resonances` record stores a literal `"forcing": []` (line 93), not the computed resonant coefficient; it is a declaration whose truth rests on the raise at line 87 and on the checker's t^5/t^2 vanishing, not on the record. Harmless, but a future version should store the computed (empty) slot.

## B. Independent checker. CONFIRMED (static), two minor notes.

Independence. checker.py imports only execution_gate; it has its own 14-axis ring (12 parameters, S/p, t/z), its own `combine/times/derivative/projection`, and rebuilds expected A from the parameter definitions (lines 116-121). Delta is constructed FACTORED as 1+ut-ell*t*Pi-t*Pi^2 with Pi=t-ut^2+St^3 (lines 142-144); the producer's descending array is never read.

Determinant. AA, BB are assembled with genuine t powers and the full A_S B_t - A_t B_S is formed (lines 138-141). It demands t-degree <= 7 and vanishing of t^2..t^7 of jacobian-Delta (lines 150-152). Saved forcings are checked by subtracting the diagonal jB_j-3SB_j' from the independently computed t^(j+2) coefficient and comparing Delta's coefficient minus that rest (lines 156-160): I verified this equals Q_j without any recurrence. Because E_jB_j has no S^1 slot at j=3 and no S^0 slot at j=0, the resonance identities are verified through the t^5 and t^2 checks, not through the metadata literal.

Low rows. `saved` residuals are compared to the actual t^1/t^0 coefficients only when `low=True` (line 172); every row is compared to `saved` (line 176). This is the one deliberately weakened path and it is confined to the two low rows, which is what the dropped-constant control needs.

Inverse substitution. S=p z^3 - z^2 + u z, t=z^-1 (line 181). For a term S^i t^k the code skips i>=k (line 190). Justification: S=z(pz^2-z+u) has z-order exactly 1 when u is the symbolic variable and order 2 when u=0, so S^i t^k has z-order >= i-k (>= 2i-k at u=0), never negative for i>=k; the skip is a sufficient no-pole condition in both modes. For i<k it expands the trinomial to at most the fourth power (k<=5), keeps every negative-z monomial, rejects any (z,p) slot outside the ten listed, and demands each listed slot is empty (lines 192-198): together this is "negative part identically zero", with the p^1 slots (-2,1), (-1,1) included. I hand-checked the three A rows on the actual A: z^-3 absent (A_3=S has no constant), z^-2: u-u=0, z^-1: -1+ud0+(1-ud0)=0.

Restoration. It demands a=[S^4]A_0 equals the variable k4 and b=[S^7]B_0 is a nonzero polynomial (line 201), that the saved a, b and guard wires equal these objects (lines 202-205), and A_3=S, B_5=S^2 via the A equality and line 126. With the accepted 16r section A this is the whole hypothesis set for A/a, B/b monic with c_orig=1/(ab); the description strings (line 208) are labels, not the evidence. It does not impose k4=1 or b=1. The u=0 mode is a literal specialization: `atom(0)` is empty and `read` drops every u-monomial (lines 63, 70-73), a ring homomorphism, so all comparisons stay consistent; b at u=0 is nonzero as a polynomial because the accepted 16r F-family (u=0) has b>0.

Wire hygiene. `no_floats` recurses over lists and dicts; exponents must be `type(x) is int` and >= 0 (bools rejected), strictly increasing keys (duplicates and disorder rejected), numerator/denominator strings re-canonicalised by `str(int(s))==s` (rejects "+1", "01", " 1", "1_0", unicode digits), nonzero numerator, positive denominator, gcd 1 (lines 52-62).

Minor notes. (1) Non-numeric coefficient strings, missing keys or a non-dict artifact raise ValueError/KeyError/TypeError, not InvalidArtifact: fail-closed, but unclassified and no receipt. (2) JSON `true` equals 1 in Python, so `"r": true` or `"k0": false` would pass lines 43-45; cosmetic, no mathematical effect.

## C. Negative controls. Preconditions CONFIRMED by hand; every control remains DESIGNED.

Dropped constant. E0's all-zero exponent monomial is exactly -1: delta_0 contributes the explicit scalar; k'B_1 always carries a k_i factor; B_0 has no parameter-free monomial because Q_0 = -ell - f'B_1 + 2fB_1' - 2h'B_2 + hB_2' - 3k'B_3 has every term parameter-bearing (B_2 does, since Q_2's only parameter-free source is h=1+... times B_4' which is parameter-bearing). So `remove_constant` finds exactly one term ["-1","1"] in residuals.E0 and in rows[9] (E0/S0), and the same at u=0. The weakened pass (low=False) sees nothing of the deletion; the full check fails at "full low bracket E0". Pass-then-fail is correctly sequenced (checker.py:272-280) and an unexpectedly passing mutation raises.

Upper coefficient. From Q_4 = -2uS - d0 S^2 - 6 d1 S^3 and eigenvalues 1,-2,-5 the genuine B_4 is -2uS + (d0/2)S^2 + (6d1/5)S^3, so the d0*S^2 term has coefficient exactly 1/2 in both B[4] and coefficient_slots.B[4][2]; the precondition holds. Prediction: the first rejection is "nonzero full upper bracket t3" (the -4k'B_4 term of the j=1 row), not t6, because the loop checks t^2 first and t^2 does not involve B_4. Guard: omega*k4*b - 1 has exactly one parameter-free term, -1, in both locations. Leading-top: replacing a by the constant 1 fails "saved leading coefficient restoration". No control has run; no pass count, no `-O`, no >2^53 precision evidence is implied or created.

## D. Execution boundary. Code CONFIRMED as a metadata-only gate; registration items are root's.

Order. Both entrypoints call `authorize` before `json`, `hashlib`, `fractions`, artifact reading or any construction (builder.py:130-132, checker.py:256-260). Rejections in order: schema/enabled (template is `enabled:false`, operation `build_or_check_separately`, so it rejects at line 19 or 23), job/admissibility presence, operation, EC2 vendor and `i-` asset tag, exact instance and hostname, `sys.flags.isolated` and `dont_write_bytecode` (real command-line flags, not the module attribute), child argv element-for-element as `/usr/bin/python3 -I -B <resolved script> argv[1:]` (so the MODE and receipt are baked into each registration), raw NUL-split parent cmdline equal to the exact required CAPRUN argv `--wall-seconds --cpu-seconds --rss-bytes --rss-sample-seconds --term-grace-seconds --cwd --stdout-file --stderr-file --telemetry-file -- child`, cwd equality, non-empty non-negative non-"0" cap strings, mandatory pins for script, execution_gate.py and runner, the checker artifact pin, then every pinned file re-hashed (lines 19-70). All nine options exist in the CAPRUN parser excerpt with `--wall-seconds`, `--stdout/stderr/telemetry-file` required and command as REMAINDER after `--`; `--overwrite`, `--stdin-file` and `--lifecycle-sample-seconds` cannot appear, so outputs stay exclusive and RSS/CPU caps are mandatory. Cap strings that pass line 60 but not CAPRUN's positive_int/positive_float never reach the child because CAPRUN parses first. Outputs use exclusive `"x"` opens.

Code flaws found: none blocking. Two limitations to record: the interpreter `/usr/bin/python3` and stdlib are not mandatory pins (root may add any path to `file_sha256`, all entries are verified); a missing /sys DMI file off-EC2 raises FileNotFoundError rather than the RuntimeError text (still fail-closed).

Root's pending registration responsibilities, distinct from code: instance/hostname/job_tag; the admissibility hash (line 21 checks presence only, no file is compared); resolved runner path, cwd, caps as the literal strings passed; exclusive stdout/stderr/telemetry/OUTPUT/RECEIPT paths; exact parent and child argv per mode; pins for script, gate, runner, artifact and optionally interpreter; current primary applicability and actual frontier output; pre/post authority hashes; the real no-CAS dummy descendant RSS/TERM/KILL regression for this new caller; an explicit operation/cap record. There is no command allowlist in the code: the only executable child is the registered script itself, and the code contains no solver, prime, Groebner, allocator or shell path. No same-user adversary claim is made or needed; parent identity is by cmdline only, an accepted CAPRUN limitation.

## E. Source, classical scope and what a PASS would mean. CONFIRMED with bounded scope.

The artifact's `r=1, m=4, n=7` are S-degree bounds of t-coefficients (t-degrees 3 and 5), and 16q/16r plus the classical-admissibility report give the actual ordinary degrees 112/196 with nonconstant intermediate brackets c*Delta, c*(p^2+ell p-u-z), c*g. Nothing in the packet types 4/7 or 28/49 as Keller degrees; any frontier declaration must be 112/196 with gcd 28, max 196, neither dividing the other. Admissibility is bounded: the checked GGV gcd>=16, GGHV max<125 table, closed-H and retired F2/F9 rows do not close it. From memory only, without new research: Magnus (coprime degrees), Nagata (prime gcd), Applegate-Onishi (gcd<=8), Moh (max<=100) and the divisibility criterion are all weaker than or subsumed by the checked conditions and do not apply to (112,196). I identify no concrete missing applicable condition; this is not an exhaustive openness statement.

A runtime PASS in every mode would establish only that the emitted artifact is an exact, complete, correctly normalised presentation of L_1 as accepted in 16r: not a point, not a unit, not properness, not a prime, basis or solve. This static all-pass licenses only root's bounded validation registration decision.

## Verdicts

A CONFIRMED (static). B CONFIRMED (static). C preconditions CONFIRMED, all seven controls DESIGNED, none PASS. D code CONFIRMED as metadata gate; registration and dummy-regression items are root's, listed above. E CONFIRMED at bounded scope. No first failure exists in any group; the precise repairs for a future version are the two cosmetic items (computed resonant slot in the record; InvalidArtifact wrapping of malformed-wire parser errors and strict `type(...) is int` on r/m/n and gauges) and the optional interpreter pin. Do not patch the frozen packet.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check; no corpus scan.

<!-- BODY-END -->
