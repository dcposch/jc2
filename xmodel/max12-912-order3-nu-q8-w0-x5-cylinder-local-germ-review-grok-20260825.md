I'll read the review prompt in full and then every producer, source, and endpoint it names, staying inside the listed mathematical checklist.The prompt’s checklist is narrow and local; next I’ll read the producer report, preregistration, generators, and both V3 endpoints.Next I’ll read the generators, replay, manifest, and the V3/replay endpoints named in the prompt.I’ll read both V3 endpoint artifacts and the replay output next, then check the pinned compiler for the six source rows.Replay artifacts and the pinned compiler come next, so I can check source identity and custody against the producer claim.I’ll check prior review format, V1/V2 negative controls, and a few Jacobian/localization details that could break the local-algebra step.I’ll pull a nearby Q8 review for tone, then check the selected-open statement, V1/V2 controls, and the 5×5 minor against the Jacobian.# Hostile review: finite `x5=0` cylinder local-germ exclusion

Date: 2026-08-25  
Reviewer: Grok (independent hostile algebraic-geometry and source-fidelity referee; replacement for the Claude adapter, which failed closed on API quota)  
Prompt executed: `xmodel/max12-912-order3-nu-q8-w0-x5-cylinder-local-germ-review-claude-20260825-prompt.md`, under the grok wrapper, which forbids writing the Claude output path and forbids Bash/CAS.  
Status: **REVIEW COMPLETE**

## Verdict summary

**CONFIRMED** (token repeated alone on the final line).

The claimed theorem is true at the stated scope. Over characteristic zero, on `D(x3)`, every geometric point `q` of the explicit cylinder

```text
B: x5=0, x1=x3, d2=d4=0, c*x3=1
```

has `O_(X,q) ≅ O_(B,q)`, a two-dimensional regular local domain. Consequently `x5` vanishes identically on a Zariski neighbourhood of `q` in `X`, so

```text
q ∉ closure_X(X ∩ D(x5)).
```

No finite point of `B` is a landing point of the smaller selected open `D(w*x5*(x3-2*x5))`. The argument is scheme-theoretic, not a first-order tangent test, and is not a global component claim for `X`.

I attacked all nine checklist items. No load-bearing algebraic gap, no source-identity substitution, no characteristic leak, and no firewall breach was found. Expository nits (how the displayed `5×5` minor is obtained from the `6×7` Jacobian; unnamed catenarity/CM of regular local rings) do not change the identities or the inference. The source-local exclusion of the finite `a≠0` cylinder survives.

## Files read (read-only)

Required by the prompt, in full:

- `xmodel/max12-912-order3-nu-q8-w0-x5-cylinder-local-germ-20260825.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/PREREGISTRATION.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/README.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate_v2.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate_v3.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/replay.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/MANIFEST.sha256`
- both V3 endpoints under `aws_box02_v3/` and `aws_box03_v3/`: `input.sing`, `stdout`, `stderr`, `run.meta`, `source.sha256`, and also `runner.rc`, `generator.stderr`
- AWS replay endpoint `aws_box02_replay/`: `stdout`, `stderr`, `run.meta`, `source.sha256`, `runner.rc`

Provenance, as needed:

- `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py` (`compile_quotient`, `APPROX_NAMES`, `imposed`)
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (header and hash-pin contract)

Supplementary custody (read-only, not CAS): `run_v3_remote.sh`, `run_replay_remote.sh`, `V3.manifest.sha256`.

## Execution disclosure

This session has no shell and no CAS. I did not recompute SHA-256, did not execute Singular, and did not run `replay.py` or any generator. Computational facts are taken from the frozen V3/replay bytes and checked by cross-file hash-string agreement, by reading the emitted Singular source, and by hand substitution of the cylinder into the lowest source rows. That is exactly the prompt’s constraint, not a second-engine confirmation.

---

## 1. Source identity — CONFIRMED

`compile_quotient("approx")` returns `names = ["w","c","d2","d4","x1","x3","x5"]` and `imposed = (1,3,5,7,2,4)`. Both V3 `input.sing` files realise that contract:

