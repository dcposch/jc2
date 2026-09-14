"""r2 two-refusal map observer, STATIC/UNEXECUTED; fresh ROOT registration only.

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

JOB = 'f10-r2-reconstruction-v1'
CONTROL_JOB = 'f10-r2-native-map-observer-v1'
CAPRUN_SHA = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
SCIENCE = {
    'authority.py': '2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b',
    'arithmetic.py': 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345',
    'produce.py': 'eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10',
    'check_arithmetic.py': 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e',
    'check.py': 'e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0'}
LIMITS = {'wall_seconds': '600', 'cpu_seconds': '500', 'memory_bytes': '2147483648',
          'aggregate_bytes': '16777216'}
PROFILES = {'control': [5, 3, 2147483648]}
LABELS = ('refuse-status', 'refuse-caps')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
TOTAL, PACKET, META = 16777216, 15728640, 1048576


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
    observed_start = now().isoformat()
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
                'mapped_files': sorted(mapped),
                'observation_started_utc': observed_start,
                'observation_finished_utc': now().isoformat()}
    except FileNotFoundError:
        return None


class Batch:
    def __init__(self, name):
        self.begin = time.monotonic()
        need(os.geteuid() == 0 and sys.platform == 'linux', 'ROOT Linux only')
        self.path = immutable(name); self.root_sha = sha(self.path); self.r = load(self.path)
        need(stat.S_IMODE(self.path.stat().st_mode) == 0o444, 'ROOT registration 0444')
        r = self.r
        need(r.get('schema') == 'f10-r2-map-observer-runtime/v1' and r.get('enabled') is True, 'disabled ROOT registration')
        need(r['jobtag'] == CONTROL_JOB and r['exclusive_no_concurrent_writer'] is True, 'job/exclusivity')
        need(r['limits'] == LIMITS and r['profiles'] == PROFILES, 'fixed cap profiles')
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
        self.cpu_start = self.cpu()
        self.files = {k: immutable(v, k not in ('python', 'setpriv')) for k, v in r['files'].items()}
        need(set(self.files) == {'python', 'setpriv', 'caprun', 'dispatcher', 'probe'}, 'exact wrapper roles')
        need(str(self.files['python']) == os.path.realpath(sys.executable), 'interpreter')
        need(self.files['dispatcher'] == pathlib.Path(__file__).resolve(), 'dispatcher identity')
        self.source = directory(r['science_dir'], 0o755)
        self.wrapper = directory(r['wrapper_dir'], 0o755)
        need(self.source != self.wrapper and os.getcwd() == str(self.wrapper), 'separate wrapper cwd')
        need(self.files['dispatcher'].parent == self.wrapper and self.files['probe'].parent == self.wrapper,
             'exact wrapper siblings')
        outer = [str(self.files['python']), '-I', '-S', '-B', str(self.files['dispatcher']), '--registration', str(self.path)]
        need(r['outer_argv'] == outer and identity(os.getpid())['argv'] == outer, 'literal ROOT argv')
        self.pins = r['pins']
        for p in self.files.values():
            need(str(p) in self.pins, 'role path pin')
        need(self.pins[str(self.files['caprun'])] == CAPRUN_SHA, 'unchanged CAPRUN')
        for name, h in SCIENCE.items():
            need(self.pins.get(str(self.source / name)) == h, 'actual science role pin: ' + name)
        self.native_path = immutable(r['native_manifest'])
        need(self.pins.get(str(self.native_path)) == sha(self.native_path), 'native manifest pin')
        self.native = load(self.native_path, 1048576)
        need(self.native.get('schema') == 'f10-native-closure/v1', 'native closure schema')
        need(set(self.native) == {'schema', 'files', 'directories', 'aliases', 'absent', 'python_path'}, 'complete native inventory fields')
        need(self.native['python_path'] == sys.path, 'exact -I -S native path')
        need(0 < len(self.native['files']) <= 3000 and 0 < len(self.native['directories']) <= 1000, 'bounded native closure')
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
                 list(self.files.values()) + [self.path, self.native_path]), 'all code/native/registration outside tmpfs')
        need(all(pathlib.Path(p) != self.mount and self.mount not in pathlib.Path(p).parents
                 for p in self.native['files']), 'native files outside tmpfs')
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
        need(now() < self.end < self.task_end, 'original deadlines')
        need(set(r['commands']) == set(LABELS), 'exact two command registrations')
        self.runs = []; self.used_labels = set()
        self.current_label = 'initialization'; self.current_phase = 'initial-validation'
        # First map validation occurs in execute, after main owns this Batch.
        # Thus strict rejection can still receive terminal durable custody.

    def deadline(self, value):
        need(isinstance(value, str) and value.endswith('+00:00'), 'literal UTC deadline')
        return datetime.datetime.fromisoformat(value)

    def cpu(self):
        records = dict(line.split() for line in (self.cg / 'cpu.stat').read_text().splitlines())
        return int(records['usage_usec']) / 1000000

    def budget(self, reserve=0):
        need(time.monotonic() - self.begin + reserve < 600 and now() + datetime.timedelta(seconds=reserve) < self.end, 'joint/original wall')
        need(self.cpu() - self.cpu_start < 480, 'CPU safety cutoff; 20 seconds cleanup reserve')

    def revalidate(self):
        need(sha(self.path) == self.root_sha, 'ROOT registration drift')
        need(socket.gethostname() == self.r['hostname']
             and pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == self.r['instance_id']
             and pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == self.r['boot_id']
             and os.readlink('/proc/self/ns/pid') == self.r['pid_namespace'], 'current host/instance/boot/namespace')
        need(pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + str(self.cg)[len('/sys/fs/cgroup'):]
             and (self.cg / 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'current cgroup/cap')
        need(set(p.name for p in self.source.iterdir()) == set(SCIENCE), 'EXACT five-file science directory')
        need(set(p.name for p in self.wrapper.iterdir()) == {'dispatch.py', 'probe.py'}, 'EXACT two-file wrapper directory')
        directory(self.source, 0o755); directory(self.wrapper, 0o755)
        for p, h in list(self.pins.items()) + list(self.native['files'].items()):
            need(re.fullmatch(r'[0-9a-f]{64}', h) and sha(immutable(p, p not in self.native['files'] and p not in (str(self.files['python']), str(self.files['setpriv'])))) == h, 'current pin')
        for name, h in SCIENCE.items():
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

    def check_maps(self, item, role='dispatcher'):
        # A separately read /proc record is NOT an atomic or validated image.
        rejected = None
        reason = 'live identity unavailable' if item is None else None
        if item is not None:
            for path in item['mapped_files']:
                resolved = str(pathlib.Path(path).resolve())
                member = resolved in self.native['files']
                alias_required = path != resolved
                alias_member = self.native['aliases'].get(path) == resolved
                if not member or (alias_required and not alias_member):
                    reason = 'mapped native file not pinned' if not member else 'mapped native alias not pinned'
                    rejected = {'raw_path': path, 'resolved_path': resolved,
                                'file_member': member, 'alias_required': alias_required,
                                'alias_member': alias_member}
                    break
        if reason is None:
            return
        need(self.current_label in ('initialization',) + LABELS
             and self.current_phase in ('initial-validation', 'prelaunch', 'runner-startup',
                                        'child-observation', 'post-return')
             and role in ('dispatcher', 'caprun-runner', 'probe-child'), 'diagnostic context')
        observation = {'schema': 'f10-r2-unvalidated-map-observation/v1',
                       'status': 'UNVALIDATED_MAP_REJECTION', 'science_outcome': 'NONE',
                       'root_registration_sha256': self.root_sha,
                       'native_manifest_sha256': self.pins[str(self.native_path)],
                       'label': self.current_label, 'phase': self.current_phase, 'role': role,
                       'rejection_utc': now().isoformat(), 'reason': reason,
                       'snapshot': item, 'first_rejected': rejected,
                       'non_atomic_proc_reads': True, 'validation_passed': False}
        raw = (json.dumps(observation, sort_keys=True, separators=(',', ':')) + '\n').encode()
        need(len(raw) <= 65536, 'STOP_MAP_OBSERVATION_RECORD_CAP: ' + reason)
        self.size_budget(additional=len(raw))
        # One fixed exclusive path: no retry, overwrite, or favorable resampling.
        emit(self.mount / 'map-rejection.UNVALIDATED.json', observation)
        syncdir(self.mount)
        raise RuntimeError(reason)

    def group_quiet(self):
        for text in (self.cg / 'cgroup.procs').read_text().split():
            if int(text) != os.getpid():
                p = identity(int(text))
                need(p is None or p['state'] == 'Z', 'owned cgroup still live; ROOT recovery required')

    def size_budget(self, additional=0):
        need(type(additional) is int and 0 <= additional <= 65536, 'metadata reservation')
        metadata = additional
        for parent, dirs, names in os.walk(self.mount, followlinks=False):
            need(all(not (pathlib.Path(parent) / d).is_symlink() for d in dirs), 'output directory symlink')
            for name in names:
                p = pathlib.Path(parent) / name
                need(p.is_file() and not p.is_symlink(), 'output regularity')
                metadata += p.stat().st_size
        need(metadata <= META, '1MiB metadata reserve exceeded')

    def authorize(self, label):
        obj = {'job_tag': JOB, 'status': 'REGISTERED', 'authority': 'ROOT-CAPRUN',
               'files': dict(SCIENCE), 'runtime': {'python_sha256': self.pins[str(self.files['python'])],
               'native_inventory_sha256': sha(self.native_path)}, 'limits': dict(LIMITS)}
        if label == 'refuse-status': obj['status'] = 'DISABLED'
        if label == 'refuse-caps': obj['limits']['cpu_seconds'] = '499'
        p = self.auth / (label + '.json')
        digest = emit(p, obj); immutable(p)
        return p, digest

    def run(self, label):
        need(label in LABELS and label not in self.used_labels, 'exact label/no retry')
        self.used_labels.add(label)
        self.current_label = label; self.current_phase = 'prelaunch'
        self.group_quiet(); self.revalidate()
        wall, cpu, rss = PROFILES['control']
        self.budget(wall + 15)
        payload = self.writer / (label + '.payload')
        auth, digest = self.authorize(label)
        supplied = digest
        tail = ['--registered-job', JOB, '--authorization', str(auth),
                '--authorization-sha256', supplied, '--output', str(payload)]
        script = [str(self.files['probe']), '--science-dir', str(self.source),
                  '--mode', 'authorize', '--'] + tail
        py = [str(self.files['python']), '-E', '-s', '-S', '-B'] + script
        child = [str(self.files['setpriv']), '--reuid', str(self.r['uid']), '--regid', str(self.r['gid']),
                 '--clear-groups', '--no-new-privs', '--'] + py
        out, err, tel = [self.mount / (label + suffix) for suffix in ('.stdout', '.stderr', '.telemetry.json')]
        command = [str(self.files['python']), '-I', '-S', '-B', str(self.files['caprun']),
                   '--wall-seconds', str(wall), '--cpu-seconds', str(cpu), '--rss-bytes', str(rss),
                   '--rss-sample-seconds', '0.05', '--term-grace-seconds', '1',
                   '--stdout-file', str(out), '--stderr-file', str(err), '--telemetry-file', str(tel),
                   '--cwd', str(self.source), '--'] + child
        registered = self.r['commands'][label]
        need(type(registered) is list and all(type(x) is str for x in registered), 'registered command strings')
        need(command == registered, 'literal ROOT CAPRUN argv mismatch')
        input_hash = None
        emit(self.mount / (label + '.pre.json'), {'utc': now().isoformat(), 'root_sha256': self.root_sha,
             'authorization_sha256': digest, 'supplied_authorization_sha256': supplied,
             'native_sha256': sha(self.native_path), 'source_pins': SCIENCE, 'input_sha256': input_hash,
             'argv': command, 'python_argv': py, 'parent': identity(os.getpid()), 'profile': PROFILES['control']})
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
                self.current_phase = 'runner-startup'
                runner = identity(p.pid)
                self.check_maps(runner, 'caprun-runner')
                emit(self.mount / (label + '.runner-live.json'), {'utc': now().isoformat(), 'identity': runner,
                     'expected_argv': command, 'actual_match': runner is not None and runner['argv'] == command})
                while p.poll() is None:
                    if live is None:
                        children = pathlib.Path('/proc') / str(p.pid) / 'task' / str(p.pid) / 'children'
                        try:
                            child_ids = children.read_text().split()
                        except FileNotFoundError:
                            child_ids = []
                        # Only the disappearing /proc children listing is tolerated;
                        # failure-evidence writes must never be swallowed here.
                        for pid in child_ids:
                            item = identity(int(pid))
                            if item and item['argv'] == py and item['pgid'] == item['pid']:
                                need(item['uid'] == [str(self.r['uid'])] * 4 and item['gid'] == [str(self.r['gid'])] * 4, 'actual science identity')
                                need(item['pid_namespace'] == self.r['pid_namespace'], 'child namespace')
                                need(item['caps']['NoNewPrivs'] == '1' and all(int(item['caps'][key], 16) == 0
                                     for key in ('CapInh', 'CapPrm', 'CapEff')), 'science effective capabilities')
                                self.current_phase = 'child-observation'
                                self.check_maps(item, 'probe-child')
                                live = item
                                emit(self.mount / (label + '.python-live.json'), {'utc': now().isoformat(), 'identity': live})
                    self.budget(); self.size_budget()
                    need(time.monotonic() - before < wall + 15, 'late CAPRUN return')
                    time.sleep(0.05)
            finally:
                if p.poll() is None:
                    p.send_signal(signal.SIGTERM)
                    p.wait(timeout=15)
        self.group_quiet()  # no terminal telemetry/hash/payload reads before group quiet
        self.current_phase = 'post-return'
        self.revalidate(); self.size_budget()
        need(sha(auth) == digest, 'postlaunch frozen pin drift')
        need(time.monotonic() - self.begin <= 600 and now() < self.end and self.cpu() - self.cpu_start <= 500, 'joint post-return cap')
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
                  'authorization_sha256': digest, 'source_pins': SCIENCE, 'native_sha256': sha(self.native_path),
                  'actual_python_live_observed': live is not None, 'runner_live_observed': runner is not None and runner['argv'] == command,
                  'owned_group_quiet': True, 'status': t['status'], 'resource': t['resource'], 'input_sha256': input_hash}
        emit(self.mount / (label + '.post.json'), record); self.runs.append(record)
        need(runner is not None and runner['argv'] == command, 'STOP: actual runner identity mismatch')
        need(live is not None, 'STOP: probe live identity unobserved; no retry')
        return t, out, err, payload

    def normal(self, t, code):
        need(t['status'] == 'NORMAL_EXIT' and t['resource'] is None and t['child_returncode'] == code, 'unexpected control/phase outcome')

    def execute(self):
        self.revalidate(); self.group_quiet()
        reasons = (('refuse-status', 'no registered ROOT CAPRUN contract'),
                   ('refuse-caps', 'registered limits/source inventory'))
        for label, reason in reasons:
            t, out, err, payload = self.run(label)
            self.normal(t, 1)
            need(not payload.exists() and out.read_bytes() == b''
                 and err.read_text() == 'REFUSED: ' + reason + '\n', 'exact no-math refusal')
        need(tuple(run['label'] for run in self.runs) == LABELS, 'exact completed two-child sequence')
        need(not list(self.writer.iterdir()) and not list(self.frozen.iterdir()), 'no diagnostic payloads')
        result = {'status': 'DIAGNOSTIC_NO_MAP_FAILURE_OBSERVED', 'science_outcome': 'NONE',
                  'completed_labels': list(LABELS), 'science_pins': SCIENCE,
                  'root_registration_sha256': self.root_sha,
                  'no_repair_or_retry_permission': True,
                  'joint_wall_seconds': time.monotonic() - self.begin,
                  'joint_cgroup_cpu_seconds': self.cpu() - self.cpu_start}
        self.size_budget(additional=4096)
        emit(self.mount / 'diagnostic-result.json', result)
        return result

    def durable_copy(self, result):
        self.group_quiet(); self.size_budget()
        need(now() < self.task_end, 'custody deadline')
        self.durable.mkdir(mode=0o700); records = []
        for parent, dirs, names in os.walk(self.mount, followlinks=False):
            need(all(not (pathlib.Path(parent) / d).is_symlink() for d in dirs), 'custody directory symlink')
            for name in sorted(names):
                need(now() < self.task_end, 'custody cutoff')
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
        emit(self.durable / 'CUSTODY.json', {'schema': 'f10-r2-map-observer-custody/v1', 'result': result,
             'root_sha256': self.root_sha, 'runs': self.runs, 'files': records, 'science_outcome': 'NONE'})
        for parent, dirs, names in os.walk(self.durable, topdown=False):
            syncdir(parent)
        syncdir(self.durable.parent)
        need(now() < self.task_end, 'final custody cutoff')


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
    return 0 if result['status'] == 'DIAGNOSTIC_NO_MAP_FAILURE_OBSERVED' else 2


if __name__ == '__main__':
    raise SystemExit(main())
