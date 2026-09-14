"""Metadata-only entry gate. A root-owned capped wrapper is still mandatory."""
import datetime
import hashlib
import json
import os
import pathlib
import platform
import re
import socket
import stat
import sys

JOB = 'f10-middle-real-certificate-20260910'
LIMIT = 16777216
RECEIPT_LIMIT = 4096
DECIMAL_LIMIT = 4096
SCIENCE = {
    'f10-middle-real-domain-astra-20260910.md': '3f79cabecdb2c0f480bde3db644eac91ea5c8d3d472a3477f575b356993347ea',
    'f10-middle-real-domain-gate-fable5-20260910.md': 'f04c174e4b3111b2b9ee3e22e4ecceb619f0cfd2b9374e99a9ec9065cc52d21f',
    'f10-middle-resonance-unit-astra-20260910.md': '8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012',
    'f10-middle-resonance-unit-gate-fable5-20260910.md': 'dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad',
    'f10-middle-full-boundary-astra-20260910.md': '82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6',
    'f10-middle-full-boundary-gate-fable5-20260910.md': '8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491',
    'f10-middle-univariate-unit-astra-20260910.md': '890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5',
    'f10-middle-septic-gate-fable5-20260910.md': 'cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62',
}

def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError('duplicate JSON key')
        out[key] = value
    return out

def no_float(_):
    raise ValueError('floating or nonfinite JSON number')

def strict_json(raw, wire=False):
    kw = dict(object_pairs_hook=pairs, parse_float=no_float, parse_constant=no_float)
    if wire:
        kw['parse_int'] = lambda _: (_ for _ in ()).throw(ValueError('JSON integer forbidden in wire'))
    return json.loads(raw, **kw)

def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def regular(path):
    p = pathlib.Path(path)
    if not p.is_absolute() or p.is_symlink() or not stat.S_ISREG(p.stat().st_mode):
        raise ValueError('absolute regular nonsymlink input required')
    return p

def code_pins():
    folder = pathlib.Path(__file__).resolve().parent
    return {name: digest(folder / name) for name in ('authority.py', 'producer.py', 'checker.py')}

def authorize(operation, tag, registration, outputs, input_path=None):
    # No Fraction, math, polynomial, or determinant import/allocation precedes this.
    if not hasattr(sys, 'set_int_max_str_digits'):
        raise RuntimeError('decimal conversion guard unavailable')
    sys.set_int_max_str_digits(DECIMAL_LIMIT)
    if tag != JOB or platform.system() != 'Linux':
        raise ValueError('wrong job or platform')
    regpath = regular(registration)
    st = regpath.stat()
    if st.st_uid != 0 or stat.S_IMODE(st.st_mode) != 0o444 or st.st_size > 65536:
        raise ValueError('root-owned readonly registration required')
    raw = regpath.read_bytes()
    reg = strict_json(raw)
    if reg.get('enabled') is not True or reg.get('jobtag') != JOB or reg.get('operation') != operation:
        raise ValueError('disabled or mismatched registration')
    if reg.get('exclusive_no_concurrent_writer') is not True:
        raise ValueError('exclusive authority writer required')
    vendor = pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip()
    instance = pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
    if vendor != 'Amazon EC2' or not re.fullmatch(r'i-[0-9a-f]+', instance):
        raise ValueError('EC2 physical gate')
    if reg.get('instance_id') != instance or reg.get('hostname') != socket.gethostname():
        raise ValueError('registered physical identity mismatch')
    if reg.get('cwd') != os.getcwd() or reg.get('argv') != sys.argv:
        raise ValueError('cwd or full script argv mismatch')
    if reg.get('executable') != os.path.realpath(sys.executable):
        raise ValueError('interpreter mismatch')
    if reg.get('science') != SCIENCE:
        raise ValueError('science binding mismatch')
    caps = reg.get('caps')
    if caps != {'aggregate_wall_seconds': 360, 'aggregate_cpu_seconds': 330,
                'rss_bytes': 2147483648, 'aggregate_wire_bytes': LIMIT}:
        raise ValueError('caps mismatch')
    deadline = datetime.datetime.fromisoformat(reg['deadline_utc'])
    if deadline.tzinfo is None or datetime.datetime.now(datetime.timezone.utc) >= deadline:
        raise ValueError('deadline expired')
    pins = reg.get('pins')
    if not isinstance(pins, dict):
        raise ValueError('missing pins')
    folder = pathlib.Path(__file__).resolve().parent
    required = [folder / n for n in ('authority.py', 'producer.py', 'checker.py')]
    required.append(pathlib.Path(os.path.realpath(sys.executable)))
    if input_path is not None:
        required.append(regular(input_path))
    for p in required:
        p = regular(p)
        if pins.get(str(p)) != digest(p):
            raise ValueError('required input pin mismatch')
    for name, expected in pins.items():
        if not re.fullmatch(r'[0-9a-f]{64}', expected) or digest(regular(name)) != expected:
            raise ValueError('input pin mismatch')
    if reg.get('outputs') != outputs:
        raise ValueError('output binding mismatch')
    for name in outputs:
        p = pathlib.Path(name)
        if not p.is_absolute() or p.exists() or p.is_symlink() or not p.parent.is_dir():
            raise ValueError('exclusive absent output required')
    return {'registration': str(regpath), 'registration_sha256': hashlib.sha256(raw).hexdigest(),
            'pins': pins, 'operation': operation, 'deadline': deadline}

def postcheck(permit):
    if digest(permit['registration']) != permit['registration_sha256']:
        raise ValueError('registration changed')
    for name, expected in permit['pins'].items():
        if digest(name) != expected:
            raise ValueError('post input pin mismatch')
    if datetime.datetime.now(datetime.timezone.utc) >= permit['deadline']:
        raise ValueError('late result')

def emit(path, data, ceiling):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()
    if len(raw) > ceiling:
        raise ValueError('aggregate wire size limit')
    with open(path, 'xb') as stream:
        stream.write(raw)
    return hashlib.sha256(raw).hexdigest(), len(raw)
