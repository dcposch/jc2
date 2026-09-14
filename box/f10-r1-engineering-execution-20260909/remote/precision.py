import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize
authority = authorize(sys.argv[1], __file__, "check")
import json, copy
from checker import verify, InvalidArtifact
data = json.loads(Path(sys.argv[2]).read_text())
verify(data)
large = 2**80 + 1
wire = json.dumps({"coefficient": str(large)})
if int(json.loads(wire)["coefficient"]) != large or int(float(large)) == large:
    raise RuntimeError("precision attack precondition failed")
changed = copy.deepcopy(data)
changed["rows"][-1]["polynomial"][0][1] = float(large)
try:
    verify(changed)
except InvalidArtifact as exc:
    reason = str(exc)
else:
    raise RuntimeError("float wire passed")
Path(sys.argv[3]).open("x").write(json.dumps({"authority":authority,"large_integer":str(large),
    "string_roundtrip":"EXACT","float_roundtrip_integer":str(int(float(large))),
    "changed_payload":"REJECTED","reason":reason}) + "\n")
