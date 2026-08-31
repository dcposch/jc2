# SEMANTIC-REPLAY/v1 — replay-integrity CI gate

## 1. Scope and input integrity

This report proposes an additive replay-certificate schema and an apply-ready,
pure-standard-library checker patch.  It does not integrate the checker with a
CI runner and does not alter any existing artifact convention or tool.

Before reading the charged inputs, I recomputed SHA-256 over the three frozen
copies.  All three matched the supplied values exactly:

```text
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  inputs/ideation-20260831T1033Z-synthesis.md
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  inputs/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  inputs/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
```

Here and below, `inputs/…` abbreviates the frozen directory
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.NdLXLC/inputs/`.

## 2. Findings from the charged artifacts

The controlling contract is
`inputs/ideation-20260831T1033Z-synthesis.md:115-123`.  In particular, lines
118-123 require the declaration per promoted claim and name the two acceptance
artifacts.

### 2.1 Quarantined reducible ledger: negative control

The ledger is itself labelled "not a review and not a promotion"
(`block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md:3-5`),
but the synthesis explicitly selects its finite replay as the negative systems
fixture.  Its finite claim is the complete incidence-tree/inertia enumeration,
not a finite enumeration of the unbounded `n22` families: see lines 64-66,
114-130, and 204-213.  The latter passage reports 16 rows, four unconditional
kills, and twelve rows live without the open missing-multiplicity identity.

The replay passage at lines 231-250 names a script, three mutation switches, a
baseline stdout hash, a payload hash, and the fact that every mutation exits
nonzero.  It supplies no `SEMANTIC-REPLAY/v1` declaration, no per-claim binding,
no accepted or rejected witness record emitted by the named path, and no
mutated claim projection or digest.  Human row labels such as `OPEN`, `S4`, and
`EULER` are not evidence that those rows were driven as replay controls.

Therefore the charged ledger **fails as-is with exit 2 (`MALFORMED`)**.  Missing
mutation evidence is not observed invariance, and assigning it exit 3 would
invent an equality that was never measured.  A structurally valid certificate
whose alleged controls were absent from the generator/path transcript would
instead fail with exit 4 (`FAIL-BYPASS`).

### 2.2 Reviewed conductor census: insufficient certificate evidence

The census contains useful ingredients:

- the sealed arithmetic core (a candidate generator dependency) and its hash at
  `block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md:81-103`;
- the consuming replay path and its hash at lines 275-280;
- the meaning of marked and unmarked rows plus a same-census positive/negative
  pair at lines 219-225: `(6,4,9)*72` is accepted and `(5,4)` is rejected with
  count zero; and
- one whole-stdout hash, one payload hash, and three mutation switch names at
  lines 281-303.

That is not enough to write a compliant certificate from the artifact.  The
missing data are exactly:

1. an executable generator invocation and output protocol; lines 81-103 call
   the hash-pinned file an imported arithmetic core, not a record emitter;
2. a machine transcript binding the two human-readable row entries to records
   emitted by that generator and consumed by the declared production path;
3. a baseline `complete-results/v1` projection and per-claim digest (the
   supplied digest covers the aggregate stdout/payload);
4. a generator mutation bound to the promoted claim which successfully emits
   records for the same controls; and
5. the resulting mutated claim digest.  Lines 294-303 state only that the
   switches exit nonzero.  Elsewhere, lines 167-168 even say the framing
   mutation fails before a new verdict is consumed.  Process failure is not a
   changed claim digest.

There is an additional typing mismatch: the documented switches mutate the
consuming compiler/criterion/promotion replay, whereas the contract calls for
a generator mutation.  The artifact does not declare a mutation of the sealed
delta-sequence generator.

Accordingly, the artifact-derived partial census certificate in the tests
**fails with exit 2 (`MALFORMED`)** and names the absent generator mutation.
This is the contract's explicit insufficient-artifact branch.  Supplying
placeholder digests, treating the whole-stdout hash as a per-claim digest, or
treating a nonzero exit as a mutated claim would manufacture evidence and is
not done.

## 3. Replay-certificate declaration format

The certificate is UTF-8 JSON.  Paths are relative to the certificate.  The
format is additive: an existing artifact may reference this new sidecar; no
existing field is renamed, and the checker does not rewrite artifacts.

```json
{
  "schema": "SEMANTIC-REPLAY/v1",
  "claims": [
    {
      "id": "complete-conductor-census",
      "generator": {
        "id": "delta-sequence-generator",
        "script": "../ops/generate_rows.py",
        "sha256": "<64 lowercase hex>",
        "args": ["--emit-semantic-replay"]
      },
      "production_path": {
        "id": "row-to-braid-to-s4-verdict",
        "script": "../ops/classify_rows.py",
        "sha256": "<64 lowercase hex>",
        "args": ["--consume-semantic-replay"]
      },
      "claim_projection": "complete-results/v1",
      "witnesses": {
        "accepted": {"conductor": 12, "row": [6, 4, 9]},
        "rejected": {"conductor": 12, "row": [5, 4]}
      },
      "mutation": {
        "id": "promote-zero-control",
        "generator_args_append": ["--mutate-generated-zero-row"],
        "claim_sha256": "<64 lowercase hex>"
      },
      "baseline_claim_sha256": "<64 lowercase hex>"
    }
  ]
}
```

The two scripts use a deliberately small JSON protocol.  A normal or mutated
generator run emits:

```json
{
  "protocol": "SEMANTIC-REPLAY/v1/generator",
  "generator_id": "delta-sequence-generator",
  "records": [
    {"witness": {"conductor": 12, "row": [5, 4]}, "data": {"count": 0}}
  ]
}
```

The gate canonically passes only the protocol, generator identifier, and exact
`{witness,data}` records to the hash-pinned production path on standard input;
generator diagnostics and mutation context are not exposed to that path.  The
path emits:

```json
{
  "protocol": "SEMANTIC-REPLAY/v1/path",
  "path_id": "row-to-braid-to-s4-verdict",
  "claim_id": "complete-conductor-census",
  "results": [
    {
      "witness": {"conductor": 12, "row": [5, 4]},
      "decision": "reject",
      "source_record_sha256": "<SHA-256 of the exact generator record>",
      "claim_fragment": {"labelled_full_s4_count": 0}
    }
  ]
}
```

For each run the checker requires a one-to-one equality, by canonical witness
object, between generator records and path results, and requires every result
to carry the SHA-256 of its complete canonical `{witness,data}` source record.
Unknown, duplicate, omitted, or record-substituted witnesses are bypasses.  On
the baseline run it also requires the two declared controls to occur with
opposite declared decisions.  On the mutant run both control identities must
still be generated and reach the same path; their decisions may change.

`complete-results/v1` is the canonical object

```text
{"claim_id": ID, "projection": "complete-results/v1", "results": RESULTS}
```

where `RESULTS` contains every `{witness, decision, claim_fragment}` sorted by
the canonical witness bytes.  Canonical JSON uses sorted keys, no insignificant
whitespace, ASCII escapes, UTF-8, and no floats or non-finite values.  The gate
computes SHA-256 itself, checks the baseline commitment, and requires the live
baseline and mutant digests to differ.  For a non-invariant run it then checks
the mutant commitment.  Hashing the complete result ledger makes the finite
domain, rejected rows, and accepted fragments part of the promoted claim;
reordering alone is inert.

Only generator arguments may change in the metamorphic run.  The production
path, its arguments, and its file hash remain fixed.  Each entrypoint hash is
rechecked immediately before every invocation, including between generator and
path runs.  Both are invoked as argument arrays with the running Python
interpreter (`shell=False`), with bytecode disabled and a 60-second per-process
timeout.  The gate itself uses no network service or CAS.

Exit classification is deterministic:

| exit | status | meaning |
|---:|---|---|
| 0 | `PASS` | every claim has bound controls and distinct committed live digests |
| 2 | `MALFORMED` | unreadable/invalid JSON or a missing/ill-typed declaration |
| 3 | `FAIL-INVARIANCE` | otherwise valid baseline and mutant projections have the same digest |
| 4 | `FAIL-BYPASS` | hash, execution, protocol, record binding, witness, or non-invariant digest-commitment provenance fails |

The checker validates the entire static schema before executing anything.  It
requires valid provenance for both live projections, then reports equal live
digests as invariance before consulting the mutant's predicted commitment.  A
bypass in any other claim still takes precedence over a recorded invariance.

## 4. Proposed implementation and tests

The following is the single patch to apply.  It adds only the checker and its
unit tests.

```diff
diff --git a/ops/replay_gate.py b/ops/replay_gate.py
new file mode 100755
--- /dev/null
+++ b/ops/replay_gate.py
@@ -0,0 +1,547 @@
+#!/usr/bin/env python3
+
+from __future__ import annotations
+
+import argparse
+import hashlib
+import json
+import os
+import subprocess
+import sys
+from dataclasses import dataclass
+from pathlib import Path
+from typing import Any
+
+
+SCHEMA = "SEMANTIC-REPLAY/v1"
+GENERATOR_PROTOCOL = f"{SCHEMA}/generator"
+PATH_PROTOCOL = f"{SCHEMA}/path"
+PROJECTION = "complete-results/v1"
+TIMEOUT_SECONDS = 60
+MAX_OUTPUT_BYTES = 8 * 1024 * 1024
+
+
+class GateFailure(Exception):
+    code = 2
+    status = "MALFORMED"
+
+    def __init__(self, reason: str, claim_id: str | None = None) -> None:
+        super().__init__(reason)
+        self.claim_id = claim_id
+
+
+class Malformed(GateFailure):
+    pass
+
+
+class Bypass(GateFailure):
+    code = 4
+    status = "FAIL-BYPASS"
+
+
+@dataclass(frozen=True)
+class EntryPoint:
+    id: str
+    script: Path
+    sha256: str
+    args: tuple[str, ...]
+
+
+@dataclass(frozen=True)
+class ClaimSpec:
+    id: str
+    generator: EntryPoint
+    production_path: EntryPoint
+    accepted: dict[str, Any]
+    rejected: dict[str, Any]
+    mutation_id: str
+    mutation_args: tuple[str, ...]
+    baseline_sha256: str
+    mutated_sha256: str
+
+
+def _reject_constant(token: str) -> None:
+    raise ValueError(f"non-finite number {token!r}")
+
+
+def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
+    value: dict[str, Any] = {}
+    for key, item in pairs:
+        if key in value:
+            raise ValueError(f"duplicate JSON key {key!r}")
+        value[key] = item
+    return value
+
+
+def _loads(text: str, label: str, failure: type[GateFailure]) -> Any:
+    try:
+        value = json.loads(
+            text,
+            object_pairs_hook=_unique_object,
+            parse_constant=_reject_constant,
+        )
+        _check_json_value(value, label, failure)
+    except RecursionError as exc:
+        raise failure(f"{label}: nesting too deep") from exc
+    except (json.JSONDecodeError, ValueError) as exc:
+        raise failure(f"{label}: invalid JSON: {exc}") from exc
+    return value
+
+
+def _check_json_value(
+    value: Any,
+    label: str,
+    failure: type[GateFailure],
+) -> None:
+    if value is None or isinstance(value, (bool, int)):
+        return
+    if isinstance(value, str):
+        try:
+            value.encode("utf-8", errors="strict")
+        except UnicodeError as exc:
+            raise failure(f"{label}: string is not Unicode scalar text") from exc
+        return
+    if isinstance(value, float):
+        raise failure(f"{label}: floating-point values are not canonical")
+    if isinstance(value, list):
+        for index, item in enumerate(value):
+            _check_json_value(item, f"{label}[{index}]", failure)
+        return
+    if isinstance(value, dict):
+        for key, item in value.items():
+            if not isinstance(key, str):
+                raise failure(f"{label}: object key is not a string")
+            _check_json_value(key, f"{label}: object key", failure)
+            _check_json_value(item, f"{label}.{key}", failure)
+        return
+    raise failure(f"{label}: unsupported JSON value {type(value).__name__}")
+
+
+def _canonical(value: Any) -> bytes:
+    return json.dumps(
+        value,
+        sort_keys=True,
+        separators=(",", ":"),
+        ensure_ascii=True,
+        allow_nan=False,
+    ).encode("utf-8")
+
+
+def _mapping(value: Any, label: str) -> dict[str, Any]:
+    if not isinstance(value, dict):
+        raise Malformed(f"{label}: expected object")
+    return value
+
+
+def _field(mapping: dict[str, Any], key: str, label: str) -> Any:
+    if key not in mapping:
+        raise Malformed(f"{label}: missing {key}")
+    return mapping[key]
+
+
+def _string(mapping: dict[str, Any], key: str, label: str) -> str:
+    value = _field(mapping, key, label)
+    if not isinstance(value, str) or not value or "\0" in value:
+        raise Malformed(f"{label}.{key}: expected nonempty string")
+    return value
+
+
+def _digest(mapping: dict[str, Any], key: str, label: str) -> str:
+    value = _string(mapping, key, label)
+    if len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
+        raise Malformed(f"{label}.{key}: expected 64 lowercase hex characters")
+    return value
+
+
+def _arguments(mapping: dict[str, Any], key: str, label: str) -> tuple[str, ...]:
+    value = _field(mapping, key, label)
+    if not isinstance(value, list):
+        raise Malformed(f"{label}.{key}: expected array")
+    if any(not isinstance(item, str) or "\0" in item for item in value):
+        raise Malformed(f"{label}.{key}: every argument must be a string")
+    return tuple(value)
+
+
+def _entry_point(
+    value: Any,
+    label: str,
+    certificate_dir: Path,
+) -> EntryPoint:
+    mapping = _mapping(value, label)
+    entry_id = _string(mapping, "id", label)
+    script_text = _string(mapping, "script", label)
+    script_relative = Path(script_text)
+    if script_relative.is_absolute():
+        raise Malformed(f"{label}.script: expected a relative path")
+    try:
+        script = (certificate_dir / script_relative).resolve()
+    except OSError as exc:
+        raise Malformed(f"{label}.script: cannot resolve path: {exc}") from exc
+    return EntryPoint(
+        id=entry_id,
+        script=script,
+        sha256=_digest(mapping, "sha256", label),
+        args=_arguments(mapping, "args", label),
+    )
+
+
+def _claim(
+    value: Any,
+    index: int,
+    certificate_dir: Path,
+) -> ClaimSpec:
+    label = f"claims[{index}]"
+    mapping = _mapping(value, label)
+    claim_id = _string(mapping, "id", label)
+    generator = _entry_point(
+        _field(mapping, "generator", label),
+        f"{label}.generator",
+        certificate_dir,
+    )
+    production_path = _entry_point(
+        _field(mapping, "production_path", label),
+        f"{label}.production_path",
+        certificate_dir,
+    )
+    projection = _string(mapping, "claim_projection", label)
+    if projection != PROJECTION:
+        raise Malformed(f"{label}.claim_projection: expected {PROJECTION!r}")
+
+    witnesses = _mapping(_field(mapping, "witnesses", label), f"{label}.witnesses")
+    accepted = _mapping(
+        _field(witnesses, "accepted", f"{label}.witnesses"),
+        f"{label}.witnesses.accepted",
+    )
+    rejected = _mapping(
+        _field(witnesses, "rejected", f"{label}.witnesses"),
+        f"{label}.witnesses.rejected",
+    )
+    if _canonical(accepted) == _canonical(rejected):
+        raise Malformed(f"{label}.witnesses: controls must be distinct")
+
+    mutation = _mapping(_field(mapping, "mutation", label), f"{label}.mutation")
+    mutation_id = _string(mutation, "id", f"{label}.mutation")
+    mutation_args = _arguments(
+        mutation,
+        "generator_args_append",
+        f"{label}.mutation",
+    )
+    if not mutation_args:
+        raise Malformed(
+            f"{label}.mutation.generator_args_append: expected a nonempty array"
+        )
+
+    return ClaimSpec(
+        id=claim_id,
+        generator=generator,
+        production_path=production_path,
+        accepted=accepted,
+        rejected=rejected,
+        mutation_id=mutation_id,
+        mutation_args=mutation_args,
+        baseline_sha256=_digest(mapping, "baseline_claim_sha256", label),
+        mutated_sha256=_digest(mutation, "claim_sha256", f"{label}.mutation"),
+    )
+
+
+def _certificate(path: Path) -> list[ClaimSpec]:
+    try:
+        text = path.read_text(encoding="utf-8")
+    except (OSError, UnicodeError) as exc:
+        raise Malformed(f"certificate: cannot read UTF-8 file: {exc}") from exc
+    root = _mapping(_loads(text, "certificate", Malformed), "certificate")
+    if _string(root, "schema", "certificate") != SCHEMA:
+        raise Malformed(f"certificate.schema: expected {SCHEMA!r}")
+    claims_value = _field(root, "claims", "certificate")
+    if not isinstance(claims_value, list) or not claims_value:
+        raise Malformed("certificate.claims: expected nonempty array")
+    claims = [
+        _claim(value, index, path.resolve().parent)
+        for index, value in enumerate(claims_value)
+    ]
+    identifiers = [claim.id for claim in claims]
+    if len(set(identifiers)) != len(identifiers):
+        raise Malformed("certificate.claims: duplicate claim id")
+    return claims
+
+
+def _file_sha256(entry: EntryPoint, claim_id: str, role: str) -> str:
+    try:
+        if not entry.script.is_file():
+            raise OSError("not a regular file")
+        actual = hashlib.sha256(entry.script.read_bytes()).hexdigest()
+    except OSError as exc:
+        raise Bypass(
+            f"{role} {entry.script}: cannot read: {exc}",
+            claim_id,
+        ) from exc
+    if actual != entry.sha256:
+        raise Bypass(
+            f"{role} {entry.id}: SHA-256 mismatch",
+            claim_id,
+        )
+    return actual
+
+
+def _run(
+    entry: EntryPoint,
+    args: tuple[str, ...],
+    stdin: str | None,
+    certificate_dir: Path,
+    claim: ClaimSpec,
+    phase: str,
+) -> dict[str, Any]:
+    _file_sha256(entry, claim.id, phase)
+    environment = os.environ.copy()
+    for name in tuple(environment):
+        if name.startswith("SEMANTIC_REPLAY_"):
+            environment.pop(name)
+    environment["PYTHONDONTWRITEBYTECODE"] = "1"
+    environment["PYTHONHASHSEED"] = "0"
+    environment["SEMANTIC_REPLAY_CLAIM_ID"] = claim.id
+    environment["SEMANTIC_REPLAY_GENERATOR_ID"] = claim.generator.id
+    environment["SEMANTIC_REPLAY_PATH_ID"] = claim.production_path.id
+    command = [sys.executable, "-B", str(entry.script), *args]
+    try:
+        process = subprocess.run(
+            command,
+            check=False,
+            cwd=certificate_dir,
+            env=environment,
+            input=stdin,
+            capture_output=True,
+            text=True,
+            encoding="utf-8",
+            errors="strict",
+            timeout=TIMEOUT_SECONDS,
+        )
+    except subprocess.TimeoutExpired as exc:
+        raise Bypass(f"{phase}: timed out", claim.id) from exc
+    except (OSError, UnicodeError) as exc:
+        raise Bypass(f"{phase}: execution failed: {exc}", claim.id) from exc
+    if process.returncode != 0:
+        raise Bypass(f"{phase}: exited {process.returncode}", claim.id)
+    if len(process.stdout.encode("utf-8")) > MAX_OUTPUT_BYTES:
+        raise Bypass(f"{phase}: stdout exceeds {MAX_OUTPUT_BYTES} bytes", claim.id)
+    value = _loads(process.stdout, f"{phase} stdout", Bypass)
+    if not isinstance(value, dict):
+        raise Bypass(f"{phase} stdout: expected JSON object", claim.id)
+    return value
+
+
+def _generator_records(
+    output: dict[str, Any],
+    claim: ClaimSpec,
+    phase: str,
+) -> dict[bytes, dict[str, Any]]:
+    if output.get("protocol") != GENERATOR_PROTOCOL:
+        raise Bypass(f"{phase}: wrong generator protocol", claim.id)
+    if output.get("generator_id") != claim.generator.id:
+        raise Bypass(f"{phase}: wrong generator id", claim.id)
+    records = output.get("records")
+    if not isinstance(records, list):
+        raise Bypass(f"{phase}: records must be an array", claim.id)
+    indexed: dict[bytes, dict[str, Any]] = {}
+    for index, record_value in enumerate(records):
+        if not isinstance(record_value, dict):
+            raise Bypass(f"{phase}: record {index} is not an object", claim.id)
+        witness = record_value.get("witness")
+        if not isinstance(witness, dict) or "data" not in record_value:
+            raise Bypass(
+                f"{phase}: record {index} needs object witness and data",
+                claim.id,
+            )
+        key = _canonical(witness)
+        if key in indexed:
+            raise Bypass(f"{phase}: duplicate generated witness", claim.id)
+        indexed[key] = {"witness": witness, "data": record_value["data"]}
+    return indexed
+
+
+def _path_results(
+    output: dict[str, Any],
+    claim: ClaimSpec,
+    phase: str,
+) -> dict[bytes, dict[str, Any]]:
+    if output.get("protocol") != PATH_PROTOCOL:
+        raise Bypass(f"{phase}: wrong path protocol", claim.id)
+    if output.get("path_id") != claim.production_path.id:
+        raise Bypass(f"{phase}: wrong production path id", claim.id)
+    if output.get("claim_id") != claim.id:
+        raise Bypass(f"{phase}: wrong claim id", claim.id)
+    results = output.get("results")
+    if not isinstance(results, list):
+        raise Bypass(f"{phase}: results must be an array", claim.id)
+    indexed: dict[bytes, dict[str, Any]] = {}
+    for index, result in enumerate(results):
+        if not isinstance(result, dict):
+            raise Bypass(f"{phase}: result {index} is not an object", claim.id)
+        witness = result.get("witness")
+        decision = result.get("decision")
+        if not isinstance(witness, dict):
+            raise Bypass(f"{phase}: result {index} has no witness object", claim.id)
+        if decision not in ("accept", "reject"):
+            raise Bypass(f"{phase}: result {index} has invalid decision", claim.id)
+        if "claim_fragment" not in result:
+            raise Bypass(f"{phase}: result {index} has no claim_fragment", claim.id)
+        source_sha256 = result.get("source_record_sha256")
+        if (
+            not isinstance(source_sha256, str)
+            or len(source_sha256) != 64
+            or any(char not in "0123456789abcdef" for char in source_sha256)
+        ):
+            raise Bypass(f"{phase}: result {index} has invalid source digest", claim.id)
+        key = _canonical(witness)
+        if key in indexed:
+            raise Bypass(f"{phase}: duplicate path witness", claim.id)
+        indexed[key] = result
+    return indexed
+
+
+def _check_bijection(
+    records: dict[bytes, dict[str, Any]],
+    results: dict[bytes, dict[str, Any]],
+    claim: ClaimSpec,
+    phase: str,
+) -> None:
+    if records.keys() != results.keys():
+        missing = len(records.keys() - results.keys())
+        unknown = len(results.keys() - records.keys())
+        raise Bypass(
+            f"{phase}: generator/path witness bijection failed "
+            f"(missing={missing}, unknown={unknown})",
+            claim.id,
+        )
+    for key, record in records.items():
+        expected = hashlib.sha256(_canonical(record)).hexdigest()
+        if results[key]["source_record_sha256"] != expected:
+            raise Bypass(f"{phase}: source record digest mismatch", claim.id)
+
+
+def _check_controls(
+    records: dict[bytes, dict[str, Any]],
+    results: dict[bytes, dict[str, Any]],
+    claim: ClaimSpec,
+    phase: str,
+    baseline: bool,
+) -> None:
+    controls = (
+        (claim.accepted, "accept", "accepted"),
+        (claim.rejected, "reject", "rejected"),
+    )
+    for witness, expected, label in controls:
+        key = _canonical(witness)
+        if key not in records or key not in results:
+            raise Bypass(
+                f"{phase}: declared {label} witness was not produced through path",
+                claim.id,
+            )
+        if baseline and results[key]["decision"] != expected:
+            raise Bypass(
+                f"{phase}: declared {label} witness has wrong decision",
+                claim.id,
+            )
+
+
+def _claim_digest(claim: ClaimSpec, results: dict[bytes, dict[str, Any]]) -> str:
+    normalized = []
+    for key in sorted(results):
+        result = results[key]
+        normalized.append(
+            {
+                "witness": result["witness"],
+                "decision": result["decision"],
+                "claim_fragment": result["claim_fragment"],
+            }
+        )
+    projection = {
+        "claim_id": claim.id,
+        "projection": PROJECTION,
+        "results": normalized,
+    }
+    return hashlib.sha256(_canonical(projection)).hexdigest()
+
+
+def _replay(
+    claim: ClaimSpec,
+    certificate_dir: Path,
+    mutated: bool,
+) -> str:
+    label = "mutated" if mutated else "baseline"
+    generator_args = claim.generator.args
+    if mutated:
+        generator_args += claim.mutation_args
+    generator_output = _run(
+        claim.generator,
+        generator_args,
+        None,
+        certificate_dir,
+        claim,
+        f"{label} generator",
+    )
+    records = _generator_records(generator_output, claim, f"{label} generator")
+    path_input = {
+        "protocol": GENERATOR_PROTOCOL,
+        "generator_id": claim.generator.id,
+        "records": [records[key] for key in sorted(records)],
+    }
+    path_output = _run(
+        claim.production_path,
+        claim.production_path.args,
+        _canonical(path_input).decode("utf-8"),
+        certificate_dir,
+        claim,
+        f"{label} production path",
+    )
+    results = _path_results(path_output, claim, f"{label} production path")
+    _check_bijection(records, results, claim, label)
+    _check_controls(records, results, claim, label, baseline=not mutated)
+    return _claim_digest(claim, results)
+
+
+def check_certificate(path: Path) -> tuple[list[str], list[str]]:
+    claims = _certificate(path)
+    certificate_dir = path.resolve().parent
+    invariant: list[str] = []
+    checked: list[str] = []
+    for claim in claims:
+        baseline = _replay(claim, certificate_dir, mutated=False)
+        if baseline != claim.baseline_sha256:
+            raise Bypass("baseline claim digest misses commitment", claim.id)
+        mutated = _replay(claim, certificate_dir, mutated=True)
+        if mutated == baseline:
+            invariant.append(claim.id)
+        elif mutated != claim.mutated_sha256:
+            raise Bypass("mutated claim digest misses commitment", claim.id)
+        checked.append(claim.id)
+    return checked, invariant
+
+
+def _emit(status: str, **fields: Any) -> None:
+    print(json.dumps({"status": status, **fields}, sort_keys=True))
+
+
+def main(argv: list[str] | None = None) -> int:
+    parser = argparse.ArgumentParser(description="SEMANTIC-REPLAY/v1 gate")
+    subparsers = parser.add_subparsers(dest="command", required=True)
+    check_parser = subparsers.add_parser("check")
+    check_parser.add_argument("certificate", type=Path)
+    arguments = parser.parse_args(argv)
+
+    try:
+        checked, invariant = check_certificate(arguments.certificate)
+    except GateFailure as exc:
+        fields: dict[str, Any] = {"reason": str(exc)}
+        if exc.claim_id is not None:
+            fields["claim_id"] = exc.claim_id
+        _emit(exc.status, **fields)
+        return exc.code
+    if invariant:
+        _emit("FAIL-INVARIANCE", claims=invariant)
+        return 3
+    _emit("PASS", claims=checked)
+    return 0
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
diff --git a/ops/test_replay_gate.py b/ops/test_replay_gate.py
new file mode 100755
--- /dev/null
+++ b/ops/test_replay_gate.py
@@ -0,0 +1,297 @@
+#!/usr/bin/env python3
+
+from __future__ import annotations
+
+import hashlib
+import json
+import os
+import subprocess
+import sys
+import tempfile
+import textwrap
+import unittest
+from pathlib import Path
+from typing import Any
+
+
+GATE = Path(__file__).with_name("replay_gate.py")
+BASELINE_DIGEST = "04bb68e54664a98f89e6cca20139cd39f95e9ffc241e7706104b4a998f909772"
+MUTATED_DIGEST = "f2840904afc832adbb98d2d8ff4e2e2679a9a69df190e020c62d242af86fcb3e"
+
+HELPER_SOURCE = r'''\
+#!/usr/bin/env python3
+
+import hashlib
+import json
+import os
+import sys
+
+
+mode = sys.argv[1]
+if mode == "generate":
+    rejected_score = 2 if "--flip-rejected" in sys.argv[2:] else 0
+    diagnostic = "mutated" if "--noise-only" in sys.argv[2:] else "baseline"
+    if "--rewrite-path" in sys.argv[2:]:
+        with open(__file__, "a", encoding="utf-8") as stream:
+            stream.write("\n# rewritten by generator\n")
+    output = {
+        "protocol": "SEMANTIC-REPLAY/v1/generator",
+        "generator_id": os.environ["SEMANTIC_REPLAY_GENERATOR_ID"],
+        "diagnostic": diagnostic,
+        "records": [
+            {"witness": {"id": "A", "row": [6, 4, 9]}, "data": {"score": 1}},
+            {"witness": {"id": "R", "row": [5, 4]}, "data": {"score": rejected_score}},
+        ],
+    }
+elif mode == "path":
+    generated = json.load(sys.stdin)
+    omit_rejected = "--omit-rejected" in sys.argv[2:]
+    bad_source = "--bad-source" in sys.argv[2:]
+    leaked_mutation = os.environ.get("SEMANTIC_REPLAY_MUTATION_ID")
+    results = []
+    for record in generated["records"]:
+        if omit_rejected and record["witness"]["id"] == "R":
+            continue
+        score = record["data"]["score"]
+        if leaked_mutation and record["witness"]["id"] == "R":
+            score = 2
+        source_sha256 = hashlib.sha256(
+            json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
+        ).hexdigest()
+        if bad_source and record["witness"]["id"] == "R":
+            source_sha256 = "0" * 64
+        results.append(
+            {
+                "witness": record["witness"],
+                "decision": "accept" if score > 0 else "reject",
+                "source_record_sha256": source_sha256,
+                "claim_fragment": {"score": score},
+            }
+        )
+    output = {
+        "protocol": "SEMANTIC-REPLAY/v1/path",
+        "path_id": os.environ["SEMANTIC_REPLAY_PATH_ID"],
+        "claim_id": os.environ["SEMANTIC_REPLAY_CLAIM_ID"],
+        "results": results,
+    }
+else:
+    raise SystemExit(9)
+print(json.dumps(output, sort_keys=True))
+'''
+
+# Exact extracts from the frozen charged ledger at
+# inputs/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md:206-212,231-250.
+LEDGER_EXTRACT = '''\
+The replay in `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` enumerates the rows of §4.1--4.2, verifies the Euler arithmetic, the forest list, the `m>=2h-1` inequality, the `S4` inertia screen, the leftover test for E1 on three components, and the one-node scope failure at `m>=2`. It does not encode (2.3), Chau, or the forest theorem.
+
+enumerated rows:                        16
+killed independently of (2.3):          4  (R2, R3 leftover; R15 S4; R16 EULER)
+surviving if only Lemmas 2.1--2.2:      12 (R1, R4--R14), each with n22 unbounded
+surviving if Lemma 2.3 is granted:      none
+
+The script `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` is a pure-stdlib enumerator.
+--mutate-allow-h-two-finite-t31     accept h=2 with e(T31)>=0
+--mutate-apply-one-node-to-T2       apply ONE-NODE to m=2
+--mutate-drop-overlapping-screen    treat pair-aligned T2 as generating S4
+stdout SHA-256:
+54df64d29d363581e4d1aa8c19c67da54a2b7c070e5aedd58d77d5e70ded2baa
+payload_sha256=bd6cedfd0328f68780c60844a4c7cb428a2a1d6fa55218911e2476588e27c283
+status=PASS-RANK4-REDUCIBLE-TREE-LEDGER
+All three mutations exit nonzero.
+'''
+
+# Exact extracts from the frozen charged census at
+# inputs/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md:81-103,219-225,275-303.
+CENSUS_EXTRACT = '''\
+In each display, `*N` marks a surviving row with labelled full-`S4` count `N`; every unmarked row has count zero.
+C=12:
+  (5,4), (6,4,9)*72, (7,3), (9,6,4)*72, (10,4,5), (13,2)
+a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
+  ops/block_descent_a1_genus_ladder_s4_replay.py
+e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b
+  ops/block_descent_a1_genus_ladder_next_s4_replay.py
+1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
+  canonical stdout under python3, python3 -O, and python3 -OO
+--mutate-framing
+--mutate-quotient
+--mutate-promote-zero
+Each mutation exits nonzero at an intended gate.
+'''
+
+
+def run_gate(certificate: Path) -> tuple[int, dict[str, Any]]:
+    environment = os.environ.copy()
+    environment["SEMANTIC_REPLAY_MUTATION_ID"] = "ambient-must-not-leak"
+    process = subprocess.run(
+        [sys.executable, "-B", str(GATE), "check", str(certificate)],
+        check=False,
+        capture_output=True,
+        env=environment,
+        text=True,
+    )
+    return process.returncode, json.loads(process.stdout)
+
+
+class ReplayGateTests(unittest.TestCase):
+    def setUp(self) -> None:
+        self.temporary = tempfile.TemporaryDirectory()
+        self.directory = Path(self.temporary.name)
+        self.helper = self.directory / "fixture_replay.py"
+        self.helper.write_text(textwrap.dedent(HELPER_SOURCE), encoding="utf-8")
+        self.helper_sha256 = hashlib.sha256(self.helper.read_bytes()).hexdigest()
+
+    def tearDown(self) -> None:
+        self.temporary.cleanup()
+
+    def certificate(self) -> dict[str, Any]:
+        entry = {
+            "id": "fixture-generator",
+            "script": self.helper.name,
+            "sha256": self.helper_sha256,
+            "args": ["generate"],
+        }
+        return {
+            "schema": "SEMANTIC-REPLAY/v1",
+            "claims": [
+                {
+                    "id": "synthetic-census",
+                    "generator": entry,
+                    "production_path": {
+                        "id": "fixture-production-path",
+                        "script": self.helper.name,
+                        "sha256": self.helper_sha256,
+                        "args": ["path"],
+                    },
+                    "claim_projection": "complete-results/v1",
+                    "witnesses": {
+                        "accepted": {"id": "A", "row": [6, 4, 9]},
+                        "rejected": {"id": "R", "row": [5, 4]},
+                    },
+                    "mutation": {
+                        "id": "flip-rejected-score",
+                        "generator_args_append": ["--flip-rejected"],
+                        "claim_sha256": MUTATED_DIGEST,
+                    },
+                    "baseline_claim_sha256": BASELINE_DIGEST,
+                }
+            ],
+        }
+
+    def write_json(self, value: Any, name: str = "certificate.json") -> Path:
+        path = self.directory / name
+        path.write_text(json.dumps(value), encoding="utf-8")
+        return path
+
+    def test_compliant_certificate_passes(self) -> None:
+        returncode, result = run_gate(self.write_json(self.certificate()))
+        self.assertEqual(returncode, 0)
+        self.assertEqual(result["status"], "PASS")
+
+    def test_invariant_generator_cannot_mutate_path_context(self) -> None:
+        certificate = self.certificate()
+        mutation = certificate["claims"][0]["mutation"]
+        mutation["id"] = "diagnostic-noise-only"
+        mutation["generator_args_append"] = ["--noise-only"]
+        mutation["claim_sha256"] = MUTATED_DIGEST
+        returncode, result = run_gate(self.write_json(certificate))
+        self.assertEqual(returncode, 3)
+        self.assertEqual(result["status"], "FAIL-INVARIANCE")
+
+    def test_bypasses_fail_four(self) -> None:
+        certificate = self.certificate()
+        certificate["claims"][0]["production_path"]["args"].append(
+            "--omit-rejected"
+        )
+        returncode, result = run_gate(self.write_json(certificate))
+        self.assertEqual(returncode, 4)
+        self.assertEqual(result["status"], "FAIL-BYPASS")
+        self.assertIn("bijection", result["reason"])
+
+        certificate = self.certificate()
+        certificate["claims"][0]["generator"]["args"].append("--rewrite-path")
+        returncode, result = run_gate(self.write_json(certificate, "rewrite.json"))
+        self.assertEqual(returncode, 4)
+        self.assertEqual(result["status"], "FAIL-BYPASS")
+        self.assertIn("SHA-256 mismatch", result["reason"])
+
+        self.helper.write_text(textwrap.dedent(HELPER_SOURCE), encoding="utf-8")
+        certificate = self.certificate()
+        certificate["claims"][0]["production_path"]["args"].append("--bad-source")
+        returncode, result = run_gate(self.write_json(certificate, "source.json"))
+        self.assertEqual(returncode, 4)
+        self.assertEqual(result["status"], "FAIL-BYPASS")
+        self.assertIn("source record digest mismatch", result["reason"])
+
+    def test_malformed_certificates_fail_two(self) -> None:
+        certificate = self.certificate()
+        del certificate["claims"][0]["mutation"]["claim_sha256"]
+        returncode, result = run_gate(self.write_json(certificate))
+        self.assertEqual(returncode, 2)
+        self.assertEqual(result["status"], "MALFORMED")
+        self.assertIn("claim_sha256", result["reason"])
+
+        certificate = self.certificate()
+        certificate["claims"][0]["generator"]["script"] = "\ud800"
+        returncode, result = run_gate(self.write_json(certificate, "surrogate.json"))
+        self.assertEqual(returncode, 2)
+        self.assertEqual(result["status"], "MALFORMED")
+        self.assertIn("Unicode scalar text", result["reason"])
+
+        deep = self.directory / "deep.json"
+        deep.write_text("[" * 1500 + "null" + "]" * 1500, encoding="utf-8")
+        returncode, result = run_gate(deep)
+        self.assertEqual(returncode, 2)
+        self.assertEqual(result["status"], "MALFORMED")
+        self.assertIn("nesting too deep", result["reason"])
+
+    def test_charged_reducible_ledger_fails_as_is(self) -> None:
+        path = self.directory / "charged-ledger-extract.md"
+        path.write_text(LEDGER_EXTRACT, encoding="utf-8")
+        returncode, result = run_gate(path)
+        self.assertEqual(returncode, 2)
+        self.assertEqual(result["status"], "MALFORMED")
+        self.assertIn("invalid JSON", result["reason"])
+
+    def test_charged_census_has_insufficient_certificate_data(self) -> None:
+        partial = {
+            "schema": "SEMANTIC-REPLAY/v1",
+            "_charged_source_extract": CENSUS_EXTRACT,
+            "claims": [
+                {
+                    "id": "complete-conductor-12-through-28-census",
+                    "generator": {
+                        "id": "ops/block_descent_a1_genus_ladder_s4_replay.py",
+                        "script": "ops/block_descent_a1_genus_ladder_s4_replay.py",
+                        "sha256": "a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a",
+                        "args": [],
+                    },
+                    "production_path": {
+                        "id": "ops/block_descent_a1_genus_ladder_next_s4_replay.py",
+                        "script": "ops/block_descent_a1_genus_ladder_next_s4_replay.py",
+                        "sha256": "e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b",
+                        "args": [],
+                    },
+                    "claim_projection": "complete-results/v1",
+                    "witnesses": {
+                        "accepted": {"conductor": 12, "row": [6, 4, 9]},
+                        "rejected": {"conductor": 12, "row": [5, 4]},
+                    },
+                    "_baseline_stdout_sha256": "1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6",
+                    "_documented_path_mutations": [
+                        "--mutate-framing",
+                        "--mutate-quotient",
+                        "--mutate-promote-zero",
+                    ],
+                }
+            ],
+        }
+        returncode, result = run_gate(
+            self.write_json(partial, "charged-census-partial.json")
+        )
+        self.assertEqual(returncode, 2)
+        self.assertEqual(result["status"], "MALFORMED")
+        self.assertIn("missing mutation", result["reason"])
+
+
+if __name__ == "__main__":
+    unittest.main()
```

## 5. Acceptance walkthroughs

### 5.1 Quarantined 16-row ledger

The test writes the exact charged extracts cited in its comment (ledger lines
206-212 and 231-250) without adapting them into a certificate, then performs:

```text
python3 -B ops/replay_gate.py check charged-ledger-extract.md
```

Expected stdout and exit are:

```text
{"reason": "certificate: invalid JSON: Expecting value: line 1 column 1 (char 0)", "status": "MALFORMED"}
exit 2
```

This is the required as-is failure.  The extract contains the 16-row summary,
script name, baseline hashes, and mutation names, but not the additive
declaration.  The test does not reinterpret a killed row as a rejected replay
control or an `OPEN` row as an accepted one.

### 5.2 Reviewed conductor census

The second acceptance fixture transcribes only data the charged census actually
contains: the two hash-pinned script paths, the accepted `(6,4,9)` and rejected
`(5,4)` rows at conductor 12, the aggregate stdout hash, and the three
documented path-mutation switches.  It adds the schema-defined projection name,
but deliberately omits a generator mutation and claim commitments because
those are absent from the artifact.  The run is:

```text
python3 -B ops/replay_gate.py check charged-census-partial.json
```

Expected stdout and exit are:

```text
{"reason": "claims[0]: missing mutation", "status": "MALFORMED"}
exit 2
```

Thus the requested census PASS cannot be demonstrated without inventing data;
the specified insufficient-artifact finding applies.  A future compliant
certificate needs the sealed generator to emit the generator protocol, the
reviewed replay to consume it and emit the path protocol, and one generator
mutation to complete successfully with a different committed
`complete-results/v1` digest.  Merely preserving the existing nonzero mutation
exits would produce a dynamic exit-4 bypass, not a pass.

## 6. Reproduction notes

The fenced patch was checked with `git apply --check` against the current clean
targets.  It was then applied to an isolated temporary tree and run with:

```text
python3 -B ops/test_replay_gate.py
```

Observed result:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 4.912s

OK
```

The six cases are: compliant synthetic pass, invariant generator mutation,
path-witness bypass, malformed certificate, charged ledger negative fixture,
and charged census insufficient-evidence fixture.  The tests create their
helper scripts and certificates only inside `TemporaryDirectory`; the proposed
patch adds no fixture files and makes no CI-runner change.

The hash boundary is the two declared Python entrypoints.  If an entrypoint
imports other custody-critical code, that dependency must remain independently
pinned by the replay or be promoted to an entrypoint in a successor schema;
v1 does not infer dependency custody from an import name.

<!-- BODY-END -->
