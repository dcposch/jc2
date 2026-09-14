"""STATIC corrected direct residue circuit; ROWS ONLY; not a baseline."""
from authority import authorize


def build(meta):
    import arithmetic as m
    from arithmetic import (Q, qa, qs, qm, field, const, var, add, sub, neg, mul,
                            scale, power, diff, coeff, shift, series, integrate,
                            scalar, equal, wire_p, wire_f)
    m.WIRE_TERMS = 0
    tau = Q(3, 10)
    dl = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    kl = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
          42 * (1 + tau) * (2 + tau) * (4 * tau - 3),
          840 * (1 - tau * tau), Q(-840)]
    ga = [tau * (1 + tau) * (2 + tau) * (3 + tau),
          -30 * tau * (1 + tau) * (2 + tau), 180 * tau * (1 + tau), -120 * tau]
    septic = qa(qa(qs(qm(kl, kl), Q(2)),
                    qs(qm(qm([1 + tau, Q(-6)], kl), dl), -140 * tau)),
                qs(qm(ga, qm(dl, dl)), Q(245)))
    lead = -245 * 120 * 144 * tau
    equal(len(septic), 8, 'septic degree')
    equal(septic[-1], lead, 'literal septic leading coefficient')
    monic = qs(septic, 1 / lead)
    m.initialize(meta['place'], monic)
    registry = [('D0:tau',10),('D0:W',210),('D0:lead',lead)]
    registry += [('D0:series:'+str(j),j) for j in range(1,8)]
    registry += [('D0:integral:'+str(j),j) for j in range(1,9)]
    for h in (5,6):
        registry += [('D0:ratio-den:'+str(h),27-h),('D0:ratio-num:'+str(h),3*(h-3)-2)]
    registry += [('D0:half',2),('D0:ell21',21),('D0:ell11',11)]
    registry += [('D1:'+str(h)+':'+str(j),10*j-3*(17-h))
                 for h in range(1,11) for j in range(5 if h<=6 else 3)]
    registry += [('D2:'+str(j)+':'+str(i),j-3*i) for j in range(5)
                 for i in range(18-3*j) if (j,i) not in ((0,0),(3,1))]
    for label,value in registry:m.denominator(label,value)
    diagnostics={}; required=set()
    def record(label,poly,zero=False):
        if label in diagnostics:raise ValueError('diagnostic label reuse')
        diagnostics[label]=m.bounded(m.Poly(m.kindof(poly),poly))
        if zero:required.add(label)

    dL, KL, gamma = field(dl), field(kl), field(ga)
    W = m.fm(field(Q(-1, 210)), m.fm(KL, m.fi(dL, 'dL')))
    Wi = m.fi(W, 'W')
    T, z = var(6), var(4)
    c = add(const(1), T, scale(power(T, 2), field([0, 1])), scale(power(T, 3), W))
    ts = series(c, Q(17, 10), 7)
    t5 = scalar(coeff(ts, 6, 5))
    t5i = m.fi(t5, 't5')
    middle, middle_i = {}, {}
    for h in (5, 6):
        middle[h] = scalar(coeff(series(c, Q(27 - h, 10), 7), 6, 7))
        middle_i[h] = m.fi(middle[h], 'H7_' + str(h))
    C, D = scale(c, Wi), scale(m.truncate(ts, 6, 5), t5i)
    equal(add(scale(mul(C, diff(D, 6)), 10), scale(mul(diff(C, 6), D), -17)),
          neg(power(T, 7)), 'leading ODE')
    equal(coeff(ts, 6, 6), {}, 'leading contact6')
    equal(coeff(ts, 6, 7), {}, 'leading contact7')
    a, F, H = [scalar(coeff(C, 6, j)) for j in (0, 2, 1)]
    b = scalar(coeff(D, 6, 0))

    def op(h, A, B):
        return add(scale(mul(C, diff(B, 6)), 10),
                   scale(mul(diff(C, 6), B), -(17 - h)),
                   scale(mul(A, diff(D, 6)), 10 - h),
                   scale(mul(diff(A, 6), D), -17))

    def upper(h, A, target, degree, fixed=None):
        V = {} if fixed is None else fixed
        for j in range(degree, -1, -1):
            residual = sub(op(h, A, V), target)
            pivot = 10 * j - 3 * (17 - h)
            if not pivot:
                raise ValueError('unlicensed band resonance')
            V = add(V, shift(scale(coeff(residual, 6, j + 2), Q(-1, pivot)), 6, j))
        residual = sub(op(h, A, V), target)
        defect=m.Poly('band',{e:c for e,c in residual.items() if e[6]>=2})
        return V, [coeff(residual, 6, 1), coeff(residual, 6, 0)], defect

    Ab, Bb, packets, psis, witnesses = [C], [D], [], [], []
    Uglobal = {}
    selections=[]
    column_residuals=[]
    for h in range(1, 11):
        forcing = {}
        for i in range(1, h):
            forcing = add(forcing,
                          scale(mul(Ab[i], diff(Bb[h - i], 6)), 10 - i),
                          scale(mul(diff(Ab[i], 6), Bb[h - i]), -(17 - h + i)))
        if h <= 6:
            part, base, defect = upper(h, {}, neg(forcing), 4)
            record('upper:'+str(h)+':part',defect,True)
            basisV, columns = [], []
            for j in range(3):
                Aj = power(T, j)
                target = scale(power(T, 6), -2) if h == 4 and j == 2 else {}
                Vj, rj, defect = upper(h, Aj, target, 4)
                record('upper:'+str(h)+':basis:'+str(j),defect,True)
                rhoj = sub(scale(coeff(Vj, 6, 0), m.fm(field(10), a)),
                           scale(coeff(Aj, 6, 0), m.fm(field(17), b)))
                basisV.append(Vj)
                columns.append([scalar(rj[0]), scalar(rj[1]), scalar(rhoj)])
            matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
            inverse = m.invert_matrix(matrix, 'det' + str(h))
            rho = var(h - 1) if h <= 4 else {}
            xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            if h in (5, 6):
                ratio = Q(3 * (h - 3) - 2, 27 - h)
                equal(inverse[2][2], m.fm(field(ratio), middle[h]), 'middle H7/Phi coefficient')
                rho = scale(xyz[2], m.fm(field(-1 / ratio), middle_i[h]))
                xyz = m.apply_matrix(inverse, [neg(base[0]), neg(base[1]), rho])
            A = add(*(shift(xyz[j], 6, j) for j in range(3)))
            V = add(part, *(mul(xyz[j], basisV[j]) for j in range(3)))
            target = scale(mul(xyz[2], power(T, 6)), -2) if h == 4 else {}
            record('early:'+str(h)+':residual',add(op(h,A,V),forcing,neg(target)),True)
            record('early:'+str(h)+':rho',sub(sub(scale(coeff(sub(V,part),6,0),m.fm(field(10),a)),
                     scale(coeff(A,6,0),m.fm(field(17),b))),rho),True)
            if h in (5, 6):
                record('middle:'+str(h)+':U2',xyz[2],True)
                record('middle:'+str(h)+':V4',coeff(V,6,4),True)
            if h == 4:
                Uglobal = neg(xyz[2])
            packets.append({'gap':h,'forcing':forcing,'part':part,'basisV':basisV,
                'matrix':matrix,'inverse':inverse,'rho':rho,'A':A,'B':V})
        else:
            if h == 7:
                d0 = coeff(Ab[3], 6, 2)
                Apart = mul(sub(z, mul(Uglobal, d0)), T)
                target = scale(mul(z, power(T, 5)), -2)
                fixed, Avar, targetvar = {}, const(1), {}
            elif h == 8:
                Apart = {}
                target = neg(mul(power(Uglobal, 2), power(T, 5)))
                fixed = mul(power(Uglobal, 2), power(T, 3))
                Avar, targetvar = const(1), {}
            elif h == 9:
                Apart, target, fixed = {}, {}, {}
                Avar, targetvar = const(1), {}
            else:
                Apart, target, fixed = {}, {}, {}
                Avar, targetvar = {}, neg(power(T, 4))
            Vpart, base, defect = upper(h,Apart,sub(target,forcing),2,fixed)
            record('upper:'+str(h)+':part',defect,h==7)
            Vvar, col, defect = upper(h,Avar,targetvar,2)
            record('upper:'+str(h)+':variation',defect,h==7)
            c1, c0 = scalar(col[0]), scalar(col[1])
            if h == 7:
                invC2 = scale(series(c, Q(-2), 6), m.fm(W, W))
                lams = []
                for R in (T, const(1)):
                    P = mul(power(C, 2), integrate(mul(R, invC2)))
                    lams.append(scalar(sub(scale(coeff(P, 6, 6), F),
                                           scale(coeff(P, 6, 5), Q(1, 2)))))
                l1, l0 = lams
            else:
                if any(c1):l1,l0=m.fi(c1,'pivot'+str(h)),field(0)
                elif any(c0):l1,l0=field(0),m.fi(c0,'pivot'+str(h))
                else:raise ValueError('STOP_BAD_COLUMN_PLACE')
                selections.append((h,1 if any(c1) else 0))
            equal(m.fa(m.fm(l1, c1), m.fm(l0, c0)), field(1), 'determinant-one column')
            value = neg(add(scale(base[0], l1), scale(base[1], l0)))
            psi = sub(scale(base[1], c1), scale(base[0], c0))
            A, V = add(Apart, mul(value, Avar)), add(Vpart, mul(value, Vvar))
            residual = sub(add(op(h, A, V), forcing), add(target, mul(value, targetvar)))
            equal(coeff(residual,6,1),scale(psi,m.fn(l0)),'column low1')
            equal(coeff(residual,6,0),scale(psi,l1),'column low0')
            column_residuals.append((residual,m.Poly('band',{e:c for e,c in residual.items() if e[6]>=2})))
            psis.append(psi)
            witnesses.append((l1, l0))
            if h == 10:
                Eglobal = value
                ge = m.fm(field(Q(1, 21)), m.fa(m.fm(field(13), H),
                         m.fn(m.fm(field(Q(24, 11)), m.fm(F, F)))))
                equal(Vvar, add(power(T, 2), scale(T, m.fm(field(Q(6, 11)), F)), const(ge)),
                      'r3 ell literal column')
            packets.append({'gap':h,'forcing':forcing,'part':Vpart,'A_part':Apart,'fixed':fixed,
                'target':target,'A_var':Avar,'target_var':targetvar,'B_var':Vvar,
                'column':(c1,c0),'lambda':(l1,l0),'base':base,'value':value,'Psi':psi,'A':A,'B':V})
        Ab.append(A)
        Bb.append(V)

    # Installation is fixed by (h,j), not by observing a residue coefficient.
    Ahat=m.Poly('raw')
    for h in range(11):
        allowed=3 if h==0 else (2 if h<=6 else (1 if h==7 else (0 if h<=9 else -1)))
        if any(e[5] or e[6]>allowed for e in Ab[h]):
            raise ValueError('fixed A-band type/gauge')
        for j in range(allowed+1):
            value=coeff(Ab[h],6,j)
            exponent=10-h-3*j
            if exponent<0:
                if (h,j) not in ((5,2),(6,2)):raise ValueError('installation index')
                record('install:'+str(h)+':'+str(j),value,True)
            else:
                Ahat=add(Ahat,shift(shift(m.retype(value,'raw'),5,exponent),6,j))
    U=m.retype(Uglobal,'raw');E=m.retype(Eglobal,'raw')
    Tr,Sr,zr=var(6,'raw'),var(5,'raw'),var(4,'raw')
    aa=[coeff(Ahat,6,j) for j in range(4)]
    Dformal=shift(m.retype(add(aa[2],U),'laurent_S'),5,-1)
    Vformal=shift(add(m.retype(sub(aa[1],zr),'laurent_S'),
                       mul(m.retype(U,'laurent_S'),Dformal)),5,-1)
    Kpar=aa[0]
    record('auxiliary.Dnegative',m.Poly('laurent_S',{e:c for e,c in Dformal.items() if e[5]<0}),True)
    record('auxiliary.Vnegative',m.Poly('laurent_S',{e:c for e,c in Vformal.items() if e[5]<0}),True)
    Pi=add(mul(zr,Tr),neg(mul(U,power(Tr,2))),mul(Sr,power(Tr,3)))
    Delta=neg(add(mul(mul(E,Tr),Pi),mul(Tr,power(Pi,2))))
    bb=[m.Poly('raw') for _ in range(9)]
    bb[5]=power(Sr,2)
    resonances={}
    for j in range(4,-1,-1):
        q=add(coeff(Delta,6,j+2),
              scale(mul(diff(aa[2],5),bb[j+1]),-(j+1)),
              scale(mul(aa[2],diff(bb[j+1],5)),2),
              scale(mul(diff(aa[1],5),bb[j+2]),-(j+2)),
              mul(aa[1],diff(bb[j+2],5)),
              scale(mul(diff(aa[0],5),bb[j+3]),-(j+3)))
        if any(e[6] or e[5]>17-3*j for e in q):raise ValueError('Euler full support')
        for i in range(18-3*j):
            value=coeff(q,5,i)
            if (j,i) in ((0,0),(3,1)):
                resonances[(j,i)]=value
            else:
                bb[j]=add(bb[j],shift(scale(value,Q(1,j-3*i)),5,i))
    for j,i in ((0,0),(3,1)):
        record('Euler-resonance:'+str(j)+':'+str(i),resonances[(j,i)])
    Bhat=add(*(shift(bb[j],6,j) for j in range(6)))
    for h in range(11):
        band=m.Poly('band')
        for e,c0 in Bhat.items():
            if e[5]+3*e[6]==17-h:
                ex=list(e);ex[5]=0;band[tuple(ex)]=c0
        record('Euler-band:'+str(h),sub(band,Bb[h]),h<=7)
    J=sub(mul(diff(Ahat,5),diff(Bhat,6)),mul(diff(Ahat,6),diff(Bhat,5)))
    residual=sub(J,Delta)

    def envelope(poly,weight,theta_weight=3):
        ww=(1,2,3,4,7,1,theta_weight)
        if any(sum(x*y for x,y in zip(e,ww))!=weight for e in poly):
            raise ValueError('exact homogeneous envelope')
    for obj,w in ((Ahat,10),(Bhat,17),(Dformal,3),(Vformal,6),(Kpar,10),
                  (U,4),(E,10),(Pi,10),(residual,23)):
        envelope(obj,w)
    if any(e[6]>7 or e[5]>23-3*e[6] for e in residual):
        raise ValueError('complete Jacobian envelope')
    jacobian=[]
    for j in range(8):
        for i in range(24-3*j):
            value=coeff(coeff(residual,6,j),5,i)
            jacobian.append(value)
            if j>=2:record('upper-J:'+str(j)+':'+str(i),value,23-i-3*j<=7)
    equal(len(jacobian),108,'108 positions')
    P1=[coeff(coeff(residual,6,1),5,i) for i in range(21)]
    P0=[coeff(coeff(residual,6,0),5,i) for i in range(24)]
    for h in range(11):
        for j,top,rows in ((1,20,P1),(0,23,P0)):
            expected={} if h<7 else scale(psis[h-7],m.fn(witnesses[h-7][1]) if j else witnesses[h-7][0])
            record('low-band:'+str(h)+':'+str(j),sub(m.retype(rows[top-h],'band'),expected),h<=7)
    for h,poly in zip(range(7,11),psis):envelope(poly,h)
    # Formal bands remain separate from the installed/Euler sequence throughout.
    for h in range(1,11):
        envelope(Ab[h],h,0)
        envelope(Bb[h],h,0)

    Pin,qin=var(5,'inverse'),var(6,'inverse')
    chartS=add(mul(Pin,power(qin,3)),neg(mul(m.retype(zr,'inverse'),power(qin,2))),
               mul(m.retype(U,'inverse'),qin))
    inverses=[];poles=[]
    for obj,low,high in ((Ahat,-3,30),(Bhat,-5,51)):
        transformed=m.Poly('inverse')
        for ex,cc in obj.items():
            e=list(ex);e[5]=e[6]=0
            term=mul(m.Poly('inverse',{tuple(e):cc}),power(chartS,ex[5]))
            transformed=add(transformed,shift(term,6,-ex[6]))
        if any(e[6]<low or e[6]>high for e in transformed):raise ValueError('inverse chart bound')
        inverses.append(transformed)
        poles.append(m.Poly('inverse',{e:c0 for e,c0 in transformed.items() if e[6]<0}))
    equal(scalar(coeff(coeff(Ahat,6,0),5,10)),Wi,'leading a')
    equal(scalar(coeff(coeff(Bhat,6,0),5,17)),t5i,'leading b')
    equal(m.fm(m.fm(W,t5),m.fm(Wi,t5i)),field(1),'leading guard')

    def scaled(poly,offset=0):
        out=m.Poly('scale')
        for ex,cc in poly.items():
            e=list(ex);e[4]=2*ex[4]+ex[6]+offset
            out=add(out,m.Poly('scale',{tuple(e):cc}))
        return m.bounded(out)
    so,SS,tt=var(4,'scale'),var(5,'scale'),var(6,'scale')
    origA,origB=scaled(Ahat,-3),scaled(Bhat,-5)
    origd,origv,origk=scaled(Dformal,-1),scaled(Vformal,-2),scaled(Kpar,-3)
    origu,origell=scaled(U,-1),scaled(E,-3)
    origPi=add(tt,neg(mul(origu,power(tt,2))),mul(SS,power(tt,3)))
    origUpper=neg(add(mul(mul(origell,tt),origPi),mul(tt,power(origPi,2))))
    origJ=sub(mul(diff(origA,5),diff(origB,6)),mul(diff(origA,6),diff(origB,5)))
    origResidual=sub(origJ,add(origUpper,const(1,'scale'),mul(origu,tt)))
    guard=scale(power(so,8),m.fm(W,t5))
    reconstruction=add(mul(SS,power(tt,3)),
        mul(sub(mul(SS,origd),origu),power(tt,2)),
        mul(add(const(1,'scale'),neg(mul(origu,origd)),mul(SS,origv)),tt),origk)
    comparisons={'A_inverse':sub(origA,reconstruction),
        'target_inverse':sub(origUpper,scaled(Delta,-7)),
        'bracket_scale':sub(origJ,scaled(J,-7))}
    low1=[];low0=[]
    for i in range(21):
        expected=sub(scaled(P1[i],-6),origu if i==0 else {})
        low1.append(sub(coeff(coeff(origResidual,6,1),5,i),expected))
    for i in range(24):
        expected=sub(scaled(P0[i],-7),const(1,'scale') if i==0 else {})
        low0.append(sub(coeff(coeff(origResidual,6,0),5,i),expected))
    comparisons['low1']=low1;comparisons['low0']=low0
    orig_a=coeff(coeff(origA,6,0),5,10)
    orig_b=coeff(coeff(origB,6,0),5,17)
    comparisons['guard_product']=sub(mul(guard,mul(orig_a,orig_b)),const(1,'scale'))
    scale_record={'origA':origA,'origB':origB,'origd':origd,'origv':origv,'origk':origk,
        'origu':origu,'origell':origell,'origPi':origPi,'origUpper':origUpper,
        'origJ':origJ,'origResidual':origResidual,'guard':guard,'comparisons':comparisons}

    Hq=m.retype(coeff(psis[0],4,0),'graph')
    critical_c=scalar(coeff(psis[0],4,1))
    equal(psis[0],add(m.retype(Hq,'band'),scale(z,critical_c)),'critical affine graph')
    critical_ci=m.fi(critical_c,'critical_c')
    zeta=scale(Hq,m.fn(critical_ci))
    graph_rows=[m.substitute_z(poly,zeta) for poly in psis[1:]+P1[1:10]+P0[1:13]]
    graph_rows.append(m.substitute_z(sub(mul(zr,P1[0]),mul(U,P0[0])),zeta))
    ell=m.substitute_z(P0[0],zeta);g=mul(Hq,ell)
    graphU=m.retype(U,'graph')
    equal(m.substitute_z(psis[0],zeta),{},'critical elimination')
    equal(mul(zeta,ell),scale(g,m.fn(critical_ci)),'guard identification')
    if len(graph_rows)!=25:raise ValueError('25 row inventory')
    if len(diagnostics)!=150 or len(required)!=111 or len(diagnostics.keys()-required)!=39:
        raise ValueError('full 150/111/39 diagnostic inventory')
    if len(inverses)!=2 or len(poles)!=2 or len(scale_record)!=13:
        raise ValueError('boundary/scale inventory')
    if set(m.UNITS)!={'dL','W','t5','H7_5','H7_6','critical_c',
                     'det1','det2','det3','det4','det5','det6','pivot8','pivot9','pivot10'}:
        raise ValueError('15 named inverse nodes')
    if list(m.DENOMINATORS)!=[label for label,value in registry]:
        raise ValueError('all named rational denominators')
    # The partition is checked only after every stipulated internal expression
    # has been computed. Alternative records and both pole subrecords may be nonzero.
    for label in sorted(required):
        if diagnostics[label]:raise ValueError('STOP_CANONICAL_ANOMALY: '+label)
    for label,value in comparisons.items():
        for poly in value if isinstance(value,list) else [value]:
            if poly:raise ValueError('STOP_CONSTRUCTION_ANOMALY: scale '+label)
    weights=[8,9,10]+list(range(19,10,-1))+list(range(22,10,-1))+[27]
    return {'schema':'f10-r3-direct-rows/v1','job_tag':'f10-source-cone-r3-direct-rows-v1',
        'contract_sha256':meta['contract_sha256'],'source_pins':meta['source_pins'],
        'place':meta['place'],'graph':{'Hq':wire_p(Hq,7),'c':wire_f(critical_c),
        'c_inverse':wire_f(critical_ci),'zeta':wire_p(zeta,7),
        'slots':[wire_p(poly,w) for poly,w in zip(graph_rows,weights)],
        'ell':wire_p(ell,23),'g':wire_p(g,30),'U':wire_p(graphU,4)}}


def main():
    meta=authorize('produce')
    import json
    import os
    import hashlib
    import tempfile
    payload=build(meta)
    raw=(json.dumps(payload,ensure_ascii=True,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    if len(raw)>134217728:raise ValueError('STOP_WIRE_BYTE_CAP')
    path=meta['artifact_path'];parent=os.path.dirname(path)
    fd,temporary=tempfile.mkstemp(prefix='.direct-rows-',dir=parent)
    try:
        with os.fdopen(fd,'wb') as stream:
            stream.write(raw);stream.flush();os.fchmod(stream.fileno(),0o444);os.fsync(stream.fileno())
        with open(temporary,'rb') as stream:
            if hashlib.sha256(stream.read()).digest()!=hashlib.sha256(raw).digest():
                raise ValueError('new artifact readback')
        os.link(temporary,path,follow_symlinks=False)
        directory=os.open(parent,os.O_RDONLY|os.O_DIRECTORY)
        try:os.fsync(directory)
        finally:os.close(directory)
    finally:
        os.unlink(temporary)
    print('FORMED_UNCHECKED_DIRECT_ROWS_25_NO_SOURCE_OUTCOME')


if __name__=='__main__':
    main()
