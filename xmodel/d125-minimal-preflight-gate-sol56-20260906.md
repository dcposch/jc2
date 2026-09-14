# Independent D125 minimal six-client coefficient preflight gate

Status: **CONFIRMED at the PREP_ONLY software/coefficient-interface scope.** No scoped producer assertion is refuted. A production stream, independent production verifier, lift emission, adapter import, ideal, and solve remain **GAP**. Review date 2026-09-06; reviewer Sol, producer Astra. No same-model independence claim is made. Producer `model_productivity` remained TERMINAL/IDLE.

## Scope and custody

The seven charged files were read from immutable `/tmp/jc2-lane.MAp4nm/inputs` and rehashed. Their SHA-256 values match `e0debc7d…` (130-line report), `ec2fa2d…` (281-line client), `15d49bf…` (184-line tests), `cd69c238…` (mathematical gate), `7dec79af…` (composition), `433cc2fe…` (sealed lift contract), and `e47fd16c…` (reasoning guardrail). Root's supplied manifest pin `3d3702f9…` and owned-pin result are provenance inputs; the individual immutable files were independently checked here.

The `cd69c238…` review licenses the face and normalization data only at its conditional standard-F2/receiver-point scope. I accept that license and do not redo or enlarge its theorem. The `433cc2fe…` report was read only for the extension interface described below; its live mathematical gate was not read and its acceptance/properness/counterexample consequences are not promoted. No live producer code/log, old source input, shared ledger, adapter, custody tool, protected-project content, CAS, SymPy, AWS, solver, or external service was used or changed.

## Separated verdicts

| area | CONFIRMED | REFUTED | GAP |
|---|---|---|---|
| field | Exact `Q(rho)` arithmetic, irreducible `rho^2-3rho+1`, norm/inverse, formal conjugation, and canonical two-coordinate wire | none | no scoped field gap |
| six contracts | Complete supports, fixed faces including zeros, free-slot order, guards, counts, and target convention | none | the 660 rows are a conservative index envelope, not emitted polynomials |
| toy-row semantics | Forced-index kernel equals an independently differentiated tiny pair; target subtraction and one-field-row semantics are correct | none | hard-capped toy evidence is not full-scale certification |
| serializer | Canonical toy JSONL, exact wire decode, roster, footer counts, and prefix hash survive independent checking | none | no production serializer or independent production verifier exists |
| production boundary | `production_export()` refuses, and the row kernel rejects a product above its cap before expansion | any reading of `ec2fa2d…` as a production exporter | complete slot/row/guard streaming and adapter import are absent |
| lift extension | The sealed two-name/105-index extension is compatible with the six base rings and fields | no interface conflict found | no augmented stream; placement/order/IDs and theorem consequences remain unreviewed |

## Independent coefficient and contract checks

I used a separately written `Fraction`-pair implementation. It recomputed

`(a+b*rho)(c+d*rho)=(ac-bd)+(ad+bc+3bd)rho`,

`N(a+b*rho)=a^2+3ab+b^2`, and

`(a+b*rho)^-1=((a+3b)-b*rho)/N`.

Discriminant 5 is nonsquare over Q. The involution `rho -> 3-rho` formally retains both embeddings; no numerical embedding was selected or counted as a separate client. Wires are exactly `[[a_num,a_den],[b_num,b_den]]`, with reduced fractions and positive denominators.

Supports were rebuilt by convex area decomposition, not the client's half-plane routine. Outer and inner face polynomials were independently multiplied in exponent dictionaries, including absent monomials as prescribed zeros. The resulting literal entry dictionaries were then compared with all six actual contracts; this is not `make_contract()==make_contract()`.

| case | raw A/B | fixed A/B | free A/B | base ring variables | planned residuals |
|---|---:|---:|---:|---:|---:|
| unequal | 83/215 | 12/19 | 71/196 | 267 | 698 |
| common-3 | 94/241 | 17/27 | 77/214 | 291+`c,z`=293 | 711 |
| common-4 | 115/296 | 17/27 | 98/269 | 367+`c,z`=369 | 711 |

