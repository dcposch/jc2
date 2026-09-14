"""UNEXECUTED finite IN-PROCESS certificate corruptions, not main evidence.
Requires the separately successful genuine checker.main from this batch.
No repeated positive verify, matrix construction, solve or FLINT import.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

def main():
    if len(sys.argv) != 8:
        raise SystemExit('AUTH INPUT PRIOR_RECEIPT ACCEPTANCE CERTIFICATE FULL_RESULT OUTPUT')
    custody = authorize(sys.argv[1], __file__, 'check')
    from evidence import verified, bound, sha, require, write_exclusive
    data, binding, spec = verified(*sys.argv[1:5])
    certificate, certificate_sha = bound(spec, sys.argv[5])
    result, result_sha = bound(spec, sys.argv[6])
    require(certificate.get('binding') == binding and result.get('binding') == binding
            and result.get('certificate_sha256') == certificate_sha, 'genuine production result binding')
    statuses = {'UNIT': 'VERIFIED-GENERIC-ZERO-QUOTIENT',
                'SEPARATOR': 'VERIFIED-GENERIC-NONZERO-QUOTIENT'}
    require(certificate.get('branch') in statuses
            and result.get('status') == statuses[certificate['branch']], 'genuine production result status')
    require(result.get('checker_sha256') == sha(Path(__file__).with_name('checker.py')),
            'genuine checker code binding')
    import checker
    import copy
    import json
    from fractions import Fraction
    cases = []
    def reject(name, mutation, reason):
        fixture = {'input': copy.deepcopy(data), 'certificate': copy.deepcopy(certificate)}
        mutation(fixture)
        require(fixture != {'input': data, 'certificate': certificate}, 'fixture must change')
        path = Path(sys.argv[7]).parent / ('fixture-' + name + '.json')
        write_exclusive(path, fixture)
        digest = sha(path)
        # Intentional malformed rational floats are read by plain JSON here
        # to test checker.verify's own independent parser, not evidence.load.
        reread = json.loads(path.read_text())
        require(reread == fixture, 'fixture JSON retention')
        try:
            checker.verify(reread['input'], reread['certificate'])
        except Exception as exc:
            require(type(exc) is ValueError and str(exc) == reason,
                    name + ': unexpected rejection ' + type(exc).__name__ + ': ' + str(exc))
        else:
            raise RuntimeError(name + ': corrupted certificate/input accepted')
        require(sha(path) == digest, 'fixture drift')
        cases.append({'name': name, 'fixture_sha256': digest, 'fixture_bytes': path.stat().st_size,
                      'reason': reason, 'status': 'EXPECTED-REJECTION',
                      'entrypoint': 'checker.verify IN-PROCESS, not checker.main'})
    def dimension(f):
        f['certificate']['rows'] = 216
    reject('omitted-high-coordinate', dimension, 'certificate dimension/schema')
    def missing(f):
        f['certificate']['witness'].pop()
    reject('missing-witness-slot', missing, 'complete rational witness dimension')
    def floating(f):
        f['certificate']['witness'][0][0] = 0.5
    reject('floating-witness', floating, 'canonical rational strings only')
    def spelling(f):
        f['certificate']['witness'][0] = ['00', '1']
    reject('noncanonical-witness', spelling, 'canonical reduced rational')
    def modulus(f):
        n, d = f['input']['modulus'][0]
        f['input']['modulus'][0] = [str(int(n) + int(d)), d]
    reject('wrong-modulus', modulus, 'literal full modulus not a factor')
    def row(f):
        f['input']['rows'][0]['id'] = 'WRONG'
    reject('wrong-indexed-row', row, 'literal row order/degree envelope')
    def guard(f):
        f['input']['guard']['factors'].pop()
    reject('missing-guard-factor', guard, 'guard and both factors retained')
    if certificate['branch'] == 'SEPARATOR':
        def scale_dual(f):
            scaled = []
            for n, d in f['certificate']['witness']:
                q = 2 * Fraction(int(n), int(d))
                scaled.append([str(q.numerator), str(q.denominator)])
            f['certificate']['witness'] = scaled
        # Scaling preserves all 1638 zero columns but changes lambda*b=1 to2.
        reject('wrong-dual-normalization', scale_dual, 'dual target normalization equals one')
    else:
        index = next((i for i, obj in enumerate(data['rows']) if any(obj['coefficients'])), None)
        if index is None:
            cases.append({'name': 'wrong-primal-identity', 'status': 'NOT-APPLICABLE-ALL-INPUT-ROWS-ZERO',
                          'scope': 'no fabricated nonzero input; separate generic toy remains required'})
        else:
            def change_primal(f):
                position = index * 26 * 7
                n, d = f['certificate']['witness'][position]
                q = Fraction(int(n), int(d)) + 1
                f['certificate']['witness'][position] = [str(q.numerator), str(q.denominator)]
            reject('wrong-primal-identity', change_primal, 'full 217-coordinate sum h_i f_i equals q^5')
    require(len(cases) == 8, 'finite eight-control inventory including applicability')
    for filename in sys.argv[2:7]:
        require(sha(filename) == spec['file_sha256'][str(Path(filename).resolve())], 'control input drift')
    write_exclusive(sys.argv[7], {'status': 'FINITE-LINEAR-CONTROLS-COMPLETE', 'execution': custody,
        'binding': binding, 'certificate_sha256': certificate_sha, 'genuine_result_sha256': result_sha,
        'harness_sha256': sha(__file__), 'cases': cases,
        'limits': 'seven common corruptions plus one branch-specific or explicit inapplicable case; no positive rerun; no generic toys executed'})
    print('FINITE LINEAR CONTROLS COMPLETE; NO NEW DECISION')

if __name__ == '__main__':
    main()
