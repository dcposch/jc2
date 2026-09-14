#!/usr/bin/env python3
"""All18 source states -> audited translation gauge -> strongest proved cut.

Full source maps, rational graph maps, all residual rows, all target scalars
and localizers remain in independently hash-bound coordinate inputs.
"""
from pathlib import Path
import argparse,hashlib,json,sys,time
HERE=Path(__file__).resolve().parent
import apply_translation_gauge as GAUGE
import apply_stronger_front as FRONT
from active_ring_backend import from_g9966_input

def invoke(module,args):
 previous=sys.argv;sys.argv=[str(module.__file__)]+list(map(str,args))
 try:module.main()
 finally:sys.argv=previous

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--original',type=Path,required=True)
 ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 records=[];start=time.monotonic();root=HERE.parent
 for stage in range(9):
  for branch in ['delta2','delta52']:
   tag=f'{branch}_stage{stage}';original=a.original/f'{tag}.json'
   gauge=a.out/'gauge'/f'{tag}.json';coordinates=a.out/'coordinates'/f'{tag}.json'
   invoke(GAUGE,['--input',original,'--output',gauge])
   Dcut,Ccut=(29,60) if stage==0 else (30,62)
   proofs=[root/'front-band-lemma.md',root/'cubic-front-improvement.md',
           root/'review/quartic-front-improvement.md',root/'review/quartic_front_control.json']
   if stage:proofs += [root/'stage-specific-front-audit.md',root/'stage-specific-front-audit.json']
   frontargs=['--input',gauge,'--output',coordinates,'--Dcut',Dcut,'--Ccut',Ccut,'--minimum-stage',int(stage>0)]
   for proof in proofs:frontargs+=['--proof',proof]
   invoke(FRONT,frontargs)
   kwargs=from_g9966_input(coordinates);data=json.loads(coordinates.read_text())
   kwargs['source_coordinate_input']={'path':str(coordinates),'sha256':hashlib.sha256(coordinates.read_bytes()).hexdigest(),
       'original_input_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
       'gauge_input_sha256':hashlib.sha256(gauge.read_bytes()).hexdigest(),
       'stage':stage,'branch':branch,'D_cut_inclusive':Dcut,'C_cut_inclusive':Ccut,
       'source_maps_residuals_and_graphs_retained':True}
   args=a.out/f'{tag}.input.json';args.write_text(json.dumps(kwargs,indent=2,sort_keys=True)+'\n')
   meta=data['stronger_characteristic_front']
   records.append({'stage':stage,'branch':branch,'input_path':str(args),
      'input_sha256':hashlib.sha256(args.read_bytes()).hexdigest(),'coordinate_path':str(coordinates),
      'coordinate_sha256':hashlib.sha256(coordinates.read_bytes()).hexdigest(),
      'full_source_generator_count':len(data['full_free_coordinates']),'circuit_ambient_generator_count':len(kwargs['names']),
      'D_cut_inclusive':Dcut,'C_cut_inclusive':Ccut,'rational_pivots':len(meta['Qstar_pivots']),
      'residual_count':len(data['residual_rows'])})
   print('CIRCUIT_INPUT_READY',tag,len(kwargs['names']),flush=True)
 receipt={'status':'PREPARED_REQUIRES_INDEPENDENT_REPLAY','field':'Q','records':records,
   'elapsed_seconds':round(time.monotonic()-start,3),'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (a.out/'preparation.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
