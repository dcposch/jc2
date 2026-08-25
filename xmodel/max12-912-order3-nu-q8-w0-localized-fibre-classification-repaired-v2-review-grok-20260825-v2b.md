I'll audit the V2 successor from source and the named V1 pins, without Bash, CAS, or network. First I need the report, preregistration, and the hash-pinned artifacts.I'll locate the V2 report, V1 pins, case directory, and named sources next.I have the case tree. Next I’ll read the V2 report, V1 report/review, and preregistration in full.V2 prose is in. Next I’ll read the generators, runners, manifests, and the V1 source they claim to repair.Manifest pins match the report hashes. I’ll now read every named AWS artifact, the V1 report, and the parent freeze.I’ll inspect every AWS lane next: inputs, metas, sources, and both factor-parser versions.# Hostile review: localized `w=0` fibre classification, repaired V2

**Reviewer.** Grok 4.6 (required different-model referee; same referee as V1). Producer is GPT-family.  
**Target.** `xmodel/max12-912-order3-nu-q8-w0-localized-fibre-classification-repaired-v2-20260825.md` and case `cases/max12_912_order3_nu_q8_w0_localized_fibre_classification_repaired_v2_aws_20260825/`.  
**Limitation.** This session used no Bash, no CAS, no network, and wrote/edited no case or report file. SHA-256 values were compared as hex strings already present in the named files; they were not recomputed from bytes. The degree-eight modular exponentiation in the Rabin search was audited as an algorithm, not re-executed.

---

## 1. Charge, parent identity, and scope

The charged statement is unchanged from the V1 theorem: only the finite affine chart

```text
p=1, k=mu=0, w=0, x5 != 0, x3-2*x5 != 0
```

of the six divided approximate-cubic rows, with scheme

```text
Y0 ≅ Spec(Q[v]/(Q8)),
```

plus the already-reviewed `r6`-unit, relative-Jacobian-unit, squarefreeness, and emptiness of unloaded and loaded non-Q8 points. V2 is a nonmutating wording/custody successor. It does **not** land a horizontal branch, close a source boundary, escape projectively in `c,d2,d4,x1,x3,x5`, impose terminal `r8` or either true-centre Taylor family, treat `p=0`, other `(9,12)` leaves, maximum twelve, a Keller pair, or JC2.

Named parent pins match as strings: V1 report `bb09d7dd…`, V1 Grok review `fa649cd0…` (verdict `CONFIRMED_WITH_REPAIRS`), V1 case manifest `b6c455ab…` equal to the V1 freeze payload, V1 generate `90b13704…`, compiler `22b0cdc4…`, `order3_fibre.py` `a4fdac5d…`, descent replay `5dcb0a67…`. The last two are exactly the constants inside `quotient_compiler.load_parent()`. V1 source bytes still display the frozen producer status; they were not rewritten to absorb this review.

Firewall in V2 §§1 and 5 is exact and remains charged.

---

## 2. Repair 1 — loaded Q8-singular citation

V1 `q8_singular` input is literally

```text
I = e1,e3,e5,e7,e2,e4,ev,einv, inu*e6-1, eq8, detJ.
```

V2 §4 now cites `(Ibase, inu*e6-1, Q8, detJ)` and licenses adding or deleting the inverse only from the reviewed unit `(Ibase,e6)=(1)`. That is the correct scheme-theoretic reason: `e6` is already a unit on `Y0`, so the graph of `inu` does not change the closed subscheme of `Y0`. The remaining generator mismatch is only the documented associate `eq8 = -Q8`. The V1 defect (omitting `inu*e6-1`) is discharged.

---

## 3. Repair 2 — irreducibility

**Primitivity / Gauss.** Displayed `Q8` has content 1 (hand gcd: `gcd(999,1539)=9`, then `gcd(9,7320)=3`, then `296` is not divisible by 3). Leading coefficient `999=3^3·37` is nonzero in `F7`, so degree is preserved. An irreducible same-degree reduction therefore implies irreducibility over `Q`.

**Reduction.** Integer coefficients modulo 7, then times the inverse of `5`, yield the unique monic

```text
q = v^8+4v^7+2v^6+v^5+6v^4+2v^3+4v^2+v+5 ∈ F7[v],
```

agreeing with the search JSON `monic_q8_ascending = [5,1,4,2,6,1,2,4,1]`, the factor generator, and the frozen `input.sing`.

**Rabin.** For `n=8` the only prime divisor is `2`. The stdlib script makes `q` monic, then requires `v^{7^8}≡v (mod q)` and `gcd(q,v^{7^4}-v)=1`. That is the degree-eight criterion. AWS stdout reports `gcd=[1]`, remainder `[0]`, `least_good_prime=7`, `tested_primes=2` (so `p=5` failed, as preregistered `p≥5`), one PASS marker, `rc=0`. Exponentiation was not recomputed here.

**Singular parser.** Valid V2 script never assigns `intvec`. It gates `factor_count=1`, `degree_sum=8`, `degree8_count=1`, and mutual principal-ideal divisibility. Output is one degree-eight factor; the printed polynomial `v^8-3v^7+…-2` is `q` with representatives in `{-3,…,4}` (`-3≡4`, `-1≡6`, `-2≡5`). Mutual divisibility is therefore the associate check, and multiplicity is redundant for a degree-eight polynomial. Failed V1 `intvec M=L[2]` stdout contains `is not supported` / `error occurred` and **no** PASS marker; `replay.py` asserts both. It is not an acceptance endpoint. Residual `factor_count=1` after the crash is garbage and is not consumed.

