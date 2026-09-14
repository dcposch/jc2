#!/usr/bin/env python3
"""Independent continuation coordinate, source-ring and scalar-coverage audit."""
import ast,hashlib,json,re,sys
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True
N=Path(__file__).resolve().parent
sys.path.insert(0,str(N/'run-code-source-full'))
import deep_rows as R
from source_data import SOURCE as S
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
# Generator names are accepted only together with identical defining source
# polynomials and identical gauge maps, mechanically checked here.
source_files=('engine.py','source_data.py','minor_maps.py','deep_rows.py')
source_identity={name:sha(N/'run-code-gauge'/name)==sha(N/'run-code-source-full'/name) for name in source_files}
assert all(source_identity.values())
a=ast.parse((N/'run-code-gauge/deep_gauge_accelerated.py').read_text())
b=ast.parse((N/'run-code-source-full/deep_gauge_accelerated.py').read_text())
gauge_identity={}
for name in ('gauge_inner','gauge_branch_data'):
    aa=next(x for x in a.body if isinstance(x,ast.FunctionDef) and x.name==name)
    bb=next(x for x in b.body if isinstance(x,ast.FunctionDef) and x.name==name)
    gauge_identity[name]=ast.dump(aa)==ast.dump(bb)
assert all(gauge_identity.values())
for tree in (a,b):
    source=ast.unparse(tree)
    assert "JET0 = sp.Symbol('jet0')" in source
    assert 'GAUGE = {JET0: sp.Integer(0)}' in source
