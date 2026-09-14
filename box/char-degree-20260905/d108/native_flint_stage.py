#!/usr/bin/env python3
"""Bounded native FLINT exact-Q preprocessing, then full coefficient-row CAS.

Uses only the monic-z divisions; all polynomial parameters remain variables.
The early D band simplification is enabled only with --early-D, after audit.
"""
import argparse,hashlib,itertools,json,os,signal,subprocess,time
from pathlib import Path
import sympy as sp
from flint import fmpq,fmpq_mpoly_ctx
from char_degree_driver import build,exprS
OUT=Path(__file__).resolve().parent

def convert(table,ctx,names):
    positions={n:i for i,n in enumerate(names)};terms={}
    for (r,q),expr in table.items():
        expr=sp.expand(expr);variables=sorted(expr.free_symbols,key=str)
        if not variables:
            exponent=[0]*len(names);exponent[0]=q;exponent[1]=r
            terms[tuple(exponent)]=fmpq(int(sp.numer(expr)),int(sp.denom(expr)));continue
        poly=sp.Poly(expr,*variables,domain=sp.QQ)
        for mon,co in poly.terms():
            exponent=[0]*len(names);exponent[0]=q;exponent[1]=r
            for v,e in zip(variables,mon):exponent[positions[str(v)]]=e
            key=tuple(exponent);value=fmpq(int(sp.numer(co)),int(sp.denom(co)))
            terms[key]=terms.get(key,fmpq(0))+value
    return ctx.from_dict(terms)

def coeff_groups(poly,names):
    """Lex(z,t,parameters) puts each coefficient's terms consecutively."""
    terms=((poly.monomial(i),poly.coefficient(i)) for i in range(len(poly)))
    for key,group in itertools.groupby(terms,lambda mc:(mc[0][1],mc[0][0])):
        pieces=[]
        for mon,co in group:
            factors=[f'({co})']
            factors += [name if power==1 else f'{name}^{power}' for name,power in zip(names[2:],mon[2:]) if power]
            pieces.append('*'.join(factors))
        yield key,'+'.join(pieces)

