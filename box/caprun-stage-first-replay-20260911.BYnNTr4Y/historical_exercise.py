"""Offline documentary fixture only; emits a patch, never installs/releases."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'caprun-latebinder-code-astra-20260911'
PINS = {
    'latebind.py': 'ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe',
    'test_latebind.py': '85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06'}


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def historical_candidates():
    for name, digest in PINS.items():
        if hashlib.sha256((OLD / name).read_bytes()).hexdigest() != digest:
            raise ValueError('dependency pin: ' + name)
    fixture = module('stage_historical_fixture', OLD / 'test_latebind.py')
    fixture.Controls.setUpClass()  # Authenticates exactly8 historical text files.
    control = fixture.Controls()
    control.setUp()
    candidates = control.call()
    if json.loads(candidates['SUMMARY.json'])['context'] != 'HISTORICAL_TEST':
        raise ValueError('historical context')
    return candidates


def main():
    if len(sys.argv) != 2:
        raise ValueError('one fresh candidate directory required')
    transport = module('stage_transport', HERE / 'stage_patch.py')
    result = transport.make_patch(historical_candidates(), sys.argv[1])
    print(json.dumps(result, ensure_ascii=True, allow_nan=False))


if __name__ == '__main__':
    main()
