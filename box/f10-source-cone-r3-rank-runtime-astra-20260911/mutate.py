"""STATIC independent inverse-coordinate mutator; never rank-authorize/import finder."""
import os
import sys
import pathlib
import json
import re

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from probe import policy, frozen, metadata, sha, need, pairs, SCIENCE, LIMITS, JOB

RANK_OK = 'R3_FULL_ROW_RANK_CHECKED_NO_AUTOMATIC_SOURCE_PROMOTION'
MUTATION = 'inverse[0][0][0] := (a+1) mod p'
CAP = 16777216


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode('ascii')


def write(path, raw, cap):
    need(0 < len(raw) <= cap, 'output cap')
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'wb') as out:
        out.write(raw); out.flush(); os.fsync(out.fileno())
    need(path.read_bytes() == raw, 'output readback')


def main():
    need(len(sys.argv) == 7 and sys.argv[1] == '--registration'
         and sys.argv[3] == '--root-registration-sha256' and sys.argv[5] == '--positive-record', 'literal mutator CLI')
    need(re.fullmatch('[0-9a-f]{64}', sys.argv[4]), 'ROOT SHA syntax')
    r, root_sha = policy(sys.argv[2], 'mutator', sys.argv[4])
    phase_path = frozen(sys.argv[6])
    need(phase_path == pathlib.Path(r['authority_dir']) / 'positive.json', 'fixed phase path')
    phase = metadata(phase_path)
    target = pathlib.Path(r['frozen_dir']) / 'certificate.json'
    output = pathlib.Path(r['writer_dir']) / 'inverse-entry.json'
    expected_policy = {'baseline': r['baseline'], 'place': r['place'],
        'certificate': str(target), 'fixture': str(pathlib.Path(r['frozen_dir']) / 'inverse-entry.json'),
        'mutation': MUTATION, 'source_files': SCIENCE, 'source_limits': LIMITS, 'positive_record': str(phase_path)}
    need(r['phase_policy'] == expected_policy and phase['policy'] == expected_policy, 'literal mutation policy')
    runtime = {'python_sha256': r['pins'][r['files']['python']], 'native_path': r['source_native_manifest'],
               'native_sha256': r['pins'][r['source_native_manifest']]}
    need(set(phase) == {'schema','status','root_registration_sha256','certificate','positive_receipt',
         'authorization','source_files','baseline','place','runtime','policy'}
         and phase['schema'] == 'f10-r3-rank-positive-phase/v1' and phase['status'] == RANK_OK
         and phase['root_registration_sha256'] == root_sha and phase['source_files'] == SCIENCE
         and phase['baseline'] == r['baseline'] and phase['place'] == r['place']
         and phase['runtime'] == runtime, 'authenticated ROOT positive phase')
    cert = phase['certificate']; frozen(target)
    need(set(cert) == {'path','sha256','bytes'} and cert['path'] == str(target)
         and type(cert['bytes']) is int and 0 < target.stat().st_size == cert['bytes'] <= CAP
         and sha(target) == cert['sha256'], 'frozen positive certificate')
    auth = phase['authorization']; receipt = phase['positive_receipt']
    for item, name, parent in ((auth,'check-positive.json',r['authority_dir']),
                              (receipt,'check-positive.receipt.json',r['frozen_dir'])):
        need(set(item) == {'path','sha256'} and item['path'] == str(pathlib.Path(parent) / name)
             and sha(frozen(item['path'])) == item['sha256'], 'positive evidence pin')
    sources = {name: {'path': str(pathlib.Path(r['science_dir']) / name), 'sha256': pin} for name,pin in SCIENCE.items()}
    a = metadata(pathlib.Path(auth['path']))
    need(a['schema'] == 'r3-rank-authorization-v1' and a['job_tag'] == JOB and a['mode'] == 'check'
         and a['authority'] == 'ROOT-CAPRUN' and a['status'] == 'REGISTERED' and a['files'] == sources
         and a['runtime'] == runtime and a['limits'] == LIMITS and a['baseline'] == r['baseline']
         and a['place'] == r['place'] and a['artifact'] == {'path':str(target),'sha256':cert['sha256']}, 'positive source policy')
    expected_receipt = {'schema':'r3-rank-receipt-v1','job_tag':JOB,'mode':'check','status':RANK_OK,
        'science':'NONE','authorization_sha256':auth['sha256'],'baseline_sha256':r['baseline']['sha256'],
        'qualification_sha256':r['baseline']['qualification_sha256'],'place':r['place'],
        'certificate_sha256':cert['sha256'],'files':sources,'runtime':runtime,
        'details':{'rows':'297','columns':'1453','identity_positions':'88209','residue_degree':str(len(r['place']['phi'])-1)}}
    need(metadata(pathlib.Path(receipt['path']),32768) == expected_receipt, 'exact positive inverse receipt')
    # All authority/evidence/native/baseline byte checks precede the sole payload read.
    raw = target.read_bytes()
    def bad(_):
        raise ValueError('native JSON number/constant forbidden')
    doc = json.loads(raw, object_pairs_hook=pairs, parse_int=bad, parse_float=bad, parse_constant=bad)
    need(encode(doc) == raw, 'canonical whole certificate')
    need(set(doc) == {'format','job_tag','baseline_sha256','qualification_sha256','place','dimensions',
                     'finder_sha256','columns','inverse'} and doc['format'] == 'r3-rank-inverse-v1'
         and doc['job_tag'] == JOB and doc['baseline_sha256'] == r['baseline']['sha256']
         and doc['qualification_sha256'] == r['baseline']['qualification_sha256']
         and doc['place'] == r['place'] and doc['dimensions'] == ['297','1453']
         and doc['finder_sha256'] == SCIENCE['finder.py'], 'positive certificate fixed schema')
    ptext = r['place']['p']
    need(type(ptext) is str and re.fullmatch('[1-9][0-9]{0,9}',ptext), 'ROOT prime integer')
    p = int(ptext); need(2 <= p <= 2147483647, 'ROOT prime bound, not primality oracle')
    degree = len(r['place']['phi']) - 1
    matrix = doc['inverse']
    need(type(matrix) is list and len(matrix) == 297 and type(doc['columns']) is list
         and len(doc['columns']) == 297, 'fixed dimensions')
    for row in matrix:
        need(type(row) is list and len(row) == 297, 'inverse row length')
        for vector in row:
            need(type(vector) is list and len(vector) == degree, 'dense fixed-degree inverse coordinate')
            for coordinate in vector:
                need(type(coordinate) is str and re.fullmatch('0|[1-9][0-9]{0,9}',coordinate)
                     and int(coordinate) < p, 'canonical residue')
    old = matrix[0][0][0]; changed = str((int(old) + 1) % p)
    need(changed != old and str((int(changed)-1) % p) == old, 'exact nonzero unit mutation')
    matrix[0][0][0] = changed; modified = encode(doc)
    matrix[0][0][0] = old
    need(encode(doc) == raw, 'inverse restoration of WHOLE baseline bytes')
    need(sha(target) == cert['sha256'], 'immutable positive still pinned')
    policy(sys.argv[2], 'mutator', root_sha)
    write(output, modified, CAP)
    write(pathlib.Path(r['writer_dir']) / 'mutation.json', encode({
        'schema':'f10-r3-inverse-entry-mutation/v1','status':'FORMED_UNCHECKED',
        'root_registration_sha256':root_sha,'input_sha256':cert['sha256'],
        'output_sha256':sha(output),'output_bytes':len(modified),'mutation':MUTATION,
        'inverse_restored_whole_bytes':True,'checker_run':False}),32768)


if __name__ == '__main__':
    main()
