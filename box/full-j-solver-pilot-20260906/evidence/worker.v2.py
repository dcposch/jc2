#!/usr/bin/env python3
"""Fresh-scratch-only worker: custody preparation, build, or exec one solver."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import socket
import subprocess
import sys
import time

ROOT = Path('/home/ubuntu/full-j-solver-pilot-20260906')
SOURCE = Path('/home/ubuntu/factored-jacobian-pilot-20260906')
TAG = 'full-j-solver-pilot-astra-20260906'
PRIME = 1073741827


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


def sha(path):
    d = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            d.update(b)
    return d.hexdigest()


def save(name, obj):
    with (ROOT/name).open('x') as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write('\n')


def guard():
    need(sys.platform.startswith('linux'), 'Linux required')
    need(socket.gethostname() == 'ip-172-30-0-56', 'Exact worker required')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2', 'EC2 required')
    need(os.environ.get('JC2_REGISTERED_JOB') == TAG, 'Registration required')
    need(Path.cwd().resolve() == ROOT, 'Fresh task root required')
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def prepare():
    started = time.monotonic()
    need(sha(SOURCE/'complete_checked.sing') == '50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091', 'Singular source hash')
    need(sha(SOURCE/'complete_export.generators.jsonl') == '39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f', 'Stream source hash')
    export = json.loads((SOURCE/'complete_export.json').read_text())
    field_map = {'prime': PRIME, 'kind': 'coefficientwise Q-to-Fp reduction', 'denominators': set()}
    inverse_cache = {}
    coeff = re.compile(r'(^|[+-])(\d+)(?:/(\d+))?(?=\*|$|[+-])')
    def modular(match):
        sign, num, den = match.groups()
        den = int(den or '1')
        need(den % PRIME != 0, 'Bad denominator prime')
        field_map['denominators'].add(den)
        if den not in inverse_cache:
            inverse_cache[den] = pow(den, -1, PRIME)
        value = int(num) % PRIME * inverse_cache[den] % PRIME
        need(value != 0, 'Zero reduced term needs canonical rewrite; refusing')
        return sign + str(value)
    def wrap(text):
        need(re.search(r'\^\d+/', text) is None, 'Unsafe fractional power spelling')
        return re.sub(r'(?<![A-Za-z0-9_^])(\d+)/(\d+)', r'(\1/\2)', text)
    row_sha = hashlib.sha256()
    labels, count, terms, kinds = [], 0, 0, {}
    with (SOURCE/'complete_export.generators.jsonl').open() as js, (SOURCE/'complete_checked.sing').open() as old, (ROOT/'complete.slimgb.sing').open('x') as sg, (ROOT/'complete.p1073741827.ms').open('x') as ms:
        header = json.loads(next(js))
        names = header['variables']
        need(header['field'] == 'Q' and header['order'] == 'global dp', 'Ring')
        need(len(names) == len(set(names)) == 600 and names == export['coordinate_order'], 'All600 variables in literal order')
        need(header['localizers'] == ['Zj*J0-1'], 'Genuine inverse')
        line1, line2 = next(old), next(old)
        need(line1 == 'ring R=0,('+','.join(names)+'),dp;\n' and line2 == 'ideal I=\n', 'Literal ring/header')
        sg.write(line1+line2)
        ms.write(','.join(names)+'\n'+str(PRIME)+'\n')
        for line in js:
            row = json.loads(line)
            if row['type'] == 'complete':
                need(not js.read().strip(), 'Trailing stream data')
                footer = row
                break
            need(row['type'] == 'generator' and row['index'] == count, 'Sequential row')
            poly, label = row['polynomial'], row['label']
            need(label not in labels, 'Unique label')
            expected = (',' if count else '') + wrap(poly) + '\n'
            need(next(old) == expected, 'Literal all-row Singular equality')
            sg.write(expected)
            modpoly = coeff.sub(modular, re.sub(r'\s+', '', poly))
            need('/' not in modpoly, 'All rational coefficients reduced')
            ms.write((',' if count else '')+modpoly+'\n')
            row_sha.update(line.encode())
            labels.append(label)
            terms += row['terms']
            kind = 'define' if label.startswith('define_') else 'inverse' if label == 'inverse_J' else 'J'
            kinds[kind] = kinds.get(kind, 0)+1
            count += 1
        need(footer == export['complete_ideal'], 'Full footer')
        need((count, terms) == (1629, 11299180), 'Full census')
        need(kinds == {'define':160, 'inverse':1, 'J':1468}, 'All required blocks')
        need(row_sha.hexdigest() == footer['generator_stream_sha256'], 'Literal row stream SHA')
        need(next(old) == ';\n', 'Complete old ideal delimiter')
        # Retain the entire exact-Q ideal, replacing only the parse-only footer.
        sg.write(';\nprint("ALL_ROWS_PARSED");\nprint("GENERATORS="+string(size(I)));\nprint("VARIABLES="+string(nvars(basering)));\n')
        sg.write('option(redSB); option(prot);\nprint("BEGIN_SLIMGB");\nideal G=slimgb(I);\nprint("END_SLIMGB");\nG=interred(G);\n')
        sg.write('print("BEGIN_RESULT");\nprint("REDUCE_ONE="+string(reduce(1,G)));\nprint("BASIS_SIZE="+string(size(G)));\nprint("DIMENSION="+string(dim(G)));\nprint("INPUT_REMAINDER_SIZE="+string(size(reduce(I,G))));\n')
        sg.write('write("'+str(ROOT/'singular'/'basis.sing')+'",G);\nprint("END_RESULT");\nquit;\n')
    field_map['denominators'] = sorted(field_map['denominators'])
    save('map.json', {'source_header':header,'field_map':field_map,'labels':labels,'kinds':kinds,
        'rows':count,'terms':terms,'row_sha256':row_sha.hexdigest(),'variables_removed':[],
        'singular_input_sha256':sha(ROOT/'complete.slimgb.sing'),
        'msolve_input_sha256':sha(ROOT/'complete.p1073741827.ms'),
        'elapsed_seconds':time.monotonic()-started})
    print('COMPLETE_INPUT_PREPARED', count, terms, flush=True)


def build():
    src = ROOT/'msolve-source'
    subprocess.run(['git','clone','--quiet','--branch','v0.10.1','--depth','1','https://github.com/algebraic-solving/msolve.git',str(src)], check=True)
    commit = subprocess.check_output(['git','rev-parse','HEAD'], cwd=src, text=True).strip()
    need(commit == '185e7b92fa0687f4db68b0f2f453a835668ac132', 'Pinned source commit')
    for name in ['heap-sort-permutation','int64-input-offset']:
        patch = ROOT/('msolve-0.10.1-'+name+'.patch')
        subprocess.run(['patch','--dry-run','-p1','-i',str(patch)],cwd=src,check=True)
        subprocess.run(['patch','-p1','-i',str(patch)],cwd=src,check=True)
        subprocess.run(['patch','--dry-run','-R','-p1','-i',str(patch)],cwd=src,check=True)
    subprocess.run(['git','diff','--check'],cwd=src,check=True)
    files = {'src/msolve/iofiles.c':'e0107ae05994a3480ca95d0f289529b9fe4537826702458fe467b68652bae874',
             'src/neogb/io.c':'71077383a1b2c1bdb2c01cffd0956593879fe627ae13766fa3342a40247ef3e6'}
    for name, digest in files.items():
        need(sha(src/name) == digest, 'Patched source differs from terminal provenance: '+name)
    for cmd in [['./autogen.sh'],['./configure','--prefix='+str(ROOT/'msolve-install'),'CFLAGS=-O3 -march=native'],['make','-j8'],['make','check','-j8']]:
        subprocess.run(cmd,cwd=src,check=True)
    bins = ['.libs/msolve','src/msolve/.libs/libmsolve.so.3.0.7','src/neogb/.libs/libneogb.so.3.0.7','msolve']
    save('binary.json', {'commit':commit,'patch_source_hashes':files,'files':{name:sha(src/name) for name in bins},
                        'binary':str(src/'msolve'),'make_check':'completed exit0'})
    print('PINNED_PATCHED_BUILD_PASS', flush=True)


def execute(engine):
    need((ROOT/'GREEN.json').is_file(), 'Explicit root GREEN required')
    out = ROOT/engine
    out.mkdir()
    inp = ROOT/('complete.slimgb.sing' if engine == 'singular' else 'complete.p1073741827.ms')
    mapping = json.loads((ROOT/'map.json').read_text())
    need(sha(inp) == mapping[engine+'_input_sha256'], 'Frozen solve input')
    if engine == 'singular':
        binary = Path('/usr/bin/Singular')
        need(sha(binary) == '90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4', 'Singular binary')
        argv = [str(binary),'-q','--no-rc','--no-warn','--no-shell','--threads=1','--flint-threads=1',str(inp)]
    else:
        rec = json.loads((ROOT/'binary.json').read_text())
        for name, digest in rec['files'].items():
            need(sha(ROOT/'msolve-source'/name) == digest, 'Patched binary/library drift')
        need((ROOT/'smoke.PASS').is_file(), 'Patched smoke checks required')
        binary = Path(rec['binary'])
        argv = [str(binary),'-g','2','-t','8','-v','2','--random-seed','0','-f',str(inp),'-o',str(out/'basis.ms')]
    save(engine+'.launch.json', {'hostname':socket.gethostname(),'pid':os.getpid(),'pgid':os.getpgrp(),
        'proc_stat':Path('/proc/self/stat').read_text(),'argv':argv,'input_sha256':sha(inp),
        'timestamp':time.time(),'environment':{'JC2_REGISTERED_JOB':TAG},'prime':0 if engine=='singular' else PRIME})
    os.environ['BROWSER'] = 'cat'
    os.environ['ESINGULAR_BROWSER'] = 'cat'
    os.environ['OMP_NUM_THREADS'] = '1' if engine == 'singular' else '8'
    os.execv(str(binary),argv)


guard()
if sys.argv[1] == 'prepare': prepare()
elif sys.argv[1] == 'build': build()
elif sys.argv[1] in ('singular','msolve'): execute(sys.argv[1])
else: raise ValueError('Unknown mode')
