"""Direct finite rows + one mixed-row runtime, STATIC/UNEXECUTED; disabled without fresh ROOT registration.

Metadata-only caller. No science import, coefficient parse, solver, retry,
installation, worker control, or inner process group. CAPRUN is unchanged.
"""
import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import resource
import shutil
import signal
import socket
import stat
import subprocess
import sys
import time

JOB = 'f10-source-cone-r3-necessary-rows-v1'
CAPRUN_SHA = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
SOURCE_NAMES = ('authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py')
LIMITS = {'wall_seconds': '900', 'cpu_seconds': '600', 'memory_bytes': '8589934592',
          'aggregate_bytes': '134217728'}
BATCH_LIMITS = {'wall_seconds': '3000', 'cpu_seconds': '2100',
                'memory_bytes': '8589934592', 'aggregate_bytes': '134217728'}
PROFILES = {'control': [5, 3, 8589934592], 'dummy': [5, 3, 33554432],
            'produce': [900, 599, 8589934592], 'check': [900, 599, 8589934592],
            'mutate': [30, 20, 8589934592]}
LABELS = ('refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source', 'refuse-hash',
          'valid', 'startup-produce', 'startup-check', 'dummy', 'produce',
          'check-positive', 'mutate', 'check-negative')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
TOTAL, PACKET, META = 134217728, 125829120, 8388608


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def pairs(items):
    out = {}
    for k, v in items:
        need(k not in out, 'duplicate metadata key')
        out[k] = v
    return out


def load(p, ceiling=65536):
    need(p.stat().st_size <= ceiling, 'metadata size cap')
    return json.loads(p.read_bytes(), object_pairs_hook=pairs)


def canonical(name):
    p = pathlib.Path(name)
    need(p.is_absolute() and re.fullmatch(r'/[A-Za-z0-9_./-]+', str(p)), 'literal absolute path')
    need(str(p.resolve()) == str(p) and not p.is_symlink(), 'canonical path')
    return p


