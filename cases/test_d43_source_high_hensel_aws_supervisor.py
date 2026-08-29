#!/usr/bin/env python3
"""Light hostile fixtures for the route-specific AWS custody layer."""

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import d43_source_high_hensel as H
import d43_source_high_hensel_aws_supervisor as S


class ContractTests(unittest.TestCase):
    def test_runner_and_supervisor_scope_firewalls_are_identical(self):
        self.assertEqual(S.SCOPE, H.SCOPE)
        self.assertEqual(S.CERTIFIED_CLAIM, H.CERTIFIED_CLAIM)
        self.assertEqual(S.EXACT_RELATIONS_REPLAYED,
                         list(H.EXACT_RELATIONS_REPLAYED))
        self.assertEqual(S.UPSTREAM_NOT_REPLAYED,
                         list(H.UPSTREAM_NOT_REPLAYED))
        self.assertEqual(S.FORBIDDEN_CLAIMS, list(H.FORBIDDEN_CLAIMS))
        self.assertEqual(S.TARGET_TAGS, H.AWS_TARGET_TAGS)
        self.assertIn("parked/source presentation equivalence",
                      S.FORBIDDEN_CLAIMS)
        self.assertIn("indefinite source solvability or formal smoothness",
                      S.FORBIDDEN_CLAIMS)
        self.assertIn("full residue-A/template/D25 p-adic point or upstream exact-equation lift",
                      S.FORBIDDEN_CLAIMS)
        worker = Path(HERE, "d43_source_high_hensel_aws_worker.sh").read_text()
        supervisor = Path(
            HERE, "d43_source_high_hensel_aws_supervisor.py").read_text()
        self.assertIn('exec "$D43_PYTHON" -I "$D43_RUNNER"', worker)
        self.assertIn('"PYTHONPATH": ""', supervisor)

    def test_direct_p3_plus_runner_route_is_fail_closed(self):
        old_path = os.environ.pop("JC2_D43_HENSEL_AWS_AUTH", None)
        old_hash = os.environ.pop("JC2_D43_HENSEL_AWS_AUTH_SHA256", None)
        try:
            with self.assertRaisesRegex(RuntimeError, "authenticated AWS"):
                H.validate_aws_lane_authorization(16, "/tmp/state", "/tmp/report")
        finally:
            if old_path is not None:
                os.environ["JC2_D43_HENSEL_AWS_AUTH"] = old_path
            if old_hash is not None:
                os.environ["JC2_D43_HENSEL_AWS_AUTH_SHA256"] = old_hash


