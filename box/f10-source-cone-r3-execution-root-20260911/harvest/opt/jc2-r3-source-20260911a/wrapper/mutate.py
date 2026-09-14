"""STATIC/UNEXECUTED. One ROOT-authorized X1^27 edit; no checker or solver.

Arithmetic imports and scientific JSON parsing occur only after the current
ROOT, host, source, immutable positive-phase and actual authority barriers.
"""
import datetime
import hashlib
import json
import os
import pathlib
import re
import socket
import stat
import sys

JOB = 'f10-source-cone-r3-reconstruction-v1'
SCIENCE = {
    'authority.py': '407c5784ba07abbf289e2ba4fd82f24fc661987eb55f378bf39cc954da1ee07b',
    'arithmetic.py': '40b18453b6127d1b8217a6d6e1d3eb3aff1e911c15243ed9c640277f24175431',
    'produce.py': '76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a',
    'check_arithmetic.py': '10e57542f9aa06eb69fd9562b2aa0bb27567c6d14186ffa90d77d6e08e80ae2c',
    'check.py': 'b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f'}
LIMITS = {'wall_seconds': '900', 'cpu_seconds': '600', 'memory_bytes': '8589934592',
          'aggregate_bytes': '134217728'}
PACKET = 125829120


def need(ok, label):
    if not ok:
        raise ValueError('MUTATOR REFUSED: ' + label)


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def immutable(name):
    p = pathlib.Path(name)
    need(p.is_absolute() and str(p.resolve()) == str(p) and not p.is_symlink(), 'canonical immutable path')
    st = p.stat()
    need(stat.S_ISREG(st.st_mode) and st.st_uid == 0 and stat.S_IMODE(st.st_mode) == 0o444, 'ROOT0444 file')
    for d in p.parents:
        st = d.stat()
        need(stat.S_ISDIR(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022, 'ROOT path ancestry')
    return p


def metadata(path):
    need(path.stat().st_size <= 65536, 'metadata cap')
    return json.loads(path.read_bytes(), object_pairs_hook=pairs)


def startup():
    need(len(sys.argv) == 7 and sys.argv[1] == '--registration'
         and sys.argv[3] == '--root-registration-sha256' and sys.argv[5] == '--positive-record', 'literal CLI')
    root = immutable(sys.argv[2]); root_hash = sys.argv[4]
    need(re.fullmatch(r'[0-9a-f]{64}', root_hash) and sha(root) == root_hash, 'ROOT byte pin')
    r = metadata(root)
    need(r.get('schema') == 'f10-source-cone-r3-runtime/v1' and r.get('enabled') is True
         and r.get('jobtag') == JOB and r.get('exclusive_no_concurrent_writer') is True, 'enabled exact ROOT policy')
    utc = datetime.datetime.now(datetime.timezone.utc)
    stops = [datetime.datetime.fromisoformat(r[k]) for k in ('admission_deadline_utc',
             'mathematical_deadline_utc', 'task_deadline_utc', 'worker_deadline_utc')]
    need(all(t.utcoffset() == datetime.timedelta(0) for t in stops)
         and utc < stops[0] <= stops[1] < stops[2] < stops[3], 'original UTC admission/stops')
    need(r['source_limits'] == LIMITS and r['environment'] == dict(os.environ)
         and dict(os.environ) == {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}, 'caps/environment')
    need(sys.platform == 'linux' and os.getuid() == r['uid'] and os.getgid() == r['gid']
         and r['uid'] > 0 and r['gid'] > 0, 'science identity')
    need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2'
         and pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == r['instance_id']
         and socket.gethostname() == r['hostname'], 'registered EC2 host')
    need(pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip() == r['boot_id']
         and os.readlink('/proc/self/ns/pid') == r['pid_namespace'], 'boot/namespace')
    need(pathlib.Path('/proc/self/cgroup').read_text().strip() == '0::' + r['cgroup_path'][len('/sys/fs/cgroup'):]
         and pathlib.Path(r['cgroup_path'], 'memory.max').read_text().strip() == LIMITS['memory_bytes'], 'owned memory cgroup')
    me = immutable(str(pathlib.Path(__file__).resolve()))
    need(str(me) == r['files']['mutator'] and sha(me) == r['pins'][str(me)], 'mutator source pin')
    source = pathlib.Path(r['science_dir'])
    need(set(os.listdir(source)) == set(SCIENCE), 'exact five source files')
    for name, digest in SCIENCE.items():
        p = immutable(str(source / name))
        need(r['pins'][str(p)] == digest and sha(p) == digest, 'current source bytes')
    phase_path = immutable(sys.argv[6])
    policy = {'baseline': str(pathlib.Path(r['frozen_dir']) / 'artifact.json'),
              'fixture': str(pathlib.Path(r['frozen_dir']) / 'mixed-row.json'),
              'mutation': 'graph.slots[24] += X1^27', 'source_files': SCIENCE,
              'source_limits': LIMITS, 'positive_record': str(pathlib.Path(r['authority_dir']) / 'positive.json')}
    need(r['phase_policy'] == policy and str(phase_path) == policy['positive_record'], 'exact ROOT phase path/policy')
    phase = metadata(phase_path)
    need(set(phase) == {'schema', 'status', 'root_registration_sha256', 'input', 'source_files',
         'authorization', 'checker_stdout_sha256', 'policy'} and phase['schema'] == 'f10-r3-positive-phase/v1'
         and phase['status'] == 'POSITIVE_CHECKED_NO_SOURCE_OUTCOME'
         and phase['root_registration_sha256'] == root_hash and phase['policy'] == policy
         and phase['source_files'] == SCIENCE, 'ROOT-authored terminal positive phase')
    baseline = immutable(policy['baseline'])
    need(phase['input'] == {'path': str(baseline), 'sha256': sha(baseline), 'bytes': baseline.stat().st_size}
         and 0 < baseline.stat().st_size < PACKET, 'frozen positive baseline pin/size')
    auth = immutable(phase['authorization']['path'])
    need(str(auth) == str(pathlib.Path(r['authority_dir']) / 'check-positive.json')
         and sha(auth) == phase['authorization']['sha256'], 'positive authorization binding')
    need(str(source.resolve()) == str(source) and source.is_absolute(), 'source import root')
    sys.path.insert(0, str(source))
    from authority import authorize
    sys.argv = [str(me), '--registered-job', JOB, '--authorization', str(auth),
                '--authorization-sha256', phase['authorization']['sha256'], '--input', str(baseline)]
    need(authorize('check') == str(baseline), 'actual source authorization/input pin')
    writer = pathlib.Path(r['writer_dir'])
    need(writer.is_absolute() and str(writer.resolve()) == str(writer)
         and writer.parent == pathlib.Path(r['output_mount']), 'registered writer path')
    st = writer.stat()
    need(st.st_uid == r['uid'] and st.st_gid == r['gid'] and stat.S_IMODE(st.st_mode) == 0o700, 'writer ownership')
    return r, root_hash, baseline, writer


