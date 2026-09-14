# D125 small-source exporter: complete implementation, prep only

Status: **PREPARED, REAL CLIENTS UNEXECUTED; INDEPENDENT ENGINEERING GATE REQUIRED.** Author `/root/model_productivity`, 2026-09-06; frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

A complete six-client normalized receiver-plus-polynomial-lift constructor is implemented in `box/d125-small-source-exporter-prep-20260906/`. It preserves every free coefficient and both unrestricted lift parameters. It has not constructed any actual degree-15/25 Jacobian or lift system, run CAS, accessed AWS, or claimed a point/proper ideal. Only metadata and tiny declared polynomial fixtures were evaluated.

## 1. Exact client and mathematical scope

The immutable preflight `e0debc7d…` supplies the full three polygon cases and two outer forms. `baseline.py` is a byte-identical private copy of its trusted `client.py`, not an edited predecessor. The terminal normalization gate `cd69c238…` confirms the normalized receiver's characteristic-zero geometric necessity/equivalence at its exact incoming-F2 scope. Both terminal mathematical producer reports and the lift producer's full checker were read. After root notified that the lift gate was terminal, its whole report `4295593a…` was read and its hash checked; no live gate report/code/log/receipt was consumed. The separate Sol engineering gate was not read.

The sufficient-client theorem is now a named **gated input**, not an implementation result: a characteristic-zero point of the complete receiver equations, monicity, nonzero c and all 105 negative coefficient equations reconstructs a polynomial Keller pair of exact degrees 75/125. The nonautomorphism conclusion uses the gate's named external plane automorphism degree-divisibility criterion. No F2 necessity theorem is needed for this sufficiency direction. Necessity for the original campaign family remains at the incoming chain's conditional scope.

The theorem is one sufficient contract, **not an “iff” characterization of every possible counterexample certificate**. In particular the gate's broad “only/iff” prose is not consumed. The 120 universally indexed Jacobian slots outside our gamma bound are identically zero, so no extra 120 rows are needed (§3). No graph pivot, B reconstruction/compression, additional target shear, unforced support deletion, or lambda saturation is used.

Over `L=Q` or `Q[rho]/(rho^2-3rho+1)`, use precisely the preflight's full fixed outer/inner faces and zero constants. The unequal scalar stays the fixed unit `c=-5/(9kappa)`; common cases retain c,z and `z*c-1`. Recorded fixed-unit guard rows are zero identities, not additional variable guards or restrictions. There is no origin guard and no c=1 gauge. Both field embeddings remain available; a row with coefficient `a+b*rho` is ONE polynomial over L, never split into two equations. Unknowns are not restricted to rational points.

Append `lambda2,lambda3`, each allowed to be zero, and substitute

`gamma=v^-1`, `pi=v^4*u-lambda2*v^2-lambda3*v-v^-1`.

Its coordinate determinant is `+v^2`, so `[A,B]=c*gamma^2` transports to `[P,Q]=c`. The constructor imposes polynomiality, rather than inferring it from the constant Laurent bracket.

## 2. Ring, counts and literal lift formula

The order is the preflight's global graded reverse lexicographic order: increasing exponent pairs for free A slots, then free B slots, then c,z when present, then lambda2,lambda3. Variable ids are zero-based and source coefficients remain literal constants or single source variables. No circuit variables are introduced.

| case, separately for each outer field | free A/B | total ring variables | full J rows | lift rows | all retained rows |
|---|---:|---:|---:|---:|---:|
| unequal | 71 / 196 | 269 | 660 | 105 | 803 |
| common-3 | 77 / 214 | 295 | 660 | 105 | 816 |
| common-4 | 98 / 269 | 371 | 660 | 105 | 816 |

These are **verified metadata counts, not observed production output**. Full row totals include 31 or 44 zero fixed-assignment residuals, six fixed-unit vertex rows and one scalar guard row. All raw polygon coefficient-map records are retained, including prescribed zero face coefficients and the two fixed constants. The six nonorigin vertex values/inverses are explicit in guard metadata. Fixed c and its inverse, or the free c/z ids, appear in the header. Exact degrees 15/25 are supplied by the prescribed monic pi tops and support bounds, not new degree variables.

For each supported coefficient `a_(i,j)` and output `u^t v^e`, the contribution is

`a_(i,j) * j!/[t! b! d! (j-t-b-d)!] * (-1)^(j-t) * lambda2^b lambda3^d`,

where `e=5t+3b+2d-i-j`. The implementation loops over `(i,j)` and b, then **forces** `d=(e+i+j-5t-3b)/2`, accepting precisely nonnegative integral d with `j-t-b-d>=0`. Factorial division is exact integer multinomial arithmetic. The source coefficient is multiplied as one coefficient-field element, and equal coefficient-variable monomials are collected exactly.

