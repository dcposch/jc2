"""Fixed no-math authorization/startup/descendant probe. UNEXECUTED."""
import argparse
import json
import os
import pathlib
import signal
import sys
import time
import authority

def identity():
    raw = pathlib.Path('/proc/self/stat').read_text()
    fields = raw[raw.rfind(')')+2:].split()
    boot = pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    return {'pid': os.getpid(), 'pgid': os.getpgrp(), 'uid': os.getuid(), 'gid': os.getgid(),
            'start_identity': 'boot='+boot+';start_ticks='+fields[19],
            'pid_namespace': os.readlink('/proc/self/ns/pid')}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mode', choices=('authorize', 'dummy'), required=True)
    p.add_argument('--job', required=True)
    p.add_argument('--registration', required=True)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    permit = authority.authorize('probe', a.job, a.registration, [a.output])
    authority.postcheck(permit)
    if a.mode == 'authorize':
        authority.emit(a.output, {'status': 'POST_AUTHORIZE', 'identity': identity()}, 4096)
        return 0
    fd = os.open(a.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    def event(name):
        os.write(fd, (json.dumps({'event': name, 'identity': identity()}, sort_keys=True)+'\n').encode())
        os.fsync(fd)
    event('parent_started')
    reader, writer = os.pipe()
    parent = os.getpid()
    child = os.fork()
    if child:
        os.close(writer)
        if os.read(reader, 1) != b'R':
            raise RuntimeError('dummy handshake failed')
        event('parent_exit_pending')
        os._exit(0)
    os.close(reader)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    event('child_ready_ignoring_term')
    os.write(writer, b'R')
    os.close(writer)
    while os.getppid() == parent:
        time.sleep(0.005)
    payload = bytearray(64*1024*1024)
    for page in range(0, len(payload), 4096):
        payload[page] = 1
    event('orphan_allocated_64MiB')
    while True:
        signal.pause()

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, RuntimeError, OSError, TypeError, KeyError) as exc:
        print('REFUSAL: '+str(exc), file=sys.stderr)
        raise SystemExit(2)
