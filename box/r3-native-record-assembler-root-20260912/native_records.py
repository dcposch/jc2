"""STATIC / UNEXECUTED. Pure bounded native-record assembly, never approval.

Reads only the nominated raw/facts files; never probes paths named in records.
No subprocess, native discovery, source import, registration or service action.
"""
import os
import sys

if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize):
    raise SystemExit('ASSEMBLY_STOP: ordinary -I -S -B required')

import datetime
import hashlib
import json
import pathlib
import re
import stat

JOB = 'f10-source-cone-r3-necessary-rows-v1'
PYTHON_PATH = ['/usr/lib/python312.zip', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload']
PACKAGES = {'python3.12', 'python3.12-minimal', 'libpython3.12-stdlib', 'util-linux', 'procps'}
FACT_KEYS = {'schema', 'collector_sha256', 'hostname', 'pid_namespace', 'boot_id', 'packages'}


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pin(s):
    need(type(s) is str and re.fullmatch('[0-9a-f]{64}', s), 'digest shape')
    return s


def decimal(s):
    need(type(s) is str and re.fullmatch('0|[1-9][0-9]{0,19}', s), 'metadata decimal')
    return s


def record_path(s):
    need(type(s) is str and 1 < len(s) <= 4096 and not s.startswith('//')
         and re.fullmatch('/[A-Za-z0-9_./-]+', s), 'record path')
    p = pathlib.PurePosixPath(s)
    need(str(p) == s and '..' not in p.parts, 'noncanonical record path')
    return s


def local_path(s):
    record_path(s)
    p = pathlib.Path(s)
    need(p.parent.resolve(strict=True) == p.parent, 'input/output ancestry symlink')
    return p


def bounded(p, limit):
    p = local_path(str(p))
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'rb') as stream:
        before = os.fstat(stream.fileno())
        need(stat.S_ISREG(before.st_mode) and before.st_size <= limit, 'bounded regular input')
        data = stream.read(limit + 1)
        after = os.fstat(stream.fileno())
        need(len(data) <= limit and len(data) == before.st_size and
             (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) ==
             (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns), 'input changed during read')
        return data


def pairs(items):
    obj = {}
    for k, v in items:
        need(k not in obj, 'duplicate JSON key'); obj[k] = v
    return obj


def forbidden_number(s):
    raise ValueError('numeric facts literal forbidden: metadata fields are strings')