def main():
    r, root_hash, baseline, writer = startup()
    # No scientific import or scientific JSON parse above this boundary.
    from fractions import Fraction
    sys.set_int_max_str_digits(4300)
    raw = baseline.read_bytes()
    need(len(raw) == baseline.stat().st_size and len(raw) < PACKET, 'bounded input read')

    def no_number(value):
        raise ValueError('MUTATOR REFUSED: JSON number in scientific wire')

    def wire(obj):
        return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode('ascii')

    doc = json.loads(raw, object_pairs_hook=pairs, parse_int=no_number,
                     parse_float=no_number, parse_constant=no_number)
    need(wire(doc) == raw and doc['format'] == 'r3-source-cone-reconstruction-v1'
         and doc['job_tag'] == JOB, 'positive canonical wire/header')
    slots = doc['graph']['slots']
    need(type(slots) is list and len(slots) == 25 and type(slots[24]) is list, 'exact selected graph slot')
    original = json.loads(json.dumps(slots[24]))
    row = slots[24]
    need(len(row) <= 20000, 'selected polynomial term cap')
    previous = None
    selected = None
    for index, term in enumerate(row):
        need(type(term) is list and len(term) == 2 and type(term[0]) is list and len(term[0]) == 4
             and type(term[1]) is list and len(term[1]) == 7, 'four exponents/seven rationals')
        need(all(type(x) is str and re.fullmatch(r'0|[1-9][0-9]*', x) and len(x) <= 2 for x in term[0]), 'exponent strings')
        ex = tuple(int(x) for x in term[0])
        need(all(x <= b for x, b in zip(ex, (30, 15, 10, 7)))
             and (previous is None or previous < ex), 'ordered bounded exponents')
        previous = ex
        values = []
        for value in term[1]:
            need(type(value) is str and re.fullmatch(r'(?:0|-?[1-9][0-9]{0,4095})/[1-9][0-9]{0,4095}', value), 'bounded rational string')
            q = Fraction(value)
            need(str(q.numerator) + '/' + str(q.denominator) == value, 'reduced rational')
            values.append(q)
        need(any(values), 'nonzero sparse term')
        if ex == (27, 0, 0, 0):
            selected = index
    if selected is None:
        need(len(row) < 20000, 'one spare sparse term required')
        row.append([['27', '0', '0', '0'], ['1/1'] + ['0/1'] * 6])
        row.sort(key=lambda term: tuple(int(x) for x in term[0]))
    else:
        values = [Fraction(x) for x in row[selected][1]]
        values[0] += 1
        if any(values):
            encoded = [str(q.numerator) + '/' + str(q.denominator) for q in values]
            need(all(re.fullmatch(r'(?:0|-?[1-9][0-9]{0,4095})/[1-9][0-9]{0,4095}', x) for x in encoded), 'changed coefficient bounds')
            row[selected][1] = encoded
        else:
            del row[selected]
    changed = wire(doc)
    need(changed != raw and len(changed) + len(raw) <= PACKET, 'changed object/joint120MiB budget')
    slots[24] = original
    need(wire(doc) == raw, 'inverse edit restores WHOLE original bytes')
    output, receipt = writer / 'mixed-row.json', writer / 'mutation.json'
    need(not output.exists() and not receipt.exists(), 'fresh mutation destinations')
    with open(output, 'xb') as f:
        f.write(changed); f.flush(); os.fsync(f.fileno())
    need(sha(output) == hashlib.sha256(changed).hexdigest() and sha(baseline) == hashlib.sha256(raw).hexdigest(), 'output/input readback pins')
    record = {'schema': 'f10-r3-mixed-row-mutation/v1', 'status': 'FORMED_UNCHECKED',
              'root_registration_sha256': root_hash, 'input_sha256': hashlib.sha256(raw).hexdigest(),
              'output_sha256': sha(output), 'output_bytes': len(changed),
              'mutation': 'graph.slots[24] += X1^27', 'inverse_restored_whole_bytes': True, 'checker_run': False}
    with open(receipt, 'xb') as f:
        f.write(wire(record)); f.flush(); os.fsync(f.fileno())
    fd = os.open(writer, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


if __name__ == '__main__':
    main()
