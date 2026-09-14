#!/usr/bin/env python3
"""Exact-Q coefficient circuit; all graph and target-subtracted rows explicit.

Polynomial graph variables prevent expanded parameter products.  Every graph
variable has a monic defining equation; projection is an isomorphism to the
full normalized characteristic ideal.  No source coordinate is specialized.
"""
import argparse,hashlib,itertools,json,os,re,signal,subprocess,sys,time
from pathlib import Path
from flint import fmpq,fmpq_mpoly,fmpq_mpoly_ctx
def coeff_groups(poly,names):
    terms=((poly.monomial(i),poly.coefficient(i)) for i in range(len(poly)))
    for key,group in itertools.groupby(terms,lambda mc:(mc[0][1],mc[0][0])):
        pieces=[]
        for mon,co in group:
            factors=[f'({co})']
            factors += [name if power==1 else f'{name}^{power}' for name,power in zip(names[2:],mon[2:]) if power]
            pieces.append('*'.join(factors))
        yield key,'+'.join(pieces)


def main(input_path,out_path,timeout):
    start=time.monotonic();inp=json.loads(input_path.read_text())
    k,target=inp['k'],inp['target'];depth=6*k-2-target
    names=['zz','tt']+list(inp['names']);assert len(names)==len(set(names))
    ctx=fmpq_mpoly_ctx.get(tuple(names),ordering='lex')
    record={'input':str(input_path),'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
      'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'field':'QQ','status':'BUILDING','graph_type':'monic polynomial coefficient graph, exact projection isomorphism',
      'target_depth':depth,'phases':[]}
    meta=out_path.with_suffix('.circuit.json');definitions={};body_path=out_path.with_suffix('.rows.tmp')
    def phase(name,**data):
        item={'name':name,'seconds':round(time.monotonic()-start,3),**data};record['phases'].append(item)
        meta.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(item),flush=True)
    for name,expression in inp.get('predefinitions',[]):
        for old,replacement in definitions.items():expression=re.sub(r'\b'+re.escape(old)+r'\b','('+replacement+')',expression)
        definitions[name]=expression
    def parse(expression):
        for name,replacement in definitions.items():expression=re.sub(r'\b'+re.escape(name)+r'\b','('+replacement+')',expression)
        return fmpq_mpoly(expression,ctx=ctx)
    def table(expression):return {pos:value for pos,value in coeff_groups(parse(expression),names)}
    g=dict(zip(names,ctx.gens()));t=g['tt'];a,b,c,d,e=[g['target_'+v] for v in 'abcde']
    h=parse(inp['h_expr']);D=parse(inp['D_expr']);C=parse(inp['C_expr'])
    H=h-b*t**k/6;v=D+(a/3+b*b/18)*t**(2*k-1)
    V=C-b*t**k*D/4+(a*b/12+b**3/54-c/2)*t**(3*k-1);U=(8*V/3)//t
    assert t*U==8*V/3
    aa=a+b*b/4;dd=d+b*c/2;p=dd-aa*aa/3;q=e+c*c/4-aa*dd/3+2*aa**3/27
    newnames=[];counts={'source':0,'graph_h':0,'lift':0,'R_high':0,'R_low_graph':0,'H2_graph':0,'vU_graph':0,'Q':0,'localizers':0}
    out_path.parent.mkdir(parents=True,exist_ok=True)
    with body_path.open('w') as body:
        first=True
        def row(expression,kind):
            nonlocal first
            if not first:body.write(',\n')
            first=False;body.write('('+expression+')');counts[kind]+=1
        for expression in inp['residual_strings']:row(expression,'source')
        if inp.get('graph_h_expr'):
            for _,expression in coeff_groups(h-parse(inp['graph_h_expr']),names):row(expression,'graph_h')
        def lift(tab,label,kind='lift'):
            result={}
            for (r,z),expression in sorted(tab.items()):
                try:constant=fmpq(expression.strip('()'))
                except (ValueError,TypeError):constant=None
                if constant is not None:result[(r,z)]=f'({constant})';continue
                name=f'cx{label}_{r}_{z}';assert name not in names and name not in newnames
                newnames.append(name);row(name+'-('+expression+')',kind);result[(r,z)]=name
            return result
        Htab=lift(dict(coeff_groups(H,names)),'H');vtab=lift(dict(coeff_groups(v,names)),'v');Utab=lift(dict(coeff_groups(U,names)),'U')
        phase('input_lifts',H=len(Htab),v=len(vtab),U=len(Utab),variables=len(newnames))
        def addterm(result,key,term):result.setdefault(key,[]).append(term)
        def mul(left,right,maxr=None):
            result={}
            for (r,z),co in left.items():
                for (s,w),cv in right.items():
                    if maxr is None or r+s<=maxr:addterm(result,(r+s,z+w),f'({co})*({cv})')
            return {key:'+'.join(value) for key,value in result.items()}
        raw=mul(vtab,vtab)
        for key,value in mul(Utab,Htab).items():raw[key]=raw.get(key,'0')+'-('+value+')'
        low={}
        for pos,expression in raw.items():
            if pos[1]>=k:row(expression,'R_high')
            else:low[pos]=expression
        Rtab=lift(low,'R','R_low_graph');del raw,low
        phase('R_graph',positions=len(Rtab),counts=counts,body_bytes=body.tell())
        # At each product only terms which can reach the requested t-band are
        # retained. All exponents are nonnegative, so this is an exact quotient.
        minR=min((r for r,z in Rtab),default=depth+1)
        HH=lift(mul(Htab,Htab,max(depth-minR,depth-(4*k-2))),'HH','H2_graph')
        vU=lift(mul(vtab,Utab,depth-1),'vU','vU_graph')
        phase('product_graphs',HH=len(HH),vU=len(vU),variables=len(newnames),body_bytes=body.tell())
        Q={}
        def merge(tab,factor='1',shift=0):
            for (r,z),expression in tab.items():
                if r+shift<=depth:addterm(Q,(r+shift,z),f'({factor})*({expression})')
        merge(mul(Rtab,HH,depth),'3/4')
        phase('RH2_collected',Q_positions=len(Q))
        merge(mul(vU,Htab,depth-1),'-1/8',1)
        merge(mul(vtab,Rtab,depth-1),'1',1)
        merge(mul(Utab,Utab,depth-2),'-9/64',2)
        # p and q terms often lie beyond this band, but are emitted by the
        # same exact support calculation rather than silently discarded.
        pt=dict(coeff_groups(p,names));qt=dict(coeff_groups(q,names))
        merge(mul(pt,HH,depth-(4*k-2)),'1',4*k-2)
        merge(mul(pt,vtab,depth-(4*k-1)),'1',4*k-1)
        merge(qt,'1',6*k-2)
        H0=h.subs({'tt':0})
        targetpoly=g[inp.get('leader_name') or f'leader{target}']*t**depth*parse(inp['face_expr'])*H0
        merge(dict(coeff_groups(targetpoly,names)),'-1')
        for _,parts in sorted(Q.items()):row('+'.join(parts),'Q')
        leader=inp.get('leader_name') or f'leader{target}';inverse=inp.get('leader_inverse') or f'Z{target}'
        row(f'{inverse}*{leader}-1','localizers')
        for expression in inp.get('localizer_rows',('Zc*c-1',)):row(expression,'localizers')
        phase('full_rows_emitted',counts=counts,body_bytes=body.tell())
    allnames=list(inp['names'])+newnames;assert len(allnames)==len(set(allnames))
    record['ring_generator_order']=allnames;record['counts']=counts
    with out_path.open('w') as out:
        out.write('ring R=0,('+','.join(allnames)+'),dp;\nideal I=\n')
        with body_path.open() as body:
            while chunk:=body.read(1024*1024):out.write(chunk)
        out.write(';\nprint("ALL_ROWS_PARSED");print(size(I));print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");\n')
        out.write(f'ideal neg={leader},{inverse}*{leader}-1;ideal pos={leader}-1,{inverse}*{leader}-1;print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;\n')
    body_path.unlink();record['script_sha256']=hashlib.sha256(out_path.read_bytes()).hexdigest();record['status']='EMITTED_NOT_DECIDED';phase('script_complete',bytes=out_path.stat().st_size,variables=len(allnames))
    if timeout<=0:return
    logfile=out_path.with_suffix('.circuit.out')
    with logfile.open('w') as log:
        proc=subprocess.Popen(['Singular','-q',str(out_path)],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:rc=proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGTERM);rc=proc.wait();record['status']='COMPUTE_BOUND_OPEN'
    text=logfile.read_text();errors=[s for s in text.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s]
    record['cas']={'returncode':rc,'errors':errors[:20],'log_sha256':hashlib.sha256(text.encode()).hexdigest()}
    controls=text.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines() if 'BEGIN_CONTROLS\n' in text and 'END_CONTROLS' in text else []
    script_unchanged=record['script_sha256']==hashlib.sha256(out_path.read_bytes()).hexdigest()
    record['cas'].update({'controls':controls,'script_unchanged':script_unchanged})
    if rc==0 and not errors and controls==['0','1'] and script_unchanged and 'ALL_ROWS_PARSED' in text and 'BEGIN_RESULT\n' in text and 'END_RESULT' in text:
        values=text.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines();record['cas']['result']=values;record['status']='UNIT' if values[0]=='0' else 'NONUNIT_NOT_POINT'
    elif 'memory' in text.lower():record['status']='MEMORY_BOUND_OPEN'
    elif record['status']!='COMPUTE_BOUND_OPEN':record['status']='CAS_ERROR_OPEN'
    phase('finished',status=record['status'])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);ap.add_argument('--timeout',type=int,default=1800);a=ap.parse_args();main(a.input,a.out,a.timeout)
