"""STATIC/UNEXECUTED. Requires external ROOT approval, FIRST and capped launcher.

One process: observe -> create nine empty leaves -> bind -> exec dispatcher.
No subprocess, import of campaign code, science, retry, cleanup or fallback.
"""
import os
import sys

if sys.platform != 'linux' or os.geteuid() != 0:
    raise SystemExit('REFUSED: ROOT Linux bootstrap only')
if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode
        and not sys.flags.optimize):
    raise SystemExit('REFUSED: exact isolated ordinary startup required')

import datetime
import hashlib
import json
import pathlib
import re
import resource
import socket
import stat
import time

BEGIN = time.monotonic()
JOB = 'f10-source-cone-r3-necessary-rows-v1'
DISPATCH = '52b3d916f4fc3941bb98c8b4f7698ab940680d09ee4e065de1f167857e3fd436'
CAPRUN = 'd78d45ef671c706706a12f4179abbc777684da13673263e54461c74351d453a3'
AUTHORITY = '804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4'
LABELS = ('refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source',
          'refuse-hash', 'valid', 'startup-produce', 'startup-check', 'dummy')
NAMES = ('authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
LIMITS = {'wall_seconds': '900', 'cpu_seconds': '600',
          'memory_bytes': '8589934592', 'aggregate_bytes': '134217728'}
BATCH = {'wall_seconds': '3000', 'cpu_seconds': '2100',
         'memory_bytes': '8589934592', 'aggregate_bytes': '134217728'}
PROFILES = {'control': [5, 3, 8589934592], 'dummy': [5, 3, 33554432],
            'produce': [900, 599, 8589934592], 'check': [900, 599, 8589934592],
            'mutate': [30, 20, 8589934592]}
REG_KEYS = set('schema enabled jobtag exclusive_no_concurrent_writer execution_mode allowed_phases closed_scope_first_sha256 source_files review_clearance source_limits limits profiles environment uid gid instance_id hostname boot_id pid_namespace cgroup_path closed_child_guard aggregate_cpu_start_usec files science_dir wrapper_dir source_pins contract_sha256 place outer_argv pins preflight_policy native_manifest source_native_manifest output_mount authority_dir frozen_dir writer_dir durable_dir durable_device mathematical_deadline_utc task_deadline_utc admission_deadline_utc worker_deadline_utc commands typed_slot_policy phase_policy'.split())
SPEC_KEYS = {'schema', 'approval', 'bootstrap_sha256', 'bootstrap_first_sha256',
             'launcher_qualification_sha256', 'native_qualification_sha256',
             'registration_path', 'binding_path', 'binding_deadline_utc',
             'binding_wall_seconds', 'cgroup_namespace', 'mount_namespace',
             'outer_started_utc', 'outer_resources', 'external_supervisor',
             'exclusive_root_contract', 'registration'}


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


def utc():
    return datetime.datetime.now(datetime.timezone.utc)


def deadline(s):
    need(type(s) is str and s.endswith('+00:00'), 'offset-explicit UTC')
    return datetime.datetime.fromisoformat(s)


def pin(s):
    need(type(s) is str and re.fullmatch('[0-9a-f]{64}', s), 'SHA256 shape')
    return s


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=True, sort_keys=True,
                       separators=(',', ':'), allow_nan=False) + '\n').encode('utf-8')


def pairs(items):
    out = {}
    for k, v in items:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def no_float(s):
    raise ValueError('floating/nonfinite metadata forbidden')


def literal(s):
    need(type(s) is str and re.fullmatch('/[A-Za-z0-9_./-]+', s), 'literal path')
    p = pathlib.Path(s)
    need(p.is_absolute() and str(p) == s and str(p.resolve()) == s
         and not p.is_symlink(), 'canonical path')
    return p


def no_acl(p):
    need(not {'system.posix_acl_access', 'system.posix_acl_default'}.intersection(
        os.listxattr(p, follow_symlinks=False)), 'ACL-free ROOT path required')


def directory(p, mode=None):
    p = literal(str(p))
    for q in (p,) + tuple(p.parents):
        s = q.lstat()
        need(stat.S_ISDIR(s.st_mode) and s.st_uid == 0 and not s.st_mode & 0o022
             and s.st_mode & 0o005 == 0o005, 'ROOT traversable ancestry')
        no_acl(q)
    if mode is not None:
        need(stat.S_IMODE(p.stat().st_mode) == mode, 'directory mode')
    return p


