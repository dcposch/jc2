#!/usr/bin/env python3
"""Exact polynomial graph extension for the degree-33 auxiliary root.

The compact tower remains graph_h_expr and every coefficient of its
difference from the newly named h2 is retained. No coefficient is capped
or specialized. Candidate support is the exact support convolution,
which can include cancellations; those give zero-valued graph variables.
"""
import argparse,hashlib,json,sys
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'review'))
from active_ring_backend import from_g9966_input

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args()
    data=json.loads(a.input.read_text());args=from_g9966_input(a.input)
    def support(key):return {(r,q) for r,q,e in data['maps'][key] if sp.sympify(e)!=0}
    def product(A,B):return {(r+s,q+j) for r,q in A for s,j in B}
    h=support('h3');h2=product(h,h)
    sites=product(h2,h)|product(support('C2'),h)|support('C3')
    assert all(r+q<=33 for r,q in sites)
    z=sp.Symbol('zz')
    top=sum(sp.sympify(e)*z**q for r,q,e in data['maps']['h3'] if r==0)
    assert sp.expand(top-z**8*(1+z)**3)==0
    assert not any(r==0 for key in ('C2','C3') for r,q,e in data['maps'][key])
    lift=[(r,q,f'liftH_{r}_{q}') for r,q in sorted(sites) if r>0]
    assert not set(n for r,q,n in lift).intersection(args['names'])
    args['graph_h_expr']=args['h_expr']
    args['h_expr']='zz^24*(1+zz)^9'+''.join(f'+{n}*tt^{r}*zz^{q}' for r,q,n in lift)
    args['names']=sorted(args['names']+[n for r,q,n in lift])
    args['graph_extension']={'type':'polynomial coefficient graph; projection is an isomorphism',
       'old_ring_generators':data['full_free_coordinates'],'old_generator_map':'identity',
       'new_generators':[{ 'name':n,'image':'[t^%d z^%d](h3^3+C2*h3+C3)'%(r,q)} for r,q,n in lift],
       'all_graph_difference_coefficients_emitted':True,'candidate_support_contains_all_actual_terms':True,
       'source_input':str(a.input),'source_input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
       'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(args,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'new_graph_variables':len(lift),'all_parameters':len(args['names']),
      'input_sha256':args['graph_extension']['source_input_sha256'],
      'output_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}))

if __name__=='__main__':main()
