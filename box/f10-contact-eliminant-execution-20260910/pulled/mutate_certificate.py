"""SOURCE ONLY; no execution/fixture. Payload downstream of payload_exec.py.

Not independently runnable authority. ROOT must first obtain an independent
positive CLI checker result and separately authorize this mutation launch.
Environment SHA fields transport the wrapper's admitted data binding only;
they are not an authorization token and do not license a direct invocation.
"""
import hashlib
import importlib.util
import os
from pathlib import Path
import re
import sys

CHECKER_SHA = "2e0dda86514a0cdb2aa0a86acf3f32de72645f6566f80a77596b1394a3c9fca7"
MAX_BYTES = 64 * 1024 * 1024
NAMES = ("F", "H1", "H2", "H3", "H4")


def main():
    if sys.platform != "linux" or not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise RuntimeError("require admitted Linux Python -I -B payload")
    if len(sys.argv) != 2 or os.environ.get("JC2_CONTACT_BRIDGE_MODE") != "mutate":
        raise RuntimeError("mutator is only an admitted bridge payload")
    expected_input = os.environ.get("JC2_CONTACT_INPUT_SHA256", "")
    authority_sha = os.environ.get("JC2_CONTACT_AUTHORITY_SHA256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", expected_input) or not re.fullmatch(r"[0-9a-f]{64}", authority_sha):
        raise RuntimeError("missing transported admitted SHA binding")
    input_path = Path(sys.argv[1]).resolve(strict=True)
    if str(input_path) != sys.argv[1] or input_path.parent != Path.cwd().resolve():
        raise RuntimeError("require admitted canonical input in fresh cwd")
    with input_path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES or hashlib.sha256(raw).hexdigest() != expected_input:
        raise RuntimeError("input size/pin differs from admitted bytes")
    targets = [input_path.parent / "contact-F-plus-one.cert",
               input_path.parent / "contact-H4-plus-one.cert"]
    if any(os.path.lexists(path) for path in targets):
        raise RuntimeError("both mutation output paths must be absent")

    # All scientific imports are in this payload, downstream of authorization.
    # Pin the unchanged parser/Poly before importing it; no producer imports.
    checker_path = Path(__file__).resolve().parent / "check_certificate.py"
    if checker_path.is_symlink() or hashlib.sha256(checker_path.read_bytes()).hexdigest() != CHECKER_SHA:
        raise RuntimeError("independent parser source changed")
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)  # Before parser int()/str(), including readback.
    module_spec = importlib.util.spec_from_file_location("contact_exact_parser", checker_path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError("cannot import admitted exact parser")
    parser = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(parser)
    source = parser.parse_certificate(raw)
    # No call to parser.check(raw): positive evidence must come from ROOT's
    # separately authorized fresh checker CLI, not an in-process API call.
    if not source["F"].terms or any(e[:3] != (0, 0, 0) for e in source["F"].terms):
        raise RuntimeError("input must have nonzero F in Q[X]")

    def serialize(polynomials):
        tokens = ["JC2_CONTACT_CERT_V1", "interface", parser.INTERFACE,
                  "gate", parser.GATE, "ring", "Q", "z", "V", "W", "X", "dp",
                  "generators", "I1", "I2", "I3", "I4"]
        for name in NAMES:
            tokens.extend(("poly", name))
            for exponent, coefficient in sorted(polynomials[name].terms.items()):
                tokens.extend(("term", str(coefficient.numerator), str(coefficient.denominator),
                               *(str(value) for value in exponent)))
            tokens.append("endpoly")
        tokens.append("endcert")
        data = ("\n".join(tokens) + "\n").encode("ascii")
        if len(data) > MAX_BYTES:
            raise RuntimeError("mutation exceeds unchanged 64MiB refusal bound")
        return data

    emitted = []
    one = parser.Poly.coerce(1)
    for changed in ("F", "H4"):
        candidate = dict(source)
        candidate[changed] = source[changed] + one
        data = serialize(candidate)
        reread = parser.parse_certificate(data)
        for name in NAMES:
            delta = reread[name] - source[name]
            expected = one if name == changed else parser.Poly()
            if delta.terms != expected.terms:
                raise RuntimeError("retained mutation bytes do not have exact intended delta")
        emitted.append(data)

    # Exclusive creation, never overwrite. A later failure can leave a partial
    # owned output; ROOT must treat the whole run as failed and collect it.
    for target, data in zip(targets, emitted):
        with target.open("xb") as stream:
            stream.write(data)
        with target.open("rb") as stream:
            retained = stream.read(MAX_BYTES + 1)
        if retained != data:
            raise RuntimeError("stored mutation differs from retained bytes")
        parser.parse_certificate(retained)
    print("CONTACT_MUTATIONS_STORED source_sha256=" + expected_input
          + " authority_sha256=" + authority_sha
          + " F_plus_one_sha256=" + hashlib.sha256(emitted[0]).hexdigest()
          + " H4_plus_one_sha256=" + hashlib.sha256(emitted[1]).hexdigest(), flush=True)
    # This is mutation/source-sameness evidence only, never a positive CHECK_OK.


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("CONTACT_MUTATION_FAIL " + str(error), file=sys.stderr, flush=True)
        raise SystemExit(2)