```text
ring R=0,(w,c,d2,d4,x1,x3,x5,ib), …
ideal I=e1,e3,e5,e7,e2,e4;
ideal E=x5,x1-x3,d2,d4,c*x3-1,ib*x3-1;
```

The six imposed rows are exactly `(e1,e3,e5,e7,e2,e4)` from the hash-pinned compiler. `w` is a ring variable and is not a generator of `E`; it remains free. The localisation equation is `ib*x3-1`, as claimed. Outputs `e6,e8` are emitted and reduced, never imposed.

V3 Boolean certificates, both lanes:

```text
cylinder_dim=2
source_rows_zero=1
Fw_zero=1
```

With `option(redSB)` and `GE` a Gröbner basis of `E`, `reduce(I[i],GE)==0` is ideal membership, so `I ⊂ E` scheme-theoretically on the localised chart: `B ⊂ X` on `D(x3)`, not a set-theoretic vanishing. `Fw_zero=1` is the six `w`-partials of the imposed rows, i.e. column 1 of the `6×7` Jacobian, all reducing to `0` modulo `E`.

No slipped extra constraint:

- `w=0` is not in `E` and is not substituted in the compiler path `coordinates="approx"`.
- Parity enters only as the already-quotiented corrected-Q8 source (`p=1` involution quotient); it is not an extra cylinder hypothesis.
- Terminal rows `e6,e8` stay out of `I`.
- Alignment `x3-2*x5=0` is not imposed. On `B` one has `x3-2*x5=a≠0`. The relation `x1=x3` is part of the definition of `B`, not a restriction of the source.

Hand check, no CAS: on `E`, `e1` is identically `0`; `e2` collapses to `4/9 x1 x3 - 4/9 x3^2 = 0`; the `w`-free part of `e3` is `-4/9 c x3^2 + 4/9 x3 = 0` once `c x3=1`. This is consistent with `source_rows_zero=1` and with `w` remaining a free parameter of `B`.

The two V3 polynomials `e1..e8` agree byte-for-byte across engine/order; only the ring ordering, `std`/`slimgb`, and the printed engine/order tags differ.

## 2. Rank exactly five — CONFIRMED

`J` is the full `6×7` Jacobian of `(e1,e3,e5,e7,e2,e4)` in `(w,c,d2,d4,x1,x3,x5)`. Column 1 is `∂/∂w`. The auxiliary `ib` is not a coordinate of `X ⊂ A^7`; it is only the localisation variable for `D(x3)`. Using `n=8` here would be a mistake; the producer does not make it.

All seven maximal minors are formed (`D1..D7`, dropping each of the seven columns in turn) and tested by `reduce(det6_k,GE)==0`. Both lanes report `all_6x6_minors_zero=1`, so `rank J ≤ 5` on `B`.

The displayed `5×5` is a genuine minor of that `6×7` matrix. In code, `Jy` is `J` with the `w`-column deleted, then `M5` takes `Jy`-rows `{1,2,4,5,6}` and `Jy`-columns `{2,3,4,5,6}`, i.e. source rows `(e1,e3,e7,e2,e4)` and ambient columns `(d2,d4,x1,x3,x5)`. That is the minor of `J` obtained by deleting row `e5` and columns `w` and `c`. Both lanes report

```text
rank5_minor_identity=1
rank5_minor_normal_form=1024/1594323*x3^6
```

matching the frozen expected value `(1024/1594323)*x3^6`.

Wording nit, not an identity error: the report says this minor is obtained by “dropping source row `e5` and coefficient column `c`”. From a `6×7` matrix that phrase leaves a `5×6` block; the missing words are that the `w`-column is deleted as well (equivalently: the minor of `Jy` dropping row `e5` and column `c`). The matrix that is actually computed is still a `5`-minor of `J`, and a nonzero `5`-minor plus vanishing `6`-minors is exactly rank five.