For A, emit all `(t,e)` with `t=0,1,2` and `5t-15<=e<0`: 15+10+5=30 rows. For B use `t=0,1,2,3,4`, `5t-25<=e<0`: 25+20+15+10+5=75 rows. Labels are `LIFT/A/t/e` and `LIFT/B/t/e`, retaining identically zero rows. No output-index or monomial sampling is used. Degree bounds are the gate's 7/12 in lambdas and 8/13 total semantic degree; they are not term-count estimates.

## 3. Complete Jacobian and row stream

Emit `J/I/J` for every `0<=I<=23`, `0<=J`, `I+J<=38`: exactly 660 rows. For each A coefficient `(i,j)`, force B's index `(k,l)=(I+1-i,J+1-j)` and add `(i*l-j*k)*a_(i,j)*b_(k,l)`. Subtract c at `(2,0)`, including when the derivative sum is zero. Thus unequal target subtraction contributes `+5/(9kappa)`.

Completeness is elementary: supported A/B gamma exponents are at most 9/15; every nonzero differentiated term has gamma exponent at most23 and total degree at most38. Negative output indices have zero determinant. The universal triangle `I+J<=38` has780 indices; its 120 points with `I>=24` have identically zero coefficients for every permitted source coefficient. Retaining660 therefore imposes the full ordinary bracket, not a truncated subsystem.

Canonical JSONL order is: header; every variable; all A/B coefficient-map records; all fixed-assignment residual rows; all660 J rows; all105 lift rows; six fixed-unit vertex rows; the scalar guard; complete footer. Each literal term is `[field_wire, sorted_variable_id_list]`, where `field_wire=[[a_num,a_den],[b_num,b_den]]` denotes `a+b*rho` exactly. In rational clients b is zero. Fractions are canonical strings, not floats. The footer includes complete row/kind/term/zero counts, all unused variable ids, prefix record count and SHA-256 of every preceding canonical byte.

`verify_stream` regenerates the exact expected full stream and compares each canonical record byte-for-byte, then requires EOF. It detects footer-resynchronized corruption, not just accidental checksum drift. This is **same-formula self-replay, not independent certification**. The row formulas' tiny independent controls do not replace a later independent full-stream review.

Optional `.sing` emission is **import only**: exact Q ring or `(0,rho)` coefficient field with `minpoly=rho^2-3*rho+1`, displayed variable order and `dp`; all literal rows including zeros, each labeled in a comment; an import marker, `size(I)` diagnostic, then `quit`. There is no basis, dimension, elimination, msolve or solver command. `size(I)` is not a mathematical verdict or a substitute for the JSONL row count. No Singular parser has been run in this prep task. JSONL is authoritative; the Singular file is generated from the same row records, hashed, and still needs an actual bounded import check and independent review.

## 4. Fail-closed production entry and custody

No production authority was issued in this task. The CLI requires an authority JSON file and exact case/branch. Before producing a real specification or opening an output, `ProductionContext` checks:

- explicit boolean root GREEN and construction-only authorization; nonempty job id and a 64-hex registration pin;
- Linux, DMI `sys_vendor == Amazon EC2`, and the **instance id from `board_asset_tag`** matching the registered instance;
- exact resolved current directory matching a registered subdirectory under `/home/ubuntu/`;
- exact builder/baseline/normalization/lift-contract/lift-gate hashes, exact client labels;
- positive integer wall/CPU/address-space/aggregate-output caps and an unexpired timezone-aware deadline no farther away than the wall cap.

Hard implementation ceilings are600 wall seconds,600 CPU seconds,8GiB address space and1GiB aggregate output; an authority may be stricter, never larger. The context applies kernel AS/CPU limits and a real-time deadline covering construction, full replay and manifest hashing. The outer reviewed campaign runner remains required for future job custody; this code does not replace that runner or authorize an instance.

Production context records PID, PGID, `/proc/self/stat` start ticks, boot id, observed DMI instance, cwd and caps. Repeated checks reject identity/cwd drift and deadline expiry. The public production specification refuses an absent context. Without context, low-level arithmetic is limited to explicitly tiny supports (at most four lift source slots of degree<=7, or a Jacobian source product<=16). Tests call no production specification and generate no actual degree-15/25 rows.

All outputs are exclusively created as `client-CASE-BRANCH.{jsonl,sing,manifest.json}` in the registered cwd. Existing files are never overwritten. The aggregate budget charges bytes **before each write**, including optional Singular and final manifest. Partial files survive exceptions or caps. A collision on the optional Singular name can leave a new empty JSONL; it cannot overwrite the colliding file. A completion manifest is written only after the JSONL footer and strict full replay; it records hashes/bytes, row footer, host/job identity, caps and `independent_certification=false`. Hashing reads bounded1MiB blocks. No subprocess, remote control or CAS invocation exists in the production constructor.

