"""Independent direct-rows checker. STATIC/UNEXECUTED; no producer science import."""
from authority import authorize


def check_file(ctx):
    import json
    import re
    import check_arithmetic as n
    from check_arithmetic import (Rational as Q, F, constant as C0, symbol as sym,
        add, sub, neg, mul, scale as sc, power as pw, derivative as der,
        extract as co, move, scalar as value, series, primitive as integ,
        equal as eq, need, Poly, zero, cast)

    def keys(obj, names):
        need(type(obj) is dict and set(obj) == set(names.split()), 'strict keys: '+names)

    def array(obj,size):
        need(type(obj) is list and len(obj) == size, 'fixed array length')
        return obj

    def integer(s,bound):
        need(type(s) is str and re.fullmatch('0|[1-9][0-9]{0,9}',s), 'canonical integer')
        v = int(s); need(v <= bound, 'integer bound'); return v

    def pairs(xs):
        out = {}
        for k,v in xs:
            need(k not in out,'duplicate JSON key'); out[k] = v
        return out

    def no_number(_): raise n.Stop('native JSON number/constant')
    keys(ctx,'artifact_path contract_sha256 source_pins place')
    with open(ctx['artifact_path'],'rb') as stream:
        raw = stream.read(134217729)
    need(0 < len(raw) <= 134217728,'encoded object cap')
    raw.decode('ascii')
    doc = json.loads(raw,object_pairs_hook=pairs,parse_int=no_number,
                     parse_float=no_number,parse_constant=no_number)
    need((json.dumps(doc,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii') == raw,
         'INPUT-only canonical round-trip')
    keys(doc,'schema job_tag contract_sha256 source_pins place graph')
    eq(doc['schema'],'f10-r3-necessary-rows/v1','schema')
    eq(doc['job_tag'],'f10-source-cone-r3-necessary-rows-v1','job tag')
    need(type(doc['source_pins']) is dict and all(type(k) is str for k in doc['source_pins']),
         'source vector mapping')
    for pin in [doc['contract_sha256']] + list(doc['source_pins'].values()):
        need(type(pin) is str and re.fullmatch('[0-9a-f]{64}',pin),'SHA256 syntax')
    eq(doc['contract_sha256'],ctx['contract_sha256'],'ROOT contract binding')
    eq(doc['source_pins'],ctx['source_pins'],'ROOT exact source vector')
    eq(doc['place'],ctx['place'],'ROOT fixed place')
    place = doc['place']; keys(place,'p degree phi P7_mod_p')
    prime = integer(place['p'],2147483647); f = integer(place['degree'],7)
    need(prime >= 2 and f >= 1,'place range')
    phi = [integer(x,prime-1) for x in array(place['phi'],f+1)]
    prescribed_septic = [integer(x,prime-1) for x in array(place['P7_mod_p'],8)]
    tau = Q(3,10)
    d = [(1+tau)*(2-3*tau),-12*(1-tau),Q(12)]
    k = [2*(2-3*tau)*(1+tau)*(2+tau)*(3+tau),
         42*(1+tau)*(2+tau)*(4*tau-3),840*(1-tau*tau),Q(-840)]
    gam = [tau*(1+tau)*(2+tau)*(3+tau),-30*tau*(1+tau)*(2+tau),
           180*tau*(1+tau),-120*tau]
    septic = n.qadd([2*x for x in n.qmul(k,k)], n.qadd(
        [-140*tau*x for x in n.qmul(n.qmul([1+tau,-6],k),d)],
        [245*x for x in n.qmul(gam,n.qmul(d,d))]))
    eq(len(septic),8,'literal septic length')
    L = -245*120*144*tau
    eq(septic[-1],L,'literal septic leading coefficient')
    rational_modulus = [x/L for x in septic]
    n.initialize(prime,phi,rational_modulus)
    eq(n.DEGREE,f,'field degree')
    eq(prescribed_septic,[n.ground(x) for x in rational_modulus],'literal P7 residues')
    names = ['K8','K9','K10']+['A1_'+str(i) for i in range(1,10)]+['A0_'+str(i) for i in range(1,13)]+['T']
    weights = [8,9,10]+list(range(19,10,-1))+list(range(22,10,-1))+[27]
    graph = doc['graph']; keys(graph,'Hq c c_inverse zeta slots ell g U')
    term_count = [0]
    def elt(v): return tuple(integer(s,prime-1) for s in array(v,f))
    def poly(v,weight):
        keys(v,'kind terms'); eq(v['kind'],'graph','graph polynomial type')
        need(type(v['terms']) is list and len(v['terms']) <= 20000,'wire polynomial term cap')
        term_count[0] += len(v['terms']); need(term_count[0] <= 400000,'wire aggregate term cap')
        out = {}; previous = None
        for term in v['terms']:
            ex,vv = array(term,2)
            exponent = tuple(integer(s,256) for s in array(ex,4))
            need(sum((j+1)*e for j,e in enumerate(exponent)) == weight,'exact graph term weight')
            coefficient = elt(vv)
            need(any(coefficient) and (previous is None or previous < exponent),'numericallex nonzero sparse term')
            previous = exponent; out[exponent+(0,0,0)] = coefficient
        return Poly('graph',out)
    parsed_graph = {key:poly(graph[key],weight) for key,weight in [('Hq',7),('zeta',7),('ell',23),('g',30),('U',4)]}
    parsed_graph['c'],parsed_graph['c_inverse'] = elt(graph['c']),elt(graph['c_inverse'])
    parsed_graph['slots'] = [poly(v,w) for v,w in zip(array(graph['slots'],25),weights)]
    # Complete strict wire parsing is over; candidate values never feed Eval_C.
    rational_registry = []
    def denominator(label,input_value):
        v = n.ground(input_value); need(v != 0,'BAD_DENOMINATOR '+label)
        inv = pow(v,-1,prime); need(v*inv % prime == 1,'denominator product '+label)
        rational_registry.append((label,v,inv)); return F(Q(1,input_value))
    for label,v in [('D0:tau',10),('D0:W',210),('D0:lead',L)]: denominator(label,v)
    for j in range(1,8): denominator('D0:series:'+str(j),j)
    for j in range(1,9): denominator('D0:integral:'+str(j),j)
    for h in (5,6):
        denominator('D0:ratio-den:'+str(h),27-h)
        denominator('D0:ratio-num:'+str(h),3*(h-3)-2)
    for label,v in [('D0:half',2),('D0:ell21',21),('D0:ell11',11)]: denominator(label,v)
    for h in range(1,11):
        for j in range(5 if h <= 6 else 3): denominator('D1:'+str(h)+':'+str(j),10*j-3*(17-h))
    for j in range(5):
        for i in range(18-3*j):
            if (j,i) not in ((0,0),(3,1)): denominator('D2:'+str(j)+':'+str(i),j-3*i)
    eq(len(rational_registry),125,'complete ordered rational registry')
    need(len({x[0] for x in rational_registry}) == 125,'distinct denominator labels')
    units = {}
    def unit(label,v):
        need(label not in units,'duplicate unit node')
        inv = n.inverse(v)
        eq(n.fmul(v,inv),F(1),'named inverse product '+label)
        eq(n.fmul(inv,v),F(1),'named reverse inverse product '+label)
        units[label] = (v,inv); return inv
    dL,KL,gamma = F(d),F(k),F(gam)
    di = unit('dL',dL)
    W = n.fmul(F(Q(-1,210)),n.fmul(KL,di)); Wi = unit('W',W)
    T,z = sym(6),sym(4)
    c = add(C0(1),T,sc(pw(T,2),F([0,1])),sc(pw(T,3),W))
    ts = series(c,Q(17,10),7); t5 = value(co(ts,6,5)); t5i = unit('t5',t5)
    C = sc(c,Wi); D = sc(Poly('band',{e:v for e,v in ts.items() if e[6] <= 5}),t5i)
    middle = {h:value(co(series(c,Q(27-h,10),7),6,7)) for h in (5,6)}
    middle_inverse = {h:unit('H7_'+str(h),middle[h]) for h in (5,6)}
    eq(add(sc(mul(C,der(D,6)),10),sc(mul(der(C,6),D),-17)),neg(pw(T,7)),'leading ODE')
    eq(co(ts,6,6),zero(),'leading contact6'); eq(co(ts,6,7),zero(),'leading contact7')
    a,b = value(co(C,6,0)),value(co(D,6,0))

    diagnostics = []
    def diagnostic(label,p,canonical):
        need(label not in {item[0] for item in diagnostics},'duplicate diagnostic label')
        diagnostics.append((label,p,canonical))

    def envelope(p,weight):
        for ex in p:
            actual = sum(ex[j]*(1,2,3,4,7)[j] for j in range(5))
            if p.kind in ('raw','laurent_S'): actual += ex[5]+3*ex[6]
            eq(actual,weight,'exact '+p.kind+' weight')

    def oper(h,ap,bp):
        out = zero()
        for i in range(4):
            for ell in range(6):
                if i+ell:
                    part = sc(mul(co(C,6,i),co(bp,6,ell)),10*ell-(17-h)*i)
                    out = add(out,move(part,6,i+ell-1))
        for i in range(3):
            for ell in range(6):
                if i+ell:
                    part = sc(mul(co(ap,6,i),co(D,6,ell)),(10-h)*ell-17*i)
                    out = add(out,move(part,6,i+ell-1))
        return out

    def low(p): return [co(p,6,1),co(p,6,0)]
    def upper(p): return Poly('band',{e:v for e,v in p.items() if e[6] >= 2})

    def solve_upper(h,ap,target,degree,fixed=None):
        bp = zero() if fixed is None else fixed
        for j in range(degree,-1,-1):
            pivot = 10*j-3*(17-h)
            defect = co(sub(oper(h,ap,bp),target),6,j+2)
            bp = add(bp,move(sc(defect,F(Q(-1,pivot))),6,j))
        res = sub(oper(h,ap,bp),target)
        return bp,low(res),upper(res)

    def determinant(m):
        ans = F(0)
        for perm,sign in (((0,1,2),1),((1,2,0),1),((2,0,1),1),
                          ((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)):
            term = F(sign)
            for i in range(3): term = n.fmul(term,m[i][perm[i]])
            ans = n.fadd(ans,term)
        return ans

    def matrix_inverse(m,h):
        det = determinant(m); invdet = unit('det'+str(h),det)
        inv = []
        for row in range(3):
            out = []
            for col in range(3):
                rr = [i for i in range(3) if i != col]
                cc = [j for j in range(3) if j != row]
                minor = n.fadd(n.fmul(m[rr[0]][cc[0]],m[rr[1]][cc[1]]),
                               n.fneg(n.fmul(m[rr[0]][cc[1]],m[rr[1]][cc[0]])))
                out.append(n.fmul(F((-1)**(row+col)),n.fmul(minor,invdet)))
            inv.append(out)
        for left,right in ((m,inv),(inv,m)):
            for i in range(3):
                for j in range(3):
                    got = F(0)
                    for k0 in range(3): got = n.fadd(got,n.fmul(left[i][k0],right[k0][j]))
                    eq(got,F(int(i == j)),'two-sided completed matrix product')
        return inv

    def act(matrix,rhs): return [add(*(sc(p,v) for p,v in zip(rhs,row))) for row in matrix]

    Ab,Bb = [C],[D]
    bands,psis,lambdas,selections = [],[],[],[]
    U = zero(); E = zero()
    for h in range(1,11):
        forcing = zero()
        for i in range(1,h):
            for ak in range(3):
                for bl in range(5):
                    if ak+bl:
                        part = sc(mul(co(Ab[i],6,ak),co(Bb[h-i],6,bl)),
                                  (10-i)*bl-(17-h+i)*ak)
                        forcing = add(forcing,move(part,6,ak+bl-1))
        envelope(forcing,h)
        if h <= 6:
            part,basepair,defect = solve_upper(h,zero(),neg(forcing),4)
            diagnostic('upper:'+str(h)+':part',defect,True)
            basis,columns = [],[]
            for j in range(3):
                Aj = pw(T,j); targetj = sc(pw(T,6),-2) if (h,j) == (4,2) else zero()
                vj,pair,defect = solve_upper(h,Aj,targetj,4)
                diagnostic('upper:'+str(h)+':basis:'+str(j),defect,True)
                basis.append(vj)
                rhoj = sub(sc(co(vj,6,0),n.fmul(F(10),a)),sc(co(Aj,6,0),n.fmul(F(17),b)))
                columns.append([value(pair[0]),value(pair[1]),value(rhoj)])
            matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
            inv = matrix_inverse(matrix,h)
            rho = sym(h-1) if h <= 4 else zero()
            rhs = [neg(basepair[0]),neg(basepair[1]),rho]; xyz = act(inv,rhs)
            if h in (5,6):
                ratio = Q(3*(h-3)-2,27-h)
                eq(inv[2][2],n.fmul(F(ratio),middle[h]),'middle Phi/H7 relation')
                rho = sc(neg(xyz[2]),n.fmul(F(1/ratio),middle_inverse[h]))
                rhs = [neg(basepair[0]),neg(basepair[1]),rho]; xyz = act(inv,rhs)
            eq(act(matrix,xyz),rhs,'forward affine completed map')
            Ah = add(*(move(x,6,j) for j,x in enumerate(xyz)))
            Bh = add(part,*(mul(xyz[j],basis[j]) for j in range(3)))
            target = sc(mul(xyz[2],pw(T,6)),-2) if h == 4 else zero()
            diagnostic('early:'+str(h)+':residual',sub(add(oper(h,Ah,Bh),forcing),target),True)
            actual_rho = sub(sc(co(sub(Bh,part),6,0),n.fmul(F(10),a)),sc(co(Ah,6,0),n.fmul(F(17),b)))
            diagnostic('early:'+str(h)+':rho',sub(actual_rho,rho),True)
            if h in (5,6):
                diagnostic('middle:'+str(h)+':U2',xyz[2],True)
                diagnostic('middle:'+str(h)+':V4',co(Bh,6,4),True)
            if h == 4: U = neg(xyz[2])
            bands.append({'gap':h,'forcing':forcing,'part':part,'basis':basis,'matrix':matrix,
                          'inverse':inv,'rho':rho,'A':Ah,'B':Bh})
        else:
            apart,fixed,target,avar,tvar = zero(),zero(),zero(),C0(1),zero()
            if h == 7:
                d0 = co(Ab[3],6,2); y = sub(z,mul(U,d0))
                apart,target = mul(y,T),sc(mul(z,pw(T,5)),-2)
                N = sub(sub(target,forcing),mul(y,sub(sc(mul(T,der(D,6)),3),sc(D,17))))
                for j in range(5):
                    eq(co(N,6,j),add(neg(co(forcing,6,j)),sc(mul(y,co(D,6,j)),17-3*j)),
                       'critical unchanged unshifted D coefficient')
            elif h == 8:
                fixed,target = mul(pw(U,2),pw(T,3)),neg(mul(pw(U,2),pw(T,5)))
            elif h == 10:
                avar,tvar = zero(),neg(pw(T,4))
            part,basepair,defect = solve_upper(h,apart,sub(target,forcing),2,fixed)
            diagnostic('upper:'+str(h)+':part',defect,h == 7)
            vvar,col,defect = solve_upper(h,avar,tvar,2)
            diagnostic('upper:'+str(h)+':variation',defect,h == 7)
            c1,c0 = [value(v) for v in col]
            if h == 7:
                invC2 = sc(series(c,Q(-2),6),n.fmul(W,W)); ll = []
                for R in (T,C0(1)):
                    v = mul(pw(C,2),integ(mul(R,invC2)))
                    ll.append(value(sub(sc(co(v,6,6),value(co(C,6,2))),sc(co(v,6,5),Q(1,2)))))
                l1,l0 = ll
            else:
                index = 1 if any(c1) else 0
                chosen = c1 if index else c0
                need(any(chosen),'STOP_BAD_COLUMN_PLACE gap'+str(h))
                pivot_inverse = unit('pivot'+str(h),chosen)
                l1,l0 = (pivot_inverse,F(0)) if index else (F(0),pivot_inverse)
                selections.append((h,index))
            eq(n.fadd(n.fmul(l1,c1),n.fmul(l0,c0)),F(1),'actual two-row column completion')
            val = neg(add(sc(basepair[0],l1),sc(basepair[1],l0)))
            psi = sub(sc(basepair[1],c1),sc(basepair[0],c0))
            Ah,Bh = add(apart,mul(val,avar)),add(part,mul(val,vvar))
            residual = sub(add(oper(h,Ah,Bh),forcing),add(target,mul(val,tvar)))
            eq(low(residual),[sc(psi,n.fneg(l0)),sc(psi,l1)],'full forced low-pair identity')
            if h == 10:
                E = val; fc,hc = value(co(C,6,2)),value(co(C,6,1))
                ge = n.fmul(F(Q(1,21)),n.fadd(n.fmul(F(13),hc),n.fneg(n.fmul(F(Q(24,11)),n.fmul(fc,fc)))))
                eq(vvar,add(pw(T,2),sc(T,n.fmul(F(Q(6,11)),fc)),C0(ge)),'literal ell column')
            psis.append(psi); lambdas.append((l1,l0))
            bands.append({'gap':h,'forcing':forcing,'part':part,'A_part':apart,'fixed':fixed,
                'target':target,'A_var':avar,'target_var':tvar,'B_var':vvar,'column':(c1,c0),
                'lambda':(l1,l0),'base':basepair,'value':val,'Psi':psi,'A':Ah,'B':Bh,
                'residual':residual,'upper_defect':upper(residual)})
        envelope(Ah,h); envelope(Bh,h)
        need(all(e[6] <= (4 if h <= 6 else (3 if h == 8 else 2)) for e in Bh),
             'complete formal mate support')
        Ab.append(Ah); Bb.append(Bh)
    eq(len(Ab),11,'formal A sequence'); eq(len(Bb),11,'formal B sequence')
    eq(len(psis),4,'all raw compatibility slots'); eq(len(selections),3,'late selection inventory')

    # Fixed installation, NEVER feeding its projection back into formal bands.
    A = zero('raw')
    install_indices = [range(4)] + [range(3)]*6 + [range(2),range(1),range(1),range(0)]
    for h in range(11):
        need(all(e[6] in install_indices[h] for e in Ab[h]),'fixed formal A support')
        for j in install_indices[h]:
            coefficient = co(Ab[h],6,j); exponent = 10-h-3*j
            if exponent >= 0:
                A = add(A,move(move(cast(coefficient,'raw'),5,exponent),6,j))
            else:
                need((h,j) in ((5,2),(6,2)),'unexpected installation discard')
                diagnostic('install:'+str(h)+':'+str(j),coefficient,True)
    eq(Ab[10],zero(),'A10 fixed gauge')
    Uraw,Eraw = cast(U,'raw'),cast(E,'raw')
    S,theta,zraw = sym(5,'raw'),sym(6,'raw'),sym(4,'raw')
    Ac = [co(A,6,j) for j in range(4)]
    dp = move(cast(add(Ac[2],Uraw),'laurent_S'),5,-1)
    vp = move(add(cast(sub(Ac[1],zraw),'laurent_S'),mul(cast(Uraw,'laurent_S'),dp)),5,-1)
    kp = Ac[0]
    diagnostic('auxiliary.Dnegative',Poly('laurent_S',{e:v for e,v in dp.items() if e[5] < 0}),True)
    diagnostic('auxiliary.Vnegative',Poly('laurent_S',{e:v for e,v in vp.items() if e[5] < 0}),True)
    pi = add(mul(zraw,theta),neg(mul(Uraw,pw(theta,2))),mul(S,pw(theta,3)))
    delta = neg(add(mul(mul(Eraw,theta),pi),mul(theta,pw(pi,2))))
    for p,w in ((A,10),(Uraw,4),(Eraw,10),(dp,3),(vp,6),(kp,10),(pi,10),(delta,23)):
        envelope(p,w)
    eq(co(kp,5,0),zero('raw'),'translation gauge')
    eq(Ac[3],S,'installed highest theta term')

    # Separate Euler mate: coefficient-pair assembly, no producer Q_j formula.
    Bc = [zero('raw') for _ in range(9)]; Bc[5] = pw(S,2)
    for j in range(4,-1,-1):
        other = zero('raw')
        for ak in range(3):
            ell = j+3-ak
            if ell <= 5:
                other = add(other,sc(mul(der(Ac[ak],5),Bc[ell]),ell),
                            sc(mul(Ac[ak],der(Bc[ell],5)),-ak))
        rhs = sub(co(delta,6,j+2),other)
        envelope(rhs,17-3*j)
        need(all(e[6] == 0 and 0 <= e[5] <= 17-3*j for e in rhs),'full Euler coefficient range')
        for i in range(18-3*j):
            qji = co(rhs,5,i); pivot = j-3*i
            if (j,i) in ((0,0),(3,1)):
                diagnostic('Euler-resonance:'+str(j)+':'+str(i),cast(qji,'band'),False)
                continue
            need(pivot != 0,'fixed Euler nonresonance')
            Bc[j] = add(Bc[j],move(sc(qji,F(Q(1,pivot))),5,i))
    B = add(*(move(Bc[j],6,j) for j in range(6)))
    envelope(B,17)
    eq(co(co(B,6,3),5,1),zero('raw'),'Euler shear gauge')
    eq(co(co(B,6,0),5,0),zero('raw'),'Euler translation gauge')
    for p,top,total in ((A,3,10),(B,5,17)):
        need(all(e[6] <= top and e[5] <= total-3*e[6] for e in p),'complete installed support')

    def band(p,total,h):
        out = {}
        for ex,v in p.items():
            if ex[5]+3*ex[6] == total-h:
                key = list(ex); key[5] = 0; out[tuple(key)] = v
        return Poly('band',out)
    for h in range(11):
        diagnostic('Euler-band:'+str(h),sub(band(B,17,h),Bb[h]),h <= 7)

    # FULL108 bracket inventory, including its45 low and63 upper positions.
    J = zero('raw')
    for ak in range(4):
        for bl in range(6):
            if ak+bl:
                part = sub(sc(mul(der(Ac[ak],5),Bc[bl]),bl),sc(mul(Ac[ak],der(Bc[bl],5)),ak))
                J = add(J,move(part,6,ak+bl-1))
    residual = sub(J,delta); envelope(residual,23)
    need(all(e[6] <= 7 and e[5] <= 23-3*e[6] for e in residual),'full residual support')
    raw_slots = []
    for j in range(8):
        for i in range(24-3*j):
            value_ji = cast(co(co(residual,6,j),5,i),'band'); raw_slots.append(value_ji)
            if j >= 2:
                diagnostic('upper-J:'+str(j)+':'+str(i),value_ji,23-i-3*j <= 7)
    eq(len(raw_slots),108,'all108 coefficient positions')
    P1 = [cast(co(co(residual,6,1),5,i),'band') for i in range(21)]
    P0 = [cast(co(co(residual,6,0),5,i),'band') for i in range(24)]
    eq(len(P1)+len(P0),45,'all45 low positions')
    for j,rows,total in ((1,P1,20),(0,P0,23)):
        for i,p in enumerate(rows): envelope(p,total-i)
    for h in range(11):
        for j,rows,total in ((1,P1,20),(0,P0,23)):
            actual = rows[total-h]
            wanted = zero() if h < 7 else sc(psis[h-7],n.fneg(lambdas[h-7][1]) if j == 1 else lambdas[h-7][0])
            diagnostic('low-band:'+str(h)+':'+str(j),sub(actual,wanted),h <= 7)

    eq(value(co(co(A,6,0),5,10)),Wi,'installed first leading scalar')
    eq(value(co(co(B,6,0),5,17)),t5i,'Euler second leading scalar')
    eq(n.fmul(n.fmul(W,t5),n.fmul(Wi,t5i)),F(1),'leading guarded inverse product')

    # Distinct Laurent scale type: coordinate4=s, coordinate6=t, NOT z/theta.
    def to_scale(p,divide_power=0,rescale_theta=False):
        need(p.kind in ('raw','band','laurent_S'),'scale input type')
        out = zero('scale')
        for ex,v in p.items():
            key = list(ex); key[4] = 2*ex[4]+(ex[6] if rescale_theta else 0)-divide_power
            out = add(out,Poly('scale',{tuple(key):v}))
        return out
    st,ss = sym(6,'scale'),sym(5,'scale')
    origA,origB = to_scale(A,3,True),to_scale(B,5,True)
    origd,origv,origk = to_scale(dp,1),to_scale(vp,2),to_scale(kp,3)
    origu,origell = to_scale(U,1),to_scale(E,3)
    origPi = add(st,neg(mul(origu,pw(st,2))),mul(ss,pw(st,3)))
    recovered_A = add(mul(ss,pw(st,3)),mul(sub(mul(ss,origd),origu),pw(st,2)),
        mul(add(C0(1,'scale'),neg(mul(origu,origd)),mul(ss,origv)),st),origk)
    origUpper = neg(add(mul(mul(origell,st),origPi),mul(st,pw(origPi,2))))
    # Independent coefficient-pair bracket again, now with signed scale powers.
    origJ = zero('scale')
    for ak in range(4):
        for bl in range(6):
            if ak+bl:
                pa,pb = co(origA,6,ak),co(origB,6,bl)
                part = sub(sc(mul(der(pa,5),pb),bl),sc(mul(pa,der(pb,5)),ak))
                origJ = add(origJ,move(part,6,ak+bl-1))
    origResidual = sub(sub(origJ,origUpper),add(C0(1,'scale'),mul(origu,st)))
    guard = move(C0(n.fmul(W,t5),'scale'),4,8)
    orig_a,orig_b = co(co(origA,6,0),5,10),co(co(origB,6,0),5,17)
    comparisons = {'A_inverse':sub(origA,recovered_A),
        'target_inverse':sub(origUpper,to_scale(delta,7,True)),
        'bracket_scale':sub(origJ,to_scale(J,7,True)), 'low1':[], 'low0':[],
        'guard_product':sub(mul(guard,mul(orig_a,orig_b)),C0(1,'scale'))}
    for i in range(21):
        wanted = to_scale(P1[i],6)
        if i == 0: wanted = sub(wanted,origu)
        comparisons['low1'].append(('scale-low1:'+str(i),sub(co(co(origResidual,6,1),5,i),wanted)))
    for i in range(24):
        wanted = to_scale(P0[i],7)
        if i == 0: wanted = sub(wanted,C0(1,'scale'))
        comparisons['low0'].append(('scale-low0:'+str(i),sub(co(co(origResidual,6,0),5,i),wanted)))
    scale_values = {'origA':origA,'origB':origB,'origd':origd,'origv':origv,'origk':origk,
        'origu':origu,'origell':origell,'origPi':origPi,'origUpper':origUpper,'origJ':origJ,
        'origResidual':origResidual,'guard':guard,'comparisons':comparisons}
    for name in ('A_inverse','target_inverse','bracket_scale','guard_product'):
        need(not comparisons[name],'CONSTRUCTION_ANOMALY scale.'+name)
    for name in ('low1','low0'):
        for label,p in comparisons[name]: need(not p,'CONSTRUCTION_ANOMALY '+label)
    eq(len(comparisons),6,'all six SCALE comparison groups')

    # Complete diagnostic inventories, reordered literally; never invented zeros.
    expected_labels = []
    for h in range(1,7):
        expected_labels.append('upper:'+str(h)+':part')
        expected_labels.extend('upper:'+str(h)+':basis:'+str(j) for j in range(3))
    for h in range(7,11): expected_labels.extend(['upper:'+str(h)+':part','upper:'+str(h)+':variation'])
    for h in range(1,7): expected_labels.extend(['early:'+str(h)+':residual','early:'+str(h)+':rho'])
    for h in (5,6): expected_labels.extend(['middle:'+str(h)+':U2','middle:'+str(h)+':V4'])
    expected_labels += ['install:5:2','install:6:2','Euler-resonance:0:0','Euler-resonance:3:1']
    expected_labels.extend('Euler-band:'+str(h) for h in range(11))
    expected_labels.extend('upper-J:'+str(j)+':'+str(i) for j in range(2,8) for i in range(24-3*j))
    expected_labels.extend('low-band:'+str(h)+':'+str(j) for h in range(11) for j in (1,0))
    expected_labels += ['auxiliary.Dnegative','auxiliary.Vnegative']
    by_label = {label:(p,canonical) for label,p,canonical in diagnostics}
    eq(len(diagnostics),150,'all150 internal diagnostics')
    eq(set(by_label),set(expected_labels),'complete diagnostic names')
    diagnostics = [(label,*by_label[label]) for label in expected_labels]
    eq(sum(int(flag) for _,_,flag in diagnostics),111,'all111 canonical anomaly checks')
    eq(sum(int(not flag) for _,_,flag in diagnostics),39,'all39 alternative records retained')
    for label,p,canonical in diagnostics:
        if canonical: need(not p,'CANONICAL_ANOMALY '+label)

    Hq = cast(co(psis[0],4,0),'graph'); critical_c = value(co(psis[0],4,1))
    eq(psis[0],add(cast(Hq,'band'),sc(z,critical_c)),'complete Psi7=Hq+c*z')
    ci = unit('critical_c',critical_c); zeta = sc(Hq,n.fneg(ci))
    eq(n.graph_substitute(psis[0],zeta),zero('graph'),'critical graph equation')
    mixed = sub(mul(z,P1[0]),mul(U,P0[0]))
    wanted_slots = [n.graph_substitute(p,zeta) for p in psis[1:]+P1[1:10]+P0[1:13]+[mixed]]
    ell = n.graph_substitute(P0[0],zeta); g = mul(Hq,ell); Ug = cast(U,'graph')
    eq(mul(zeta,ell),sc(g,n.fneg(ci)),'critical localization guard identity')
    expected_units = {'dL','W','t5','H7_5','H7_6','critical_c'} | {'det'+str(h) for h in range(1,7)} | {'pivot'+str(h) for h in (8,9,10)}
    eq(set(units),expected_units,'exact15 scalar inverse nodes')
    need(len(units) == 15,'all scalar inverses retained')
    ordered_units = [(label,*units[label]) for label in
        ['dL','W','t5','H7_5','H7_6']+['det'+str(h) for h in range(1,7)]+['critical_c']+
        ['pivot'+str(h) for h in (8,9,10)]]
    eq(len(ordered_units),15,'fixed ordered scalar registry')
    # Parser compares received bytes only with their OWN encoding, never Eval_C.
    # Compare every field/slot separately; no earlier aggregate can mask T.
    eq(parsed_graph['c'],critical_c,'direct-source critical c')
    eq(parsed_graph['c_inverse'],ci,'direct-source critical inverse')
    for key,actual,weight in [('Hq',Hq,7),('zeta',zeta,7),('ell',ell,23),('g',g,30),('U',Ug,4)]:
        envelope(actual,weight); eq(parsed_graph[key],actual,'direct-source graph '+key)
    for label,record,actual,weight in zip(names,parsed_graph['slots'],wanted_slots,weights):
        envelope(actual,weight)
        eq(record,actual,'direct-source graph slot '+label)
    eq(len(wanted_slots),25,'all25 source-derived rows')
    return 'CHECKED_NECESSARY_ROWS_25_NO_SOURCE_OUTCOME'


def main():
    import sys
    if sys.flags.optimize:
        raise SystemExit('REFUSED: ordinary interpreter required')
    ctx = authorize('check')
    import check_arithmetic as n
    try:
        verdict = check_file(ctx)
        # Reauthenticate the same ROOT/source/input metadata before success.
        n.equal(authorize('check'),ctx,'terminal ROOT metadata drift')
        print(verdict)
    except n.Mismatch as exc:
        # A correctly rebound semantic fixture retains the same metadata here.
        n.equal(authorize('check'),ctx,'rejection ROOT metadata drift')
        print('CHECK FAILED: '+str(exc),file=sys.stderr)
        raise SystemExit(2)
    except (n.Stop,ValueError,TypeError,KeyError,AttributeError,MemoryError,OverflowError,RecursionError,OSError) as exc:
        print('STOP_NONDECISION: '+str(exc)[:240],file=sys.stderr)
        raise SystemExit(2)


if __name__ == '__main__':
    main()
