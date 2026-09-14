import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize
authority = authorize(sys.argv[1], __file__, "check")
import json, copy, hashlib
from checker import verify, InvalidArtifact
raw = Path(sys.argv[2]).read_bytes()
data = json.loads(raw)
verify(data)
guard_constant = [[0] * 12, "-1", "1"]
if data["rows"][-1]["polynomial"][0] != guard_constant:
    raise RuntimeError("guard constant mutation precondition failed")
large = -(2**80 + 1)
rounded = int(float(large))
rounded_string = str(rounded)
if rounded == large or abs(rounded) <= 2**53 or str(int(rounded_string)) != rounded_string:
    raise RuntimeError("genuine large-integer rounding precondition failed")
float_case = copy.deepcopy(data)
float_case["rows"][-1]["polynomial"][0][1] = float(large)
try:
    verify(float_case)
except InvalidArtifact as exc:
    float_reason = str(exc)
    if float_reason != "floating point anywhere in artifact":
        raise RuntimeError("unexpected float-type rejection path")
else:
    raise RuntimeError("float wire passed")
string_case = copy.deepcopy(data)
string_case["rows"][-1]["polynomial"][0][1] = rounded_string
try:
    verify(string_case)
except InvalidArtifact as exc:
    string_reason = str(exc)
    if string_reason != "full guard row":
        raise RuntimeError("rounded canonical string did not reach the exact guard comparison")
else:
    raise RuntimeError("rounded integer disguised as canonical string passed")
Path(sys.argv[3]).open("x").write(json.dumps({
    "authority": authority,
    "artifact_sha256": hashlib.sha256(raw).hexdigest(),
    "synthetic_exact_integer": str(large),
    "synthetic_rounded_integer": rounded_string,
    "rounding_precondition": "DIFFERENT_AND_MAGNITUDE_ABOVE_2^53",
    "float_type_rejection": float_reason,
    "rounded_string_identity_rejection": string_reason,
    "scope": "Two changed guard payloads, not generic JSON roundtrip or positive large-coefficient parser fidelity"
}) + "\n")
