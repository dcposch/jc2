"""UNEXECUTED service-entry launcher. No install/start/holder/retry interface.

ROOT supplies ordinary units and a separately approved immutable card.
This process replaces itself with the unchanged repaired bootstrap.
"""
import os
import sys

if sys.platform != 'linux' or os.geteuid() != 0:
    raise SystemExit('LAUNCH_REFUSED: ROOT Linux only')
if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize):
    raise SystemExit('LAUNCH_REFUSED: ordinary -I -S -B required')

import datetime
import hashlib
import json
import pathlib
import re
import resource
import stat
import subprocess
import time

ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
BOOTSTRAP_SHA = 'f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2'
KEYS = set('schema approval launcher_sha256 launcher_first_sha256 launcher_qualification_sha256 native_qualification_sha256 accounting_qualification_sha256 retirement_qualification_sha256 python env systemctl tool_pins bootstrap spec spec_sha256 unit slice watchdog_timer watchdog_service epoch_utc epoch_timestamp_raw epoch_timer_monotonic_usec task_scope task_scope_device task_scope_inode cpu_quota_percent'.split())


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def pin(s):
    need(type(s) is str and re.fullmatch('[0-9a-f]{64}', s), 'SHA256 shape')
    return s


def path(s):
    need(type(s) is str and re.fullmatch('/[A-Za-z0-9_./-]+', s), 'literal absolute path')
    p = pathlib.Path(s)
    need(str(p) == s and str(p.resolve()) == s and not p.is_symlink(), 'canonical nonsymlink path')
    return p


def rooted(p):
    for q in (p,) + tuple(p.parents):
        t = q.lstat()
        need(t.st_uid == 0 and not t.st_mode & 0o022, 'ROOT no writable ancestry')
        need(not {'system.posix_acl_access', 'system.posix_acl_default'}.intersection(os.listxattr(q, follow_symlinks=False)), 'no migration/write ACL')


def raw(p, limit=262144, immutable=True):
    p = path(str(p)); rooted(p); t = p.stat()
    need(stat.S_ISREG(t.st_mode) and (not immutable or stat.S_IMODE(t.st_mode) == 0o444), 'literal regular file mode')
    with open(p, 'rb') as f:
        data = f.read(limit + 1)
    need(len(data) <= limit, 'bounded input')
    return data


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(p):
    p = path(str(p)); rooted(p); need(p.is_file(), 'pinned regular executable')
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def pairs(xs):
    out = {}
    for k, v in xs:
        need(k not in out, 'duplicate JSON key'); out[k] = v
    return out


def numeric_refusal(s):
    raise ValueError('float/nonfinite JSON forbidden')


