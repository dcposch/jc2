"""SOURCE ONLY; UNEXECUTED. Fixed child bridge, not an authority issuer.

Future authorized CLI: /usr/bin/python3 -I -B payload_exec.py AUTHORITY INPUT MODE
MODE is exactly produce/check/mutate. ROOT owns every launch and CAPRUN cap.
Fixed payloads and execution_gate.py must be staged as pinned siblings.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

GATE_SHA = "cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6"
PRODUCER_SHA = "3c4f18e6a7d0d63b0f3dfa539eca41712ba39f3204907b0e35badaced0b67d04"
CHECKER_SHA = "2e0dda86514a0cdb2aa0a86acf3f32de72645f6566f80a77596b1394a3c9fca7"
RUNNER_SHA = "4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2"
PYTHON = "/usr/bin/python3"
SINGULAR = "/usr/bin/Singular"


def digest(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def canonical_argument(value):
    path = Path(value)
    resolved = path.resolve(strict=True)
    if not path.is_absolute() or str(resolved) != value or not resolved.is_file():
        raise RuntimeError("require canonical absolute regular-file argument")
    return resolved


def main():
    if sys.platform != "linux":
        raise RuntimeError("Linux only")
    if len(sys.argv) != 4 or sys.argv[3] not in ("produce", "check", "mutate"):
        raise RuntimeError("usage: payload_exec.py AUTHORITY INPUT produce|check|mutate")
    if not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise RuntimeError("require Python -I -B")
    authority = canonical_argument(sys.argv[1])
    input_path = canonical_argument(sys.argv[2])
    mode = sys.argv[3]
    script = Path(__file__).resolve(strict=True)
    base = script.parent
    gate_path = base / "execution_gate.py"
    if gate_path.is_symlink() or digest(gate_path) != GATE_SHA:
        raise RuntimeError("execution gate source pin mismatch before import")
    module_spec = importlib.util.spec_from_file_location("contact_execution_gate", gate_path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError("cannot load pinned metadata gate")
    gate = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(gate)  # Only admitted metadata code.
    receipt = gate.authorize(str(authority), str(script), mode)

    # Bind the reread used for selected-file admission to the gate receipt.
    with authority.open("rb") as stream:
        raw_authority = stream.read(65537)
    if (len(raw_authority) > 65536 or
            hashlib.sha256(raw_authority).hexdigest() != receipt["authority_sha256"]):
        raise RuntimeError("authority reread differs from authorize receipt")
    registration = json.loads(raw_authority)
    if registration.get("operation") != mode:
        raise RuntimeError("mode changed in authority")
    files = registration["file_sha256"]
    selected = {}

    def require_pin(path, fixed_sha=None):
        key = str(path)
        expected = files.get(key)
        if not isinstance(expected, str) or len(expected) != 64:
            raise RuntimeError("selected file not explicitly registered: " + key)
        if fixed_sha is not None and expected != fixed_sha:
            raise RuntimeError("selected accepted source pin changed: " + key)
        if digest(path) != expected:
            raise RuntimeError("selected file changed after authorization: " + key)
        selected[key] = expected
        return expected

    def sibling(name, fixed_sha=None):
        path = base / name
        if path.is_symlink() or not path.is_file():
            raise RuntimeError("payload must be a regular nonsymlink sibling: " + name)
        require_pin(path, fixed_sha)
        return path

    def native(path):
        # Pin both the exact invocation name and resolved target if different.
        invoked = Path(path)
        resolved = invoked.resolve(strict=True)
        if not resolved.is_file() or not os.access(invoked, os.X_OK):
            raise RuntimeError("selected native executable unavailable")
        require_pin(invoked)
        if resolved != invoked:
            require_pin(resolved)

    require_pin(script)
    require_pin(gate_path, GATE_SHA)
    require_pin(Path(registration["runner_path"]).resolve(strict=True), RUNNER_SHA)
    native(PYTHON)
    registered_input_sha = require_pin(input_path)
    cwd = Path.cwd().resolve(strict=True)
    outputs = []
    if mode == "produce":
        payload = sibling("produce.sing", PRODUCER_SHA)
        if input_path != payload:
            raise RuntimeError("produce INPUT must be the fixed sibling produce.sing")
        native(SINGULAR)
        argv = [SINGULAR, "-q", "--no-rc", "--no-stdlib", "--no-tty",
                "--random=0", str(payload)]
        outputs = [cwd / "contact-eliminant.cert"]
    elif mode == "check":
        payload = sibling("check_certificate.py", CHECKER_SHA)
        argv = [PYTHON, "-I", "-B", str(payload), str(input_path)]
    else:
        payload = sibling("mutate_certificate.py")
        sibling("check_certificate.py", CHECKER_SHA)
        if input_path.parent != cwd:
            raise RuntimeError("mutate INPUT must be in the registered fresh cwd")
        argv = [PYTHON, "-I", "-B", str(payload), str(input_path)]
        outputs = [input_path.parent / "contact-F-plus-one.cert",
                   input_path.parent / "contact-H4-plus-one.cert"]
        # Data binding only, NOT a new authority or a standalone capability.
        os.environ["JC2_CONTACT_BRIDGE_MODE"] = "mutate"
        os.environ["JC2_CONTACT_INPUT_SHA256"] = registered_input_sha
        os.environ["JC2_CONTACT_AUTHORITY_SHA256"] = receipt["authority_sha256"]
    for output in outputs:
        if os.path.lexists(output):
            raise RuntimeError("output must be absent before exec: " + str(output))
    print(json.dumps({"event": "CONTACT_AUTHORIZED_EXEC", "mode": mode,
                      "hostname": receipt["hostname"], "instance_id": receipt["instance_id"],
                      "job_tag": receipt["job_tag"],
                      "authority_sha256": receipt["authority_sha256"],
                      "pid": os.getpid(), "pgid": os.getpgrp(),
                      "exec_argv": argv, "selected_sha256": selected}, sort_keys=True), flush=True)
    sys.stdout.flush()
    sys.stderr.flush()
    os.execv(argv[0], argv)  # Replace the recorded child; no fork or PGID change.


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("CONTACT_BRIDGE_REFUSE " + str(error), file=sys.stderr, flush=True)
        raise SystemExit(2)
