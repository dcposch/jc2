"""UNEXECUTED finite in-process negative controls, not a production verifier.
Run only after a separate successful production checker receipt. No solver.
argv: AUTH ORIGINAL RETAINED FULL_RECEIPT CONTROLS_RECEIPT
The unchanged checker's private rational parser is NOT exposed or replaced.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize


def main():
    if len(sys.argv) != 6:
        raise SystemExit('usage: semantic_controls.py AUTH ORIGINAL RETAINED FULL_RECEIPT CONTROLS_RECEIPT')
    custody = authorize(sys.argv[1], __file__, 'check')
    # Every mathematical import and changed-object operation is below authority.
    import copy
    import hashlib
    import json
    import checker

    def require(ok, why):
        if not ok:
            raise RuntimeError(why)

    def sha(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    spec = json.loads(Path(sys.argv[1]).read_text())
    paths = [Path(x).resolve(strict=True) for x in sys.argv[2:5]]
    original_path, retained_path, full_path = paths
    for path in paths:
        require(spec['file_sha256'].get(str(path)) == sha(path), 'each control input must be freshly registered')
    original = json.loads(original_path.read_text())
    retained = json.loads(retained_path.read_text())
    full = json.loads(full_path.read_text())
    checker_path = Path(checker.__file__).resolve(strict=True)
    require(sha(original_path) == checker.SOURCE_SHA, 'frozen original source')
    require(spec['file_sha256'].get(str(checker_path)) == sha(checker_path), 'registered checker code')
    require(full['verdict'] == 'PASS-REPRESENTATION-NOT-IDEAL-DECISION'
            and full['source_sha256'] == sha(original_path)
            and full['retained_sha256'] == sha(retained_path)
            and full['checker_sha256'] == sha(checker_path), 'genuine prior production receipt binding')
    require(full['original_slots'] == 20 and full['retained_slots'] == 17
            and full['full_bracket_bands'] == 8 and full['inverse_pole_slots'] == 10, 'genuine full-condition inventory')
    cases = []

    def reject(name, mutate, exception_type, reason):
        changed = copy.deepcopy(retained)
        mutate(changed)
        fixture = Path(sys.argv[5]).parent / ('fixture-' + name + '.json')
        with fixture.open('x') as stream:
            json.dump(changed, stream, sort_keys=True, separators=(',', ':'), allow_nan=False)
            stream.write('\n')
        fixture_sha = sha(fixture)
        reread = json.loads(fixture.read_text())
        require(reread == changed, 'harness JSON changed fixture values')
        try:
            checker.verify(original, reread)
        except Exception as exc:
            require(type(exc) is exception_type and str(exc) == reason,
                    name + ': unexpected rejection: ' + type(exc).__name__ + ': ' + str(exc))
        else:
            raise RuntimeError(name + ': changed object accepted')
        require(sha(fixture) == fixture_sha, 'fixture drift during in-process control')
        cases.append({'name': name, 'fixture_sha256': fixture_sha, 'fixture_bytes': fixture.stat().st_size,
                      'exception': exception_type.__name__, 'reason': reason,
                      'entrypoint': 'checker.verify IN-PROCESS, not checker.main', 'status': 'EXPECTED-REJECTION'})

    reject('dropped-retained-row', lambda x: x['rows'].pop(0), ValueError, 'all20 original slots')
    reject('incorrect-L-inverse', lambda x: x['units'].__setitem__('Linv', []), ValueError, 'L inverse identity')
    reject('incorrect-scale', lambda x: x['mapping'].__setitem__(3, []), ValueError, 'retained scale/parameter mapping')
    reject('incorrect-modulus', lambda x: x.__setitem__('modulus', []), ValueError, 'wrong modulus')

    def lose_negative_s(x):
        wire = x['mapping'][6]
        require(wire and all(term[0][8] < 0 for term in wire), 'negative-s fixture precondition')
        for term in wire:
            term[0][8] = -term[0][8]
    reject('negative-s-sign-loss', lose_negative_s, ValueError, 'retained scale/parameter mapping')
    reject('negative-lower-exponent', lambda x: x['mapping'][0][0][0].__setitem__(0, -1), ValueError, 'Laurent/basis exponent domain')
    reject('omitted-pole-slot', lambda x: x['pole_slots']['B'].pop(), ValueError, 'all ten pole slots')
    reject('omitted-restoration-slot', lambda x: x['restoration'].pop('a'), KeyError, "'a'")
    reject('incorrect-leading-B5', lambda x: x['B'].__setitem__(5, []), ValueError, 'leading B coefficient')
    reject('float-anywhere', lambda x: x.__setitem__('control_float', 0.5), ValueError, 'floating point forbidden anywhere')

    big = 9007199254740993
    rounded = int(float(big))
    require(big > 2**53 and rounded != big, 'genuine beyond-binary64 rounding precondition')
    def wrong_large_row(value):
        def mutate(x):
            require(x['rows'][0]['id'] == 'E1/S0', 'precision row identity')
            wire = [[[0] * 12, str(value), '1']]
            require(x['rows'][0]['polynomial'] != wire, 'precision fixture must change the row')
            x['rows'][0]['polynomial'] = wire
        return mutate
    reject('large-canonical-string', wrong_large_row(big), ValueError, 'original row substitution E1/S0')
    reject('rounded-canonical-string', wrong_large_row(rounded), ValueError, 'original row substitution E1/S0')
    require(len(cases) == 12, 'finite controls inventory')
    for path in paths:
        require(sha(path) == spec['file_sha256'][str(path)], 'registered control input drift')
    report = {'status': 'FINITE-CONTROLS-PASS-NOT-IDEAL-DECISION', 'execution': custody,
              'source_sha256': sha(original_path), 'retained_sha256': sha(retained_path),
              'genuine_production_receipt_sha256': sha(full_path), 'checker_sha256': sha(checker_path),
              'harness_sha256': sha(__file__), 'cases': cases,
              'precision': {'exact_string': str(big), 'rounded_string': str(rounded),
                            'scope': 'harness persistence plus two semantic rejections; NO successful nested-parser precision payload claim'},
              'positive_scope': 'separate registered checker.main; this harness does not repeat a positive verification',
              'negative_limit': 'no altered-pair negative claim for the late bracket or pole equations'}
    with Path(sys.argv[5]).open('x') as stream:
        json.dump(report, stream, sort_keys=True, separators=(',', ':'), allow_nan=False)
        stream.write('\n')
    print(report['status'])


if __name__ == '__main__':
    main()
