"""STATIC / UNEXECUTED. One ROOT-approved AWS administrative service, no retry.

No campaign imports. No science, native collection, installation of sources,
leaf creation, authority creation, worker control, timer cancellation or cleanup.
"""
import os
import sys

if sys.platform != 'linux' or os.geteuid() != 0:
    raise SystemExit('BIND_REFUSED: ROOT Linux only')
if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize):
    raise SystemExit('BIND_REFUSED: ordinary -I -S -B required')

import datetime
import hashlib
import json
import pathlib
import re
import stat
import subprocess
import time

P = '/opt/jc2-r3-bootstrap-20260912'
META = P + '/metadata'
OWN = P + '/administration/bind_once.py'
SEED = META + '/binding-seed.json'
SPEC = META + '/bootstrap-spec.json'
CARD = META + '/launch-card.json'
EVIDENCE = '/var/lib/jc2-r3-bootstrap-20260912/preparation/binding'
UNIT = 'r3bootstrap20260912.service'
SLICE = 'r3bootstrap20260912.slice'
ADMIN = 'r3bootstrap20260912bind.service'
TIMER = 'r3bootstrap20260912watch.timer'
WATCH = 'r3bootstrap20260912watch.service'
SCOPE = '/sys/fs/cgroup/' + SLICE
OUTER = SCOPE + '/' + UNIT
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
BOOT = 'f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2'
LAUNCH = 'c3b42e78f01e469594c9d17f105bdffb42fcff2e79e33a131f72be9bff91b7e7'
LABELS = ['refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source', 'refuse-hash', 'valid', 'startup-produce', 'startup-check', 'dummy']
KEYS = set('schema approval source_sha256 source_first_sha256 qualification_files loaded_unit_mapping_qualification_sha256 spec card offsets epoch_not_before_utc epoch_not_after_utc worker_deadline_utc'.split())
SPEC_KEYS = set('schema approval bootstrap_sha256 bootstrap_first_sha256 launcher_qualification_sha256 native_qualification_sha256 registration_path binding_path binding_deadline_utc binding_wall_seconds cgroup_namespace mount_namespace outer_started_utc outer_resources external_supervisor exclusive_root_contract registration'.split())
CARD_KEYS = set('schema approval launcher_sha256 launcher_first_sha256 launcher_qualification_sha256 native_qualification_sha256 accounting_qualification_sha256 retirement_qualification_sha256 python env systemctl tool_pins bootstrap spec spec_sha256 unit slice watchdog_timer watchdog_service epoch_utc epoch_timestamp_raw epoch_timer_monotonic_usec task_scope task_scope_device task_scope_inode cpu_quota_percent'.split())


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def pin(s):
    need(type(s) is str and re.fullmatch('[0-9a-f]{64}', s), 'pin shape')
    return s


def path(s):
    need(type(s) is str and re.fullmatch('/[A-Za-z0-9_./-]+', s), 'literal absolute path')
    p = pathlib.Path(s)
    need(str(p) == s and str(p.resolve()) == s and not p.is_symlink(), 'canonical nonsymlink path')
    return p


def rooted(p):
    for q in (p,) + tuple(p.parents):
        st = q.lstat()
        need(st.st_uid == 0 and not st.st_mode & 0o022, 'ROOT exclusive ancestry')
        need(not {'system.posix_acl_access', 'system.posix_acl_default'}.intersection(os.listxattr(q, follow_symlinks=False)), 'ACL-free ancestry')


def raw(p, ceiling=262144, immutable=True):
    p = path(str(p)); rooted(p); st = p.stat()
    need(stat.S_ISREG(st.st_mode) and (not immutable or stat.S_IMODE(st.st_mode) == 0o444), 'regular file/mode')
    with open(p, 'rb') as f:
        data = f.read(ceiling + 1)
    need(len(data) <= ceiling, 'bounded file')
    return data


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(p):
    p = path(p); rooted(p); need(p.is_file(), 'regular pinned input')
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def pairs(xs):
    d = {}
    for k, v in xs:
        need(k not in d, 'duplicate key'); d[k] = v
    return d


def no_number(s):
    raise ValueError('float/nonfinite metadata forbidden')


