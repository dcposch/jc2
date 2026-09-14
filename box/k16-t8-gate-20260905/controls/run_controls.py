#!/usr/bin/env python3
"""Regenerate t6 controls from exact rows, export by substitution/rename, run F4."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path('/home/ubuntu/jc2')
OUT = Path(__file__).resolve().parent
GEN = ROOT / 'box/k16t8-20260905/gen.py'
MSOLVE = ROOT / 'box/moh14-charts-20260905/tools/msolve-0.10.1-official-intel-avx512/msolve'
spec = importlib.util.spec_from_file_location('charged_gen', GEN)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args, prefix, seconds=600):
    started = time.time()
    with prefix.with_suffix('.out').open('w') as stdout, prefix.with_suffix('.err').open('w') as stderr:
        result = subprocess.run(['/usr/bin/time', '-v', '-o', str(prefix.with_suffix('.time')),
                                 'timeout', '-k', '15s', str(seconds)] + list(map(str, args)),
                                stdout=stdout, stderr=stderr)
    data = {'argv': list(map(str, args)), 'timeout_seconds': seconds,
            'exit_code': result.returncode, 'wall_seconds': round(time.time() - started, 3)}
    prefix.with_suffix('.status.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'prefix': str(prefix), **data}), flush=True)
    assert result.returncode == 0, data
    return data


summary = {'source': {'gen.py': digest(GEN),
                      'terminal_t6_exact_none.out': digest(gen.ROWS / 'terminal_t6_exact_none.out'),
                      'ctrl_t6_affinew_ms.sing': digest(ROOT / 'box/k16t8-20260905/ctrl_t6_affinew_ms.sing'),
                      'msolve': digest(MSOLVE)}, 'runs': []}
rows = gen.read_rows(6)
denominators = [int(d) for s in rows.values() for d in re.findall(r'/([0-9]+)', s)]
for p in [32003, 32009]:
    roots = gen.mod_roots(6, p)
    assert len(roots) == 2
    assert all(d % p for d in denominators)
    stem = f't6_p{p}'
    lines, vars_p = gen.prefix(6, 'mod', p, 0, stem)
    lines += ['print("GATE_RING_ASSERT="+string(nvars(basering)==5 && char(basering)==' + str(p) + '));',
              'ideal SysY=subst(I2,b4,1);',
              'ideal SysW=subst(I2+Ws,b4,1);',
              'print("GATE_GENERATOR_COUNTS Y="+string(size(SysY))+" W="+string(size(SysW)));',
              'int i; int elimok=1; int zerogens=0; int constantgens=0;',
              'for(i=1;i<=size(SysW);i++){ if(SysW[i]!=subst(SysW[i],b4,0)){elimok=0;} if(SysW[i]==0){zerogens++;} if(deg(SysW[i])==0){constantgens++;} }',
              'print("GATE_B4_ELIMINATED="+string(elimok)+" ZERO_GENS="+string(zerogens)+" CONSTANT_GENS="+string(constantgens));']
    for kind in ['Y', 'W']:
        path = OUT / f'{stem}_{kind}_raw.txt'
        lines += [f'write(":w {path}","BEGIN");',
                  f'for(i=1;i<=size(Sys{kind});i++){{ write(":a {path}",string(Sys{kind}[i])); }}']
    lines += ['print("GATE_EXPORT_DONE");', 'quit;']
    driver = OUT / f'{stem}_export.sing'
    driver.write_text('\n'.join(lines) + '\n')
    export = run(['Singular', '-q', driver], OUT / f'{stem}_export', seconds=60)
    transcript = (OUT / f'{stem}_export.out').read_text()
    assert 'FAIL' not in transcript and 'error' not in transcript and 'div. by 0' not in transcript
    assert 'GATE_RING_ASSERT=1' in transcript
    assert 'GATE_GENERATOR_COUNTS Y=10 W=15' in transcript
    assert 'GATE_B4_ELIMINATED=1 ZERO_GENS=0 CONSTANT_GENS=0' in transcript
    assert 'GATE_EXPORT_DONE' in transcript
    for kind, expected_count in [('Y', 10), ('W', 15)]:
        raw = OUT / f'{stem}_{kind}_raw.txt'
        raw_lines = raw.read_text().splitlines()
        assert raw_lines.pop(0) == 'BEGIN'
        assert len(raw_lines) == expected_count
        renamed = []
        for line in raw_lines:
            image = line
            for j in range(2, 6):
                image = image.replace(f'q{j}_0', f'q{j}')
            assert not re.search(r'_|b4|b3|yy', image)
            assert set(re.findall(r'[a-zA-Z][a-zA-Z0-9]*', image)) <= {'q2', 'q3', 'q4', 'q5'}
            assert re.fullmatch(r'[0-9q+*^\-]+', image)
            inverse = re.sub(r'\bq([2-5])\b', r'q\1_0', image)
            assert inverse == line
            renamed.append(image)
        ms = OUT / f'{stem}_{kind}.ms'
        ms.write_text('q2,q3,q4,q5\n' + str(p) + '\n' + ',\n'.join(renamed) + '\n')
        original_kind = 'y6' if kind == 'Y' else 'wlocus'
        charged_match = None
        if p == 32003:
            charged_match = ms.read_bytes() == (ROOT / f'box/k16t8-20260905/ctrl_t6_{original_kind}.ms').read_bytes()
            assert charged_match
        gb = OUT / f'{stem}_{kind}_gb.txt'
        run_result = run([MSOLVE, '-f', ms, '-o', gb, '-g', '2', '-t', '4', '-v', '2'],
                         OUT / f'{stem}_{kind}_msolve')
        gb_text = gb.read_text()
        count = int(re.search(r'#length of basis:\s+(\d+)', gb_text).group(1))
        is_unit = re.sub(r'(?m)^#.*\n?', '', gb_text).strip() == '[1]:'
        assert (kind == 'W' and is_unit and count == 1) or (kind == 'Y' and not is_unit and count > 1)
        record = {'prime': p, 'roots': roots, 'chosen_root': roots[0],
                  'denominator_occurrences': len(denominators), 'bad_denominators': 0,
                  'kind': kind, 'generators': expected_count, 'basis_length': count,
                  'unit': is_unit, 'same_bytes_as_charged_32003': charged_match,
                  'driver_sha256': digest(driver), 'raw_sha256': digest(raw),
                  'ms_sha256': digest(ms), 'gb_sha256': digest(gb),
                  'export': export, 'msolve': run_result}
        summary['runs'].append(record)
        (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
        print(json.dumps(record), flush=True)
print('ALL_FOUR_CONTROLS_PASS', flush=True)
