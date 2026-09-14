"""ONE prospective Q(t)[X] gcdex; never run on the coordinator."""
import sys
from authority import JOB, authorize, finish, need, write

def main():
    ctx = authorize('produce')
    sys.path.extend(ctx['authority']['library_paths'])
    import sympy as sp
    t, X, Y = sp.symbols('t X Y')
    Q = sp.Rational
    U = 3*X**2 - 3*(t-1)*X - (t-3)*(3*t-4)/4
    V = X**3+(t-3)*(t-1)*X**2+(t-3)*(t-4)*(4*t-5)*X/20+(t-3)*(t-4)*(t-5)*(3*t-4)/420
    K = X**3+Q(3,2)*(t-3)*X**2+(t-3)*(t-4)*X/4+(t-3)*(t-4)*(t-5)/120
    P0 = sp.Poly(3*V**2+(t-2)*((6*X+t-3)*V*U+K*U**2), t, X, domain=sp.QQ)
    ph = [sp.Integer(1),sp.Integer(1),X,Y]
    def trunc(s):
        a = [sp.Integer(1)]
        for k in range(1,8):
            a.append(sp.expand(sum(((s+1)*j-k)*ph[j]*a[k-j]
                                   for j in range(1,min(3,k)+1))/k))
        return a
    aa, bb = trunc(2*t-1), trunc(4-t)
    inv = [sp.Integer(1)]
    for k in range(1,15):
        inv.append(sp.expand(-sum(ph[j]*inv[k-j] for j in range(1,min(3,k)+1))))
    ell = [sp.expand(inv[k]+(2*X*inv[k-1] if k>=1 else 0)
                     +(3*Y*inv[k-2] if k>=2 else 0)) for k in range(15)]
    B = sp.Poly(sum(aa[i]*bb[j]*ell[14-i-j] for i in range(8) for j in range(8)),t,X,Y,domain=sp.QQ)
    need(all(i<=14 and 2*j+3*k<=15 and j+k<=7 for (i,j,k),c in B.terms()), 'B envelope')
    F = sp.Poly(sum(c*t**i*X**j*V**k*U**(7-k) for (i,j,k),c in B.terms()),t,X,domain=sp.QQ)
    need(P0.degree(X)==7 and F.degree(X)<=21, 'target degree')
    field = sp.QQ.frac_field(t)
    pp = sp.Poly(P0.as_expr(),X,domain=field)
    ff = sp.Poly(F.as_expr(),X,domain=field)
    a, b, g = pp.gcdex(ff)
    if g.is_zero or g.degree()!=0:
        finish(ctx)
        write(ctx['values']['--receipt'], {'schema':'f10-mixed-producer-receipt/v1',
              'status':'INCONCLUSIVE_GENERIC_GCD','science_outcome':'NONE',
              'authority_sha256':ctx['authority_sha256']},32768)
        return 2
    a, b = a.mul_ground(1/g.LC()), b.mul_ground(1/g.LC())
    need(a*pp+b*ff == sp.Poly(1,X,domain=field), 'gcdex identity')
    den = sp.Poly(1,t,domain=sp.QQ)
    for c in a.all_coeffs()+b.all_coeffs():
        n, d = sp.cancel(c).as_numer_denom()
        den = den.lcm(sp.Poly(d,t,domain=sp.QQ))
    N = sp.Poly(den.as_expr(),t,X,domain=sp.QQ)
    def clear(poly):
        return sp.Poly(sum(sp.cancel(c*den.as_expr())*X**i
                           for (i,),c in poly.terms()),t,X,domain=sp.QQ)
    A1, A2 = clear(a), clear(b)
    need(A1*P0+A2*F==N and not N.is_zero, 'cleared full identity')
    def wire(poly, dx):
        out=[]
        for (i,j),c in sorted(poly.terms()):
            if not c:
                continue
            need(i<=16384 and j<=dx, 'wire degree cap')
            n,d = int(c.p),int(c.q)
            need(abs(n).bit_length()<=8192 and d.bit_length()<=8192, 'coefficient bit cap')
            out.append([str(i),str(j),str(n)+'/'+str(d)])
        need(len(out)<=100000, 'wire term cap')
        return out
    artifact={'schema':'f10-mixed-bezout-data/v1','job':JOB,'status':'CANDIDATE_UNCHECKED',
              'sources':ctx['authority']['sources'],'A1':wire(A1,20),'A2':wire(A2,6),'N':wire(N,0)}
    finish(ctx)
    sha=write(ctx['values']['--output'],artifact)
    write(ctx['values']['--receipt'],{'schema':'f10-mixed-producer-receipt/v1',
          'status':'CANDIDATE_UNCHECKED','science_outcome':'NONE','artifact_sha256':sha,
          'authority_sha256':ctx['authority_sha256'],'sympy_version':sp.__version__},32768)
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print('STOP: '+str(exc),file=sys.stderr)
        sys.exit(1)
