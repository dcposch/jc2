"""Prospective byte interlock, NOT a supervisor or self-granted ROOT authority."""
import os
import sys

TAG = 'f10-source-cone-r3-fullrank-v1'
FILES = ('authority.py', 'wire.py', 'finder.py', 'checker.py')
SOURCE_CHECKER = 'b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f'
SOURCE_OK = 'CHECKED_R3_25_GRAPH_SLOTS_45_LOW_108_JACOBIAN_NO_SOURCE_OUTCOME'
LIMITS = {'joint_wall_seconds': '600', 'joint_cpu_seconds': '550',
          'memory_bytes': '8589934592', 'baseline_bytes': '134217728',
          'certificate_bytes': '16777216', 'receipt_bytes': '32768'}


def authorize(mode):
    if mode not in ('find', 'check') or sys.platform != 'linux':
        raise SystemExit('REFUSED: mode/Linux')
    try:
        with open('/sys/class/dmi/id/sys_vendor', encoding='ascii') as f:
            vendor = f.read(128).strip()
    except OSError:
        raise SystemExit('REFUSED: DMI unavailable')
    if vendor != 'Amazon EC2':
        raise SystemExit('REFUSED: off AWS')
    if (len(sys.argv) != 9 or sys.argv[1:3] != ['--registered-job', TAG]
            or sys.argv[3] != '--authorization' or sys.argv[5] != '--authorization-sha256'
            or sys.argv[7] != ('--output' if mode == 'find' else '--input')):
        raise SystemExit('REFUSED: exact registered CLI')
    if not (sys.flags.ignore_environment and sys.flags.no_user_site
            and sys.flags.no_site and sys.dont_write_bytecode):
        raise SystemExit('REFUSED: required -E -s -S -B')
    # Exclude sibling shadow modules before importing metadata libraries. ROOT
    # must independently authenticate these four files before interpreter start.
    source_dir = os.path.dirname(os.path.realpath(__file__))
    if set(os.listdir(source_dir)) != set(FILES):
        raise SystemExit('REFUSED: exact four-file source directory')
    sys.path[:] = [p for p in sys.path if p and os.path.realpath(p) != source_dir]
    # Stdlib is loaded without sibling resolution; restore only after all pins.
    if not hasattr(sys, 'set_int_max_str_digits'):
        raise SystemExit('REFUSED: decimal protection unavailable')
    sys.set_int_max_str_digits(4300)
    import hashlib
    import json
    import stat
    import datetime

    def need(test, label):
        if not test:
            raise ValueError('AUTHORITY REFUSED: ' + label)

    def pin(s):
        need(isinstance(s, str) and len(s) == 64
             and all(c in '0123456789abcdef' for c in s), 'pin')
        return s

    def path(s):
        need(isinstance(s, str) and os.path.isabs(s)
             and os.path.realpath(s) == s, 'absolute canonical path')
        return s

    def digest(s, cap=None, frozen=False):
        s = path(s)
        fd = os.open(s, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, 'rb') as f:
            st = os.fstat(f.fileno())
            need(stat.S_ISREG(st.st_mode), 'regular file')
            if frozen:
                need(st.st_uid == 0 and stat.S_IMODE(st.st_mode) == 0o444,
                     'ROOT-owned readonly input')
            if cap is not None:
                need(st.st_size <= cap, 'byte cap')
            h = hashlib.sha256()
            while True:
                block = f.read(1048576)
                if not block:
                    break
                h.update(block)
            return h.hexdigest(), st.st_size

    def pairs(items):
        out = {}
        for k, v in items:
            need(k not in out, 'duplicate JSON key')
            out[k] = v
        return out

    def bad(_):
        raise ValueError('AUTHORITY REFUSED: JSON numbers/constants')

    def load(s, sha, cap=65536):
        need(digest(s, cap, True)[0] == pin(sha), 'metadata hash')
        fd = os.open(s, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, 'rb') as f:
            raw = f.read(cap + 1)
        need(len(raw) <= cap and hashlib.sha256(raw).hexdigest() == sha, 'metadata readback')
        return json.loads(raw, object_pairs_hook=pairs, parse_int=bad,
                          parse_float=bad, parse_constant=bad)

    meta = load(sys.argv[4], sys.argv[6])
    need(isinstance(meta, dict) and set(meta) == set(
        'schema job_tag authority status mode full_argv files runtime limits expires_utc baseline artifact receipt place'.split()), 'keys')
    need((meta['schema'], meta['job_tag'], meta['authority'], meta['status'], meta['mode']) ==
         ('r3-rank-authorization-v1', TAG, 'ROOT-CAPRUN', 'REGISTERED', mode), 'registration')
    need(meta['limits'] == LIMITS, 'limits')
    expected_argv = [sys.executable, '-E', '-s', '-S', '-B'] + sys.argv
    declared = meta['full_argv']
    need(isinstance(declared, list) and len(declared) == len(expected_argv)
         and declared.count('ROOT_AUTHORIZATION_SHA256') == 1
         and declared[11] == 'ROOT_AUTHORIZATION_SHA256', 'single typed argv hash hole')
    declared = list(declared)
    declared[11] = sys.argv[6]
    need(declared == expected_argv, 'literal full argv')
    with open('/proc/self/cmdline', 'rb') as f:
        live_argv = f.read(65537)
    need(len(live_argv) <= 65536 and live_argv.rstrip(b'\0').decode().split('\0') == expected_argv,
         'actual interpreter argv')
    base = os.path.dirname(os.path.realpath(__file__))
    need(sys.argv[0] == os.path.join(base, 'finder.py' if mode == 'find' else 'checker.py'), 'entry path')
    st = os.stat(base)
    need(st.st_uid == 0 and stat.S_IMODE(st.st_mode) == 0o755, 'trusted source directory')
    need(isinstance(meta['files'], dict) and set(meta['files']) == set(FILES), 'four source roles')
    for name in FILES:
        need(meta['files'][name]['path'] == os.path.join(base, name)
             and set(meta['files'][name]) == {'path', 'sha256'}, 'source path/key')
        need(digest(meta['files'][name]['path'], 262144, True)[0] == pin(meta['files'][name]['sha256']), 'source hash')
    rt = meta['runtime']
    need(isinstance(rt, dict) and set(rt) == {'python_sha256', 'native_path', 'native_sha256'}, 'runtime keys')
    need(digest(os.path.realpath(sys.executable))[0] == pin(rt['python_sha256']), 'interpreter hash')
    inv = load(rt['native_path'], rt['native_sha256'])
    need(isinstance(inv, dict) and set(inv) == {'job_tag', 'files'}
         and inv['job_tag'] == TAG and isinstance(inv['files'], dict) and inv['files'], 'native inventory')
    for s, sha in inv['files'].items():
        need(digest(s)[0] == pin(sha), 'native entry')

    def clock_check():
        expiry = datetime.datetime.strptime(meta['expires_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
        need(datetime.datetime.now(datetime.timezone.utc) < expiry, 'expired')

    clock_check()
    bl = meta['baseline']
    need(isinstance(bl, dict) and set(bl) == {'path', 'sha256', 'bytes', 'qualification_path', 'qualification_sha256'}, 'baseline binding')
    actual = digest(bl['path'], 134217728, True)
    need(actual == (pin(bl['sha256']), int(bl['bytes'])) and str(actual[1]) == bl['bytes'], 'baseline size/hash')
    qualification = load(bl['qualification_path'], bl['qualification_sha256'])
    need(qualification == {'schema': 'r3-baseline-qualified-v1', 'authority': 'ROOT-CAPRUN',
         'status': 'ROOT_QUALIFIED_COMPLETE_SOURCE', 'baseline_sha256': bl['sha256'],
         'baseline_bytes': bl['bytes'], 'source_checker_sha256': SOURCE_CHECKER,
         'checker_exit': '0', 'checker_stdout': SOURCE_OK + '\n'}, 'ROOT qualification evidence')
    artifact = meta['artifact']
    need(isinstance(artifact, dict) and set(artifact) == {'path', 'sha256'}
         and artifact['path'] == path(sys.argv[8]), 'artifact binding')
    if mode == 'find':
        need(artifact['sha256'] == 'UNFORMED' and not os.path.lexists(artifact['path']), 'output must be absent')
    else:
        need(digest(artifact['path'], 16777216, True)[0] == pin(artifact['sha256']), 'certificate binding')
    receipt = meta['receipt']
    need(isinstance(receipt, dict) and set(receipt) == {'path', 'sha256'}
         and receipt['sha256'] == 'UNFORMED' and not os.path.lexists(path(receipt['path'])), 'receipt absent')
    need(isinstance(meta['place'], dict) and set(meta['place']) == {'p', 'phi'}, 'place fields')
    protected = {path(sys.argv[4]), bl['path'], bl['qualification_path'], rt['native_path']}
    protected.update(v['path'] for v in meta['files'].values())
    protected.update(inv['files'])
    protected.add(os.path.realpath(sys.executable))
    need(artifact['path'] not in protected and receipt['path'] not in protected
         and receipt['path'] != artifact['path'], 'input/output separation')

    def postcheck():
        clock_check()
        if mode == 'check':
            need(digest(artifact['path'], 16777216, True)[0] == artifact['sha256'], 'certificate postpin')
        need(digest(sys.argv[4], 65536, True)[0] == sys.argv[6], 'authority postpin')
        need(digest(bl['path'], 134217728, True) == actual, 'baseline postpin')
        need(digest(bl['qualification_path'], 65536, True)[0] == bl['qualification_sha256'], 'qualification postpin')
        need(digest(rt['native_path'], 65536, True)[0] == rt['native_sha256'], 'inventory postpin')
        need(digest(os.path.realpath(sys.executable))[0] == rt['python_sha256'], 'interpreter postpin')
        for item in meta['files'].values():
            need(digest(item['path'], 262144, True)[0] == item['sha256'], 'source postpin')
        for s, sha in inv['files'].items():
            need(digest(s)[0] == sha, 'native postpin')

    def write_new(s, raw, cap):
        need(isinstance(raw, bytes) and len(raw) <= cap, 'output cap')
        fd = os.open(path(s), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'wb') as f:
            f.write(raw)
            f.flush()
            os.fchmod(f.fileno(), 0o444)
            os.fsync(f.fileno())
        parent = os.open(os.path.dirname(s), os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(parent)
        finally:
            os.close(parent)
        sha = hashlib.sha256(raw).hexdigest()
        need(digest(s, cap) == (sha, len(raw)), 'output readback')
        return sha

    def finish(status, certificate_sha, details):
        postcheck()
        if certificate_sha != 'UNFORMED':
            need(digest(artifact['path'], 16777216, mode == 'check')[0] == certificate_sha,
                 'receipt binds current certificate')
        receipt_doc = {'schema': 'r3-rank-receipt-v1', 'job_tag': TAG,
            'mode': mode, 'status': status, 'science': 'NONE',
            'authorization_sha256': sys.argv[6], 'baseline_sha256': bl['sha256'],
            'qualification_sha256': bl['qualification_sha256'], 'place': meta['place'],
            'certificate_sha256': certificate_sha, 'files': meta['files'],
            'runtime': rt, 'details': details}
        raw = (json.dumps(receipt_doc, sort_keys=True, separators=(',', ':')) + '\n').encode('ascii')
        write_new(receipt['path'], raw, 32768)

    # ROOT must independently authenticate this record/evidence and supply native,
    # startup, UID/GID, cgroup, caps, readonly custody and quiet-harvest enforcement.
    # These byte checks do not prove an actual full-source check ever occurred.
    sys.path.insert(0, source_dir)
    return {'meta': meta, 'write_new': write_new, 'finish': finish,
            'postcheck': postcheck, 'digest': digest}
