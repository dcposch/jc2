"""Independent direct-row T mutator. Embedded metadata barriers only; no peer science imports."""
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
            'pid_namespace': os.readlink('/proc/self/ns/pid')}


def root_policy(root_name, role, label, actual):
    # ROOT0444/no-concurrent-writer trust; command contains no recursive ROOT hash.
    root = file(root_name); r = load(root); root_hash = sha(root)
    need(r.get('schema') == 'f10-necessary-rows-runtime/v1' and r.get('enabled') is True
         and r.get('jobtag') == JOB and r.get('exclusive_no_concurrent_writer') is True, 'enabled ROOT policy')
    need(r['review_clearance']['status'] == 'SOURCE_AND_RUNTIME_FIRST_CONFIRMED', 'ROOT FIRST clearance')
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
    need(str(cg).startswith('/sys/fs/cgroup/') and str(cg.resolve()) == str(cg)
         and pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + str(cg)[len('/sys/fs/cgroup'):]
         and (cg / 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'owned cgroup')
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


def startup():
    need(len(sys.argv) == 7 and sys.argv[1::2] == ['--registration', '--root-registration-sha256', '--positive-record'], 'literal mutator CLI')
    actual = [os.path.realpath(sys.executable), '-I', '-S', '-B'] + sys.argv
    r, root_hash = root_policy(sys.argv[2], 'mutator', 'mutate', actual)
    need(sys.argv[4] == root_hash, 'registered ROOT hash')
    source = pathlib.Path(r['science_dir']); frozen = pathlib.Path(r['frozen_dir'])
    policy = {'baseline': str(frozen / 'artifact.json'), 'fixture': str(frozen / 'mixed-row.json'),
              'mutation': 'graph.slots[24] += X1^27 over ROOT place', 'source_files': r['source_files'],
              'source_limits': LIMITS, 'positive_record': str(pathlib.Path(r['authority_dir']) / 'positive.json')}
    phase_path = file(sys.argv[6]); phase = load(phase_path)
    need(r['phase_policy'] == policy and str(phase_path) == policy['positive_record'], 'ROOT phase policy')
    need(set(phase) == {'schema', 'status', 'root_registration_sha256', 'input', 'source_files', 'authorization', 'checker_stdout_sha256', 'policy'}
         and phase['schema'] == 'f10-necessary-rows-positive-phase/v1'
         and phase['status'] == 'POSITIVE_CHECKED_NO_SOURCE_OUTCOME'
         and phase['root_registration_sha256'] == root_hash and phase['policy'] == policy
         and phase['source_files'] == r['source_files']
         and phase['checker_stdout_sha256'] == hashlib.sha256(b'CHECKED_NECESSARY_ROWS_25_NO_SOURCE_OUTCOME\n').hexdigest(), 'ROOT-derived genuine positive checker record')
    baseline = file(policy['baseline'])
    need(phase['input'] == {'path': str(baseline), 'sha256': sha(baseline), 'bytes': baseline.stat().st_size}
         and 0 < baseline.stat().st_size < 125829120, 'positive input byte binding')
    auth = file(phase['authorization']['path'])
    need(str(auth) == str(pathlib.Path(r['authority_dir']) / 'check-positive.json')
         and sha(auth) == phase['authorization']['sha256'], 'positive authority pin')
    expected = {'job_tag': JOB, 'status': 'REGISTERED', 'authority': 'ROOT-CAPRUN', 'mode': 'check',
                'artifact': {'path': str(baseline), 'sha256': phase['input']['sha256']},
                'files': r['source_files'], 'runtime': {'python_sha256': r['pins'][r['files']['python']],
                'native_inventory_path': r['source_native_manifest'],
                'native_inventory_sha256': sha(file(r['source_native_manifest']))}, 'limits': LIMITS,
                'contract_sha256': r['contract_sha256'], 'source_pins': r['source_pins'], 'place': r['place']}
    need(load(auth) == expected, 'exact eleven-key positive source authority, without calling it')
    writer = pathlib.Path(r['writer_dir']); st = writer.stat()
    need(str(writer.resolve()) == str(writer) and writer.parent == pathlib.Path(r['output_mount'])
         and st.st_uid == r['uid'] and st.st_gid == r['gid'] and stat.S_IMODE(st.st_mode) == 0o700, 'writer ownership')
    return r, root_hash, baseline, writer


def main():
    r, root_hash, baseline, writer = startup()
    # Only now parse mathematical JSON or perform the one finite-coordinate edit.
    def no_number(value):
        raise ValueError('MUTATOR REFUSED: JSON number in scientific wire')
    def wire(obj):
        return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode('ascii')
    raw = baseline.read_bytes()
    need(0 < len(raw) == baseline.stat().st_size < 125829120, 'bounded baseline read')
    doc = json.loads(raw, object_pairs_hook=pairs, parse_int=no_number, parse_float=no_number, parse_constant=no_number)
    need(wire(doc) == raw and set(doc) == {'schema', 'job_tag', 'contract_sha256', 'source_pins', 'place', 'graph'}
         and doc['schema'] == 'f10-r3-necessary-rows/v1' and doc['job_tag'] == JOB
         and doc['contract_sha256'] == r['contract_sha256'] and doc['source_pins'] == r['source_pins']
         and doc['place'] == r['place'], 'canonical six-key ROOT-bound direct wire')
    def decimal(value, bound):
        need(type(value) is str and len(value) <= 10 and re.fullmatch(r'0|[1-9][0-9]*', value), 'canonical bounded decimal')
        number = int(value); need(number <= bound, 'coordinate range'); return number
    place = r['place']; p = decimal(place['p'], 2147483647); f = decimal(place['degree'], 7)
    need(p >= 2 and 1 <= f <= 7 and len(place['phi']) == f + 1 and len(place['P7_mod_p']) == 8
         and place['phi'][-1] == place['P7_mod_p'][-1] == '1', 'authenticated place dimensions')
    for value in place['phi'] + place['P7_mod_p']:
        decimal(value, p - 1)
    graph = doc['graph']
    need(type(graph) is dict and set(graph) == {'Hq', 'c', 'c_inverse', 'zeta', 'slots', 'ell', 'g', 'U'}
         and type(graph['slots']) is list and len(graph['slots']) == 25, 'graph thirty-polynomial/two-scalar inventory')
    def coordinates(row):
        need(type(row) is list and len(row) == f, 'dense field length')
        return [decimal(value, p - 1) for value in row]
    coordinates(graph['c']); coordinates(graph['c_inverse'])
    inventory = list(zip(graph['slots'], [8, 9, 10] + list(range(19, 10, -1)) + list(range(22, 10, -1)) + [27]))
    inventory += [(graph[name], weight) for name, weight in (('Hq', 7), ('zeta', 7), ('ell', 23), ('g', 30), ('U', 4))]
    total = 0
    for poly, weight in inventory:
        need(type(poly) is dict and set(poly) == {'kind', 'terms'} and poly['kind'] == 'graph'
             and type(poly['terms']) is list and len(poly['terms']) <= 20000, 'typed graph polynomial')
        total += len(poly['terms']); need(total <= 400000, 'whole polynomial term cap')
        previous = None
        for term in poly['terms']:
            need(type(term) is list and len(term) == 2 and type(term[0]) is list and len(term[0]) == 4, 'term dimensions')
            ex = tuple(decimal(value, 256) for value in term[0])
            need(sum((i + 1) * x for i, x in enumerate(ex)) == weight
                 and (previous is None or previous < ex) and any(coordinates(term[1])), 'canonical nonzero homogeneous sorted term')
            previous = ex
    selected_poly = graph['slots'][24]
    original = json.loads(json.dumps(selected_poly))
    row = selected_poly['terms']; selected = None
    for index, term in enumerate(row):
        if term[0] == ['27', '0', '0', '0']:
            selected = index
    if selected is None:
        need(len(row) < 20000 and total < 400000, 'one spare whole-wire term required')
        row.append([['27', '0', '0', '0'], ['1'] + ['0'] * (f - 1)])
        row.sort(key=lambda term: tuple(int(value) for value in term[0]))
    else:
        values = coordinates(row[selected][1]); values[0] = (values[0] + 1) % p
        if any(values):
            row[selected][1] = [str(value) for value in values]
        else:
            del row[selected]
    changed = wire(doc)
    need(changed != raw and len(changed) + len(raw) <= 125829120, 'changed bytes/joint120MiB')
    graph['slots'][24] = original
    need(wire(doc) == raw, 'inverse change restores WHOLE input bytes')
    output, receipt = writer / 'mixed-row.json', writer / 'mutation.json'
    need(not output.exists() and not receipt.exists(), 'fresh one-fixture destinations')
    with open(output, 'xb') as stream:
        stream.write(changed); stream.flush(); os.fsync(stream.fileno())
    need(sha(output) == hashlib.sha256(changed).hexdigest()
         and sha(baseline) == hashlib.sha256(raw).hexdigest(), 'actual fixture/baseline readback')
    record = {'schema': 'f10-necessary-rows-T-mutation/v1', 'status': 'FORMED_UNCHECKED',
              'root_registration_sha256': root_hash, 'input_sha256': hashlib.sha256(raw).hexdigest(),
              'output_sha256': sha(output), 'output_bytes': len(changed),
              'mutation': 'graph.slots[24] += X1^27 over ROOT place',
              'inverse_restored_whole_bytes': True, 'checker_run': False}
    with open(receipt, 'xb') as stream:
        stream.write(wire(record)); stream.flush(); os.fsync(stream.fileno())
    fd = os.open(writer, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


if __name__ == '__main__':
    main()
