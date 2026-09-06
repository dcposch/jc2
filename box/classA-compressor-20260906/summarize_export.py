#!/usr/bin/env python3
"""Worker-only validation and paired primitive-Z / finite-field export.

Reads one completed Singular polynomial row at a time.  No SymPy expression
trees and no whole presentation on the host.  All monomials and variable
images are checked; modular reduction happens only after primitive-Z custody.
"""
import argparse
import hashlib
import json
import math
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

TERM=re.compile(r'[+-]?[^+-]+')
FACTOR=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
NUMBER=re.compile(r'\d+(?:/\d+)?')

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def terms(expr,indices):
    expr=expr.strip()
    if expr=='0':return
    end=0
    for m in TERM.finditer(expr):
        assert m.start()==end;end=m.end()
        t=m.group();sign=-1 if t[0]=='-' else 1
        if t[0] in '+-':t=t[1:]
        coeff=Fraction(sign);powers={}
        for factor in t.split('*'):
            if NUMBER.fullmatch(factor):coeff*=Fraction(factor)
            else:
                vm=FACTOR.fullmatch(factor)
                assert vm and vm[1] in indices,('unknown factor',factor)
                i=indices[vm[1]];powers[i]=powers.get(i,0)+int(vm[2] or 1)
        assert coeff
        yield coeff,tuple(sorted(powers.items()))
    assert end==len(expr)

