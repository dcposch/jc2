#!/usr/bin/env python3
"""Collect bounded computation facts and mechanically bind per-case artifacts."""
import datetime,hashlib,json,re
from pathlib import Path
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for stage in range(9):
    item={'stage':stage}
    for suffix,label in [('', 'normalized12GiB'),('_m24','normalized24GiB')]:
        p=D/f'd108_totalface_stage{stage}{suffix}.json'
        if not p.exists():item[label]={'status':'NOT_STARTED'};continue
        a=json.loads(p.read_text());r=a.get('run',{})
        item[label]={'status':a.get('verdict'),'elapsed_seconds':r.get('elapsed_seconds'),
          'last_marker':r.get('last_progress_marker'),'metadata':p.name,'metadata_sha256':sha(p)}
    p=D/f'd108_circuit_stage{stage}_translated_strongfront.circuit.json'
    if not p.exists():item['coefficient_circuit']={'status':'NOT_STARTED'}
    else:
        a=json.loads(p.read_text());script=D/f'd108_circuit_stage{stage}_translated_strongfront.sing'
        inp=D/f'd108_remainder_stage{stage}_translated_strongfront.input.json';sm=D/f'd108_remainder_stage{stage}_translated_strongfront.json'
        logfile=D/f'd108_circuit_stage{stage}_translated_strongfront.circuit.out';log=logfile.read_text() if logfile.exists() else ''
        match=re.search(r'ALL_ROWS_PARSED\n(\d+)\n',log)
        parsed_count=int(match.group(1)) if match else None
        declared_count=sum(a.get('counts',{}).values())
        gens=a.get('ring_generator_order',[])
        checks={'script_hash_matches':script.exists() and sha(script)==a.get('script_sha256'),
          'input_hash_matches':inp.exists() and sha(inp)==a.get('input_sha256'),
          'generators_distinct':len(gens)==len(set(gens)),
          'all_five_target_constants_declared':all('target_'+c in gens for c in 'abcde'),
          'leaders_and_localizers_declared':all(v in gens for v in ['leader63','Z63','c','Zc']),
          'all_declared_rows_parsed':parsed_count==declared_count if parsed_count is not None else False}
        source=json.loads(sm.read_text()) if sm.exists() else {}
        item['coefficient_circuit']={'status':a.get('status'),'row_counts':a.get('counts'),
          'total_rows':declared_count,'parsed_rows':parsed_count,'variables':len(gens),
          'script_bytes':script.stat().st_size if script.exists() else None,
          'source_raw_rows':source.get('source_rows'),'source_pivots':source.get('source_pivots'),
          'source_residual':source.get('source_residual'),'jet0_free':source.get('jet0_free'),
          'checks':checks,'source_metadata':sm.name,'source_metadata_sha256':sha(sm) if sm.exists() else None,
          'metadata':p.name,'metadata_sha256':sha(p),'script_sha256':sha(script) if script.exists() else None,
          'last_phase':a.get('phases',[])[-1] if a.get('phases') else None,'cas':a.get('cas')}
    rows.append(item)
meanfree=[]
for stage in range(9):
    p=D/f'd108_meanfree_circuit_stage{stage}_strongfront.circuit.json'
    if not p.exists():meanfree.append({'stage':stage,'status':'NOT_STARTED'});continue
    a=json.loads(p.read_text());script=D/f'd108_meanfree_circuit_stage{stage}_strongfront.sing'
    inp=D/f'd108_meanfree_stage{stage}_strongfront.input.json';sm=D/f'd108_meanfree_stage{stage}_strongfront.map.json'
    logfile=D/f'd108_meanfree_circuit_stage{stage}_strongfront.circuit.out';log=logfile.read_text() if logfile.exists() else ''
    match=re.search(r'ALL_ROWS_PARSED\n(\d+)\n',log);parsed=int(match.group(1)) if match else None
    total=sum(a.get('counts',{}).values());gens=a.get('ring_generator_order',[]);source=json.loads(sm.read_text())
    meanfree.append({'stage':stage,'status':a.get('status'),'row_counts':a.get('counts'),'total_rows':total,
      'parsed_rows':parsed,'variables':len(gens),'script_bytes':script.stat().st_size if script.exists() else None,
      'checks':{'script_hash_matches':script.exists() and sha(script)==a.get('script_sha256'),
        'input_hash_matches':inp.exists() and sha(inp)==a.get('input_sha256'),'generators_distinct':len(gens)==len(set(gens)),
        'all_five_targets_and_mean_declared':all(v in gens for v in ['target_'+c for c in 'abcde']+['minor_mean']),
        'leaders_and_localizers_declared':all(v in gens for v in ['leader63','Z63','c','Zc']),
        'all_declared_rows_parsed':parsed==total if parsed is not None else False,
        'mean_free_and_arc_unchanged':source.get('mean_free') and source.get('arc_unchanged')},
      'source_raw_rows':source.get('source_rows'),'source_pivots':source.get('source_pivots'),
      'source_residual':source.get('source_residual'),'metadata':p.name,'metadata_sha256':sha(p),
      'source_metadata':sm.name,'source_metadata_sha256':sha(sm),'script_sha256':sha(script) if script.exists() else None,
      'last_phase':a.get('phases',[])[-1] if a.get('phases') else None,'cas':a.get('cas')})
selected=[]
for result_path in sorted((D/'selected').glob('*/result.json')):
    result=json.loads(result_path.read_text());case=result_path.parent
    script=case/'augmented.sing';base=case/'base.sing';base_meta=case/'base.circuit.json'
    bm=json.loads(base_meta.read_text()) if base_meta.exists() else {}
    selected.append({'case':case.name,'result':result,'result_sha256':sha(result_path),
      'base_script_sha256':sha(base) if base.exists() else None,
      'base_metadata_sha256':sha(base_meta) if base_meta.exists() else None,
      'total_rows':sum(bm.get('counts',{}).values()),'variables':len(bm.get('ring_generator_order',[])),
      'script_hash_matches':script.exists() and sha(script)==result.get('script_sha256')})
record={'collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'coefficient_field':'QQ','rows':rows,'supplementary_mean_free_rows':meanfree,'selected':selected,
 'classification':'A timeout or resource failure is OPEN; NONUNIT_NOT_POINT is not a necessary-chart survivor. No unrestricted unit or point is inferred from controls.',
 'primary_schedule':'all stages0–8 full normalized characteristic degree/top rows, full source rows transported by rational pivots',
 'circuit_schedule':'all stages0–8 stronger audited radical front consequences; invertible translation retains jet0; all polynomial coefficient graph and target rows'}
(D/'schedule-summary.json').write_text(json.dumps(record,indent=2)+'\n')
for row in rows:
    c=row['coefficient_circuit'];print(row['stage'],row['normalized12GiB']['status'],row['normalized24GiB']['status'],c['status'],c.get('total_rows'),c.get('parsed_rows'))
for row in meanfree:print('meanfree',row['stage'],row['status'],row.get('total_rows'),row.get('parsed_rows'))
