"""STATIC/UNEXECUTED metadata binding. Never issues ROOT acceptance.

Call only AFTER unchanged execution_gate.authorize. No mathematical imports.
The external ROOT acceptance is cooperative custody, not authentication.
"""
import hashlib
import json
from pathlib import Path

ADAPTER = '11ebf4307e7cff9b7909020dcdf69cda32f689236453763ce9433fff66fd7b67'
UNIV_CHECKER = '6547063b8cf2970ce0aa1e47e5a49db31c2fd4b1e97d87690c954487500a61f0'
INPUT_HELPER = 'd262f3d498323b4606c51828a647b7334e8885095b099acbff41d17dd6db88b9'
ARITHMETIC = '7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc'
ORIGINAL = '168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
NORMAL_GENERATOR = 'd444d022593c99a8d5a22d9cd9cbcac2bea9c88ef1a305d3c1c8ddf1635a6d8e'
NORMAL_CHECKER = '091bbf35693c52833f2de936eeecd2e734f8404f26e9c68039bb8ab6aaecb551'

def require(ok, why):
    if not ok:
        raise ValueError(why)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    def forbidden(value):
        raise ValueError('floating/nonfinite JSON forbidden')
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_float=forbidden, parse_constant=forbidden)

def bound(spec, filename):
    path = Path(filename).resolve(strict=True)
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(spec['file_sha256'].get(str(path)) == digest,
            'input not explicitly pinned or changed')
    return load(raw), digest

def verified(authority, artifact, receipt, acceptance_file):
    spec = load(Path(authority).read_bytes())
    acceptance, acceptance_sha = bound(spec, acceptance_file)
    require(type(acceptance) is dict and acceptance == spec.get('univariate_acceptance'),
            'ROOT acceptance file/payload mismatch')
    require(acceptance.get('schema') == 'F10-UNIVARIATE-ACCEPTANCE/v1'
            and acceptance.get('status') == 'ROOT-ACCEPTED-GENUINE-UNIVARIATE-CHECKER-RECEIPT',
            'no ROOT-issued univariate runtime acceptance')
    versions = {'adapter_sha256': ADAPTER, 'checker_sha256': UNIV_CHECKER,
                'backend_sha256': ARITHMETIC, 'input_evidence_sha256': INPUT_HELPER}
    require(all(acceptance.get(k) == v for k, v in versions.items()),
            'accepted univariate implementation versions differ')
    data, artifact_sha = bound(spec, artifact)
    full, receipt_sha = bound(spec, receipt)
    require(acceptance.get('univariate_sha256') == artifact_sha
            and acceptance.get('receipt_sha256') == receipt_sha,
            'ROOT acceptance binds different input/receipt')
    evidence = acceptance.get('input_evidence')
    require(type(evidence) is dict and set(evidence) == {
        'normalized_sha256', 'normalized_receipt_sha256', 'normal_generator_sha256',
        'normal_checker_sha256', 'original_source_sha256'}, 'input evidence shape')
    require(evidence['normal_generator_sha256'] == NORMAL_GENERATOR
            and evidence['normal_checker_sha256'] == NORMAL_CHECKER
            and evidence['original_source_sha256'] == ORIGINAL, 'original backend/source evidence')
    for key in ('normalized_sha256', 'normalized_receipt_sha256'):
        value = evidence[key]
        require(type(value) is str and len(value) == 64
                and all(c in '0123456789abcdef' for c in value), 'upstream evidence hash')
    require(data.get('implementation_sha256') == ADAPTER
            and data.get('input_evidence') == evidence, 'artifact producer/input evidence')
    require(full.get('status') == 'PASS-NINE-ROW-ADAPTER-NOT-IDEAL-DECISION'
            and full.get('univariate_sha256') == artifact_sha
            and full.get('input_evidence') == evidence, 'genuine full receipt binding')
    require(type(full.get('row_slots')) is int and full['row_slots'] == 9
            and full.get('guard_factors') == ['r', 'h0'], 'full receipt scope')
    require(type(full.get('actual_degrees')) is list and len(full['actual_degrees']) == 9
            and all(type(n) is int and -1 <= n <= 5 for n in full['actual_degrees'])
            and type(full.get('actual_guard_degree')) is int
            and -1 <= full['actual_guard_degree'] <= 5, 'receipt degree scope')
    root = Path(__file__).resolve().parent
    for name in ('solver.py', 'checker.py', 'evidence.py', 'algebra.py', 'execution_gate.py'):
        require(spec['file_sha256'].get(str(root / name)) == sha(root / name),
                'all decision source pins required')
    require(sha(root / 'algebra.py') == ARITHMETIC, 'frozen producer arithmetic changed')
    # The prior checker is NOT executed here, and a spelled receipt alone is
    # insufficient: the fresh independently issued ROOT acceptance is required.
    return data, {'univariate_sha256': artifact_sha, 'full_receipt_sha256': receipt_sha,
                  'acceptance_sha256': acceptance_sha, 'input_evidence': evidence,
                  'versions': versions}, spec

def producer_environment(spec):
    env = spec.get('python_flint')
    require(type(env) is dict and set(env) == {'version', 'module_file', 'module_sha256'},
            'explicit installed python-flint metadata required')
    require(type(env['version']) is str and bool(env['version']), 'installed version required')
    path = Path(env['module_file']).resolve(strict=True)
    require(spec['file_sha256'].get(str(path)) == env['module_sha256'] == sha(path),
            'installed python-flint module must be pinned before import')
    require('/usr/bin/python3' in spec['file_sha256'], 'interpreter pin required')
    # ROOT must additionally bind the installed native dependency closure in
    # file_sha256 before dispatch; this is NOT a package discovery or installer.
    return env

def write_exclusive(filename, data):
    with Path(filename).open('x', encoding='utf-8') as stream:
        json.dump(data, stream, sort_keys=True, separators=(',', ':'), allow_nan=False)
        stream.write('\n')