def encode(x):
    return (json.dumps(x, ensure_ascii=True, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()


def load(p, h):
    data = raw(p); need(digest(data) == pin(h), 'approved input SHA mismatch')
    obj = json.loads(data, object_pairs_hook=pairs, parse_float=numeric_refusal, parse_constant=numeric_refusal)
    need(encode(obj) == data, 'canonical JSON required')
    return obj


def utc(s):
    need(type(s) is str and s.endswith('+00:00'), 'explicit UTC')
    return datetime.datetime.fromisoformat(s)


def kernel(p):
    with open(p, encoding='ascii') as f:
        s = f.read(65537)
    need(len(s) <= 65536, 'kernel text cap')
    return s.strip()


def show(tool, unit, names):
    # Only exact read-only properties of the three registered units.
    result = subprocess.run([tool, '--system', 'show', unit, '--no-pager',
                             '--property=' + ','.join(names)], env=ENV,
                            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, close_fds=True, timeout=2, check=False)
    need(result.returncode == 0 and not result.stderr and len(result.stdout) <= 16384, 'bounded systemd property read')
    out = {}
    for line in result.stdout.decode('ascii').splitlines():
        k, v = line.split('=', 1); need(k not in out, 'duplicate systemd property'); out[k] = v
    need(set(out) == set(names), 'exact systemd property set')
    return out


def outer_unit(c, card, card_sha, spec):
    r = spec['registration']; q = c['cpu_quota_percent']
    command = [c['env'], '-i'] + [k + '=' + v for k, v in ENV.items()] + [c['python'], '-I', '-S', '-B',
               str(path(__file__)), '--card', str(card), '--card-sha256', card_sha]
    return ('[Unit]\nDescription=ROOT preflight bootstrap only\n'
            '[Service]\nType=exec\nUser=root\nGroup=root\nSlice=' + c['slice'] + '\n'
            'WorkingDirectory=' + r['wrapper_dir'] + '\nExecStart=' + ' '.join(command) + '\n'
            'StandardInput=null\nStandardOutput=append:' + r['output_mount'] + '/outer.stdout\n'
            'StandardError=append:' + r['output_mount'] + '/outer.stderr\n'
            'Restart=no\nRemainAfterExit=no\nDelegate=no\nKillMode=control-group\nSendSIGKILL=yes\n'
            'RuntimeMaxSec=2875s\nTimeoutStartSec=5s\nTimeoutStopSec=5s\n'
            'MemoryAccounting=yes\nCPUAccounting=yes\nTasksAccounting=yes\n'
            'MemoryMax=8589934592\nMemorySwapMax=0\nTasksMax=32\n'
            'CPUQuota=' + q + '%\nCPUQuotaPeriodSec=10ms\nCPUSchedulingPolicy=other\n'
            'UMask=0022\nLimitCORE=0\nLimitNOFILE=1048576\nLimitFSIZE=134217728\n').encode()


def watchdog_units(c):
    timer = ('[Unit]\nDescription=Original monotonic task bound\n[Timer]\n'
             'OnActiveSec=115s\nAccuracySec=1us\nRandomizedDelaySec=0\n'
             'Persistent=no\nRemainAfterElapse=yes\nUnit=' + c['watchdog_service'] + '\n').encode()
    service = ('[Unit]\nDescription=Stop exact original outer unit\n[Service]\n'
               'Type=oneshot\nUser=root\nGroup=root\nExecStart=' + c['systemctl'] +
               ' --system stop ' + c['unit'] + ' ' + c['slice'] + '\nTimeoutStartSec=10s\nKillMode=control-group\nRestart=no\n').encode()
    return timer, service


def run(card, card_sha):
    c = load(card, card_sha)
    need(type(c) is dict and set(c) == KEYS and c['schema'] == 'r3-bootstrap-launch/v1'
         and c['approval'] == 'ROOT_APPROVED_PREFLIGHT_LAUNCH', 'external approved launch card')
    need(dict(os.environ) == ENV, 'systemd environment must be cleared by env -i')
    own = path(__file__)
    for key in ('launcher_sha256', 'launcher_first_sha256', 'launcher_qualification_sha256', 'native_qualification_sha256',
                'accounting_qualification_sha256', 'retirement_qualification_sha256'):
        pin(c[key])
    need(digest(raw(own)) == c['launcher_sha256'], 'approved launcher pin')
    expected = [c['python'], '-I', '-S', '-B', str(own), '--card', str(card), '--card-sha256', card_sha]
    need(sys.orig_argv == expected and os.readlink('/proc/self/exe') == c['python'], 'same pinned Python argv/exe')
    need(set(c['tool_pins']) == {c['python'], c['env'], c['systemctl']}, 'three exact launcher tools')
    for p, h in c['tool_pins'].items():
        need(file_sha(p) == pin(h), 'current launcher tool pin')
    need(digest(raw(c['bootstrap'])) == BOOTSTRAP_SHA, 'unchanged repaired bootstrap')
    s = load(c['spec'], c['spec_sha256']); r = s['registration']
    need(s['bootstrap_sha256'] == BOOTSTRAP_SHA and s['launcher_qualification_sha256'] == c['launcher_qualification_sha256']
         and s['native_qualification_sha256'] == c['native_qualification_sha256']
         and r['files']['python'] == c['python'] and r['enabled'] is False
         and r['execution_mode'] == 'PREFLIGHT_ONLY_9', 'spec/source/qualification binding')
    need(r['pins'].get(str(own)) == c['launcher_sha256']
         and all(r['pins'].get(p) == h for p, h in c['tool_pins'].items()), 'launcher/tool vector retained by bootstrap')
    need(kernel('/sys/class/dmi/id/sys_vendor') == 'Amazon EC2'
         and kernel('/sys/class/dmi/id/board_asset_tag') == r['instance_id']
         and os.uname().nodename == r['hostname']
         and kernel('/proc/sys/kernel/random/boot_id') == r['boot_id']
         and os.readlink('/proc/self/ns/pid') == r['pid_namespace']
         and os.readlink('/proc/self/ns/cgroup') == s['cgroup_namespace']
         and os.readlink('/proc/self/ns/mnt') == s['mount_namespace'], 'same qualified EC2 host/boot/namespaces')
    null = os.stat('/dev/null'); incoming = os.fstat(0)
    need(stat.S_ISCHR(null.st_mode) and os.major(null.st_rdev) == 1 and os.minor(null.st_rdev) == 3
         and (incoming.st_dev, incoming.st_ino, incoming.st_rdev) == (null.st_dev, null.st_ino, null.st_rdev)
         and os.readlink('/proc/self/fd/0') == '/dev/null', 'trusted actual null stdin')
    for fd, name in ((1, 'outer.stdout'), (2, 'outer.stderr')):
        stream = path(r['output_mount']) / name; rooted(stream); st = stream.stat(); opened = os.fstat(fd)
        need(stat.S_ISREG(st.st_mode) and (opened.st_dev, opened.st_ino) == (st.st_dev, st.st_ino)
             and os.readlink('/proc/self/fd/' + str(fd)) == str(stream), 'original exact outer streams')
    for key, suffix in (('unit', '.service'), ('slice', '.slice'), ('watchdog_timer', '.timer'), ('watchdog_service', '.service')):
        need(re.fullmatch('r3bootstrap[a-z0-9]+[.]' + suffix[1:], c[key]), 'fixed simple ROOT unit name')
    need(len({c[k] for k in ('unit', 'slice', 'watchdog_timer', 'watchdog_service')}) == 4, 'distinct registered units')
    need(type(c['cpu_quota_percent']) is str and re.fullmatch('[1-9][0-9]?', c['cpu_quota_percent'])
         and 1 <= int(c['cpu_quota_percent']) <= 69, 'conservative qualified quota')
    need(s['outer_resources']['cpu.max'] == str(100 * int(c['cpu_quota_percent'])) + ' 10000', 'same observed quota/period')
    need(s['outer_started_utc'] == c['epoch_utc'] and s['external_supervisor']['unit'] == c['unit'], 'original task epoch, not service start')
    epoch = utc(c['epoch_utc'])
    need(epoch.microsecond == 0 and c['epoch_timestamp_raw'] == epoch.strftime('%a %Y-%m-%d %H:%M:%S UTC'), 'literal systemd epoch rendering')
    need(re.fullmatch('[1-9][0-9]*', c['epoch_timer_monotonic_usec']), 'observed monotonic epoch')
    mono = int(c['epoch_timer_monotonic_usec'])
    unit_path = '/etc/systemd/system/' + c['unit']
    timer_path = '/etc/systemd/system/' + c['watchdog_timer']; guard_path = '/etc/systemd/system/' + c['watchdog_service']
    need(raw(unit_path) == outer_unit(c, card, card_sha, s), 'exact outer unit bytes')
    timer_bytes, guard_bytes = watchdog_units(c)
    need(raw(timer_path) == timer_bytes and raw(guard_path) == guard_bytes, 'exact independent watchdog units')
    timer_names = ('LoadState', 'ActiveState', 'SubState', 'FragmentPath', 'DropInPaths', 'ActiveEnterTimestamp', 'ActiveEnterTimestampMonotonic')
    timer = show(c['systemctl'], c['watchdog_timer'], timer_names)
    need(timer == dict(LoadState='loaded', ActiveState='active', SubState='waiting', FragmentPath=timer_path, DropInPaths='',
                       ActiveEnterTimestamp=c['epoch_timestamp_raw'], ActiveEnterTimestampMonotonic=c['epoch_timer_monotonic_usec']), 'original timer still armed, never restarted')
    guard = show(c['systemctl'], c['watchdog_service'], ('LoadState', 'ActiveState', 'SubState', 'FragmentPath', 'DropInPaths'))
    need(guard == dict(LoadState='loaded', ActiveState='inactive', SubState='dead', FragmentPath=guard_path, DropInPaths=''), 'guard not already fired')
    live = show(c['systemctl'], c['unit'], ('LoadState', 'ActiveState', 'SubState', 'ActiveEnterTimestampMonotonic',
                                             'FragmentPath', 'DropInPaths', 'MainPID', 'ExecMainPID',
                                             'InvocationID', 'ExecMainStartTimestampMonotonic', 'ExecMainStartTimestamp', 'ControlGroup'))
    need(live['LoadState'] == 'loaded' and live['FragmentPath'] == unit_path and live['DropInPaths'] == ''
         and live['ActiveState'] == 'active' and live['SubState'] == 'running'
         and live['MainPID'] == live['ExecMainPID'] == str(os.getpid()) and re.fullmatch('[0-9a-f]{32}', live['InvocationID']), 'actual same service process/invocation')
    need(live['ExecMainStartTimestampMonotonic'].isdigit() and int(live['ExecMainStartTimestampMonotonic']) >= mono,
         'later actual process start, distinct from original epoch')
    need('/sys/fs/cgroup' + live['ControlGroup'] == r['cgroup_path']
         and kernel('/proc/self/cgroup') == '0::' + live['ControlGroup'], 'actual outer membership')
    scope = path(c['task_scope']); rooted(scope); st = scope.stat()
    need(type(c['task_scope_device']) is int and type(c['task_scope_inode']) is int
         and (st.st_dev, st.st_ino) == (c['task_scope_device'], c['task_scope_inode'])
         and scope.name == c['slice'] and path(r['cgroup_path']).parent == scope, 'earlier exclusive accounting ancestor')
    for name, value in s['outer_resources'].items():
        need(kernel(scope / name) == value, 'whole-task ancestor cap')
    cpu = dict(line.split() for line in kernel(scope / 'cpu.stat').splitlines())
    need(cpu.get('usage_usec', '').isdigit() and int(cpu['usage_usec']) < 2050000000, 'whole-task accounting origin zero')
    now_mono = time.clock_gettime_ns(time.CLOCK_MONOTONIC) // 1000
    now = datetime.datetime.now(datetime.timezone.utc)
    need(live['ActiveEnterTimestampMonotonic'].isdigit()
         and mono <= int(live['ActiveEnterTimestampMonotonic']) <= now_mono, 'already active monotonic service clock')
    need(0 <= now_mono - mono < 100000000 and 0 <= (now - epoch).total_seconds() < 100,
         'original entry admission: 100s, never a renewed epoch')
    need(abs((now - epoch).total_seconds() - (now_mono - mono) / 1000000) <= 2, 'paired clock drift at entry')
    need(now < utc(s['binding_deadline_utc']) <= epoch + datetime.timedelta(seconds=120)
         and utc(r['task_deadline_utc']) <= epoch + datetime.timedelta(seconds=3000), 'original absolute bounds')
    need(kernel('/proc/self/task/' + str(os.getpid()) + '/children') == '', 'all property-reader children reaped')
    need(os.listdir('/proc/self/task') == [str(os.getpid())], 'one entry thread')
    need(digest(raw(card)) == card_sha and digest(raw(c['spec'])) == c['spec_sha256']
         and digest(raw(c['bootstrap'])) == BOOTSTRAP_SHA, 'final exact pin recheck')
    record = {'status': 'LAUNCH_ENTRY_CHECKED_NOT_BOOTSTRAP_RESULT', 'science_outcome': 'NONE', 'card_sha256': card_sha,
              'spec_sha256': c['spec_sha256'], 'epoch_utc': c['epoch_utc'], 'epoch_timer_monotonic_usec': str(mono),
              'entry_utc': now.isoformat(), 'entry_monotonic_usec': str(now_mono), 'actual_service': live,
              'whole_task_cpu_usec': cpu['usage_usec']}
    data = encode(record); need(len(data) <= 16384, 'entry record cap')
    need(os.write(1, data) == len(data), 'complete entry record write'); os.fsync(1)
    os.chdir(r['wrapper_dir']); os.umask(0o022)
    ceiling = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
    need(type(ceiling) is int and 3 <= ceiling <= 1048576, 'finite inherited descriptor ceiling')
    os.closerange(3, ceiling)
    need(time.clock_gettime_ns(time.CLOCK_MONOTONIC) // 1000 - mono < 100000000
         and datetime.datetime.now(datetime.timezone.utc) < utc(s['binding_deadline_utc']), 'final original entry deadline')
    os.execve(c['python'], [c['python'], '-I', '-S', '-B', c['bootstrap'], '--spec', c['spec'], '--spec-sha256', c['spec_sha256']], ENV)
    raise RuntimeError('exec unexpectedly returned')


def main():
    try:
        need(len(sys.argv) == 5 and sys.argv[1] == '--card' and sys.argv[3] == '--card-sha256', 'literal entry CLI')
        run(path(sys.argv[2]), pin(sys.argv[4]))
    except Exception as e:
        print(json.dumps({'status': 'LAUNCH_STOP', 'science_outcome': 'NONE', 'error_type': type(e).__name__, 'reason': str(e)[:400]}, sort_keys=True), flush=True)
        try:
            os.fsync(1)
        except OSError:
            pass
        return 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
