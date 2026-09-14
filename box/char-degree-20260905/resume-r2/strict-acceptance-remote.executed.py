__name__="strict_acceptance_remote"
#!/usr/bin/env python3
"""Independent conservative output acceptance; no source-chart adequacy inference."""
import hashlib,json,re,subprocess,time
from pathlib import Path
MARKERS=('ALL_ROWS_PARSED','BEGIN_GB','END_GB','BEGIN_RESULT','END_RESULT','BEGIN_CONTROLS','END_CONTROLS')
def digest(b):return hashlib.sha256(b).hexdigest()
def inspect_log(text,rc,hash_bound=True,expected_rows=None):
 lines=text.splitlines();errors=[s for s in lines if re.search(r'^\s*\?|error occurred|singular error|syntax error|fatal error|segmentation fault|^\s*halt\b',s,re.I)]
 counts={m:lines.count(m) for m in MARKERS};reasons=[]
 if rc!=0:reasons.append('returncode_not_zero_or_unrecorded')
 if not hash_bound:reasons.append('script_or_output_not_hash_bound')
 if errors:reasons.append('parser_cas_or_termination_diagnostic')
 if any(v!=1 for v in counts.values()):reasons.append('required_unique_marker_missing_or_duplicate')
 values=[];controls=[];row_count=None
 if all(v==1 for v in counts.values()):
  positions=[lines.index(m) for m in MARKERS]
  if positions!=sorted(positions):reasons.append('marker_order_invalid')
  values=lines[positions[3]+1:positions[4]];controls=lines[positions[5]+1:positions[6]]
  try:row_count=int(lines[positions[0]+1])
  except (ValueError,IndexError):reasons.append('parsed_row_count_missing_or_invalid')
  if row_count is not None and (row_count<1 or expected_rows is not None and row_count!=expected_rows):reasons.append('parsed_row_count_wrong')
  if len(values)!=3 or values[0] not in ('0','1') or not all(re.fullmatch(r'-?\d+',v) for v in values[1:]):reasons.append('result_vector_invalid')
  elif int(values[2])<1 or (values[0]=='0' and (values[1]!='-1' or values[2]!='1')) or (values[0]=='1' and int(values[1])<0):reasons.append('result_vector_inconsistent')
  if controls!=['0','1']:reasons.append('localizer_control_vector_wrong')
 verdict='OPEN_REJECTED_OR_INCOMPLETE' if reasons else ('COMPLETE_CLEAN_UNIT_CANDIDATE_NEEDS_REPLAY' if values[0]=='0' else 'COMPLETE_CLEAN_PROPER_COMPUTATION')
 return {'verdict':verdict,'returncode':rc,'markers':counts,'parser_cas_or_termination_diagnostics':errors[:10],'result':values,'controls':controls,'parsed_row_count':row_count,'reasons':reasons,'log_sha256':digest(text.encode())}

def main():
 out=Path(__file__).resolve().parent
 clean='ALL_ROWS_PARSED\n2\nBEGIN_GB\nEND_GB\nBEGIN_RESULT\n1\n0\n2\nEND_RESULT\nBEGIN_CONTROLS\n0\n1\nEND_CONTROLS\n'
 tests=[('clean_proper',clean,0,True,2,True),('clean_unit',clean.replace('1\n0\n2\nEND_RESULT','0\n-1\n1\nEND_RESULT'),0,True,2,True)]
 for marker in MARKERS:tests.append(('missing_'+marker,clean.replace(marker+'\n',''),0,True,2,False))
 tests.extend([
 ('truncated_gb',clean.split('END_GB')[0],0,True,2,False),
 ('parser_error_rc0','   ? poly ^ number failed\n'+clean,0,True,2,False),
 ('generic_error_rc0','error occurred in procedure emit\n'+clean,0,True,2,False),
 ('memory_error_rc0',clean+'Singular error: no more memory\n',0,True,2,False),
 ('wrong_control_vector',clean.replace('BEGIN_CONTROLS\n0\n1','BEGIN_CONTROLS\n1\n0'),0,True,2,False),
 ('missing_control_value',clean.replace('BEGIN_CONTROLS\n0\n1','BEGIN_CONTROLS\n0'),0,True,2,False),
 ('nonzero_rc',clean,1,True,2,False),('unrecorded_rc',clean,None,True,2,False),
 ('hash_mismatch',clean,0,False,2,False),('wrong_row_count',clean,0,True,3,False),
 ('duplicated_marker',clean+'END_RESULT\n',0,True,2,False),
 ('invalid_reduce_one',clean.replace('BEGIN_RESULT\n1','BEGIN_RESULT\n2'),0,True,2,False),
 ('extra_result_value',clean.replace('END_RESULT','3\nEND_RESULT'),0,True,2,False),
 ('wrong_marker_order',clean.replace('END_GB\nBEGIN_RESULT','BEGIN_RESULT\nEND_GB'),0,True,2,False)])
 results=[]
 for name,text,rc,bound,rows,expected in tests:
  r=inspect_log(text,rc,bound,rows);accepted=r['verdict'].startswith('COMPLETE_CLEAN_');assert accepted==expected,(name,r)
  results.append({'case':name,'expected_complete_clean':expected,'check':'PASS',**r})
 actual=[]
 for name,prefix,unit in [('clean_proper','',False),('clean_unit','',True),('malformed_parser_rc0','poly malformed=b^2/4;\n',False)]:
  script='ring R=0,(b,z),dp;\n'+prefix+'ideal I='+('b,z*b-1' if unit else 'b-1,z*b-1')+';\nprint("ALL_ROWS_PARSED");print(size(I));print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");ideal neg=b,z*b-1;ideal pos=b-1,z*b-1;print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;\n'
  start=time.monotonic();p=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,timeout=15);log=p.stdout+p.stderr
  (out/('acceptance-toy-'+name+'.sing')).write_text(script);(out/('acceptance-toy-'+name+'.out')).write_text(log)
  r=inspect_log(log,p.returncode,True,2);assert r['verdict'].startswith('COMPLETE_CLEAN_')==(not prefix),(name,r)
  actual.append({'case':name,'script_sha256':digest(script.encode()),'wall_seconds':round(time.monotonic()-start,4),'check':'PASS',**r})
 inherited=json.loads((out/'audit-99.json').read_text());harvest_controls=[]
 for c in inherited['backend_controls']:
  rr=c['replay'];r=inspect_log(rr['output'],rr['returncode'],rr['output_sha256']==digest(rr['output'].encode()))
  assert r['verdict'].startswith('COMPLETE_CLEAN_');harvest_controls.append({'case':c['case'],**r})
 record={'scope':'Independent acceptance-parser controls and read-only classification of existing toy replay outputs. No production Groebner calculation rerun; no source-chart claim.','status':'PASS','control_script_sha256':digest(Path(__file__).read_bytes()),'synthetic_cases':results,'actual_toy_singular':actual,'existing_toy_replay_classification':harvest_controls}
 (out/'strict-acceptance-controls.json').write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps({'status':'PASS','synthetic_count':len(results),'actual_toys':[{k:r[k] for k in ('case','returncode','verdict')} for r in actual],'existing_toy_replays':len(harvest_controls)}))
