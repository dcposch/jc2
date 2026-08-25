#!/usr/bin/env python3
"""Lightweight provenance/semantic audit for the harvested order-128 run.

This does not recompute the Hensel lifts or rank matrices.  Those exact
finite-field computations are reproduced by the pinned worker on an
appropriately provisioned host.  Here we fail closed on the source and
payload hashes and independently reconstruct the tested rectangle set.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
AWS = CASE / "aws"
ACTIVE = ROOT / "cases/max12_912_order3_nu_q8_invariant_support_20260824"
PARENT = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824"

EXPECTED_FILES = {
    ROOT / "ops/aws_q8_invariant_support_run.sh":
        "389d9eb23eae1080a9dce3b3521322f9de2adc8766a7c74a2db55e61fbd981a1",
    ACTIVE / "modular_support.py":
        "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0",
    ACTIVE / "run_matrix.py":
        "c57bea5c7423a26aaf22caf4d2894dc5dc5645793d58f127d101d86d4b68cfe6",
    ACTIVE / "replay.py":
        "b94cc59a2d64602481a1e5709709c990dc3dc5f766b8c2b0eab9a5439746aa1a",
    PARENT / "MANIFEST.sha256":
        "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4",
    PARENT / "FREEZE.txt":
        "c34fff2b838ca4803872b709857ae7becb1751a7e1ce261c9fa8c7e6d8b46c97",
    AWS / "metadata.txt":
        "ecabb2af6dbd8af659cb762164541971d238a699dbc30053fdb826633f23324b",
    AWS / "summary.json":
        "32147526bd6522a9ffb5fc672415765cedd3e6f653314fa8064a214f943c3d79",
    AWS / "stderr.log":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}

RESULTS = {
    (10007, 980): (2820,
        "cfb1b6f7ed26df91e03df73d7e97a8d052749179d74d2ef14e5689a0771b421e"),
    (10037, 1220): (4798,
        "ad6ed48366cc36e56bb4753d53bb77a2c954c22c0ef8507ed45d5b7cb8b3184d"),
    (10039, 8298): (4999,
        "4639c9127d24e55f70957f1ab67bb24f7920c8f475558f8e753885fa38223dbf"),
    (10061, 5525): (4921,
        "cf6705e1a7ebf1b56f83164cf585eb6baf409493851135bf8aedb4f6519e0129"),
    (10067, 1853): (6058,
        "f9772b60646d93d79ea04d96e1715ea1422072459ae129b3129ef876269b1a48"),
    (10069, 5814): (5358,
        "f30385abf8881d4cf4fcdbe1c1f07b778a52fed7d1e98f28107352617e7eff96"),
    (10079, 8882): (8870,
        "7ce0e431ee08b423493a12b51046998a6ab7ac556ee16599ac2b5117e8168d25"),
    (10091, 5216): (4305,
        "e773e0ec0abeeb025d7f9caf352dca017ee383cb381eca7d1bbe0a33bcc94ce3"),
}

PAIRS = ("n,q", "theta,Z", "theta,q", "w,q")
RECTANGLE_SHA256 = (
    "5ca5018958874fca091d18a8eafd4a4bd3a089bdb59b4c75232d70310e932ae1"
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def reconstruct_rectangles() -> tuple[list[dict], str]:
    tested = []
    for left_degree in range(1, 25):
        for right_degree in range(1, 25):
            columns = (left_degree + 1) * (right_degree + 1)
            if columns > 108 or columns > 112:
                continue
            tested.append({
                "left_degree": left_degree,
                "right_degree": right_degree,
                "columns": columns,
                "fit_nullity": 0,
                "holdout_pass": False,
            })
    canonical = json.dumps(tested, sort_keys=True, separators=(",", ":"))
    return tested, sha256(canonical.encode()).hexdigest()


def parse_metadata() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for line in (AWS / "metadata.txt").read_text().splitlines():
        key, value = line.split("=", 1)
        out.setdefault(key, []).append(value)
    return out


def main() -> None:
    for path, expected in EXPECTED_FILES.items():
        check(digest(path) == expected, f"hash mismatch: {path}")

    metadata = parse_metadata()
    for key, expected in {
        "tag": "q8_invariant_support_order128_v1",
        "backend": "python-exact-modular-q8-support",
        "workers": "8",
        "order": "128",
        "max_left": "24",
        "max_right": "24",
        "max_columns": "108",
        "holdout": "16",
        "exit_code": "0",
        "stderr_bytes": "0",
        "result_count": "8",
        "final_status": "DONE",
    }.items():
        check(metadata.get(key) == [expected], f"metadata mismatch: {key}")
    check(metadata["summary_sha256"] == [EXPECTED_FILES[AWS / "summary.json"]],
          "metadata summary hash")
    check(metadata["stderr_sha256"] == [EXPECTED_FILES[AWS / "stderr.log"]],
          "metadata stderr hash")

    summary = json.loads((AWS / "summary.json").read_text())
    check(summary["all_pass"] is True, "matrix run did not pass")
    check(summary["worker_sha256"] == EXPECTED_FILES[ACTIVE / "modular_support.py"],
          "summary worker hash")
    check(summary["parameters"] == {
        "workers": 8,
        "order": 128,
        "max_left": 24,
        "max_right": 24,
        "max_columns": 108,
        "holdout": 16,
        "timeout": 3600,
    }, "summary parameters")
    check(len(summary["jobs"]) == 8, "job count")

    rectangles, rectangle_hash = reconstruct_rectangles()
    check(len(rectangles) == 229, "rectangle count")
    check(rectangle_hash == RECTANGLE_SHA256, "rectangle-set hash")

    jobs = {(job["prime"], job["root"]): job for job in summary["jobs"]}
    check(set(jobs) == set(RESULTS), "job set")
    determinants = {}
    for (prime, root), (expected_det, expected_hash) in RESULTS.items():
        job = jobs[(prime, root)]
        check(job["returncode"] == 0 and job["stderr"] == "", "job failure")
        path = AWS / "results" / f"support-p{prime}-v{root}.json"
        check(digest(path) == expected_hash, f"result hash: {prime}")
        data = json.loads(path.read_text())
        check((data["prime"], data["q8_root"]) == (prime, root), "prime/root")
        good = data["good_reduction"]
        check(good["prime_by_trial_division"] is True, "primality check")
        check(good["Q8_at_root"] == 0, "Q8 root")
        check(good["all_fraction_denominators_inverted"] is True,
              "denominator check")
        check(good["six_by_six_jacobian_determinant"] == expected_det,
              "Jacobian determinant")
        check(expected_det % prime != 0, "singular Jacobian")
        check(data["order"] == 128 and data["holdout"] == 16, "series order")
        check(data["max_degrees"] == [24, 24], "degree box")
        check(data["max_columns"] == 108, "column cap")
        check(data["monomial_closure_size"] == 297, "closure size")
        check(set(data["relation_searches"]) == set(PAIRS), "pair set")
        for pair in PAIRS:
            search = data["relation_searches"][pair]
            check(search["tested_rectangles"] == 229, "tested rectangles")
            check(search["full_column_rank_rectangles"] == 229, "full ranks")
            check(search["all_fit_matrices_full_column_rank"] is True,
                  "rank flag")
            check(search["max_tested_columns"] == 108, "tested columns")
            check(search["hits"] == [], "unexpected relation hit")
            check(search["nonzero_fit_nullities"] == [], "unexpected nullity")
            check(search["tested_rectangles_sha256"] == RECTANGLE_SHA256,
                  "tested rectangle hash")
        determinants[str(prime)] = expected_det

    payload = {
        "status": "PASS",
        "scope": (
            "harvest/source audit plus exact finite-box Q-relation exclusion; "
            "not a global equation or trajectory theorem"
        ),
        "good_reductions": len(RESULTS),
        "pairs": list(PAIRS),
        "rectangles_per_pair_per_prime": 229,
        "rectangles_per_pair_across_primes": 229 * len(RESULTS),
        "total_full_column_rank_matrices": 229 * len(PAIRS) * len(RESULTS),
        "fit_rows": 112,
        "holdout_rows": 16,
        "max_columns": 108,
        "tested_rectangles_sha256": RECTANGLE_SHA256,
        "jacobian_determinants": determinants,
        "summary_sha256": EXPECTED_FILES[AWS / "summary.json"],
        "stderr_sha256": EXPECTED_FILES[AWS / "stderr.log"],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
