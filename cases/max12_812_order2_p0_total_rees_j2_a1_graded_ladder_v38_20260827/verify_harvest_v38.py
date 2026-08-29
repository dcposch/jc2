#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath


HERE = Path(__file__).resolve().parent
EXPECTED_RANKS = {
    "i1_j0": 0, "i1_j1": 0, "i1_j2": 0, "i1_j3": 0, "i1_j4": 0, "i1_j5": 0,
    "i2_j0": 0, "i2_j1": 0, "i2_j2": 0, "i2_j3": 0,
    "i3_j0": 6, "i3_j1": 50, "i3_j2": 333,
    "i4_j0": 156, "i4_j1": 1111, "i5_j0": 2286,
}
PRIMES = (65519, 65521)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw, parse_constant=lambda token: fail(("JSON constant", token)))
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail(("noncanonical JSON", str(path)))
    return value


def verify_evidence(job: Path) -> int:
    manifest = job / "EVIDENCE.sha256"
    count = 0
    for line in manifest.read_text().splitlines():
        if len(line) < 68 or line[64:68] != "  ./":
            fail(("evidence syntax", str(manifest), line))
        expected = line[:64]
        relative = PurePosixPath(line[68:])
        if relative.is_absolute() or ".." in relative.parts or relative.name == "EVIDENCE.sha256":
            fail(("nonrelocatable evidence path", str(relative)))
        path = job.joinpath(*relative.parts)
        if not path.is_file() or digest(path) != expected:
            fail(("evidence hash", str(path)))
        count += 1
    if count != 11:
        fail(("evidence count", str(job), count))
    return count


def one_lane(label: str, prime: int):
    job = HERE / f"aws_q{prime}_{label}"
    if not job.is_dir() or verify_evidence(job) != 11:
        fail(("job", label, prime))
    final = canonical_json(job / "RESULT.json")
    compiled = canonical_json(job / "compiled/result.json")
    if (final.get("status") != "PASS-A1-GRADED-LADDER-V38"
            or final.get("target_label") != label
            or type(final.get("selector_prime_requested")) is not int
            or final["selector_prime_requested"] != prime
            or type(final.get("selector_prime_used")) is not int
            or final["selector_prime_used"] != prime
            or final.get("outcome") != "nonmember"
            or type(final.get("exact_rank")) is not int
            or final["exact_rank"] != EXPECTED_RANKS[label]
            or final.get("result_sha256") != digest(job / "compiled/result.json")):
        fail(("validated result contract", label, prime))
    if (compiled.get("target_label") != label or compiled.get("selector_prime_requested") != prime
            or compiled.get("record", {}).get("selector_prime_used") != prime
            or compiled.get("record", {}).get("outcome") != "nonmember"
            or compiled.get("record", {}).get("exact_rank") != EXPECTED_RANKS[label]):
        fail(("compiled result contract", label, prime))
    compiler_stdout = tuple((job / "run").glob("*_compiler.stdout"))
    validator_stdout = tuple((job / "run").glob("*_validator.stdout"))
    if len(compiler_stdout) != 1 or len(validator_stdout) != 1:
        fail(("stdout census", label, prime))
    if compiler_stdout[0].read_text().splitlines().count(f"RESULT_SHA256={digest(job / 'compiled/result.json')}") != 1:
        fail(("compiler stdout binding", label, prime))
    if validator_stdout[0].read_text().splitlines().count(f"RESULT_SHA256={digest(job / 'RESULT.json')}") != 1:
        fail(("validator stdout binding", label, prime))
    core = dict(compiled["record"])
    core.pop("selector_prime_requested")
    core.pop("selector_prime_used")
    core_bytes = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {
        "core_sha256": sha256(core_bytes).hexdigest(),
        "result_sha256": digest(job / "RESULT.json"),
        "compiled_sha256": digest(job / "compiled/result.json"),
        "evidence_sha256": digest(job / "EVIDENCE.sha256"),
    }


def main() -> None:
    for label in sorted(EXPECTED_RANKS):
        lanes = {prime: one_lane(label, prime) for prime in PRIMES}
        if lanes[65519]["core_sha256"] != lanes[65521]["core_sha256"]:
            fail(("dual-lane canonical core disagreement", label))
        print("\t".join((
            label, str(EXPECTED_RANKS[label]), lanes[65519]["core_sha256"],
            lanes[65519]["result_sha256"], lanes[65519]["compiled_sha256"], lanes[65519]["evidence_sha256"],
            lanes[65521]["result_sha256"], lanes[65521]["compiled_sha256"], lanes[65521]["evidence_sha256"],
        )))
    print("PASS-V38-HARVEST-32-LANES")


if __name__ == "__main__":
    main()
