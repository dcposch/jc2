#!/usr/bin/env python3
"""Worker-only independently checked pivot-prefix replay and h-adic rebase.

Each flushed pivot is checked against the actual current ordinary xy
coefficient, calculated with safe nonnegative-xy truncation. Only then is
its exact substitution replayed. A completed ordinary snapshot is retained
before optional monic h-division, so a bounded rebase can fail harmlessly.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import importlib.util
import json
import re
import resource
import time
from collections import defaultdict
from pathlib import Path
from flint import fmpq

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def imp(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def parse_q(expr,indices):
    if expr.strip()=='0':return {}
    result={}
    for term in re.findall(r'[+-]?[^+-]+',expr.strip()):
        coefficient=fmpq(-1 if term.startswith('-') else 1)
        if term[0] in '+-':term=term[1:]
        mon=[]
        for factor in term.split('*'):
            if re.fullmatch(r'\d+(?:/\d+)?',factor):coefficient*=fmpq(factor)
            else:
                m=re.fullmatch(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?',factor)
                assert m and m[1] in indices,('bad factor',factor)
                mon.extend([indices[m[1]]]*int(m[2] or 1))
        key=tuple(sorted(mon));value=result.get(key,0)+coefficient
        if value:result[key]=value
        else:result.pop(key,None)
    return result

def multiply(left,right,cap=None):
    if cap is None:return SP.bp_mul(left,right)
    result={}
    for (lx,ly),lp in left.items():
        for (rx,ry),rp in right.items():
            xy=lx+rx,ly+ry
            if xy[0]>cap[0] or xy[1]>cap[1]:continue
            target=result.setdefault(xy,{})
            SP.pp_addto(target,SP.pp_mul(lp,rp))
            if not target:del result[xy]
    return result

def jacobian(left,right,cap=None):
    result=multiply(SP.bp_derivative(left,0),SP.bp_derivative(right,1),cap)
    SP.bp_addto(result,multiply(SP.bp_derivative(left,1),SP.bp_derivative(right,0),cap),-1)
    return result

def pair_levels(blocks,e,q,cap=None):
    one={(0,0):{():fmpq(1)}}
    P=[(one,e)]+[(blocks[f'AA{i}'],e-i) for i in range(1,e+1)]
    Q=[(one,q)]+[(blocks[f'BB{i}'],q-i) for i in range(2,q+1)]
    levels=defaultdict(dict);h=blocks['h']
    for left,r in P:
        for right,s in Q:
            SP.bp_addto(levels[r+s],jacobian(left,right,cap))
            if r+s:
                if s:SP.bp_addto(levels[r+s-1],multiply(right,jacobian(left,h,cap),cap),s)
                if r:SP.bp_addto(levels[r+s-1],multiply(left,jacobian(h,right,cap),cap),r)
    return levels

def coefficient_at(blocks,e,q,ci,ell,xy):
    levels=pair_levels(blocks,e,q,xy)
    one={(0,0):{():fmpq(1)}};powers={0:one}
    top=max((i for i,p in levels.items() if p),default=0)
    for i in range(1,top+1):powers[i]=multiply(powers[i-1],blocks['h'],xy)
    result={}
    for level,table in levels.items():
        if not table:continue
        for (x,y),poly in table.items():
            complement=xy[0]-x,xy[1]-y
            if complement in powers[level]:SP.pp_addto(result,SP.pp_mul(poly,powers[level][complement]))
    if xy==(ell,0):SP.pp_addto(result,{(ci,):fmpq(1)},-1)
    return result

def main():
    global SP
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory',type=Path,required=True)
    ap.add_argument('--transcript',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--roster',type=Path,required=True)
    ap.add_argument('--extractor',type=Path,required=True)
    ap.add_argument('--engine',type=Path,default=Path(__file__).with_name('fast_compress.py'))
    ap.add_argument('--pivots',type=int)
    ap.add_argument('--rebase',action='store_true')
    args=ap.parse_args();started=time.monotonic()
    E=imp('snapshot_engine',args.engine)
    assert sha(args.extractor)==E.EXTRACTOR_SHA and sha(args.roster)==E.ROSTER_SHA
    SP=imp('snapshot_sparse',args.extractor);E.SP=SP
    source=args.directory.resolve();transcript=args.transcript.resolve();out=args.output.resolve()
    out.mkdir(exist_ok=False)
    meta=json.loads((source/'meta.json').read_text())
    roster=[json.loads(l) for l in args.roster.read_text().splitlines()]
    row=next(r for r in roster if r['row_id']==meta['row_id']);rc=row['receiver_chart']
    program=(source/'pinned-builder.sing').read_text()
    assert hashlib.sha256(program.encode()).hexdigest()==rc['production_emitter_dry_run']['emitted_program_sha256']
    names=meta['variables'];indices={v:i for i,v in enumerate(names)}
    assert len(names)==len(indices)==rc['unknowns_without_T'] and names[-1]=='c'
    ring=re.search(r'^ring R=.*;$',program,re.M)[0]
    assert re.search(r'^ring R=0,\((.*?)\),',program,re.M)[1].split(',')==['y','x']+names
    setup=dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$',program,re.M))
    blocks={k:SP.parse_base_polynomial(v,indices) for k,v in setup.items()}
    for table in blocks.values():
        for poly in table.values():
            for mon in poly:poly[mon]=fmpq(poly[mon])
    K,e,q,ell,ci=rc['K'],rc['e'],rc['q'],row['own_child']['ell'],indices['c']
    source_audit=json.loads((source/'sparse-ordinary.json').read_text())
    audit_lines=(transcript/'pivot-audit.tsv').read_text().splitlines()
    xy_lines=(transcript/'pivot-coordinates.tsv').read_text().splitlines()
    assert audit_lines[0]=='step|row_slot|variable|unit|row_terms|rhs_terms|rhs'
    assert xy_lines[0]=='step|x_power|y_power|derivative_scalar_check|image_zero_check'
    n=min(len(audit_lines),len(xy_lines))-1
    if args.pivots is not None:assert 0<=args.pivots<=n;n=args.pivots
    audit_lines=audit_lines[:n+1];xy_lines=xy_lines[:n+1]
    audit_text='\n'.join(audit_lines)+'\n';xy_text='\n'.join(xy_lines)+'\n'
    (out/'pivot-audit.snapshot.tsv').write_text(audit_text)
    (out/'pivot-coordinates.snapshot.tsv').write_text(xy_text)
    # Exact control for the selective-coefficient operation, including truncation.
    tiny={'h':{(0,2):{():fmpq(1)},(1,0):{(0,):fmpq(1)}},
          'AA1':{(0,1):{(1,):fmpq(1)}},'AA2':{},'AA3':{(1,0):{(1,):fmpq(1)}},
          'BB2':{(0,1):{(0,):fmpq(1)}}}
    expected=E.regenerate(tiny,3,2,2,0)
    for xy in set(expected)|{(30,0),(0,30)}:assert coefficient_at(tiny,3,2,2,0,xy)==expected.get(xy,{})
    print('SELECTIVE_COEFFICIENT_CONTROL=PASS',flush=True)
    images=[{(i,):fmpq(1)} for i in range(len(names))];gone=set();chosen=set()
    for i,(line,xyline) in enumerate(zip(audit_lines[1:],xy_lines[1:]),1):
        fields=line.split('|',6);pos=xyline.split('|')
        assert int(fields[0])==int(pos[0])==i and pos[3:]==['PASS','PASS']
        v=indices[fields[2]];unit=fmpq(fields[3]);rhs=parse_q(fields[6],indices)
        xy=int(pos[1]),int(pos[2])
        assert v not in gone and v!=ci and unit and xy not in chosen
        assert not any((gone|{v}).intersection(mon) for mon in rhs)
        actual=coefficient_at(blocks,e,q,ci,ell,xy)
        rebuilt={(v,):unit};SP.pp_addto(rebuilt,rhs,-unit)
        assert actual==rebuilt,('transcript pivot is not current coefficient',i,xy)
        assert len(actual)==int(fields[4]) and len(rhs)==int(fields[5])
        assert E.derivative(actual,v)=={():unit} and not E.substitute(actual,v,rhs)
        blocks=E.subst_blocks(blocks,v,rhs)
        images=[E.substitute(image,v,rhs) for image in images]
        gone.add(v);chosen.add(xy)
        print(f'REPLAY_PIVOT={i} variable={names[v]} xy={xy} wall_seconds={time.monotonic()-started:.3f}',flush=True)
    assert all(not gone.intersection(mon) for image in images for mon in image)
    image_text='variable|image\n'+''.join(name+'|'+SP.pp_text(image,names)+'\n' for name,image in zip(names,images))
    common=dict(meta)
    common.update(compression_engine='independently verified exact-Q pivot-prefix replay',
        compression_driver_sha256=sha(__file__),source_engine_sha256=sha(args.engine),
        pivot_prefix_sha256=hashlib.sha256(audit_text.encode()).hexdigest(),
        pivot_coordinate_prefix_sha256=hashlib.sha256(xy_text.encode()).hexdigest(),
        fixed_point_not_claimed=True,selected_pivots=n)
    def emit(kind,rows):
        target=out/kind;target.mkdir()
        (target/'pivot-audit.tsv').write_text(audit_text)
        (target/'pivot-coordinates.tsv').write_text(xy_text)
        (target/'images.tsv').write_text(image_text)
        (target/'pinned-builder.sing').write_text(program)
        full_rows=full_terms=c1_rows=c1_terms=0
        with (target/'compressed-Q.tsv').open('w',buffering=1<<20) as qf,(target/'compressed-c1.tsv').open('w',buffering=1<<20) as cf,(target/'compress.sing').open('w',buffering=1<<20) as sf,(target/'coordinates.tsv').open('w') as coords:
            qf.write('index|expr\n');cf.write('index|expr\n');coords.write('index|coordinate\n')
            sf.write('// Final equivalent snapshot presentation; replay driver is snapshot_rebase.py.\n'+ring+'\nideal I=\n')
            for coordinate,poly in rows:
                if not poly:continue
                assert all(not gone.intersection(mon) for mon in poly)
                full_rows+=1;full_terms+=len(poly);expr=SP.pp_text(poly,names)
                qf.write(f'{full_rows}|{expr}\n');coords.write(f'{full_rows}|{coordinate}\n')
                if full_rows>1:sf.write(',\n')
                sf.write(expr)
                value=E.substitute(poly,ci,{():fmpq(1)})
                if value:
                    c1_rows+=1;c1_terms+=len(value)
                    cf.write(f'{c1_rows}|{SP.pp_text(value,names)}\n')
            if not full_rows:sf.write('0')
            sf.write(';\nquit;\n')
        counts=dict(DIRECT_J_TERMS=source_audit['terms'],ORDINARY_GENERATORS=source_audit['rows'],
            ORDINARY_TERMS=source_audit['terms'],COMPRESSED_VARIABLES=len(names)-n,
            COMPRESSED_GENERATORS=full_rows,COMPRESSED_TERMS=full_terms,
            C1_VARIABLES=len(names)-n-1,C1_GENERATORS=c1_rows,C1_TERMS=c1_terms)
        (target/'compress.log').write_text('DIRECT_ORIENTATION=PASS\nSNAPSHOT_PIVOT_MEMBERSHIP_CHECKS=PASS\n'+''.join(f'{k}={v}\n' for k,v in counts.items())+'COMPRESSION_COMPLETE=1\n')
        kindmeta=dict(common,presentation_basis=kind,compression_program_sha256=sha(target/'compress.sing'))
        (target/'meta.json').write_text(json.dumps(kindmeta,indent=2,sort_keys=True)+'\n')
        result=dict(kind=kind,pivots=n,counts=counts,wall_seconds=round(time.monotonic()-started,3),
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (target/'snapshot.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
        print(json.dumps(result),flush=True)
        return result
    ordinary=E.regenerate(blocks,e,q,ci,ell)
    assert not chosen.intersection(ordinary)
    results=[emit('ordinary',iter(sorted(ordinary.items())))]
    del ordinary
    if args.rebase:
        assert blocks['h'].get((0,K))=={():1}
        assert all(y<K for (x,y) in blocks['h'] if (x,y)!=(0,K))
        def hadic_rows():
            levels=pair_levels(blocks,e,q);level=0;last=max(levels)
            while level<=last or levels.get(level):
                before=levels.pop(level,{})
                quotient,remainder=SP.monic_y_division(before,blocks['h'],K)
                if quotient:SP.bp_addto(levels[level+1],quotient)
                if level==0:SP.pp_addto(remainder.setdefault((ell,0),{}),{(ci,):fmpq(1)},-1)
                print(f'REBASE_LEVEL={level} rows={len(remainder)} terms={SP.count_terms(remainder)}',flush=True)
                for (x,y),poly in sorted(remainder.items()):
                    if poly:yield (level,x,y),poly
                level+=1
        results.append(emit('hadic',hadic_rows()))
    (out/'snapshot-summary.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
    print('SNAPSHOT_COMPLETE=1',flush=True)

if __name__=='__main__':main()