For each branch the outer faces contain all 10 A and 16 B slots; the unequal inner faces contain 2/3 slots and the common faces 7/11. Each inner/outer intersection is the one shared high corner, and the origin is disjoint. Rational outer powers contain 6 A and 10 B fixed-zero slots; golden outer powers are dense. Both constants are fixed zero. Every other polygon lattice slot remains free, with contiguous zero-based IDs: A first, then B, each lexicographic in `(gamma,pi)`.

Exactly six nonorigin vertices are fixed nonzero and guarded; the origin is not guarded. Unequal has low coefficients `1` and `5/(9*kappa)` and fixed `c=-5/(9*kappa)`, so the `(2,0)` residual adds `+5/(9*kappa)`. Common cases use the same normalized `mu=1`, one free `c`, and one `z` with literal row `z*c-1`. The exact variable tails are empty or `c,z`; `c1extra` is absent.

The independently enumerated row coordinates are every `(I,J)` with `0<=I<=23`, `J>=0`, `I+J<=38`: `sum_(I=0)^23(39-I)=660`, including zero rows and `(2,0)`. Adding 31 or 44 fixed-slot residuals, six vertex rows, and one scalar row gives 698/711/711. No coefficient pair census or full Jacobian was formed.

## Tiny semantics, serialization, and corruptions

An own formal-derivative/product oracle agreed with the forced-index kernel on a 3-by-3 support. A discriminating golden fixture serialized `z+rho=0` as one field-valued row and retained the witness `z=-rho`; replacing it by two coordinate rows loses that semantics.

An independent tiny verifier parses canonical bytes, decodes every wire, recomputes rows by that derivative oracle, enforces each declared index once, and independently recomputes footer counts and SHA-256. In both normal and `-O` modes it rejected actual changed target, missing-row, missing-footer, field-coefficient, split-row, internally consistent nonzero-vertex, and fully reindexed fixed-zero-face objects. Missing-row, field, and split-row corruptions carried recomputed footer checksums. The producer's own 52 controls also passed in both modes, while its target and fixed-zero-face mutations exited nonzero in both. Producer self-replay remains only corroboration, not independent full-scale certification.

## Extension interface only

The sealed report specifies two unrestricted, zero-permitted parameters `lambda2,lambda3`, with no inverse or guard. Algebraic simplification and an exhaustive tiny-domain identity loop confirm its negative-power exponent `e=5t+3b+2d-i-j` and sign `(-1)^(j-t)`. Independent roster arithmetic gives A `t=0..2` with 30 negative-v indices and B `t=0..4` with 75, hence 105. This does not verify multinomial coefficients, specialized-zero lift rows, or any emitted lift polynomial.

The two names do not collide with base variables, add no scalar, and require no field split. Textually combining this interface with the base contracts projects to 269/295/371 variables and 803/816/816 rows. These are future bookkeeping counts only. Lambda free-zero semantics come from the sealed contract; no executable augmented object exists.

## Evidence and minimum next gate

Final evidence is under `box/d125-minimal-preflight-gate-sol56-20260906/`: `audit.py` `3e955871…`, `run_controls.py` `d37c78a8…`, normal receipt `f7aab7ec…`, `-O` receipt `c2bea69b…`, direct producer receipts `3c087efe…`/`b4926900…`, and `control-receipts-v2.json` `438d9fee…`. The independent runs each recorded 478 PASS; the final runner recorded 4 expected-zero and 18 expected-nonzero subprocesses. Each child was capped at 30 wall seconds, 25 CPU seconds, and 512 MiB; positives used under 0.17 seconds and 28 MiB. Earlier non-v2 files in the box are superseded preliminary evidence and are not cited for this verdict. No worker remains.

The minimum future full-stream gate must use a separately implemented exporter and independent verifier; seal lambda placement and all variable/row IDs; emit every slot assignment, all 660 receiver indices including zeros and target, seven guards, and all 105 extension indices including specialized zeros; independently recompute receiver differentiation and lift coefficients from the actual slot map; preserve each `Q(rho)` equation as one canonical row; and reject actual omission, sign, exponent, field-split, face, guard, and recomputed-checksum mutations. Adapter import needs a later bounded gate. None of this implies solver speedup, properness, a point, a counterexample, or any global degree-125 conclusion.

<!-- BODY-END -->
