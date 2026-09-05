#!/usr/bin/env python3
"""Exact receiver certificates and contravariant coefficient-map controls."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import importlib.util, sys, json, hashlib
from pathlib import Path
sys.dont_write_bytecode = True
import sympy as s
ROOT=Path(__file__).resolve().parent
FROZEN=Path('/tmp/jc2-lane.MMCkx9/inputs/guided_gb.py')
spec=importlib.util.spec_from_file_location('receiver_frozen_guided_gb',FROZEN)
gb=importlib.util.module_from_spec(spec);sys.modules[spec.name]=gb;spec.loader.exec_module(gb)
g,p=s.symbols('gamma pi')
def jac(f,h):return s.expand(s.diff(f,g)*s.diff(h,p)-s.diff(f,p)*s.diff(h,g))
def singular(f):return str(s.expand(f)).replace('**','^')
def run(name, variables, generators):
    prelude='ring r=0,('+','.join(map(str,variables))+'),dp;\n'
    names=[]
    for i,f in enumerate(generators):
        names.append('r'+str(i));prelude+='poly '+names[-1]+'='+singular(f)+';\n'
    out=gb.guided_groebner(gb.SingularSystem(name,prelude,tuple(names),variables=tuple(map(str,variables))),policy=gb.PromotionPolicy.exact_q(),config=gb.RunConfig(ROOT/name,timeout_seconds=60,total_cores=1,max_parallel_jobs=1,memory_kb=512000))
    return out.to_json()
# Full literal wedge at a finite test size. The proof in report works at every size.
pp={};qq={}
for j in range(3):
    for i in range(3*j+1):pp[i,j]=s.Symbol(f'p{i}x{j}');qq[i,j]=s.Symbol(f'q{i}x{j}')
P=sum(a*g**i*p**j for (i,j),a in pp.items());Q=sum(a*g**i*p**j for (i,j),a in qq.items())
c,z=s.symbols('c z');E=jac(P,Q)-c*g
coeff=s.Poly(E,g,p);rho=coeff.coeff_monomial(g)
assert rho==-c
assert s.expand((-z)*rho+(1-z*c))==1
rows=coeff.coeffs()
res={}
res['literal_unit']=run('literal-unit',list(pp.values())+list(qq.values())+[c,z],rows+[1-z*c])
assert res['literal_unit']['verdict']=='UNIT_IDEAL_CHAR0'
Psmall=sum(a*g**i*p**j for (i,j),a in pp.items() if j<=1)
Qsmall=sum(a*g**i*p**j for (i,j),a in qq.items() if j<=1)
smallvars=[a for (i,j),a in pp.items() if j<=1]+[a for (i,j),a in qq.items() if j<=1]+[c]
res['c_zero_control']=run('c-zero-control',smallvars,s.Poly(jac(Psmall,Qsmall)-c*g,g,p).coeffs())
assert res['c_zero_control']['verdict']=='POSDIM'
# Missing j=0 bound: monic pi-linear genuine family with J=-2 gamma.
P1=p;Q1=p+g**2
assert jac(P1,Q1)==-2*g
res['constant_row_omitted_witness']={'P':str(P1),'Q':str(Q1),'J':str(jac(P1,Q1)),'literal_bound':False}
# Positive characteristic-free literal certificate no saturation black box.
res['uniform_unit_certificate']={'rho':'[gamma^1*pi^0](J(P,Q)-c*gamma)=-c','normalizer':'h=1-z*c','identity':'1=(-z)*rho+h','all_degrees':True}
# Control: source polynomiality after recentering does not imply unshifted wedge.
y,w=s.symbols('y w');A=g+g**2
F=y**3*w-y**2-y;H=y*w-1
D=s.expand((F**2+H).subs({y:g**-1,w:A+p*g**3}, simultaneous=True))
assert D==p**2+g**2*p+g
shift=s.expand(D.subs(p,p-A*g**-3))
# Shifted support is Laurent; gamma exponent may be negative.
for term in s.Add.make_args(shift):
    powers=term.as_powers_dict();i=int(powers.get(g,0));j=int(powers.get(p,0));assert i<=3*j
res['shifted_support_control']={'source':str(F**2+H),'descendant':str(D),'shifted':str(shift),'constant_coefficient':str(D.subs(p,0))}
# Finite exact coefficient-level chain-rule pullback, with negative rows retained.
f=s.symbols('f0:6');h=s.symbols('h0:6');mons=[1,y,w,y*y,y*w,w*w]
f0=sum(a*m for a,m in zip(f,mons));h0=sum(a*m for a,m in zip(h,mons))
K=s.expand(s.diff(f0,y)*s.diff(h0,w)-s.diff(f0,w)*s.diff(h0,y)-1)
checks=[]
for u,v in [(1,3),(2,5),(2,4)]:
    # Source orientation (y,z) normalizes J=1; x,y version adds b^-1.
    aa=s.symbols('a0:'+str(v));center=sum(a*g**i for i,a in enumerate(aa))
    subst={y:g**(-u),w:center+p*g**v}
    Ft=s.expand(f0.subs(subst,simultaneous=True));Ht=s.expand(h0.subs(subst,simultaneous=True))
    def parts(expr):
        pos=0;neg=0
        for term in s.Add.make_args(expr):
            if int(term.as_powers_dict().get(g,0))<0 or int(term.as_powers_dict().get(p,0))>1:neg+=term
            else:pos+=term
        return s.expand(pos),s.expand(neg)
    Fp,Fm=parts(Ft);Hp,Hm=parts(Ht);ell=v-u-1
    chain=s.expand(jac(Ft,Ht)+u*g**ell*(K.subs(subst,simultaneous=True)+1))
    assert chain==0
    correction=s.expand(-jac(Fm,Hp)-jac(Fp,Hm)-jac(Fm,Hm))
    pull=s.expand(jac(Fp,Hp)+u*g**ell)
    rhs=s.expand(-u*g**ell*K.subs(subst,simultaneous=True)+correction)
    assert s.expand(pull-rhs)==0
    # Grouping by coefficients of excluded negative-gamma or high-pi terms gives literal cofactors.
    def laurent_coeffs(expr):
        ans={}
        for term in s.Add.make_args(s.expand(expr)):
            powers=term.as_powers_dict();i=int(powers.get(g,0));j=int(powers.get(p,0))
            ans[i,j]=s.expand(ans.get((i,j),0)+term/(g**i*p**j))
        return {key:value for key,value in ans.items() if value!=0}
    negrows=list(laurent_coeffs(Fm).values())+list(laurent_coeffs(Hm).values())
    # All terms in the correction have an excluded-row factor.
    checks.append({'u':u,'v':v,'ell':ell,'source_monomials':list(map(str,mons)),'excluded_negative_or_high_pi_row_count':len(negrows),'receiver_pi_cap':1,'receiver_row_count':len(laurent_coeffs(pull)),'chain_zero':True,'pullback_difference_zero':True,'F_retained':str(Fp),'F_excluded':str(Fm),'G_retained':str(Hp),'G_excluded':str(Hm),'K':str(K),'correction':str(correction),'jacobian_rows':{str(k):str(vv) for k,vv in laurent_coeffs(pull).items()}})
res['pullback_controls']=checks
# Incorrect projection without negative-row equations fails even for source (y,z).
Ft=g**-1;Ht=g+g**2+p*g**3
assert jac(Ft,Ht)==-g
assert jac(0,Ht)==0
res['omitted_negative_rows_control']={'source_J':'1','full_J':str(jac(Ft,Ht)),'positive_part_J':'0','required_J':'-gamma','rejected':True}
assert jac(g**-1,-c*g**3*p)==c*g
res['laurent_wedge_witness']={'P':'gamma^(-1)','Q':'-c*gamma^3*pi','Jacobian':'c*gamma'}
res['versions']={'sympy':s.__version__,'frozen_guided_gb_sha256':hashlib.sha256(FROZEN.read_bytes()).hexdigest()}
(ROOT/'receiver-exact-results.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps({'literal_unit':res['literal_unit']['verdict'],'c_zero_control':res['c_zero_control']['verdict'],'uniform_certificate':'PASS','shifted_support':'PASS','coefficient_pullbacks':[(x['u'],x['v'],x['pullback_difference_zero']) for x in checks],'negative_controls':'PASS'}))
