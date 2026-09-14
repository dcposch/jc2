#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib,time
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
fibres={j['stem']:dict(stem=j['stem'],intrinsic_unknowns=j['intrinsic_unknowns'],auxiliary_unknowns=j['auxiliary_unknowns'],graph_solver_variables=j['extended_unknowns']+1,graph_solver_generators=j['total_equations']+1,attempts=[])for j in json.loads((BASE/'ops/circuit-emission.json').read_text())}
for path in sorted((BASE/'fleet').glob('*/*/status.json')):
 st=json.loads(path.read_text());stem=st.get('stem')
 if stem not in fibres:continue
 record={'directory':str(path.parent),'host':st.get('host'),'representation':st.get('mode'),'process_state':st.get('state'),'returncode':st.get('solve_returncode',st.get('returncode')),'source_chart_unknowns':st.get('chart_unknowns',fibres[stem]['intrinsic_unknowns']),'native_or_direct_rows':st.get('rows_count'),'input_sha256':st.get('input_sha256')}
 if record['process_state']=='TRANSPORT_PREFLIGHT_FAILED':record['result']='NO_SOLVER_INVOCATION_TRANSPORT_BLOCKED'
 elif record['process_state']=='BUILD_STOPPED_REDUNDANT':record['result']='EXTRACTION_STOPPED_AFTER_COMPLETE_GRAPH_SOLVE'
 elif record['returncode']==124:record['result']='TIMEOUT_NO_VERDICT'
 elif record['returncode'] is not None:record['result']='NO_CERTIFIED_VERDICT'
 else:record['result']='RUNNING_OR_INCOMPLETE'
 errfiles=list(path.parent.glob('*.g2.stderr'));err=errfiles[0].read_text(errors='replace')if errfiles else''
 if 'Enlarging exponent vector for hash table failed'in err:record['result']='ALLOCATION_FAILURE_NO_VERDICT'
 rss=re.search(r'Maximum resident set size \(kbytes\): (\d+)',err)
 if rss:record['gnu_time_peak_RSS_KiB']=int(rss[1])
 elapsed=re.search(r'Elapsed \(wall clock\) time[^\n]*?: ([0-9:.]+)',err)
 if elapsed:record['gnu_time_elapsed_seconds']=sum(float(x)*60**i for i,x in enumerate(reversed(elapsed[1].split(':'))))
 metas=list(path.parent.glob('*.g2.meta'))
 if metas:
  md=dict(line.split('=',1)for line in metas[0].read_text().splitlines()if'='in line)
  record['invocation_start_utc']=md.get('start_utc');record['invocation_end_utc']=md.get('end_utc');record['solver_binary_sha256']=md.get('msolve_sha256');record['extra_args']=md.get('extra_args');record['watchdog_seconds']=md.get('timeout_seconds')
 live=path.parent/'live-resources.jsonl'
 if live.exists():
  hwm=0;last=None
  for line in live.read_text().splitlines():
   entry=json.loads(line)
   if entry['ssh_rc']:continue
   sample=json.loads(entry['stdout']);last=sample['utc']
   for p in sample['processes']:
    m=re.search(r'^VmHWM:\s*(\d+)',p['status'],re.M)
    if m:hwm=max(hwm,int(m[1]))
  record['maximum_sampled_VmHWM_KiB']=hwm;record['last_resource_sample_utc']=last
 outs=list(path.parent.glob('*.g2.out'))
 if outs:record['output_bytes']=outs[0].stat().st_size
 ps=path.parent/'msolve.status.json'
 if ps.exists():
  parsed=json.loads(ps.read_text());record['parsed_status']=parsed.get('status');record['unit_ideal']=parsed.get('unit_ideal')
  if parsed.get('unit_ideal')is True:record['result']='UNIT_SIGNAL_NEEDS_INDEPENDENT_EXACT_Q'
 fibres[stem]['attempts'].append(record)
result={'snapshot_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'fibres':list(fibres.values()),'exact_Q_production_unit_certificates':0,'production_theorem_kills':0}
(BASE/'ops/final-solve-summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'snapshot_utc':result['snapshot_utc'],'attempt_count':sum(len(x['attempts'])for x in fibres.values()),'unit_signals':[a for f in fibres.values()for a in f['attempts']if a.get('unit_ideal')is True]},indent=2))
