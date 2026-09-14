"""DISABLED administrative holder. STATIC/UNTESTED; ROOT finalization required."""
import datetime
import os
import re
import select
import signal
import stat
import sys
import time

ENABLED = False
RELEASE = 'JC2_HOLDER_RELEASE_PLACEHOLDER'
TOKEN = 'JC2_ONE_TIME_TOKEN_PLACEHOLDER'
INSTANCE = 'JC2_INSTANCE_PLACEHOLDER'
BOOT = 'JC2_BOOT_ID_PLACEHOLDER'
PIDNS = 'JC2_PID_NAMESPACE_PLACEHOLDER'
CUTOFF = '2026-09-12T09:02:00+00:00'
ADMISSION = '2026-09-12T09:02:15+00:00'
BASE = '/opt/jc2-closedchild-preflight9-20260912a'
CHANNEL = '/run/jc2-closedchild-preflight9-20260912a-admission'
FIFO = CHANNEL + '/release.fifo'
OUTER_CGROUP = '0::/system.slice/jc2-closedchild-preflight9-20260912a.service'
OUTER = ['/usr/bin/python3.12', '-I', '-S', '-B', BASE + '/wrapper/dispatch.py',
         '--registration', BASE + '/metadata/ROOT-REGISTRATION.json']
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
START = time.monotonic()


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def interrupted(signum, frame):
    raise RuntimeError('holder interrupted')


def text(path):
    with open(path, 'r', encoding='ascii') as f:
        value = f.read(4097)
    need(len(value) <= 4096, 'identity metadata size')
    return value.strip()


def host():
    need(text('/sys/class/dmi/id/sys_vendor') == 'Amazon EC2', 'EC2 required')
    need(text('/sys/class/dmi/id/board_asset_tag') == INSTANCE, 'instance')
    need(text('/proc/sys/kernel/random/boot_id') == BOOT, 'boot')
    need(os.readlink('/proc/self/ns/pid') == PIDNS, 'PID namespace')
    need(text('/proc/self/cgroup') == OUTER_CGROUP, 'outer membership')


def close_extra():
    # No threads, fork or new concurrent descriptor owner exists in this holder.
    names = os.listdir('/proc/self/fd')
    need(len(names) <= 256, 'unexpected inherited descriptor count')
    for name in names:
        fd = int(name)
        if fd > 2:
            try:
                os.close(fd)
            except OSError as exc:
                if exc.errno != 9:  # proc listing's own already-closed descriptor
                    raise


def main():
    need(ENABLED is True and RELEASE == 'ROOT_HOLDER_ADMISSION_ONLY', 'disabled holder')
    need(os.geteuid() == 0 and sys.platform == 'linux', 'ROOT Linux required')
    need(sys.argv == [BASE + '/admin/holder.py'] and sys.flags.isolated == 1
         and sys.flags.no_site == 1 and sys.dont_write_bytecode, 'literal isolated holder')
    need(os.path.realpath(sys.executable) == OUTER[0] and dict(os.environ) == ENV, 'interpreter/environment')
    for value in (RELEASE, TOKEN, INSTANCE, BOOT, PIDNS, CUTOFF, ADMISSION):
        need('PLACEHOLDER' not in value, 'unformed metadata')
    need(re.fullmatch('[0-9a-f]{64}', TOKEN) is not None, 'fixed token grammar')
    stop = datetime.datetime.fromisoformat(CUTOFF)
    admission = datetime.datetime.fromisoformat(ADMISSION)
    need(CUTOFF.endswith('+00:00') and ADMISSION.endswith('+00:00') and stop < admission,
         'fixed holder deadline before admission')

    def remaining():
        left = min(120.0 - (time.monotonic() - START),
                   (stop - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
        need(left > 0, 'holder cutoff; no release')
        return left

    for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGALRM):
        signal.signal(sig, interrupted)
    signal.pthread_sigmask(signal.SIG_SETMASK, [])
    signal.setitimer(signal.ITIMER_REAL, remaining())
    close_extra()
    fd0 = os.open('/dev/null', os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW)
    os.dup2(fd0, 0, inheritable=True)
    os.set_inheritable(0, True)
    if fd0 != 0:
        os.close(fd0)
    need(all(stat.S_ISREG(os.fstat(fd).st_mode) for fd in (1, 2)), 'regular outer streams')
    for output in (1, 2):
        os.set_inheritable(output, True)
    host()
    need(not os.path.lexists(OUTER[-1]), 'final registration must be absent at admission')
    need(os.path.realpath(CHANNEL) == CHANNEL, 'literal channel ancestry')
    directory = os.stat(CHANNEL, follow_symlinks=False)
    need(stat.S_ISDIR(directory.st_mode) and directory.st_uid == 0
         and stat.S_IMODE(directory.st_mode) == 0o700, 'root0700 channel')
    before = os.stat(FIFO, follow_symlinks=False)
    need(stat.S_ISFIFO(before.st_mode) and before.st_uid == 0
         and stat.S_IMODE(before.st_mode) == 0o600, 'root0600 FIFO')
    fd = os.open(FIFO, os.O_RDONLY | os.O_NONBLOCK | os.O_CLOEXEC | os.O_NOFOLLOW)
    try:
        actual = os.fstat(fd)
        need((actual.st_dev, actual.st_ino) == (before.st_dev, before.st_ino), 'FIFO identity')
        expected = ('RELEASE ' + TOKEN + '\n').encode('ascii')
        poller = select.poll()
        poller.register(fd, select.POLLIN | select.POLLHUP | select.POLLERR)
        data = b''
        os.write(1, b'HOLDER_WAITING_FOR_ROOT_RELEASE\n')
        while True:
            remaining()
            events = poller.poll(max(1, min(100, int(remaining() * 1000))))
            need(not any(mask & (select.POLLERR | select.POLLNVAL) for _, mask in events), 'FIFO poll error')
            try:
                chunk = os.read(fd, len(expected) + 1 - len(data))
            except BlockingIOError:
                continue
            if chunk:
                data += chunk
                need(len(data) <= len(expected) and expected.startswith(data), 'invalid/extra release bytes')
            elif data:
                need(data == expected, 'partial release at EOF')
                break
            else:
                # Before the first writer, FIFO EOF is not a release. Bound HUP spin.
                time.sleep(min(0.05, remaining()))
    finally:
        os.close(fd)
    remaining()
    host()
    frozen = os.stat(OUTER[-1], follow_symlinks=False)
    need(stat.S_ISREG(frozen.st_mode) and frozen.st_uid == 0
         and stat.S_IMODE(frozen.st_mode) == 0o444, 'ROOT frozen registration missing')
    need(os.path.realpath(OUTER[-1]) == OUTER[-1], 'literal final registration')
    # ROOT authenticates final SHA, leaves, namespaces and all pins before writing.
    os.chdir(BASE + '/wrapper')
    os.umask(0o022)
    close_extra()
    remaining()
    signal.setitimer(signal.ITIMER_REAL, 0)
    for sig in signal.valid_signals():
        if sig not in (signal.SIGKILL, signal.SIGSTOP):
            signal.signal(sig, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_SETMASK, [])
    # No child: PID/start/cgroup and unit timers/accounting survive this exec.
    remaining()
    os.execve(OUTER[0], OUTER, ENV)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        os.write(2, b'HOLDER_STOP_NO_DISPATCH\n')
        raise SystemExit(2)
