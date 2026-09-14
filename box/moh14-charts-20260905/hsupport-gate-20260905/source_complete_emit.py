#!/usr/bin/env python3
"""Replay the full source-support completion, retaining every raw D1 monomial.

The source map first applies (x,y)->(x,y+eta(x)), where eta is the mean
of the roots of Q. It preserves the monomial Jacobian and puts every
P/Q root at valuation >= delta_s. The resulting weighted supports G_i
are necessary. The union D1_i U G_i remains a necessary overapproximation
and contains the 76 raw D1 h coordinates missing from the old compiler.
No inner-disc centering or total-degree cap is assumed.
"""
import copy
import json
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import sprime3_compiler as S


def main():
    enum=S.enumerate_12()
    audit=[]
    for r in enum['live']:
        C=r['C']
        old={"h":copy.deepcopy(r['h']),"alpha":copy.deepcopy(r['alpha']),
             "beta":copy.deepcopy(r['beta']),"nunk":r['nunk']}
        C['support_basis']='raw_D1_union_trace_centered_outer_disc_v1'
        r['h']=S.coeff_inventory_source_complete(C,1)
        r['alpha']={i:S.coeff_inventory_source_complete(C,i) for i in r['alpha']}
        r['beta']={i:S.coeff_inventory_source_complete(C,i) for i in r['beta']}
        am,bm,gauges,notes,ga=S.apply_gauges(C['e'],C['q'],r['alpha'],r['beta'])
        assert not any(g.startswith('P -> P - alpha_') for g in gauges)
        r.update(alpha_g=am,beta_g=bm,gauges=gauges,
                 nunk=len(r['h'])+sum(map(len,am.values()))+sum(map(len,bm.values()))+1)
        stem=S.class_id_of(r['class_key'])+'_V'+'_'.join(str(r['V'][i]) for i in range(2,r['s']+1))
        audit.append(dict(stem=stem,delta_s=S.qstr(C['delta_s']),
            d=S.qstr(-C['delta_s']),raw_D1_unknowns=old['nunk'],
            source_complete_unknowns=r['nunk'],raw_h_count=len(old['h']),
            completed_h_count=len(r['h']),
            outer_h_support=S.coeff_inventory_outer_disc(C,1),
            h_added_beyond_raw=S.inventory_cokernel(r['h'],old['h']),
            alpha_added_beyond_raw={i:S.inventory_cokernel(r['alpha'][i],old['alpha'][i]) for i in r['alpha']},
            beta_added_beyond_raw={i:S.inventory_cokernel(r['beta'][i],old['beta'][i]) for i in r['beta']},
            gauges=gauges))
    out=HERE/'source-complete'
    S.emit_all(enum,output_root=out)
    (out/'support-completion.json').write_text(json.dumps(audit,indent=2,default=S.jdefault)+'\n')
    print(json.dumps([{'stem':a['stem'],'unknowns':a['source_complete_unknowns']} for a in audit],indent=2))

if __name__=='__main__':main()
