#!/usr/bin/env python3
"""Run and replay one exact Singular R4-00 packet on registered AWS.

The first Singular process proposes either a unit cofactor or a tracked proper
standard basis.  A fresh second process re-parses the serialized artifact and
replays the exact polynomial identity.  No msolve unit basis is consumed.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


FORMAT = "K00_R400_EXACT_PACKET_V1"
STATUS_UNIT = "EXACT_Q_UNIT_IDENTITY_REPLAYED_CELL_EMPTY_PRODUCER_UNREVIEWED"
STATUS_PROPER = "EXACT_Q_PROPER_IDEAL_WITH_ENCODED_OPENS_PRODUCER_UNREVIEWED"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("R4-00 exact worker refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("R4-00 exact worker refused non-Amazon EC2 host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe path", value))
    return value


def run_singular(executable: str, script: Path, cwd: Path, stdout: Path,
                 stderr: Path, timeout: int) -> str:
    try:
        completed = subprocess.run(
            [executable, "-q", str(script)], cwd=cwd, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        stdout.write_text(error.stdout or "")
        stderr.write_text(error.stderr or "")
        raise
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    lowered = completed.stderr.lower()
    diagnostics = ("error", "halt", "segment", "out of memory", "killed")
    if completed.returncode != 0 or any(marker in lowered for marker in diagnostics):
        fail(("Singular failure", completed.returncode, completed.stdout[-3000:], completed.stderr[-3000:]))
    if "K00_R400_FAIL=" in completed.stdout:
        fail(("Singular fail-closed marker", completed.stdout[-4000:]))
    return completed.stdout


def definitions(packet: dict, ideal_name: str = "J") -> list[str]:
    variables = packet.get("variables")
    generators = packet.get("generators")
    if not isinstance(variables, list) or not variables or not all(isinstance(item, str) for item in variables):
        fail("malformed packet variables")
    if not isinstance(generators, list) or not generators:
        fail("malformed packet generators")
    if any(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", item) is None for item in variables):
        fail("unsafe packet variable")
    polynomials = []
    for item in generators:
        if not isinstance(item, dict) or not isinstance(item.get("singular"), str) or not item["singular"]:
            fail("malformed packet generator")
        if sha256((item["singular"] + "\n").encode()).hexdigest() != item.get("sha256"):
            fail(("packet generator digest mismatch", item.get("label")))
        polynomials.append(item["singular"])
    return [
        f"ring R=0,({','.join(variables)}),dp;",
        f"ideal {ideal_name}=" + ",\n".join(f"({poly})" for poly in polynomials) + ";",
    ]


def control_lines(variable_name: str) -> list[str]:
    return [
        f"ideal CTRLproper={variable_name}; ideal GCTRLproper=std(CTRLproper);",
        'if (reduce(1,GCTRLproper)==0) { print("K00_R400_FAIL=KNOWN_PROPER_CONTROL"); quit; }',
        f"ideal CTRLunit={variable_name},1; ideal GCTRLunit=std(CTRLunit);",
        'if (reduce(1,GCTRLunit)!=0) { print("K00_R400_FAIL=FORCED_UNIT_CONTROL"); quit; }',
        'print("K00_R400_CONTROLS=PASS");',
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("packet", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=43200)
    args = parser.parse_args()
    lane = require_aws()
    packet_path = args.packet.resolve()
    if not packet_path.is_file():
        fail(("packet missing", str(packet_path)))
    packet = json.loads(packet_path.read_text())
    if packet.get("format") != FORMAT or packet.get("characteristic") != 0:
        fail(("packet format/characteristic", packet.get("format"), packet.get("characteristic")))
    if "OPEN" not in " ".join(str(item.get("label")) for item in packet.get("generators", [])):
        fail("packet has no encoded open equation")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing on registered AWS host")

    generator_count = len(packet["generators"])
    basis_path = output / "EXACT_STANDARD_BASIS.txt"
    transform_path = output / "EXACT_LIFTSTD_TRANSFORM.matrix"
    unit_path = output / "EXACT_UNIT_COEFFICIENTS.matrix"
    producer = output / "producer.sing"
    producer.write_text("\n".join(definitions(packet) + control_lines(packet["variables"][0]) + [
        "ideal G0=slimgb(J); poly N0=reduce(1,G0); int D0=dim(G0);",
        'print("K00_R400_PREFLIGHT_DIM="+string(D0));',
        "if (N0==0)",
        "{",
        '  print("K00_R400_PREFLIGHT=UNIT");',
        '  matrix U; matrix C=lift(J,ideal(1),U,"slimgb");',
        f'  if ((nrows(C)!={generator_count})||(ncols(C)!=1)||(nrows(U)!=1)||(ncols(U)!=1)) {{ print("K00_R400_FAIL=UNIT_LIFT_SHAPE"); quit; }}',
        '  if (U[1,1]!=1) { print("K00_R400_FAIL=UNIT_LIFT_U"); quit; }',
        '  matrix UID=matrix(J)*C-matrix(ideal(1)); if (UID!=0) { print("K00_R400_FAIL=UNIT_IDENTITY"); quit; }',
        "  int pick=0; int rr; for (rr=1;rr<=nrows(C);rr++) { if ((pick==0)&&(J[rr]!=0)&&(C[rr,1]!=0)) { pick=rr; } }",
        '  if (pick==0) { print("K00_R400_FAIL=UNIT_MUTATION_PICK"); quit; }',
        '  matrix CDROP=C; CDROP[pick,1]=0; if (matrix(J)*CDROP-matrix(ideal(1))==0) { print("K00_R400_FAIL=UNIT_DROP_MUTATION"); quit; }',
        f'  write("{qpath(unit_path)}",string(C));',
        '  print("K00_R400_UNIT_PICK="+string(pick)); print("K00_R400_BRANCH=UNIT"); quit;',
        "}",
        'if ((N0!=1)||(D0<0)) { print("K00_R400_FAIL=PREFLIGHT_PROPER_MARKERS"); quit; }',
        'print("K00_R400_PREFLIGHT=PROPER");',
        "matrix T; ideal G=liftstd(J,T);",
        f'if ((nrows(T)!={generator_count})||(ncols(T)!=size(G))) {{ print("K00_R400_FAIL=TRACKED_SHAPE"); quit; }}',
        'matrix TREPLAY=matrix(J)*T-matrix(G); if (TREPLAY!=0) { print("K00_R400_FAIL=TRACKED_IDENTITY"); quit; }',
        'poly N1=reduce(1,G); int D1=dim(G); if ((N1!=1)||(D1!=D0)||(D1<0)) { print("K00_R400_FAIL=TRACKED_PROPER_MARKERS"); quit; }',
        "int pickr=0; int pickc=0; int cc; int rr; for (cc=1;cc<=ncols(T);cc++) { for (rr=1;rr<=nrows(T);rr++) { if ((pickr==0)&&(J[rr]!=0)&&(T[rr,cc]!=0)) { pickr=rr; pickc=cc; } } }",
        'if (pickr==0) { print("K00_R400_FAIL=TRACKED_MUTATION_PICK"); quit; }',
        'matrix TBAD=T; TBAD[pickr,pickc]=0; if (matrix(J)*TBAD-matrix(G)==0) { print("K00_R400_FAIL=TRACKED_DROP_MUTATION"); quit; }',
        f'write("{qpath(basis_path)}",string(G)); write("{qpath(transform_path)}",string(T));',
        'print("K00_R400_PROPER_GSIZE="+string(size(G))); print("K00_R400_PROPER_PICKR="+string(pickr)); print("K00_R400_PROPER_PICKC="+string(pickc)); print("K00_R400_BRANCH=PROPER"); quit;',
    ]) + "\n")

    producer_stdout = output / "producer.stdout"
    producer_stderr = output / "producer.stderr"
    try:
        text = run_singular(singular, producer, output, producer_stdout, producer_stderr, args.timeout)
    except subprocess.TimeoutExpired:
        result = {
            "status": "RESOURCE_CAP_NO_VERDICT",
            "registered_aws_lane": lane,
            "packet_id": packet.get("packet_id"),
            "packet_sha256": digest(packet_path),
            "stage": "PRODUCER",
            "timeout_seconds": args.timeout,
            "scope": "NO_CELL_VERDICT",
        }
        (output / "RESULT.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        print("K00_R400_EXACT_ENDPOINT=RESOURCE_CAP_NO_VERDICT")
        return
    if "K00_R400_CONTROLS=PASS" not in text:
        fail("producer controls marker missing")
    dim_match = re.search(r"K00_R400_PREFLIGHT_DIM=(-?\d+)", text)
    if dim_match is None:
        fail("producer dimension marker missing")
    dimension = int(dim_match.group(1))

    replay = output / "replay.sing"
    if "K00_R400_BRANCH=UNIT" in text:
        pick_match = re.search(r"K00_R400_UNIT_PICK=(\d+)", text)
        if pick_match is None or not unit_path.is_file() or not unit_path.read_text().strip():
            fail("unit artifact custody missing")
        pick = int(pick_match.group(1))
        replay.write_text("\n".join(definitions(packet) + [
            f"matrix C[{generator_count}][1]={unit_path.read_text().strip()};",
            'matrix UID=matrix(J)*C-matrix(ideal(1)); if (UID!=0) { print("K00_R400_FAIL=SERIALIZED_UNIT_IDENTITY"); quit; }',
            f"matrix CDROP=C; CDROP[{pick},1]=0;",
            'if (matrix(J)*CDROP-matrix(ideal(1))==0) { print("K00_R400_FAIL=SERIALIZED_UNIT_MUTATION"); quit; }',
            'print("K00_R400_SECOND_PROCESS=UNIT_REPLAY_PASS"); quit;',
        ]) + "\n")
        status = STATUS_UNIT
        replay_marker = "K00_R400_SECOND_PROCESS=UNIT_REPLAY_PASS"
        certificate = {"kind": "UNIT_COEFFICIENTS", "path": unit_path.name, "sha256": digest(unit_path), "mutation_index": pick}
    elif "K00_R400_BRANCH=PROPER" in text:
        matches = {
            name: re.search(rf"K00_R400_PROPER_{name}=(\d+)", text)
            for name in ("GSIZE", "PICKR", "PICKC")
        }
        if any(value is None for value in matches.values()) or not basis_path.is_file() or not transform_path.is_file():
            fail("proper artifact custody missing")
        values = {name: int(match.group(1)) for name, match in matches.items() if match is not None}
        replay.write_text("\n".join(definitions(packet) + [
            f"ideal Graw={basis_path.read_text().strip()};",
            f"matrix T[{generator_count}][{values['GSIZE']}]={transform_path.read_text().strip()};",
            'matrix TREPLAY=matrix(J)*T-matrix(Graw); if (TREPLAY!=0) { print("K00_R400_FAIL=SERIALIZED_TRACKED_IDENTITY"); quit; }',
            "ideal G=std(Graw); poly N1=reduce(1,G); int D1=dim(G);",
            f'if ((N1!=1)||(D1!={dimension})||(D1<0)) {{ print("K00_R400_FAIL=SERIALIZED_PROPER_MARKERS"); quit; }}',
            f"matrix TBAD=T; TBAD[{values['PICKR']},{values['PICKC']}]=0;",
            'if (matrix(J)*TBAD-matrix(Graw)==0) { print("K00_R400_FAIL=SERIALIZED_TRACKED_MUTATION"); quit; }',
            'ideal JUNIT=J,1; if (reduce(1,std(JUNIT))!=0) { print("K00_R400_FAIL=FORCED_UNIT_MUTATION"); quit; }',
            'print("K00_R400_SECOND_PROCESS=PROPER_REPLAY_PASS"); quit;',
        ]) + "\n")
        status = STATUS_PROPER
        replay_marker = "K00_R400_SECOND_PROCESS=PROPER_REPLAY_PASS"
        certificate = {
            "kind": "TRACKED_PROPER_STANDARD_BASIS",
            "basis": {"path": basis_path.name, "sha256": digest(basis_path)},
            "transform": {"path": transform_path.name, "sha256": digest(transform_path)},
            "mutation_entry": [values["PICKR"], values["PICKC"]],
        }
    else:
        fail("producer branch marker missing")

    replay_stdout = output / "replay.stdout"
    replay_stderr = output / "replay.stderr"
    try:
        replay_text = run_singular(singular, replay, output, replay_stdout, replay_stderr, min(args.timeout, 7200))
    except subprocess.TimeoutExpired:
        result = {
            "status": "RESOURCE_CAP_NO_VERDICT",
            "registered_aws_lane": lane,
            "packet_id": packet.get("packet_id"),
            "packet_sha256": digest(packet_path),
            "stage": "SECOND_PROCESS_REPLAY",
            "timeout_seconds": min(args.timeout, 7200),
            "scope": "NO_CELL_VERDICT",
        }
        (output / "RESULT.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        print("K00_R400_EXACT_ENDPOINT=RESOURCE_CAP_NO_VERDICT")
        return
    if replay_marker not in replay_text:
        fail("second-process replay marker missing")

    result = {
        "status": status,
        "registered_aws_lane": lane,
        "packet_id": packet.get("packet_id"),
        "route": packet.get("route"),
        "packet_sha256": digest(packet_path),
        "packet_source_sha256": packet.get("source_sha256"),
        "dimension": dimension,
        "encoded_opens_checked_inside_ideal": True,
        "second_process_replay": True,
        "certificate": certificate,
        "epistemic_scope": (
            "Exact-Q polynomial ideal with Rabinowitsch opens. Empty only on replayed unit identity; "
            "proper means algebraic-closure point for this packet. Full residual packets include Jdet open."
        ),
        "firewall": "FINITE_FIELD_VALUED_JETS_ONLY_NO_ARC_MAP_ATTAINMENT_OR_JC2_CLAIM",
        "lifecycle": "PRODUCER_UNREVIEWED",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    artifacts = [path for path in sorted(output.iterdir()) if path.is_file() and path.name != "EVIDENCE.sha256"]
    (output / "EVIDENCE.sha256").write_text("".join(f"{digest(path)}  {path.name}\n" for path in artifacts))
    print(f"K00_R400_EXACT_ENDPOINT={status}")
    print(canonical_json(result), end="")


if __name__ == "__main__":
    main()
