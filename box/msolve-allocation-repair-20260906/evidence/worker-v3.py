#!/usr/bin/env python3
"""Task-owned preparation/build/tiny-tests only. No giant input mode exists."""
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
from fractions import Fraction

ROOT=Path('/home/ubuntu/msolve-allocation-repair-20260906')
TAG='msolve-allocation-repair-astra-20260906'
COMMIT='185e7b92fa0687f4db68b0f2f453a835668ac132'

def need(ok, why):
    if not ok: raise RuntimeError(why)

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def save(name, value):
    with (ROOT/name).open('x') as f:
        json.dump(value,f,indent=2,sort_keys=True); f.write('\n')

def run(argv, cwd=None):
    print('ARGV',json.dumps(argv),flush=True)
    subprocess.run(argv,cwd=cwd or ROOT,check=True)

def guard():
    need(sys.platform.startswith('linux'), 'Linux required')
    need(socket.gethostname()=='ip-172-30-0-56', 'exact worker required')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','EC2 required')
    need(os.environ.get('JC2_REGISTERED_JOB')==TAG,'registered tag required')
    need(Path.cwd().resolve()==ROOT,'fresh task root required')
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    save(sys.argv[1]+'.identity.json', {'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        'hostname':socket.gethostname(),'pid':os.getpid(),'pgid':os.getpgrp(),
        'proc_stat':Path('/proc/self/stat').read_text(),'tag':TAG,'argv':sys.argv})

def build():
    src=ROOT/'msolve-source'
    run(['git','clone','--quiet','--branch','v0.10.1','--depth','1',
         'https://github.com/algebraic-solving/msolve.git',str(src)])
    need(subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip()==COMMIT,'pinned commit')
    record=json.loads((ROOT/'source-inputs.json').read_text())
    for name in ('heap-sort-permutation','int64-input-offset','checked-input-allocation'):
        p=ROOT/('msolve-0.10.1-'+name+'.patch')
        need(sha(p)==record[p.name],'patch hash '+name)
        run(['patch','--dry-run','-p1','-i',str(p)],src)
        run(['patch','-p1','-i',str(p)],src)
        if name=='int64-input-offset':
            need(sha(src/'src/msolve/iofiles.c')=='e0107ae05994a3480ca95d0f289529b9fe4537826702458fe467b68652bae874','historical parser hash')
            need(sha(src/'src/neogb/io.c')=='71077383a1b2c1bdb2c01cffd0956593879fe627ae13766fa3342a40247ef3e6','historical heap hash')
    for name,digest in record['edited_source'].items():
        need(sha(src/name)==digest,'edited source hash '+name)
    run(['git','diff','--check'],src)
    for cmd in (['./autogen.sh'],['./configure','--prefix='+str(ROOT/'msolve-install'),'CFLAGS=-O3 -march=native'],
                ['make','-j8'],['make','check','-j8']):
        run(cmd,src)
    names=['.libs/msolve','msolve','src/msolve/.libs/libmsolve.so.3.0.7','src/neogb/.libs/libneogb.so.3.0.7']
    save('build.json', {'commit':COMMIT,'input':record,'binaries':{n:sha(src/n) for n in names},
        'compiler':subprocess.check_output(['cc','--version'],text=True),
        'upstream_tests':'make check -j8 exited 0'})
    print('BUILD_PASS',flush=True)

def upgrade():
    # The allocation-only first build is terminal and recorded, not live.
    old=json.loads((ROOT/'build.telemetry.json').read_text())
    need(old['status']=='NORMAL_EXIT' and old['child_returncode']==0,'first build terminal')
    src=ROOT/'msolve-source'
    rec=json.loads((ROOT/'source-inputs-v2.json').read_text())
    run(['patch','--dry-run','-R','-p1','-i',str(ROOT/'msolve-0.10.1-checked-input-allocation.patch')],src)
    run(['patch','-R','-p1','-i',str(ROOT/'msolve-0.10.1-checked-input-allocation.patch')],src)
    need(sha(src/'src/msolve/iofiles.c')=='e0107ae05994a3480ca95d0f289529b9fe4537826702458fe467b68652bae874','restored historical parser')
    p=ROOT/'msolve-0.10.1-checked-input-allocation-v2.patch'
    need(sha(p)==rec[p.name],'v2 patch hash')
    run(['patch','--dry-run','-p1','-i',str(p)],src)
    run(['patch','-p1','-i',str(p)],src)
    for n,d in rec['edited_source'].items(): need(sha(src/n)==d,'v2 source '+n)
    run(['git','diff','--check'],src)
    run(['make','-j8'],src)
    run(['make','check','-j8'],src)
    names=['.libs/msolve','msolve','src/msolve/.libs/libmsolve.so.3.0.7','src/neogb/.libs/libneogb.so.3.0.7']
    save('build-v2.json',{'commit':COMMIT,'input':rec,'binaries':{n:sha(src/n) for n in names},
         'upstream_tests':'make check -j8 exited 0'})
    print('BUILD_V2_PASS',flush=True)

