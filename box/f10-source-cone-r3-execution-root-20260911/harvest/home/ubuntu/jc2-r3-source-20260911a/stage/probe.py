"""No-math r3 authorization / descendant control; STATIC, NOT EXECUTED."""
import os
import sys


def identity():
    import pathlib
    raw = pathlib.Path('/proc/self/stat').read_text()
    f = raw[raw.rfind(')') + 2:].split()
    return {'pid': os.getpid(), 'pgid': os.getpgrp(), 'uid': os.getuid(), 'gid': os.getgid(),
            'start_ticks': f[19],
            'boot_id': pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'pid_namespace': os.readlink('/proc/self/ns/pid')}


def main():
    # ROOT already pins this separate three-file wrapper directory and the exact
    # five-file science directory. Only the actual nonmathematical authority
    # module is loaded; neither arithmetic module nor either entry is imported.
    if len(sys.argv) != 14 or sys.argv[1] != '--science-dir' or sys.argv[3] != '--mode' or sys.argv[5] != '--':
        raise SystemExit('REFUSED: probe arguments')
    base, mode, tail = sys.argv[2], sys.argv[4], sys.argv[6:]
    if mode not in ('authorize', 'dummy') or not os.path.isabs(base):
        raise SystemExit('REFUSED: probe mode/directory')
    if set(os.listdir(base)) != {'authority.py', 'arithmetic.py', 'produce.py', 'check_arithmetic.py', 'check.py'}:
        raise SystemExit('REFUSED: probe science inventory')
    sys.path.insert(0, base)
    from authority import authorize
    sys.argv = [sys.argv[0]] + tail
    try:
        output = authorize('produce')
    except ValueError as exc:
        # Literal actual authority exception; no science is imported.
        sys.stderr.write('ValueError: ' + str(exc) + '\n')
        raise SystemExit(1)
    import json
    import signal
    import time
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    def event(name):
        os.write(fd, (json.dumps({'event': name, 'identity': identity()}, sort_keys=True) + '\n').encode())
        os.fsync(fd)
    if mode == 'authorize':
        event('POST_AUTHORIZE')
        os.close(fd)
        return
    event('parent_started')
    reader, writer = os.pipe()
    parent = os.getpid()
    child = os.fork()
    if child:
        os.close(writer)
        if os.read(reader, 1) != b'R':
            raise RuntimeError('dummy handshake')
        event('parent_exit_pending')
        os._exit(0)
    os.close(reader)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    event('child_ready_ignoring_term')
    os.write(writer, b'R')
    os.close(writer)
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
