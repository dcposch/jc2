#!/usr/bin/env python3
"""Supplementary D108 necessary chart with an arbitrary quadratic mean.

The frozen mean-zero chart is preserved separately.  No arc or coefficient
is translated here.  This adapter retains the missing mean as a new scalar
and changes each forced polynomial face by coefficient-minus-target.
"""
import argparse,hashlib,json,sys,time
from pathlib import Path
import sympy as sp
OUT=Path(__file__).resolve().parent
from char_degree_driver import E,build,exprS,rows_hash
from normalized_backend import normalized_polyS
old_incidence=E.minor_incidence
mean=sp.Symbol('minor_mean')

def meanfree_incidence(R,cutoff,jet0free):
    old,hvars,h3=old_incidence(R,cutoff,jet0free)
    rows=dict(old)
    rows['minor_n8_pi1']=sp.expand(rows.get('minor_n8_pi1',0)-2*mean)
    rows['minor_n8_pi0']=sp.expand(rows.get('minor_n8_pi0',0)+mean**2)
    result=sorted(rows.items())
    old0={name:sp.expand(value) for name,value in old if value!=0}
    new0={name:sp.expand(value.subs(mean,0)) for name,value in result if value.subs(mean,0)!=0}
    assert new0==old0
    return result,hvars,h3

def meanfree_target(name):
    pi,c=sp.symbols('pi c');power=12 if name=='F' else 8 if name=='G' else None
    if power is None:raise ValueError(name)
    poly=sp.Poly(sp.expand(((pi-mean)**2-c)**power),pi)
    return {int(mon[0]):value for mon,value in poly.terms()}

def main(stage,jet0free=True):
    E.minor_incidence=meanfree_incidence;E.leading_pole_target_table=meanfree_target
    # This is a new supplementary metadata ledger, not an edit of the frozen
    # source or campaign ledgers. The unsupported mean normalization is
    # explicitly absent from this new chart.
    E.GAUGE_LEDGER=[dict(entry) for entry in E.GAUGE_LEDGER]
    for entry in E.GAUGE_LEDGER:
        if entry['normalization'].startswith('p = pi^2'):
            entry.update({'normalization':'p = (pi-minor_mean)^2-c with minor_mean free',
              'group_element':'none used; all quadratic means retained',
              'status':'FREE; supplementary coverage repair, no arc reparametrization'})
    if not jet0free:
        for entry in E.GAUGE_LEDGER:
            if entry['normalization']=='minor constant jet0':
                entry.update({'normalization':'minor constant jet0=0 after retaining arbitrary quadratic mean',
                  'group_element':'diagonal affine translation (x,y)->(x+q,y+q), q=old jet0',
                  'status':'SPENT; independently audited mean-free slice, no even-face pin'})
    start=time.monotonic();maps,res,meta=build(stage,jet0free,normalized=True,strong_front=True)
    names=set(sp.symbols('target_a target_b target_c target_d target_e leader63 Z63 c Zc minor_mean'))
    for table in maps.values():
        for value in table.values():names|=value.free_symbols
    for _,value in res:names|=value.free_symbols
    inputs={'h_expr':normalized_polyS(maps['h2']),'D_expr':normalized_polyS(maps['B2']),'C_expr':normalized_polyS(maps['A3']),
      'residual_strings':[exprS(value) for _,value in res],'names':sorted(map(str,names)),
      'k':36,'target':63,'face_expr':'zz^21*(1+zz)^6'}
    tag=f'd108_meanfree_stage{stage}_strongfront'+('_jet0slice' if not jet0free else '');path=OUT/f'{tag}.input.json';path.write_text(json.dumps(inputs,indent=2)+'\n')
    meta.update({'tag':tag,'source_variant':'supplementary mean-free quadratic-face necessary chart',
      'mean_parameter':'minor_mean','mean_free':True,'arc_unchanged':jet0free,
      'jet0_gauge':(None if jet0free else {'type':'polynomial orbit slice after free-mean repair',
        'forward':{'jet0':'0','jet1':'jet1','jet2':'jet2-q*jet1','minor_mean':'minor_mean+q^2*jet1-2*q*jet2','c':'c'},
        'q':'old jet0','proof_control':'../../../d108-meanfree-translation-control.json',
        'source_graph_and_arc_transport_audited':True}),
      'quadratic_face':'(pi-minor_mean)^2-c','source_c_nonzero_role':'nonzero quadratic discriminant, with arbitrary mean',
      'incidence_row_changes':{'minor_n8_pi1':'old-2*minor_mean','minor_n8_pi0':'old+minor_mean^2'},
      'mean_zero_restriction_checked':True,'leading_targets_generalized':{'F':'((pi-minor_mean)^2-c)^12','G':'((pi-minor_mean)^2-c)^8'},
      'scheduled_pole_powers':list(range(1,5+stage)),'mean_leading_targets_reached_in_schedule':False,
      'computational_translation':False,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'adapter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'coefficient_field':'QQ','ring_generator_order':inputs['names'],'build_seconds':round(time.monotonic()-start,3),
      'verdict':'EMITTED_NOT_DECIDED'})
    (OUT/f'{tag}.map.json').write_text(json.dumps(meta,indent=2,default=str)+'\n')
    print(json.dumps({'tag':tag,'seconds':meta['build_seconds'],'parameters':len(names),'source_residual':len(res),'input_sha256':meta['input_sha256']}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=int,required=True,choices=range(9));ap.add_argument('--jet0-slice',action='store_true');args=ap.parse_args();main(args.stage,not args.jet0_slice)
