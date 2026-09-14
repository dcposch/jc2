"""Prospective interlock only. ROOT registration and reviewed launcher required."""
import os
import sys

TAG = 'f10-source-cone-r3-direct-rows-v1'
FILES = ('authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py')
LIMITS = {'wall_seconds': '900', 'cpu_seconds': '600',
          'memory_bytes': '8589934592', 'aggregate_bytes': '134217728'}


def authorize(mode):
    if sys.flags.optimize:
        raise SystemExit('REFUSED: ordinary interpreter required')
    if mode not in ('produce', 'check'):
        raise SystemExit('REFUSED: unsupported mode')
    if sys.platform != 'linux':
        raise SystemExit('REFUSED: Linux EC2 only')
    try:
        with open('/sys/class/dmi/id/sys_vendor', encoding='ascii') as stream:
            vendor = stream.read(128).strip()
    except OSError:
        raise SystemExit('REFUSED: missing EC2 DMI identity')
    if vendor != 'Amazon EC2':
        raise SystemExit('REFUSED: off AWS')
    if (len(sys.argv) != 9 or sys.argv[1:3] != ['--registered-job', TAG]
            or sys.argv[3] != '--authorization'
            or sys.argv[5] != '--authorization-sha256'
            or sys.argv[7] != ('--output' if mode == 'produce' else '--input')):
        raise SystemExit('REFUSED: registered CLI contract')
    base = os.path.dirname(os.path.realpath(__file__))
    expected_entry = os.path.join(base, 'produce.py' if mode == 'produce' else 'check.py')
    if sys.argv[0] != expected_entry:
        raise SystemExit('REFUSED: actual entry path')
    if set(os.listdir(base)) != set(FILES):
        raise SystemExit('REFUSED: exact installed five-file inventory')
    sys.path[:] = [p for p in sys.path if p and os.path.realpath(p) != base]
    if not hasattr(sys, 'set_int_max_str_digits'):
        raise SystemExit('REFUSED: giant-decimal protection unavailable')
    sys.set_int_max_str_digits(4300)
    import hashlib
    import json

    def pin(value):
        if (not isinstance(value, str) or len(value) != 64
                or any(c not in '0123456789abcdef' for c in value)):
            raise ValueError('pin format')
        return value

    def digest(path):
        h = hashlib.sha256()
        with open(path, 'rb') as stream:
            while True:
                block = stream.read(1048576)
                if not block:
                    break
                h.update(block)
        return h.hexdigest()

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate authority key')
            result[key] = value
        return result

    def no_number(value):
        raise ValueError('authority numbers must be strings')

    def load_pinned(path, expected):
        with open(path, 'rb') as stream:
            raw = stream.read(65537)
        if len(raw) > 65536 or hashlib.sha256(raw).hexdigest() != pin(expected):
            raise ValueError('authority/inventory byte pin')
        return json.loads(raw, object_pairs_hook=pairs, parse_int=no_number,
                          parse_float=no_number, parse_constant=no_number)

    meta = load_pinned(sys.argv[4], sys.argv[6])
    if set(meta) != {'job_tag', 'status', 'authority', 'mode', 'artifact', 'files', 'runtime', 'limits', 'contract_sha256', 'source_pins', 'place'}:
        raise ValueError('authority keys')
    if (meta['job_tag'], meta['status'], meta['authority']) != (TAG, 'REGISTERED', 'ROOT-CAPRUN'):
        raise ValueError('no ROOT registration')
    artifact = meta['artifact']
    if (meta['mode'] != mode or not isinstance(artifact, dict)
            or set(artifact) != {'path', 'sha256'}
            or artifact['path'] != os.path.abspath(sys.argv[8])):
        raise ValueError('registered mode/artifact path')
    if mode == 'produce':
        if artifact['sha256'] != 'UNFORMED' or os.path.lexists(sys.argv[8]):
            raise ValueError('producer output state')
    elif (os.stat(sys.argv[8]).st_size > 134217728
          or digest(sys.argv[8]) != pin(artifact['sha256'])):
        raise ValueError('registered checker input bytes/pin')
    if meta['limits'] != LIMITS or set(meta['files']) != set(FILES):
        raise ValueError('registered limits/source inventory')
    if not os.path.isabs(sys.argv[8]) or os.path.realpath(sys.argv[8]) != sys.argv[8]:
        raise ValueError('canonical artifact path')
    for name in FILES:
        if digest(os.path.join(base, name)) != pin(meta['files'][name]):
            raise ValueError('source pin: ' + name)
    pin(meta['contract_sha256'])
    sp = meta['source_pins']
    if not isinstance(sp, dict) or not sp or any(not isinstance(k, str) for k in sp):
        raise ValueError('source vector shape')
    for value in sp.values():
        pin(value)
    for name in FILES:
        if sp.get(os.path.join(base, name)) != meta['files'][name]:
            raise ValueError('installed source pin repeated in source vector')
    place = meta['place']
    if not isinstance(place, dict) or set(place) != {'p', 'degree', 'phi', 'P7_mod_p'}:
        raise ValueError('place metadata shape')
    if (not isinstance(place['p'], str) or not isinstance(place['degree'], str)
            or any(not isinstance(place[k], list) or any(not isinstance(v, str) for v in place[k])
                   for k in ('phi', 'P7_mod_p'))):
        raise ValueError('place string containers')
    rt = meta['runtime']
    if set(rt) != {'python_sha256', 'native_inventory_path', 'native_inventory_sha256'}:
        raise ValueError('runtime keys')
    if digest(sys.executable) != pin(rt['python_sha256']):
        raise ValueError('interpreter pin')
    inv = load_pinned(rt['native_inventory_path'], rt['native_inventory_sha256'])
    if set(inv) != {'job_tag', 'files'} or inv['job_tag'] != TAG or not isinstance(inv['files'], dict) or not inv['files']:
        raise ValueError('native inventory shape')
    for path, expected in inv['files'].items():
        if not os.path.isabs(path) or digest(path) != pin(expected):
            raise ValueError('native inventory entry')
    # This authenticates bytes, not provenance or completeness. ROOT's separately
    # reviewed launcher must supply genuine registration, complete native closure,
    # process/cgroup limits and harvest custody. Self-authored JSON is no authority.
    sys.path.insert(0, base)
    return {'artifact_path': sys.argv[8], 'contract_sha256': meta['contract_sha256'],
            'source_pins': dict(sp), 'place': dict(place)}