def regular(p, writable_root=False):
    p = literal(str(p)); directory(p.parent)
    s = p.lstat(); no_acl(p)
    need(stat.S_ISREG(s.st_mode) and s.st_uid == 0 and s.st_mode & 0o004
         and not s.st_mode & (0o022 if writable_root else 0o222), 'pinned file mode')
    return p


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def read_json(p, expected, ceiling):
    p = regular(p)
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC)
    with os.fdopen(fd, 'rb') as f:
        before = os.fstat(f.fileno()); raw = f.read(ceiling + 1); after = os.fstat(f.fileno())
    stable = lambda s: (s.st_dev, s.st_ino, s.st_mode, s.st_uid, s.st_gid, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    need(stable(before) == stable(after) and len(raw) <= ceiling and hashlib.sha256(raw).hexdigest() == pin(expected), 'metadata bytes/pin')
    obj = json.loads(raw, object_pairs_hook=pairs, parse_float=no_float, parse_constant=no_float)
    need(encoded(obj) == raw, 'canonical JSON bytes required')
    return obj


def small(p):
    with open(p, encoding='ascii') as f:
        value = f.read(65537)
    need(len(value) <= 65536, 'kernel metadata cap')
    return value.strip()


def syncdir(p):
    fd = os.open(p, os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def exclusive(p, raw):
    need(len(raw) <= 65536, 'output metadata cap')
    directory(p.parent)
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o444)
    with os.fdopen(fd, 'wb') as f:
        f.write(raw); f.flush(); os.fsync(f.fileno()); os.fchmod(f.fileno(), 0o444)
    syncdir(p.parent)
    need(regular(p).read_bytes() == raw, 'exclusive byte readback')
    return hashlib.sha256(raw).hexdigest()


def mounts():
    rows = []
    for line in small('/proc/self/mountinfo').splitlines():
        left, right = line.split(' - ', 1); a, b = left.split(), right.split()
        rows.append((a[3], a[4], b[0]))
    return rows


def mount_for(p):
    hits = [(len(m), m, fs) for root, m, fs in mounts()
            if str(p) == m or str(p).startswith(m.rstrip('/') + '/')]
    need(hits, 'mount absent')
    return max(hits)[1:]


def self_identity():
    raw = small('/proc/self/stat'); fields = raw[raw.rfind(')') + 2:].split()
    return {'pid': os.getpid(), 'pgid': int(fields[2]), 'start_ticks': fields[19],
            'boot_id': small('/proc/sys/kernel/random/boot_id'),
            'pid_namespace': os.readlink('/proc/self/ns/pid'),
            'cgroup_namespace': os.readlink('/proc/self/ns/cgroup'),
            'mount_namespace': os.readlink('/proc/self/ns/mnt'),
            'cgroup': small('/proc/self/cgroup'),
            'exe': os.readlink('/proc/self/exe'),
            'argv': pathlib.Path('/proc/self/cmdline').read_bytes().rstrip(b'\0').decode().split('\0')}


class Bootstrap:
    def __init__(self, spec_path, expected):
        self.spec_path = regular(spec_path); self.spec_sha = pin(expected)
        self.s = read_json(self.spec_path, self.spec_sha, 262144)
        s = self.s
        need(type(s) is dict and set(s) == SPEC_KEYS and s['schema'] == 'r3-exec-bootstrap/v1'
             and s['approval'] == 'ROOT_APPROVED_PREFLIGHT_ONLY_9', 'external launch specification')
        for key in ('bootstrap_sha256', 'bootstrap_first_sha256', 'launcher_qualification_sha256', 'native_qualification_sha256'):
            pin(s[key])
        self.own = regular(__file__)
        need(sha(self.own) == s['bootstrap_sha256'] and stat.S_IMODE(self.own.stat().st_mode) == 0o444
             and stat.S_IMODE(self.spec_path.stat().st_mode) == 0o444, 'approved bootstrap/spec bytes and modes')
        self.r = s['registration']; r = self.r
        need(type(r) is dict and set(r) == REG_KEYS, 'exact registration skeleton keys')
        need(r['schema'] == 'f10-necessary-rows-runtime/closed-child-v1' and r['enabled'] is False
             and r['jobtag'] == JOB and r['exclusive_no_concurrent_writer'] is True
             and r['execution_mode'] == 'PREFLIGHT_ONLY_9' and r['allowed_phases'] == list(LABELS)
             and r['commands'] == {} and r['typed_slot_policy'] == {} and r['phase_policy'] is None,
             'disabled nine-only skeleton, no future hash slots')
        need(r['source_limits'] == LIMITS and r['limits'] == BATCH and r['profiles'] == PROFILES
             and r['environment'] == ENV and dict(os.environ) == ENV
             and r['aggregate_cpu_start_usec'] == '0', 'unchanged limits/environment/conservative CPU origin')
        need(type(r['uid']) is int and type(r['gid']) is int and r['uid'] > 0 and r['gid'] > 0, 'unprivileged child IDs')
        review = r['review_clearance']
        need(set(review) == {'status', 'source_first_sha256', 'runtime_first_sha256'}
             and review['status'] == 'SOURCE_AND_RUNTIME_FIRST_CONFIRMED', 'ROOT source/runtime reviews')
        for h in (review['source_first_sha256'], review['runtime_first_sha256'], r['closed_scope_first_sha256'], r['contract_sha256']):
            pin(h)
        need(s['binding_wall_seconds'] == 120 and type(s['binding_wall_seconds']) is int, 'fixed bootstrap wall bound')
        self.bind_end = deadline(s['binding_deadline_utc'])
        self.ends = [deadline(r[k]) for k in ('admission_deadline_utc', 'mathematical_deadline_utc', 'task_deadline_utc', 'worker_deadline_utc')]
        need(self.bind_end <= self.ends[0] <= self.ends[1] < self.ends[2] < self.ends[3], 'original deadline ordering')
        self.outer_start = deadline(s['outer_started_utc'])
        need(self.bind_end <= self.outer_start + datetime.timedelta(seconds=120)
             and self.ends[2] <= self.outer_start + datetime.timedelta(seconds=3000),
             'binding and whole-task absolute bounds from original outer start')
        external = s['external_supervisor']
        need(set(external) == {'already_armed', 'no_restart', 'covers_bootstrap_exec_descendants', 'qualification_sha256', 'unit', 'outer_deadline_utc', 'retirement_deadline_utc'}
             and all(external[k] is True for k in ('already_armed', 'no_restart', 'covers_bootstrap_exec_descendants')),
             'externally armed immutable supervisor contract')
        pin(external['qualification_sha256'])
        need(re.fullmatch('[A-Za-z0-9_.@-]+[.]service', external['unit'])
             and deadline(external['outer_deadline_utc']) <= self.ends[2]
             and external['retirement_deadline_utc'] == r['worker_deadline_utc'], 'external fixed unit cutoffs')
        need(s['exclusive_root_contract'] == dict.fromkeys(('no_concurrent_writer', 'no_entrants', 'no_migration', 'no_replacement', 'no_delegation', 'no_inherited_cgroup_fds'), True), 'exclusive ROOT trust contract')
        self.reg_path = literal(s['registration_path']); self.binding = literal(s['binding_path'])
        directory(self.reg_path.parent); directory(self.binding.parent)
        need(len({self.reg_path, self.binding, self.spec_path, self.own}) == 4
             and not os.path.lexists(self.reg_path) and not os.path.lexists(self.binding), 'fresh distinct outputs')
        self.files = r['files']
        need(set(self.files) == {'python', 'setpriv', 'caprun', 'dispatcher', 'probe', 'mutator'}, 'exact runtime roles')
        self.science = directory(r['science_dir'], 0o755); self.wrapper = directory(r['wrapper_dir'], 0o755)
        self.mount = directory(r['output_mount'], 0o755)
        self.cg = literal(r['cgroup_path'])
        need(str(self.cg).startswith('/sys/fs/cgroup/') and self.cg != pathlib.Path('/sys/fs/cgroup'), 'owned outer path')
        self.guard = r['closed_child_guard']
        need(set(self.guard) == {'schema', 'outer_device', 'outer_inode', 'root_no_migration', 'leaves'}
             and self.guard['schema'] == 'CAPRUN-closed-child/v1' and self.guard['root_no_migration'] is True
             and self.guard['outer_device'] is None and self.guard['outer_inode'] is None
             and set(self.guard['leaves']) == set(LABELS), 'only enumerated late scope identities')
        for label, leaf in self.guard['leaves'].items():
            need(leaf == {'path': str(self.cg / label), 'device': None, 'inode': None}, 'fixed direct leaf skeleton')
        need(r['outer_argv'] == [self.files['python'], '-I', '-S', '-B', self.files['dispatcher'], '--registration', str(self.reg_path)], 'exact future dispatcher argv')
        expected_argv = [self.files['python'], '-I', '-S', '-B', str(self.own), '--spec', str(self.spec_path), '--spec-sha256', self.spec_sha]
        need(sys.orig_argv == expected_argv and self_identity()['argv'] == expected_argv, 'actual bootstrap argv')
        self.initial = self_identity(); self.created = {}; self.reg_sha = None
        need(self.files['python'] == os.path.realpath(sys.executable)
             and self.initial['exe'] == self.files['python'], 'same pinned interpreter')
        need(r['pins'].get(str(self.own)) == s['bootstrap_sha256']
             and r['pins'].get(self.files['dispatcher']) == DISPATCH
             and r['pins'].get(self.files['caprun']) == CAPRUN, 'exact current code lineage')
        self.native = read_json(r['native_manifest'], r['pins'][r['native_manifest']], 1048576)
        self.simple = read_json(r['source_native_manifest'], r['pins'][r['source_native_manifest']], 65536)
        self.policy = read_json(r['preflight_policy'], r['pins'][r['preflight_policy']], 65536)
        self.audit_static(); self.observe(False); self.outputs(False)

    def clock(self):
        need(time.monotonic() - BEGIN < 120 and utc() < self.bind_end
             and self.outer_start <= utc() and (utc() - self.outer_start).total_seconds() < 3000,
             'original bootstrap/outer deadline; no reset')
        need(utc() + datetime.timedelta(seconds=20) < self.ends[1]
             and utc() < self.ends[0] and utc() < deadline(self.s['external_supervisor']['outer_deadline_utc']), 'first child wall plus 15s admission')

    def audit_static(self):
        self.clock(); r = self.r; n = self.native
        need(sha(regular(self.spec_path)) == self.spec_sha and sha(regular(self.own)) == self.s['bootstrap_sha256'], 'input/code drift')
        need(set(r['source_files']) == set(NAMES) and r['source_files']['authority.py'] == AUTHORITY, 'five source identities')
        need(type(r['source_pins']) is dict and 5 <= len(r['source_pins']) <= 64, 'source reference vector')
        for p in (str(self.spec_path), str(self.reg_path), str(self.binding)):
            need(p not in r['pins'] and p not in r['source_pins'] and p not in n['files'], 'no self/generated hash cycle')
        need(set(n) == {'schema', 'files', 'directories', 'aliases', 'absent', 'python_path'}
             and n['schema'] == 'f10-native-closure/v1' and n['python_path'] == sys.path
             and 0 < len(n['files']) <= 3000 and 0 < len(n['directories']) <= 1000, 'complete native closure')
        need(str(self.reg_path.parent) not in n['directories'], 'registration parent outside native inventory')
        need(set(self.simple) == {'job_tag', 'files'} and self.simple['job_tag'] == JOB
             and self.files['python'] in self.simple['files']
             and all(n['files'].get(p) == h for p, h in self.simple['files'].items()), 'simple native subset')
        need(set(self.policy) == {'schema', 'source_files', 'entries'} and self.policy['schema'] == 'f10-necessary-rows-preflight-policy/v1'
             and self.policy['source_files'] == r['source_files']
             and set(self.policy['entries']) == set(LABELS[:5]) | {'startup-produce', 'startup-check'}, 'seven literal refusals')
        for p in self.policy['entries'].values():
            need(set(p) == {'exit_code', 'stdout', 'stderr'} and type(p['exit_code']) is int and 1 <= p['exit_code'] <= 125
                 and p['stdout'] == '' and type(p['stderr']) is str and p['stderr'].isascii()
                 and 0 < len(p['stderr']) <= 8192 and p['stderr'].endswith('\n'), 'exact refusal strings')
        need(set(os.listdir(self.science)) == set(NAMES) and set(os.listdir(self.wrapper)) == {'dispatch.py', 'probe.py', 'mutate.py'}, 'source/wrapper exact inventories')
        need(self.science != self.wrapper and self.own.parent not in (self.science, self.wrapper), 'bootstrap separate directory')
        need(self.files['dispatcher'] == str(self.wrapper / 'dispatch.py') and self.files['probe'] == str(self.wrapper / 'probe.py')
             and self.files['mutator'] == str(self.wrapper / 'mutate.py'), 'literal runtime siblings')
        for name, h in r['source_files'].items():
            p = str(self.science / name)
            need(r['pins'].get(p) == h and r['source_pins'].get(p) == h
                 and stat.S_IMODE(regular(p).stat().st_mode) == 0o444, 'source repeated binding/mode')
        for p in self.files.values():
            need(p in r['pins'], 'runtime pin present')
        for p, h in list(r['pins'].items()) + list(r['source_pins'].items()) + list(n['files'].items()):
            self.clock(); path = regular(p, p in n['files'] or p in (self.files['python'], self.files['setpriv']))
            need(path != self.mount and self.mount not in path.parents and sha(path) == pin(h), 'all current static/native pins outside tmpfs')
        for role in ('dispatcher', 'probe', 'mutator', 'caprun'):
            need(stat.S_IMODE(regular(self.files[role]).stat().st_mode) == 0o444, 'runtime source 0444')
        for d, names in n['directories'].items():
            self.clock(); directory(d)
            need(sorted(os.listdir(d)) == names and len(names) == len(set(names)), 'native directory inventory')
            for name in names:
                p = str(pathlib.Path(d) / name)
                need(p in n['files'] or p in n['directories'] or p in n['aliases'], 'native unlisted child')
        for alias, target in n['aliases'].items():
            need(os.path.isabs(alias) and alias != target and os.path.realpath(alias) == target
                 and (target in n['files'] or target in n['directories']), 'native alias')
        for p in n['absent']:
            need(not os.path.lexists(p), 'native registered absence')
        for p in sys.path:
            need(p in n['files'] or p in n['directories'] or p in n['absent'], 'sys.path closure')
        for p in ('/bin/ps', '/usr/bin/ps'):
            need(p in n['files'] or p in n['aliases'], 'runner ps closure')
        for line in small('/proc/self/maps').splitlines():
            f = line.split(None, 5)
            if len(f) == 6 and f[5].startswith('/'):
                p = f[5]; q = os.path.realpath(p)
                need(not p.endswith(' (deleted)') and q in n['files']
                     and (p == q or n['aliases'].get(p) == q), 'strict mapped native closure')
        for key in ('native_manifest', 'source_native_manifest', 'preflight_policy'):
            need(sha(regular(r[key])) == r['pins'][r[key]], 'manifest drift')
        place = r['place']
        need(set(place) == {'p', 'degree', 'phi', 'P7_mod_p'}
             and all(type(place[k]) is str and re.fullmatch('0|[1-9][0-9]{0,9}', place[k]) for k in ('p', 'degree'))
             and all(type(place[k]) is list and 2 <= len(place[k]) <= 8
                     and all(type(v) is str and re.fullmatch('0|[1-9][0-9]{0,9}', v) for v in place[k]) for k in ('phi', 'P7_mod_p')),
             'place strings only; no arithmetic validation')

    def leaf(self, label):
        p = self.cg / label; directory(p)
        s = p.stat()
        need((s.st_dev, s.st_ino) == self.created[label], 'leaf identity changed')
        need(small(p / 'cgroup.type') == 'domain' and small(p / 'cgroup.subtree_control') == ''
             and not any(q.is_dir() for q in p.iterdir()), 'closed leaf topology')
        for name in ('cgroup.procs', 'cgroup.threads', 'cgroup.subtree_control', 'cgroup.events'):
            regular(p / name, True)
        events = dict(line.split() for line in small(p / 'cgroup.events').splitlines())
        need(events.get('populated') == '0' and small(p / 'cgroup.procs') == ''
             and small(p / 'cgroup.threads') == '', 'kernel empty leaf')

    def observe(self, complete):
        self.clock(); r = self.r
        need(self_identity() == self.initial, 'same process/start/argv/namespaces')
        need(small('/sys/class/dmi/id/sys_vendor') == 'Amazon EC2'
             and small('/sys/class/dmi/id/board_asset_tag') == r['instance_id']
             and re.fullmatch('i-[0-9a-f]{17}', r['instance_id'])
             and socket.gethostname() == r['hostname'], 'physical worker binding')
        need(self.initial['boot_id'] == r['boot_id'] and self.initial['pid_namespace'] == r['pid_namespace']
             and r['pid_namespace'] == os.readlink('/proc/1/ns/pid')
             and self.initial['cgroup_namespace'] == self.s['cgroup_namespace'] == os.readlink('/proc/1/ns/cgroup')
             and self.initial['mount_namespace'] == self.s['mount_namespace'] == os.readlink('/proc/1/ns/mnt'), 'ROOT namespace bindings')
        need(self.initial['cgroup'] == '0::' + str(self.cg).removeprefix('/sys/fs/cgroup')
             and [(root, m) for root, m, fs in mounts() if fs == 'cgroup2'] == [('/', '/sys/fs/cgroup')], 'actual outer cgroup/mount')
        directory(self.cg)
        pair = (self.cg.stat().st_dev, self.cg.stat().st_ino)
        if not hasattr(self, 'outer_pair'):
            self.outer_pair = pair
        need(pair == self.outer_pair and min(pair) > 0, 'outer immutable identity')
        need(small(self.cg / 'cgroup.type') == 'domain' and small(self.cg / 'cgroup.subtree_control') == '', 'outer domain/no delegation')
        for name in ('cgroup.procs', 'cgroup.threads', 'cgroup.subtree_control', 'cgroup.events'):
            regular(self.cg / name, True)
        need(small(self.cg / 'cgroup.procs') == str(os.getpid()) and small(self.cg / 'cgroup.threads') == str(os.getpid())
             and os.listdir('/proc/self/task') == [str(os.getpid())]
             and small('/proc/self/task/' + str(os.getpid()) + '/children') == '', 'only bootstrap, no surviving child/thread')
        resources = self.s['outer_resources']
        need(set(resources) == {'memory.max', 'memory.swap.max', 'pids.max', 'cpu.max', 'cpu.max.burst'}
             and resources['memory.max'] == '8589934592' and resources['memory.swap.max'] == '0'
             and resources['pids.max'] == '32' and resources['cpu.max.burst'] == '0'
             and re.fullmatch('[1-9][0-9]* [1-9][0-9]*', resources['cpu.max']), 'outer resource contract')
        for name, value in resources.items():
            need(small(self.cg / name) == value, 'current outer resource mismatch')
        cpu = dict(line.split() for line in small(self.cg / 'cpu.stat').splitlines())
        need(cpu.get('usage_usec', '').isdigit() and int(cpu['usage_usec']) < 2050000000, 'CPU origin zero/cutoff')
        dirs = {q.name for q in self.cg.iterdir() if q.is_dir()}
        need(dirs == (set(LABELS) if complete else set()), 'exact outer leaf inventory')
        if complete:
            for label in LABELS:
                self.leaf(label)

    def outputs(self, bound):
        r = self.r; dev = self.mount.stat().st_dev
        incoming = os.fstat(0); null = os.stat('/dev/null')
        need(stat.S_ISCHR(incoming.st_mode) and stat.S_ISCHR(null.st_mode)
             and (incoming.st_dev, incoming.st_ino, incoming.st_rdev) == (null.st_dev, null.st_ino, null.st_rdev)
             and os.readlink('/proc/self/fd/0') == '/dev/null', 'stdin actual /dev/null')
        need(mount_for(self.mount) == (str(self.mount), 'tmpfs'), 'exact working tmpfs')
        fs = os.statvfs(self.mount)
        need(0 < fs.f_blocks * fs.f_frsize <= 134217728, 'physical aggregate output cap')
        paths = [literal(r[k]) for k in ('authority_dir', 'frozen_dir', 'writer_dir')]
        need(len(set(paths)) == 3 and all(p.parent == self.mount for p in paths), 'three distinct working directories')
        for p in paths[:2]:
            directory(p, 0o755); need(not os.listdir(p), 'authority/frozen initially empty')
        w = paths[2]; st = w.lstat(); no_acl(w)
        need(stat.S_ISDIR(st.st_mode) and stat.S_IMODE(st.st_mode) == 0o700
             and st.st_uid == r['uid'] and st.st_gid == r['gid'] and not os.listdir(w), 'empty child-owned writer')
        need(self.binding == self.mount / 'bootstrap-binding.json', 'fixed bounded receipt location')
        expected = {p.name for p in paths} | {'outer.stdout', 'outer.stderr'}
        if bound:
            expected.add(self.binding.name)
        need(set(os.listdir(self.mount)) == expected, 'fresh working inventory')
        for fd, name in ((1, 'outer.stdout'), (2, 'outer.stderr')):
            st = os.fstat(fd); p = self.mount / name
            need(stat.S_ISREG(st.st_mode) and st.st_dev == dev and (st.st_dev, st.st_ino) == (p.stat().st_dev, p.stat().st_ino)
                 and os.readlink('/proc/self/fd/' + str(fd)) == str(p), 'all outer streams on working mount')
        for p in (self.own, self.spec_path, self.reg_path):
            need(self.mount not in p.parents, 'code/spec/registration outside working mount')
        durable = literal(r['durable_dir']); directory(durable.parent)
        need(not os.path.lexists(durable) and type(r['durable_device']) is int
             and r['durable_device'] > 0 and durable.parent.stat().st_dev == r['durable_device']
             and mount_for(durable.parent)[1] in ('ext4', 'xfs'), 'fresh durable EBS custody destination')

    def commands(self):
        r = self.r; files = self.files; authorities = {}; commands = {}
        for label in LABELS:
            target = str(pathlib.Path(r['writer_dir']) / (label + '.payload'))
            auth = str(pathlib.Path(r['authority_dir']) / (label + '.json'))
            profile = PROFILES['dummy' if label == 'dummy' else 'control']
            leaf = self.guard['leaves'][label]
            if label in ('valid', 'dummy'):
                obj = {'schema': 'f10-necessary-rows-root-policy/v1', 'root_registration_path': str(self.reg_path),
                       'job_tag': JOB, 'label': label, 'artifact': target, 'science_outcome': 'NONE',
                       'source_files': r['source_files'], 'limits': LIMITS, 'closed_scope': leaf, 'profile': profile}
            else:
                check = label == 'startup-check'
                obj = {'job_tag': JOB, 'status': 'REGISTERED', 'authority': 'ROOT-CAPRUN', 'mode': 'check' if check else 'produce',
                       'artifact': {'path': target, 'sha256': '0' * 64 if check else 'UNFORMED'}, 'files': dict(r['source_files']),
                       'runtime': {'python_sha256': r['pins'][files['python']], 'native_inventory_path': r['source_native_manifest'],
                                   'native_inventory_sha256': r['pins'][r['source_native_manifest']]},
                       'limits': dict(LIMITS), 'contract_sha256': r['contract_sha256'], 'source_pins': r['source_pins'], 'place': r['place']}
                if label == 'refuse-status': obj['status'] = 'DISABLED'
                if label == 'refuse-caps': obj['limits']['cpu_seconds'] = '599'
                if label == 'refuse-inventory': del obj['files']['check.py']
                if label == 'refuse-source': obj['files']['produce.py'] = '0' * 64
            raw = encoded(obj); need(len(raw) <= 65536, 'prospective authority byte cap')
            digest = hashlib.sha256(raw).hexdigest(); supplied = '0' * 64 if label == 'refuse-hash' else digest
            authorities[label] = {'path': auth, 'bytes': len(raw), 'sha256': digest, 'supplied_sha256': supplied}
            py = [files['python'], '-E', '-s', '-S', '-B']
            if label in ('valid', 'dummy'):
                py += [files['probe'], '--registration', str(self.reg_path), '--policy', auth, '--policy-sha256', supplied, '--mode', label, '--output', target]
            else:
                check = label == 'startup-check'
                py += [str(self.science / ('check.py' if check else 'produce.py')), '--registered-job',
                       'WRONG-JOB' if label.startswith('startup-') else JOB, '--authorization', auth,
                       '--authorization-sha256', supplied, '--input' if check else '--output', target]
            child = [files['setpriv'], '--reuid', str(r['uid']), '--regid', str(r['gid']), '--clear-groups', '--no-new-privs', '--'] + py
            cmd = [files['python'], '-I', '-S', '-B', files['caprun'], '--closed-child-cgroup', leaf['path'],
                   '--closed-child-device', str(leaf['device']), '--closed-child-inode', str(leaf['inode']),
                   '--closed-outer-cgroup', str(self.cg), '--closed-outer-device', str(self.guard['outer_device']),
                   '--closed-outer-inode', str(self.guard['outer_inode']), '--closed-boot-id', r['boot_id'],
                   '--closed-pid-namespace', r['pid_namespace'], '--wall-seconds', str(profile[0]), '--cpu-seconds', str(profile[1]),
                   '--rss-bytes', str(profile[2]), '--rss-sample-seconds', '0.05', '--term-grace-seconds', '1']
            for flag, suffix in (('--stdout-file', '.stdout'), ('--stderr-file', '.stderr'), ('--telemetry-file', '.telemetry.json')):
                cmd += [flag, str(self.mount / (label + suffix))]
            commands[label] = cmd + ['--cwd', str(self.science), '--'] + child
        return commands, authorities

    def run(self):
        os.umask(0o022)
        for label in LABELS:
            self.clock(); p = self.cg / label
            os.mkdir(p, 0o755)
            st = p.stat(); self.created[label] = (st.st_dev, st.st_ino); self.leaf(label)
        self.guard['outer_device'], self.guard['outer_inode'] = self.outer_pair
        for label, (dev, ino) in self.created.items():
            self.guard['leaves'][label].update(device=dev, inode=ino)
        self.r['commands'], authorities = self.commands(); self.r['enabled'] = True
        self.audit_static(); self.observe(True); self.outputs(False); self.clock()
        raw = encoded(self.r); self.reg_sha = exclusive(self.reg_path, raw)
        binding = {'schema': 'r3-exec-bootstrap-binding/v1', 'status': 'PREEXEC_BINDING_ONLY_NO_PREFLIGHT_RESULT',
                   'science_outcome': 'NONE', 'spec_path': str(self.spec_path), 'spec_sha256': self.spec_sha,
                   'bootstrap_sha256': self.s['bootstrap_sha256'], 'registration_path': str(self.reg_path),
                   'registration_sha256': self.reg_sha, 'observation_utc': utc().isoformat(), 'process': self.initial,
                   'closed_child_guard': self.guard, 'authority_metadata': authorities, 'dispatcher_argv': self.r['outer_argv'],
                   'external_supervisor': self.s['external_supervisor'], 'outer_started_utc': self.s['outer_started_utc'],
                   'binding_deadline_utc': self.s['binding_deadline_utc'], 'binding_wall_seconds': 120,
                   'original_deadlines': {k: v for k, v in self.r.items() if k.endswith('_deadline_utc')}}
        binding_sha = exclusive(self.binding, encoded(binding))
        self.audit_static(); self.observe(True); self.outputs(True); self.clock()
        need(sha(self.reg_path) == self.reg_sha and sha(self.binding) == binding_sha, 'final frozen binding drift')
        os.chdir(self.wrapper); os.umask(0o077)
        ceiling = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
        need(type(ceiling) is int and 3 <= ceiling <= 1048576, 'finite inherited descriptor closure')
        os.closerange(3, ceiling)
        os.execve(self.files['python'], self.r['outer_argv'], ENV)
        raise RuntimeError('exec unexpectedly returned')


def main():
    try:
        need(len(sys.argv) == 5 and sys.argv[1] == '--spec' and sys.argv[3] == '--spec-sha256', 'literal bootstrap CLI')
        Bootstrap(literal(sys.argv[2]), sys.argv[4]).run()
    except Exception as e:
        # No retry, deletion, migration, signal, timer operation or success status.
        print(json.dumps({'status': 'BOOTSTRAP_STOP', 'science_outcome': 'NONE',
                          'error_type': type(e).__name__, 'reason': str(e)[:500]}, sort_keys=True), flush=True)
        try:
            os.fsync(1)
        except OSError:
            pass
        return 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
