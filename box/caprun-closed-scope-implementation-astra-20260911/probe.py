"""ROOT-policy-only sentinel/dummy. Never imports scientific authority or arithmetic."""
import datetime
import hashlib
import json
import os
import pathlib
import re
import socket
import stat
import sys

JOB = 'f10-source-cone-r3-necessary-rows-v1'
SOURCE_NAMES = ('authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py')
LIMITS = {'wall_seconds': '900', 'cpu_seconds': '600', 'memory_bytes': '8589934592', 'aggregate_bytes': '134217728'}
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}


def need(ok, why):
    if not ok:
        raise ValueError('ROOT POLICY REFUSED: ' + why)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as stream:
        for part in iter(lambda: stream.read(1048576), b''):
            h.update(part)
    return h.hexdigest()


def pairs(items):
    obj = {}
    for key, value in items:
        need(key not in obj, 'duplicate metadata key')
        obj[key] = value
    return obj


def file(name, strict=True):
    p = pathlib.Path(name)
    need(p.is_absolute() and str(p.resolve()) == str(p) and not p.is_symlink(), 'canonical file')
    info = p.stat()
    need(stat.S_ISREG(info.st_mode) and info.st_uid == 0 and info.st_mode & 0o004
         and not info.st_mode & (0o222 if strict else 0o022), 'ROOT immutable file')
    for d in p.parents:
        st = d.stat()
        need(stat.S_ISDIR(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022
             and st.st_mode & 0o005 == 0o005, 'ROOT traversable ancestry')
    return p


def load(p, ceiling=65536):
    need(p.stat().st_size <= ceiling, 'metadata byte cap')
    return json.loads(p.read_bytes(), object_pairs_hook=pairs)


def identity():
    raw = pathlib.Path('/proc/self/stat').read_text()
    f = raw[raw.rfind(')') + 2:].split()
    return {'pid': os.getpid(), 'pgid': os.getpgrp(), 'uid': os.getuid(), 'gid': os.getgid(),
            'start_ticks': f[19], 'boot_id': pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'pid_namespace': os.readlink('/proc/self/ns/pid'),
            'cgroup': pathlib.Path('/proc/self/cgroup').read_text().strip()}


def root_policy(root_name, role, label, actual):
    # ROOT0444/no-concurrent-writer trust; command contains no recursive ROOT hash.
    root = file(root_name); r = load(root); root_hash = sha(root)
    need(r.get('schema') == 'f10-necessary-rows-runtime/closed-child-v1' and r.get('enabled') is True
         and r.get('jobtag') == JOB and r.get('exclusive_no_concurrent_writer') is True, 'enabled ROOT policy')
    need(r['review_clearance']['status'] == 'SOURCE_AND_RUNTIME_FIRST_CONFIRMED', 'ROOT FIRST clearance')
    need(type(r.get('closed_scope_first_sha256')) is str and re.fullmatch(r'[0-9a-f]{64}', r['closed_scope_first_sha256']), 'closed-scope FIRST')
    early = ['refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source', 'refuse-hash',
             'valid', 'startup-produce', 'startup-check', 'dummy']
    full = early + ['produce', 'check-positive', 'mutate', 'check-negative']
    need(r.get('execution_mode') in ('PREFLIGHT_ONLY_9', 'FULL_13')
         and r['allowed_phases'] == (early if r['execution_mode'] == 'PREFLIGHT_ONLY_9' else full)
         and set(r['commands']) == set(r['allowed_phases']) and label in r['allowed_phases'], 'ROOT exact phase mode')
    need(role != 'mutator' or r['execution_mode'] == 'FULL_13', 'no preflight-only mutator authority')
    stops = [datetime.datetime.fromisoformat(r[k]) for k in ('admission_deadline_utc', 'mathematical_deadline_utc', 'task_deadline_utc', 'worker_deadline_utc')]
    need(all(x.utcoffset() == datetime.timedelta(0) for x in stops)
         and datetime.datetime.now(datetime.timezone.utc) < stops[0] <= stops[1] < stops[2] < stops[3], 'immutable UTC stops')
    need(r['source_limits'] == LIMITS and r['environment'] == ENV == dict(os.environ), 'caps/environment')
    need(sys.platform == 'linux' and os.getuid() == r['uid'] > 0 and os.getgid() == r['gid'] > 0, 'science UID/GID')
    need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2'
         and pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == r['instance_id']
         and socket.gethostname() == r['hostname'], 'actual EC2 identity')
    need(pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == r['boot_id']
         and os.readlink('/proc/self/ns/pid') == r['pid_namespace'], 'boot/namespace')
    cg = pathlib.Path(r['cgroup_path'])
    guard = r['closed_child_guard']
    need(type(guard) is dict and set(guard) == {'schema', 'outer_device', 'outer_inode', 'root_no_migration', 'leaves'}
         and guard['schema'] == 'CAPRUN-closed-child/v1' and guard['root_no_migration'] is True
         and set(guard['leaves']) == set(r['allowed_phases']), 'ROOT closed membership contract')
    spec = guard['leaves'][label]
    need(type(spec) is dict and set(spec) == {'path', 'device', 'inode'}, 'literal child metadata')
    child = pathlib.Path(spec['path'])
    need(str(cg).startswith('/sys/fs/cgroup/') and str(cg.resolve()) == str(cg)
         and child.parent == cg and child.name == label and str(child.resolve()) == str(child)
         and pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + str(child)[len('/sys/fs/cgroup'):]
         and (cg / 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'outer cap and exact child membership')
    for path, dev, ino in ((cg, guard['outer_device'], guard['outer_inode']), (child, spec['device'], spec['inode'])):
        st = path.stat()
        need(type(dev) is int and type(ino) is int and dev > 0 and ino > 0
             and (st.st_dev, st.st_ino) == (dev, ino) and st.st_uid == 0 and not st.st_mode & 0o022
             and stat.S_ISDIR(st.st_mode), 'immutable root cgroup identity')
        need((path / 'cgroup.type').read_text().strip() == 'domain'
             and not (path / 'cgroup.subtree_control').read_text().strip(), 'outer domain/no delegated controllers')
        for field in ('cgroup.procs', 'cgroup.threads', 'cgroup.subtree_control', 'cgroup.events'):
            st = (path / field).lstat()
            need(stat.S_ISREG(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022, 'no workload migration write access')
    need(set(p.name for p in cg.iterdir() if p.is_dir()) == set(r['allowed_phases'])
         and not any(p.is_dir() for p in child.iterdir()), 'exact root-owned closed leaves')
    me = file(str(pathlib.Path(__file__).resolve()))
    need(str(me) == r['files'][role] and sha(me) == r['pins'][str(me)], 'own source pin')
    py = file(r['files']['python'], False)
    need(str(py) == os.path.realpath(sys.executable) and sha(py) == r['pins'][str(py)], 'interpreter')
    need(sys.flags.optimize == 0 and sys.flags.no_site == 1, 'ordinary no-site startup')
    command = list(r['commands'][label])
    if role == 'mutator':
        flag = '--root-registration-sha256'
        need(command.count(flag) == command.count('ROOT_REGISTRATION_SHA256') == 1
             and command[command.index(flag) + 1] == 'ROOT_REGISTRATION_SHA256', 'single ROOT hash slot')
        command[command.index(flag) + 1] = root_hash
    need(command[-len(actual):] == actual and pathlib.Path('/proc/self/cmdline').read_bytes().rstrip(b'\0').decode().split('\0') == actual, 'actual exact ROOT command suffix')
    source = pathlib.Path(r['science_dir']); wrapper = pathlib.Path(r['wrapper_dir'])
    need(str(source.resolve()) == str(source) and str(wrapper.resolve()) == str(wrapper)
         and set(os.listdir(source)) == set(SOURCE_NAMES)
         and set(os.listdir(wrapper)) == {'dispatch.py', 'probe.py', 'mutate.py'}, 'isolated inventories')
    native_path = file(r['native_manifest']); native = load(native_path, 1048576)
    need(sha(native_path) == r['pins'][str(native_path)] and set(native) == {'schema', 'files', 'directories', 'aliases', 'absent', 'python_path'}
         and native['schema'] == 'f10-native-closure/v1'
         and 0 < len(native['files']) <= 3000 and 0 < len(native['directories']) <= 1000, 'full native closure')
    for path, digest in list(r['pins'].items()) + list(native['files'].items()):
        need(type(digest) is str and re.fullmatch(r'[0-9a-f]{64}', digest)
             and sha(file(path, path not in native['files'] and path not in (r['files']['python'], r['files']['setpriv']))) == digest, 'current code/native pin')
    for name in SOURCE_NAMES:
        p = file(str(source / name))
        need(sha(p) == r['source_files'][name] == r['source_pins'][str(p)] == r['pins'][str(p)], 'source/reference agreement')
    for directory, entries in native['directories'].items():
        d = pathlib.Path(directory)
        need(str(d.resolve()) == str(d) and d.stat().st_uid == 0 and not d.stat().st_mode & 0o022
             and sorted(os.listdir(d)) == entries and len(entries) == len(set(entries)), 'native directory inventory')
        for name in entries:
            path = str(d / name)
            need(path in native['files'] or path in native['directories'] or path in native['aliases'], 'listed closure child')
    for alias, target in native['aliases'].items():
        need(str(pathlib.Path(alias).resolve()) == target and alias != target
             and (target in native['files'] or target in native['directories']), 'native alias')
    for path in native['absent']:
        need(not os.path.lexists(path), 'native absence')
    for path in sys.path:
        need(path in (str(source), str(wrapper)) or path in native['files'] or path in native['directories'] or path in native['absent'], 'startup path closure')
    for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            raw = fields[5]; resolved = str(pathlib.Path(raw).resolve())
            need(not raw.endswith(' (deleted)') and resolved in native['files']
                 and (raw == resolved or native['aliases'].get(raw) == resolved), 'own mapped closure')
    simple_path = file(r['source_native_manifest']); simple = load(simple_path)
    need(sha(simple_path) == r['pins'][str(simple_path)] and set(simple) == {'job_tag', 'files'}
         and simple['job_tag'] == JOB and simple['files']
         and simple['files'].get(str(py)) == r['pins'][str(py)]
         and all(native['files'].get(p) == h for p, h in simple['files'].items()), 'source native subset')
    need(sha(root) == root_hash, 'ROOT policy drift')
    return r, root_hash


def main():
    need(len(sys.argv) == 11 and sys.argv[1::2] == ['--registration', '--policy', '--policy-sha256', '--mode', '--output'], 'literal ROOT probe CLI')
    mode = sys.argv[8]
    need(mode in ('valid', 'dummy'), 'ROOT policy mode only')
    actual = [os.path.realpath(sys.executable), '-E', '-s', '-S', '-B'] + sys.argv
    r, root_hash = root_policy(sys.argv[2], 'probe', mode, actual)
    auth = file(sys.argv[4]); digest = sys.argv[6]
    need(re.fullmatch(r'[0-9a-f]{64}', digest) and sha(auth) == digest
         and str(auth) == str(pathlib.Path(r['authority_dir']) / (mode + '.json')), 'actual ROOT policy bytes')
    output = pathlib.Path(sys.argv[10])
    need(str(output) == str(pathlib.Path(r['writer_dir']) / (mode + '.payload')) and not output.exists(), 'fresh exact sentinel target')
    expected = {'schema': 'f10-necessary-rows-root-policy/v1', 'root_registration_path': str(pathlib.Path(sys.argv[2])),
                'job_tag': JOB, 'label': mode, 'artifact': str(output), 'science_outcome': 'NONE',
                'source_files': r['source_files'], 'limits': LIMITS,
                'closed_scope': r['closed_child_guard']['leaves'][mode],
                'profile': r['profiles']['dummy' if mode == 'dummy' else 'control']}
    need(load(auth) == expected, 'ROOT derivative policy exact fields')
    writer = output.parent; st = writer.stat()
    need(str(writer.resolve()) == str(writer) and writer.parent == pathlib.Path(r['output_mount'])
         and st.st_uid == r['uid'] and st.st_gid == r['gid'] and stat.S_IMODE(st.st_mode) == 0o700, 'writer identity')
    # Barrier complete: still no scientific authorize(), import, field or source assertion.
    import signal
    import time
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    def event(name):
        os.write(fd, (json.dumps({'event': name, 'identity': identity()}, sort_keys=True) + '\n').encode())
        os.fsync(fd)
    if mode == 'valid':
        event('ROOT_POLICY_ONLY_SENTINEL'); os.close(fd); return
    event('parent_started')
    reader, writer_fd = os.pipe(); parent = os.getpid(); child = os.fork()
    if child:
        os.close(writer_fd)
        need(os.read(reader, 1) == b'R', 'dummy handshake')
        event('parent_exit_pending'); os._exit(0)
    os.close(reader); signal.signal(signal.SIGTERM, signal.SIG_IGN)
    event('child_ready_ignoring_term'); os.write(writer_fd, b'R'); os.close(writer_fd)
    while os.getppid() == parent:
        time.sleep(0.005)
    payload = bytearray(64 * 1024 * 1024)
    for page in range(0, len(payload), 4096):
        payload[page] = 1
    event('orphan_allocated_64MiB')
    while True:
        signal.pause()


if __name__ == '__main__':
    main()
