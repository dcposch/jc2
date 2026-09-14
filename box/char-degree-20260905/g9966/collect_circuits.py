#!/usr/bin/env python3
"""Audit all 18 full coefficient-circuit executions without promoting OPEN."""
import hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    records=[]
    for stage in range(9):
        for branch in ('delta2','delta52'):
            case=HERE/'circuit-runs'/f'{branch}_stage{stage}'
            path=case/'augmented.circuit.json';inp=HERE/'circuit-inputs'/f'{branch}_stage{stage}.input.json'
            record={'branch':branch,'stage':stage,'status':'NOT_YET_EMITTED'}
            if path.exists():
                data=json.loads(path.read_text());script=case/'augmented.sing';log=case/'augmented.circuit.out'
                names=data.get('ring_generator_order',[]);text=log.read_text() if log.exists() else ''
                counts=data.get('counts',{})
                match=re.search(r'ALL_ROWS_PARSED\n(\d+)\nBEGIN_GB',text)
                expected=sum(counts.values()) if counts else None
                errors=[l for l in text.splitlines() if l.lstrip().startswith('?') or 'error occurred' in l]
                checks={'input_sha256':data['input_sha256']==sha(inp),
                    'script_sha256':script.exists() and data.get('script_sha256')==sha(script),
                    'unique_generators':len(names)==len(set(names)),
                    'all_five_targets':set('target_'+v for v in 'abcde')<=set(names),
                    'leader_and_inverse':{'leader55','Z55'}<=set(names),
                    'separation_and_inverse':({'rho','Zrho'} if branch=='delta2' else {'c','Zc'})<=set(names)}
                if match:checks['parsed_row_count_matches']=int(match[1])==expected
                assert all(checks.values()),(case,checks)
                status=data['status']
                if status in ('UNIT','NONUNIT_NOT_POINT'):
                    assert not errors and data['cas']['returncode']==0 and data['cas']['controls']==['0','1']
                    assert checks.get('parsed_row_count_matches') and data['cas']['script_unchanged']
                record.update(status=status,input_sha256=sha(inp),script_sha256=sha(script),
                    result_sha256=sha(path),ring_variables=len(names),row_counts=counts,total_rows=expected,
                    all_rows_parsed=bool(match),entered_GB='BEGIN_GB' in text,finished_GB='END_GB' in text,
                    validation=checks,parser_or_cas_errors=errors[:10],
                    log_sha256=sha(log) if log.exists() else None)
                record['scope']='complete coefficient ideal' if match and not errors else 'no mathematical decision from partial execution'
            records.append(record)
    result={'field':'Q','expected_cases':18,'cases':records,
        'all_emitted':all(r['status']!='NOT_YET_EMITTED' for r in records),
        'all_full_rows_parsed':all(r.get('all_rows_parsed') for r in records),
        'unit_cases':[f"{r['branch']}_stage{r['stage']}" for r in records if r['status']=='UNIT'],
        'proper_cases':[f"{r['branch']}_stage{r['stage']}" for r in records if r['status']=='NONUNIT_NOT_POINT']}
    (HERE/'circuit-summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},sort_keys=True))
if __name__=='__main__':main()
