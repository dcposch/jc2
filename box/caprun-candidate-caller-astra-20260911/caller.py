"""Read supplied metadata; emit one unapplied candidate patch packet."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
# Location-only binding: a flat reviewer may replace these two paths in memory.
# Digests are separate fixed constants and must not be replaced with file hashes.
DEPENDENCY_PATHS = {
    'latebind': HERE.parent / 'caprun-latebinder-code-astra-20260911/latebind.py',
    'stage_patch': HERE.parent / 'caprun-candidate-stage-root-20260911/stage_patch.py',
}
DEPENDENCY_SHA256 = {
    'latebind': 'ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe',
    'stage_patch': 'f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066',
}
FORBIDDEN = '\v\f\x1c\x1d\x1e\x85\u2028\u2029'
MAX_READ = 131072
MAX_PACKET = 8388608


def read_bounded(path):
    with open(path, 'rb') as stream:
        raw = stream.read(MAX_READ + 1)
    if len(raw) > MAX_READ:
        raise ValueError('input size')
    return raw


def dependencies():
    if set(DEPENDENCY_PATHS) != set(DEPENDENCY_SHA256):
        raise ValueError('dependency binding')
    # Both hashes precede either import. ROOT supplies immutable trusted paths;
    # this is not a concurrent-writer or symlink authentication mechanism.
    for name, path in DEPENDENCY_PATHS.items():
        if hashlib.sha256(read_bounded(path)).hexdigest() != DEPENDENCY_SHA256[name]:
            raise ValueError('dependency hash')
    result = {}
    # Read-only caller: helper imports must not create __pycache__ files even
    # when a future invoker forgets -B. This does not execute any input payload.
    sys.dont_write_bytecode = True
    for name, path in DEPENDENCY_PATHS.items():
        spec = importlib.util.spec_from_file_location('candidate_' + name, path)
        if spec is None or spec.loader is None:
            raise ValueError('dependency loader')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result[name] = module
    return result['latebind'], result['stage_patch']


def packet(argv):
    if len(argv) != 6:
        raise ValueError('six arguments required')
    directory, pin_path, obs_path, decision_path, prefix, context = argv
    if context not in ('HISTORICAL_TEST', 'ROOT_ATTESTED_CANDIDATE'):
        raise ValueError('expected context')
    binder, stage = dependencies()
    pins = binder.load(read_bounded(pin_path))
    obs = read_bounded(obs_path)
    decision = read_bounded(decision_path)
    if binder.load(obs).get('context') != context or binder.load(decision).get('context') != context:
        raise ValueError('supplied context')
    bundle = {name: read_bounded(Path(directory) / name) for name in binder.NAMES}
    candidates = binder.bind(bundle, pins, obs, decision)
    if binder.load(candidates['SUMMARY.json']).get('context') != context:
        raise ValueError('candidate context')
    for raw in candidates.values():
        if any(char in raw.decode('utf-8', 'strict') for char in FORBIDDEN):
            raise ValueError('forbidden universal-newline separator')
    answer = stage.make_patch(candidates, prefix)
    if answer['context'] != context:
        raise ValueError('patch context')
    wire = json.dumps(answer, ensure_ascii=True, allow_nan=False, separators=(',', ':')) + '\n'
    if len(wire) > MAX_PACKET:
        raise ValueError('packet size')
    return wire


def main(argv=None):
    try:
        wire = packet(sys.argv[1:] if argv is None else argv)
    except Exception:
        sys.stderr.write('REFUSED: candidate input or dependency\n')
        return 2
    # One fully constructed ASCII JSON packet; no earlier stdout writes.
    sys.stdout.write(wire)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