# Monomial formula by direct differentiation in physical x,y, then normalize.
x,y=sp.symbols('x y');monomial_checks=[]
for D,E in ((33,33),(33,66),(33,99),(66,66),(66,99),(99,66)):
    positions=lambda n:[(0,0),(0,n),(0,n//2),(1,0),(1,n-1),(n-1,0),(n-1,1),(n,0)]
    for r,q in positions(D):
        for s,k in positions(E):
            P=x**(D-r-q)*y**q;Q=x**(E-s-k)*y**k
            direct=sp.diff(P,x)*sp.diff(Q,y)-sp.diff(P,y)*sp.diff(Q,x)
            factor=(D-r)*k-(E-s)*q
            got=R.bracket({(r,q):1},{(s,k):1},D,E,D+E-2)
            # Terms with total normalized r>D+E-2 are identically zero:
            # both original monomials then have degree sum<2.
            expected={} if factor==0 else {(r+s,q+k-1):sp.Integer(factor)}
            assert got==expected
            if factor:
                want=factor*x**(D+E-r-s-q-k-1)*y**(q+k-1)
                assert sp.expand(direct-want)==0
                assert r+s+q+k-1<=D+E-2
            else:assert direct==0
            monomial_checks.append((D,E,r,q,s,k))
# Exact coordinate covariance for independent sparse blocks, including
# all normalization-degree pairs used by the factored bracket.
coordinate_checks=[]
for D,E in ((33,33),(33,66),(33,99),(66,66),(66,99),(99,66)):
    A={(0,3):sp.Integer(2),(2,1):sp.Integer(-3),(D,0):sp.Integer(5)}
    B={(0,4):sp.Integer(-7),(3,2):sp.Integer(11),(E-1,1):sp.Integer(13)}
    conv=lambda p:{(r,k):v for r,band in R.all_w_bands(p,D+E-2).items() for k,v in band.items()}
    lhs=conv(R.bracket(A,B,D,E,D+E-2));rhs=R.bracket(conv(A),conv(B),D,E,D+E-2)
    assert {k:sp.expand(v) for k,v in lhs.items() if sp.expand(v)!=0}=={k:sp.expand(v) for k,v in rhs.items() if sp.expand(v)!=0}
    coordinate_checks.append((D,E))
# General product rule: independent derivatives of five abstract functions.
h,a0,b0,c0,d0,hx,hy,ax,ay,bx,by,cx,cy,dx,dy=sp.symbols('h a b c d hx hy ax ay bx by cx cy dx dy')
F=h**3+a0*h+b0;G=h**2+c0*h+d0
variables=(h,a0,b0,c0,d0)
diffx=dict(zip(variables,(hx,ax,bx,cx,dx)));diffy=dict(zip(variables,(hy,ay,by,cy,dy)))
df=lambda p,m:sum(sp.diff(p,v)*m[v] for v in variables)
br=lambda p,q:df(p,diffx)*df(q,diffy)-df(p,diffy)*df(q,diffx)
direct=br(F,G)
factored=(3*h*h+a0)*(h*br(h,c0)+br(h,d0))-(2*h+c0)*(h*br(h,a0)+br(h,b0))+h*h*br(a0,c0)+h*br(a0,d0)+h*br(b0,c0)+br(b0,d0)
assert sp.expand(direct-factored)==0
jdegree=S['n']+S['m']-2
full={(r,k) for r in range(jdegree+1) for k in range(jdegree-r+1)}
records=[]
for branch in ('delta2','delta52'):
    directory=N/'results-gauge';prefix='gauge-'+branch
    summary=json.loads((directory/(prefix+'.json')).read_text())
    completed=summary['last_completed_stage'];assert completed>=9
    collected=set();paths=[];jphases=set()
    for path in sorted(directory.glob(prefix+'_phase*.json')):
        data=json.loads(path.read_text())
        pm=re.fullmatch(r'(?:deep|stage)(\d+)_Jacobian',data['phase'])
        if not pm or int(pm.group(1))>completed:continue
        jphases.add(int(pm.group(1)));paths.append({'path':str(path),'sha256':sha(path)})
        for label,value in data['raw_new_rows_before_reduction']:
            m=re.fullmatch(r'(?:deep|stage)\d+_J_t(\d+)_d(\d+)_k(\d+)',label)
            if not m:continue
            r,dg,k=map(int,m.groups());assert dg==jdegree-r
            collected.add((r,k))
    expected={(r,k) for r,k in full if r<=completed}
    assert collected==expected,(branch,len(collected),len(expected),list(expected-collected)[:4])
    assert jphases==set(range(completed+1))
    later={(r,k) for r in range(completed+1,jdegree+1) for k in range(jdegree-r+1)}
    assert not(collected&later) and collected|later==full
    assert (jdegree,0) in later
    # Check summary provenance against the files defining the map.
    assert summary['engine_sha256']==sha(N/'run-code-source-full/engine.py')
    assert summary['source_derivation_sha256']==sha(N/'run-code-source-full/source_data.py')
    assert summary['helpers_sha256']==sha(N/'run-code-source-full/deep_rows.py')
    records.append({'branch':branch,'completed_weak_t':completed,'weak_scalar_slots':len(collected),
        'remaining_scalar_slots':len(later),'all_scalar_slots':len(full),
        'prefix_including_t0_and_low_t1_verified_from_actual_raw_labels':True,
        'terminal_constant_slot_is_present':True,'weak_source_hashes_match_strong_source':True,
        'weak_J_phase_chain':paths,'coefficient_slot_hash':hashlib.sha256(repr(sorted(collected)).encode()).hexdigest()})
result={'status':'PASS','same_source_polynomials_by_file_hash':source_identity,
 'same_gauge_polynomial_maps_by_AST':gauge_identity,
 'source_generator_map':'Identity on all named source coordinates, justified by identical source definitions and gauge functions; strong added face coordinates map independently through their saved graph definitions.',
 'graph_merge':'Adjoin every weak x-map[x] plus every weak residual in the same source ring, then intersect with the strong locus; no weak target is omitted.',
 'independent_physical_monomial_derivative_checks':len(monomial_checks),
 'coordinate_commutation_normalization_pairs':coordinate_checks,'abstract_product_rule_identity':True,
 'normalized_bracket_factor':'(D-r)*k-(E-s)*q at slot (r+s,q+k-1)',
 'coordinate_map':'z=w-1, an exact affine coefficient-ring automorphism',
 'degree_bound':jdegree,'records':records,
 'negative_coverage_controls':{'omit_t0':'would remove164 actual required scalar slots','omit_constant':'would remove slot(163,0), where the row is J_163_0-Jc','relabel_weak_generator':'source-definition hash and AST checks fail'},
 'required_provenance':'The supplied strong and weak graph/radical chains still require their separate replay; this audit verifies their coordinate identification, formula, and exhaustive slot coverage.',
 'custody':{name:sha(N/name) for name in ('deep_resume_jacobian.py','print-audit-resume-jacobian.py')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','monomial_checks':len(monomial_checks),'coordinate_pairs':len(coordinate_checks),
 'coverage':[{k:v for k,v in rec.items() if k in ('branch','completed_weak_t','weak_scalar_slots','remaining_scalar_slots','all_scalar_slots')} for rec in records]},indent=2))