def encode(obj):
    return (json.dumps(obj, ensure_ascii=True, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode('ascii')


def timestamp(line, label):
    match = re.fullmatch(label + r' (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{9}) UTC', line)
    need(match is not None, 'timestamp grammar')
    value = match[1]
    datetime.datetime.fromisoformat(value[:19])
    return value


def owner_mode(values, directory=False):
    uid, gid, mode = values
    need(uid == gid == '0' and re.fullmatch('[0-7]{3,4}', mode), 'ROOT ownership/mode')
    permission = int(mode, 8)
    need(not permission & 0o022 and (not directory or permission & 0o111 == 0o111), 'writable/nontraversable native record')


def parse(raw, facts):
    text = raw.decode('ascii')
    need(text.endswith('\n') and '\r' not in text and '\x00' not in text, 'raw ASCII/LF format')
    lines = text[:-1].split('\n')
    need(16 <= len(lines) <= 20000 and all(0 < len(line) <= 8300 for line in lines), 'raw line bounds')
    start = timestamp(lines[0], 'NATIVE_START'); end = timestamp(lines[-1], 'NATIVE_END')
    need(start <= end, 'reversed collector timestamps')
    need(lines[1:4] == [facts['hostname'], facts['pid_namespace'], facts['boot_id']], 'raw physical header mismatch')
    packages = {}
    for line in lines[4:9]:
        fields = line.split(' ')
        need(len(fields) == 2 and fields[0] in PACKAGES and fields[0] not in packages, 'package header')
        packages[fields[0]] = fields[1]
    need(packages == facts['packages'], 'package/version mismatch')
    need(lines[9:12] == ['PYTHON_PATH ' + p for p in PYTHON_PATH], 'declared Python path order')
    counts = lines[-2].split(' ')
    need(len(counts) == 4 and counts[0] == 'COUNTS', 'single terminal counts')
    for value in counts[1:]:
        decimal(value)
    files, directories, aliases, absent, file_stat, dir_stat = {}, {}, {}, [], {}, {}
    pending = None
    for line in lines[12:-2]:
        fields = line.split(' '); tag = fields[0]
        if pending is not None:
            need(tag == 'FILE' and len(fields) == 6 and fields[5] == pending[0], 'SHA/FILE adjacency or path mismatch')
            decimal(fields[1]); owner_mode(fields[2:5])
            p, h = pending; need(p not in files, 'duplicate file')
            files[p] = h; file_stat[p] = fields[1:5]; pending = None
        elif re.fullmatch('[0-9a-f]{64}  /[A-Za-z0-9_./-]+', line):
            h, p = line.split('  '); pending = (record_path(p), pin(h))
        elif tag == 'DIRECTORY' and len(fields) == 5:
            owner_mode(fields[1:4], True); p = record_path(fields[4])
            need(p not in directories, 'duplicate directory')
            directories[p] = []; dir_stat[p] = fields[1:4]
        elif tag == 'ENTRY' and len(fields) == 3:
            p = record_path(fields[1]); name = fields[2]
            need(p in directories and len(name) <= 255 and re.fullmatch('[A-Za-z0-9_.-]+', name)
                 and name not in ('.', '..'), 'directory entry grammar')
            directories[p].append(name)
        elif tag == 'ALIAS' and len(fields) == 3:
            p, target = map(record_path, fields[1:])
            need(p != target and p not in aliases, 'duplicate/self alias'); aliases[p] = target
        elif tag == 'ABSENT' and len(fields) == 2:
            p = record_path(fields[1]); need(p == PYTHON_PATH[0] and p not in absent, 'only declared absent zip')
            absent.append(p)
        else:
            raise ValueError('unknown or misplaced native record')
        need(len(files) <= 3000 and len(directories) <= 1000 and len(aliases) <= 4000, 'native record count ceiling')
    need(pending is None and 0 < len(files) <= 3000 and 0 < len(directories) <= 1000, 'complete nonempty native records')
    need(counts[1:] == [str(len(files)), str(len(directories)), str(len(aliases))], 'collector counts mismatch')
    groups = [set(files), set(directories), set(aliases), set(absent)]
    for index, group in enumerate(groups):
        need(not any(group & other for other in groups[index + 1:]), 'conflicting native path roles')
    present = set(files) | set(directories) | set(aliases)
    for p, names in directories.items():
        need(names == sorted(set(names)), 'unordered or duplicate direct entries')
        need(all(str(pathlib.PurePosixPath(p) / name) in present for name in names), 'undeclared directory child')
    for p in present:
        named = pathlib.PurePosixPath(p); parent = str(named.parent)
        need(parent not in directories or named.name in directories[parent], 'present direct child missing ENTRY')
    need(all(p in files or p in directories for p in aliases.values()), 'alias target not canonical present path')
    need(all(p in present or p in absent for p in PYTHON_PATH), 'Python path closure')
    required = ['/usr/bin/python3', '/usr/bin/python3.12', '/usr/bin/setpriv', '/bin/ps', '/usr/bin/ps', '/usr/lib/python3.12', '/etc/ld.so.cache']
    need(all(p in present for p in required), 'collector root missing')
    need(all(p in files for p in ('/usr/bin/python3.12', '/usr/bin/setpriv')), 'canonical subset paths missing')
    full = {'schema': 'f10-native-closure/v1', 'files': files, 'directories': directories,
            'aliases': aliases, 'absent': absent, 'python_path': PYTHON_PATH}
    subset = {'job_tag': JOB, 'files': {p: files[p] for p in ('/usr/bin/python3.12', '/usr/bin/setpriv')}}
    stats = {'schema': 'r3-native-record-stats/v1', 'source_facts': facts,
             'start_utc_record': start + ' UTC', 'end_utc_record': end + ' UTC',
             'file_fields': ['size', 'uid', 'gid', 'octal_mode'], 'directory_fields': ['uid', 'gid', 'octal_mode'],
             'files': file_stat, 'directories': dir_stat}
    return full, subset, stats


def write_new(p, data):
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o444)
    with os.fdopen(fd, 'wb') as stream:
        os.fchmod(stream.fileno(), 0o444)
        need(stream.write(data) == len(data), 'short output write')
        stream.flush(); os.fsync(stream.fileno())
    need(bounded(p, len(data)) == data, 'whole output byte readback')


def run():
    need(len(sys.argv) == 11 and sys.argv[1::2] ==
         ['--raw', '--raw-sha256', '--facts', '--facts-sha256', '--out'], 'exact metadata CLI')
    raw_path = local_path(sys.argv[2]); raw_pin = pin(sys.argv[4])
    facts_path = local_path(sys.argv[6]); facts_pin = pin(sys.argv[8]); out = local_path(sys.argv[10])
    need(len({raw_path, facts_path, out}) == 3 and not os.path.lexists(out), 'distinct fresh output path')
    raw = bounded(raw_path, 4194304); facts_bytes = bounded(facts_path, 16384)
    need(sha(raw) == raw_pin and sha(facts_bytes) == facts_pin, 'raw/facts input pin')
    facts = json.loads(facts_bytes, object_pairs_hook=pairs, parse_int=forbidden_number,
                       parse_float=forbidden_number, parse_constant=forbidden_number)
    need(type(facts) is dict and set(facts) == FACT_KEYS and facts['schema'] == 'r3-native-expected-facts/v1'
         and encode(facts) == facts_bytes, 'canonical exact facts schema')
    pin(facts['collector_sha256'])
    need(type(facts['hostname']) is str and re.fullmatch('[A-Za-z0-9][A-Za-z0-9.-]{0,252}', facts['hostname'])
         and type(facts['pid_namespace']) is str and re.fullmatch(r'pid:\[[1-9][0-9]*\]', facts['pid_namespace'])
         and type(facts['boot_id']) is str and re.fullmatch('[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}', facts['boot_id']), 'expected physical grammar')
    need(type(facts['packages']) is dict and set(facts['packages']) == PACKAGES
         and all(type(v) is str and 0 < len(v) <= 200 and re.fullmatch('[A-Za-z0-9.+:~_-]+', v)
                 for v in facts['packages'].values()), 'five expected package versions')
    full, subset, stats = parse(raw, facts)
    outputs = {'native-manifest.json': encode(full), 'source-native-manifest.json': encode(subset),
               'native-stat-records.json': encode(stats),
               'native.sha256': ''.join(h + '  ' + p + '\n' for p, h in sorted(full['files'].items())).encode('ascii')}
    limits = {'native-manifest.json': 1048576, 'source-native-manifest.json': 65536,
              'native-stat-records.json': 2097152, 'native.sha256': 1048576}
    need(all(len(data) <= limits[name] for name, data in outputs.items()), 'serialized metadata ceiling')
    receipt = {'schema': 'r3-native-assembly-receipt/v1', 'status': 'ASSEMBLED_METADATA_ONLY_UNQUALIFIED',
               'science_outcome': 'NONE', 'raw_path': str(raw_path), 'raw_sha256': raw_pin,
               'facts_path': str(facts_path), 'facts_sha256': facts_pin,
               'collector_sha256_external_assertion': facts['collector_sha256'],
               'outputs': {name: {'sha256': sha(data), 'bytes': str(len(data))} for name, data in outputs.items()},
               'boundary': 'No collector execution, host freshness, native completeness, ROOT approval or launch authority is certified.'}
    outputs['assembly-receipt.json'] = encode(receipt)
    need(len(outputs['assembly-receipt.json']) <= 32768 and sum(map(len, outputs.values())) <= 4194304, 'whole assembly ceiling')
    need(bounded(raw_path, 4194304) == raw and bounded(facts_path, 16384) == facts_bytes, 'input drift before publication')
    os.mkdir(out, 0o700)
    for name, data in outputs.items():
        write_new(out / name, data)
    fd = os.open(out, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    fd = os.open(out.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    need(set(os.listdir(out)) == set(outputs), 'exact output inventory')
    need(bounded(raw_path, 4194304) == raw and bounded(facts_path, 16384) == facts_bytes, 'input drift after publication')
    print(json.dumps({'status': 'ASSEMBLED_METADATA_ONLY_UNQUALIFIED', 'science_outcome': 'NONE',
                      'receipt_sha256': sha(outputs['assembly-receipt.json'])}, sort_keys=True), flush=True)


if __name__ == '__main__':
    try:
        run()
    except Exception as error:
        print(json.dumps({'status': 'ASSEMBLY_STOP_NO_QUALIFICATION', 'science_outcome': 'NONE',
                          'reason': str(error)[:400]}, sort_keys=True), flush=True)
        raise SystemExit(2)