def encode(x):
    return (json.dumps(x, ensure_ascii=True, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()


def load(p, h, ceiling=262144):
    b = raw(p, ceiling); need(sha(b) == pin(h), 'input SHA')
    x = json.loads(b, object_pairs_hook=pairs, parse_float=no_number, parse_constant=no_number)
    need(encode(x) == b, 'canonical JSON'); return x


def small(p):
    with open(p, encoding='ascii') as f:
        b = f.read(65537)
    need(len(b) <= 65536, 'kernel text cap'); return b.strip()


def utc(s):
    need(type(s) is str and s.endswith('+00:00'), 'explicit UTC')
    return datetime.datetime.fromisoformat(s)


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def exclusive(p, b, ceiling=262144):
    p = path(p); rooted(p.parent); need(len(b) <= ceiling, 'output cap')
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o444)
    with os.fdopen(fd, 'wb') as f:
        f.write(b); f.flush(); os.fchmod(f.fileno(), 0o444); os.fsync(f.fileno())
    fd = os.open(p.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    need(raw(p, ceiling) == b, 'whole-byte readback'); return sha(b)


def record(name, obj):
    return exclusive(EVIDENCE + '/' + name + '.json', encode(obj), 65536)


def command(tool, args, timeout=2):
    # Every child remains in this administrative cgroup and is waited/reaped.
    p = subprocess.run([tool, '--system'] + args, env=ENV, stdin=subprocess.DEVNULL,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True,
                       timeout=timeout, check=False)
    need(p.returncode == 0 and not p.stderr and len(p.stdout) <= 65536, 'systemctl failure/cap')
    return p.stdout.decode('ascii')


def show(tool, unit, fields):
    d = {}
    for line in command(tool, ['show', unit, '--no-pager', '--property=' + ','.join(fields)]).splitlines():
        k, v = line.split('=', 1); need(k not in d, 'duplicate property'); d[k] = v
    need(set(d) == set(fields), 'exact property set'); return d


def outer_unit(c, card_sha, s):
    # Literal duplication of accepted launcher.outer_unit; __file__ replaced
    # ONLY with its fixed installed launcher path. No campaign import/eval.
    r = s['registration']; q = c['cpu_quota_percent']
    argv = [c['env'], '-i'] + [k + '=' + v for k, v in ENV.items()] + [c['python'], '-I', '-S', '-B', P + '/launcher/launcher.py', '--card', CARD, '--card-sha256', card_sha]
    return ('[Unit]\nDescription=ROOT preflight bootstrap only\n'
            '[Service]\nType=exec\nUser=root\nGroup=root\nSlice=' + c['slice'] + '\n'
            'WorkingDirectory=' + r['wrapper_dir'] + '\nExecStart=' + ' '.join(argv) + '\n'
            'StandardInput=null\nStandardOutput=append:' + r['output_mount'] + '/outer.stdout\n'
            'StandardError=append:' + r['output_mount'] + '/outer.stderr\n'
            'Restart=no\nRemainAfterExit=no\nDelegate=no\nKillMode=control-group\nSendSIGKILL=yes\n'
            'RuntimeMaxSec=2875s\nTimeoutStartSec=5s\nTimeoutStopSec=5s\n'
            'MemoryAccounting=yes\nCPUAccounting=yes\nTasksAccounting=yes\n'
            'MemoryMax=8589934592\nMemorySwapMax=0\nTasksMax=32\n'
            'CPUQuota=' + q + '%\nCPUQuotaPeriodSec=10ms\nCPUSchedulingPolicy=other\n'
            'UMask=0022\nLimitCORE=0\nLimitNOFILE=1048576\nLimitFSIZE=134217728\n').encode()


def watch_bytes(tool):
    return (('[Unit]\nDescription=Original monotonic task bound\n[Timer]\n'
             'OnActiveSec=115s\nAccuracySec=1us\nRandomizedDelaySec=0\n'
             'Persistent=no\nRemainAfterElapse=yes\nUnit=' + WATCH + '\n').encode(),
            ('[Unit]\nDescription=Stop exact original outer unit\n[Service]\n'
             'Type=oneshot\nUser=root\nGroup=root\nExecStart=' + tool +
             ' --system stop ' + UNIT + ' ' + SLICE + '\nTimeoutStartSec=10s\nKillMode=control-group\nRestart=no\n').encode())


def no_children():
    need(os.listdir('/proc/self/task') == [str(os.getpid())]
         and small('/proc/self/task/' + str(os.getpid()) + '/children') == '', 'administrative children/threads must be reaped')


def run(seed_sha):
    need(dict(os.environ) == ENV and sys.orig_argv == [sys.executable, '-I', '-S', '-B', OWN, '--seed-sha256', seed_sha]
         and os.readlink('/proc/self/exe') == sys.executable, 'exact administration argv/environment')
    a = load(SEED, seed_sha)
    need(type(a) is dict and set(a) == KEYS and a['schema'] == 'r3-bootstrap-bind-once/v1'
         and a['approval'] == 'ROOT_APPROVED_BIND_PREFLIGHT_ONLY_9', 'externally approved pre-epoch seed')
    need(sha(raw(OWN)) == pin(a['source_sha256']), 'binding source pin')
    s, c = a['spec'], a['card']; r = s['registration']
    need(set(s) == SPEC_KEYS and set(c) == CARD_KEYS, 'exact inherited spec/card keys')
    need(s['schema'] == 'r3-exec-bootstrap/v1' and s['approval'] == 'ROOT_APPROVED_PREFLIGHT_ONLY_9'
         and s['bootstrap_sha256'] == BOOT and c['schema'] == 'r3-bootstrap-launch/v1'
         and c['approval'] == 'ROOT_APPROVED_PREFLIGHT_LAUNCH' and c['launcher_sha256'] == LAUNCH,
         'unchanged inherited source and external clearances')
    need(c['python'] == sys.executable and c['bootstrap'] == P + '/bootstrap/bootstrap.py'
         and c['spec'] == SPEC and c['unit'] == UNIT and c['slice'] == SLICE
         and c['watchdog_timer'] == TIMER and c['watchdog_service'] == WATCH
         and c['task_scope'] == SCOPE and c['cpu_quota_percent'] == '69', 'fixed selected layout/quota')
    for key in ('spec_sha256', 'epoch_utc', 'epoch_timestamp_raw', 'epoch_timer_monotonic_usec', 'task_scope_device', 'task_scope_inode'):
        need(c[key] is None, 'only null late card slots')
    need(s['outer_started_utc'] is None and s['binding_deadline_utc'] is None and s['binding_wall_seconds'] == 120,
         'only null epoch slots, unchanged binding ceiling')
    e = s['external_supervisor']
    need(e['unit'] == UNIT and e['already_armed'] is None and e['outer_deadline_utc'] is None
         and e['retirement_deadline_utc'] == a['worker_deadline_utc']
         and e['no_restart'] is True and e['covers_bootstrap_exec_descendants'] is True, 'prequalified external policy with unobserved activation')
    need(r['enabled'] is False and r['execution_mode'] == 'PREFLIGHT_ONLY_9'
         and r['allowed_phases'] == LABELS and r['commands'] == {} and r['typed_slot_policy'] == {}
         and r['phase_policy'] is None and r['aggregate_cpu_start_usec'] == '0', 'unchanged disabled nine-only registration')
    need(r['science_dir'] == P + '/science' and r['wrapper_dir'] == P + '/wrapper'
         and r['cgroup_path'] == OUTER and r['output_mount'] == '/run/jc2-r3-bootstrap-20260912'
         and s['registration_path'] == META + '/ROOT-REGISTRATION.json'
         and s['binding_path'] == r['output_mount'] + '/bootstrap-binding.json', 'fixed output/source locations')
    need(r['worker_deadline_utc'] == a['worker_deadline_utc'], 'independent absolute worker cutoff retained')
    for k in ('admission', 'mathematical', 'task'):
        need(r[k + '_deadline_utc'] is None, 'null late original deadlines')
    offsets = a['offsets']
    need(set(offsets) == {'binding', 'admission', 'mathematical', 'task', 'outer'}
         and all(type(v) is int and 0 < v <= 3000 for v in offsets.values())
         and offsets['binding'] <= 120 and offsets['binding'] <= offsets['admission'] <= offsets['mathematical'] < offsets['task']
         and offsets['outer'] == 120 and offsets['outer'] <= offsets['task'], 'fixed ROOT offset policy, unchanged 115+5 stop')
    need(utc(a['epoch_not_before_utc']) <= now() <= utc(a['epoch_not_after_utc']) < utc(a['worker_deadline_utc']), 'preapproved epoch window')
    qs = a['qualification_files']
    need(type(qs) is dict and 1 <= len(qs) <= 16, 'finite prior qualification vector')
    refs = [a['source_first_sha256'], a['loaded_unit_mapping_qualification_sha256'], e['qualification_sha256']]
    refs += [c[k] for k in ('launcher_first_sha256', 'launcher_qualification_sha256', 'native_qualification_sha256', 'accounting_qualification_sha256', 'retirement_qualification_sha256')]
    refs += [s['bootstrap_first_sha256']]
    need(all(pin(h) in qs.values() for h in refs)
         and s['launcher_qualification_sha256'] == c['launcher_qualification_sha256']
         and s['native_qualification_sha256'] == c['native_qualification_sha256'], 'actual prior evidence references, no synthetic substitution')
    for p, h in qs.items():
        need(sha(raw(p)) == pin(h), 'prior ROOT record bytes')
    tool = c['systemctl']
    need(set(c['tool_pins']) == {c['python'], c['env'], tool}
         and r['pins'].get(OWN) == a['source_sha256'], 'administrative/tool source vector')
    for p, h in c['tool_pins'].items():
        need(file_sha(p) == pin(h) and r['pins'].get(p) == h, 'actual canonical tool pin')
    need(sha(raw(c['bootstrap'])) == BOOT and sha(raw(P + '/launcher/launcher.py')) == LAUNCH, 'unchanged installed entry sources')
    need(small('/sys/class/dmi/id/sys_vendor') == 'Amazon EC2'
         and small('/sys/class/dmi/id/board_asset_tag') == r['instance_id']
         and os.uname().nodename == r['hostname'] and small('/proc/sys/kernel/random/boot_id') == r['boot_id'], 'actual qualified physical host')
    for short, expected in (('pid', r['pid_namespace']), ('mnt', s['mount_namespace']), ('cgroup', s['cgroup_namespace'])):
        need(os.readlink('/proc/self/ns/' + short) == os.readlink('/proc/1/ns/' + short) == expected, 'actual ROOT namespace')
    scope = path(SCOPE); rooted(scope); st = scope.stat()
    need(small('/proc/self/cgroup') == '0::/' + SLICE + '/' + ADMIN
         and {p.name for p in scope.iterdir() if p.is_dir()} == {ADMIN}, 'administration already sole sibling before epoch')
    need(small(scope / ADMIN / 'cgroup.procs') == str(os.getpid()), 'one administrative process before arming')
    resources = {'memory.max': '8589934592', 'memory.swap.max': '0', 'pids.max': '32', 'cpu.max': '6900 10000', 'cpu.max.burst': '0'}
    need(s['outer_resources'] == resources, 'unchanged selected outer expected resources')
    for k, v in resources.items():
        need(small(scope / k) == v, 'actual whole-task ancestor resource')
    c['task_scope_device'], c['task_scope_inode'] = st.st_dev, st.st_ino
    fields = ('LoadState', 'ActiveState', 'SubState', 'FragmentPath', 'DropInPaths')
    admin = show(tool, ADMIN, fields + ('MainPID', 'ControlGroup', 'KillMode', 'TimeoutStopUSec', 'Restart'))
    need(admin['LoadState'] == 'loaded' and admin['ActiveState'] == 'active' and admin['SubState'] == 'running'
         and admin['MainPID'] == str(os.getpid()) and admin['ControlGroup'] == '/' + SLICE + '/' + ADMIN
         and admin['FragmentPath'] == '/etc/systemd/system/' + ADMIN
         and admin['DropInPaths'] == '' and admin['KillMode'] == 'control-group'
         and admin['TimeoutStopUSec'] == '5s' and admin['Restart'] == 'no', 'actual administrative service/stop contract')
    directory = path(EVIDENCE); rooted(directory)
    need(stat.S_IMODE(directory.stat().st_mode) == 0o700 and set(os.listdir(directory)) == {'admin.stdout', 'admin.stderr'}, 'private fresh administrative evidence directory')
    for fd, name in ((1, 'admin.stdout'), (2, 'admin.stderr')):
        t = (directory / name).stat(); opened = os.fstat(fd)
        need(stat.S_ISREG(t.st_mode) and (t.st_dev, t.st_ino) == (opened.st_dev, opened.st_ino), 'original administrative streams')
    targets = [SPEC, CARD, '/etc/systemd/system/' + UNIT, s['registration_path'], s['binding_path'], OUTER]
    need(all(not os.path.lexists(p) for p in targets), 'every late target absent')
    native = load(r['native_manifest'], r['pins'][r['native_manifest']], 1048576)
    need(set(native) == {'schema', 'files', 'directories', 'aliases', 'absent', 'python_path'}, 'six-field native manifest')
    changed_parents = {META, '/etc/systemd/system', EVIDENCE}
    generated = targets[:5] + [SEED, '/etc/systemd/system/' + ADMIN]
    need(not changed_parents.intersection(native['directories'])
         and all(p not in native['files'] and p not in r['pins'] and p not in r['source_pins'] for p in generated)
         and not set(targets[:5]).intersection(native['absent']), 'no generated hash cycle or native inventory mutation')
    for p in (c['python'], c['env'], tool):
        need(native['files'].get(p) == c['tool_pins'][p], 'canonical tool FILE entries')
    for p, h in r['pins'].items():
        need(file_sha(p) == pin(h), 'installed registration input binding')
    for p, names in native['directories'].items():
        need(sorted(os.listdir(path(p))) == names, 'current native directory inventory')
    tbytes, wbytes = watch_bytes(tool)
    need(raw('/etc/systemd/system/' + TIMER) == tbytes and raw('/etc/systemd/system/' + WATCH) == wbytes, 'preinstalled unchanged watchdog unit bytes')
    timer_fields = fields + ('ActiveEnterTimestamp', 'ActiveEnterTimestampMonotonic')
    before = show(tool, TIMER, timer_fields)
    need(before['LoadState'] == 'loaded' and before['ActiveState'] == 'inactive' and before['SubState'] == 'dead'
         and before['ActiveEnterTimestampMonotonic'] == '0' and before['DropInPaths'] == ''
         and before['FragmentPath'] == '/etc/systemd/system/' + TIMER, 'fresh never-activated preinstalled timer')
    guard = show(tool, WATCH, fields + ('Slice', 'ExecMainPID', 'InvocationID'))
    need(guard['LoadState'] == 'loaded' and guard['ActiveState'] == 'inactive' and guard['SubState'] == 'dead'
         and guard['FragmentPath'] == '/etc/systemd/system/' + WATCH and guard['DropInPaths'] == ''
         and guard['Slice'] != SLICE and guard['ExecMainPID'] == '0' and guard['InvocationID'] == '', 'fresh watchdog outside stopped slice')
    no_children()
    need(sha(raw(SEED)) == seed_sha, 'pre-arm immutable seed')
    record('attempt', {'status': 'ONE_SHOT_CONSUMED_NO_RETRY', 'seed_sha256': seed_sha, 'utc': now().isoformat(), 'admin': admin, 'timer_before': before, 'watch_before': guard})
    # The sole activation. Any later exception retains evidence; never rearm.
    command(tool, ['start', TIMER], 5)
    observed = show(tool, TIMER, timer_fields)
    need(observed['LoadState'] == 'loaded' and observed['ActiveState'] == 'active' and observed['SubState'] == 'waiting'
         and observed['DropInPaths'] == '' and observed['FragmentPath'] == '/etc/systemd/system/' + TIMER, 'observed first watchdog activation')
    epoch = datetime.datetime.strptime(observed['ActiveEnterTimestamp'], '%a %Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc)
    need(observed['ActiveEnterTimestamp'] == epoch.strftime('%a %Y-%m-%d %H:%M:%S UTC')
         and re.fullmatch('[1-9][0-9]*', observed['ActiveEnterTimestampMonotonic']), 'literal paired epoch')
    mono = int(observed['ActiveEnterTimestampMonotonic'])
    need(utc(a['epoch_not_before_utc']) <= epoch <= utc(a['epoch_not_after_utc']), 'actual activation in approved epoch window')
    def clock():
        elapsed = time.clock_gettime_ns(time.CLOCK_MONOTONIC) // 1000 - mono
        wall = (now() - epoch).total_seconds()
        need(0 <= elapsed < 100000000 and 0 <= wall < min(100, offsets['binding'])
             and abs(wall - elapsed / 1000000) <= 2, 'original paired admission clocks')
        need(now() < utc(a['worker_deadline_utc']), 'unchanged independent retirement deadline')
    clock()
    record('epoch', {'status': 'WATCHDOG_OBSERVED_NOT_OUTER_STARTED', 'timer': observed, 'utc': now().isoformat(), 'scope_device': st.st_dev, 'scope_inode': st.st_ino})
    s['outer_started_utc'] = epoch.isoformat()
    s['binding_deadline_utc'] = (epoch + datetime.timedelta(seconds=offsets['binding'])).isoformat()
    for key in ('admission', 'mathematical', 'task'):
        r[key + '_deadline_utc'] = (epoch + datetime.timedelta(seconds=offsets[key])).isoformat()
    need(utc(r['task_deadline_utc']) < utc(a['worker_deadline_utc']), 'original task before absolute worker stop')
    e['already_armed'] = True
    e['outer_deadline_utc'] = (epoch + datetime.timedelta(seconds=offsets['outer'])).isoformat()
    c.update(epoch_utc=epoch.isoformat(), epoch_timestamp_raw=observed['ActiveEnterTimestamp'], epoch_timer_monotonic_usec=str(mono))
    clock(); spec_sha = exclusive(SPEC, encode(s))
    c['spec_sha256'] = spec_sha
    clock(); card_sha = exclusive(CARD, encode(c))
    unit_path = '/etc/systemd/system/' + UNIT
    unit_bytes = outer_unit(c, card_sha, s)
    clock(); unit_sha = exclusive(unit_path, unit_bytes, 16384)
    clock(); command(tool, ['daemon-reload'], 5)
    loaded = show(tool, UNIT, fields + ('NeedDaemonReload', 'MainPID', 'ExecMainPID', 'InvocationID', 'Type', 'Slice', 'User', 'Group', 'Restart', 'KillMode', 'TimeoutStopUSec', 'RuntimeMaxUSec', 'MemoryMax', 'MemorySwapMax', 'TasksMax', 'ExecStart'))
    expected = dict(LoadState='loaded', ActiveState='inactive', SubState='dead', FragmentPath=unit_path, DropInPaths='', NeedDaemonReload='no', MainPID='0', ExecMainPID='0', InvocationID='', Type='exec', Slice=SLICE, User='root', Group='root', Restart='no', KillMode='control-group', TimeoutStopUSec='5s', RuntimeMaxUSec='47min 55s', MemoryMax='8589934592', MemorySwapMax='0', TasksMax='32')
    need(all(loaded[k] == v for k, v in expected.items()) and loaded['ExecStart'], 'fresh loaded unit properties')
    # ExecStart serialization/effective byte mapping is explicitly a PRIOR
    # ROOT host qualification, not a substring or invented parser check.
    need(show(tool, TIMER, timer_fields) == observed, 'same never-rearmed timer')
    need(show(tool, WATCH, fields + ('Slice', 'ExecMainPID', 'InvocationID')) == guard, 'watchdog has not fired')
    for p, h in r['pins'].items():
        clock(); need(file_sha(p) == h, 'last static input pin')
    need(sha(raw(SEED)) == seed_sha and raw(SPEC) == encode(s) and raw(CARD) == encode(c) and raw(unit_path) == unit_bytes, 'last installed byte commitment')
    need(not os.path.lexists(OUTER) and not os.path.lexists(s['registration_path']) and not os.path.lexists(s['binding_path']), 'no preexisting outer/authority')
    clock()
    record('commitment', {'status': 'INSTALLED_READBACK_NOT_PREFLIGHT_RESULT', 'seed_sha256': seed_sha, 'spec_sha256': spec_sha, 'card_sha256': card_sha, 'outer_unit_sha256': unit_sha, 'loaded': loaded, 'timer': observed, 'mapping_qualification_sha256': a['loaded_unit_mapping_qualification_sha256'], 'utc': now().isoformat()})
    no_children(); clock()
    command(tool, ['start', UNIT], 5)  # Sole outer start; no wait for nine phases.
    live = show(tool, UNIT, ('LoadState', 'ActiveState', 'SubState', 'MainPID', 'ExecMainPID', 'InvocationID', 'ExecMainStartTimestamp', 'ExecMainStartTimestampMonotonic', 'ControlGroup', 'Result'))
    no_children()
    record('start-returned', {'status': 'ONE_START_RETURNED_NO_PREFLIGHT_VERDICT', 'actual_outer': live, 'utc': now().isoformat(), 'science_outcome': 'NONE'})
    return 0


def main():
    try:
        need(len(sys.argv) == 3 and sys.argv[1] == '--seed-sha256', 'literal binding CLI')
        return run(pin(sys.argv[2]))
    except Exception as e:
        obj = {'status': 'BIND_STOP_NO_RETRY', 'science_outcome': 'NONE', 'error_type': type(e).__name__, 'reason': str(e)[:400]}
        print(json.dumps(obj, sort_keys=True), flush=True)
        try:
            os.fsync(1)
        except OSError:
            pass
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