def directory(p, mode=None):
    p = canonical(p)
    for d in (p,) + tuple(p.parents):
        st = d.stat()
        need(stat.S_ISDIR(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022
             and st.st_mode & 0o005 == 0o005, 'root-owned traversable directory')
    if mode is not None:
        need(stat.S_IMODE(p.stat().st_mode) == mode, 'exact directory mode')
    return p


def immutable(p, strict=True):
    p = canonical(p)
    directory(p.parent)
    st = p.stat()
    need(stat.S_ISREG(st.st_mode) and st.st_uid == 0 and st.st_mode & 0o004
         and not st.st_mode & (0o222 if strict else 0o022), 'immutable readable file')
    return p


def emit(p, obj):
    raw = (json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n').encode()
    need(len(raw) <= 65536, 'record byte cap')
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    with os.fdopen(fd, 'wb') as f:
        f.write(raw); f.flush(); os.fsync(f.fileno()); os.fchmod(f.fileno(), 0o444)
    return sha(p)


def syncdir(p):
    fd = os.open(p, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def mount_type(p):
    hits = []
    for line in pathlib.Path('/proc/self/mountinfo').read_text().splitlines():
        left, right = line.split(' - ', 1)
        mount = left.split()[4]
        if str(p) == mount or str(p).startswith(mount.rstrip('/') + '/'):
            hits.append((len(mount), mount, right.split()[0]))
    need(hits, 'mount identity absent')
    return max(hits)[1:]


def identity(pid):
    try:
        base = pathlib.Path('/proc') / str(pid)
        raw = (base / 'stat').read_text(); f = raw[raw.rfind(')') + 2:].split()
        status = dict(line.split(':', 1) for line in (base / 'status').read_text().splitlines() if ':' in line)
        mapped = set()
        for line in (base / 'maps').read_text().splitlines():
            fields = line.split(None, 5)
            if len(fields) == 6 and fields[5].startswith('/'):
                need(not fields[5].endswith(' (deleted)'), 'deleted mapped native file')
                mapped.add(fields[5])
        return {'pid': pid, 'pgid': int(f[2]), 'state': f[0], 'start_ticks': f[19],
                'boot_id': pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                'pid_namespace': os.readlink(base / 'ns/pid'),
                'argv': (base / 'cmdline').read_bytes().rstrip(b'\0').decode().split('\0'),
                'uid': status['Uid'].split(), 'gid': status['Gid'].split(),
                'caps': {k: status[k].strip() for k in ('CapInh', 'CapPrm', 'CapEff', 'CapBnd', 'NoNewPrivs')},
                'limits': (base / 'limits').read_text(), 'cgroup': (base / 'cgroup').read_text().strip(),
                'mapped_files': sorted(mapped)}
    except FileNotFoundError:
        return None


class Batch:
    def __init__(self, name):
        self.begin = time.monotonic()
        need(os.geteuid() == 0 and sys.platform == 'linux', 'ROOT Linux only')
        self.path = immutable(name); self.root_sha = sha(self.path); self.r = load(self.path)
        need(stat.S_IMODE(self.path.stat().st_mode) == 0o444, 'ROOT registration 0444')
        r = self.r
        need(r.get('schema') == 'f10-necessary-rows-runtime/v1' and r.get('enabled') is True, 'disabled ROOT registration')
        need(r['jobtag'] == JOB and r['exclusive_no_concurrent_writer'] is True, 'job/exclusivity')
        self.science = r['source_files']
        need(type(self.science) is dict and set(self.science) == set(SOURCE_NAMES)
             and all(type(h) is str and re.fullmatch(r'[0-9a-f]{64}', h) for h in self.science.values()), 'ROOT final five source hashes')
        review = r['review_clearance']
        need(set(review) == {'status', 'source_first_sha256', 'runtime_first_sha256'}
             and review['status'] == 'SOURCE_AND_RUNTIME_FIRST_CONFIRMED'
             and all(type(review[k]) is str and re.fullmatch(r'[0-9a-f]{64}', review[k])
                     for k in ('source_first_sha256', 'runtime_first_sha256')), 'both FIRSTs required by ROOT')
        need(r['source_limits'] == LIMITS and r['limits'] == BATCH_LIMITS
             and r['profiles'] == PROFILES, 'fixed cap profiles')
        need(r['environment'] == ENV and dict(os.environ) == ENV, 'ROOT clear environment required')
        need(type(r['uid']) is int and type(r['gid']) is int and r['uid'] > 0 and r['gid'] > 0, 'science UID/GID')
        need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2', 'EC2 only')
        need(pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == r['instance_id']
             and re.fullmatch(r'i-[0-9a-f]+', r['instance_id']), 'actual EC2 instance')
        need(socket.gethostname() == r['hostname'], 'host')
        need(pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == r['boot_id'], 'boot')
        need(os.readlink('/proc/self/ns/pid') == r['pid_namespace'], 'PID namespace')
        self.cg = canonical(r['cgroup_path'])
        need(str(self.cg).startswith('/sys/fs/cgroup/') and str(self.cg) != '/sys/fs/cgroup', 'owned cgroup')
        need(pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + str(self.cg)[len('/sys/fs/cgroup'):], 'exact cgroup')
        need((self.cg / 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'outer cgroup memory cap')
        need(type(r['aggregate_cpu_start_usec']) is str and re.fullmatch(r'[0-9]+', r['aggregate_cpu_start_usec']), 'ROOT aggregate CPU origin')
        self.cpu_start = int(r['aggregate_cpu_start_usec']) / 1000000
        need(self.cpu_start <= self.cpu(), 'CPU origin is no later than current usage')
        self.files = {k: immutable(v, k not in ('python', 'setpriv')) for k, v in r['files'].items()}
        need(set(self.files) == {'python', 'setpriv', 'caprun', 'dispatcher', 'probe', 'mutator'}, 'exact wrapper roles')
        need(str(self.files['python']) == os.path.realpath(sys.executable), 'interpreter')
        need(self.files['dispatcher'] == pathlib.Path(__file__).resolve(), 'dispatcher identity')
        self.source = directory(r['science_dir'], 0o755)
        self.wrapper = directory(r['wrapper_dir'], 0o755)
        need(self.source != self.wrapper and os.getcwd() == str(self.wrapper), 'separate wrapper cwd')
        self.source_pins = r['source_pins']
        need(type(self.source_pins) is dict and 5 <= len(self.source_pins) <= 64, 'bounded fixed reference vector')
        for path, digest in self.source_pins.items():
            need(type(path) is str and pathlib.Path(path).is_absolute()
                 and type(digest) is str and re.fullmatch(r'[0-9a-f]{64}', digest), 'literal source reference pin')
        need(all(self.source_pins.get(str(self.source / name)) == h for name, h in self.science.items()), 'installed absolute source pins agree')
        need(type(r['contract_sha256']) is str and re.fullmatch(r'[0-9a-f]{64}', r['contract_sha256']), 'ROOT contract manifest binding')
        place = r['place']
        need(type(place) is dict and set(place) == {'p', 'degree', 'phi', 'P7_mod_p'}
             and all(type(place[k]) is str and re.fullmatch(r'0|[1-9][0-9]{0,9}', place[k]) for k in ('p', 'degree'))
             and all(type(place[k]) is list and 2 <= len(place[k]) <= 8
                     and all(type(x) is str and re.fullmatch(r'0|[1-9][0-9]{0,9}', x) for x in place[k])
                     for k in ('phi', 'P7_mod_p')), 'ROOT place metadata shape only')
        need(self.files['dispatcher'].parent == self.wrapper and self.files['probe'].parent == self.wrapper,
             'exact wrapper siblings')
        need(self.files['mutator'] == self.wrapper / 'mutate.py', 'literal mutator sibling')
        outer = [str(self.files['python']), '-I', '-S', '-B', str(self.files['dispatcher']), '--registration', str(self.path)]
        need(r['outer_argv'] == outer and identity(os.getpid())['argv'] == outer, 'literal ROOT argv')
        self.pins = r['pins']
        self.preflight_path = immutable(r['preflight_policy'])
        need(self.pins.get(str(self.preflight_path)) == sha(self.preflight_path), 'reviewed preflight policy pin')
        preflight = load(self.preflight_path)
        need(set(preflight) == {'schema', 'source_files', 'entries'}
             and preflight['schema'] == 'f10-necessary-rows-preflight-policy/v1'
             and preflight['source_files'] == self.science, 'preflight bound to final source')
        self.refusals = preflight['entries']
        need(type(self.refusals) is dict and set(self.refusals) == set(LABELS[:5]) | {'startup-produce', 'startup-check'}, 'seven exact refusal predicates')
        for spec in self.refusals.values():
            need(type(spec) is dict and set(spec) == {'exit_code', 'stdout', 'stderr'}
                 and type(spec['exit_code']) is int and 1 <= spec['exit_code'] <= 125
                 and spec['stdout'] == '' and type(spec['stderr']) is str
                 and 0 < len(spec['stderr']) <= 8192 and spec['stderr'].isascii()
                 and spec['stderr'].endswith('\n'), 'literal bounded source refusal, no wildcard interpretation')
        for p in self.files.values():
            need(str(p) in self.pins, 'role path pin')
        need(self.pins[str(self.files['caprun'])] == CAPRUN_SHA, 'unchanged CAPRUN')
        for name, h in self.science.items():
            need(self.pins.get(str(self.source / name)) == h, 'actual science role pin: ' + name)
        self.native_path = immutable(r['native_manifest'])
        need(self.pins.get(str(self.native_path)) == sha(self.native_path), 'native manifest pin')
        self.native = load(self.native_path, 1048576)
        need(self.native.get('schema') == 'f10-native-closure/v1', 'native closure schema')
        need(set(self.native) == {'schema', 'files', 'directories', 'aliases', 'absent', 'python_path'}, 'complete native inventory fields')
        need(self.native['python_path'] == sys.path, 'exact -I -S native path')
        need(0 < len(self.native['files']) <= 3000 and 0 < len(self.native['directories']) <= 1000, 'bounded native closure')
        self.simple_path = immutable(r['source_native_manifest'])
        need(self.pins.get(str(self.simple_path)) == sha(self.simple_path), 'simple native manifest pin')
        self.simple = load(self.simple_path)
        need(set(self.simple) == {'job_tag', 'files'} and self.simple['job_tag'] == JOB
             and type(self.simple['files']) is dict and self.simple['files'], 'simple native schema')
        need(str(self.files['python']) in self.simple['files'], 'simple subset includes interpreter')
        for name, digest in self.simple['files'].items():
            need(self.native['files'].get(name) == digest, 'simple subset of full native closure')
        self.mount = directory(r['output_mount'], 0o755)
        self.auth = directory(r['authority_dir'], 0o755)
        self.frozen = directory(r['frozen_dir'], 0o755)
        self.writer = canonical(r['writer_dir'])
        need(len({self.auth, self.frozen, self.writer}) == 3 and all(p.parent == self.mount for p in (self.auth, self.frozen, self.writer)), 'output children')
        st = self.writer.stat()
        need(self.writer.is_dir() and st.st_uid == r['uid'] and st.st_gid == r['gid'] and stat.S_IMODE(st.st_mode) == 0o700, 'writer ownership')
        need(all(not list(p.iterdir()) for p in (self.auth, self.frozen, self.writer)), 'fresh output children')
        need(mount_type(self.mount) == (str(self.mount), 'tmpfs'), 'exact tmpfs')
        self.mount_id = (self.mount.stat().st_dev, self.mount.stat().st_ino)
        need(self.source != self.mount and self.mount not in self.source.parents and self.mount not in self.wrapper.parents, 'code outside outputs')
        need(all(p != self.mount and self.mount not in p.parents for p in
                 list(self.files.values()) + [self.path, self.native_path, self.simple_path, self.preflight_path]), 'static inputs outside tmpfs')
        for fd in (1, 2):
            need(os.fstat(fd).st_dev == self.mount_id[0] and stat.S_ISREG(os.fstat(fd).st_mode), 'outer streams on working tmpfs')
            stream = self.mount / ('outer.stdout' if fd == 1 else 'outer.stderr')
            need(os.readlink('/proc/self/fd/' + str(fd)) == str(stream) and not stream.is_symlink()
                 and stream.stat().st_ino == os.fstat(fd).st_ino, 'literal outer stream binding')
        self.durable = canonical(r['durable_dir']); directory(self.durable.parent)
        need(not self.durable.exists() and mount_type(self.durable.parent)[1] in ('ext4', 'xfs')
             and self.durable.parent.stat().st_dev == r['durable_device'], 'absent durable EBS target')
        self.end = self.deadline(r['mathematical_deadline_utc'])
        self.task_end = self.deadline(r['task_deadline_utc'])
        self.admission_end = self.deadline(r['admission_deadline_utc'])
        self.worker_end = self.deadline(r['worker_deadline_utc'])
        need(now() < self.admission_end <= self.end < self.task_end < self.worker_end, 'original deadlines')
        need(set(r['commands']) == set(LABELS), 'exact thirteen command registrations')
        need(r['typed_slot_policy'] == {
             'check-positive': {'flag': '--authorization-sha256', 'token': 'AUTHORIZATION_SHA256'},
             'check-negative': {'flag': '--authorization-sha256', 'token': 'AUTHORIZATION_SHA256'},
             'mutate': {'flag': '--root-registration-sha256', 'token': 'ROOT_REGISTRATION_SHA256'}}, 'only approved typed slots')
        need(r['phase_policy'] == {'baseline': str(self.frozen / 'artifact.json'),
             'fixture': str(self.frozen / 'mixed-row.json'),
             'mutation': 'graph.slots[24] += X1^27 over ROOT place', 'source_files': self.science,
             'source_limits': LIMITS, 'positive_record': str(self.auth / 'positive.json')}, 'literal phase policy')
        self.runs = []; self.used_labels = set(); self.frozen_pins = {}
        self.revalidate(); self.group_quiet()

    def deadline(self, value):
        need(isinstance(value, str) and value.endswith('+00:00'), 'literal UTC deadline')
        return datetime.datetime.fromisoformat(value)

    def cpu(self):
        records = dict(line.split() for line in (self.cg / 'cpu.stat').read_text().splitlines())
        return int(records['usage_usec']) / 1000000

    def budget(self, reserve=0):
        need(time.monotonic() - self.begin + reserve < 3000 and now() + datetime.timedelta(seconds=reserve) < self.end, 'joint/original wall')
        need(self.cpu() - self.cpu_start < 2050, 'sampled CPU safety cutoff; 50 seconds cleanup reserve')

    def revalidate(self):
        need(sha(self.path) == self.root_sha, 'ROOT registration drift')
        need(socket.gethostname() == self.r['hostname']
             and pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == self.r['instance_id']
             and pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == self.r['boot_id']
             and os.readlink('/proc/self/ns/pid') == self.r['pid_namespace'], 'current host/instance/boot/namespace')
        need(pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + str(self.cg)[len('/sys/fs/cgroup'):]
             and (self.cg / 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'current cgroup/cap')
        need(set(p.name for p in self.source.iterdir()) == set(self.science), 'EXACT five-file science directory')
        need(set(p.name for p in self.wrapper.iterdir()) == {'dispatch.py', 'probe.py', 'mutate.py'}, 'EXACT three-file wrapper directory')
        for p in self.files.values():
            if p.parent == self.wrapper:
                need(stat.S_IMODE(immutable(p).stat().st_mode) == 0o444, 'wrapper 0444')
        for p, digest in self.frozen_pins.items():
            need(sha(immutable(p)) == digest and stat.S_IMODE(pathlib.Path(p).stat().st_mode) == 0o444,
                 'frozen phase pin')
        need(sha(immutable(self.simple_path)) == self.pins[str(self.simple_path)], 'simple inventory drift')
        directory(self.source, 0o755); directory(self.wrapper, 0o755)
        for p, h in list(self.pins.items()) + list(self.native['files'].items()):
            need(re.fullmatch(r'[0-9a-f]{64}', h) and sha(immutable(p, p not in self.native['files'] and p not in (str(self.files['python']), str(self.files['setpriv'])))) == h, 'current pin')
        for name, h in self.science.items():
            p = immutable(self.source / name)
            need(stat.S_IMODE(p.stat().st_mode) == 0o444 and sha(p) == h, 'science 0444 and literal SHA')
        for d, entries in self.native['directories'].items():
            directory(d)
            need(sorted(os.listdir(d)) == entries and len(entries) == len(set(entries)), 'exact native directory')
            for name in entries:
                p = str(pathlib.Path(d) / name)
                need(p in self.native['directories'] or p in self.native['files'] or p in self.native['aliases'], 'native closure child unlisted')
        for alias, target in self.native['aliases'].items():
            p = pathlib.Path(alias)
            need(p.is_absolute() and str(p.resolve()) == target and str(p) != target, 'native alias drift')
            need(target in self.native['files'] or target in self.native['directories'], 'alias target closure')
        for p in self.native['absent']:
            need(not os.path.lexists(p), 'registered absent native/ZIP path appeared')
        for p in sys.path:
            need(p in self.native['directories'] or p in self.native['files'] or p in self.native['absent'], 'native sys.path closure')
        for p in ('/bin/ps', '/usr/bin/ps'):
            need(p in self.native['files'] or p in self.native['aliases'], 'CAPRUN ps alias closure')
        need(sha(self.native_path) == self.pins[str(self.native_path)], 'native manifest drift')
        need((self.mount.stat().st_dev, self.mount.stat().st_ino) == self.mount_id and mount_type(self.mount) == (str(self.mount), 'tmpfs'), 'tmpfs identity')
        fs = os.statvfs(self.mount)
        need(0 < fs.f_blocks * fs.f_frsize <= TOTAL, 'aggregate tmpfs capacity')
        need(now() < self.task_end, 'task cutoff')
        self.check_maps(identity(os.getpid()))

    def check_maps(self, item):
        need(item is not None, 'live identity unavailable')
        for path in item['mapped_files']:
            resolved = str(pathlib.Path(path).resolve())
            need(resolved in self.native['files'], 'mapped native file not pinned')
            if path != resolved:
                need(self.native['aliases'].get(path) == resolved, 'mapped native alias not pinned')

    def group_quiet(self):
        for text in (self.cg / 'cgroup.procs').read_text().split():
            if int(text) != os.getpid():
                p = identity(int(text))
                need(p is None or p['state'] == 'Z', 'owned cgroup still live; ROOT recovery required')

    def size_budget(self):
        metadata = 0
        packet_bytes = 0
        packet_paths = {self.writer / 'produce.payload', self.frozen / 'artifact.json',
                        self.writer / 'mixed-row.json', self.frozen / 'mixed-row.json'}
        for parent, dirs, names in os.walk(self.mount, followlinks=False):
            need(all(not (pathlib.Path(parent) / d).is_symlink() for d in dirs), 'output directory symlink')
            for name in names:
                p = pathlib.Path(parent) / name
                need(p.is_file() and not p.is_symlink(), 'output regularity')
                size = p.stat().st_size
                if p in packet_paths:
                    packet_bytes += size
                else:
                    metadata += size
        need(metadata <= META and packet_bytes <= PACKET, 'joint 120MiB packets / 8MiB metadata')

    def authorize(self, label, mode, target, input_hash):
        if label in ('valid', 'dummy', 'mutate'):
            obj = {'schema': 'f10-necessary-rows-root-policy/v1', 'root_registration_path': str(self.path),
                   'job_tag': JOB, 'label': label, 'artifact': str(target), 'science_outcome': 'NONE',
                   'source_files': self.science, 'limits': LIMITS, 'profile': PROFILES['dummy' if label == 'dummy' else 'control' if label == 'valid' else 'mutate']}
            p = self.auth / (label + '.json')
            digest = emit(p, obj); immutable(p)
            return p, digest
        obj = {'job_tag': JOB, 'status': 'REGISTERED', 'authority': 'ROOT-CAPRUN',
               'mode': mode, 'artifact': {'path': str(target),
               'sha256': (input_hash or '0' * 64) if mode == 'check' else 'UNFORMED'},
               'files': dict(self.science), 'runtime': {'python_sha256': self.pins[str(self.files['python'])],
               'native_inventory_path': str(self.simple_path),
               'native_inventory_sha256': sha(self.simple_path)}, 'limits': dict(LIMITS),
               'contract_sha256': self.r['contract_sha256'], 'source_pins': self.source_pins,
               'place': self.r['place']}
        if label == 'refuse-status': obj['status'] = 'DISABLED'
        if label == 'refuse-caps': obj['limits']['cpu_seconds'] = '599'
        if label == 'refuse-inventory': del obj['files']['check.py']
        if label == 'refuse-source': obj['files']['produce.py'] = '0' * 64
        p = self.auth / (label + '.json')
        digest = emit(p, obj); immutable(p)
        return p, digest

    def run(self, label, role, profile, input_path=None):
        need(label not in self.used_labels, 'no retry'); self.used_labels.add(label)
        self.group_quiet(); self.revalidate()
        wall, cpu, rss = PROFILES[profile]
        need(now() < self.admission_end, 'original admission stop')
        self.budget(wall + 15)
        payload = self.writer / (label + '.payload')
        target = input_path if input_path is not None else payload
        input_hash = sha(immutable(input_path)) if input_path is not None else None
        auth, digest = self.authorize(label, 'check' if role == 'check' else 'produce', target, input_hash)
        supplied = '0' * 64 if label == 'refuse-hash' else digest
        tag = 'WRONG-JOB' if label.startswith('startup-') else JOB
        tail = ['--registered-job', tag, '--authorization', str(auth), '--authorization-sha256', supplied,
                '--input' if role == 'check' else '--output', str(target)]
        if role == 'mutate':
            script = [str(self.files['mutator']), '--registration', str(self.path),
                      '--root-registration-sha256', self.root_sha,
                      '--positive-record', str(self.auth / 'positive.json')]
        elif role == 'probe':
            script = [str(self.files['probe']), '--registration', str(self.path), '--policy', str(auth),
                      '--policy-sha256', digest, '--mode', label, '--output', str(target)]
        else:
            script = [str(self.source / ('produce.py' if role == 'produce' else 'check.py'))] + tail
        py = [str(self.files['python'])] + (['-I', '-S', '-B'] if role == 'mutate'
              else ['-E', '-s', '-S', '-B']) + script
        child = [str(self.files['setpriv']), '--reuid', str(self.r['uid']), '--regid', str(self.r['gid']),
                 '--clear-groups', '--no-new-privs', '--'] + py
        out, err, tel = [self.mount / (label + suffix) for suffix in ('.stdout', '.stderr', '.telemetry.json')]
        command = [str(self.files['python']), '-I', '-S', '-B', str(self.files['caprun']),
                   '--wall-seconds', str(wall), '--cpu-seconds', str(cpu), '--rss-bytes', str(rss),
                   '--rss-sample-seconds', '0.05', '--term-grace-seconds', '1',
                   '--stdout-file', str(out), '--stderr-file', str(err), '--telemetry-file', str(tel),
                   '--cwd', str(self.source), '--'] + child
        registered = self.r['commands'][label]
        need(type(registered) is list and all(type(x) is str for x in registered), 'literal command strings')
        registered = list(registered)
        allowed = {'check-positive': ('--authorization-sha256', 'AUTHORIZATION_SHA256', digest),
                   'check-negative': ('--authorization-sha256', 'AUTHORIZATION_SHA256', digest),
                   'mutate': ('--root-registration-sha256', 'ROOT_REGISTRATION_SHA256', self.root_sha)}
        for token in ('AUTHORIZATION_SHA256', 'ROOT_REGISTRATION_SHA256'):
            if label in allowed and token == allowed[label][1]:
                flag, token, replacement = allowed[label]
                need(registered.count(flag) == registered.count(token) == 1, 'unique typed future slot')
                at = registered.index(flag) + 1
                need(at < len(registered) and registered[at] == token, 'correctly placed typed future slot')
                registered[at] = replacement
            else:
                need(token not in registered, 'future slot forbidden in this phase')
        need(command == registered, 'literal expanded ROOT CAPRUN argv mismatch')
        emit(self.mount / (label + '.pre.json'), {'utc': now().isoformat(), 'root_sha256': self.root_sha,
             'authorization_sha256': digest, 'supplied_authorization_sha256': supplied,
             'native_sha256': sha(self.native_path), 'source_pins': self.science, 'input_sha256': input_hash,
             'argv': command, 'python_argv': py, 'parent': identity(os.getpid()), 'profile': PROFILES[profile]})
        # Hash/native/host/authority barrier AFTER authority freeze and directly BEFORE Popen.
        self.revalidate(); self.budget(wall + 15); self.size_budget()
        need(sha(immutable(auth)) == digest, 'prelaunch authority drift')
        def file_limits():
            resource.setrlimit(resource.RLIMIT_FSIZE, (PACKET, PACKET))
            resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        before = time.monotonic(); live = None
        with open(self.mount / (label + '.runner.stdout'), 'xb') as rout, open(self.mount / (label + '.runner.stderr'), 'xb') as rerr:
            p = subprocess.Popen(command, cwd=self.wrapper, env=ENV, stdin=subprocess.DEVNULL,
                                 stdout=rout, stderr=rerr, close_fds=True, preexec_fn=file_limits)
            try:
                runner = identity(p.pid)
                if runner is not None:
                    self.check_maps(runner)
                emit(self.mount / (label + '.runner-live.json'), {'utc': now().isoformat(), 'identity': runner,
                     'expected_argv': command, 'actual_match': runner is not None and runner['argv'] == command})
                while p.poll() is None:
                    if live is None:
                        children = pathlib.Path('/proc') / str(p.pid) / 'task' / str(p.pid) / 'children'
                        try:
                            for pid in children.read_text().split():
                                item = identity(int(pid))
                                if item and item['argv'] == py and item['pgid'] == item['pid']:
                                    need(item['uid'] == [str(self.r['uid'])] * 4 and item['gid'] == [str(self.r['gid'])] * 4, 'actual science identity')
                                    need(item['pid_namespace'] == self.r['pid_namespace'], 'child namespace')
                                    need(item['caps']['NoNewPrivs'] == '1' and all(int(item['caps'][key], 16) == 0
                                         for key in ('CapInh', 'CapPrm', 'CapEff')), 'science effective capabilities')
                                    self.check_maps(item)
                                    live = item
                                    emit(self.mount / (label + '.python-live.json'), {'utc': now().isoformat(), 'identity': live})
                        except FileNotFoundError:
                            pass
                    self.budget(); self.size_budget()
                    need(time.monotonic() - before < wall + 15, 'late CAPRUN return')
                    time.sleep(0.05)
            finally:
                if p.poll() is None:
                    p.send_signal(signal.SIGTERM)
                    p.wait(timeout=15)
        self.group_quiet()  # no terminal telemetry/hash/payload reads before group quiet
        self.revalidate(); self.size_budget()
        need(sha(auth) == digest and (input_path is None or sha(immutable(input_path)) == input_hash), 'postlaunch frozen pin drift')
        need(time.monotonic() - self.begin <= 3000 and now() < self.end and self.cpu() - self.cpu_start <= 2100, 'joint post-return cap')
        t = load(tel)
        expected_hash = hashlib.sha256((json.dumps(child, ensure_ascii=False, separators=(',', ':')) + '\n').encode()).hexdigest()
        need(t.get('schema') == 'CAPRUN/v1' and t['argv_sha256'] == expected_hash and t['argv_count'] == len(child), 'CAPRUN command binding')
        need(t['runner_exit_code'] == p.returncode and t['cwd'] == str(self.source), 'CAPRUN result/cwd')
        need(t['caps']['wall_seconds'] == wall and t['caps']['cpu_seconds'] == cpu and t['caps']['rss_bytes'] == rss, 'CAPRUN limits')
        need(type(t['pid']) is int and t['pid'] == t['pgid'] and t['start_identity'].startswith('boot=' + self.r['boot_id'] + ';start_ticks='), 'CAPRUN leader identity')
        current = identity(t['pid'])
        need(current is None or 'boot=' + current['boot_id'] + ';start_ticks=' + current['start_ticks'] != t['start_identity'], 'leader not reaped')
        for key, path in (('stdout', out), ('stderr', err)):
            need(t[key]['path'] == str(path) and t[key]['sha256'] == sha(path) and t[key]['bytes'] == path.stat().st_size, 'terminal stream binding')
        record = {'label': label, 'utc': now().isoformat(), 'telemetry_sha256': sha(tel),
                  'authorization_sha256': digest, 'source_pins': self.science, 'native_sha256': sha(self.native_path),
                  'actual_python_live_observed': live is not None, 'runner_live_observed': runner is not None and runner['argv'] == command,
                  'owned_group_quiet': True, 'status': t['status'], 'resource': t['resource'], 'input_sha256': input_hash}
        emit(self.mount / (label + '.post.json'), record); self.runs.append(record)
        if label in ('produce', 'check-positive', 'mutate', 'check-negative'):
            need(live is not None and runner is not None and runner['argv'] == command, 'GAP: required live capture missed; no retry')
        return t, out, err, payload

    def normal(self, t, code):
        need(t['status'] == 'NORMAL_EXIT' and t['resource'] is None and t['child_returncode'] == code, 'unexpected control/phase outcome')

    def execute(self):
        for label in LABELS[:5]:
            t, out, err, payload = self.run(label, 'produce', 'control')
            spec = self.refusals[label]
            self.normal(t, spec['exit_code'])
            need(t['child_signal'] is None and not payload.exists() and out.read_bytes() == b''
                 and err.read_bytes() == spec['stderr'].encode('ascii'), 'exact actual producer-entry refusal')
        t, out, err, payload = self.run('valid', 'probe', 'control')
        self.normal(t, 0)
        event = load(payload)
        need(event['event'] == 'ROOT_POLICY_ONLY_SENTINEL' and event['identity']['uid'] == self.r['uid'] and event['identity']['gid'] == self.r['gid'], 'ROOT policy sentinel, not science authorization')
        need(out.read_bytes() == err.read_bytes() == b'', 'valid control streams')
        for role in ('produce', 'check'):
            t, out, err, payload = self.run('startup-' + role, role, 'control')
            spec = self.refusals['startup-' + role]
            self.normal(t, spec['exit_code'])
            need(t['child_signal'] is None and not payload.exists() and out.read_bytes() == b''
                 and err.read_bytes() == spec['stderr'].encode('ascii'), 'actual entry exact startup refusal')
        t, out, err, payload = self.run('dummy', 'probe', 'dummy')
        term = t['termination']
        need(t['status'] == 'RESOURCE_CAP' and t['resource'] == 'rss' and term['term_sent'] is True and term['kill_sent'] is True
             and term['leader_reaped'] is True and term['cleanup_complete'] is True and not term['group_live_before_reap'], 'descendant TERM/KILL cleanup')
        for stage, sig in (('before-term', 15), ('before-kill', 9)):
            checks = [x for x in t['identity_checks'] if x.get('stage') == stage]
            sends = [x for x in t['identity_checks'] if x.get('stage') == stage + '-send']
            need(len(checks) == len(sends) == 1 and checks[0]['result'] == 'MATCH' and checks[0]['observed_pid'] == t['pid']
                 and checks[0]['observed_pgid'] == t['pgid'] and checks[0]['observed_start_identity'] == t['start_identity']
                 and sends[0]['result'] == 'SENT' and sends[0]['signal'] == sig, 'exact dummy signal identity')
        events = [json.loads(line) for line in payload.read_text().splitlines()]
        need([e['event'] for e in events] == ['parent_started', 'child_ready_ignoring_term', 'parent_exit_pending', 'orphan_allocated_64MiB'], 'dummy sequence')
        need(events[0]['identity'] == events[2]['identity'] and events[1]['identity'] == events[3]['identity']
             and events[0]['identity']['pid'] == t['pid'] and events[1]['identity']['pid'] != t['pid'], 'dummy parent/descendant identity')
        need(all(e['identity']['pgid'] == t['pgid'] and e['identity']['pid_namespace'] == self.r['pid_namespace'] for e in events)
             and t['max_observed_group_rss_bytes'] > 33554432, 'dummy actual group RSS')
        t, out, err, packet = self.run('produce', 'produce', 'produce')
        self.normal(t, 0)
        need(out.read_bytes() == b'FORMED_UNCHECKED_NECESSARY_ROWS_25_NO_SOURCE_OUTCOME\n' and err.read_bytes() == b'', 'producer literal verdict')
        need(packet.is_file() and not packet.is_symlink() and 0 < packet.stat().st_size <= PACKET, 'formed packet size')
        target = self.freeze(packet, 'artifact.json')
        digest = sha(target)
        t, out, err, ignored = self.run('check-positive', 'check', 'check', target)
        self.normal(t, 0)
        need(out.read_bytes() == b'CHECKED_NECESSARY_ROWS_25_NO_SOURCE_OUTCOME\n'
             and err.read_bytes() == b'', 'independent checker literal verdict')
        phase = {'schema': 'f10-necessary-rows-positive-phase/v1', 'status': 'POSITIVE_CHECKED_NO_SOURCE_OUTCOME',
                 'root_registration_sha256': self.root_sha, 'input': {'path': str(target),
                 'sha256': digest, 'bytes': target.stat().st_size}, 'source_files': self.science,
                 'authorization': {'path': str(self.auth / 'check-positive.json'),
                 'sha256': sha(self.auth / 'check-positive.json')},
                 'checker_stdout_sha256': sha(out), 'policy': self.r['phase_policy']}
        self.frozen_pins[str(self.auth / 'positive.json')] = emit(self.auth / 'positive.json', phase)
        syncdir(self.auth)
        t, out, err, ignored = self.run('mutate', 'mutate', 'mutate', target)
        self.normal(t, 0)
        need(out.read_bytes() == err.read_bytes() == b'', 'silent mutator completion')
        fixture = self.writer / 'mixed-row.json'
        receipt = load(self.writer / 'mutation.json')
        need(set(receipt) == {'schema', 'status', 'root_registration_sha256', 'input_sha256',
             'output_sha256', 'output_bytes', 'mutation', 'inverse_restored_whole_bytes', 'checker_run'}
             and receipt['schema'] == 'f10-necessary-rows-T-mutation/v1'
             and receipt['status'] == 'FORMED_UNCHECKED' and receipt['root_registration_sha256'] == self.root_sha
             and receipt['input_sha256'] == digest and receipt['mutation'] == 'graph.slots[24] += X1^27 over ROOT place'
             and receipt['inverse_restored_whole_bytes'] is True and receipt['checker_run'] is False,
             'exact unchecked mutation receipt')
        need(fixture.is_file() and not fixture.is_symlink() and type(receipt['output_bytes']) is int
             and fixture.stat().st_size == receipt['output_bytes'] and sha(fixture) == receipt['output_sha256']
             and receipt['output_sha256'] != digest, 'actual changed fixture pin/size')
        need(set(p.name for p in self.writer.iterdir()) == {'valid.payload', 'dummy.payload',
             'mixed-row.json', 'mutation.json'}, 'exact one-fixture writer inventory')
        fixture = self.freeze(fixture, 'mixed-row.json')
        self.freeze(self.writer / 'mutation.json', 'mutation.json')
        os.chmod(self.frozen, 0o555); syncdir(self.frozen); syncdir(self.mount)
        t, out, err, ignored = self.run('check-negative', 'check', 'check', fixture)
        self.normal(t, 2)
        need(t['child_signal'] is None and t['child_exit_code'] == 2 and out.read_bytes() == b''
             and err.read_bytes() == b'CHECK FAILED: direct-source graph slot T\n', 'exact normal semantic exit2, no traceback')
        need(tuple(x['label'] for x in self.runs) == LABELS, 'exact thirteen completed commands')
        result = {'status': 'NECESSARY_ROWS_AND_T_REJECTION_CHECKED_NO_SOURCE_OUTCOME',
                  'baseline_sha256': digest, 'fixture_sha256': sha(fixture), 'source_files': self.science,
                  'negative_predicate': 'direct-source graph slot T', 'other_five_semantic_controls': 'NOT_RUN_SPEC',
                  'root_registration_sha256': self.root_sha, 'joint_wall_seconds': time.monotonic() - self.begin,
                  'joint_cgroup_cpu_seconds': self.cpu() - self.cpu_start, 'science_outcome': 'NONE'}
        emit(self.mount / 'final-binding.json', result)
        return result

    def freeze(self, source, name):
        self.group_quiet(); self.size_budget()
        need(source.is_file() and not source.is_symlink(), 'regular freeze source')
        target = self.frozen / name
        need(not target.exists(), 'fresh frozen target')
        digest = sha(source)
        os.rename(source, target); os.chown(target, 0, 0); os.chmod(target, 0o444)
        with open(target, 'rb') as f:
            os.fsync(f.fileno())
        syncdir(self.writer); syncdir(self.frozen)
        need(sha(immutable(target)) == digest, 'move/freeze identity')
        self.frozen_pins[str(target)] = digest
        return target

    def durable_copy(self, result):
        self.group_quiet(); self.size_budget()
        self.custody_budget()
        self.durable.mkdir(mode=0o700); records = []
        for parent, dirs, names in os.walk(self.mount, followlinks=False):
            need(all(not (pathlib.Path(parent) / d).is_symlink() for d in dirs), 'custody directory symlink')
            for name in sorted(names):
                self.custody_budget()
                source = pathlib.Path(parent) / name
                need(source.is_file() and not source.is_symlink(), 'custody regular file')
                target = self.durable / source.relative_to(self.mount)
                target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                with open(source, 'rb') as src, open(target, 'xb') as dst:
                    shutil.copyfileobj(src, dst, 1048576); dst.flush(); os.fsync(dst.fileno())
                os.chmod(target, 0o444)
                need(sha(target) == sha(source), 'durable byte identity')
                records.append({'path': str(target.relative_to(self.durable)), 'bytes': target.stat().st_size, 'sha256': sha(target)})
                need(len(records) <= 200, 'bounded custody file inventory')
        emit(self.durable / 'CUSTODY.json', {'schema': 'f10-necessary-rows-runtime-custody/v1', 'result': result,
             'root_sha256': self.root_sha, 'runs': self.runs, 'files': records, 'science_outcome': 'NONE'})
        for parent, dirs, names in os.walk(self.durable, topdown=False):
            syncdir(parent)
        syncdir(self.durable.parent)
        self.custody_budget()

    def custody_budget(self):
        need(now() < self.task_end and time.monotonic() - self.begin <= 3000
             and self.cpu() - self.cpu_start <= 2100, 'joint original custody wall/CPU/task cutoff')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--registration', required=True); args = p.parse_args()
    batch = None; result = {'status': 'STOP_NONDECISION', 'reason': 'not launched'}
    try:
        batch = Batch(args.registration)
        result = batch.execute()
    except Exception as exc:
        result = {'status': 'STOP_NONDECISION', 'reason': str(exc)[:500]}
    if batch is None:
        print(json.dumps(result)); return 2
    try:
        batch.durable_copy(result)
    except Exception as exc:
        print(json.dumps({'status': 'STOP_CUSTODY_INCOMPLETE', 'reason': str(exc)[:500],
                          'ROOT_terminal_cleanup_capture_required': True}))
        return 2
    # ROOT reads durable custody only after this writer is terminal. No output
    # after successful copy; no deletion, unmount, retry or worker-stop here.
    return 0 if result['status'] == 'NECESSARY_ROWS_AND_T_REJECTION_CHECKED_NO_SOURCE_OUTCOME' else 2


if __name__ == '__main__':
    raise SystemExit(main())
