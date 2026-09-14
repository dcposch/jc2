#!/usr/bin/env python3
"""Exact replay of GGHV v1 (5.9)/Prop5.4 only; no Groebner solve."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import resource
import time
import sympy as S
from collections import defaultdict

root=Path(__file__).resolve().parent
repo=root.parents[1]
started=time.monotonic()
a,b,c,u,v,w,z,t,k,l,m,T,y,x,q=S.symbols('a b c u v w z t k l m T y x q')
variables=(a,b,c,u,v,w,z,t,k,l,m,T)
namespace={str(n):n for n in variables+(y,x,q)}
def req(ok,why):
    if not ok:raise ValueError(why)
def zero(p):return S.expand(p)==0
def parse(s):return S.sympify(s,locals=namespace)
def conv(A,B):
    out=defaultdict(lambda:S.Integer(0))
    for i,xv in A.items():
        for j,yv in B.items():out[i+j]+=xv*yv
    return {i:S.expand(vv) for i,vv in out.items()}

def manual_equations():
    return [2*b*c+2*a*u+2*w,
      c**2+2*b*u+2*a*v+2*z,
      2*c*u+2*b*v+2*a*w+2*t,
      u**2+2*c*v+2*b*w+2*a*z+2*k,
      2*u*v+2*c*w+2*b*z+2*a*t+2*l,
      2*m+2*v*w+2*u*z+2*c*t+2*b*k+2*a*l,
      3*b**2*c+3*a*c**2+6*b*a*u+3*u**2+3*a**2*v+6*c*v+6*b*w+6*a*z+3*k,
      3*b*c**2+3*b**2*u+6*a*c*u+6*b*a*v+6*u*v+3*a**2*w+6*c*w+6*b*z+6*a*t+3*l,
      3*m+3*c**2*u+3*b*u**2+6*b*c*v+6*a*u*v+3*b**2*w+6*a*c*w+6*v*w+6*b*a*z+6*u*z+3*a**2*t+6*c*t+6*b*k+6*a*l+T]

def expanded_equations():
    D={3:S.Integer(1),1:a,0:b,-1:c,-2:u,-3:v,-4:w,-5:z,-6:t,-7:k,-8:l,-10:m}
    D2=conv(D,D);D3=conv(D2,D)
    return [D2[-i] for i in (1,2,3,4,5,7)]+[D3[-1],D3[-2],D3[-4]+T]

def build():
    equations=manual_equations()
    triangular=[]
    def normal_form(f):
        coefs=[S.Integer(0)]*6
        for var,value,old_coefs in triangular:
            new=S.expand(f.subs(var,value))
            quotient,remainder=S.div(S.expand(f-new),var-value,var)
            req(zero(remainder),'nonexact monic division')
            for j,coef in enumerate(old_coefs):coefs[j]=S.expand(coefs[j]+quotient*coef)
            f=new
        return f,coefs
    for i,var in enumerate((w,z,t,k,l,m)):
        reduced,coefs=normal_form(equations[i])
        req(S.expand(reduced).coeff(var)==2,'nonconstant pivot')
        value=S.expand(-(reduced-2*var)/2)
        coefs=[-r/2 for r in coefs];coefs[i]+=S.Rational(1,2)
        triangular.append((var,value,coefs))
    reductions=[normal_form(e) for e in equations[6:]]
    A=a*c**2+2*c*v+u**2
    B=-b*c**2+2*u*v
    C=2*T-6*a*u*v-6*b*c*v-3*b*u**2-3*c**2*u
    req(all(zero(r[0]-s) for r,s in zip(reductions,(3*A/2,3*B/2,C/2))),'reduction mismatch')
    V=4*T**2+6*T*c**2*u+9*c**4*u**2+9*a*c**6
    ca=27*c**6*u+3*b*V
    cb=-27*c**7+3*a*V
    cc=V
    target=8*T**3+18*a*c**6*T+27*b*c**9
    M=[S.expand(2*ca/3),S.expand(2*cb/3),S.expand(2*cc)]
    coefs=[S.Integer(0)]*9
    for j,(mult,(red,old)) in enumerate(zip(M,reductions)):
        coefs[6+j]=mult
        for i in range(6):coefs[i]=S.expand(coefs[i]-mult*old[i])
    g=-(35-42*y+54*y**2-81*y**3+243*y**4)/S.Integer(910)
    f1=S.expand(y**9*(y+1)**2*g)
    f=S.expand(y*(y+1)*g)
    gp=S.diff(g,y)
    bezg,bezgp,gcd=S.gcdex(g,gp,y)
    req(gcd==1,'quartic nontrivial gcd')
    # All certificate data are literal rational polynomials, not computed-at-points claims.
    return {'schema':'GGHV_SECTION5_EXACT/v1','field':'Q and any characteristic-zero field extension',
       'pdf_sha256':'ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd',
       'text_sha256':'f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368',
       'variables':[str(vv) for vv in variables],'T_meaning':'C3^23*F_-4',
       'equations':[str(e) for e in equations],
       'constant_pivot_reconstruction':[{'variable':str(var),'value':str(value),'multipliers_in_first_six_equations':[str(ccc) for ccc in coeff]} for var,value,coeff in triangular],
       'reduced_Q':[str(rr[0]) for rr in reductions],
       'ABC':[str(A),str(B),str(C)],'V':str(V),'ABC_multipliers':[str(ca),str(cb),str(cc)],
       'eliminant':str(target),'full_nine_equation_multipliers':[str(c_) for c_ in coefs],
       'C3':str(y**8*(y+1)),'f1':str(f1),'g':str(g),'f':str(f),
       'quartic_bezout':[str(bezg),str(bezgp)],
       'no_parameter_division':True,'localizers':[],
       'scope':'finite nine-equation consequence and scalar differential identity only; not full reduction-chain or JC2 validation'}

def verify(packet):
    generated=expanded_equations()
    eq=[parse(e) for e in packet['equations']]
    req(len(eq)==9,'equation census')
    req(all(zero(e-g) for e,g in zip(eq,generated)),'nine equations differ from independent Laurent multiplication')
    for row in packet['constant_pivot_reconstruction']:
        var=parse(row['variable']);value=parse(row['value'])
        coeff=[parse(e) for e in row['multipliers_in_first_six_equations']]
        req(zero(var-value-sum(ccc*e for ccc,e in zip(coeff,eq[:6]))),'constant-pivot ideal identity mismatch')
    coeff=[parse(e) for e in packet['full_nine_equation_multipliers']]
    E=parse(packet['eliminant'])
    req(len(coeff)==9 and zero(E-sum(ccc*e for ccc,e in zip(coeff,eq))),'full nine-generator eliminant identity mismatch')
    req(zero(E-(8*T**3+18*a*c**6*T+27*b*c**9)),'displayed eliminant transcription mismatch')
    A,B,C=map(parse,packet['ABC']);ca,cb,cc=map(parse,packet['ABC_multipliers'])
    req(zero(E-ca*A-cb*B-cc*C),'short multiplication identity mismatch')
    f1,g,f,C3=[parse(packet[key]) for key in ('f1','g','f','C3')]
    req(zero(C3-y**8*(y+1)),'C3 mismatch')
    req(zero(6*y*(y+1)*S.diff(f1,y)-10*(9*y+8)*f1-y**9*(y+1)**2),'f1 differential identity mismatch')
    req(zero(6*C3*S.diff(f1,y)-10*S.diff(C3,y)*f1-C3**2),'un-cancelled differential identity mismatch')
    req(zero(f1-C3*f) and zero(f-y*(y+1)*g),'f1/f/g factor identity mismatch')
    req(S.degree(g,y)==4 and S.degree(f,y)==6,'scalar degree mismatch')
    req(g.subs(y,0)!=0 and g.subs(y,-1)!=0,'quartic endpoint factor mismatch')
    U,V=map(parse,packet['quartic_bezout'])
    req(zero(U*g+V*S.diff(g,y)-1),'quartic squarefreeness Bezout mismatch')
    req(S.gcd(f,S.diff(f,y))==1,'f squarefreeness mismatch')
    # Check nearby typography with the actual leading cubic, not a verbal assertion.
    leading=x**3+q*x**2
    req(S.expand(leading.subs(x,x-q)).coeff(x,2)==-2*q,'printed shift control mismatch')
    req(S.expand(leading.subs(x,x-q/3)).coeff(x,2)==0,'corrected shift control mismatch')
    return {'all_nine_coefficient_rows':True,'full_nine_generator_polynomial_identity':True,
      'constant_pivots_only':True,'parameter_saturation_used':False,
      'f1_ODE_and_uncancelled_identity':True,'quartic_gcd_bezout':True,
      'g_at_0':str(g.subs(y,0)),'g_at_minus1':str(g.subs(y,-1)),
      'f_squarefree_degree':6,'f1_degree':int(S.degree(f1,y)),
      'quartic_discriminant':str(S.discriminant(g,y)),
      'full_identity_multiplier_terms':[len(S.Poly(ccc,*variables).terms()) for ccc in coeff],
      'printed_shift_x_squared_coefficient':'-2*q','corrected_shift_x_squared_coefficient':'0'}

def negative_controls(packet):
    controls=[]
    def reject(label,fn):
        bad=copy.deepcopy(packet);fn(bad)
        try:verify(bad)
        except ValueError as e:controls.append({'mutation':label,'status':'REJECTED_BY_ACTUAL_CHECKER','reason':str(e)})
        else:raise ValueError('mutation escaped:'+label)
    reject('remove 2*d_-10 from sixth equation',lambda p:p['equations'].__setitem__(5,str(parse(p['equations'][5])-2*m)))
    reject('change eliminant 18 to -18',lambda p:p.__setitem__('eliminant',str(parse(p['eliminant'])-36*a*c**6*T)))
    reject('perturb ideal multiplier',lambda p:p['full_nine_equation_multipliers'].__setitem__(0,str(parse(p['full_nine_equation_multipliers'][0])+1)))
    reject('f1 scalar -1/910 to -1/911',lambda p:p.__setitem__('f1',str(parse(p['f1'])*S.Rational(910,911))))
    reject('reverse quartic Bezout sign',lambda p:p['quartic_bezout'].__setitem__(0,str(-parse(p['quartic_bezout'][0]))))
    return controls

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    for ext,expected in [('pdf','ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd'),('txt','f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368')]:
        p=repo/('box/ideation-20260906T1210Z/ggvh-2204.14178v1.'+ext)
        req(hashlib.sha256(p.read_bytes()).hexdigest()==expected,'primary source hash mismatch')
    packet=json.loads(args.verify.read_text()) if args.verify else build()
    result=verify(packet)
    result['negative_controls']=negative_controls(packet)
    result['status']='EXACT_PASS_FINITE_INSTRUMENT_ONLY'
    result['sympy_version']=S.__version__
    result['seconds']=time.monotonic()-started
    result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    raw=(json.dumps(packet,sort_keys=True,indent=2)+'\n').encode()
    result['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    if not args.verify:
        req(not (root/'certificate.json').exists(),'no overwrite')
        (root/'certificate.json').write_bytes(raw)
        (root/'summary.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
