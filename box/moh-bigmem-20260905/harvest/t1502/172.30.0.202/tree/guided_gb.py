#!/usr/bin/env python3
"""Guarded Singular standard-basis jobs with typed promotion scope.

The public entry point is :func:`guided_groebner`.  It emits a standalone
Singular script from a caller-supplied prelude and generator list, runs it under
``stdbuf -oL``, parses machine markers, and returns a typed verdict plus a JSON
serializable certificate.

The modular-to-characteristic-zero promotion implemented here is intentionally
narrow: a modular dimension-zero result is promoted only when the caller has
declared the ideal homogeneous for positive weights and requested the
properness scope.  Modular unit ideals are not promoted by default.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from enum import Enum
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import threading
import time
from typing import Any, Iterable, Mapping, Sequence


class Verdict(str, Enum):
    DIM0_CHAR0 = "DIM0_CHAR0"
    UNIT_IDEAL_CHAR0 = "UNIT_IDEAL_CHAR0"
    POSDIM = "POSDIM"
    MODULAR_ONLY = "MODULAR_ONLY"
    INCONCLUSIVE_TIMEOUT = "INCONCLUSIVE_TIMEOUT"


class PromotionScope(str, Enum):
    NONE = "NONE"
    EXACT_Q = "EXACT_Q"
    HOMOGENEOUS_POSITIVE_WEIGHTS_PROPERNESS = (
        "HOMOGENEOUS_POSITIVE_WEIGHTS_PROPERNESS"
    )


@dataclass(frozen=True)
class HilbertHint:
    """Hilbert-series hint for Singular's ``std(I, hilb, weights)`` call."""

    numerator: tuple[int, ...]
    weights: tuple[int, ...]
    predicted_length: int | None = None
    perturbed_numerator: tuple[int, ...] | None = None
    perturbed_predicted_length: int | None = None

    def __post_init__(self) -> None:
        if not self.numerator:
            raise ValueError("HilbertHint.numerator must be nonempty")
        if not self.weights or any(weight <= 0 for weight in self.weights):
            raise ValueError("HilbertHint.weights must be positive")

    @classmethod
    def from_sequences(
        cls,
        numerator: Sequence[int],
        weights: Sequence[int],
        predicted_length: int | None,
    ) -> "HilbertHint":
        return cls(tuple(numerator), tuple(weights), predicted_length)

    def perturbed(self) -> "HilbertHint":
        """Return the deliberate negative-control hint.

        The perturbation changes the numerator and, when a predicted length is
        available, also changes the acceptance target.  This catches the common
        case where Singular ignores a poor hint and still computes the true
        basis.
        """

        if self.perturbed_numerator is None:
            numerator = list(self.numerator)
            index = 1 if len(numerator) > 1 else 0
            numerator[index] += 1
        else:
            numerator = list(self.perturbed_numerator)

        if self.perturbed_predicted_length is not None:
            length = self.perturbed_predicted_length
        elif self.predicted_length is None:
            length = None
        else:
            length = self.predicted_length + 1
        return HilbertHint(tuple(numerator), self.weights, length)


