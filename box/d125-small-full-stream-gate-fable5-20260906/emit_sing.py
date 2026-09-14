#!/usr/bin/env python3
"""Own emitter: JSONL and Singular bytes from the independent reconstruction; compare SHA-256 to remote hashes."""
import json, hashlib, sys, time, resource
from collections import Counter
sys.path.insert(0, '.')
import gate
REMOTE = {('unequal','rational'):('b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718'),
('unequal','golden'):('ad83add3ccdeb56914cf73ab06fe733f7b89aa984e586bb973dde04ca471613b','77f127a903152cc52ebb2fd40d8e0d7ca76aeba2fe7306b4e87872189c9c28ec'),
('common_3','rational'):('cb6dd5a002db764412ed5f755d868ef11d91eaa20835a1d981e4fabe9d0eb177','1cf13975b7b4daea1f895defa38aa777af861d804d051605c610fa61d483f632'),
('common_3','golden'):('7fa9f5d1be4aca6745f67a1e4a3dcc495f10ec6612fa13c9d87b01890643bc2c','101c4562a87f1ae5cff9745470f63f6a4fc0995ab7f9c54115bcb76f4595a607'),
('common_4','rational'):('276ee6f4c23df9577cbeb832f06e84ae1c06dcf29b960e067d08083d3a0db13e','0fde2d1d3cfcc3659f31431bbc2dca8ea506a870c6309e73217f4cd12b68ab7c'),
('common_4','golden'):('3e897ad6578a25aa0ce90e16ae8ab68c4ddf94f5bc2426045792982bf9ea892e','addff558c331a1e963e5a764feb192f6c3dc57a9e2b3a1b37aa355d3bcbd0f7b')}
def rt(q): return str(q.numerator) if q.denominator == 1 else f'({q.numerator}/{q.denominator})'
def emit(recs, variables, golden):
    s = 'ring R=' + ('(0,rho)' if golden else '0') + ',(' + ','.join(variables) + '),dp;\n' + ('minpoly=rho^2-3*rho+1;\n' if golden else '') + 'ideal I=\n'
    parts = []
    for r in recs:
        if r['type'] != 'row': continue
        terms = []
        for w, m in r['terms']:
            c = gate.decode(w)
            coeff = f'({rt(c.a)}+({rt(c.b)})*rho)' if c.b != 0 else rt(c.a)
            f = [f'({coeff})'] + [variables[i] if p == 1 else f'{variables[i]}^{p}' for i, p in sorted(Counter(m).items())]
            terms.append('*'.join(f))
        parts.append('// ' + r['label'] + '\n' + ('+'.join(terms) if terms else '0'))
    return (s + ',\n'.join(parts) + ';\nprint("D125_COMPLETE_LITERAL_IMPORT_ONLY");\nprint(size(I));\nquit;\n').encode('ascii')
cust = json.load(open('/tmp/jc2-lane.aUnxIy/inputs/custody.json'))
out = []
for c in cust['cases']:
    t0 = time.time(); case, branch = c['case'], c['branch']; golden = branch == 'golden'
    hdr = json.loads(c['header']) if isinstance(c['header'], str) else c['header']
    recs, variables = gate.reconstruct(case, branch)
    recs[0]['authority_sha256'] = hdr['authority_sha256']; recs.append(gate.footer_for(recs))
    jb = b''.join(gate.canon(r) for r in recs); sb = emit(recs, variables, golden)
    # own restricted parser on own emitted bytes (self-consistency of the grammar reading)
    rows = [r for r in recs if r['type'] == 'row']
    nr, nz = gate.check_singular(sb.decode('ascii'), variables, golden, rows)
    r = {'case': case, 'branch': branch, 'jsonl_sha256': hashlib.sha256(jb).hexdigest(), 'jsonl_bytes': len(jb), 'sing_sha256': hashlib.sha256(sb).hexdigest(), 'sing_bytes': len(sb),
         'jsonl_match_remote': hashlib.sha256(jb).hexdigest() == REMOTE[(case, branch)][0], 'sing_match_remote': hashlib.sha256(sb).hexdigest() == REMOTE[(case, branch)][1],
         'singular_rows': nr, 'singular_nonzero': nz, 'seconds': round(time.time()-t0, 2)}
    out.append(r); print(json.dumps(r))
res = {'schema': 'own-emission-vs-remote-hash/v1', 'gate_sha256': hashlib.sha256(open('gate.py','rb').read()).hexdigest(), 'results': out, 'all_match': all(r['jsonl_match_remote'] and r['sing_match_remote'] for r in out), 'max_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, 'cpu_seconds': round(resource.getrusage(resource.RUSAGE_SELF).ru_utime, 2)}
json.dump(res, open('local-emission-vs-remote-hash.json', 'w'), indent=1); print('ALL_MATCH', res['all_match'], 'rss', res['max_rss_kib'], 'cpu', res['cpu_seconds'])
