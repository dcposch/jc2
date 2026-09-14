"""Independent literal reconstruction. Certificate input is DATA, never source."""
import json
import re
import sys
from authority import JOB, MAX_WIRE, authorize, canonical, digest, finish, frozen, need, pairs, write

def main():
    ctx=authorize('check')
    raw=frozen(ctx['values']['--input'],ctx['authority']['input_sha256'],MAX_WIRE)
    def bad_number(value):
        raise ValueError('numeric JSON forbidden')
    data=json.loads(raw.decode('ascii'),object_pairs_hook=pairs,parse_int=bad_number,
                    parse_float=bad_number,parse_constant=bad_number)
    need(canonical(data)==raw,'noncanonical JSON or trailing bytes')
    need(type(data) is dict and set(data)=={'schema','job','status','sources','A1','A2','N'},'certificate schema')
    need(data['schema']=='f10-mixed-bezout-data/v1' and data['job']==JOB
         and data['status']=='CANDIDATE_UNCHECKED','certificate tag')
    need(data['sources']==ctx['authority']['sources'],'certificate source binding')
    sys.path.extend(ctx['authority']['library_paths'])
    import math
    import sympy as sp
    t,X,Y=sp.symbols('t X Y')
    def polynomial(rows,dx):
        need(type(rows) is list and len(rows)<=100000,'term count')
        terms={}
        previous=None
        for row in rows:
            need(type(row) is list and len(row)==3 and all(type(v) is str for v in row),'term shape')
            st,sx,rat=row
            need(len(st)<=5 and len(sx)<=2 and re.fullmatch(r'0|[1-9][0-9]*',st)
                 and re.fullmatch(r'0|[1-9][0-9]*',sx),'canonical exponents')
            powers=(int(st),int(sx))
            need(powers[0]<=16384 and powers[1]<=dx and (previous is None or previous<powers),'degree/order/duplicate')
            previous=powers
            need(len(rat)<=5000 and re.fullmatch(r'-?[1-9][0-9]*/[1-9][0-9]*',rat),'canonical nonzero rational')
            ns,ds=rat.split('/')
            n,d=int(ns),int(ds)
            need(abs(n).bit_length()<=8192 and d.bit_length()<=8192 and math.gcd(abs(n),d)==1,'rational reduction/bit cap')
            terms[powers]=sp.Rational(n,d)
        return sp.Poly.from_dict(terms,(t,X),domain=sp.QQ)
    A1,A2,N=polynomial(data['A1'],20),polynomial(data['A2'],6),polynomial(data['N'],0)
    need(not N.is_zero,'zero scalar forbidden')

    # Finite multinomial sums, not the producer's power/inverse recurrence.
    def falling(s,n):
        v=sp.Integer(1)
        for k in range(n):
            v*=s-k
        return v
    def coefficient(s,k):
        value=sp.Integer(0)
        for c in range(k//3+1):
            for b in range((k-3*c)//2+1):
                a=k-2*b-3*c
                value+=falling(s,a+b+c)*X**b*Y**c/sp.Integer(math.factorial(a)*math.factorial(b)*math.factorial(c))
        return sp.expand(value)
    def log_derivative(k):
        value=sp.Integer(0)
        for c in range(k//3+1):
            for b in range((k-3*c)//2+1):
                a=k-2*b-3*c
                n=a+b+c
                value+=sp.Rational(k*(-1)**(n-1)*math.factorial(n-1),
                                   math.factorial(a)*math.factorial(b)*math.factorial(c))*X**b*Y**c
        return value
    d6,d7=coefficient(t,6),coefficient(t,7)
    c3=t*(t-1)*(t-2)/6
    tau=2-t
    D=12*X**2-12*(1-tau)*X+(1+tau)*(2-3*tau)
    Kold=-840*X**3+840*(1-tau**2)*X**2+42*(1+tau)*(2+tau)*(4*tau-3)*X+2*(2-3*tau)*(1+tau)*(2+tau)*(3+tau)
    U,V=sp.expand(D/4),sp.expand(-Kold/840)
    need(sp.cancel(d7-(t-2)*d6-c3*(U*Y-V))==0,'independent linear elimination mismatch')
    E=sp.Poly(sp.cancel(120*(t-2)*d6/c3),Y,domain=sp.QQ[t,X])
    beta=120*tau*(1+tau-6*X)
    need(E.degree()==2 and E.nth(2)==360 and sp.expand(E.nth(1)-beta)==0,'independent quartic normalization')
    gamma=E.nth(0)
    Sold=2*Kold**2-140*tau*(1+tau-6*X)*Kold*D+245*gamma*D**2
    P0=sp.Poly(Sold/470400,t,X,domain=sp.QQ)
    K=sp.cancel(d6.subs(Y,0)/c3)
    target=3*V**2+(t-2)*((6*X+t-3)*V*U+K*U**2)
    need(P0==sp.Poly(target,t,X,domain=sp.QQ),'old/new septic scaling')
    need(P0.degree(X)==7 and sp.expand(sp.Poly(P0.as_expr(),X).LC()-9*(t-2))==0,'septic leading term')
    aa=[coefficient(2*t-1,k) for k in range(8)]
    bb=[coefficient(4-t,k) for k in range(8)]
    ll=[log_derivative(k) for k in range(1,16)]
    B=sp.Poly(sum(aa[i]*bb[j]*ll[14-i-j] for i in range(8) for j in range(8)),t,X,Y,domain=sp.QQ)
    need(all(i<=14 and 2*j+3*k<=15 and j+k<=7 for (i,j,k),c in B.terms()),'B support envelope')
    # Independent substitution via a rational expression, followed by polynomial coercion.
    F=sp.Poly(sp.cancel(U**7*B.as_expr().subs(Y,V/U)),t,X,domain=sp.QQ)
    need(F.degree(X)<=21,'F degree')
    need((A1*P0+A2*F-N).is_zero,'CHECK FAILED: full polynomial Bezout identity')

    # Exact rational-root exhaustion over Q[t]. No parameter sampling.
    nt=sp.Poly(N.as_expr(),t,domain=sp.QQ)
    content,factors=nt.factor_list()
    rebuilt=sp.Poly(content,t,domain=sp.QQ)
    exceptional=[]
    for f,m in factors:
        need(type(m) is int and m>=1 and f.degree()>=1,'factor API shape')
        rebuilt*=f**m
        # Irreducible factors of degree>1 have no rational roots.
        if f.degree()==1:
            root=-f.nth(0)/f.nth(1)
            if root==sp.Rational(5,3):
                continue
            r=sp.cancel((2-root)/(3*root-5))
            if r.q==1 and r>=2:
                exceptional.append(str(r.p))
    need(rebuilt==nt,'factor recombination')
    status='INCONCLUSIVE_ACTUAL_R_EXCEPTION' if exceptional else 'MIXED_UNIT_ALL_INTEGER_R_CHECKED'
    finish(ctx)
    # Only the independent checker can emit this final verdict; never trusted from input.
    result={'schema':'f10-mixed-checker-receipt/v1','status':status,'science_outcome':'SCALAR_ONLY',
            'artifact_sha256':digest(raw),'authority_sha256':ctx['authority_sha256'],
            'sources':ctx['authority']['sources'],'exceptional_r':exceptional,
            'identity':'A1*P0+A2*F=N','sympy_version':sp.__version__}
    outsha=write(ctx['values']['--output'],result,32768)
    write(ctx['values']['--receipt'],{'schema':'f10-mixed-checker-custody/v1','status':status,
          'checked_output_sha256':outsha,'artifact_sha256':digest(raw)},32768)
    if exceptional:
        return 2
    print('MIXED_UNIT_ALL_INTEGER_R_CHECKED')
    return 0

if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print('STOP: '+str(exc),file=sys.stderr)
        sys.exit(1)
