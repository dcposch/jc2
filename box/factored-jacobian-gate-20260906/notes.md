# Reviewer notes: factored-jacobian gate (Fable), 2026-09-06

Lane: /tmp/jc2-lane.IvFwBi ; frozen basis 0d39df3c9fd69c939a8420c54d03228b9077777d ; start 10:25:58Z.

## Custody / hashes
- 11/11 indexed receipt inputs: sha256 OK in lane inputs dir and at repo paths (verified from charged-inputs.list and the .run.v2 charged_input_i_sha256 fields).
- Worker 172.30.0.56 = i-0da0cebfc97c9fd54 (IMDSv2), r7i.8xlarge, hostname ip-172-30-0-56, uptime 44 min at 10:30:26Z, 32 vCPU, 247 GB RAM (244 free), 22 GB disk free.
- Process state at 10:30Z: NO Singular/msolve/run_capped/producer python processes; load 0.00. Only system python (networkd-dispatcher, unattended-upgrades).
- All 54 custody artifacts re-hashed on worker: every SHA equals custody.json (complete_checked.sing 50792efe..., generators.jsonl 39ea3365..., J0.json bc4dfd95..., complete_export.json b91d706e..., custody.json f9000c9f...). Producer files are mode r--r--r-- / r-------- ; not touched.
- Review scratch: /home/ubuntu/factored-jacobian-review-20260906 (did not exist before; created by reviewer). Reviewer scripts hashed in scripts.sha256.

## Host-side source audit (delta2_stage8.strongest.json, 778eda93...)
- residual_rows = [] ; field Q ; branch delta2 ; stage 8 ; normalization {A3:98,B2:65,C2:22,C3:33,h2:33,h3:11}.
- maps: h3 24 rows (N=11, min_r 0), C2 33 rows (N=22, min_r 8), C3 37 rows (N=33, min_r 19), B2 194 rows (N=65, min_r 31), A3 201 rows (N=98, min_r 63); every r+z<=N; no duplicates; every coefficient expression polynomial over Q (integer literals, nonneg integer exponents, numeric denominators only).
- identifiers in maps: 437, plus target_a,target_b = 439; all in full_free_coordinates (444); unused: Z55, leader55, target_c, target_d, target_e.
- h3 r=0 row = z^8(1+z)^3 numerically -> h3_top = W^8 (X+W)^3 ; h_top = W^24 (X+W)^9 = y^9 (y-x)^24.
- degree_premap: 220 A2c rows all equal 3*B2c_r_z/2, plus target_a/2 at A2c_65_0 ; 162 B1c rows all 0 except B1c_32_0 = -target_b/3. => F = h^3 + (3D+a)h/2 + C, G = h^2 - b h/3 + D.
- Physical map (build_direct.py string_table/map_table + prior gate Arrow 1): (r,z,e) -> e X^(N-r-z) W^z with X=x, W=y-x (det +1).

## Singular 4.3.2 semantics micro test (worker, parse-only, 2-var ring)
- `1/2*x^9-3/4*y` -> 1/2x9-3/4y ; `(1/2)*x^9-(3/4)*y` -> 1/2x9-3/4y (identical) ; `3/2*x*y` -> 3/2xy ; `-1/3*x` -> -1/3x ; `33075/2*y^2` -> 33075/2y2.
- `x^9/32768` -> ERROR (`poly` ^ `number`): a fraction after an exponent is genuinely unsafe; `int i=1/2` -> error (int/int is a NUMBER in a char-0 ring, not integer division 0).
- dp lead of x*z^2+y^2*z+x^2*y is x2y (standard dp).

## Worker verification results (all under ulimit -v 48 GiB, timeout 600 s; evidence/ holds logs)
- review_reconstruct.py: 602-var flint single-polynomial rebuild; brackets hd 37,614 / ch 38,520 / cd 47,783 terms; A*hd 7,685,332; B*ch 3,556,009; J_mine 11,289,124 terms; J_mine - sum(row_ij X^i W^j) == 12-term linear-jet J0 EXACTLY (t=113.6 s, RSS 33.1 GB). graph rows 160/160 exact; inverse row == Zj*J0-1; footer/hash/census PASS; J0 compose == source J0 (45 terms, deg 8) == J0.json texts. Process then aborted at the virtual cap (rc 134) during the sign-flip control: in-script exact mutation controls NOT executed.
- review_stream_audit.py (85 s, 125 MB): all structural checks PASS; A3c_98_0 (constant of C) occurs in no generator; checked .sing == wrapped JSONL rows (1,325 rows with rationals), original .sing == unwrapped rows; footers exact.
- Singular 4.3.2 parse-only of review.sing (= first 1631 lines of complete_checked.sing + footer 668a0a7e...): rc 0, 100.5 s, 15.3 GB; 1629/1629 (size,deg,leadcoef,leadmonom,trailcoef,trailmonom) equal flint (0 mismatches).
- review_scalar_direct.py (79 s, 120 MB): direct unfactored J of explicit F,G at a point: 1468/1468 rows agree, 0 unlisted nonzero positions, 160/160 define rows vanish, inverse row 0, J0=-230872758; controls: J(G,F) 1468 mismatches, a-sign 640, W-sign 734, perturbed J_8_52 1, dropped J_1_0 -> 1 unlisted position.
- Producer artifacts after review: 54/54 hashes == custody.json; latest mtime 10:20:24Z. No reviewer processes left. Worker NOT terminated.
- Concurrent foreign dirs observed on .56 during the gate: linear-c-discriminator-20260906 (10:33-10:48Z) and linear-c-root-replay-20260906 (10:55Z); not touched.
