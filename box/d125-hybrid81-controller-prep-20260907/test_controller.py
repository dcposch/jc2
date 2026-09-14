"""Only pure/fully mocked tests; no valid authority, source or process dispatch."""
import ast,importlib.util,json,sys,uuid
from pathlib import Path
from unittest.mock import patch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));import controller as C
def need(x,msg):
 if not x:raise RuntimeError(msg)
def rejects(fn):
 try:fn()
 except (ValueError,AttributeError):return
 raise RuntimeError('changed object accepted')
boot='12345678-1234-4234-8234-123456789abc';base=['hybrid',boot,'a'*64,'b'*64,None,1010,1000]
C.validate(*base)
for i,value in [(0,'solver'),(1,'BOOT_PENDING'),(1,'00000000-0000-0000-0000-000000000000'),(2,'0'*64),(2,'PENDING'),(3,'z'*64),(4,'c'*64),(5,999),(5,1061)]:
 q=base.copy();q[i]=value;rejects(lambda:C.validate(*q))
q=base.copy();q[0]='alarm';rejects(lambda:C.validate(*q));q[4]='c'*64;C.validate(*q)
# Derive registered vector from frozen prose, independently of controller code.
reg=HERE.parent/'d125-hybrid81-parent-repair-20260907'/'REGISTRATION.md'
line=next(s for s in reg.read_text().splitlines() if s.startswith('/usr/bin/prlimit '))
expected=line.split();expected=expected[expected.index('--')+1:]
for op in ('hybrid','alarm'):
 v=[s.replace('OP',op).encode() for s in expected];C.compare_vector(op,v)
 need(len(v)==29,'registered vector length')
 for i in range(len(v)):
  changed=v.copy();changed[i]+=b'_CHANGED';rejects(lambda:C.compare_vector(op,changed))
rejects(lambda:C.vector('decision'))
# A syntactically plausible future command still stops on current cwd BEFORE
# hash reads, writes, imports of engine/driver or any process dispatch.
argv=['controller.py','hybrid','--boot',boot,'--green-sha256','a'*64,'--controller-sha256','b'*64,'--dispatch-before','1010']
with patch.object(sys,'argv',argv),patch.object(C.time,'time',return_value=1000),patch.object(C,'save',side_effect=RuntimeError('write occurred')),patch.object(C.subprocess,'Popen',side_effect=RuntimeError('dispatch occurred')),patch.object(C,'digest',side_effect=RuntimeError('hash read occurred')):
 rejects(C.main)
for p in (HERE/'controller.py',HERE/'test_controller.py'):
 need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert node')
print(json.dumps({'status':'PREP_ONLY_MOCK_PASS','operation_vectors':2,'scalar_rejections':10,'vector_mutations':58,'wrong_cwd_before_effects':True,'normal_optimized_same_checks':True}))
