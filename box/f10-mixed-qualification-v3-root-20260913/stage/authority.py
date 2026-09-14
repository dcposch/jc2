"""Metadata only. DISABLED until a separately reviewed ROOT registration exists."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import stat
import sys

JOB = 'f10-mixed-univariate-bezout-20260912'
MAX_WIRE = 16777216

def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode('ascii')

def absolute(name):
    need(type(name) is str and name.startswith('/'), 'absolute path required')
    p = Path(name)
    need(str(p.resolve()) == name, 'resolved path required')
    return p

def read(name, limit):
    p = absolute(name)
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'rb') as f:
        s = os.fstat(f.fileno())
        need(stat.S_ISREG(s.st_mode) and s.st_size <= limit, 'regular bounded file required')
        raw = f.read(limit + 1)
        need(len(raw) <= limit, 'file cap')
    return raw

def frozen(name, expected, limit):
    p = absolute(name)
    s = p.stat()
    need(s.st_uid == 0 and s.st_mode & 0o022 == 0, 'ROOT-owned non-public-writable input required')
    raw = read(name, limit)
    need(type(expected) is str and len(expected) == 64 and digest(raw) == expected, 'input SHA mismatch')
    return raw

def now():
    return datetime.datetime.now(datetime.timezone.utc)

def deadline(value):
    need(type(value) is str and value.endswith('+00:00'), 'explicit UTC deadline required')
    return datetime.datetime.fromisoformat(value)

def authorize(role):
    args = sys.argv[1:]
    keys = ['--job', '--authority', '--authority-sha256', '--output', '--receipt']
    if role == 'check':
        keys += ['--input']
    need(len(args) == 2 * len(keys) and args[::2] == keys, 'exact CLI required')
    values = dict(zip(keys, args[1::2]))
    need(values['--job'] == JOB, 'registered literal job required')
    need(sys.platform == 'linux' and os.geteuid() != 0, 'Linux unprivileged workload required')
    need(sys.orig_argv[1:5] == ['-E', '-s', '-S', '-B'], 'exact startup flags required')
    raw = frozen(values['--authority'], values['--authority-sha256'], 65536)
    a = json.loads(raw, object_pairs_hook=pairs)
    fields = {'schema','enabled','job','role','argv','worker','boot_id','hostname','not_before','deadline',
              'limits','sources','native_manifest','library_paths','input_sha256','qualification'}
    need(type(a) is dict and set(a) == fields, 'authority schema')
    need(a['schema'] == 'f10-mixed-univariate-authority/v1' and a['enabled'] is True,
         'authority disabled')
    expected = a['argv']
    need(type(expected) is list and len(expected) == len(sys.argv)
         and expected[6] == 'ROOT_AUTHORITY_SHA256', 'typed authority SHA slot')
    expanded = expected[:]
    expanded[6] = digest(raw)
    need(a['job'] == JOB and a['role'] == role and expanded == sys.argv, 'authority command mismatch')
    need(deadline(a['not_before']) <= now() < deadline(a['deadline']), 'authority time window')
    need((deadline(a['deadline']) - deadline(a['not_before'])).total_seconds() <= 3600, 'wall envelope')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2', 'EC2 required')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == a['worker']
         and type(a['worker']) is str and a['worker'].startswith('i-'), 'worker identity')
    need(Path('/proc/sys/kernel/random/boot_id').read_text().strip() == a['boot_id'], 'boot identity')
    need(os.uname().nodename == a['hostname'], 'hostname identity')
    need(a['limits'] == {'wall':3600,'cpu':3300,'memory':34359738368,'wire':268435456}, 'fixed ceiling')
    for which, ceiling in ((resource.RLIMIT_CPU,3300),(resource.RLIMIT_AS,34359738368),
                           (resource.RLIMIT_FSIZE,268435456)):
        soft, hard = resource.getrlimit(which)
        need(0 < soft <= hard <= ceiling, 'external rlimit absent')
    need(type(a['sources']) is dict and len(a['sources']) == 4, 'four source/interpreter pins required')
    base = Path(__file__).resolve().parent
    required = {str(base / n) for n in ('authority.py','produce.py','check.py')}
    required.add(str(Path(sys.executable).resolve()))
    need(set(a['sources']) == required, 'source inventory mismatch')
    for p, sha in a['sources'].items():
        frozen(p, sha, 67108864)
        if p != str(Path(sys.executable).resolve()):
            need(absolute(p).stat().st_mode & 0o222 == 0, 'source must be frozen read-only')
    m = a['native_manifest']
    need(type(m) is dict and set(m) == {'path','sha256'}, 'native manifest binding')
    native = json.loads(frozen(m['path'], m['sha256'], 2097152), object_pairs_hook=pairs)
    need(type(native) is dict and set(native) == {'schema','files'}
         and native['schema'] == 'f10-mixed-native-files/v1', 'native schema')
    need(type(native['files']) is dict and 1 <= len(native['files']) <= 8192, 'native inventory bound')
    for p, sha in native['files'].items():
        frozen(p, sha, 268435456)
    q = a['qualification']
    need(type(q) is dict and set(q) == {'path','sha256'}, 'ROOT qualification binding')
    frozen(q['path'], q['sha256'], 65536)
    need(type(a['library_paths']) is list and 1 <= len(a['library_paths']) <= 4, 'library paths')
    for name in a['library_paths']:
        p = absolute(name)
        need(p.is_dir() and p.stat().st_uid == 0 and p.stat().st_mode & 0o022 == 0, 'library directory')
    outputs = [values['--output'], values['--receipt']]
    need(len(set(outputs)) == 2, 'distinct outputs required')
    for name in outputs:
        p = absolute(name)
        need(not p.exists() and not p.is_symlink() and p.parent.is_dir(), 'fresh exclusive output required')
        need(name not in a['sources'] and name not in (m['path'], q['path'], values['--authority']), 'output collision')
    if role == 'check':
        need(values['--input'] not in outputs, 'input/output collision')
        frozen(values['--input'], a['input_sha256'], MAX_WIRE)
    else:
        need(a['input_sha256'] is None, 'producer has no coefficient input')
    return {'authority':a,'values':values,'native':native,'authority_sha256':digest(raw)}

def finish(ctx):
    a = ctx['authority']
    need(now() < deadline(a['deadline']), 'deadline expired')
    frozen(ctx['values']['--authority'], ctx['authority_sha256'], 65536)
    for p, sha in a['sources'].items():
        frozen(p, sha, 67108864)
    for p, sha in ctx['native']['files'].items():
        frozen(p, sha, 268435456)
    if a['role'] == 'check':
        frozen(ctx['values']['--input'], a['input_sha256'], MAX_WIRE)

def write(name, obj, limit=MAX_WIRE):
    raw = canonical(obj)
    need(len(raw) <= limit, 'output byte cap')
    p = absolute(name)
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
    d = os.open(p.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(d)
    finally:
        os.close(d)
    need(read(name, limit) == raw, 'exclusive output readback mismatch')
    return digest(raw)