def small_polynomial(text, prime):
    answer={}
    for term in re.findall(r'[+-]?[^+-]+',text.replace(' ','')):
        sign=-1 if term.startswith('-') else 1
        term=term.lstrip('+-')
        coefficient=Fraction(sign); exponent=[0,0]
        for factor in term.split('*'):
            if factor.startswith(('x','y')):
                m=re.fullmatch(r'([xy])(?:\^(\d+))?',factor)
                need(m is not None,'small polynomial variable token')
                exponent['xy'.index(m.group(1))]+=int(m.group(2) or 1)
            else:
                need(re.fullmatch(r'\d+(?:/\d+)?',factor) is not None,'small polynomial coefficient token')
                coefficient*=Fraction(factor)
        if prime: coefficient=coefficient.numerator*pow(coefficient.denominator,-1,prime)%prime
        key=tuple(exponent); answer[key]=answer.get(key,0)+coefficient
        if prime: answer[key]%=prime
    return tuple(sorted((k,str(v)) for k,v in answer.items() if v))

def tests():
    src=ROOT/'msolve-source'
    record=json.loads((ROOT/'build-v2.json').read_text())
    for n,d in record['binaries'].items(): need(sha(src/n)==d,'binary drift '+n)
    run(['cc','-std=c11','-O2','-Wall','-Wextra','-Werror','-fsanitize=undefined',
         '-fno-sanitize-recover=all','-I'+str(src/'src/msolve'),str(ROOT/'boundary-v2.c'),'-o',str(ROOT/'boundary')])
    results={}
    for mode,expected in [('positive',None),('overflow','size_t product overflow'),
       ('ptrdiff','array exceeds PTRDIFF_MAX bytes'),('exponent-overflow','size_t product overflow'),
       ('negative-dimension','nonpositive exponent dimension'),('null-malloc','allocator returned NULL'),
       ('negative-index','invalid import exponent index/dimension'),
       ('null-calloc','allocator returned NULL')]:
        p=subprocess.run([str(ROOT/'boundary'),mode],capture_output=True,text=True)
        need(p.returncode==(0 if expected is None else 1),'boundary exit '+mode)
        need('UNEXPECTED_LARGE_ALLOCATION' not in p.stderr,'large allocation attempt')
        need('runtime error' not in p.stderr,'UBSan finding')
        if expected: need(p.stderr.strip()=='msolve input size/allocation error: '+expected,'rejection text '+mode)
        else: need(p.stdout.strip()=='BOUNDARY_CONTROLS_PASS no allocation over 24 bytes','positive controls')
        results[mode]={'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    # Tiny known ideals only: this is not a complete-input parser/F4 experiment.
    controls={
      'unit':['x+y','x-y','x-1'],
      'proper':['x*y-1','y^2-x'],
      'rational':['1/2*x+1/3*y','3/4*x-1/5*y']}
    engine={}
    for prime in (0,1073741827):
        for name,rows in controls.items():
            if name=='rational' and prime: continue
            label=f'retry-{name}-p{prime}'
            inp=ROOT/(label+'.ms'); out=ROOT/(label+'.basis')
            with inp.open('x') as f: f.write('x,y\n'+str(prime)+'\n'+',\n'.join(rows)+'\n')
            argv=[str(src/'msolve'),'-g','2','-t','1','-v','2','--random-seed','0','-f',str(inp),'-o',str(out)]
            with (ROOT/(label+'.stdout')).open('x') as so,(ROOT/(label+'.stderr')).open('x') as se:
                p=subprocess.run(argv,stdout=so,stderr=se)
            need(p.returncode==0,'tiny engine exit '+label)
            data=out.read_text()
            need('#Reduced Groebner basis data' in data,'basis header '+label)
            m=re.search(r'\[([^\[\]]*)\]\s*:\s*\Z',data,re.S)
            need(m is not None,'terminal basis '+label)
            polys=[s.strip() for s in m.group(1).split(',') if s.strip()]
            expected=['1'] if name=='unit' else ['x','y'] if name=='rational' else ['y^2-x','x*y-1','x^2-y']
            need(len(polys)==len(expected) and
                 {small_polynomial(s,prime) for s in polys}=={small_polynomial(s,prime) for s in expected},
                 'small basis exact coefficient dictionary '+label)
            # Wrong constant/coefficients must not pass this semantic reader.
            need(small_polynomial('x*y-1',prime)!=small_polynomial('x*y+1',prime),'sign mutation reader control')
            engine[label]={'argv':argv,'returncode':p.returncode,'polynomials':polys,
                          'input_sha256':sha(inp),'output_sha256':sha(out)}
    save('tests-retry.json',{'boundary':results,'tiny_engine':engine,'boundary_binary_sha256':sha(ROOT/'boundary'),
                       'UBSan':True,'giant_input_or_solve':False})
    print('ALL_TINY_TESTS_PASS',flush=True)

guard()
if sys.argv[1]=='dummy': os.execv(sys.executable,[sys.executable,str(ROOT/'dummy.py')])
elif sys.argv[1]=='build': build()
elif sys.argv[1]=='upgrade': upgrade()
elif sys.argv[1] in ('tests','tests-retry'): tests()
else: raise SystemExit('unrecognized mode')