---

## 4. Repair 3 — characteristic-zero `V(e8)` / `D(e8)`

All four lanes are the V1 generator at `prime=0`, modes `nonq8_rho0` and `nonq8_rho_loaded`:

| lane | ring extras | engine/order | ideal |
|---|---|---|---|
| Box02 `rho0` | `inu,iq`, block `std` | `Ibase + inu*e6-1 + iq*eq8-1 + e8` |
| Box02 `rho_loaded` | `inu,iq,irho`, block `std` | `Ibase + inu*e6-1 + iq*eq8-1 + irho*e8-1` |
| Box03 `rho0` | `inu,iq`, `slimgb`/`dp` | same as Box02 `rho0` |
| Box03 `rho_loaded` | `inu,iq,irho`, `slimgb`/`dp` | same as Box02 `rho_loaded` |

Source rows `e1,e3,e5,e7,e2,e4,e6,e8,ev,einv,eq8` are character-identical to frozen V1 `q8_singular` / `nonq8` inputs. Inverses are fresh equations, not saturations. Jacobian is the same unused 8×8 in `(c,d2,d4,x1,x3,x5,inv,v)`. Every stdout is exactly the ten-line unit-ideal block: one `Q8_W0_FIBRE_STRATUM_PASS`, `original_remainder_zero=1`, `dim=-1`, `size=1`, `vdim=0`. In Singular that is `I=(1)`. Remainder-zero plus `dim=-1` is the unit-ideal certificate, and it is consistent with the reviewed parent `nonq8=(1)`.

The stratum wrapper gates only PASS and remainder-zero, **not** `dim=-1`. Emptiness is enforced by `replay.py`, not by `run_v2_remote.sh`.

---

## 5. Repairs 4–6 — shape, transitive pins, sign

V2 §4 correctly narrows the Box02 `q8` shape basis to an optional coordinate reconstruction and restates the V1 linear-algebra isomorphism `ker(Q[v]→A)=(Q8)` with `dim_Q A=8`. That argument never needed the printed basis.

Every new non-Q8 `source.sha256` / `run.meta` contains `a4fdac5d…` and `5dcb0a67…`. The octic-only factor lane pins `generate_factor7_v2.py` and does not pin those fibre sources. The Rabin scan uses the shared stratum runner, so it *also* records the fibre hashes, but its mathematics is only the hardcoded integer octic.

Displayed `Q8` has leading `+999`; generator `eq8` is the associate `-Q8`. Kernels and gcds are unaffected.

---

## 6. Manifest, wrappers, replay

Decisive stdout hex strings in the report, `MANIFEST.sha256`, `run.meta`, and `replay.py` agree:

```text
Rabin     eb389979…
factor v2 8a05b14f…
Box02 V   85cbc6c6…
Box02 D   85a00523…
Box03 V   00625142…
Box03 D   197c6d52…
replay    b9a22080…
```

Valid replay stdout is exactly one `Q8_W0_LOCALIZED_FIBRE_REPAIRED_V2_REPLAY_PASS`, `rc=0`, `runner.rc=0`, stderr is `/usr/bin/time -v` with exit 0. The V2 wrapper hashes itself and uses `grep`.

Replay v1 already produced that same stdout digest. Box02 had successfully invoked `rg` on earlier V2 lanes, so the claim that v1 failed because `rg` was unavailable is **not evidenced** in the retained files (post-python wrapper stderr is not captured). V1 replay is also absent from `MANIFEST.sha256`. The V2 grep wrapper remains the named acceptance endpoint.

Further custody nits, all repairable: `run_v2_remote.sh` is pinned in `PREREGISTRATION.manifest.sha256` and in `run.meta` (`0894e6ab…`) but is not a first-class V2 MANIFEST row; factor `source.sha256` / `runner.rc` are omitted; factor v1 records Singular `rc=0` despite diagnostics on stdout; `generate_factor7_v2.py` hardcodes `q` rather than reducing `Q8`; the valid factor runner still depends on `rg`; `generate.py` still prints PASS unconditionally.

---

## 7. Defects

1. **Source-fidelity, minor.** Loaded singular ideal is cited with `Q8` rather than the computed generator `eq8`. Ideals coincide; the inverse is now present.
2. **Wrapper gating.** Characteristic-zero emptiness is not fail-closed in `run_v2_remote.sh`; only replay checks `dim=-1` and `size=1`.
3. **Custody holes.** Replay-v1 artifacts, factor-lane `source.sha256`, and the live stratum runner are not first-class V2 MANIFEST rows. The “unavailable `rg`” negative-control story is unsupported on Box02.
4. **Process.** Factor `q` is copied, not derived, from the integer octic (hand-checked).
5. **Reviewer-side.** Bytes were not rehashed; `v^{7^8} mod q` was not recomputed.

No mathematical hole was found in the six requested repairs, the scheme isomorphism inherited from V1, or the stated affine scope.

CONFIRMED_WITH_REPAIRS
