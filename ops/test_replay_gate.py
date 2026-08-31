#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from typing import Any


GATE = Path(__file__).with_name("replay_gate.py")
BASELINE_DIGEST = "04bb68e54664a98f89e6cca20139cd39f95e9ffc241e7706104b4a998f909772"
MUTATED_DIGEST = "f2840904afc832adbb98d2d8ff4e2e2679a9a69df190e020c62d242af86fcb3e"

HELPER_SOURCE = r'''\
#!/usr/bin/env python3

import hashlib
import json
import os
import sys


mode = sys.argv[1]
if mode == "generate":
    rejected_score = 2 if "--flip-rejected" in sys.argv[2:] else 0
    diagnostic = "mutated" if "--noise-only" in sys.argv[2:] else "baseline"
    if "--rewrite-path" in sys.argv[2:]:
        with open(__file__, "a", encoding="utf-8") as stream:
            stream.write("\n# rewritten by generator\n")
    output = {
        "protocol": "SEMANTIC-REPLAY/v1/generator",
        "generator_id": os.environ["SEMANTIC_REPLAY_GENERATOR_ID"],
        "diagnostic": diagnostic,
        "records": [
            {"witness": {"id": "A", "row": [6, 4, 9]}, "data": {"score": 1}},
            {"witness": {"id": "R", "row": [5, 4]}, "data": {"score": rejected_score}},
        ],
    }
elif mode == "path":
    generated = json.load(sys.stdin)
    omit_rejected = "--omit-rejected" in sys.argv[2:]
    bad_source = "--bad-source" in sys.argv[2:]
    leaked_mutation = os.environ.get("SEMANTIC_REPLAY_MUTATION_ID")
    results = []
    for record in generated["records"]:
        if omit_rejected and record["witness"]["id"] == "R":
            continue
        score = record["data"]["score"]
        if leaked_mutation and record["witness"]["id"] == "R":
            score = 2
        source_sha256 = hashlib.sha256(
            json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        if bad_source and record["witness"]["id"] == "R":
            source_sha256 = "0" * 64
        results.append(
            {
                "witness": record["witness"],
                "decision": "accept" if score > 0 else "reject",
                "source_record_sha256": source_sha256,
                "claim_fragment": {"score": score},
            }
        )
    output = {
        "protocol": "SEMANTIC-REPLAY/v1/path",
        "path_id": os.environ["SEMANTIC_REPLAY_PATH_ID"],
        "claim_id": os.environ["SEMANTIC_REPLAY_CLAIM_ID"],
        "results": results,
    }
else:
    raise SystemExit(9)
print(json.dumps(output, sort_keys=True))
'''

# Exact extracts from the frozen charged ledger at
# inputs/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md:206-212,231-250.
LEDGER_EXTRACT = '''\
The replay in `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` enumerates the rows of §4.1--4.2, verifies the Euler arithmetic, the forest list, the `m>=2h-1` inequality, the `S4` inertia screen, the leftover test for E1 on three components, and the one-node scope failure at `m>=2`. It does not encode (2.3), Chau, or the forest theorem.

enumerated rows:                        16
killed independently of (2.3):          4  (R2, R3 leftover; R15 S4; R16 EULER)
surviving if only Lemmas 2.1--2.2:      12 (R1, R4--R14), each with n22 unbounded
surviving if Lemma 2.3 is granted:      none

The script `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` is a pure-stdlib enumerator.
--mutate-allow-h-two-finite-t31     accept h=2 with e(T31)>=0
--mutate-apply-one-node-to-T2       apply ONE-NODE to m=2
--mutate-drop-overlapping-screen    treat pair-aligned T2 as generating S4
stdout SHA-256:
54df64d29d363581e4d1aa8c19c67da54a2b7c070e5aedd58d77d5e70ded2baa
payload_sha256=bd6cedfd0328f68780c60844a4c7cb428a2a1d6fa55218911e2476588e27c283
status=PASS-RANK4-REDUCIBLE-TREE-LEDGER
All three mutations exit nonzero.
'''

# Exact extracts from the frozen charged census at
# inputs/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md:81-103,219-225,275-303.
CENSUS_EXTRACT = '''\
In each display, `*N` marks a surviving row with labelled full-`S4` count `N`; every unmarked row has count zero.
C=12:
  (5,4), (6,4,9)*72, (7,3), (9,6,4)*72, (10,4,5), (13,2)
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
  ops/block_descent_a1_genus_ladder_s4_replay.py
e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b
  ops/block_descent_a1_genus_ladder_next_s4_replay.py
1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
  canonical stdout under python3, python3 -O, and python3 -OO
--mutate-framing
--mutate-quotient
--mutate-promote-zero
Each mutation exits nonzero at an intended gate.
'''


def run_gate(certificate: Path) -> tuple[int, dict[str, Any]]:
    environment = os.environ.copy()
    environment["SEMANTIC_REPLAY_MUTATION_ID"] = "ambient-must-not-leak"
    process = subprocess.run(
        [sys.executable, "-B", str(GATE), "check", str(certificate)],
        check=False,
        capture_output=True,
        env=environment,
        text=True,
    )
    return process.returncode, json.loads(process.stdout)


class ReplayGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)
        self.helper = self.directory / "fixture_replay.py"
        self.helper.write_text(textwrap.dedent(HELPER_SOURCE), encoding="utf-8")
        self.helper_sha256 = hashlib.sha256(self.helper.read_bytes()).hexdigest()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def certificate(self) -> dict[str, Any]:
        entry = {
            "id": "fixture-generator",
            "script": self.helper.name,
            "sha256": self.helper_sha256,
            "args": ["generate"],
        }
        return {
            "schema": "SEMANTIC-REPLAY/v1",
            "claims": [
                {
                    "id": "synthetic-census",
                    "generator": entry,
                    "production_path": {
                        "id": "fixture-production-path",
                        "script": self.helper.name,
                        "sha256": self.helper_sha256,
                        "args": ["path"],
                    },
                    "claim_projection": "complete-results/v1",
                    "witnesses": {
                        "accepted": {"id": "A", "row": [6, 4, 9]},
                        "rejected": {"id": "R", "row": [5, 4]},
                    },
                    "mutation": {
                        "id": "flip-rejected-score",
                        "generator_args_append": ["--flip-rejected"],
                        "claim_sha256": MUTATED_DIGEST,
                    },
                    "baseline_claim_sha256": BASELINE_DIGEST,
                }
            ],
        }

    def write_json(self, value: Any, name: str = "certificate.json") -> Path:
        path = self.directory / name
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def test_compliant_certificate_passes(self) -> None:
        returncode, result = run_gate(self.write_json(self.certificate()))
        self.assertEqual(returncode, 0)
        self.assertEqual(result["status"], "PASS")

    def test_invariant_generator_cannot_mutate_path_context(self) -> None:
        certificate = self.certificate()
        mutation = certificate["claims"][0]["mutation"]
        mutation["id"] = "diagnostic-noise-only"
        mutation["generator_args_append"] = ["--noise-only"]
        mutation["claim_sha256"] = MUTATED_DIGEST
        returncode, result = run_gate(self.write_json(certificate))
        self.assertEqual(returncode, 3)
        self.assertEqual(result["status"], "FAIL-INVARIANCE")

    def test_bypasses_fail_four(self) -> None:
        certificate = self.certificate()
        certificate["claims"][0]["production_path"]["args"].append(
            "--omit-rejected"
        )
        returncode, result = run_gate(self.write_json(certificate))
        self.assertEqual(returncode, 4)
        self.assertEqual(result["status"], "FAIL-BYPASS")
        self.assertIn("bijection", result["reason"])

        certificate = self.certificate()
        certificate["claims"][0]["generator"]["args"].append("--rewrite-path")
        returncode, result = run_gate(self.write_json(certificate, "rewrite.json"))
        self.assertEqual(returncode, 4)
        self.assertEqual(result["status"], "FAIL-BYPASS")
        self.assertIn("SHA-256 mismatch", result["reason"])

        self.helper.write_text(textwrap.dedent(HELPER_SOURCE), encoding="utf-8")
        certificate = self.certificate()
        certificate["claims"][0]["production_path"]["args"].append("--bad-source")
        returncode, result = run_gate(self.write_json(certificate, "source.json"))
        self.assertEqual(returncode, 4)
        self.assertEqual(result["status"], "FAIL-BYPASS")
        self.assertIn("source record digest mismatch", result["reason"])

    def test_malformed_certificates_fail_two(self) -> None:
        certificate = self.certificate()
        del certificate["claims"][0]["mutation"]["claim_sha256"]
        returncode, result = run_gate(self.write_json(certificate))
        self.assertEqual(returncode, 2)
        self.assertEqual(result["status"], "MALFORMED")
        self.assertIn("claim_sha256", result["reason"])

        certificate = self.certificate()
        certificate["claims"][0]["generator"]["script"] = "\ud800"
        returncode, result = run_gate(self.write_json(certificate, "surrogate.json"))
        self.assertEqual(returncode, 2)
        self.assertEqual(result["status"], "MALFORMED")
        self.assertIn("Unicode scalar text", result["reason"])

        deep = self.directory / "deep.json"
        deep.write_text("[" * 1500 + "null" + "]" * 1500, encoding="utf-8")
        returncode, result = run_gate(deep)
        self.assertEqual(returncode, 2)
        self.assertEqual(result["status"], "MALFORMED")
        self.assertIn("nesting too deep", result["reason"])

    def test_charged_reducible_ledger_fails_as_is(self) -> None:
        path = self.directory / "charged-ledger-extract.md"
        path.write_text(LEDGER_EXTRACT, encoding="utf-8")
        returncode, result = run_gate(path)
        self.assertEqual(returncode, 2)
        self.assertEqual(result["status"], "MALFORMED")
        self.assertIn("invalid JSON", result["reason"])

    def test_charged_census_has_insufficient_certificate_data(self) -> None:
        partial = {
            "schema": "SEMANTIC-REPLAY/v1",
            "_charged_source_extract": CENSUS_EXTRACT,
            "claims": [
                {
                    "id": "complete-conductor-12-through-28-census",
                    "generator": {
                        "id": "ops/block_descent_a1_genus_ladder_s4_replay.py",
                        "script": "ops/block_descent_a1_genus_ladder_s4_replay.py",
                        "sha256": "a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a",
                        "args": [],
                    },
                    "production_path": {
                        "id": "ops/block_descent_a1_genus_ladder_next_s4_replay.py",
                        "script": "ops/block_descent_a1_genus_ladder_next_s4_replay.py",
                        "sha256": "e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b",
                        "args": [],
                    },
                    "claim_projection": "complete-results/v1",
                    "witnesses": {
                        "accepted": {"conductor": 12, "row": [6, 4, 9]},
                        "rejected": {"conductor": 12, "row": [5, 4]},
                    },
                    "_baseline_stdout_sha256": "1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6",
                    "_documented_path_mutations": [
                        "--mutate-framing",
                        "--mutate-quotient",
                        "--mutate-promote-zero",
                    ],
                }
            ],
        }
        returncode, result = run_gate(
            self.write_json(partial, "charged-census-partial.json")
        )
        self.assertEqual(returncode, 2)
        self.assertEqual(result["status"], "MALFORMED")
        self.assertIn("missing mutation", result["reason"])


if __name__ == "__main__":
    unittest.main()