Authority schema: `jc2.d125-small-source-authority/v1`, with keys `root_green`, `construction_only`, `job_id`, `registration_sha256`, `instance_id`, `working_directory`, `case`, `branch`, `deadline_utc`, `caps` and `pins`. The caps keys are `wall_seconds,cpu_seconds,as_bytes,aggregate_output_bytes`. Pins keys are `exporter_sha256,baseline_sha256,normalization_gate_sha256,lift_contract_sha256,lift_gate_sha256`. Test authority fixtures are explicitly fake observations passed only to the pure checker; they never create a production context.

## 5. Tiny controls and remaining gate

Final **53 controls PASS** in normal Python and `-O`; normal arithmetic 0.054s,21,792KiB peak RSS. Each process is capped at30 wall seconds,25 CPU seconds,512MiB AS. The largest direct polynomial fixture has receiver degree6, four slots per member and two symbolic lambdas, not a real client. Tests include:

- all tiny negative coefficients versus independent repeated multiplication of the actual Laurent inverse; forced Jacobian rows versus an independent tiny pair loop;
- a positive forward-image fixture reconstructing u exactly with both symbolic lambdas; its negative rows vanish;
- the actual zero-lambda omission fixture `(A,B)=(gamma,gamma^2*pi+gamma^3)`, whose bracket is gamma² but whose inverse has exactly the negative coefficient `[u^0v^-1]P=1`;
- six-client **metadata only** counts; golden inversion; a single exact quadratic-field Singular coefficient and refusal to put it in a Q ring;
- missing/incorrect authority, caps, registered identity and host checks; explicit refusal of actual-degree lift/J arithmetic without context; aggregate-byte-cap and real exclusive-file-collision controls.

Six **actual stream mutations**, each with its footer checksum/counts deliberately repaired, are rejected: delete `LIFT/A/0/-1`; replace a golden polynomial row by its two rational-component rows; reverse the target's c sign; change a fixed-zero coefficient-map entry; remove the scalar guard constant; alter a literal coefficient elsewhere. Each mutation is also run as a separate subprocess in normal and optimized Python, exiting1 at the intended strict replay error. Missing-footer and existing-file-preservation tests pass. These are data-integrity controls, not properness claims about the toy ideal.

Final receipts contain13 terminal subprocesses (one optimized positive run plus12 external mutations); the direct normal run is separately pinned. Earlier passing receipts and their tiny files remain. Following root's terminal theorem notification, final source additionally pins that gate and emits explicit unit-guard metadata; all final controls were replayed afterward. There was no failing production attempt and no production output.

Next action requires root's separate engineering review and explicit GREEN, exact EBS/worker readiness custody and a fresh registered directory. A measured construction/import pilot may then exercise this unchanged code. No solve, graph substitution, B compression or paid worker is authorized or retained by this prep. All owned local subprocesses/file writers are terminal at handoff; STOP/idle.

## 6. Pins

Immutable inputs:

- preflight report: `e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80`;
- `xmodel/d125-minimal-receiver-gate-fable5-20260906.md`: `cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d`;
- `xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md`: `433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad`;
- its `check.py`: `77f8ee1b0eae54831bdf1e255685449e41f30feb2b9697c6808ef9110230f10d`;
- `xmodel/d125-small-polynomial-lift-gate-fable5-20260906.md`: `4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122`.

Owned box `box/d125-small-source-exporter-prep-20260906/`:

- `baseline.py`: `ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`;
- `exporter.py`: `9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703`;
- `test_exporter.py`: `331e97c84f22592a1a28842df7c11e84e4f72355a906c156403eb5eaca490b2b`;
- `run_controls.py`: `ef6c9f011a723b16e744911a540e41bdc70822856f74609bcd55e02d667f1429`;
- `test-normal-final.json`: `3822fede355b747a313f1bf9580b78dc18d83f4776aab59bd72e66bf8d39f10e`;
- `test-O-pass-final.json`: `84079e32f53f0e185ec92975264d181d691e295d4a3543af198e687ff2f6d119`;
- `control-receipts-final.json`: `cdc9bd7c98c8c1f5502ecb4521e8b2cd7193992ef1bffbd565cd65bf22dfbe70`.

`custody.json` SHA-256 `5b9472c169288d84b01d8a6ab38a73f668c1a6db881dfeccece32a31e6f2e16d` records source pins, no production authority, no remote ownership, zero production rows and terminal writers. No shared ledger, immutable predecessor or protected project was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14915`.
- Body SHA-256:
  `8bfbe17f61533904053eaa8428e42772be09733a5175301fee3264ade94ad86a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
