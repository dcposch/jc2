#!/usr/bin/env python3
"""D108 full-row no-division experiment using the independently audited backend."""
import argparse,hashlib,json,os,signal,subprocess,sys,time
from pathlib import Path
import sympy as sp
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(OUT.parent))
from remainder_backend import script_for
from char_degree_driver import build,exprS
from normalized_backend import normalized_polyS

def main(stage,translated,timeout,strong_front=False,emit_only=False):
    start=time.monotonic();maps,res,meta=build(stage,True,normalized=True,early_D=not strong_front,strong_front=strong_front)
    if translated:
        from translation_backend import audit_and_translate
        maps,translation=audit_and_translate(maps);meta['translation']=translation
    names=set(sp.symbols('target_a target_b target_c target_d target_e leader63 Z63 c Zc'))
    for table in maps.values():
        for expr in table.values():names|=expr.free_symbols
    for _,expr in res:names|=expr.free_symbols
    names=sorted(map(str,names));tag=f'd108_remainder_stage{stage}'+('_translated' if translated else '')+('_strongfront' if strong_front else '')
    inputs={'h_expr':normalized_polyS(maps['h2']),'D_expr':normalized_polyS(maps['B2']),'C_expr':normalized_polyS(maps['A3']),
       'residual_strings':[exprS(v) for _,v in res],'names':names,'k':36,'target':63,'face_expr':'zz^21*(1+zz)^6'}
    input_path=OUT/f'{tag}.input.json';input_path.write_text(json.dumps(inputs,indent=2)+'\n')
    script=script_for(**inputs);path=OUT/f'{tag}.sing';path.write_text(script)
    meta.update({'tag':tag,'method':'full remainder identity; no expanded monic division','script_sha256':hashlib.sha256(script.encode()).hexdigest(),
      'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),'coefficient_field':'QQ','ring_generator_order':['zz','tt']+names,
      'Q_normalizer_degree':214,'target_depth':151,'full_target':'leader63*tt^151*zz^49*(1+zz)^14',
      'verdict':'EMITTED_NOT_DECIDED','build_seconds':round(time.monotonic()-start,3)})
    jpath=OUT/f'{tag}.json';jpath.write_text(json.dumps(meta,indent=2,default=str)+'\n')
    print(json.dumps({'tag':tag,'emitted':len(script),'build_seconds':meta['build_seconds']}),flush=True)
    if emit_only:return
    t0=time.monotonic()
    with (OUT/f'{tag}.out').open('w') as out:
        proc=subprocess.Popen(['Singular','-q',str(path)],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
        timed=False
        try:code=proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:code=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);code=proc.wait()
    log=(OUT/f'{tag}.out').read_text();errors=[s for s in log.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s]
    run={'timeout':timed,'returncode':code,'elapsed_seconds':round(time.monotonic()-t0,3),'errors':errors[:30],
       'last_progress_marker':next((s for s in reversed(log.splitlines()) if s.startswith(('BEGIN_','END_','CHAR_'))),None),
       'log_sha256':hashlib.sha256(log.encode()).hexdigest()}
    if not errors and 'BEGIN_RESULT\n' in log and 'END_RESULT' in log:
        vals=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines();run.update({'reduce_one':vals[0],'dimension':vals[1],'gb_size':vals[2]});meta['verdict']='UNIT' if vals[0]=='0' else 'NONUNIT_NOT_POINT'
    else:meta['verdict']='MEMORY_BOUND_OPEN' if ('no more memory' in log.lower() or 'unable to allocate memory' in log.lower()) else ('CAS_ERROR_OPEN' if errors else 'COMPUTE_BOUND_OPEN' if timed else 'PROCESS_ERROR_OPEN')
    meta['run']=run;jpath.write_text(json.dumps(meta,indent=2,default=str)+'\n');print(json.dumps({'tag':tag,'verdict':meta['verdict'],'run':run}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=int,default=8);ap.add_argument('--translated',action='store_true');ap.add_argument('--strong-front',action='store_true');ap.add_argument('--emit-only',action='store_true');ap.add_argument('--timeout',type=int,default=1800);a=ap.parse_args();main(a.stage,a.translated,a.timeout,a.strong_front,a.emit_only)
