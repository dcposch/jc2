#!/usr/bin/env python3
"""Native exact-Q remainder products and streamed coefficient-row emission.

Avoid Singular coef() and repeated ideal resizing. No division by H occurs.
Indexed monomial iteration avoids allocating all Python exponent tuples.
"""
import argparse,hashlib,json,os,re,signal,subprocess,sys,time
from pathlib import Path
from flint import fmpq_mpoly,fmpq_mpoly_ctx
HERE=Path(__file__).resolve().parent
from native_flint_stage import coeff_groups

def select(poly,ctx,predicate,chunk=2048):
    result=ctx.constant(0);terms={}
    for i in range(len(poly)):
        mon=poly.monomial(i)
        if predicate(mon):terms[mon]=poly.coefficient(i)
        if len(terms)>=chunk:
            result.iadd(ctx.from_dict(terms));terms={}
    if terms:result.iadd(ctx.from_dict(terms))
    return result

def main(input_path,out_path,timeout):
    start=time.monotonic();inp=json.loads(input_path.read_text())
    if 'h_expr' not in inp:
        sys.path.insert(0,str(HERE.parent/'review'))
        from active_ring_backend import from_g9966_input
        inp=from_g9966_input(input_path)
    k,target=inp['k'],inp['target'];degree=6*k-2;depth=degree-target
    leader=inp.get('leader_name') or f'leader{target}';inverse=inp.get('leader_inverse') or f'Z{target}'
    names=['zz','tt']+list(inp['names']);ctx=fmpq_mpoly_ctx.get(tuple(names),ordering='lex');g=dict(zip(names,ctx.gens()))
    record={'input':str(input_path),'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
       'coefficient_field':'QQ','ring_generator_order':names,'status':'RUNNING','phases':[],'depth':depth,'normalizer_degree':degree}
    meta=out_path.with_suffix('.native.json');log_path=out_path.with_suffix('.native.out')
    def phase(name,**data):
        item={'name':name,'elapsed_seconds':round(time.monotonic()-start,3),**data};record['phases'].append(item)
        meta.write_text(json.dumps(record,indent=2,default=str)+'\n');print(json.dumps(item),flush=True)
    definitions={}
    for name,expression in inp.get('predefinitions',[]):
        for old,replacement in definitions.items():expression=re.sub(r'\b'+re.escape(old)+r'\b','('+replacement+')',expression)
        definitions[name]=expression
    def parse(expression):
        for name,replacement in definitions.items():expression=re.sub(r'\b'+re.escape(name)+r'\b','('+replacement+')',expression)
        return fmpq_mpoly(expression,ctx=ctx)
    h,D,C=[parse(inp[name]) for name in ['h_expr','D_expr','C_expr']]
    t=g['tt'];a,b,c,d,e=[g['target_'+name] for name in 'abcde']
    H=h-b*t**k/6;v=D+(a/3+b*b/18)*t**(2*k-1)
    V=C-b*t**k*D/4+(a*b/12+b**3/54-c/2)*t**(3*k-1)
    U=(8*V/3)//t;assert t*U==8*V/3
    aa=a+b*b/4;dd=d+b*c/2;p=dd-aa*aa/3;q=e+c*c/4-aa*dd/3+2*aa**3/27
    phase('inputs',h_terms=len(H),v_terms=len(v),U_terms=len(U),parameters=len(names)-2)
    Rraw=v*v-U*H;phase('Rraw',terms=len(Rraw))
    RR=select(Rraw,ctx,lambda mon:mon[0]<k);phase('Rlow',terms=len(RR))
    counts={'source':len(inp['residual_strings']),'graph_h':0,'R_high':0,'Q':0}
    out_path.parent.mkdir(parents=True,exist_ok=True)
    with out_path.open('w') as f:
        f.write(f'ring R=0,({",".join(inp["names"])}),dp;\nideal I=\n')
        first=True
        def row(expression):
            nonlocal first
            if not first:f.write(',\n')
            first=False;f.write('('+expression+')')
        for expression in inp['residual_strings']:row(expression)
        if inp.get('graph_h_expr'):
            # h_expr contains independent coefficient generators; the optional
            # graph is an exact polynomial extension, with every old tower
            # coefficient equation retained in the full declared ring.
            graph=h-parse(inp['graph_h_expr'])
            for _,expression in coeff_groups(graph,names):
                row(expression);counts['graph_h']+=1
            phase('h_graph_rows_emitted',graph_terms=len(graph),rows=counts['graph_h'])
            del graph
        for (r,z),expression in coeff_groups(Rraw,names):
            if z>=k:row(expression);counts['R_high']+=1
        if first:f.write('0')
        f.write(';\nprint("R_ROWS_PARSED");\n')
        f.flush();phase('R_rows_emitted',counts=counts,script_bytes=f.tell())
        del Rraw
        def jet(poly):return select(poly,ctx,lambda mon:mon[1]<=depth)
        def product(label,left,right):
            phase(label+'_begin',left_terms=len(left),right_terms=len(right))
            ans=jet(left*right);phase(label+'_end',terms=len(ans));return ans
        HH=H*H;phase('H2',terms=len(HH))
        Q=3*product('RH2',RR,HH)/4
        term=product('vU',v,U);term=product('vUH',term,H);Q.isub(jet(t*term/8));del term
        term=product('vR',v,RR);Q.iadd(jet(t*term));del term
        term=product('U2',U,U);Q.isub(jet(9*t*t*term/64));del term
        Q.iadd(jet(p*t**(4*k-2)*HH+p*t**(4*k-1)*v+q*t**(6*k-2)))
        H0=select(h,ctx,lambda mon:mon[1]==0)
        Q.isub(g[leader]*t**depth*parse(inp['face_expr'])*H0)
        phase('Q_complete',terms=len(Q))
        f.write('ideal Qrows=\n');first=True
        for _,expression in coeff_groups(Q,names):row(expression);counts['Q']+=1
        if first:f.write('0')
        f.write(';\nI=I,Qrows;kill Qrows;\n')
        f.write(f'I=I,{inverse}*{leader}-1')
        for expression in inp.get('localizer_rows',('Zc*c-1',)):f.write(','+expression)
        f.write(';\nprint("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");\n')
        f.write(f'ideal neg={leader},{inverse}*{leader}-1;ideal pos={leader}-1,{inverse}*{leader}-1;print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;\n')
    record['counts']=counts;record['script_sha256']=hashlib.sha256(out_path.read_bytes()).hexdigest();phase('full_rows_emitted',counts=counts,script_bytes=out_path.stat().st_size)
    with log_path.open('w') as out:
        proc=subprocess.Popen(['Singular','-q',str(out_path)],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
        try:rc=proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid,signal.SIGTERM);rc=proc.wait();record['status']='COMPUTE_BOUND_OPEN'
    log=log_path.read_text();errors=[line for line in log.splitlines() if line.lstrip().startswith('?') or 'error occurred' in line]
    record['cas']={'returncode':rc,'errors':errors[:30],'log_sha256':hashlib.sha256(log.encode()).hexdigest()}
    if not errors and 'BEGIN_RESULT\n' in log and 'END_RESULT' in log:
        values=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines();record['cas']['result']=values;record['status']='UNIT' if values[0]=='0' else 'NONUNIT_NOT_POINT'
    elif 'memory' in log.lower():record['status']='MEMORY_BOUND_OPEN'
    elif record['status']!='COMPUTE_BOUND_OPEN':record['status']='CAS_ERROR_OPEN'
    phase('finished',status=record['status'])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--timeout',type=int,default=1800);a=ap.parse_args();main(a.input,a.out,a.timeout)