def textterm(a,mon,alias):
    s=str(abs(a))
    for i,p in mon:
        s+='*'+alias[i]+(f'^{p}' if p!=1 else '')
    return ('-' if a<0 else '+')+s

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path)
    ap.add_argument('--prime',type=int,default=1073741827)
    ap.add_argument('--native',action='store_true')
    a=ap.parse_args();d=a.directory;meta=json.loads((d/'meta.json').read_text())
    log=(d/'compress.log').read_text()
    assert 'COMPRESSION_COMPLETE=1' in log
    assert 'DIRECT_ORIENTATION=PASS' in log
    assert not re.search(r'^\s*\?',log,re.M) and 'COMPRESS_FAIL' not in log
    counts={k:int(v) for k,v in re.findall(r'^(DIRECT_J_TERMS|ORDINARY_GENERATORS|ORDINARY_TERMS|COMPRESSED_VARIABLES|COMPRESSED_GENERATORS|COMPRESSED_TERMS|C1_VARIABLES|C1_GENERATORS|C1_TERMS)=(\d+)$',log,re.M)}
    assert len(counts)==9,counts
    pivots=[]
    with (d/'pivot-audit.tsv').open() as f:
        assert next(f).strip()=='step|row_slot|variable|unit|row_terms|rhs_terms|rhs'
        for l in f:
            z=l.rstrip().split('|',6)
            pivots.append(dict(step=int(z[0]),row_slot=int(z[1]),variable=z[2],
                unit=z[3],row_terms=int(z[4]),rhs_terms=int(z[5]),rhs=z[6]))
    gone={p['variable'] for p in pivots};assert len(gone)==len(pivots)
    assert len(meta['variables'])==len(set(meta['variables']))
    assert gone<=set(meta['variables']) and 'c' not in gone
    assert counts['COMPRESSED_VARIABLES']==len(meta['variables'])-len(gone)==counts['C1_VARIABLES']+1
    assert all(Fraction(p['unit']).numerator%a.prime and
               Fraction(p['unit']).denominator%a.prime for p in pivots)
    assert [p['step'] for p in pivots]==list(range(1,len(pivots)+1))
    keep=[v for v in meta['variables'] if v not in gone and v!='c']
    assert len(keep)==counts['C1_VARIABLES']
    indices={v:i for i,v in enumerate(keep)};aliases=[f'z{i+1}' for i in range(len(keep))]
    canonical=hashlib.sha256();total=0;nr=0;maxrow=0;maxdegree=0;denoms=set()
    with (d/'compressed-c1.tsv').open() as source,(d/'c1-primitive-Q.sing').open('w') as qf,(d/'c1.msolve').open('w') as mf:
        assert next(source).strip()=='index|expr'
        qf.write('ring C=0,('+','.join(aliases)+'),dp;\nideal I=\n')
        mf.write(','.join(aliases)+'\n'+str(a.prime)+'\n')
        first=True
        for line in source:
            label,expr=line.rstrip().split('|',1)
            assert int(label)==nr+1
            lcm=1
            for coeff,mon in terms(expr,indices):lcm=math.lcm(lcm,coeff.denominator)
            denoms.add(lcm);g=0
            assert lcm%a.prime, 'bad prime for rational row denominator'
            for coeff,mon in terms(expr,indices):g=math.gcd(g,abs(int(coeff*lcm)))
            assert g
            assert g%a.prime, 'bad prime for primitive content division'
            rowterms=0;firstterm=True
            if not first:qf.write(',\n');mf.write(',\n')
            first=False
            canonical.update(f'row {nr}\n'.encode())
            for coeff,mon in terms(expr,indices):
                zz=int(coeff*lcm)//g
                if firstterm:sgn=1 if zz>0 else -1
                zz*=sgn
                canonical.update((str(zz)+':'+','.join(f'{i}^{p}' for i,p in mon)+'\n').encode())
                qs=textterm(zz,mon,aliases);ff=zz%a.prime
                assert ff, 'prime divides a primitive coefficient; implement term dropping explicitly'
                ms=textterm(ff,mon,aliases)
                qf.write(qs[1:] if firstterm and qs[0]=='+' else qs)
                mf.write(ms[1:] if firstterm else ms)
                firstterm=False;rowterms+=1;maxdegree=max(maxdegree,sum(p for i,p in mon))
            total+=rowterms;maxrow=max(maxrow,rowterms);nr+=1
        qf.write(';\n');mf.write('\n')
    assert nr==counts['C1_GENERATORS'] and total==counts['C1_TERMS']
    # Full-Q TSV counts are independently read, protecting the pre-section result.
    full_indices={v:i for i,v in enumerate(meta['variables']) if v not in gone}
    qrows=qterms=0
    with (d/'compressed-Q.tsv').open() as f:
        assert next(f).strip()=='index|expr'
        for line in f:
            label,expr=line.rstrip().split('|',1)
            assert int(label)==qrows+1
            qterms+=sum(1 for _ in terms(expr,full_indices));qrows+=1
    assert qrows==counts['COMPRESSED_GENERATORS'] and qterms==counts['COMPRESSED_TERMS']
    with (d/'images.tsv').open() as f:
        assert next(f).strip()=='variable|image'
        seen=[]
        for line in f:
            variable,expr=line.rstrip().split('|',1);seen.append(variable)
            parsed=list(terms(expr,full_indices))
            if variable not in gone:
                assert parsed==[(Fraction(1),((full_indices[variable],1),))]
        assert seen==meta['variables']
    result=dict(schema='classA-compressor/v1',row_id=meta['row_id'],status='EXACT_Q_EQUIVALENT_PRESENTATION',
        counts=counts,arithmetic_auxiliary_pivots=0,constraint_scalar_monic_pivots=len(pivots),
        pivot_families=dict(Counter(p['variable'].split('_')[0] for p in pivots)),
        original_unknowns=meta['original_unknowns'],original_generators=meta['original_coefficient_generators'],
        semantic_variables_full=[v for v in meta['variables'] if v not in gone],semantic_variables_c1=keep,
        prime=a.prime,solver_order='DRL',canonical_primitive_stream_sha256=canonical.hexdigest(),
        generator_count=nr,term_count=total,largest_row_terms=maxrow,max_total_degree=maxdegree,
        row_denominator_lcms=sorted(denoms),solver_alias_map=dict(zip(keep,aliases)),
        pivot_units=dict(Counter(p['unit'] for p in pivots)),
        f4_threshold_pass=(len(keep)<=600 and total<=1000000))
    paths=['meta.json','pinned-builder.sing','compress.sing','compress.log','pivot-audit.tsv','images.tsv',
           'compressed-Q.tsv','compressed-c1.tsv','c1-primitive-Q.sing','c1.msolve']
    result['artifacts']={p:dict(sha256=sha(d/p),bytes=(d/p).stat().st_size) for p in paths}
    if a.native and (d/'native.tsv').exists():
        coords=[];nt=0;h=hashlib.sha256()
        with (d/'native.tsv').open('rb') as f:
            head=next(f);h.update(head)
            assert head==b'source_index|h_power|x_power|y_power|expr\n'
            for l in f:
                h.update(l);idx,hp,xp,yp,expr=l.decode().rstrip().split('|',4)
                assert int(idx)==len(coords)
                coords.append((int(hp),int(xp),int(yp)))
                nt+=sum(1 for _ in TERM.finditer(expr))
        result['native']=dict(rows=len(coords),terms=nt,sha256=h.hexdigest(),bytes=(d/'native.tsv').stat().st_size)
        import importlib.util
        spec=importlib.util.spec_from_file_location('cc',Path(__file__).resolve().parents[2]/'box/residual66-20260905/chart_counts.py')
        cc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cc)
        digest=cc.coordinate_digest(coords)
        assert digest==meta['original_coordinate_sha256'] and len(coords)==meta['original_coefficient_generators']
        result['native']['coordinate_sha256']=digest
    (d/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('artifacts','semantic_variables_full','semantic_variables_c1','solver_alias_map')}))

if __name__=='__main__':main()