def main(stage,early_D,timeout,translated=False):
    start=time.monotonic();tag=f'd108_native_stage{stage}'+('_earlyD' if early_D else '')+('_translated' if translated else '')
    record={'tag':tag,'stage':stage,'early_D':early_D,'coefficient_field':'QQ','status':'BUILDING','phases':[]}
    path=OUT/f'{tag}.json'
    def save():path.write_text(json.dumps(record,indent=2,default=str)+'\n')
    def phase(name,**data):
        record['phases'].append({'name':name,'elapsed_seconds':round(time.monotonic()-start,3),**data});save();print(json.dumps(record['phases'][-1]),flush=True)
    maps,res,meta=build(stage,True,normalized=True,early_D=early_D);record['source']=meta
    if translated:
        from translation_backend import audit_and_translate
        maps,translation=audit_and_translate(maps)
        record['translation']=translation;phase('translation_audited',basis_roundtrips=True,h_t1_removed=True)
    targets=set(sp.symbols('target_a target_b target_c target_d target_e'))
    active=targets|set().union(*(e.free_symbols for key in ['h2','B2'] for e in maps[key].values()))
    names=['zz','tt']+sorted(map(str,active));ctx=fmpq_mpoly_ctx.get(tuple(names),ordering='lex');gens=dict(zip(names,ctx.gens()))
    record['division_generator_order']=names;record['division_map']='identity on tt,zz and each declared polynomial parameter; source A3 is retained in the full row ring'
    h=convert(maps['h2'],ctx,names);D=convert(maps['B2'],ctx,names)
    z,t=gens['zz'],gens['tt'];a,b,c,d,e=[gens['target_'+q] for q in 'abcde']
    H=h-b*t**36/6;v=D+(a/3+b**2/18)*t**71
    assert H.leading_coefficient()==1 and H.degrees()[0]==36 and v.degrees()[0]<36
    phase('native_inputs',active_variables=len(names)-2,h_terms=len(H),v_terms=len(v))
    def divide(label,f):
        phase(label+'_begin',dividend_terms=len(f))
        q,r=divmod(f,H)
        assert f-q*H-r==0 and (r.is_zero() or r.degrees()[0]<36)
        phase(label+'_end',quotient_terms=len(q),remainder_terms=len(r))
        return q,r
    U,R=divide('v2',v*v)
    P,R1=divide('vU',v*U)
    Q,R2=divide('vR',v*R)
    W,R3=divide('U2',U*U)
    aa=a+b*b/4;dd=d+b*c/2;p=dd-aa*aa/3;q=e+c*c/4-aa*dd/3+2*aa**3/27
    upper=3*R/4+p*t**142-t*P/8
    digit=Q-R1/8-9*t*W/64
    low=R2-9*t*R3/64+p*t**142*v+q*t**213
    derived_without_C=-b*t**36*D/4+(a*b/12+b**3/54-c/2)*t**107-3*t*U/8
    phase('row_polynomials',upper_terms=len(upper),digit_terms=len(digit),low_terms=len(low),derived_terms=len(derived_without_C))
    full=targets|{sp.Symbol('leader63'),sp.Symbol('Z63'),sp.Symbol('c'),sp.Symbol('Zc')}
    for tab in maps.values():
        for value in tab.values():full|=value.free_symbols
    for _,value in res:full|=value.free_symbols
    fullnames=sorted(map(str,full));record['row_ring_generator_order']=fullnames
    script=OUT/f'{tag}.sing';counts={'source':len(res),'derivedV':0,'upper':0,'digit_face':0,'low':0}
    with script.open('w') as f:
        f.write(f'ring R=0,({",".join(fullnames)}),dp;\noption(redSB);ideal I=0;\n')
        def row(s):f.write('I[size(I)+1]='+s+';\n')
        for _,value in res:row(exprS(value))
        C=dict(maps['A3'])
        for key,value in coeff_groups(derived_without_C,names):
            row('('+value+')+('+exprS(C.pop(key,0))+')');counts['derivedV']+=1
        for value in C.values():row(exprS(value));counts['derivedV']+=1
        for _,value in coeff_groups(upper,names):row(value);counts['upper']+=1
        target={q+21:str(sp.binomial(6,q)) for q in range(7)}
        for (r,q),value in coeff_groups(digit,names):
            if r>150:continue
            rhs=target.pop(q,None) if r==150 else None
            row('('+value+')'+(f'-({rhs})*leader63' if rhs is not None else ''));counts['digit_face']+=1
        for value in target.values():row(f'-({value})*leader63');counts['digit_face']+=1
        for (r,q),value in coeff_groups(low,names):
            if r<151:row(value);counts['low']+=1
        row('Z63*leader63-1');row('Zc*c-1')
        f.write('print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");\n')
        f.write('ideal neg=leader63,Z63*leader63-1;ideal pos=leader63-1,Z63*leader63-1;print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;\n')
    record['row_counts']=counts;record['script_sha256']=hashlib.sha256(script.read_bytes()).hexdigest();phase('emitted',script_bytes=script.stat().st_size)
    with (OUT/f'{tag}.out').open('w') as out:
        process=subprocess.Popen(['Singular','-q',str(script)],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
        try:rc=process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGTERM);rc=process.wait();record['status']='COMPUTE_BOUND_OPEN'
    log=(OUT/f'{tag}.out').read_text();errors=[line for line in log.splitlines() if line.lstrip().startswith('?') or 'error occurred' in line]
    record['cas']={'returncode':rc,'errors':errors[:30],'log_sha256':hashlib.sha256(log.encode()).hexdigest()}
    if not errors and 'BEGIN_RESULT\n' in log and 'END_RESULT' in log:
        values=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines();record['cas']['result']=values;record['status']='UNIT' if values[0]=='0' else 'NONUNIT_NOT_POINT'
    elif 'memory' in log.lower():record['status']='MEMORY_BOUND_OPEN'
    elif record['status']!='COMPUTE_BOUND_OPEN':record['status']='CAS_ERROR_OPEN'
    phase('finished',status=record['status'])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=int,default=8);ap.add_argument('--early-D',action='store_true');ap.add_argument('--translated',action='store_true');ap.add_argument('--timeout',type=int,default=1800);args=ap.parse_args();main(args.stage,args.early_D,args.timeout,args.translated)
