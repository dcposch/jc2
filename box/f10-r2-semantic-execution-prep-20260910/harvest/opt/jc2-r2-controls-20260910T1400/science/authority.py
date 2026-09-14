"""Prospective CLI interlock, not registration or execution authority."""
import sys
import os

TAG = 'f10-r2-reconstruction-v1'
FILES = ('authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py')


def authorize(mode):
    # Host rejection precedes JSON, hashing, Fraction, scientific imports/data.
    if sys.platform != 'linux':
        raise SystemExit('REFUSED: Linux EC2 only')
    try:
        with open('/sys/class/dmi/id/sys_vendor', 'r', encoding='ascii') as f:
            vendor = f.read(128).strip()
    except OSError:
        raise SystemExit('REFUSED: no EC2 DMI identity')
    if vendor != 'Amazon EC2':
        raise SystemExit('REFUSED: off AWS')
    if len(sys.argv) != 9 or sys.argv[1] != '--registered-job' or sys.argv[2] != TAG:
        raise SystemExit('REFUSED: explicit registered tag required')
    if sys.argv[3] != '--authorization' or sys.argv[5] != '--authorization-sha256':
        raise SystemExit('REFUSED: authorization arguments')
    if sys.argv[7] != ('--output' if mode == 'produce' else '--input'):
        raise SystemExit('REFUSED: mode arguments')
    expected = sys.argv[6]
    if len(expected) != 64 or any(x not in '0123456789abcdef' for x in expected):
        raise SystemExit('REFUSED: authorization pin')
    # Required process-local giant-decimal ceiling, before any coefficient parse.
    if not hasattr(sys, 'set_int_max_str_digits'):
        raise SystemExit('REFUSED: guarded Python integer conversion unavailable')
    sys.set_int_max_str_digits(4300)
    import hashlib
    import json

    def pairs(items):
        d = {}
        for k, v in items:
            if k in d:
                raise ValueError('duplicate authorization key')
            d[k] = v
        return d

    with open(sys.argv[4], 'rb') as f:
        raw = f.read(65537)
    if len(raw) > 65536 or hashlib.sha256(raw).hexdigest() != expected:
        raise SystemExit('REFUSED: authorization bytes/pin')
    meta = json.loads(raw, object_pairs_hook=pairs)
    if set(meta) != {'job_tag', 'status', 'authority', 'files', 'runtime', 'limits'}:
        raise SystemExit('REFUSED: authorization shape')
    if (meta['job_tag'], meta['status'], meta['authority']) != (TAG, 'REGISTERED', 'ROOT-CAPRUN'):
        raise SystemExit('REFUSED: no registered ROOT CAPRUN contract')
    limits = {'wall_seconds': '600', 'cpu_seconds': '500', 'memory_bytes': '2147483648',
              'aggregate_bytes': '16777216'}
    if meta['limits'] != limits or set(meta['files']) != set(FILES):
        raise SystemExit('REFUSED: registered limits/source inventory')
    base = os.path.dirname(os.path.abspath(__file__))
    for name in FILES:
        with open(os.path.join(base, name), 'rb') as f:
            source = f.read(1048577)
        if len(source) > 1048576:
            raise SystemExit('REFUSED: source byte bound')
        digest = hashlib.sha256(source).hexdigest()
        if digest != meta['files'][name]:
            raise SystemExit('REFUSED: source pin ' + name)
    if set(meta['runtime']) != {'python_sha256', 'native_inventory_sha256'}:
        raise SystemExit('REFUSED: native runtime inventory missing')
    for pin in meta['runtime'].values():
        if not isinstance(pin, str) or len(pin) != 64 or any(c not in '0123456789abcdef' for c in pin):
            raise SystemExit('REFUSED: runtime pin format')
    with open(sys.executable, 'rb') as f:
        if hashlib.sha256(f.read()).hexdigest() != meta['runtime']['python_sha256']:
            raise SystemExit('REFUSED: interpreter pin')
    # ROOT's existing future wrapper must authenticate registration provenance,
    # enforce CAPRUN/PGID/native inventory/aggregate limits and run dummy controls.
    # A self-authored JSON or an environment variable is not that authority.
    return sys.argv[8]
