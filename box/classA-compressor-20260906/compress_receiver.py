#!/usr/bin/env python3
"""Exact-Q class-A receiver compressor; all CAS/expanded files belong on a worker.

Reconstruct the frozen production program, verify its digest, and use its
literal P-first setup.  Native h-adic and ordinary xy coefficients generate
the same ideal (monic polynomial basis change).  The latter can avoid enormous
intermediate generator expressions.  Scalar-monic pivots are checked on whole
rows over Q, recursively composed, and recorded; c is protected.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def imp(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s); sys.modules[name] = m
    s.loader.exec_module(m); return m

def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True)+'\n')

def reconstruct(row, out):
    cc = imp('compress_counts', ROOT/'box/residual66-20260905/chart_counts.py')
    compiler, emitter, fix, custody = cc.production_emitter_runtime()
    rc = row['receiver_chart']; child = row['own_child']
    K,e,q,ell = rc['K'],rc['e'],rc['q'],child['ell']
    C = dict(K=K,e=e,q=q,u=0,R=0,Pi=0,d3prime=1,delta1=F(0),delta2=F(0),
             delta_s=-F(rc['d']),B=F(-1),B_safe=F(-1),B_tight=F(-1),
             lambda_P=F(0),lambda_Q=F(0),s=2,ell=ell,two_point=False,
             support_basis='proved_outer_disc_G_only_H1_H2_H3_v1')
    inv = emitter.supports(compiler,C)
    key = child['n_prime'],child['m_prime'],child['M_prime'][-1],ell
    name = cc.receiver_key_string(key)
    rr = compiler.OB.Row(key=name,label=f'residual66 dry production {name}',
                        n=key[0],m=key[1],M2=key[2],V2=0,k=ell)
    spec = compiler.build_spec(C,inv['h'],inv['alpha_pre'],inv['beta_pre'],rr,
                               'proved_G_only_class_uniform_count_only')
    spec['low_terms'],spec['high_terms'] = list(spec['high_terms']),list(spec['low_terms'])
    raw = compiler.OB.native_builder_text(spec,Path('/tmp/residual66-production-count-only-rows.tsv'))
    program,fixinfo = fix.fix_text(raw)
    expected = rc['production_emitter_dry_run']
    assert hashlib.sha256(raw.encode()).hexdigest()==expected['raw_emitted_program_sha256']
    assert hashlib.sha256(program.encode()).hexdigest()==expected['emitted_program_sha256']
    model=cc.parse_emitted_row_program(program,e=e,q=q,
                 expected_program_sha256=expected['emitted_program_sha256'])
    variables=model['parameters']
    assert variables==[str(p) for p in spec['params']]
    assert len(variables)==rc['unknowns_without_T']
    assert cc.coordinate_digest(cc.emitted_program_structural_rows(model))==rc['coefficient_coordinate_sha256']
    (out/'pinned-builder.sing').write_text(program)
    native = program.replace('/tmp/residual66-production-count-only-rows.tsv',str(out/'native.tsv'))
    (out/'native-builder.sing').write_text(native)
    ring = re.search(r'^ring R=.*;$',program,re.M).group()
    setup='\n'.join(spec['setup'])
    P='+'.join(f'({a})*h^{r}' for a,r in spec['low_terms'])
    Q='+'.join(f'({a})*h^{r}' for a,r in spec['high_terms'])
    # Arithmetic expression substitution uses the exact production pair blocks.
    expr=[]
    for a,r in spec['low_terms']:
        for b,s in spec['high_terms']:
            expr.append(f'(diff(({a}),x)*diff(({b}),y)-diff(({a}),y)*diff(({b}),x))*h^{r+s}')
            if r+s:
                expr.append(f'(({s})*({b})*(diff(({a}),x)*diff(h,y)-diff(({a}),y)*diff(h,x))+({r})*({a})*(diff(h,x)*diff(({b}),y)-diff(h,y)*diff(({b}),x)))*h^{r+s-1}')
    J='+\n'.join(expr)+f'-c*x^{ell}'
    prefix=f'''{ring}
option(redSB);
{setup}
poly JJ={J};
print("DIRECT_J_TERMS="+string(size(JJ)));
matrix CM=coef(JJ,x*y);
ideal I;
int k;
for(k=1;k<=ncols(CM);k++) {{ I[k]=CM[2,k]; }}
kill CM; kill JJ;
I=simplify(I,2);
'''
    # A direct derivative identity is checked before any pivot or section.
    check=f'''poly checkP={P}; poly checkQ={Q};
poly control=diff(checkP,x)*diff(checkQ,y)-diff(checkP,y)*diff(checkQ,x)-c*x^{ell};
if(control!=JJ){{print("COMPRESS_FAIL DIRECT_ORIENTATION_FAILED");quit;}}
print("DIRECT_ORIENTATION=PASS");
kill checkP; kill checkQ; kill control;
'''
    prefix=prefix.replace('matrix CM=coef(JJ,x*y);',check+'matrix CM=coef(JJ,x*y);')
    (out/'compress.sing').write_text(prefix+singular_compressor(out,len(variables)))
    meta=dict(row_id=row['row_id'],receiver_key=name,variables=variables,
        original_unknowns=len(variables),original_coefficient_generators=rc['coefficient_generators'],
        original_coordinate_sha256=rc['coefficient_coordinate_sha256'],
        arithmetic_auxiliary_unknowns=0,production_custody=custody,
        pinned_program_sha256=sha(out/'pinned-builder.sing'),
        native_program_sha256=sha(out/'native-builder.sing'),
        compression_program_sha256=sha(out/'compress.sing'),
        roster_row_sha256=hashlib.sha256(json.dumps(row,sort_keys=True).encode()).hexdigest())
    dump(out/'meta.json',meta)
    return meta

def singular_compressor(out, n):
    # Whole-row derivative scalar check implies row = a*v+f in characteristic 0.
    # Earlier pivot images and ALL residual rows are updated after each pivot.
    return r'''
proc termsum(ideal L) { int j; int s=0; for(j=1;j<=size(L);j++){s=s+size(L[j]);} return(s); }
proc must(int ok,string msg) { if(!ok){print("COMPRESS_FAIL "+msg);quit;} }
ideal images=maxideal(1);
intvec gone;
int np=0; int ri; int vi; int bestrow; int bestvar; int bestsize;
poly lin; poly cand; poly deriv; poly rhs; poly rowpoly;
number unit;
string stem="OUT";
write(":w "+stem+"/pivot-audit.tsv","step|row_slot|variable|unit|row_terms|rhs_terms|rhs");
print("ORDINARY_GENERATORS="+string(size(I)));
print("ORDINARY_TERMS="+string(termsum(I)));
int rounds=0;
while(1) {
  bestrow=0; bestvar=0; bestsize=2147483647;
  for(ri=1;ri<=size(I);ri++) {
    if(size(I[ri])<bestsize) {
      lin=jet(I[ri],1)-jet(I[ri],0);
      while(lin!=0) {
        cand=leadmonom(lin);
        for(vi=3;vi<nvars(basering);vi++) {
          if(cand==var(vi)) {
            deriv=diff(I[ri],var(vi));
            if(deriv!=0 && deg(deriv)==0) {
              bestrow=ri; bestvar=vi; bestsize=size(I[ri]); break;
            }
          }
        }
        if(bestrow==ri){break;}
        lin=lin-lead(lin);
      }
    }
  }
  if(bestrow==0){break;}
  rowpoly=I[bestrow]; deriv=diff(rowpoly,var(bestvar));
  must(deriv!=0 && deg(deriv)==0,"NONUNIT_OR_NONLINEAR_PIVOT");
  unit=leadcoef(deriv);
  rhs=var(bestvar)-rowpoly/unit;
  must(diff(rhs,var(bestvar))==0,"SELF_DEPENDENT_PIVOT");
  must(subst(rowpoly,var(bestvar),rhs)==0,"PIVOT_IMAGE_NOT_ZERO");
  np=np+1; gone[np]=bestvar;
  write(":a "+stem+"/pivot-audit.tsv",string(np)+"|"+string(bestrow)+"|"+string(var(bestvar))+"|"+string(unit)+"|"+string(size(rowpoly))+"|"+string(size(rhs))+"|"+string(rhs));
  images=subst(images,var(bestvar),rhs);
  I=subst(I,var(bestvar),rhs); I=simplify(I,2);
  print("PIVOT="+string(np)+" var="+string(var(bestvar))+" generators="+string(size(I))+" terms="+string(termsum(I)));
}
// Certify recursively composed images contain no eliminated variable.
for(ri=1;ri<=np;ri++) {
  must(size(simplify(diff(images,var(gone[ri])),2))==0,"IMAGE_RETAINS_ELIMINATED_VARIABLE");
  must(size(simplify(diff(I,var(gone[ri])),2))==0,"IDEAL_RETAINS_ELIMINATED_VARIABLE");
}
write(":w "+stem+"/images.tsv","variable|image");
for(ri=3;ri<=nvars(basering);ri++){write(":a "+stem+"/images.tsv",string(var(ri))+"|"+string(images[ri]));}
write(":w "+stem+"/compressed-Q.tsv","index|expr");
for(ri=1;ri<=size(I);ri++){write(":a "+stem+"/compressed-Q.tsv",string(ri)+"|"+string(I[ri]));}
print("COMPRESSED_VARIABLES="+string(nvars(basering)-2-np));
print("COMPRESSED_GENERATORS="+string(size(I)));
print("COMPRESSED_TERMS="+string(termsum(I)));
I=subst(I,c,1); I=simplify(I,2);
write(":w "+stem+"/compressed-c1.tsv","index|expr");
for(ri=1;ri<=size(I);ri++){write(":a "+stem+"/compressed-c1.tsv",string(ri)+"|"+string(I[ri]));}
print("C1_VARIABLES="+string(nvars(basering)-3-np));
print("C1_GENERATORS="+string(size(I)));
print("C1_TERMS="+string(termsum(I)));
print("COMPRESSION_COMPLETE=1");
quit;
'''.replace('OUT',str(out))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--row',required=True,help='R005 or receiver key or class ID')
    p.add_argument('--roster',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--run',action='store_true')
    p.add_argument('--engine',choices=['sparse','singular'],default='sparse')
    p.add_argument('--extractor',type=Path,default=ROOT/'box/gi-only-20260905/experiments/fast-extract/sparse_hadic_extract.py')
    p.add_argument('--native',action='store_true',help='run original 53M-term h-adic presentation')
    a=p.parse_args()
    rows=[json.loads(s) for s in a.roster.read_text().splitlines()]
    def matches(r):
        rc=r.get('receiver_chart') or {}; ch=r.get('own_child') or {}
        cid=f"C_n{ch.get('n_prime')}m{ch.get('m_prime')}_M{(ch.get('M_prime') or [None])[-1]}_ell{ch.get('ell')}_s2"
        return a.row in (r['row_id'],rc.get('receiver_key_string'),cid)
    selected=[r for r in rows if matches(r)]
    if not selected: raise SystemExit('no matching frozen receiver')
    out=a.output.resolve(); out.mkdir(parents=True,exist_ok=True)
    meta=reconstruct(selected[0],out)
    print(json.dumps({k:v for k,v in meta.items() if k not in ('variables','production_custody')}),flush=True)
    if a.run:
        if a.engine=='sparse' and not a.native:
            here=Path(__file__).resolve().parent
            commands=[
                [sys.executable,'-B',str(here/'audit_ordinary.py'),'--directory',str(out),
                 '--roster',str(a.roster.resolve()),'--extractor',str(a.extractor.resolve())],
                [sys.executable,'-B',str(here/'fast_compress.py'),'--directory',str(out),
                 '--roster',str(a.roster.resolve()),'--extractor',str(a.extractor.resolve()),
                 '--output',str(out/'semantic')]]
            for filename,command in zip(['ordinary-audit.log','semantic.log'],commands):
                with (out/filename).open('w') as log:
                    cp=subprocess.run(command,stdout=log,stderr=log,cwd=out)
                if cp.returncode: raise SystemExit(f'{filename} failed, rc={cp.returncode}')
            logtext=(out/'semantic.log').read_text()
            assert 'COMPRESSION_COMPLETE=1' in logtext and 'Traceback' not in logtext
            (out/'semantic'/'compress.log').write_text(logtext)
            subprocess.run([sys.executable,'-B',str(here/'summarize_export.py'),str(out/'semantic')],check=True)
            return
        program='native-builder.sing' if a.native else 'compress.sing'
        with (out/('native.log' if a.native else 'compress.log')).open('w') as log:
            cp=subprocess.run(['/usr/bin/time','-v','Singular','-q',str(out/program)],stdout=log,stderr=log,cwd=out)
        if cp.returncode: raise SystemExit(cp.returncode)
        logtext=(out/('native.log' if a.native else 'compress.log')).read_text()
        marker='NATIVE_DONE equations=' if a.native else 'COMPRESSION_COMPLETE=1'
        if marker not in logtext or re.search(r'^\s*\?',logtext,re.M) or 'COMPRESS_FAIL' in logtext:
            raise SystemExit('rejected Singular log: missing completion or error')

if __name__=='__main__': main()