class ManifestTests(unittest.TestCase):
    def test_exact_manifest_and_preregistration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.txt").write_text("alpha\n")
            (root / "b.txt").write_text("beta\n")
            entries = {name: S.sha256_path(root / name)
                       for name in ("a.txt", "b.txt")}
            manifest = root / "payload.sha256"
            manifest.write_text("".join("%s  %s\n" % (digest, name)
                                        for name, digest in entries.items()))
            observed = S.parse_hash_manifest(root, manifest)
            self.assertEqual(observed, entries)
            manifest_sha256 = S.sha256_path(manifest)
            prereg = {
                "protocol": S.ROUTE,
                "state_schema": S.STATE_SCHEMA,
                "status": S.AUTHORIZED_PREREG_STATUS,
                "scope": S.SCOPE,
                "certified_claim": S.CERTIFIED_CLAIM,
                "exact_relations_replayed": S.EXACT_RELATIONS_REPLAYED,
                "upstream_not_replayed": S.UPSTREAM_NOT_REPLAYED,
                "forbidden_claims": S.FORBIDDEN_CLAIMS,
                "inputs": entries,
                "aws_route": {
                    "schema": "D43-HIGH-HENSEL-AWS-ROUTE-V1",
                    "timeout_seconds": S.TIMEOUT_SECONDS,
                    "rss_limit_bytes": S.RSS_LIMIT_BYTES,
                    "swap_bytes_allowed": 0,
                    "sample_interval_seconds": S.SAMPLE_INTERVAL_SECONDS,
                    "instance_type": S.EXPECTED_INSTANCE_TYPE,
                    "target_tags": {"16": S.TARGET_TAGS[16],
                                    "64": S.TARGET_TAGS[64]},
                    "payload_manifest_sha256": manifest_sha256,
                    "payload_files": list(entries),
                },
            }
            prereg_path = root / "prereg.json"
            prereg_path.write_text(json.dumps(prereg))
            got = S.verify_preregistration(
                root, prereg_path, observed, 16, S.TARGET_TAGS[16],
                manifest_sha256)
            self.assertEqual(got["protocol"], S.ROUTE)

    def test_rereview_pending_preregistration_blocks_launch(self):
        root = Path(HERE).parent
        manifest = root / "cases/d43_source_high_hensel_aws_payload_20260828.sha256"
        prereg = root / "cases/d43_source_high_hensel_prereg_20260828.json"
        entries = S.parse_hash_manifest(root, manifest)
        with self.assertRaisesRegex(S.CustodyFault, "hostile rereview"):
            S.verify_preregistration(
                root, prereg, entries, 16, S.TARGET_TAGS[16],
                S.sha256_path(manifest))

    def test_manifest_tamper_symlink_and_coverage_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target"
            target.write_text("one")
            digest = S.sha256_path(target)
            manifest = root / "payload.sha256"
            manifest.write_text("%s  target\n" % digest)
            target.write_text("two")
            with self.assertRaisesRegex(S.CustodyFault, "target"):
                S.parse_hash_manifest(root, manifest)
            target.write_text("one")
            link = root / "link"
            link.symlink_to(target)
            manifest.write_text("%s  link\n" % digest)
            with self.assertRaisesRegex(S.CustodyFault, "symlink"):
                S.parse_hash_manifest(root, manifest)


class ResourceAndArchiveTests(unittest.TestCase):
    def test_process_topology_detects_escape_foreign_group_and_resources(self):
        table = {
            100: {"ppid": 1, "pgrp": 100, "rss": 10, "swap": 0},
            101: {"ppid": 100, "pgrp": 100, "rss": 20, "swap": 3},
            102: {"ppid": 101, "pgrp": 102, "rss": 30, "swap": 0},
            103: {"ppid": 1, "pgrp": 100, "rss": 40, "swap": 0},
        }
        got = S.process_topology(table, 100)
        self.assertEqual(got["group_pids"], [100, 101, 103])
        self.assertEqual(got["descendant_pids"], [101, 102])
        self.assertEqual(got["escaped_descendant_pids"], [102])
        self.assertEqual(got["unexpected_group_pids"], [103])
        self.assertEqual(got["rss_bytes"], 70)
        self.assertEqual(got["process_swap_bytes"], 3)

    def test_swap_parser(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as handle:
            handle.write("MemTotal: 100 kB\nSwapTotal: 64 kB\nSwapFree: 48 kB\n")
            path = handle.name
        try:
            self.assertEqual(S.meminfo_swap_used_bytes(path), 16 * 1024)
        finally:
            os.unlink(path)

    def test_deterministic_archive_and_terminal_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            first.write_text("a")
            second.write_text("b")
            one = root / "one.tar.gz"
            two = root / "two.tar.gz"
            members = [("first", first), ("second", second)]
            self.assertEqual(S.deterministic_tar(one, root, members),
                             S.deterministic_tar(two, root, members))
            run_dir = root / "run"
            run_dir.mkdir()
            (run_dir / "worker.stdout").write_text("done\n")
            result = S.terminal_bundle(
                run_dir, {"schema": S.TERMINAL_SCHEMA,
                          "status": "NO_VERDICT_CUSTODY_FAULT"})
            self.assertTrue((run_dir / "terminal_manifest.sha256").is_file())
            self.assertTrue((run_dir / "evidence_archive.tar.gz").is_file())
            self.assertRegex(result["archive_sha256"], r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main()