On `D(x3)` this value is a unit in characteristic zero: `1024=2^{10}`, `1594323=3^{13}`, and `x3^6` is invertible. The only primes that could kill the coefficient are `2` and `3`; the ring is `R=0`. Geometric points of a `Q`-scheme have characteristic-zero residue fields, so the minor remains a unit after any residue-field extension. Rank cannot drop on `B`. Hence `rank J = 5` at every geometric point of `B`.

## 3. Tangent statement — CONFIRMED

The cylinder parametrisation `(w,a) ↦ (c,d2,d4,x1,x3,x5) = (a^{-1},0,0,a,a,0)` has `a`-derivative `(-a^{-2},0,0,1,1,0)`. V3 checks the equivalent linear combination

```text
kyentry = -ib^2 * Jy[k,1] + Jy[k,4] + Jy[k,5]
```

and both lanes report `a_kernel_zero=1`. On `B` one has `ib=a^{-1}`, so `-ib^2=-a^{-2}`. Combined with `Fw_zero=1`, both displayed directions lie in `ker J`. Kernel dimension is `7-5=2`, and the two vectors are independent (`δw=1,δx3=0` versus `δw=0,δx3=1`), so they are the full tangent space. Both have `δx5=0`.

The predecessor test `rank(J_y)=rank([J_y|F_w])=5` is tautological once `F_w=0`, and does not exhibit a first-order motion off `{x5=0}`. The report is right to retract that interpretation. First-order vanishing of `x5` is not the exclusion; the local-ring isomorphism in §3 of the producer is.

## 4. Dimension and embedding dimension — CONFIRMED

Read “geometric point `q ∈ B`” as a `K`-point with `K` algebraically closed of characteristic zero, equivalently a closed point of `B_K`. That is the only reading compatible with `embdim = 7-rank(J)`. (At the generic point of `B` one would have `dim O_(B,η)=0`; the Jacobian formula is not being applied there.)

`B ≅ A^1_w × G_{m,a}` over `Q`, hence geometrically integral, smooth, and of dimension two. For any such `q`, `dim O_(B,q)=2`. Closed immersion `B ⊂ X` on `D(x3)` gives a surjection `O_(X,q) → O_(B,q)`, so `dim O_(X,q) ≥ 2`.

The Jacobian criterion in the smooth ambient `A^7` (or its open `D(x3)`) gives

```text
embdim O_(X,q) = 7 - rank J(q) = 2,
```

for the scheme `X=V(I)` defined by the six given generators, reduced or not. Always `dim ≤ embdim` for a Noetherian local ring, so `dim O_(X,q)=2=embdim`.

Attacks requested by the prompt, and why they fail:

- **Localisation.** `q` lies on `D(x3)`, so `O_(X,q) ≅ O_(X∩D(x3),q)`. The extra equation `ib*x3-1` in `A^8` raises both `n` and `rank` by one (`∂/∂ib` of the source rows is zero, while `x3(q)≠0`), and again yields `embdim=8-6=2`. Same local ring.
- **Residue-field extension.** The minor is a unit in every characteristic-zero field. Rank remains five on `X_K`.
- **Nonreduced structure.** The Jacobian computes the cotangent space of the possibly nonreduced scheme `Spec A/I`. Equality `dim=embdim` forces regularity, hence reducedness at `q`. Nilpotents are not an extra hypothesis; they are excluded by the equality.
- **Embedded components.** A regular local ring is a domain, so `Spec O_(X,q)` is irreducible and has no embedded associated prime.

## 5. Regular local domain — CONFIRMED

`O_(X,q)` is Noetherian (localisation of a finitely generated `Q`-algebra). A Noetherian local ring with `dim=embdim` is regular. A regular local ring is an integral domain. Both steps are standard; the producer uses them correctly. Over characteristic zero, finite type over a field, regularity at geometric points is geometric regularity / smoothness, which matches the Jacobian rank already computed.

## 6. Equal-dimension quotient — CONFIRMED

