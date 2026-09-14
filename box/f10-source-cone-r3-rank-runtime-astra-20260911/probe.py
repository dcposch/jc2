"""STATIC no-math ROOT-policy sentinel/dummy. Never calls rank authorize."""
import datetime
import hashlib
import json
import os
import pathlib
import re
import socket
import stat
import sys

JOB = 'f10-source-cone-r3-fullrank-v1'
SCIENCE = {
    'authority.py': '75d86856f0da7e8e0779ba9abecad08bce7a5f5e7424b09000bbbd4a45a980a9',
    'wire.py': '492ce280b9069d377051c9b4193847d261b53453123a7e78143d5346c23fb9bf',
    'finder.py': 'e644208e84b5f2800559489af71f9fb05806a45c5abc0ae7c719ca38225401b7',
    'checker.py': '6e780b49ad344879dd48b9e6e4d59724172820e0194cd7e8daf356282dbf695f'}
LIMITS = {'joint_wall_seconds':'600','joint_cpu_seconds':'550','memory_bytes':'8589934592',
          'baseline_bytes':'134217728','certificate_bytes':'16777216','receipt_bytes':'32768'}
ENV = {'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
SOURCE_CHECKER = 'b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f'
SOURCE_OK = 'CHECKED_R3_25_GRAPH_SLOTS_45_LOW_108_JACOBIAN_NO_SOURCE_OUTCOME\n'


def need(ok, reason):
    if not ok:
        raise ValueError('ROOT POLICY REFUSED: ' + reason)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for part in iter(lambda: f.read(1048576), b''):
            h.update(part)
    return h.hexdigest()


def frozen(name):
    p = pathlib.Path(name)
    need(p.is_absolute() and str(p.resolve()) == str(p) and not p.is_symlink(), 'canonical file')
    st = p.stat()
    need(stat.S_ISREG(st.st_mode) and st.st_uid == 0 and stat.S_IMODE(st.st_mode) == 0o444, 'ROOT0444 file')
    for d in p.parents:
        st = d.stat()
        need(stat.S_ISDIR(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022, 'trusted ancestry')
    return p


def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate metadata key')
        out[key] = value
    return out


def metadata(p, cap=65536):
    need(p.stat().st_size <= cap, 'metadata cap')
    return json.loads(p.read_bytes(), object_pairs_hook=pairs)


def policy(root_name, role, root_hash=None):
    root = frozen(root_name)
    digest = sha(root)
    need(root_hash is None or digest == root_hash, 'ROOT byte pin')
    r = metadata(root)
    need(r.get('schema') == 'f10-source-cone-r3-rank-runtime/v1' and r.get('enabled') is True
         and r.get('jobtag') == JOB and r.get('exclusive_no_concurrent_writer') is True, 'ROOT registration')
    need(r['source_limits'] == r['limits'] == LIMITS and r['environment'] == ENV == dict(os.environ), 'fixed limits/environment')
    now = datetime.datetime.now(datetime.timezone.utc)
    stops = [datetime.datetime.fromisoformat(r[k]) for k in ('admission_deadline_utc',
             'mathematical_deadline_utc','task_deadline_utc','worker_deadline_utc')]
    need(all(t.utcoffset() == datetime.timedelta(0) for t in stops)
         and now < stops[0] <= stops[1] < stops[2] < stops[3], 'original admission/stops')
    need(sys.platform == 'linux' and os.getuid() == r['uid'] > 0 and os.getgid() == r['gid'] > 0, 'UID/GID')
    need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2'
         and pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == r['instance_id']
         and socket.gethostname() == r['hostname'], 'EC2 host')
    need(pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == r['boot_id']
         and os.readlink('/proc/self/ns/pid') == r['pid_namespace'], 'boot/namespace')
    need(r['cgroup_path'].startswith('/sys/fs/cgroup/')
         and pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + r['cgroup_path'][len('/sys/fs/cgroup'):]
         and pathlib.Path(r['cgroup_path'], 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'owned cgroup')
    for name in ('dispatcher','probe','mutator'):
        p = frozen(r['files'][name])
        need(p.parent == pathlib.Path(r['wrapper_dir']) and sha(p) == r['pins'][str(p)], 'wrapper pins')
    need(set(os.listdir(r['wrapper_dir'])) == {'dispatch.py','probe.py','mutate.py'}, 'wrapper inventory')
    source = pathlib.Path(r['science_dir'])
    need(set(os.listdir(source)) == set(SCIENCE), 'four source siblings')
    for name, pin in SCIENCE.items():
        p = frozen(str(source / name))
        need(sha(p) == r['pins'][str(p)] == pin, 'source pin')
    native = frozen(r['native_manifest']); simple = frozen(r['source_native_manifest'])
    need(sha(native) == r['pins'][str(native)] and sha(simple) == r['pins'][str(simple)], 'native manifest pins')
    full, small = metadata(native,1048576), metadata(simple)
    need(set(full) == {'schema','files','directories','aliases','absent','python_path'}
         and full['schema'] == 'f10-native-closure/v1' and set(small) == {'job_tag','files'}
         and small['job_tag'] == JOB and small['files'], 'full/subset native separation')
    need(os.path.realpath(sys.executable) == r['files']['python']
         and sha(sys.executable) == r['pins'][r['files']['python']], 'interpreter pin')
    for name, pin in small['files'].items():
        need(full['files'].get(name) == pin and sha(name) == pin, 'subset pin within authenticated full closure')
    bl = r['baseline']; base = frozen(bl['path']); qual = frozen(bl['qualification_path'])
    need(0 < base.stat().st_size <= 134217728 and str(base.stat().st_size) == bl['bytes']
         and sha(base) == r['pins'][str(base)] == bl['sha256']
         and sha(qual) == r['pins'][str(qual)] == bl['qualification_sha256'], 'qualified baseline bytes')
    need(metadata(qual) == {'schema':'r3-baseline-qualified-v1','authority':'ROOT-CAPRUN',
         'status':'ROOT_QUALIFIED_COMPLETE_SOURCE','baseline_sha256':bl['sha256'],'baseline_bytes':bl['bytes'],
         'source_checker_sha256':SOURCE_CHECKER,'checker_exit':'0','checker_stdout':SOURCE_OK}, 'qualification record')
    need(type(r['qualification_evidence']) is dict and 0 < len(r['qualification_evidence']) <= 16, 'genuine prior evidence required')
    for name, pin in r['qualification_evidence'].items():
        need(sha(frozen(name)) == r['pins'][name] == pin, 'prior source evidence pin')
    expected = [sys.executable,'-I','-S','-B',r['files'][role]] + sys.argv[1:]
    live = pathlib.Path('/proc/self/cmdline').read_bytes().rstrip(b'\0').decode().split('\0')
    need(live == expected, 'literal actual wrapper argv')
    return r, digest


def identity():
    text = pathlib.Path('/proc/self/stat').read_text()
    f = text[text.rfind(')')+2:].split()
    return {'pid':os.getpid(),'pgid':os.getpgrp(),'uid':os.getuid(),'gid':os.getgid(),
            'start_ticks':f[19],'boot_id':pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'pid_namespace':os.readlink('/proc/self/ns/pid')}


def main():
    need(len(sys.argv) == 7 and sys.argv[1] == '--registration' and sys.argv[3] == '--mode'
         and sys.argv[5] == '--output' and sys.argv[4] in ('valid','dummy'), 'probe CLI')
    mode = sys.argv[4]
    r, digest = policy(sys.argv[2], 'probe')
    output = pathlib.Path(sys.argv[6])
    need(output == pathlib.Path(r['writer_dir']) / (mode + '.payload'), 'literal probe output')
    import signal
    import time
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    def event(name):
        os.write(fd, (json.dumps({'event':name,'identity':identity(),'root_sha256':digest},sort_keys=True)+'\n').encode())
        os.fsync(fd)
    if mode == 'valid':
        event('ROOT_POLICY_ONLY_NO_RANK_AUTHORIZE')
        os.close(fd)
        return
    event('parent_started')
    reader, writer = os.pipe(); parent = os.getpid(); child = os.fork()
    if child:
        os.close(writer)
        need(os.read(reader,1) == b'R', 'dummy handshake')
        event('parent_exit_pending'); os._exit(0)
    os.close(reader); signal.signal(signal.SIGTERM,signal.SIG_IGN)
    event('child_ready_ignoring_term'); os.write(writer,b'R'); os.close(writer)
    while os.getppid() == parent:
        time.sleep(0.005)
    data = bytearray(64*1024*1024)
    for index in range(0,len(data),4096):
        data[index] = 1
    event('orphan_allocated_64MiB')
    while True:
        signal.pause()


if __name__ == '__main__':
    main()
