"""UNEXECUTED. One exact-Q std, conditional lift; only under registered CAPRUN."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hashlib, json, os, subprocess
from execution_gate import authorize

ARTIFACT = '168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
VARIABLES = ['u','ell','d0','d1','v0','v1','v2','k1','k2','k3','k4','omega']
IDS = ['E1/S'+str(i) for i in range(9)]+['E0/S'+str(i) for i in range(10)]+['GUARD/omega*a*b-1']
FLAGS = ['--no-rc','--no-stdlib','--no-shell','-q','-t']

def need(ok, text):
    if not ok: raise RuntimeError(text)

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def expression(wire):
    # Separate emitter implementation; no certificate arithmetic is imported.
    from fractions import Fraction
    terms=[]; previous=None
    for exps,num,den in wire:
        need(len(exps)==12 and all(type(e) is int and e>=0 for e in exps),'bad input exponent')
        need(type(num) is str and type(den) is str,'input rational not strings')
        n,d=int(num),int(den)
        need(str(n)==num and str(d)==den and n!=0 and d>0,'noncanonical input rational')
        fraction=Fraction(n,d)
        need(fraction.numerator==n and fraction.denominator==d,'unreduced input rational')
        key=tuple(exps); need(previous is None or previous<key,'input monomial order'); previous=key
        factors=['('+num+'/'+den+')']+[name+'^'+str(e) for name,e in zip(VARIABLES,exps) if e]
        terms.append('*'.join(factors))
    return '+'.join(terms) or '0'

def script(data):
    need(data['schema']=='F10-L1-EXACT/v1' and data['variables']==VARIABLES,'source schema/variables')
    need([r['id'] for r in data['rows']]==IDS,'all twenty row IDs')
    lines=['ring R=0,('+','.join(VARIABLES)+'),dp;',
           'proc emitpoly(poly f,string tag)', '{',
           'print("POLY|"+tag);',
           'while(f!=0){',
           'print("TERM|"+string(leadexp(f))+"|"+string(numerator(leadcoef(f)))+"|"+string(denominator(leadcoef(f))));',
           'f=f-lead(f);','}', 'print("ENDPOLY");','return();','}',
           'print("F10-DECISION/1");','print("ARTIFACT|'+ARTIFACT+'");',
           'print("RING|Q|dp|'+','.join(VARIABLES)+'");']
    for i,row in enumerate(data['rows']):
        lines += ['poly f'+str(i)+'='+expression(row['polynomial'])+';',
                  'emitpoly(f'+str(i)+',"ROW/'+str(i)+'");']
    lines += ['ideal I='+','.join('f'+str(i) for i in range(20))+';',
              'ideal G=std(I);','int unitflag=0;','int i;',
              'for(i=1;i<=size(G);i++){if(G[i]!=0 && deg(G[i])==0){unitflag=1;}}',
              'if(unitflag){', 'ideal target=1;','matrix U;','matrix T=lift(I,target,U,"std");',
              'if(nrows(U)!=1 || ncols(U)!=1 || nrows(T)!=20 || ncols(T)!=1){print("ERROR|lift dimensions");quit;}',
              'print("BRANCH|UNIT");','emitpoly(U[1,1],"U");',
              'for(i=1;i<=20;i++){emitpoly(T[i,1],"T/"+string(i-1));}',
              '}else{','print("BRANCH|PROPER");','int index=0;',
              'for(i=1;i<=size(G);i++){if(G[i]!=0){emitpoly(G[i]/leadcoef(G[i]),"G/"+string(index));index++;}}',
              '}', 'print("DONE");','quit;']
    return '\n'.join(lines)+'\n'

def main():
    need(len(sys.argv)==4,'engine AUTH ARTIFACT RECEIPT')
    custody=authorize(sys.argv[1],__file__,'check')
    authority=json.loads(Path(sys.argv[1]).read_text())
    root=Path.cwd(); artifact=Path(sys.argv[2]).resolve(strict=True)
    need(sha(artifact)==ARTIFACT,'frozen artifact hash')
    executable=Path(authority['engine_path']).resolve(strict=True)
    need(str(executable)==authority['engine_path'],'engine path must be canonical absolute')
    need(authority['file_sha256'].get(str(executable))==authority['engine_sha256']==sha(executable),'engine pin')
    need(type(authority['engine_version']) is str and authority['engine_version'],'root must pin installed version')
    inputfile=root/'input.sing'; stdout=root/'singular.stdout'; stderr=root/'singular.stderr'
    argv=[str(executable),*FLAGS,str(inputfile)]
    need(authority['engine_argv']==argv,'exact nested engine argv')
    data=json.loads(artifact.read_text())
    with inputfile.open('x') as f: f.write(script(data))
    ns=os.readlink('/proc/self/ns/pid'); pgid=os.getpgrp()
    with stdout.open('xb') as out, stderr.open('xb') as err:
        child=subprocess.Popen(argv,stdin=subprocess.DEVNULL,stdout=out,stderr=err,
                               cwd=root,start_new_session=False)
        stat=Path('/proc/'+str(child.pid)+'/stat').read_text()
        childns=os.readlink('/proc/'+str(child.pid)+'/ns/pid')
        raw=Path('/proc/'+str(child.pid)+'/cmdline').read_bytes().split(b'\0')
        if raw and raw[-1]==b'': raw.pop()
        need([os.fsdecode(x) for x in raw]==argv,'nested actual argv mismatch/too-fast identity unavailable')
        need(childns==ns and os.getpgid(child.pid)==pgid,'nested engine escaped namespace/PGID')
        rc=child.wait()
    need(rc==0 and sha(executable)==authority['engine_sha256'],'engine failed/changed: INCONCLUSIVE')
    result={'schema':'F10-ENGINE/1','execution':custody,'artifact_sha256':ARTIFACT,
            'engine_path':str(executable),'engine_sha256':sha(executable),
            'engine_version':authority['engine_version'],'engine_argv':argv,
            'engine_pid':child.pid,'engine_stat':stat,'pgid':pgid,'namespace':ns,
            'input_path':str(inputfile),'input_sha256':sha(inputfile),
            'stdout_path':str(stdout),'stdout_sha256':sha(stdout),
            'stderr_path':str(stderr),'stderr_sha256':sha(stderr),'returncode':rc,
            'status':'CANDIDATE-ONLY-NOT-DECISION'}
    with Path(sys.argv[3]).open('x') as f: json.dump(result,f,sort_keys=True); f.write('\n')

if __name__=='__main__': main()