The closed immersion induces a surjection `O_(X,q) → O_(B,q)` whose kernel `K` is the ideal of `B` in `O_(X,q)`. Both rings have dimension two.

If `K≠0`, then `K` is a proper nonzero ideal of a two-dimensional regular local domain. Regular local rings are domains, Cohen–Macaulay, and catenary. Any nonzero element `f∈K` is a nonzerodivisor of height one (Krull’s principal ideal theorem, using that `(0)` is prime), so `dim O_(X,q)/(f)=1`, hence `dim O_(X,q)/K ≤ 1`. This contradicts `dim O_(B,q)=2`. Therefore `K=0`.

Hypotheses that must be named, and that hold here:

- **Height.** Nonzero ideals in a domain have height at least one. Stated by the producer.
- **Catenarity / CM.** Needed to turn positive height into a dimension drop. Regular local rings supply this; the producer does not print the words “catenary” or “Cohen–Macaulay”. That is expository, not a missing geometric hypothesis.
- **Residue field.** The isomorphism is of local rings with the same residue field as `q`. No extra residue-field condition appears. The Jacobian unit already survives every characteristic-zero extension, so one may equally work with closed points of `X` or of `X_{\overline Q}`.
- **Finite type over a field.** Used implicitly; it is the setting.

The preregistration’s weaker sentence (“a nonzero ideal in a Noetherian local domain lowers dimension”) is not true for arbitrary Noetherian local domains. The producer’s actual sentence uses a *regular* local domain of dimension two, which is sufficient. I do not charge the preregistration wording against the theorem.

## 7. Closure conclusion — CONFIRMED

`K=0` means the ideal sheaf of `B` in `X` vanishes at `q`. A quasi-coherent ideal sheaf that vanishes at `q` vanishes on a Zariski neighbourhood `U` of `q` in `X`. In particular `x5=0` as a section of `O_X` on `U`, so `X∩U = B∩U` as schemes, and `(X ∩ D(x5)) ∩ U = ∅`. Hence

```text
q ∉ closure_X(X ∩ D(x5)).
```

The closure is taken *inside* `X`, which is the correct landing statement. The inclusion `X ∩ D(w*x5*(x3-2*x5)) ⊂ X ∩ D(x5)` preserves the non-membership, so no finite point of `B` is a landing point of the selected open.

Directions: the argument is that a neighbourhood of `q` in `X` lies in `{x5=0}`, not merely that `δx5=0` on the tangent space. It does not assert that `B` is a global irreducible component of `X` on all of `D(x3)`: extra components of `X` disjoint from `B` are not excluded, and need not be. Any component of `X` whose closure contains `q` is visible in `O_(X,q)`, which is a domain equal to `O_(B,q)`, so no other branch through `q` exists, Zariski or formally (the completion of a regular local ring is a domain, and `x5=0` there).

A trajectory leaf *contained in* `B` is a different object; it is not a limit of `D(x5)`. The producer does not claim otherwise.

## 8. Custody / software — CONFIRMED

Accepted lanes are V3 only, two independent engine/order implementations, diagnostic-free, one PASS marker each, hashes agreeing across producer, `run.meta`, `replay.py`, and `MANIFEST.sha256`.

| Lane | engine/order | host | wall | max RSS | input SHA-256 | stdout SHA-256 |
|---|---|---|---|---|---|---|
| Box02 | `std` / `dp` | `ip-172-30-0-186` | 6.83 s | 33148 KiB | `c089ea4f4800716578c73ff8f9fbd78a6bd5a59297bbdf34b11f0620fe6ee76a` | `0b12669b9faa754325966a0ed9d07b6ae0b0365db361455d0dea2728bfc76b69` |
| Box03 | `slimgb` / `block` | `ip-172-30-0-249` | 11.42 s | 34364 KiB | `e7a647537e4d065bebde46ccedd15a761071b8ae6914725e71583ab92b9c30d7` | `2ccb5db3d8cde38dcb959996e4c2fe7713763895c199d015dae9f0b06c6ed1b8` |

