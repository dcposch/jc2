#!/usr/bin/env python3
"""Attach immutable shell-abort evidence, never promote restarted partial CAS."""
import datetime,hashlib,json,re
from pathlib import Path
OUT=Path(__file__).resolve().parent
cases=[('d108_native_stage0_earlyD.json','native-stage0-earlyD.driver.log',32),
 ('d108_native_stage8_earlyD.json','native-stage8-earlyD.driver.log',64),
 ('d108_native_stage8_earlyD_translated.json','native-stage8-earlyD-translated.driver.log',64),
 ('d108_native_remainder_stage8_translated.native.json','native-remainder-stage8-translated.driver.log',48)]
for name,logname,limit in cases:
    path=OUT/name;logpath=OUT/logname
    if not path.exists() or not logpath.exists():continue
    log=logpath.read_text();exit_match=re.search(r'NATIVE_EXIT_CODE=(\d+)',log)
    if not exit_match:continue
    record=json.loads(path.read_text());code=int(exit_match.group(1));requested=re.search(r'Unable to allocate memory \((\d+)\)',log)
    if requested:
        record['status']='MEMORY_BOUND_OPEN'
        record['native_abort']={'exit_code':code,'requested_allocation_bytes':int(requested.group(1)),
          'address_space_limit_gib':limit,'last_recorded_phase':record['phases'][-1]['name'],
          'shell_log':logpath.name,'shell_log_sha256':hashlib.sha256(log.encode()).hexdigest(),
          'collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'mathematical_verdict':'OPEN; full characteristic ideal not emitted, no point decision'}
        path.write_text(json.dumps(record,indent=2,default=str)+'\n')
        print(json.dumps({'case':name,'status':record['status'],'native_abort':record['native_abort']}))
path=OUT/'d108_remainder_stage8_translated.json';logpath=OUT/'d108_remainder_stage8_translated.out'
if path.exists() and logpath.exists():
    log=logpath.read_text();requested=re.search(r'Unable to allocate memory \((\d+)\)',log)
    if requested:
        record=json.loads(path.read_text());record['verdict']='MEMORY_BOUND_OPEN'
        record['post_failure_audit']={'type':'CAS_AFTER_FAILURE_REJECTED','requested_allocation_bytes':int(requested.group(1)),
          'failure_location':'first characteristic product RR*H^2','accepted_characteristic_row_count':None,
          'restart_consequence':'Qrow undefined; subsequent BEGIN_GB ran an incomplete ideal and cannot support any mathematical verdict',
          'termination':'owned Singular process terminated after discovering invalid restart; source runner collected its exit',
          'log_sha256':hashlib.sha256(log.encode()).hexdigest()}
        path.write_text(json.dumps(record,indent=2,default=str)+'\n');print(json.dumps(record['post_failure_audit']))
