"""Tiny root replay of sealed actual engine output; no CAS/production parse."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import runpy
import signal
import sys
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25,25))
signal.alarm(30)
HERE=Path(__file__).resolve().parent
EV=HERE/'evidence'
sys.path.insert(0,str(EV))
import exact as E
import driver as D
M=json.loads((HERE/'remote-custody.json').read_bytes())
for name,item in M['files'].items():
    data=(EV/name).read_bytes()
    E.need(E.digest(data)==item['sha256'] and len(data)==item['bytes'],'download mismatch '+name)
for filename in ('driver.py','exact.py'):
    E.need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((EV/filename).read_text()))),'assertion')
stdout=(EV/'control.stdout').read_bytes()
control=D.check_control(stdout,(EV/'control.stderr').read_bytes())
E.need(control['original_rows']==control['engine_columns']==control['cofactor_rows']==6,'index columns')
E.need(control['engine_to_original']==[0,1,0,1,4,0],'duplicate mapping')
for mutated in (stdout.replace(b'T 4 1\n',b'T 4 2\n'),stdout.replace(b'I 6 0\n',b'')):
    E.need(mutated!=stdout,'unchanged mutation')
    try:D.check_control(mutated,b'')
    except ValueError:pass
    else:raise RuntimeError('actual corrupted control accepted')
# Read-only import of frozen engineering constants; main/host/engine never run.
env=runpy.run_path(str(EV/'engineering/engineering.py'),run_name='root_import_constants')
text=(EV/'engineering/long.stdout').read_text()
E.need(not (EV/'engineering/long.stderr').read_bytes(),'long stderr')
prefix='LONG_BEGIN\n';middle='\nLONG_END\nRATIONAL_BEGIN\n';end='\nRATIONAL_END\n'
E.need(text.startswith(prefix) and text.endswith(end) and text.count(middle)==1,'long framing')
actual,rational=text[len(prefix):-len(end)].split(middle)
E.need(E.polynomial(actual,env['VARS'])==E.polynomial('+'.join(env['TERMS']),env['VARS']),'long exact equality')
E.need(E.polynomial(rational,env['VARS'])==E.polynomial(env['RATIONAL'],env['VARS']),'rational exact equality')
E.need(M['all_groups_absent'] and all(not g for g in M['groups'].values()),'custody group absence')
for stem,selected in [('stdout-limit','stdout'),('stderr-limit','stderr')]:
    t=E.strict_json((EV/('engineering/'+stem+'.telemetry.json')).read_bytes())
    E.need(t['status']=='SIGNAL' and t['child_signal']==25,'FSIZE signal')
    E.need((EV/('engineering/'+stem+'.'+selected)).stat().st_size==4096,'actual stream size')
t=E.strict_json((EV/'engineering/rss.telemetry.json').read_bytes())
E.need(t['status']=='RESOURCE_CAP' and t['resource']=='rss' and t['termination']['kill_sent']
       and t['termination']['cleanup_complete'],'descendant control')
print(json.dumps({'status':'PASS','optimized':not __debug__,'download_pins':len(M['files']),
                  'index':control,'long_terms':161,'actual_mutations_rejected':2},sort_keys=True))