Both `runner.rc` are `0`; both `run.meta` contain `rc=0`; both `generator.stderr` are empty (`e3b0c442…`); both `stderr` files are `/usr/bin/time -v` logs with `Exit status: 0` and no banned diagnostic. Each stdout contains `Q8_W0_X5_CYLINDER_LOCAL_GERM_PASS` once, together with every replay marker, including `e6_normal_form=-4/81*x3^3` (i.e. `-4 a^3/81`) and `e8_normal_form=0`. Cylinder bases differ in Gröbner order and both exhibit `x5`, `x1-x3`, `d4`, `d2`, `c-ib`, `x3*ib-1`.

Replay (Box02, `rc=0`) prints `Q8_W0_X5_CYLINDER_LOCAL_GERM_V3_REPLAY_PASS` once; stdout SHA-256 `ecad27d9b47d66eafdb9edbc9b32be635c0493dd58eb3b5eda43835dd3782208` matches the producer and the manifest. It checks both lane hashes, both input hashes, unique markers, every listed source pin, cylinder generators, zero runner codes, and absence of `redefining` / `not defined` / `error occurred` / `segmentation fault` / `killed` / `timed out` on stdout and stderr.

Pinned transitive sources appear in both V3 `source.sha256` files and in `generate.py`:

- compiler `22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545`
- `order3_fibre.py` `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf`

V1/V2 remain negative software controls, not acceptance endpoints. V1’s two construction defects are visible in `generate.py`: unparenthesised `1024*x3^6/1594323`, and `Jy*ky` matrix product. V2 repairs both and then redeclares `poly kyentry` inside the loop, which is the `redefining` diagnostic. V3 hoists that declaration; the polynomial checks are unchanged from V2. No V1/V2 AWS trees are treated as evidence.

Custody nits, not mathematical defects: this referee did not re-hash bytes; independence is engine/order/host, not independently authored generators; `run_v3_remote.sh` does not itself assert the `e6`/`e8` normal forms (the replay does).

## 9. Firewall — CONFIRMED

The theorem is local on finite `B ⊂ D(x3)`. The producer does not classify `a=0`, `a=∞`, projective coefficient escape, Taylor/terminal reconstruction, `p=0`, other `(9,12)` leaves, maximum twelve, Keller pairs, or JC2. The `e6,e8` normal forms are explicitly quarantined as successor input.

§3 already concludes that the selected open cannot land on finite `B`, using only the germ identity and `D(w*x5*(x3-2*x5)) ⊂ D(x5)`. §5’s “combined with separately exact …” sentence is landscape narrative: it names the remaining finite gate `x3=x5=0, e6=0` and coefficient/projective infinity, and it does not claim their exclusion. That is what the prompt permits the last paragraph to do. I reject any reading that this report excludes the unloaded overlap or infinity.

---

## Issues and smallest exact repairs

None of the following is load-bearing. No producer edit is required for the theorem to stand.

1. **`5×5` provenance wording.** Repair: say “the `5×5` minor of `J` on rows `(e1,e3,e7,e2,e4)` and columns `(d2,d4,x1,x3,x5)`”, or “the `5×5` minor of `Jy` obtained by dropping row `e5` and column `c`”. The value and the rank inference are already correct.
2. **Named commutative-algebra lemmas.** Repair: cite that a Noetherian local ring with `dim=embdim` is regular, that regular local rings are domains, and that they are Cohen–Macaulay/catenary, so a nonzero ideal in a two-dimensional regular local ring has height at least one and quotient dimension at most one. These are theorems, not extra geometric hypotheses.
3. **§5 composition sentence.** Repair: keep the remaining-gate list; do not phrase the selected-open non-landing of `B` as depending on the separate `A=0` and loaded-overlap facts. §3 already has the selected-open conclusion.

## Survival

The source-local exclusion of the finite `a≠0` cylinder survives: no geometric point of `B` on `D(x3)` lies in `closure_X(X ∩ D(x5))`, and therefore none is a landing point of `D(w*x5*(x3-2*x5))`.

CONFIRMED