@dataclass(frozen=True)
class SingularSystem:
    """A Singular ideal in an already-declared ring.

    ``prelude`` must declare ``basering`` and every generator named in
    ``generators``.  It may also contain cheap sanity checks.  The emitted job
    appends its own ideal and controls after the prelude.
    """

    name: str
    prelude: str
    generators: tuple[str, ...]
    characteristic: int = 0
    variables: tuple[str, ...] = ()
    homogeneous: bool = False
    positive_weights: tuple[int, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("SingularSystem.name must be nonempty")
        if not self.generators:
            raise ValueError("SingularSystem.generators must be nonempty")
        if self.homogeneous and (
            not self.positive_weights or any(weight <= 0 for weight in self.positive_weights)
        ):
            raise ValueError("homogeneous systems need positive weights")


@dataclass(frozen=True)
class PromotionPolicy:
    """Rules for turning accepted computations into public verdicts."""

    scope: PromotionScope = PromotionScope.NONE
    require_controls: bool = True
    allow_modular_unit_promotion: bool = False
    note: str = ""

    @classmethod
    def exact_q(cls, note: str = "") -> "PromotionPolicy":
        return cls(PromotionScope.EXACT_Q, True, False, note)

    @classmethod
    def homogeneous_properness(cls, note: str = "") -> "PromotionPolicy":
        return cls(
            PromotionScope.HOMOGENEOUS_POSITIVE_WEIGHTS_PROPERNESS,
            True,
            False,
            note,
        )


@dataclass(frozen=True)
class RunConfig:
    output_dir: Path
    timeout_seconds: int = 1800
    total_cores: int = 4
    singular: str = "Singular"
    max_parallel_jobs: int | None = None
    memory_kb: int | None = None
    run_perturbed_control: bool = True
    no_rc: bool = True


@dataclass
class RunControls:
    nf_all_zero: bool = False
    unit: bool = False
    dimension: int | None = None
    vdim: int | None = None
    basis_size: int | None = None
    lead_dim: int | None = None
    lead_vdim: int | None = None
    vdim_matches_predicted: bool | None = None
    accepted: bool = False
    missing_markers: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SingularRunResult:
    label: str
    characteristic: int
    command: list[str]
    script: str
    stdout: str
    stderr: str
    returncode: int | None
    elapsed_seconds: float
    timed_out: bool
    main: RunControls
    perturbed: RunControls | None = None
    stdout_sha256: str = ""
    stderr_sha256: str = ""
    script_sha256: str = ""

    def to_json(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["main"] = self.main.to_json()
        payload["perturbed"] = None if self.perturbed is None else self.perturbed.to_json()
        return payload


@dataclass
class GuidedGBResult:
    verdict: Verdict
    certificate: dict[str, Any]

    def to_json(self) -> dict[str, Any]:
        return {"verdict": self.verdict.value, "certificate": self.certificate}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def intvec(values: Sequence[int]) -> str:
    return ",".join(str(value) for value in values)


def singular_quote(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def prelude_from_script(path: Path, stop_regex: str = r"^intvec TARGET_HNUM=") -> str:
    """Return a script prefix ending before the first matching line."""

    pattern = re.compile(stop_regex)
    lines: list[str] = []
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if pattern.search(line):
                break
            lines.append(line.rstrip("\n"))
    if not lines:
        raise ValueError(f"no prelude read from {path}")
    return "\n".join(lines).rstrip() + "\n"


def _emit_one_analysis(
    run_id: str,
    generators: Sequence[str],
    hint: HilbertHint | None,
    expected_length: int | None,
) -> list[str]:
    basis = f"GG_G_{run_id}"
    ideal = f"GG_I_{run_id}"
    lines = [
        f'print("GG__RUN {run_id} START");',
        f"ideal {ideal}=" + ",".join(f"({generator})" for generator in generators) + ";",
        f'print("GG__GENERATOR_COUNT {run_id} "+string(size({ideal})));',
        f'print("GG__STD_BEGIN {run_id}");',
        "timer=1;",
        f"int GG_TIMER_{run_id}=timer;",
    ]
    if hint is None:
        lines.append(f"ideal {basis}=std({ideal});")
    else:
        hvar = f"GG_HNUM_{run_id}"
        wvar = f"GG_WTS_{run_id}"
        lines.extend(
            [
                f"intvec {hvar}={intvec(hint.numerator)};",
                f"intvec {wvar}={intvec(hint.weights)};",
                f'print("GG__TARGET_HNUM {run_id} "+string({hvar}));',
                f'print("GG__WEIGHTS {run_id} "+string({wvar}));',
                f"ideal {basis}=std({ideal},{hvar},{wvar});",
            ]
        )
    lines.extend(
        [
            f'print("GG__STD_SECONDS {run_id} "+string(timer-GG_TIMER_{run_id}));',
            f"int GG_NF_ALL_{run_id}=1;",
        ]
    )
    for index, generator in enumerate(generators):
        lines.extend(
            [
                f"poly GG_NF_{run_id}_{index}=reduce(({generator}),{basis});",
                f"int GG_NFZ_{run_id}_{index}=(GG_NF_{run_id}_{index}==0);",
                f"if (GG_NFZ_{run_id}_{index}==0) {{ GG_NF_ALL_{run_id}=0; }}",
                f'print("GG__NF_ZERO {run_id} {index} "+string(GG_NFZ_{run_id}_{index}));',
                f'print("GG__NF_SIZE {run_id} {index} "+string(size(GG_NF_{run_id}_{index})));',
            ]
        )
    lines.extend(
        [
            f'print("GG__NF_ALL_ZERO {run_id} "+string(GG_NF_ALL_{run_id}));',
            f"poly GG_NF1_{run_id}=reduce(1,{basis});",
            f"int GG_UNIT_{run_id}=(GG_NF1_{run_id}==0);",
            f'print("GG__UNIT {run_id} "+string(GG_UNIT_{run_id}));',
            f'print("GG__NF1_SIZE {run_id} "+string(size(GG_NF1_{run_id})));',
            f'print("GG__BASIS_SIZE {run_id} "+string(size({basis})));',
            f"int GG_DIM_{run_id}=dim({basis});",
            f'print("GG__DIM {run_id} "+string(GG_DIM_{run_id}));',
            f"int GG_VDIM_{run_id}=-1;",
            f"if (GG_DIM_{run_id}==0)",
            "{",
            f"  GG_VDIM_{run_id}=vdim({basis});",
            f'  print("GG__VDIM {run_id} "+string(GG_VDIM_{run_id}));',
            "}",
            "else",
            "{",
            f'  print("GG__VDIM {run_id} NONTERMINATING");',
            "}",
            f"ideal GG_LEADRAW_{run_id}=lead({basis});",
            f"ideal GG_LEADMIN_{run_id}=minbase(GG_LEADRAW_{run_id});",
            f"ideal GG_GLEAD_{run_id}=std(GG_LEADMIN_{run_id});",
            f'print("GG__LEAD_MIN_COUNT {run_id} "+string(size(GG_LEADMIN_{run_id})));',
            f"int GG_LEAD_DIM_{run_id}=dim(GG_GLEAD_{run_id});",
            f'print("GG__LEAD_DIM {run_id} "+string(GG_LEAD_DIM_{run_id}));',
            f"int GG_LEAD_VDIM_{run_id}=-1;",
            f"if (GG_LEAD_DIM_{run_id}==0)",
            "{",
            f"  GG_LEAD_VDIM_{run_id}=vdim(GG_GLEAD_{run_id});",
            f'  print("GG__LEAD_VDIM {run_id} "+string(GG_LEAD_VDIM_{run_id}));',
            "}",
            "else",
            "{",
            f'  print("GG__LEAD_VDIM {run_id} NONTERMINATING");',
            "}",
        ]
    )
    if expected_length is not None:
        lines.extend(
            [
                f"int GG_VDIM_MATCH_{run_id}="
                f"(GG_LEAD_DIM_{run_id}==0 and GG_LEAD_VDIM_{run_id}=={expected_length});",
                f'print("GG__VDIM_MATCH_PREDICTED {run_id} "+string(GG_VDIM_MATCH_{run_id}));',
                f"int GG_ACCEPT_{run_id}=(GG_NF_ALL_{run_id}==1 and "
                f"GG_LEAD_DIM_{run_id}==0 and GG_LEAD_VDIM_{run_id}=={expected_length});",
                f'print("GG__ACCEPT {run_id} "+string(GG_ACCEPT_{run_id}));',
            ]
        )
    else:
        lines.extend(
            [
                f"int GG_ACCEPT_{run_id}=(GG_NF_ALL_{run_id}==1);",
                f'print("GG__VDIM_MATCH_PREDICTED {run_id} NA");',
                f'print("GG__ACCEPT {run_id} "+string(GG_ACCEPT_{run_id}));',
            ]
        )
    lines.append(f'print("GG__RUN {run_id} END");')
    return lines


def emit_guided_script(
    system: SingularSystem,
    hint: HilbertHint | None = None,
    include_perturbed_control: bool = True,
) -> str:
    """Emit a standalone Singular script with mandatory controls."""

    lines = [
        "// generated by box/lib/guided_gb.py",
        f"// system={system.name}",
        f"// characteristic={system.characteristic}",
        f"// homogeneous={int(system.homogeneous)}",
    ]
    lines.append(system.prelude.rstrip())
    lines.extend(
        _emit_one_analysis(
            "main",
            system.generators,
            hint,
            None if hint is None else hint.predicted_length,
        )
    )
    if hint is not None and include_perturbed_control:
        bad = hint.perturbed()
        lines.extend(
            _emit_one_analysis(
                "perturbed",
                system.generators,
                bad,
                bad.predicted_length,
            )
        )
        lines.extend(
            [
                "int GG_PERTURBED_FAILED=(GG_ACCEPT_perturbed==0);",
                'print("GG__PERTURBED_FAILED control "+string(GG_PERTURBED_FAILED));',
            ]
        )
    lines.extend(['print("GG__SCRIPT_DONE main 1");', "quit;", ""])
    return "\n".join(lines)


def _stream_pipe(pipe: Any, path: Path, sink: list[str]) -> None:
    with path.open("w", encoding="utf-8", errors="replace") as output:
        while True:
            chunk = pipe.readline()
            if chunk == "":
                break
            sink.append(chunk)
            output.write(chunk)
            output.flush()


def run_singular_script(
    script_path: Path,
    output_prefix: Path,
    config: RunConfig,
    cpus: int,
) -> tuple[list[str], str, str, int | None, bool, float]:
    """Run Singular under ``stdbuf -oL`` and stream stdout/stderr to disk."""

    env = os.environ.copy()
    thread_count = str(max(1, cpus))
    for key in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
    ):
        env[key] = thread_count

    cmd = [
        "stdbuf",
        "-oL",
        "-eL",
        config.singular,
        f"--cpus={cpus}",
        f"--threads={cpus}",
        f"--flint-threads={cpus}",
    ]
    if config.no_rc:
        cmd.append("--no-rc")
    cmd.extend(["-q", str(script_path)])

    stdout_path = output_prefix.with_suffix(".out")
    stderr_path = output_prefix.with_suffix(".err")
    stdout_chunks: list[str] = []
    stderr_chunks: list[str] = []
    started = time.monotonic()
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        env=env,
        start_new_session=True,
    )
    assert process.stdout is not None
    assert process.stderr is not None
    threads = [
        threading.Thread(
            target=_stream_pipe,
            args=(process.stdout, stdout_path, stdout_chunks),
            daemon=True,
        ),
        threading.Thread(
            target=_stream_pipe,
            args=(process.stderr, stderr_path, stderr_chunks),
            daemon=True,
        ),
    ]
    for thread in threads:
        thread.start()
    timed_out = False
    returncode: int | None
    try:
        returncode = process.wait(timeout=config.timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            returncode = process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            returncode = process.wait()
    for thread in threads:
        thread.join(timeout=5)
    elapsed = time.monotonic() - started
    return cmd, "".join(stdout_chunks), "".join(stderr_chunks), returncode, timed_out, elapsed


def _parse_int_token(value: str) -> int | None:
    value = value.strip()
    if value in {"NA", "NONTERMINATING", ""}:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def parse_marker_controls(stdout: str, run_id: str) -> RunControls:
    controls = RunControls()
    markers: dict[str, str] = {}
    nf_seen = False
    pattern = re.compile(rf"^GG__([A-Z0-9_]+) {re.escape(run_id)}(?: (.*))?$")
    for line in stdout.splitlines():
        match = pattern.match(line.strip())
        if not match:
            continue
        key = match.group(1)
        rest = (match.group(2) or "").strip()
        markers[key] = rest
        if key == "NF_ALL_ZERO":
            controls.nf_all_zero = rest == "1"
        elif key == "UNIT":
            controls.unit = rest == "1"
        elif key == "DIM":
            controls.dimension = _parse_int_token(rest)
        elif key == "VDIM":
            controls.vdim = _parse_int_token(rest)
        elif key == "BASIS_SIZE":
            controls.basis_size = _parse_int_token(rest)
        elif key == "LEAD_DIM":
            controls.lead_dim = _parse_int_token(rest)
        elif key == "LEAD_VDIM":
            controls.lead_vdim = _parse_int_token(rest)
        elif key == "VDIM_MATCH_PREDICTED":
            controls.vdim_matches_predicted = None if rest == "NA" else rest == "1"
        elif key == "ACCEPT":
            controls.accepted = rest == "1"
        elif key == "NF_ZERO":
            nf_seen = True
    required = ["NF_ALL_ZERO", "UNIT", "DIM", "BASIS_SIZE", "LEAD_DIM", "ACCEPT"]
    controls.missing_markers = [key for key in required if key not in markers]
    if not nf_seen:
        controls.missing_markers.append("NF_ZERO")
    return controls


def parse_perturbed_failed(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        if line.strip().startswith("GG__PERTURBED_FAILED control "):
            return line.strip().endswith(" 1")
    return None


def run_one(
    system: SingularSystem,
    hint: HilbertHint | None,
    policy: PromotionPolicy,
    config: RunConfig,
    cpus: int,
) -> SingularRunResult:
    config.output_dir.mkdir(parents=True, exist_ok=True)
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", system.name).strip("_") or "guided"
    suffix = "Q" if system.characteristic == 0 else f"p{system.characteristic}"
    prefix = config.output_dir / f"{stem}_{suffix}"
    script_path = prefix.with_suffix(".sing")
    script = emit_guided_script(
        system,
        hint,
        include_perturbed_control=(hint is not None and config.run_perturbed_control),
    )
    atomic_write(script_path, script)
    command, stdout, stderr, returncode, timed_out, elapsed = run_singular_script(
        script_path,
        prefix,
        config,
        cpus,
    )
    main = parse_marker_controls(stdout, "main")
    perturbed = (
        parse_marker_controls(stdout, "perturbed")
        if hint is not None and config.run_perturbed_control
        else None
    )
    result = SingularRunResult(
        label=system.name,
        characteristic=system.characteristic,
        command=command,
        script=str(script_path),
        stdout=str(prefix.with_suffix(".out")),
        stderr=str(prefix.with_suffix(".err")),
        returncode=returncode,
        elapsed_seconds=round(elapsed, 6),
        timed_out=timed_out,
        main=main,
        perturbed=perturbed,
        stdout_sha256=sha256_file(prefix.with_suffix(".out")),
        stderr_sha256=sha256_file(prefix.with_suffix(".err")),
        script_sha256=sha256_file(script_path),
    )
    json_path = prefix.with_suffix(".guided.json")
    atomic_write(json_path, json.dumps(result.to_json(), indent=2, sort_keys=True) + "\n")
    return result


def _controls_accepted(
    run: SingularRunResult,
    hint: HilbertHint | None,
    policy: PromotionPolicy,
    require_perturbed: bool,
) -> bool:
    if run.timed_out or run.returncode != 0:
        return False
    main = run.main
    if policy.require_controls and main.missing_markers:
        return False
    if not main.accepted or not main.nf_all_zero:
        return False
    if hint is not None and hint.predicted_length is not None:
        if main.lead_dim != 0 or main.lead_vdim != hint.predicted_length:
            return False
        if main.vdim_matches_predicted is not True:
            return False
    if require_perturbed and hint is not None:
        failed = parse_perturbed_failed(Path(run.stdout).read_text(encoding="utf-8", errors="replace"))
        if failed is not True:
            return False
    return True


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """Combine two congruences, returning ``(residue, modulus)``."""

    g = math.gcd(m, n)
    if (b - a) % g:
        raise ValueError("inconsistent residues")
    m1 = m // g
    n1 = n // g
    inv = pow(m1, -1, n1)
    t = ((b - a) // g * inv) % n1
    modulus = m * n1
    return (a + m * t) % modulus, modulus


def crt_many(items: Iterable[tuple[int, int]]) -> tuple[int, int]:
    iterator = iter(items)
    try:
        residue, modulus = next(iterator)
    except StopIteration as exc:
        raise ValueError("empty CRT input") from exc
    for next_residue, next_modulus in iterator:
        residue, modulus = crt_pair(residue, modulus, next_residue, next_modulus)
    return residue, modulus


def rational_reconstruct(
    residue: int,
    modulus: int,
    max_numerator: int | None = None,
    max_denominator: int | None = None,
) -> Fraction | None:
    """Small rational reconstruction by bounded denominator scan."""

    if modulus <= 1:
        raise ValueError("modulus must be > 1")
    residue %= modulus
    default_bound = math.isqrt(max(1, (modulus - 1) // 2))
    max_numerator = default_bound if max_numerator is None else max_numerator
    max_denominator = default_bound if max_denominator is None else max_denominator
    for denominator in range(1, max_denominator + 1):
        numerator = (residue * denominator) % modulus
        if numerator > modulus // 2:
            numerator -= modulus
        if abs(numerator) <= max_numerator and math.gcd(numerator, denominator) == 1:
            return Fraction(numerator, denominator)
    return None


def reconstruct_invariants(runs: Sequence[SingularRunResult]) -> dict[str, Any]:
    """CRT/rational-reconstruct small integer invariants from modular runs."""

    modular = [run for run in runs if run.characteristic > 1 and not run.timed_out]
    out: dict[str, Any] = {
        "method": "CRT plus bounded rational reconstruction for scalar invariants",
        "available": len(modular) >= 2,
        "items": {},
    }
    if len(modular) < 2:
        return out
    for key in ("dimension", "lead_dim", "lead_vdim", "basis_size"):
        residues = []
        for run in modular:
            value = getattr(run.main, key)
            if value is None:
                break
            residues.append((value % run.characteristic, run.characteristic))
        else:
            residue, modulus = crt_many(residues)
            reconstructed = rational_reconstruct(residue, modulus)
            out["items"][key] = {
                "residue": residue,
                "modulus": modulus,
                "rational_reconstruction": (
                    None if reconstructed is None else str(reconstructed)
                ),
                "direct_singular_values": [getattr(run.main, key) for run in modular],
                "direct_values_agree": len({getattr(run.main, key) for run in modular}) == 1,
            }
    return out


def guided_groebner(
    systems: SingularSystem | Sequence[SingularSystem],
    hint: HilbertHint | None = None,
    policy: PromotionPolicy | None = None,
    config: RunConfig | None = None,
) -> GuidedGBResult:
    """Run one or more Singular systems and return a typed verdict.

    Pass multiple systems to run good-prime fibres in parallel.  The aggregate
    verdict is promoted to characteristic zero only by exact-Q computation or by
    the homogeneous/properness policy for modular dimension zero.
    """

    if config is None:
        config = RunConfig(Path("guided-gb-runs"))
    if policy is None:
        policy = PromotionPolicy.exact_q() if _as_list(systems)[0].characteristic == 0 else PromotionPolicy()
    job_list = _as_list(systems)
    max_jobs = config.max_parallel_jobs or min(len(job_list), max(1, config.total_cores))
    max_jobs = max(1, min(max_jobs, len(job_list)))
    cpus = max(1, config.total_cores // max_jobs)

    runs: list[SingularRunResult] = []
    with ThreadPoolExecutor(max_workers=max_jobs) as executor:
        futures = [
            executor.submit(run_one, system, hint, policy, config, cpus)
            for system in job_list
        ]
        for future in as_completed(futures):
            runs.append(future.result())
    runs.sort(key=lambda run: (run.label, run.characteristic))

    require_perturbed = bool(hint is not None and config.run_perturbed_control)
    accepted = [
        run
        for run in runs
        if _controls_accepted(run, hint, policy, require_perturbed)
    ]
    timeouts = [run for run in runs if run.timed_out or run.returncode == 124]
    any_exact = any(run.characteristic == 0 for run in accepted)
    any_modular = any(run.characteristic > 1 for run in accepted)
    all_exact_posdim = (
        bool(runs)
        and all(run.characteristic == 0 for run in runs)
        and all(run.main.dimension is not None and run.main.dimension > 0 for run in runs)
    )

    verdict = Verdict.MODULAR_ONLY
    promotion_note = ""
    if accepted:
        if any(run.characteristic == 0 and run.main.unit for run in accepted):
            verdict = Verdict.UNIT_IDEAL_CHAR0
            promotion_note = "exact Q standard basis reduced 1 to 0"
        elif any(run.characteristic == 0 and run.main.dimension == 0 for run in accepted):
            verdict = Verdict.DIM0_CHAR0
            promotion_note = "exact Q standard basis has dimension zero"
        elif all_exact_posdim:
            verdict = Verdict.POSDIM
            promotion_note = "exact Q standard basis has positive dimension"
        elif any_modular and any(run.main.dimension == 0 for run in accepted):
            if _properness_allowed(job_list, policy):
                verdict = Verdict.DIM0_CHAR0
                promotion_note = (
                    "modular dimension zero promoted only for a homogeneous "
                    "positive-weight ideal by the properness scope"
                )
            else:
                verdict = Verdict.MODULAR_ONLY
                promotion_note = "modular dimension zero lacks declared properness scope"
        elif any(run.main.unit for run in accepted):
            if policy.allow_modular_unit_promotion and _properness_allowed(job_list, policy):
                verdict = Verdict.UNIT_IDEAL_CHAR0
                promotion_note = "modular unit promoted under explicit caller policy"
            else:
                verdict = Verdict.MODULAR_ONLY
                promotion_note = "modular unit ideal was not promoted to characteristic zero"
    elif all_exact_posdim:
        verdict = Verdict.POSDIM
        promotion_note = "exact Q standard basis has positive dimension"
    elif timeouts:
        verdict = Verdict.INCONCLUSIVE_TIMEOUT
        promotion_note = "no accepted result before timeout"
    else:
        verdict = Verdict.MODULAR_ONLY
        promotion_note = "controls did not accept a characteristic-zero conclusion"

    certificate = {
        "policy": {
            "scope": policy.scope.value,
            "require_controls": policy.require_controls,
            "allow_modular_unit_promotion": policy.allow_modular_unit_promotion,
            "note": policy.note,
        },
        "properness_scope": {
            "statement": (
                "A modular dimension-zero result for an ideal homogeneous in "
                "positive weights certifies characteristic-zero dimension zero "
                "through the properness lemma.  A modular positive-dimensional "
                "result proves no characteristic-zero statement.  A modular "
                "unit ideal is not promoted unless exact-Q or an explicit "
                "caller policy supplies the missing scope."
            ),
            "systems_declared_homogeneous": all(system.homogeneous for system in job_list),
            "positive_weights": [list(system.positive_weights) for system in job_list],
        },
        "promotion_note": promotion_note,
        "hilbert_hint": None
        if hint is None
        else {
            "numerator_sha256": sha256_text(json.dumps(list(hint.numerator))),
            "weights": list(hint.weights),
            "predicted_length": hint.predicted_length,
            "perturbed_control": config.run_perturbed_control,
        },
        "runs": [run.to_json() for run in runs],
        "accepted_run_count": len(accepted),
        "crt_rational_reconstruction": reconstruct_invariants(runs),
    }
    result = GuidedGBResult(verdict, certificate)
    config.output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write(
        config.output_dir / "guided_gb_result.json",
        json.dumps(result.to_json(), indent=2, sort_keys=True) + "\n",
    )
    return result


def _as_list(systems: SingularSystem | Sequence[SingularSystem]) -> list[SingularSystem]:
    if isinstance(systems, SingularSystem):
        return [systems]
    return list(systems)


def _properness_allowed(systems: Sequence[SingularSystem], policy: PromotionPolicy) -> bool:
    if policy.scope != PromotionScope.HOMOGENEOUS_POSITIVE_WEIGHTS_PROPERNESS:
        return False
    return all(system.homogeneous and all(weight > 0 for weight in system.positive_weights) for system in systems)


def cli() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prelude", type=Path, required=True)
    parser.add_argument("--generators", required=True, help="comma-separated generator names")
    parser.add_argument("--name", default="guided")
    parser.add_argument("--char", type=int, default=0)
    parser.add_argument("--weights", help="comma-separated Hilbert weights")
    parser.add_argument("--hnum", help="comma-separated Hilbert numerator")
    parser.add_argument("--length", type=int)
    parser.add_argument("--homogeneous", action="store_true")
    parser.add_argument("--properness", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()

    hint = None
    if args.hnum or args.weights or args.length is not None:
        if not (args.hnum and args.weights):
            raise SystemExit("--hnum and --weights are both required for a Hilbert hint")
        hint = HilbertHint(
            tuple(int(piece) for piece in args.hnum.split(",") if piece),
            tuple(int(piece) for piece in args.weights.split(",") if piece),
            args.length,
        )
    weights = tuple(int(piece) for piece in args.weights.split(",") if piece) if args.weights else ()
    system = SingularSystem(
        name=args.name,
        prelude=args.prelude.read_text(encoding="utf-8"),
        generators=tuple(piece.strip() for piece in args.generators.split(",") if piece.strip()),
        characteristic=args.char,
        homogeneous=args.homogeneous,
        positive_weights=weights,
    )
    policy = (
        PromotionPolicy.homogeneous_properness()
        if args.properness
        else PromotionPolicy.exact_q()
    )
    result = guided_groebner(
        system,
        hint=hint,
        policy=policy,
        config=RunConfig(args.output_dir, timeout_seconds=args.timeout),
    )
    print(json.dumps(result.to_json(), indent=2, sort_keys=True))


if __name__ == "__main__":
    cli()