if __name__=='__main__':main()

import datetime
ROOT=Path('/home/ubuntu/jc2/box/char-degree-20260905')
def sha_path(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
def readj(p):return json.loads(p.read_text())
def run_record(metadata,log,script,category,base_metadata=None):
 m=readj(metadata); mm=readj(base_metadata) if base_metadata else m;cas=m if base_metadata else m.get('cas',{})
 before=log.stat() if log.exists() else None;raw=log.read_bytes() if log.exists() else b'';text=raw.decode('utf8','replace');after=log.stat() if log.exists() else None
 loghash=hashlib.sha256(raw).hexdigest();scripthash=sha_path(script) if script.exists() else None
 script_bound=scripthash==m.get('script_sha256');output_bound=loghash==cas.get('log_sha256')
 unchanged=before is not None and (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns)
 result=inspect_log(text,cas.get('returncode'),script_bound and output_bound and unchanged,sum(mm['counts'].values()))
 return {'category':category,'metadata':str(metadata.relative_to(ROOT)),'metadata_sha256':sha_path(metadata),'raw_status':m.get('status'),'output':str(log.relative_to(ROOT)),'output_bytes':len(raw),'output_sha256':loghash,'output_matches_receipt':output_bound,'output_stable_during_read':unchanged,'script_sha256':scripthash,'script_matches_receipt':script_bound,'expected_rows':sum(mm['counts'].values()),'acceptance':result}
records=[]
for metadata in sorted((ROOT/'g9966/circuit-runs').glob('*/augmented.circuit.json')):
 records.append(run_record(metadata,metadata.with_suffix('.out'),metadata.with_suffix('').with_suffix('.sing'),'99 schedule'))
for metadata in sorted((ROOT/'d108').glob('d108*circuit_stage*.circuit.json')):
 records.append(run_record(metadata,metadata.with_suffix('.out'),metadata.with_suffix('').with_suffix('.sing'),'D108 schedule'))
for base,pattern,category in [(ROOT/'g9966','circuit-selected/*/result.json','99 selected'),(ROOT/'d108','selected/*/result.json','D108 selected')]:
 for metadata in sorted(base.glob(pattern)):
  m=readj(metadata);script=Path(m['script']);script=script if script.is_absolute() else (ROOT.parents[1]/script if script.parts[0]=='box' else base/script)
  records.append(run_record(metadata,metadata.parent/'singular.out',script,category,metadata.parent/'base.circuit.json'))
print(json.dumps({'audit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Independent read-only acceptance parsing of actual worker output bytes; no solver rerun and no source-chart adequacy inference. Missing completion, parser/CAS/termination errors, rc!=0, or missing custody cannot become unit/proper.','worker':'172.30.0.40','counts':{'records':len(records),'complete_clean_candidates':sum(r['acceptance']['verdict'].startswith('COMPLETE_CLEAN_') for r in records)},'records':records},indent=2))
